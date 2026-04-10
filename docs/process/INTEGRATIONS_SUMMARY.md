# 🎯 Integrações e Configurações do Projeto

> **Resumo Executivo de Todas as Integrações Implementadas**
> 
> Este documento fornece uma visão geral de alto nível de todas as integrações e configurações do Projeto Editorial Education. Use como referência rápida para entender o ecossistema técnico.

---

## 📊 Visão Geral do Ecossistema

```
┌─────────────────────────────────────────────────────────────────┐
│                  PROJETO EDITORIAL EDUCATION                     │
│                     (Bibline Academy)                            │
└─────────────────────────────────────────────────────────────────┘

📦 22 Agentes AI    |  🔄 7-Stage Workflow  |  📊 Vision Board
🐍 44+ Scripts      |  🎨 3 AI APIs         |  🚀 2 Deploy Platforms
📝 683+ Docs        |  ⏱️ Sync 5min        |  📁 5 Anos (1º-5º)
```

---

## 🗂️ Categorias de Integração

### 1. 🚀 Deploy & Hosting (2 plataformas)

| Plataforma | Propósito | Status |
|------------|-----------|--------|
| **Vercel** | Agent Command Center (dashboard) | ✅ Produção |
| **GitHub Pages** | Vision Board (métricas em tempo real) | ✅ Produção |

**Arquivos de Configuração:**
- `vercel.json` - Rotas e build Vercel
- `.github/workflows/data-sync.yml` - Auto-sync Vision Board

---

### 2. 🔌 GitHub Integrations (3 fluxos)

| Integração | Propósito | Frequência |
|------------|-----------|------------|
| **GitHub Projects V2** | Kanban de produção (Bibline Aulas) | Contínuo |
| **GitHub Actions** | Sync automático de dados | A cada 5 minutos |
| **GitHub MCP Server** | AI agents (Claude/Cursor) | Sob demanda |

**IDs de Projetos:**
- `PVT_kwDODLv1ac4BH1XW` - Bibline Aulas (Org: bibline)

**Secrets Necessárias:**
- `VISIONBOARDBIBLINE` - Token para Actions
- `GITHUB_MCP_TOKEN` - Token para MCP Server

---

### 3. 🎨 AI Image Generation (3 APIs)

| API | Tipo | Limite | Status |
|-----|------|--------|--------|
| **Pollinations.ai** | Primária (Flux model) | Ilimitado | ✅ Ativo |
| **HuggingFace** | Backup (SDXL) | 1000/day | ✅ Standby |
| **DeepAI** | Terciário | 500/day | ✅ Standby |

**Output:**
- Local: `generated/imagens-narrar/[ANO]-ano/semana-[N]/`
- Formato: `[X.Y]_narrar.png` + `[X.Y]_narrar_prompt.txt`

---

### 4. 🐍 Python Automation (44+ scripts)

#### Categorias:

| Categoria | Scripts | Função Principal |
|-----------|---------|------------------|
| **GitHub Integration** | 2 | Criar Issues, auditar Projects |
| **Sync** | 5 | Sincronizar títulos (Macro → todos) |
| **Curriculum** | 3 | Gestão de currículo, tickets |
| **Descriptions** | 1 | Gerar descrições de Issues |
| **Converters** | 2 | Converter blocos (Music → Rhyme) |
| **Formatters** | 1 | Corrigir formatação (Accordion) |
| **Image Generation** | 8 | Gerar imagens via API |
| **Utils** | 22+ | Diversos utilitários |

**Scripts Principais:**
- `sync_titles.py` - **MASTER SYNC** (Macro → Matriz, Visão, Tickets, Aulas)
- `create_issues.py` - Cria Issues em lote + adiciona ao Project
- `check_matriz.py` - Auditoria de consistência
- `check_project_items.py` - Lista itens do Projects por status

---

### 5. 🤖 AI Agents (22 agentes)

#### Estrutura:

