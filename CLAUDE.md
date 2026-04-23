# Trivium Method Editorial

Arquivo principal de instruções do Claude para este repositório.

## Objetivo

Este projeto mantém uma plataforma editorial para produção de aulas da Educação Clássica Cristã Reformada.
O framework oficial vive em `trivium-method-editorial/`.

## Ordem de Leitura

1. Leia [AGENTS.md](/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/AGENTS.md).
2. Leia os módulos em `.claude/rules/`.
3. Use `.claude/commands/` para slash commands.
4. Use `.claude/skills/` para fluxos reutilizáveis.
5. Use `.claude/agents/` para personas especializadas.

## Regras Inegociáveis

- Responder sempre em português.
- Nunca inventar títulos de aula.
- Tratar `1 - Curriculo Macro` de cada ano como fonte absoluta dos títulos.
- Usar `trivium-method-editorial/knowledge-base/` como base de conhecimento.
- Usar `trivium-method-editorial/templates/padrao_final_aula.md` como golden template.
- Executar `trivium-method-editorial/scripts/sync_titles.py` quando houver divergência de títulos.
- Adotar commits convencionais, `feat:`, `fix:`, `content:`, `chore:`, `docs:`.

## Mapa da Pasta .claude

```text
.claude/
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

- `.claude/rules/project-context.md`
- `.claude/rules/editorial-pipeline.md`
- `.claude/rules/writing-quality.md`
- `.claude/rules/title-synchronization.md`
- `.claude/rules/repo-operations.md`

## Observação

`CLAUDE.local.md` é reservado para preferências pessoais e não deve ir para o Git.
