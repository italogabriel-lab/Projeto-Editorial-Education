# Trivium Method Editorial

Framework de agentes especializados para produção de conteúdo didático cristão reformado.

## Estrutura

```
trivium-method-editorial/
├── agents/
│   └── skills/              # Skills especializadas
│       ├── orchestrator/    # Diretor editorial
│       ├── curriculum-macro-adapter/ # Adequação de grades curriculares
│       ├── researcher/      # Pesquisa (Etapa 1)
│       ├── writer/          # Redação (Etapa 2)
│       ├── standardizer/    # Rise Blocks (Etapa 3)
│       ├── reviewer/        # QA (Etapa 4)
│       ├── copywriter/      # Polimento (Etapa 5)
│       ├── publisher/       # Publicação (Etapa 6)
│       ├── devops/          # Git e GitHub
│       ├── capitalizer/     # Capitalização europeia
│       ├── bimester-exam-builder/
│       ├── bimester-review-builder/
│       ├── image-generator/
│       ├── design-thinking/
│       ├── ui-designer/
│       ├── vision-github-analyzer/
│       ├── vision-progress-engine/
│       ├── vision-bottleneck-detector/
│       └── performance-analytics/
├── knowledge-base/
│   ├── guia-de-estilo.md
│   ├── doutrina-pedagogica.md
│   ├── rise-blocks-reference.md
│   └── visao-geral-fluxo-editorial.md
├── templates/
│   ├── padrao_final_aula.md     # Golden template
│   ├── exemplo_aula_final.md
│   ├── defining.md
│   ├── narrating.md
│   ├── perceiving.md
│   ├── practicing.md
│   └── remembering.md
├── workflows/
│   ├── produce_class.md         # Pipeline de 7 etapas
│   ├── publish.md               # Push para GitHub
│   ├── full-pipeline.md
│   ├── create-lesson.md
│   ├── create-macro.md
│   ├── create-matriz.md
│   └── create-vision.md
└── scripts/
    ├── sync_titles.py           # Sincroniza títulos com Currículo Macro
    ├── align_titles.py
    ├── generate_descriptions.py
    ├── image-generation/        # Scripts de geração de imagem
    ├── converters/
    └── formatters/
```

## Uso com Claude Code

Todas as skills estão disponíveis como slash commands:

```
/orchestrator          # Diagnóstico e delegação
/curriculum-macro-adapter # Adequação de grade curricular
/researcher            # Pesquisa (Etapa 1)
/writer                # Redação (Etapa 2)
/standardizer          # Formatação Rise Blocks (Etapa 3)
/reviewer              # QA e revisão (Etapa 4)
/copywriter            # Polimento final (Etapa 5)
/publisher             # Publicação (Etapa 6)
/devops                # Operações Git
/capitalizer           # Capitalização
/bimester-exam-builder
/bimester-review-builder
/image-generator
/design-thinking
/ui-designer
/vision-github-analyzer
/vision-progress-engine
/vision-bottleneck-detector
/performance-analytics
```

## Padrão Atual do Accordion

No hábito Definir, o `[+ACCORDION]` deve conter tema ou pergunta simples, `@link_png@`, MP3 e texto visual.

O bloco `[MP3/]...[MP3\]` narra a definição curta e a explicação completa em texto narrável. O texto após `[MP3\]` repete o conteúdo do áudio, com negritos visuais permitidos. A definição curta permanece literalmente idêntica no cabeçalho do Definir, no Recordar, no Praticar e nas revisões.

## Alinhamento entre Camadas

Este diretório é a fonte oficial do framework. Sempre que um padrão operacional mudar, alinhe também `AGENTS.md`, `CLAUDE.md`, `CLAUDE.local.md`, `CODEX.md`, `README.md`, `.claude/` e `.codex/`.

## Base de Conhecimento

| Arquivo | Finalidade |
|---------|-----------|
| `knowledge-base/guia-de-estilo.md` | Tom, métricas e pontuação |
| `knowledge-base/doutrina-pedagogica.md` | Cosmovisão reformada e Trivium |
| `knowledge-base/rise-blocks-reference.md` | Markdown → Rise 360 Blocks |
| `knowledge-base/visao-geral-fluxo-editorial.md` | Visão geral do pipeline |
| `templates/padrao_final_aula.md` | Golden template de aula |
