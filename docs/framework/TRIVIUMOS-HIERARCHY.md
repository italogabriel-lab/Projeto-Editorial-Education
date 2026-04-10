# TriviumOS Hierarchy

## Hierarquia estrutural

```text
TriviumOS
├── .triviumos-core/            -> governanca, registries, wrappers, workflows, checklists
├── triviumos/                  -> biblioteca editorial compartilhada
├── disciplines/                -> bases por disciplina
├── docs/                       -> arquitetura, ajustes, guias
└── observability layer         -> public/, src/sync.js, HTMLs e workflows GitHub
```

## Hierarquia de agentes

### 1. Core

- `orchestrator`
- `researcher`
- `writer`
- `standardizer`
- `reviewer`
- `publisher`

Responsabilidade:
fluxo editorial principal, do diagnóstico à publicação.

### 2. Enablement

- `copywriter`
- `design-thinking`
- `ui-designer`
- `devops`
- `image-generator`

Responsabilidade:
capacidades transversais que apoiam produção, UX, release e ativos visuais.

### 3. Analytics

- `performance-analytics`
- `vision-progress-engine`
- `vision-bottleneck-detector`
- `vision-github-analyzer`

Responsabilidade:
medir saúde operacional e alimentar a observabilidade.

### 4. Assessment

- `bimester-exam-builder`
- `bimester-review-builder`

Responsabilidade:
derivados avaliativos do conteúdo já produzido.

### 5. Legacy

- `capitalizer`
- `exam-builder`
- `image-link-extractor`
- `review-builder`

Responsabilidade:
compatibilidade e transição de fluxos antigos.

## Hierarquia operacional

```text
Constitution
  -> Core Config
    -> Registry
      -> Agent Wrapper
        -> Canonical Skill
          -> Workflow
            -> Template
              -> Knowledge Base
                -> Script / Automation
```

