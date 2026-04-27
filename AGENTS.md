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

## Estrutura Codex

Quando o agente em uso for o Codex, consultar também esta ordem:

1. `CODEX.md`
2. `.codex/rules/`
3. `.codex/commands/`
4. `.codex/skills/`
5. `.codex/agents/`

Objetivo, manter no Codex a mesma organização operacional já usada em `.claude/`.

## Qualidade de Escrita

- Voz ativa, imperativo nos enunciados
- Frases ≤ 30 palavras, parágrafos ≤ 70 palavras
- Sem `;`, `:`, `—` — usar `,` ou `.`
- Capitalização sentence-case (padrão europeu / Acordo Ortográfico 1990)
- Sem emojis no corpo do texto
