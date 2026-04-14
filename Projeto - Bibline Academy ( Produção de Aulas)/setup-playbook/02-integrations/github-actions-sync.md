# 🔄 GitHub Actions CI/CD

## 🎯 Objetivo
Automatizar sincronização de dados do GitHub Projects (Kanban) para JSON estático com deploy automático via GitHub Pages.

---

## 📋 Pré-requisitos
- [ ] GitHub Personal Access Token (PAT) com escopos: `repo`, `read:org`, `read:project`
- [ ] GitHub Projects V2 habilitado na organização
- [ ] Node.js 20+ instalado
- [ ] GitHub Pages habilitado no repositório

---

## 🔧 Arquitetura do Fluxo

```
GitHub Projects (Kanban)
        ↓ (GraphQL API - cron */5)
GitHub Actions Workflow
        ↓ (node src/sync.js)
public/data.json
        ↓ (auto commit + push)
GitHub Pages
        ↓ (hosting)
Vision Board Dashboard
```

---

## 📁 Estrutura de Arquivos

### Workflow Principal
```
.github/workflows/
└── data-sync.yml
```

### Scripts de Sincronização
```
src/
├── sync.js              # Script principal de sync
└── utils/               # Utilitários (se houver)
```

### Output
```
public/
├── data.json            # Dados sincronizados
├── index.html           # Dashboard Vision Board
├── app.js               # Lógica do dashboard
├── metas.js             # Motor de metas
├── sidebar.js           # Navegação lateral
└── videos.js            # Player de vídeos
```

---

## 🔧 Passo a Passo

### Passo 1: Criar Personal Access Token

1. Acesse: https://github.com/settings/tokens
2. Clique em **"Generate new token (classic)"**
3. **Note:** `VisionBoard-Sync`
4. **Expiration:** 90 dias (recomendado)
5. **Scopes:**
   - ✅ `repo` (Full control of private repositories)
   - ✅ `read:org` (Read org membership)
   - ✅ `read:project` (Read projects data)
6. Clique em **"Generate token"**
7. **Copie o token** (não será mostrado novamente)

---

### Passo 2: Configurar Secret no GitHub

1. Acesse o repositório: `italogabriel-lab/Projeto-Editorial-Education`
2. Vá em **Settings → Secrets and variables → Actions**
3. Clique em **"New repository secret"**
4. Adicione:
   - **Name:** `VISIONBOARDBIBLINE`
   - **Value:** `ghp_your_token_here`
5. Clique em **"Add secret"**

---

### Passo 3: Criar Workflow (.github/workflows/data-sync.yml)

```yaml
name: Vision Board Live Sync

on:
  schedule:
    - cron: '*/5 * * * *'  # Every 5 minutes
  workflow_dispatch:       # Manual trigger

jobs:
  sync:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 1
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      
      - name: Sync Kanban Data
        env:
          GITHUB_TOKEN: ${{ secrets.VISIONBOARDBIBLINE }}
        run: |
          node src/sync.js
      
      - name: Verify data.json
        run: |
          if [ ! -f public/data.json ]; then
            echo "❌ data.json not created!"
            exit 1
          fi
      
      - name: Commit and Push if Changed
        run: |
          git config --global user.name 'github-actions[bot]'
          git config --global user.email 'github-actions[bot]@users.noreply.github.com'
          git add public/data.json
          if ! git diff --staged --quiet; then
            git commit -m "chore: auto-sync Kanban data $(date -u '+%Y-%m-%d %H:%M UTC')"
            git push
            echo "✅ Sync successful"
          else
            echo "✅ No changes to sync"
          fi
      
      - name: Summary
        run: |
          echo "## 📊 Sync Summary" >> $GITHUB_STEP_SUMMARY
          echo "- **Time:** $(date -u '+%Y-%m-%d %H:%M UTC')" >> $GITHUB_STEP_SUMMARY
          echo "- **Status:** ✅ Success" >> $GITHUB_STEP_SUMMARY
          jq '.total_items' public/data.json >> $GITHUB_STEP_SUMMARY
```

---

### Passo 4: Criar Script de Sync (src/sync.js)

