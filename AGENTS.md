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
- **Progressão por palavras-chave**: o tema e a definição de `x.1` geram as palavras-chave estruturantes da semana. As aulas `x.2` e `x.3` devem retomar palavras literais desse eixo no exemplo central, no Definir, no Perceber, no Praticar e no Narrar.
- Exemplo de progressão: se `x.1` define "O ponto representa o começo de uma arte", `x.1` apresenta o tema de forma abrangente, `x.2` trabalha `ponto` e `começo`, e `x.3` trabalha `ponto` e `arte`.
- Em `x.2` e `x.3`, só variam o parágrafo livre do Definir, a explicação do Accordion, as imagens e a Atividade Extra.
- **Narrar = espelho literal do Definir**: o bloco `[+IMAGE_TEXT_ASIDE]` do Narrar repete literalmente o conteúdo do Definir daquela aula — definição curta + parágrafo livre. Antes de `[MP3\]`, texto plain (sem negrito). Após `[MP3\]`, texto com negritos progressivos idênticos ao Accordion. Nenhuma frase adicional é permitida.
- **Pergunta do Narrar**: uma única pergunta por aula, heading `Pergunta` (singular). Derivada diretamente do vocabulário do parágrafo livre. Formatos válidos: "O que [TERMO] [VERBO]?", "Como [TERMO] [VERBO]?", "Onde [TERMO] aparece?", "Para que [TERMO] [VERBO]?". A resposta aparece explicitamente no texto do Narrar (definição + parágrafo livre). Proibido: "O que você percebeu sobre...", perguntas abertas, reflexivas, abstratas ou inferenciais.
- As variações de `x.2` e `x.3` não podem criar tema paralelo. Elas devem ser exemplos ou aplicações de palavras-chave já presentes no tema central de `x.1`.
- Bloco de termo no Currículo Macro: 1 termo central por semana (`# Semana N\n[TermoCentral] ✅`), não 3 termos distintos.
- Accordion do Definir: tema ou pergunta simples, `@link_png@`, MP3 e texto visual.
- MP3 do Accordion: narrar a definição curta e a explicação completa em texto narrável.
- Texto após `[MP3\]`: repetir o conteúdo do áudio, com negritos visuais permitidos.
- Definição curta: manter literalmente idêntica no cabeçalho do Definir, no Recordar, no Praticar e nas revisões — e entre as 3 aulas da mesma semana.
- **Fill-In progressivo**: a frase-base do `[+FILL_IN]` é sempre a definição curta da semana. A posição da lacuna (`_____`) muda em cada aula para cobrir a palavra-chave específica daquela aula. Em `x.1`, a lacuna fica no termo central da semana. Em `x.2`, a lacuna fica na palavra-chave do desdobramento. Em `x.3`, a lacuna fica na palavra-chave do contexto. Exemplo: "O ponto representa o começo de uma arte" → `x.1` `O _____ representa o começo de uma arte.` (ponto); `x.2` `O ponto representa o _____ de uma arte.` (começo); `x.3` `O ponto representa o começo de uma _____.` (arte).
- **Progressão de negritos no parágrafo livre**: em `x.1`, o parágrafo livre coloca em negrito somente o TERMO da semana. Em `x.2`, coloca em negrito o TERMO e a palavra-chave específica de `x.2` (a mesma resposta do fill-in). Em `x.3`, coloca em negrito o TERMO e a palavra-chave específica de `x.3`. O Accordion espelha o parágrafo: versão plain (sem negrito) no áudio; versão bold no texto visual após `[MP3\]`. Exemplo (semana 3): `x.1` → 'Você observa **pontos** na arte'; `x.2` → 'o **ponto** pode ser o **começo** de um desenho'; `x.3` → 'Você usa o **ponto** na **arte** para marcar lugares'.
- **Parágrafo livre com uma frase única**: o parágrafo livre é SEMPRE UMA ÚNICA FRASE direta e objetiva focada no conceito da aula. Proibido adicionar segunda frase do tipo "A criança aprende a...", "A criança percebe que..." ou similar — são genéricas e não acrescentam conteúdo.
- **[+MULTIPLE] — pergunta específica por aula**: a pergunta é derivada do parágrafo livre daquela aula — nunca genérica nem igual para x.1, x.2 e x.3. Formatos válidos: "O que [TERMO] [VERBO]?", "Como [TERMO] [VERBO]?", "Onde [TERMO] aparece?", "Para que [TERMO] [VERBO]?", "Quando [TERMO] [VERBO]?", "Quais [ELEMENTOS]?". Resposta correta = frase-chave do parágrafo livre. Distrator = temático mas conceitualmente errado. 2 opções para o 1º ano. Proibido: pergunta genérica fixa "Qual é o significado de [TERMO]?" ou "O que estudamos nesta aula?".
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
