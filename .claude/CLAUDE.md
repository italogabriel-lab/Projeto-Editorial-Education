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
- **Referência pedagógica canônica**: consultar `docs-estratégicos-funcionamento-framework/1-Projeto plataforma Editorial Bibline/Abordagem pedagógica por fase do Trivium e fundamentos de conceituação.md` antes de redigir ou validar qualquer definição.
- **Conceituação ontológica obrigatória**: toda definição deve responder "O que é?" com o verbo ser no presente. Proibido definir pela função ("Para que serve?", "O que faz?").
- **Webster 1828 obrigatório**: consultar webstersdictionary1828.com antes de propor qualquer definição. Hierarquia: (1) Webster 1828, (2) Breve Catecismo de Westminster, (3) fontes primárias, (4) enciclopédias clássicas.
- Manter a **perspectiva obrigatória de Belas Artes e artes visuais**: todo tema deve ser tratado pela observação de imagem, desenho, forma, linha, cor, textura, espaço, composição, obra de arte e beleza visual. Exemplos de natureza, casa, igreja, objetos ou histórias bíblicas devem servir à leitura visual, sem virar tema paralelo.
- No **1º ano**, cada aula deve funcionar como introdução à linguagem visual e aos elementos da arte, mostrando como a criança observa elementos visuais em imagens, desenhos, obras ou composições artísticas.
- Manter o Accordion do Definir com tema ou pergunta simples, `@link_png@`, MP3 com definição curta e explicação completa na mesma linha, separadas por espaço, e texto visual equivalente após `[MP3\]`. Aplicar a mesma linha única ao áudio do Narrar.
- Usar os enunciados fixos dos hábitos: em Definir, "Leia o fato e ouça o áudio clicando abaixo." antes do Accordion; em Recordar, "Ouça e repita o fato abaixo."; em Praticar, antes do Fill_In, "Complete o fato abaixo com a palavra correta.".
- No Recordar da revisão semanal `.4`, usar literalmente "Recorde o fato estudado durante a semana.".
- Tratar a **semana como unidade pedagógica**: definição curta única em `x.1`, `x.2` e `x.3`; termo principal compartilhado; música ou rima comum no Recordar. Só variam o parágrafo livre do Definir, a explicação do Accordion, as imagens e a Atividade Extra.
- **Narrar = espelho literal do Definir**: o bloco de áudio e o texto visual do `[+IMAGE_TEXT_ASIDE]` no Narrar são literalmente idênticos ao conteúdo do Definir daquela aula (definição curta + parágrafo livre). Antes de `[MP3\]`, texto plain (sem negrito). Após `[MP3\]`, texto com negritos progressivos, igual ao texto visual do Accordion. Nenhuma frase adicional é permitida.
- **Pergunta do Narrar**: uma única pergunta por aula, heading `Pergunta` (singular). Derivada diretamente do vocabulário do parágrafo livre. Formatos válidos: "O que [TERMO] [VERBO]?", "Como [TERMO] [VERBO]?", "Onde [TERMO] aparece?", "Para que [TERMO] [VERBO]?". A resposta aparece explicitamente no texto. Proibido: "O que você percebeu sobre...", perguntas abertas, reflexivas, abstratas ou inferenciais.
- Aplicar **Fill-In progressivo**: a frase do `[+FILL_IN]` é sempre a definição curta da semana. A lacuna (`_____`) fica na palavra-chave específica de cada aula. Em `x.1`, lacuna no termo central. Em `x.2`, lacuna na palavra-chave do desdobramento. Em `x.3`, lacuna na palavra-chave do contexto. Exemplo: `x.1` → `O _____ representa o começo de uma arte.` (ponto); `x.2` → `O ponto representa o _____ de uma arte.` (começo); `x.3` → `O ponto representa o começo de uma _____.` (arte).
- Aplicar **progressão por palavras-chave**: tema e definição de `x.1` geram as palavras-chave estruturantes da semana. Em `x.2` e `x.3`, o exemplo central, o Definir, o Perceber, o Praticar e o Narrar devem retomar palavras literais desse eixo, sem abrir tema paralelo.
- Aplicar **progressão de negritos no parágrafo livre**: em `x.1`, o parágrafo livre coloca em negrito somente o TERMO da semana. Em `x.2`, coloca em negrito o TERMO e a palavra-chave específica de `x.2` (a mesma resposta do fill-in). Em `x.3`, coloca em negrito o TERMO e a palavra-chave específica de `x.3`. O negrito da palavra-chave no parágrafo e a resposta do fill-in são sempre a mesma palavra. Exemplo (semana 3): `x.1` → 'Você observa **pontos** na arte'; `x.2` → 'Você aprende que o **ponto** pode ser o **começo** de um desenho'; `x.3` → 'Você usa o **ponto** na **arte** para marcar lugares'. O Accordion espelha o parágrafo: versão plain (sem negrito) no áudio; versão bold (com negrito) no texto visual após `[MP3\]`.
- **Parágrafo livre com uma frase única**: o parágrafo livre do Definir contém UMA Única frase direta e objetiva focada no conceito da aula. Nunca adicionar uma segunda frase do tipo "A criança aprende a...", "A criança percebe que...", "A criança cria..." ou qualquer variação — essas frases são genéricas, não acrescentam conteúdo e violam o padrão.
- **[+MULTIPLE] — pergunta específica por aula**: a pergunta é derivada do parágrafo livre daquela aula — nunca genérica, nunca igual entre x.1, x.2 e x.3. Formatos: "O que [TERMO] [VERBO]?", "Como [TERMO] [VERBO]?", "Onde [TERMO] aparece?", "Para que [TERMO] [VERBO]?", "Quando [TERMO] [VERBO]?", "Quais [ELEMENTOS]?". Resposta correta = frase-chave do parágrafo livre. Distrator = temático mas errado. 2 opções para o 1º ano. Proibido: "Qual é o significado de [TERMO]?" ou "O que estudamos nesta aula?" como pergunta fixa.
- **MULTIPLE_CHOICE em provas**: em toda prova CANVAS_QUIZ, a primeira linha não vazia depois de `MULTIPLE_CHOICE 10` é uma pergunta e deve terminar com `?`.
- **Revisão semanal `.4` — Praticar temático**: o bloco `## [QUIZ] Praticar` usa 1 `[+FILL_IN]` com a definição curta da semana e 3 `[+MULTIPLE]`, uma por aula `x.1`, `x.2` e `x.3`. As perguntas devem ser copiadas ou derivadas diretamente do `Praticar` das três aulas e tratar do tema, das palavras-chave e dos exemplos estudados. Proibido usar perguntas estruturais ou metapedagógicas como "Qual frase resume a semana?", "Qual frase resume melhor a semana?", "Qual aula apresentou o coração da semana?", "Como podemos praticar o tema da semana?", "Como o aluno deve praticar o tema?", "Qual foi o termo da semana?" e "O que a revisão da semana deve manter?".
- **Provas semanais `.5`**: gerar as questões a partir do `Praticar` das aulas `x.1`, `x.2` e `x.3`. Usar os `[+FILL_IN]` progressivos e as perguntas `[+MULTIPLE]` específicas como referência direta. As perguntas devem tratar do tema, das palavras-chave e dos exemplos da semana. Proibido usar perguntas estruturais ou metapedagógicas como "Qual frase resume melhor a semana?", "Qual foi o termo da semana?", "Qual aula apresentou o coração da semana?", "Relacione cada aula ao foco estudado nesta semana.", "Como o aluno deve praticar o tema?" e "O que a revisão da semana deve manter?".
- **Provas bimestrais `10.md`, `20.md`, `30.md`, `40.md`**: título obrigatório `# Prova`, nunca `# Provas` nem `# Prova bimestral`. O arquivo usa `[CANVAS_QUIZ]` e tem exatamente 10 questões de 10 pontos, separadas por 9 linhas `--`. A prova cobre todo o conteúdo das 8 semanas do bimestre: 1–8, 11–18, 21–28 ou 31–38. Usar as revisões bimestrais `9.md`, `19.md`, `29.md`, `39.md`, as revisões semanais `.4` e as provas semanais `.5` como fontes diretas. Padrão preferencial: 4 `[FILL_IN]` com definições semanais, 4 `[MULTIPLE_CHOICE]` com perguntas específicas de conteúdo visual, 1 `[MATCHING]` relacionando os 8 termos centrais às definições, e 1 `[TRUE_OR_FALSE]` com definição literal estudada. Proibido usar perguntas estruturais ou metapedagógicas como "Qual termo pertence ao bloco estudado?", "Como a prova deve avaliar o aluno?", "Título inventado", "Assunto fora do Macro", "Qual foi o termo do bimestre?" ou equivalentes.
- **Revisão bimestral**: arquivos `9.md`, `19.md`, `29.md` e `39.md` têm título `# Revisão`. Usam 8 blocos, um por semana, cada um com `## [nome da aula .1]`, parágrafo `Nesta semana estudamos que **...**`, `[+HEADING] Atividade` e `[+IMAGE_TEXT_ON]`. O quiz final tem 8 questões alternando 4 `[+FILL_IN]` e 4 `[+MULTIPLE]`, copiados das revisões `.4`.
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