```javascript
const https = require('https');

const GRAPHQL_ENDPOINT = 'https://api.github.com/graphql';
const TOKEN = process.env.GITHUB_TOKEN;

// Project ID: PVT_kwDODLv1ac4BH1XW (Bibline Aulas)
const PROJECT_ID = 'PVT_kwDODLv1ac4BH1XW';

const QUERY = `
query($projectId: ID!) {
  node(id: $projectId) {
    ... on ProjectV2 {
      items(first: 100) {
        nodes {
          id
          content {
            ... on Issue {
              number
              title
              state
              createdAt
              closedAt
              assignees(first: 1) {
                nodes {
                  login
                }
              }
              labels(first: 10) {
                nodes {
                  name
                }
              }
              repository {
                name
              }
            }
          }
          fieldValues(first: 20) {
            nodes {
              ... on ProjectV2ItemFieldSingleSelectValue {
                name
              }
              ... on ProjectV2ItemFieldIterationValue {
                title
              }
            }
          }
        }
      }
    }
  }
}
`;

async function graphql(query, variables = {}) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({ query, variables });
    
    const options = {
      hostname: GRAPHQL_ENDPOINT,
      port: 443,
      path: '/',
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${TOKEN}`,
        'Content-Type': 'application/json',
        'User-Agent': 'VisionBoard-Sync'
      }
    };
    
    const req = https.request(options, (res) => {
      let body = '';
      res.on('data', (chunk) => body += chunk);
      res.on('end', () => {
        if (res.statusCode === 200) {
          resolve(JSON.parse(body));
        } else {
          reject(new Error(`HTTP ${res.statusCode}: ${body}`));
        }
      });
    });
    
    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

function extractSubjectFromLabels(labels) {
  if (!labels || labels.length === 0) return 'Unknown';
  const subjectLabel = labels.find(l => 
    !l.name.includes('ano:') && !l.name.includes('status:')
  );
  return subjectLabel ? subjectLabel.name : 'Unknown';
}

function extractYearFromLabels(labels) {
  if (!labels || labels.length === 0) return 0;
  const yearLabel = labels.find(l => l.name.startsWith('ano:'));
  if (yearLabel) {
    return parseInt(yearLabel.name.replace('ano:', ''));
  }
  return 0;
}

function parseStatus(fieldValues) {
  const statusValue = fieldValues.nodes.find(
    node => node && node.name && ['Backlog', 'In Progress', 'In Review', 'Video', 'Block', 'Done/Published'].includes(node.name)
  );
  return statusValue ? statusValue.name : 'Backlog';
}

async function syncProjectData() {
  console.log('🔄 Starting sync...');
  
  try {
    const result = await graphql(QUERY, { projectId: PROJECT_ID });
    
    if (!result.data || !result.data.node) {
      throw new Error('Project not found');
    }
    
    const items = result.data.node.items.nodes;
    const processedItems = items.map(item => {
      const content = item.content;
      if (!content) return null;
      
      const status = parseStatus(item.fieldValues);
      const labels = content.labels?.nodes || [];
      
      return {
        id: item.id,
        number: content.number,
        title: content.title,
        status: status,
        state: content.state,
        assignee: content.assignees?.nodes[0]?.login || 'Unassigned',
        subject: extractSubjectFromLabels(labels),
        year: extractYearFromLabels(labels),
        created_at: content.createdAt,
        closed_at: content.closedAt,
        lead_time_days: content.closedAt 
          ? (new Date(content.closedAt) - new Date(content.createdAt)) / (1000 * 60 * 60 * 24)
          : null,
        labels: labels.map(l => l.name)
      };
    }).filter(item => item !== null);
    
    const output = {
      last_updated: new Date().toISOString(),
      total_items: processedItems.length,
      items: processedItems
    };
    
    const fs = require('fs');
    fs.writeFileSync('public/data.json', JSON.stringify(output, null, 2));
    
    console.log(`✅ Sync complete: ${processedItems.length} items`);
    
  } catch (error) {
    console.error('❌ Sync failed:', error.message);
    process.exit(1);
  }
}

syncProjectData();
```

---

### Passo 5: Habilitar GitHub Pages

1. Acesse: **Settings → Pages**
2. **Source:** Deploy from a branch
3. **Branch:** `main` / folder: `/ (root)`
4. Clique em **"Save"**

**URL de Acesso:**
```
https://italogabriel-lab.github.io/Projeto-Editorial-Education/
```

---

## ✅ Validação

### Testar Workflow Manualmente

1. Vá em **Actions → Vision Board Live Sync**
2. Clique em **"Run workflow"**
3. Selecione branch `main`
4. Clique em **"Run workflow"**
5. Aguarde ~2-3 minutos
6. Verifique:
   - ✅ Build succeeded
   - ✅ `public/data.json` criado
   - ✅ Commit automático no `main`

### Verificar Dados

```bash
# Localmente (após pull)
cat public/data.json | jq '.total_items'