```
trivium-method/agents/
├── skills/           (20 agentes)
│   ├── core/         (7 pipeline principal)
│   ├── specialized/  (5 suporte técnico)
│   ├── analytics/    (4 Vision Board)
│   ├── bimester/     (2 avaliação)
│   └── legacy/       (4 histórico)
└── skills/image-generator/ (1 image generator)
```

#### Agentes Core (Fluxo Principal):

| Nome Criativo | Original | Função |
|---------------|----------|--------|
| 🎼 Maestro | Orchestrator | Diretor editorial |
| 🔍 Seeker | Researcher | Pesquisa |
| ✒️ Scribe | Writer | Redação |
| 🏗️ Architect | Standardizer | Formatação Rise |
| 🛡️ Guardian | Reviewer | QA (13 categorias) |
| ✨ Polisher | Copywriter | Polimento final |
| 📢 Herald | Publisher | Publicação GitHub |

#### Agentes Especializados:

| Nome Criativo | Original | Função |
|---------------|----------|--------|
| 🤖 Sentinel | DevOps | Gatekeeper Git |
| 🧭 Navigator | Design Thinking | UX Research |
| 🎨 Artificer | UI Designer | Design System |
| 🖼️ Illustrator | Image Generator | IA de imagens |
| 🔤 Lexicon | Capitalizer | Capitalização |

#### Agentes Analytics (Vision Board):

| Nome Criativo | Original | Função |
|---------------|----------|--------|
| 📊 Strategist | Performance Analytics | Performance team |
| 🌾 Harvester | GitHub Analyzer | Extrai dados |
| 🔮 Oracle | Progress Engine | Meta vs progresso |
| 📡 Radar | Bottleneck Detector | Gargalos |

---

### 6. 📊 Vision Board (Dashboard de Métricas)

#### Arquitetura:

```
GitHub Projects (Kanban)
        ↓ (GraphQL API)
GitHub Actions (cron */5)
        ↓ (node src/sync.js)
public/data.json
        ↓ (auto-commit)
GitHub Pages
        ↓ (hosting)
Dashboard (italogabriel-lab.github.io)
```

#### Métricas em Tempo Real:

- **Produção Individual** - Tickets por autor
- **Performance por Disciplina** - Meta vs realizado
- **Status do Pipeline** - Backlog, In Progress, Review, Video, Done
- **Ritmo e Velocidade** - Lead time, throughput
- **Gargalos** - Alertas de SLA, quedas de performance

#### Arquivos:
- `src/sync.js` - Sync script (Node.js)
- `public/data.json` - Dados sincronizados
- `public/app.js` - Lógica do dashboard
- `public/metas.js` - Motor de metas

---

### 7. 📚 Workflows Editoriais (3 principais)

#### 1. produce_class.md (7 etapas)

```
1. PESQUISA    (Researcher/Seeker)
2. REDAÇÃO     (Writer/Scribe)
3. FORMATAÇÃO  (Standardizer/Architect + Capitalizer/Lexicon)
4. REVISÃO     (Reviewer/Guardian) - 13 categorias
5. POLIMENTO   (Copywriter/Polisher)
6. REGISTRO    (Manual/Auto)
7. PUBLICAÇÃO  (Publisher/Herald) - GitHub
```

#### 2. publish.md

- Versionamento Git
- Sync local → remote
- Limpeza estrutural (DevOps/Sentinel)

#### 3. orchestrate.md

- Diagnóstico de progresso
- Priorização inteligente
- Delegação ao agente correto

---

### 8. 🔐 Environment & Secrets

#### Variáveis Locais (.env):

```bash
# GitHub
GITHUB_TOKEN=ghp_xxxxx
GITHUB_MCP_TOKEN=ghp_xxxxx
GITHUB_OWNER=bibline
GITHUB_REPO=curriculum
GITHUB_PROJECT_ID=PVT_kwDODLv1ac4BH1XW

# Image Generation (opcional)
HUGGINGFACE_TOKEN=hf_xxxxx
DEEPAI_API_KEY=xxxxx

# Application
APP_NAME=Bibline Editorial Framework
APP_ENV=development/production
```

