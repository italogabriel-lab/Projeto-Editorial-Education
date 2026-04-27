# Trivium Method Editorial

Arquivo principal de instruções do Codex para este repositório.

## Objetivo

Este projeto mantém uma plataforma editorial para produção de aulas da Educação Clássica Cristã Reformada.
O framework oficial vive em `trivium-method-editorial/`.

## Ordem de Leitura

1. Leia `AGENTS.md`.
2. Leia os módulos em `.codex/rules/`.
3. Use `.codex/commands/` para comandos e playbooks operacionais.
4. Use `.codex/skills/` para fluxos reutilizáveis.
5. Use `.codex/agents/` para personas especializadas.

## Regras Inegociáveis

- Responder sempre em português.
- Nunca inventar títulos de aula.
- Tratar `1 - Curriculo Macro` de cada ano como fonte absoluta dos títulos.
- Usar `trivium-method-editorial/knowledge-base/` como base de conhecimento.
- Usar `trivium-method-editorial/templates/padrao_final_aula.md` como golden template.
- Executar `trivium-method-editorial/scripts/sync_titles.py` quando houver divergência de títulos.
- Adotar commits convencionais, `feat:`, `fix:`, `content:`, `chore:`, `docs:`.

## Mapa da Pasta .codex

```text
.codex/
├── settings.json
├── settings.local.json
├── commands/
├── rules/
├── skills/
└── agents/
```

## Fonte de Verdade do Framework

- Skills reais, `trivium-method-editorial/agents/skills/`
- Knowledge base, `trivium-method-editorial/knowledge-base/`
- Workflows, `trivium-method-editorial/workflows/`
- Templates, `trivium-method-editorial/templates/`
- Scripts, `trivium-method-editorial/scripts/`

## Módulos Carregados

- `.codex/rules/project-context.md`
- `.codex/rules/editorial-pipeline.md`
- `.codex/rules/writing-quality.md`
- `.codex/rules/title-synchronization.md`
- `.codex/rules/repo-operations.md`

## Observação

`CODEX.local.md` fica reservado para preferências pessoais e não deve ir para o Git.
