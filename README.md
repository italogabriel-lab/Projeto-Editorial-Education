# Trivium Method Editorial

Framework de produção de conteúdo didático com agentes de IA especializados, projetado para equipes editoriais de Educação Clássica Cristã Reformada.

## O que é

O **Trivium Method Editorial** combina três camadas em um único repositório:

| Camada | O que faz |
|--------|-----------|
| **Framework de agentes** | 21 skills especializadas ativadas como slash commands no Claude Code |
| **Pipeline editorial** | Fluxo de 7 etapas: pesquisa → redação → formatação → revisão → polimento → publicação |
| **Dashboard de observabilidade** | Painel web que consome o Kanban do GitHub Projects para monitorar metas e progresso |

O conteúdo produzido segue os **5 Hábitos do Trivium** (Definir, Perceber, Recordar, Praticar, Narrar) e é formatado para publicação no Rise 360.

---

## Começar

### Pré-requisitos

- Node.js 18+
- Claude Code CLI (com conta Anthropic)
- Git + GitHub CLI (`gh`)

### Instalação do scaffolder em novo projeto

```bash
npx create-trivium-method-editorial meu-projeto-editorial
```

O scaffolder gera a estrutura base com framework, templates e configuração do Claude Code.

### Uso direto neste repositório

```bash
git clone <repo>
cd Projeto-Editorial-Education
npm install
```

---

## Framework de Agentes (`trivium-method-editorial/`)

### Estrutura

```
trivium-method-editorial/
├── agents/skills/       # 21 skills especializadas (fonte de verdade)
├── knowledge-base/      # Guia de estilo, doutrina pedagógica, referência Rise Blocks
├── templates/           # Golden template + templates dos 5 hábitos
├── workflows/           # produce_class, full-pipeline, publish e mais
└── scripts/             # sync_titles.py, geradores e utilitários
```

### Pipeline de produção

```
/orchestrator → /researcher → /writer → /standardizer → /reviewer → /copywriter → /publisher
      0               1            2             3              4             5             6
  Diagnóstico     Pesquisa     Redação      Rise Blocks      QA         Polimento    Publicação
```

### Slash commands disponíveis no Claude Code

**Pipeline editorial:**

| Comando | Etapa | Função |
|---------|-------|--------|
| `/orchestrator` | 0 | Diagnostica o projeto e delega ao skill correto |
| `/researcher` | 1 | Pesquisa acadêmica e teológica (Ad Fontes) |
| `/writer` | 2 | Redação pelos 5 Hábitos da Gramática |
| `/standardizer` | 3 | Formatação Rise Blocks + capitalização europeia |
| `/reviewer` | 4 | QA: precisão doutrinária, estilo e conformidade |
| `/copywriter` | 5 | Polimento final de títulos e enunciados |
| `/publisher` | 6 | Salva a aula e publica no GitHub |

**Skills de apoio:**

| Comando | Função |
|---------|--------|
| `/devops` | Gestão de Git, GitHub e `.gitignore` |
| `/capitalizer` | Revisão de capitalização (padrão europeu / AO 1990) |
| `/bimester-exam-builder` | Monta provas bimestrais com 10 questões CANVAS_QUIZ |
| `/bimester-review-builder` | Monta revisões bimestrais a partir das aulas `.4` |
| `/image-generator` | Gera ilustrações aquarela via APIs de IA (Pollinations.ai) |
| `/design-thinking` | Pesquisa UX, personas, wireframes e prototipagem |
| `/ui-designer` | Design system, componentes responsivos e acessibilidade |

**Vision Board:**

| Comando | Função |
|---------|--------|
| `/vision-github-analyzer` | Extrai e modela dados brutos do GitHub Projects |
| `/vision-progress-engine` | Compara volume produzido com metas do calendário escolar |
| `/vision-bottleneck-detector` | Detecta gargalos operacionais e alertas de SLA |
| `/performance-analytics` | Relatórios de produtividade individual e da equipe |

### Como ativar um skill

```
/writer Semana 7, aula 7.2, 3º ano
/orchestrator
/bimester-exam-builder bimestre 2, 3º ano
```

---

## Dashboard de Observabilidade

Painel web para acompanhamento de metas, disciplinas e progresso editorial.

```bash
# Desenvolvimento local
npx serve . -p 3000
# Acesse: http://localhost:3000
```

**Páginas:**

| Arquivo | Conteúdo |
|---------|---------|
| `index.html` | Kanban e visão geral do projeto |
| `metas.html` | Metas por ano escolar |
| `metas-disciplinas.html` | Progresso por disciplina |
| `videos.html` | Biblioteca de vídeos |
| `agent-command-center.html` | Central de controle dos agentes |

**Deploy:** Configurado para Vercel via `vercel.json`.

---

## Estrutura do Repositório

```
.
├── .claude/
│   ├── CLAUDE.md              # Contexto do framework para o Claude Code
│   ├── settings.json          # Configuração de idioma
│   ├── settings.local.json    # Permissões de ferramentas
│   └── commands/              # 21 slash commands (/.claude/commands/*.md)
│
├── trivium-method-editorial/  # Framework de agentes (fonte de verdade)
│
├── Projeto Bibline Academy/   # Conteúdo educacional por ano e disciplina
│   ├── Belas Artes - Fase da Gramática/   # 1º ao 5º ano
│   ├── Belas Artes - Fase da Lógica/      # 6º ano
│   ├── Base de Conhecimento/
│   └── setup-playbook/
│
├── scripts/
│   ├── diagnostics/           # diagnose_kanban.py
│   ├── tests/                 # Testes de API e GraphQL
│   └── validation/            # check_titles.py
│
├── src/                       # Motor do scaffolder (lib/, cli/, data/)
├── scaffold/                  # Template instalado pelo npx create-trivium-method-editorial
├── public/                    # Assets do dashboard (JS, CSS)
├── docs/                      # Arquitetura, guias e roadmap
├── bin/                       # Entrypoint do CLI
└── tests/                     # Testes do scaffolder
```

---

## Qualidade

```bash
npm run lint        # Verificação de estilo
npm run typecheck   # Verificação de tipos
npm test            # Suite de testes
npm run build:artifacts  # Gera artefatos do framework
```

---

## Convenções

- **Commits:** `feat:`, `fix:`, `content:`, `docs:`, `chore:`
- **Títulos de aula:** somente o que consta no `1 - Curriculo Macro` (fonte oficial)
- **Sincronização:** `trivium-method-editorial/scripts/sync_titles.py` ao detectar divergências
- **Idioma:** todas as interações com agentes em português

---

## Licença

MIT — Italo Gabriel
