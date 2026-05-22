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
- Manter o Accordion do Definir com tema ou pergunta simples, `@link_png@`, MP3 com definição curta e explicação completa, e texto visual equivalente após `[MP3\]`.
- Tratar a **semana como unidade pedagógica**: definição curta única em `x.1`, `x.2` e `x.3`; termo principal compartilhado; música ou rima comum no Recordar. Só variam o parágrafo livre do Definir, a explicação do Accordion, as imagens, o texto do Narrar e a Atividade Extra.
- Registrar 1 termo único por semana no Currículo Macro (`# Semana N\n[TermoCentral] ✅`), não 3 termos distintos.
- Ao modificar um padrão operacional, atualizar `AGENTS.md`, `CLAUDE.md`, `CLAUDE.local.md`, `CODEX.md`, `README.md`, `.claude/`, `.codex/` e `trivium-method-editorial/`.
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

## Governança de Alinhamento

`.claude/` é o espelho operacional do Claude Code. Sempre que uma regra editorial mudar em `.claude/`, conferir e alinhar a regra equivalente em `.codex/` e na fonte oficial `trivium-method-editorial/`.

## Módulos Carregados

- `.claude/rules/project-context.md`
- `.claude/rules/editorial-pipeline.md`
- `.claude/rules/writing-quality.md`
- `.claude/rules/title-synchronization.md`
- `.claude/rules/repo-operations.md`

## Observação

`CLAUDE.local.md` é reservado para preferências pessoais e não deve ir para o Git.
