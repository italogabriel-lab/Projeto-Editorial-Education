# Trivium Method Editorial — Framework de Produção Educacional

Este projeto usa o **Trivium Method Editorial**, um framework de agentes especializados para produção de conteúdo didático cristão reformado. O framework vive em `trivium-method-editorial/`.

## Língua

Responda **sempre em português** em todas as interações.

## Framework: trivium-method-editorial/

```
trivium-method-editorial/
├── agents/skills/       # 21 skills especializadas (fonte de verdade)
├── knowledge-base/      # guia-de-estilo, doutrina-pedagogica, rise-blocks-reference
├── templates/           # padrao_final_aula.md e templates dos 5 hábitos
├── workflows/           # produce_class, publish, full-pipeline, etc.
├── scripts/             # sync_titles.py e utilitários de manutenção
│   ├── image-generation/
│   ├── diagnostics/
│   ├── converters/
│   └── formatters/
└── reports/performance/
```

## Pipeline Editorial (7 Etapas)

| Etapa | Skill | Invocação | Função |
|-------|-------|-----------|--------|
| 0 | `/orchestrator` | diagnóstico e delegação | Diretor editorial |
| 1 | `/researcher` | pesquisa de conteúdo | Investigador |
| 2 | `/writer` | redação da aula | Escriba |
| 3 | `/standardizer` | formatação Rise Blocks | Arquiteto |
| 4 | `/reviewer` | QA e revisão | Editor-Chefe |
| 5 | `/copywriter` | polimento final | Polidor |
| 6 | `/publisher` | salvar e publicar | Distribuidor |

## Skills de Apoio

| Skill | Função |
|-------|--------|
| `/devops` | Git, GitHub, .gitignore |
| `/capitalizer` | Capitalização padrão europeu |
| `/bimester-exam-builder` | Provas bimestrais (10 questões) |
| `/bimester-review-builder` | Revisões bimestrais (8 semanas) |
| `/image-generator` | Geração de imagens aquarela via IA |
| `/design-thinking` | UX, pesquisa, prototipagem |
| `/ui-designer` | Design system, componentes, responsividade |

## Skills Vision Board

| Skill | Função |
|-------|--------|
| `/vision-github-analyzer` | Extrai e modela dados do GitHub Projects |
| `/vision-progress-engine` | Meta vs. progresso por ano escolar |
| `/vision-bottleneck-detector` | Gargalos operacionais e SLA |
| `/performance-analytics` | Relatórios de produtividade |

## Convenções de Código

- Commits convencionais: `feat:`, `fix:`, `docs:`, `chore:`, `content:`
- Títulos de aula: **somente** o que consta no `1 - Curriculo Macro` (fonte oficial)
- Paths da knowledge-base: sempre relativos a `trivium-method-editorial/`
- Scripts de sincronização: `trivium-method-editorial/scripts/sync_titles.py`

## Estrutura do Projeto

```
Projeto Bibline Academy/
├── Belas Artes - Fase da Gramática/    # Conteúdo por ano (1º–5º)
├── Belas Artes - Fase da Lógica/       # 6º ano
├── Base de Conhecimento/               # Pesquisa e referências
├── Descrições e criação de tickets/
├── setup-playbook/                     # Guias de implantação
└── Excalidraw/

scripts/
├── diagnostics/    # diagnose_kanban.py e variantes
├── tests/          # test-graphql.js, test_project_access.py
└── validation/     # check_titles.py
```

## Regra de Títulos (CRÍTICA)

O arquivo `1 - Curriculo Macro` de cada ano é a **única fonte oficial** de títulos.
Sempre execute `trivium-method-editorial/scripts/sync_titles.py` ao detectar divergências.
