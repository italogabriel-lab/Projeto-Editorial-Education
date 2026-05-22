# AGENTS.md — Trivium Method Editorial

Instruções para agentes de IA que operam neste projeto.

## Identidade do Projeto

Plataforma de produção de conteúdo didático para Educação Clássica Cristã Reformada.
Framework: **Trivium Method Editorial** (`trivium-method-editorial/`).

## Língua

Responder **sempre em português** em todas as interações.

## Pipeline de Produção

As aulas seguem um pipeline de 7 etapas com agentes especializados:

1. **Orchestrator** — diagnóstico de progresso e delegação
2. **Researcher** — pesquisa acadêmica e teológica (Ad Fontes)
3. **Writer** — redação pelos 5 Hábitos da Gramática
4. **Standardizer** — formatação Rise Blocks + capitalização europeia
5. **Reviewer** — QA: precisão doutrinária, estilo, conformidade
6. **Copywriter** — polimento final de títulos e enunciados
7. **Publisher** — salvar aula e publicar no GitHub

## Regras Fundamentais

1. **Fonte de verdade dos títulos**: `1 - Curriculo Macro` de cada ano — nunca inventar títulos
2. **Base de conhecimento**: `trivium-method-editorial/knowledge-base/`
3. **Golden template**: `trivium-method-editorial/templates/padrao_final_aula.md`
4. **Sincronização de títulos**: executar `trivium-method-editorial/scripts/sync_titles.py` ao detectar divergências
5. **Commits**: convencionais (`feat:`, `fix:`, `content:`, `chore:`, `docs:`)

## Padrão Operacional Atual

- **Semana como unidade pedagógica**: cada semana tem 1 tema central (definido em `x.1`), 1 definição curta única literal nas 3 aulas, 1 termo principal compartilhado e 1 música ou rima comum no Recordar.
- Em `x.2` e `x.3`, só variam o parágrafo livre do Definir, a explicação do Accordion, as imagens, o texto do Narrar e a Atividade Extra.
- Bloco de termo no Currículo Macro: 1 termo central por semana (`# Semana N\n[TermoCentral] ✅`), não 3 termos distintos.
- Accordion do Definir: tema ou pergunta simples, `@link_png@`, MP3 e texto visual.
- MP3 do Accordion: narrar a definição curta e a explicação completa em texto narrável.
- Texto após `[MP3\]`: repetir o conteúdo do áudio, com negritos visuais permitidos.
- Definição curta: manter literalmente idêntica no cabeçalho do Definir, no Recordar, no Praticar e nas revisões — e entre as 3 aulas da mesma semana.
- Revisão semanal `.4`: usar uma única definição curta da semana, não três.

## Sincronização Documental Obrigatória

Sempre que um padrão novo de funcionamento for criado ou modificado, atualizar na mesma tarefa:

1. `AGENTS.md`
2. `CLAUDE.md`
3. `CLAUDE.local.md`
4. `CODEX.md`
5. `README.md`
6. `.claude/`
7. `.codex/`
8. `trivium-method-editorial/`

O objetivo é manter agentes, skills, comandos, templates, workflows, guias de estilo e documentação raiz refletindo o mesmo fluxo editorial.

## Estrutura Claude e Codex

Quando o agente em uso for Claude, consultar também esta ordem:

1. `CLAUDE.md`
2. `.claude/rules/`
3. `.claude/commands/`
4. `.claude/skills/`
5. `.claude/agents/`

Quando o agente em uso for Codex, consultar também esta ordem:

1. `CODEX.md`
2. `.codex/rules/`
3. `.codex/commands/`
4. `.codex/skills/`
5. `.codex/agents/`

Objetivo, manter Claude, Codex e `trivium-method-editorial/` alinhados como camadas do mesmo framework.

## Qualidade de Escrita

- Voz ativa, imperativo nos enunciados
- Frases ≤ 30 palavras, parágrafos ≤ 70 palavras
- Sem `;`, `:`, `—` — usar `,` ou `.`
- Capitalização sentence-case (padrão europeu / Acordo Ortográfico 1990)
- Sem emojis no corpo do texto
