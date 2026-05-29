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
- Manter o Accordion do Definir com tema ou pergunta simples, `@link_png@`, MP3 com definição curta e explicação completa, e texto visual equivalente após `[MP3\]`.
- Tratar a **semana como unidade pedagógica**: definição curta única em `x.1`, `x.2` e `x.3`; termo principal compartilhado; música ou rima comum no Recordar. Só variam o parágrafo livre do Definir, a explicação do Accordion, as imagens e a Atividade Extra.
- **Narrar = espelho literal do Definir**: o bloco de áudio e o texto visual do `[+IMAGE_TEXT_ASIDE]` no Narrar são literalmente idênticos ao conteúdo do Definir daquela aula (definição curta + parágrafo livre). Antes de `[MP3\]`, texto plain (sem negrito). Após `[MP3\]`, texto com negritos progressivos, igual ao texto visual do Accordion. Nenhuma frase adicional é permitida.
- **Pergunta do Narrar**: uma única pergunta por aula, heading `Pergunta` (singular). Derivada diretamente do vocabulário do parágrafo livre. Formatos válidos: "O que [TERMO] [VERBO]?", "Como [TERMO] [VERBO]?", "Onde [TERMO] aparece?", "Para que [TERMO] [VERBO]?". A resposta aparece explicitamente no texto. Proibido: "O que você percebeu sobre...", perguntas abertas, reflexivas, abstratas ou inferenciais.
- Aplicar **Fill-In progressivo**: a frase do `[+FILL_IN]` é sempre a definição curta da semana. A lacuna (`_____`) fica na palavra-chave específica de cada aula. Em `x.1`, lacuna no termo central. Em `x.2`, lacuna na palavra-chave do desdobramento. Em `x.3`, lacuna na palavra-chave do contexto. Exemplo: `x.1` → `O _____ representa o começo de uma arte.` (ponto); `x.2` → `O ponto representa o _____ de uma arte.` (começo); `x.3` → `O ponto representa o começo de uma _____.` (arte).
- Aplicar **progressão por palavras-chave**: tema e definição de `x.1` geram as palavras-chave estruturantes da semana. Em `x.2` e `x.3`, o exemplo central, o Definir, o Perceber, o Praticar e o Narrar devem retomar palavras literais desse eixo, sem abrir tema paralelo.
- Aplicar **progressão de negritos no parágrafo livre**: em `x.1`, o parágrafo livre coloca em negrito somente o TERMO da semana. Em `x.2`, coloca em negrito o TERMO e a palavra-chave específica de `x.2` (a mesma resposta do fill-in). Em `x.3`, coloca em negrito o TERMO e a palavra-chave específica de `x.3`. O negrito da palavra-chave no parágrafo e a resposta do fill-in são sempre a mesma palavra. Exemplo (semana 3): `x.1` → 'Você observa **pontos** na arte'; `x.2` → 'Você aprende que o **ponto** pode ser o **começo** de um desenho'; `x.3` → 'Você usa o **ponto** na **arte** para marcar lugares'. O Accordion espelha o parágrafo: versão plain (sem negrito) no áudio; versão bold (com negrito) no texto visual após `[MP3\]`.
- **Parágrafo livre = uma frase única**: o parágrafo livre do Definir contém UMA ÚNICA FRASE direta e objetiva focada no conceito da aula. Proibido adicionar segunda frase do tipo "A criança aprende a...", "A criança percebe que...", "A criança cria..." — são genéricas e não acrescentam conteúdo.
- **[+MULTIPLE] — pergunta específica por aula**: a pergunta é derivada do parágrafo livre daquela aula — nunca genérica, nunca igual entre x.1, x.2 e x.3. Formatos: "O que [TERMO] [VERBO]?", "Como [TERMO] [VERBO]?", "Onde [TERMO] aparece?", "Para que [TERMO] [VERBO]?", "Quando [TERMO] [VERBO]?", "Quais [ELEMENTOS]?". Resposta correta = frase-chave do parágrafo livre. Distrator = temático mas errado. 2 opções para o 1º ano. Proibido: "Qual é o significado de [TERMO]?" ou "O que estudamos nesta aula?" como pergunta fixa.
- Registrar 1 termo único por semana no Currículo Macro (`# Semana N\n[TermoCentral] ✅`), não 3 termos distintos.
- Ao modificar um padrão operacional, atualizar `AGENTS.md`, `CLAUDE.md`, `CLAUDE.local.md`, `CODEX.md`, `README.md`, `.claude/`, `.codex/` e `trivium-method-editorial/`.
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

## Governança de Alinhamento

`.codex/` é o espelho operacional do Codex. Sempre que uma regra editorial mudar em `.codex/`, conferir e alinhar a regra equivalente em `.claude/` e na fonte oficial `trivium-method-editorial/`.

## Módulos Carregados

- `.codex/rules/project-context.md`
- `.codex/rules/editorial-pipeline.md`
- `.codex/rules/writing-quality.md`
- `.codex/rules/title-synchronization.md`
- `.codex/rules/repo-operations.md`

## Observação

`CODEX.local.md` fica reservado para preferências pessoais e não deve ir para o Git.
