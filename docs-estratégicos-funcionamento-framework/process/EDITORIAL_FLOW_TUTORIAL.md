# Tutorial Completo do Fluxo Editorial - Bibline Academy

## 📋 Índice

1. [Visão Geral do Projeto](#visao-geral)
2. [Estrutura de Arquivos](#estrutura-arquivos)
3. [GitHub Actions Workflows](#github-actions)
4. [Agentes e Skills](#agentes-skills)
5. [Pipeline Editorial de 7 Etapas](#pipeline-7-etapas)
6. [Data Sync Processes](#data-sync)
7. [UI Pages e Funções](#ui-pages)
8. [Scripts de Automação](#scripts)
9. [Templates e Conhecimento](#templates)
10. [Como Navegar e Trabalhar](#como-trabalhar)

---

## 1. Visão Geral do Projeto {#visao-geral}

### O que é o Projeto Editorial Education?

O **Trivium Method** é um sistema completo de produção, gestão e publicação de conteúdo educacional para a Bibline Academy. Ele integra:

- **GitHub Projects** como Kanban para gestão de tarefas
- **20 Agentes de IA** especializados em diferentes etapas do fluxo editorial
- **Pipeline de 7 etapas** para produção de aulas
- **Dashboard em tempo real** para monitoramento de progresso
- **Deploy automático** para GitHub Pages e Vercel

### Arquitetura de Alto Nível

```
[GitHub Projects Kanban] ←→ [GitHub Actions Sync]
         ↓
   [public/data.json]
         ↓
[Dashboard Vision Board] ←→ [Vision Board Live Sync (5min)]
         ↓
   [GitHub Pages / Vercel]

[EDITORIAL PRODUCTION]
Orchestrator → Researcher → Writer → Standardizer → Reviewer → Copywriter → Publisher
     ↓
[7-Stage Pipeline]
     ↓
[Curriculum Repository]
```

### Principais Métricas
- **22 Agentes Ativos** (18 operacionais + 4 legacy)
- **7 Etapas no Pipeline** (Orquestração → Publicação)
- **21 Skills Registradas** (habilidades operacionais)
- **5 Categorias de Agentes** (Core, Specialized, Analytics, Bimester, Legacy)
- **~4,200 aulas** planejadas (5 disciplinas × 5 anos × ~168 aulas/ano)

---

## 2. Estrutura de Arquivos {#estrutura-arquivos}

### Root Level (Vision Board UI)

```
Projeto-Editorial-Education/
│
├── index.html                      # Landing page / Overview
├── metas.html                      # Metas do Currículo (tracking)
├── metas-disciplinas.html          # Metas por Disciplina + Year Health
├── videos.html                     # Pipeline de Vídeos
├── agent-command-center.html       # Centro de Comando dos Agentes (4665 linhas)
│
├── vercel.json                     # Configuração Vercel (static HTML)
├── .gitignore                      # node_modules, media, caches
├── README.md                       # Documentação do Framework
├── QUICK_REFERENCE.md              # URLs rápidas e comandos
├── requirements.txt                # Python dependencies
├── query.graphql                   # GraphQL query para sync
└── test-*.js                       # Scripts de teste
```

### public/ - Dados e Scripts do Dashboard

```
public/
├── data.json                       # Dados live do Kanban (auto-generated)
├── app.js                          # Lógica do dashboard principal
├── sidebar.js                      # Navegação sidebar
├── styles.css                      # Estilos globais
├── metas.js                        # Lógica da página Metas
├── metas-disciplinas.js            # Metas por disciplina + Year Health
└── videos.js                       # Lógica da página Videos
```

### src/ - Sync Engine

```
src/
└── sync.js                         # Core sync engine (GraphQL → data.json)
```

### .github/workflows/ - CI/CD

```
.github/workflows/
├── deploy-pages.yml                # Deploy para GitHub Pages (on push to main)
└── data-sync.yml                   # Vision Board Live Sync (cron 5min)
```

### trivium-method/ - Trivium Method (Canonical Reference)

```
trivium-method/
├── agents/skills/                  # 18 definições de skills de agentes
│   ├── orchestrator/
│   ├── researcher/
│   ├── writer/
│   ├── standardizer/
│   ├── reviewer/
│   ├── publisher/
│   └── ... (outros agentes)
├── workflows/                      # Definições de workflows
├── knowledge-base/                 # Base de conhecimento
└── templates/                      # Templates de conteúdo
```

### Projeto Bibline Academy/ - Editorial Vault

```
Projeto Bibline Academy/
├── .env                            # Variáveis de ambiente (tokens, secrets)
│
├── editorial-squad/                # Configuração da equipe editorial
│   ├── skills/                     # 20 skills de agentes ativos
│   ├── workflows/                  # Workflows operacionais
│   │   ├── produce_class.md        # Pipeline de 7 etapas
│   │   ├── publish.md              # Workflow de publicação Git
│   │   └── orchestrate.md          # Ativação do Orchestrator
│   ├── knowledge-base/             # Base de conhecimento ativa
│   │   ├── visao-geral-fluxo-editorial.md   # Mapa editorial master (572 linhas)
│   │   ├── doutrina-pedagogica.md           # Fundação teológica/filosófica
│   │   ├── guia-de-estilo.md                # Guia de estilo editorial
│   │   ├── rise-blocks-reference.md         # Referência blocos Rise 360
│   │   └── relatorio-vision-board-projeto.md
│   ├── templates/                  # Templates de aula
│   │   ├── padrao_final_aula.md             # Golden Template
│   │   ├── exemplo_aula_final.md            # Exemplo do Golden Template
│   │   ├── defining.md                      # Template "Definir"
│   │   ├── perceiving.md                    # Template "Perceber"
│   │   ├── remembering.md                   # Template "Recordar"
│   │   ├── practicing.md                    # Template "Praticar"
│   │   └── narrating.md                     # Template "Narrar"
│   ├── scripts/                    # Scripts de automação Python
│   │   ├── README.md                         # Catálogo de scripts
│   │   ├── sync_titles.py                    # MASTER: Sincroniza títulos
│   │   ├── align_titles.py                   # Alinha títulos em tickets
│   │   ├── align_review_titles.py            # Alinha referências de review
│   │   ├── fix_lesson_h1.py                  # Corrige headers H1
│   │   ├── fix_titles.py                     # Limpa sufixos cosméticos
│   │   ├── check_matriz.py                   # Audit: Matriz vs Macro
│   │   ├── generate_descriptions.py          # Regenera descrições em massa
│   │   └── ... (outros scripts)
│   ├── AGENTS-DOCUMENTATION.md     # Documentação central de agentes
│   └── DOCUMENTATION-PLAN.md       # Plano de documentação
│
├── setup-playbook/                 # Configuração de ambiente
│   ├── README.md                   # Overview de setup
│   ├── 01-deployment/vercel.md
│   ├── 02-integrations/
│   │   ├── ai-image-generation.md
│   │   ├── github-actions-sync.md
│   │   └── github-mcp.md
│   ├── 07-environment/env-setup.md
│   └── 08-agents/python-automation.md
│
├── .agent/                         # Configuração de agente de IA
│   ├── workflows/
│   │   ├── create-lesson.md
│   │   ├── create-macro.md
│   │   ├── create-matriz.md
│   │   ├── create-vision.md
│   │   ├── full-pipeline.md
│   │   └── publish.md
│   └── knowledge-base/
│
└── Belas Artes - Fase da Gramática/  # Conteúdo curricular
    └── 1 Fase - Gramática/
        ├── 1º Ano - ARTE CRISTÃ PRIMITIVA E ÍCONES BIZANTINOS/
        ├── 2º Ano - DA CRIAÇÃO ATÉ A ARTE BIZANTINA/
        ├── 3º Ano - RENASCIMENTO E REFORMA/
        ├── 4º Ano - BARROCO ATÉ O NEOCLASSICISMO/
        └── 5º Ano - MANEIRISMO ATÉ O REALISMO AMERICANO/
            └── Estrutura Curricular/
                ├── 0 - Movimentos Artisticos trabalhados.md
                ├── 1 - Curriculo Macro - *.md         # FONTE DA VERDADE para títulos
                ├── 2 - Matriz-Curricular-objetivos - *.md
                ├── 3 - Visão e Plano pedagogico - *.md
                ├── 4 - Links-para-imagens-perceber - *.md
                ├── 5 - Prompts-para-imagens-narrar - *.md
                └── 6 - Descricoes para tickets.md
```

---

## 3. GitHub Actions Workflows {#github-actions}

### Workflow 1: Deploy to GitHub Pages

**Arquivo**: `.github/workflows/deploy-pages.yml`

**Triggers**:
- Push para branch `main` (paths: `*.html`, `public/**`)
- Manual (`workflow_dispatch`)

**Jobs**:
1. **Build**:
   - Valida arquivos HTML/JS
   - Gera relatório de deploy
2. **Deploy**:
   - Upload para GitHub Pages via `actions/upload-pages-artifact@v3`
   - Deploy via `actions/deploy-pages@v4`

**Output URL**: `https://italogabriel-lab.github.io/Projeto-Editorial-Education/`

**Concurrency**: Grupo `github-pages-deploy`, cancela execuções anteriores

---

### Workflow 2: Vision Board Live Sync

**Arquivo**: `.github/workflows/data-sync.yml`

**Triggers**:
- Cron a cada 5 minutos (`*/5 * * * *`)
- Manual (`workflow_dispatch`)

**Token**: `VISIONBOARDBIBLINE` (PAT para usuário `Italo-bibline`, scopes: repo + project)

**Project ID**: `PVT_kwDODLv1ac4BH1XW` ("Bibline Aulas" na org `bibline`)

**Jobs**:
1. **Checkout**: Clone shallow (`fetch-depth: 1`)
2. **Sync**: Executa `node src/sync.js`
   - Query GitHub Projects via GraphQL
   - Extrai todos os items com paginação
   - Parse subject/year de títulos
   - Calcula lead time
3. **Verify**: Verifica se `public/data.json` foi criado com `total_items`
4. **Commit & Push**: Commit atômico apenas se dados mudaram
   - Mensagem: `data: sync Kanban - N items (auto-sync)`

**SLA**:
- Execução: ~2-3 minutos
- Deploy: ~30 segundos
- Total: ~3-4 minutos

---

## 4. Agentes e Skills {#agentes-skills}

### Core Pipeline Agents (7-stage flow)

| Agente | Stage | Papel | Localização |
|--------|-------|-------|-------------|
| **Orchestrator** | Transversal | Diretor editorial — diagnostica, prioriza, delega | `editorial-squad/skills/orchestrator/SKILL.md` |
| **Researcher** | 1 | Pesquisa de conteúdo, Webster 1828, versos bíblicos, sourcing de arte | `editorial-squad/skills/researcher/SKILL.md` |
| **Writer** | 2 | Redação de aulas usando framework 5 Habits | `editorial-squad/skills/writer/SKILL.md` |
| **Standardizer** | 3 | Aplica formatação Rise Blocks, correções editoriais, capitalização europeia | `editorial-squad/skills/standardizer/SKILL.md` |
| **Reviewer** | 4 | Audit de 13 categorias, 10 erros conhecidos de IA, validação Golden Template | `editorial-squad/skills/reviewer/SKILL.md` |
| **Copywriter** | 5 | Polimento final — otimização de títulos, ritmo, clareza, cadência | `editorial-squad/skills/copywriter/SKILL.md` |
| **Publisher** | 7 | Salva localmente, marca termos no Macro, push para GitHub via MCP | `editorial-squad/skills/publisher/SKILL.md` |

### Specialized Agents

| Agente | Papel |
|--------|-------|
| **Design Thinking** | UX research, personas, wireframes, design pedagógico |
| **UI Designer** | Design systems, componentes responsivos, UI premium |
| **DevOps** | Guardião do repositório — enforce `.gitignore`, gestão Git, cleanup de emergência |
| **Capitalizer** | Capitalização em Português Europeu (Acordo Ortográfico 1990) — sub-step do Stage 3 |

### Analytics Agents (Vision Board)

| Agente | Papel |
|--------|-------|
| **Performance Analytics** | Análise de produtividade individual/equipe, comandos `/performance user/discipline/team` |
| **Vision Progress Engine** | Engine de tracking de progresso para dashboard Vision Board |
| **Vision Bottleneck Detector** | Identifica bottlenecks no pipeline de produção |
| **Vision GitHub Analyzer** | Análise de dados GitHub para saúde do projeto |

### Bimester Agents

| Agente | Papel |
|--------|-------|
| **Bimester Exam Builder** | Cria exams bimestrais CANVAS_QUIZ de 10 questões (semanas 10, 20, 30, 40) |
| **Bimester Review Builder** | Compila reviews bimestrais dos .4 semanais (semanas 9, 19, 29, 39) |

### Legacy Agents (deprecated, mantidos por referência)

| Agente | Substituído Por |
|--------|-----------------|
| **Exam Builder** | Bimester Exam Builder |
| **Review Builder** | Bimester Review Builder |
| **Image Link Extractor** | (Sem substituto direto) |
| **Image Generator** | Skill separada em `trivium-method/agents/skills/image-generator/` (usa Pollinations.ai, HuggingFace, DeepAI APIs) |

---

## 5. Pipeline Editorial de 7 Etapas {#pipeline-7-etapas}

### The 7-Stage Pipeline (`produce_class.md`)

```
1. PESQUISA (Researcher)
   Input: Tema + Plano Pedagógico
   Output: research_report.md
   Regras: Fontes primárias: Webster 1828, ARA/ARC, obras clássicas

2. REDAÇÃO (Writer)
   Input: Relatório de pesquisa
   Output: draft_class.md
   Regras: 5 Habits, voz ativa, imperativo, máx 30 palavras/frase

3. FORMATAÇÃO (Standardizer + Capitalizer)
   Input: Draft
   Output: formatted_class.md
   Regras: Rise Blocks, capitalização europeia, remover pontuação proibida

4. REVISÃO (Reviewer)
   Input: Aula formatada
   Output: reviewed_class.md ou rejeição
   Regras: Checklist 13 categorias, 10 erros de IA, validação Golden Template
   
   FEEDBACK LOOPS:
   - Erro de conteúdo → volta para Stage 2 (Writer)
   - Erro de formato → volta para Stage 3 (Standardizer)

5. POLIMENTO (Copywriter)
   Input: Aula aprovada
   Output: final_class.md
   Regras: Otimizar títulos, ritmo, clareza, cadência

6. REGISTRO (Automático/Manual)
   Input: Aula completa
   Output: Currículo Macro atualizado (mark checkboxes e termos)
   Regras: Deve executar quando uma semana completa (3 aulas) é finalizada

7. PUBLICAÇÃO (Publisher)
   Input: Aula final
   Output: Arquivo local + commit GitHub
   Regras: Salvar como X.Y.md, commit com mensagem padrão
```

### Estrutura Semanal

Cada semana produz 5 arquivos:
- `X.1.md` — Aula Dia 1
- `X.2.md` — Aula Dia 2
- `X.3.md` — Aula Dia 3
- `X.4.md` — Review Semanal (flashcards, matching, perguntas das 3 aulas)
- `X.5.md` — Quiz Semanal (CANVAS_QUIZ)

### Estrutura Bimestral (ciclos de 10 semanas)

- Semanas 1-8, 11-18, 21-28, 31-38: Conteúdo (8 semanas × 5 arquivos)
- Semanas 9, 19, 29, 39: Review Bimestral
- Semanas 10, 20, 30, 40: Exam Bimestral

---

## 6. Data Sync Processes {#data-sync}

### Sync 1: Vision Board Kanban Sync

**Arquivos**: `src/sync.js` + `.github/workflows/data-sync.yml`

**Frequência**: A cada 5 minutos (cron)

**Mecanismo**: GitHub GraphQL API consulta ProjectV2 (`PVT_kwDODLv1ac4BH1XW`)

**Dados extraídos por item**:
- id, number, title, status, state, assignee, labels
- created_at, closed_at, lead_time_days

**Parse**: Extrai subject do prefixo `[Subject]` e year de `Ano N` no título

**Output**: `public/data.json` com `last_updated`, `total_items`, `items[]`

**Commit**: Apenas se dados mudaram (atomic diff check)

---

### Sync 2: Title Synchronization

**Arquivo**: `scripts/sync_titles.py`

**Fonte da Verdade**: Arquivo `1 - Curriculo Macro`

**Alvos**:
- Arquivo 2 (Matriz)
- Arquivo 3 (Visao)
- Arquivo 6 (Tickets)
- Headers H1 de todos os arquivos `.md` de aulas

**Execução**: DEVE ser executado após QUALQUER mudança nos títulos do Curriculo Macro

---

### Sync 3: Curriculum Synchronization

Quando aulas existentes são modificadas, 5 arquivos devem ser atualizados:
1. `1 - Curriculo Macro` (se H1 muda)
2. `2 - Matriz-Curricular-objetivos` (se abordagem pedagógica muda)
3. `3 - Visao e Plano pedagogico` (se tema ou progressão muda)
4. `4 - Links-para-imagens-perceber` (se seção Perceber muda)
5. Aula `X.4.md` Review (deve match com definições/atividades)

---

### Sync 4: GitHub Issue/Project Sync

**Scripts**: `create_issues.py`, `update_github_issues_to_year1.py`, `update_backlog_tickets.py`, `sync_issues_week13.py`

**Propósito**: Criar e gerenciar Issues do GitHub como cartões Kanban para o Vision Board

---

## 7. UI Pages e Funções {#ui-pages}

### Vision Board Dashboard (deployado via GitHub Pages + Vercel)

| Página | URL Path | Função |
|--------|----------|--------|
| **Home** | `/` | Landing page com overview do projeto |
| **Overview Geral** | `/index.html` | Dashboard principal mostrando todos os dados do Kanban de `data.json` |
| **Metas (Curriculo)** | `/metas.html` | Tracking de metas do currículo |
| **Metas (Disciplinas)** | `/metas-disciplinas.html` | Metas baseadas em disciplina com **Year Health Feature** (4 status levels: Completado, Saudavel, Atencao, Critico) |
| **Videos Pipeline** | `/videos.html` | Tracking de pipeline de produção de vídeos |
| **Agent Command Center** | `/agent-command-center.html` | UI premium de 4665 linhas mostrando todos os 20 agentes, workflow visualization, performance de equipe, status do pipeline |

---

## 8. Scripts de Automação {#scripts}

### Catálogo de Scripts (`editorial-squad/scripts/`)

| Script | Função |
|--------|--------|
| `sync_titles.py` | **MASTER**: Propaga títulos do Macro para todos os arquivos |
| `align_titles.py` | Sincroniza títulos em arquivo de tickets |
| `align_review_titles.py` | Sincroniza referências de review |
| `fix_lesson_h1.py` | Corrige headers H1 em arquivos de aula |
| `fix_titles.py` | Limpa sufixos cosméticos em títulos |
| `check_matriz.py` | Audit: compara Matriz vs Macro |
| `generate_descriptions.py` | Regenera descrições de tickets em massa (DESTRUTIVO) |
| `sync_issues_week13.py` | Sincroniza issues para semana 13 |
| `create_issues.py` | Cria issues no GitHub |
| `update_github_issues_to_year1.py` | Atualiza issues do Year 1 |
| `update_backlog_tickets.py` | Atualiza tickets do backlog |
| `update_year1_tickets.py` | Atualiza tickets do Year 1 |
| `update_tickets_fixed.py` | Atualiza tickets corrigidos |
| `build_year1_tickets.py` | Constrói base de tickets do Year 1 |
| `check_project_items.py` | Audit: confere itens do ProjectV2 do GitHub |
| `converters/convert_recordar.py` | Converte blocos de música para blocos de rima |
| `converters/convert_recordar_to_rhyme.py` | Audit: quais aulas precisam de conversão |
| `formatters/fix_accordion.py` | Corrige redundância de accordion no 4º ano |

---

## 9. Templates e Conhecimento {#templates}

### Templates de Aula (`editorial-squad/templates/`)

| Template | Uso |
|----------|-----|
| `padrao_final_aula.md` | **Golden Template** — esqueleto de aula final |
| `exemplo_aula_final.md` | Exemplo concreto do Golden Template |
| `defining.md` | Template do hábito "Definir" |
| `perceiving.md` | Template do hábito "Perceber" |
| `remembering.md` | Template do hábito "Recordar" |
| `practicing.md` | Template do hábito "Praticar" |
| `narrating.md` | Template do hábito "Narrar" |

### Base de Conhecimento (`editorial-squad/knowledge-base/`)

| Documento | Conteúdo |
|-----------|----------|
| `visao-geral-fluxo-editorial.md` | **Mapa editorial master** (572 linhas, documento mais importante) |
| `doutrina-pedagogica.md` | Fundação teológica/filosófica |
| `guia-de-estilo.md` | Guia de estilo (máx 30 palavras/frase, máx 70/parágrafo, pontuação proibida) |
| `rise-blocks-reference.md` | Dicionário de sintaxe de blocos Rise 360 (12 blocos) |
| `relatorio-vision-board-projeto.md` | Relatório do projeto Vision Board |

---

## 10. Como Navegar e Trabalhar {#como-trabalhar}

### Fluxo de Trabalho Diário

1. **Acesse o Dashboard**:
   - URL: `https://italogabriel-lab.github.io/Projeto-Editorial-Education/`
   - Verifique o status dos cards no Kanban
   - Monitore métricas de produtividade

2. **Verifique o Agent Command Center**:
   - URL: `https://italogabriel-lab.github.io/Projeto-Editorial-Education/agent-command-center.html`
   - Veja status de cada agente
   - Monitore o pipeline de produção
   - Identifique bottlenecks

3. **Use o Orchestrator para Diagnóstico**:
   - Analise o progresso geral
   - Identifique tarefas pendentes
   - Delegue para agentes especializados

4. **Execute o Pipeline de Produção**:
   ```
   Orchestrator → Researcher → Writer → Standardizer → Reviewer → Copywriter → Publisher
   ```

5. **Sincronize Títulos** (se necessário):
   ```bash
   cd "Projeto Bibline Academy/editorial-squad/scripts"
   python sync_titles.py
   ```

6. **Commit e Push**:
   ```bash
   git add -A
   git commit -m "feat: descrição da mudança"
   git push origin main
   ```

### Comandos Úteis

#### Verificar status do sync:
```bash
curl -s https://italogabriel-lab.github.io/Projeto-Editorial-Education/public/data.json | jq '.total_items'
```

#### Forçar re-sync manual:
- Acesse: GitHub → Actions → Vision Board Live Sync → Run workflow

#### Verificar status do deploy:
- Acesse: GitHub → Actions → Deploy to GitHub Pages

#### Testar GraphQL query:
```bash
node test-graphql.js
```

### Estrutura de Navegação Rápida

```
Dashboard Overview (index.html)
    ↓
Metas (metas.html) — Visão geral de metas por disciplina/ano
    ↓
Metas por Disciplina (metas-disciplinas.html) — Saúde das metas com Year Health
    ↓
Videos Pipeline (videos.html) — Tracking de produção de vídeos
    ↓
Agent Command Center (agent-command-center.html) — Centro de comando completo
```

### Links Importantes

- **Vision Board Live**: `https://italogabriel-lab.github.io/Projeto-Editorial-Education/`
- **GitHub Repo**: `https://github.com/italogabriel-lab/Projeto-Editorial-Education`
- **Actions**: `https://github.com/italogabriel-lab/Projeto-Editorial-Education/actions`
- **Kanban Project**: `https://github.com/orgs/bibline/projects/2/views/1`

---

## 🎯 Resumo Visual do Fluxo Completo

```
[GitHub Projects Kanban] (bibline/org - Project V2)
         │
         │ GraphQL API (cron 5 min)
         ▼
[GitHub Actions: data-sync.yml] (node src/sync.js)
         │
         │ Gera public/data.json
         ▼
[Commit automático se mudou] (atomic diff check)
         │
         │ Push para main
         ▼
[GitHub Pages Deploy] (deploy-pages.yml)
         │
         │ Live URL:
         ▼
https://italogabriel-lab.github.io/Projeto-Editorial-Education/
         │
         ├─→ Overview Geral
         ├─→ Metas (Curriculo)
         ├─→ Metas (Disciplinas) + Year Health
         ├─→ Videos Pipeline
         └─→ Agent Command Center


[EDITORIAL CONTENT PRODUCTION]
         │
         │ Orchestrator diagnostica → delega para pipeline
         ▼
[1. Researcher] → [2. Writer] → [3. Standardizer+Capitalizer]
         │                                                    │
         ▼                                                    ▼
[Research Report]  [Draft Lesson]  [Formatted Lesson - Rise Blocks]
                                                        │
                                                        ▼
                                              [4. Reviewer] (audit 13 categorias)
                                                        │
                                             APROVADO? /  \ REJEITADO
                                                      ▼    ▼
                                    [5. Copywriter]  [Volta para 2 ou 3]
                                          │
                                          ▼
                                  [6. Registrar no Macro] (mark checkboxes + terms)
                                          │
                                          ▼
                                  [7. Publisher] (save local + GitHub commit via MCP)
                                          │
                                          ▼
                                  [Curriculum Repository: bibline/curriculum]
```

---

**Última Atualização**: Abril 2026  
**Versão do Tutorial**: 1.0  
**Status**: 🟢 Produção Ready
