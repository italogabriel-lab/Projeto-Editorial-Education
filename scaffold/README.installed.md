# Trivium Method Editorial

Framework editorial inspirado na metodologia estrutural do AIOX.

## Estrutura

- `.trivium-method-editorial-core/`: governanca, registries, wrappers de agentes, workflows e scripts de diagnostico
- `trivium-method-editorial/`: biblioteca editorial canonica com agents, workflows, templates, knowledge base e automacoes
- `docs/`: arquitetura, hierarquia, ajustes e guias operacionais
- `disciplines/`: ponto de entrada para bases disciplinares da equipe
- `public/`, `src/`, `*.html`: camada atual de observabilidade herdada da operacao existente
- `public/data.json`: seed neutro de observabilidade ate o primeiro sync real

## Comandos

```bash
npm run trivium-method-editorial:inventory
npm run trivium-method-editorial:doctor
npm run trivium-method-editorial:sync
```

## Proximo passo

1. Configure os dados da sua disciplina em `disciplines/`
2. Revise `docs/framework/ADJUSTMENTS.md`
3. Ajuste variaveis e segredos antes de habilitar os workflows do GitHub
4. Rode o sync para substituir o seed inicial de `public/data.json`