#### GitHub Secrets (Actions):

| Nome | Descrição |
|------|-----------|
| `VISIONBOARDBIBLINE` | PAT Token para GitHub Actions sync |

---

## 📁 Estrutura de Arquivos Chave

### Root do Projeto:
```
/
├── agent-command-center.html      # Dashboard de agentes (Vercel)
├── vercel.json                     # Config Vercel
├── .github/workflows/data-sync.yml # GitHub Actions
├── src/sync.js                     # Sync script Vision Board
├── public/                         # Vision Board dashboard
│   ├── data.json                   # Dados sincronizados
│   ├── index.html                  # Dashboard HTML
│   ├── app.js                      # Lógica principal
│   └── metas.js                    # Motor de metas
└── generated/imagens-narrar/       # Imagens geradas
    └── [ANO]-ano/semana-[N]/
```

### BEF Framework:
```
trivium-method/
├── agents/                         # 22 agentes AI
│   ├── skills/                     # 20 skills
│   │   ├── orchestrator/
│   │   ├── researcher/
│   │   ├── writer/
│   │   └── ...
│   └── specialized/
│       └── image-generator/
├── scripts/scripts/                # 44+ scripts Python
│   ├── github_integration/
│   ├── sync/
│   ├── curriculum/
│   └── ...
├── workflows/workflows/            # Definições de workflow
│   ├── produce_class.md
│   ├── publish.md
│   └── orchestrate.md
└── knowledge-base/knowledge-base/  # 683+ docs
    ├── visao-geral-fluxo-editorial.md
    ├── doutrina-pedagogica.md
    ├── guia-de-estilo.md
    └── ...
```

### Setup Playbook:
```
Projeto Bibline Academy/setup-playbook/
├── README.md                       # Hub central
├── 01-deployment/
│   └── vercel.md                   # Deploy Vercel
├── 02-integrations/
│   ├── github-mcp.md               # MCP Server
│   ├── github-actions-sync.md      # Actions pipeline
│   └── ai-image-generation.md      # APIs de imagem
├── 07-environment/
│   └── env-setup.md                # Environment variables
└── 08-agents/
    └── python-automation.md        # Scripts Python
```

---

## 🔄 Fluxos de Dados Principais

### 1. Vision Board Data Flow

```
GitHub Projects (Kanban V2)
    ↓ GraphQL API (a cada 5 min)
GitHub Actions (data-sync.yml)
    ↓ node src/sync.js
public/data.json (JSON estruturado)
    ↓ auto-commit + push
GitHub Pages (hosting estático)
    ↓
Dashboard Web (métricas em tempo real)
```

**Dados Extraídos:**
- Issues do Projects (100+ itens)
- Campos: status, assignee, labels, dates
- Cálculos: lead_time_days, percent_complete

---

### 2. Image Generation Flow

```
5 - Prompts-para-imagens-narrar-[ANO].md
    ↓ extract_prompts.py
Lista de prompts (JSON)
    ↓ optimize_prompt (traduz + keywords)
Prompt em inglês + style keywords
    ↓ Pollinations.ai API
Imagem PNG (1024x1024)
    ↓ organize_images.py
generated/imagens-narrar/[ANO]/semana-[N]/[X.Y]_narrar.png
    ↓ generate_log.py
LOG.md (status de produção)
```

---

### 3. Curriculum Sync Flow

```
1 - Curriculo Macro (fonte da verdade)
    ↓ sync_titles.py
2 - Matriz-Curricular-objetivos
3 - Visao e Plano pedagogico
6 - Descricoes para tickets
Todos arquivos de aula (.md H1)
    ↓ check_matriz.py (auditoria)
Relatório de consistência
```