# Deve retornar número > 0
```

### Acessar Dashboard

1. Acesse: https://italogabriel-lab.github.io/Projeto-Editorial-Education/
2. Verifique:
   - ✅ Cards de métricas carregados
   - ✅ Gráficos de status
   - ✅ Ranking de membros
   - ✅ Dados atualizados (últimos 5 min)

---

## 🔑 Variáveis de Ambiente

### GitHub Secrets

| Nome | Descrição | Exemplo |
|------|-----------|---------|
| `VISIONBOARDBIBLINE` | PAT Token para GitHub API | `ghp_xxxxxxxxxxxx` |

### Variáveis no Workflow

| Variável | Escopo | Descrição |
|----------|--------|-----------|
| `GITHUB_TOKEN` | Workflow | Token automático do GitHub Actions |
| `PROJECT_ID` | Hardcoded no script | ID do Projects V2 |

---

## 🔄 Cron Schedule

### Expressão: `*/5 * * * *`

| Campo | Valor | Significado |
|-------|-------|-------------|
| Minuto | `*/5` | A cada 5 minutos |
| Hora | `*` | Toda hora |
| Dia | `*` | Todo dia |
| Mês | `*` | Todo mês |
| Semana | `*` | Toda semana |

### SLA de Atualização

| Etapa | Tempo |
|-------|-------|
| Trigger (cron) | 0 min |
| Checkout + Setup | ~30 seg |
| GraphQL Fetch | ~1-2 min |
| Commit + Push | ~30 seg |
| GitHub Pages Deploy | ~30 seg |
| **Total** | **~3-4 minutos** |

---

## 📊 Estrutura do data.json

```json
{
  "last_updated": "2026-04-02T15:30:00.000Z",
  "total_items": 150,
  "items": [
    {
      "id": "PVTI_lADODLv1ac4BH1XWzgABC123",
      "number": 45,
      "title": "[Belas Artes] - Ano 3 - 13.1 Arte Bizantina",
      "status": "In Progress",
      "state": "open",
      "assignee": "joao-silva",
      "subject": "Belas Artes",
      "year": 3,
      "created_at": "2026-03-01T10:00:00.000Z",
      "closed_at": null,
      "lead_time_days": null,
      "labels": ["ano:3", "status:em-producao", "belas-artes"]
    }
  ]
}
```

---

## 🐛 Troubleshooting

| Problema | Solução |
|----------|---------|
| Workflow falha no GraphQL | Verifique token e escopos no GitHub Secrets |
| Project not found | Confirme PROJECT_ID (deve ser PVT_...) |
| Rate limit exceeded | Token tem limite de 5000 req/hora - reduza frequência |
| data.json não atualiza | Verifique permissões de write no repositório |
| GitHub Pages não atualiza | Pages deve estar configurado para / (root) |
| Status não mapeia | Verifique nomes exatos dos campos no Projects |

---

## 💡 Melhores Práticas

### Performance
- ✅ Use `fetch-depth: 1` para checkout rápido
- ✅ Limite a 100 items no GraphQL (pagination se necessário)
- ✅ Execute apenas em branches principais

### Segurança
- ✅ Nunca hardcode tokens no código
- ✅ Use secrets do GitHub Actions
- ✅ Rotacione tokens a cada 90 dias

### Monitoramento
- ✅ Adicione summary no workflow
- ✅ Configure alerts para falhas
- ✅ Monitore tempo de execução

---

## 🔗 Links Úteis
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [GitHub Projects GraphQL API](https://docs.github.com/en/graphql/guides/using-the-graphql-api-for-projects)
- [GitHub Pages](https://pages.github.com/)
- [Cron Schedule Syntax](https://crontab.guru/)

---

## 📝 Histórico de Configurações

| Data | Mudança | Responsável |
|------|---------|-------------|
| 2026-03-01 | Configuração inicial do Vision Board Sync | Editorial Squad |
| 2026-04-02 | Documentação no setup-playbook | Editorial Squad |

---

**Última atualização:** 2026-04-02  
**Status:** ✅ Documentado e em Produção
