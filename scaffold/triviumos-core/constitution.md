# TriviumOS Constitution

> Version: 1.0.0

Este documento define os principios nao negociaveis do TriviumOS.

## I. CLI First

- MUST: toda automacao editorial deve funcionar via CLI ou script antes de depender de dashboard
- MUST: observabilidade apenas exibe, nao toma decisoes
- SHOULD: interfaces visuais permanecem desacopladas do motor editorial

## II. Agent Authority

- MUST: cada agente opera apenas em sua autoridade declarada
- MUST: revisao editorial final pertence ao `reviewer`
- MUST: automacoes de release e CI/CD pertencem ao `devops`
- SHOULD: o `orchestrator` roteia, mas nao substitui o trabalho especializado

## III. Workflow-Driven Production

- MUST: novas execucoes editoriais usam workflows definidos em `.triviumos-core/development/workflows/`
- MUST: templates canonicos saem de `triviumos/templates/templates/`
- MUST: a knowledge base compartilhada vive em `triviumos/knowledge-base/knowledge-base/`

## IV. Single Source of Truth

- MUST: o pacote instala a biblioteca editorial a partir de uma fonte unica catalogada no registry
- MUST: duplicacoes historicas ficam fora do fluxo de empacotamento
- SHOULD: toda disciplina herda o mesmo framework-base e customiza apenas `disciplines/`

## V. Quality Gates

- MUST: `npm run lint`
- MUST: `npm run typecheck`
- MUST: `npm test`
- MUST: registries e wrappers permanecerem sincronizados