**Regra de Ouro:**
> `1 - Curriculo Macro` é a **única fonte oficial** de títulos. Todos os outros arquivos devem refletir exatamente os mesmos títulos.

---

## 📊 Status de Produção

| Sistema | Status | SLA | Última Atualização |
|---------|--------|-----|-------------------|
| Vercel (Agent Command Center) | ✅ Online | 99.9% | 2026-04-02 |
| GitHub Pages (Vision Board) | ✅ Online | 99.9% | Auto-sync 5min |
| GitHub Actions Sync | ✅ Ativo | Every 5min | Contínuo |
| Image Generator | ✅ Ativo | On-demand | Sob demanda |
| Python Scripts | ✅ Ativo | On-demand | Sob demanda |
| AI Agents (22) | ✅ Documentados | On-demand | Sob demanda |

---

## 🔗 URLs de Acesso

### Produção:
- **Agent Command Center:** `https://projeto-editorial-education-[user].vercel.app`
- **Vision Board:** `https://italogabriel-lab.github.io/Projeto-Editorial-Education/`
- **GitHub Repo:** `https://github.com/italogabriel-lab/Projeto-Editorial-Education`

### Local:
- **Agent Command Center:** `file:///.../agent-command-center.html`
- **Vision Board:** `file:///.../public/index.html`

---

## 📚 Documentação

### Setup Playbook (Configurações):
- `setup-playbook/README.md` - Hub central
- `01-deployment/vercel.md` - Deploy Vercel
- `02-integrations/` - Todas as integrações
- `07-environment/env-setup.md` - Environment
- `08-agents/python-automation.md` - Scripts Python

### Agentes:
- `trivium-method/agents/skills/*/SKILL.md` - Definição de cada agente (20 files)
- `trivium-method/agents/skills/*/README.md` - Documentação de cada agente
- `editorial-squad/AGENTS-DOCUMENTATION.md` - Índice mestre

### Workflows:
- `trivium-method/workflows/workflows/produce_class.md` - Pipeline de 7 etapas
- `trivium-method/workflows/workflows/publish.md` - Workflow de publicação
- `trivium-method/workflows/workflows/orchestrate.md` - Workflow do Orchestrator

### Knowledge Base:
- `trivium-method/knowledge-base/knowledge-base/visao-geral-fluxo-editorial.md` - Visão geral (572 linhas)
- `trivium-method/knowledge-base/knowledge-base/doutrina-pedagogica.md` - Doutrina pedagógica
- `trivium-method/knowledge-base/knowledge-base/guia-de-estilo.md` - Guia de estilo
- `trivium-method/knowledge-base/knowledge-base/rise-blocks-reference.md` - Referência Rise Blocks

---

## 🎯 Próximos Passos (Backlog)

### Configurações Pendentes:
- [ ] Database PostgreSQL
- [ ] OAuth Authentication
- [ ] Sentry Error Tracking
- [ ] Email (Resend/SendGrid)
- [ ] Slack Notifications

### Melhorias:
- [ ] Exportar relatórios em PDF
- [ ] Integração com Slack
- [ ] Alertas automáticos de gargalo
- [ ] Métricas de qualidade (revisões, retrabalho)
- [ ] Dashboard interativo avançado

---

## 📞 Suporte e Referências

### Documentação Oficial:
- [Vercel Docs](https://vercel.com/docs)
- [GitHub Actions](https://docs.github.com/en/actions)
- [GitHub Projects GraphQL](https://docs.github.com/en/graphql/guides/using-the-graphql-api-for-projects)
- [Pollinations.ai](https://pollinations.ai/docs)
- [HuggingFace Inference API](https://huggingface.co/docs/api-inference)
- [MCP Protocol](https://modelcontextprotocol.io/)

### Contatos:
- **Repo:** `italogabriel-lab/Projeto-Editorial-Education`
- **Org:** `bibline`
- **Equipe:** Editorial Squad

---

**Versão:** 1.0  
**Última atualização:** 2026-04-02  
**Status:** ✅ Produção
