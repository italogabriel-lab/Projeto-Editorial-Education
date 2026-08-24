# Trivium Method Editorial

Framework de agentes especializados para produção de conteúdo didático cristão reformado.

## Estrutura

```
trivium-method-editorial/
├── agents/
│   └── skills/              # Skills especializadas
│       ├── orchestrator/    # Diretor editorial
│       ├── curriculum-macro-adapter/ # Adequação de grades curriculares
│       ├── researcher/      # Pesquisa (Etapa 1)
│       ├── writer/          # Redação (Etapa 2)
│       ├── standardizer/    # Rise Blocks (Etapa 3)
│       ├── reviewer/        # QA (Etapa 4)
│       ├── copywriter/      # Polimento (Etapa 5)
│       ├── publisher/       # Publicação (Etapa 6)
│       ├── devops/          # Git e GitHub
│       ├── capitalizer/     # Capitalização europeia
│       ├── bimester-exam-builder/
│       ├── bimester-review-builder/
│       ├── image-generator/
│       ├── design-thinking/
│       ├── ui-designer/
│       ├── vision-github-analyzer/
│       ├── vision-progress-engine/
│       ├── vision-bottleneck-detector/
│       └── performance-analytics/
├── knowledge-base/
│   ├── guia-de-estilo.md
│   ├── doutrina-pedagogica.md
│   ├── rise-blocks-reference.md
│   └── visao-geral-fluxo-editorial.md
├── templates/
│   ├── padrao_final_aula.md     # Golden template
│   ├── exemplo_aula_final.md
│   ├── defining.md
│   ├── narrating.md
│   ├── perceiving.md
│   ├── practicing.md
│   └── remembering.md
├── workflows/
│   ├── produce_class.md         # Pipeline de 7 etapas
│   ├── publish.md               # Push para GitHub
│   ├── full-pipeline.md
│   ├── create-lesson.md
│   ├── create-macro.md
│   ├── create-matriz.md
│   └── create-vision.md
└── scripts/
    ├── sync_titles.py           # Sincroniza títulos com Currículo Macro
    ├── align_titles.py
    ├── generate_descriptions.py
    ├── image-generation/        # Scripts de geração de imagem
    ├── converters/
    └── formatters/
```

## Uso com Claude Code

Todas as skills estão disponíveis como slash commands:

```
/orchestrator          # Diagnóstico e delegação
/curriculum-macro-adapter # Adequação de grade curricular
/researcher            # Pesquisa (Etapa 1)
/writer                # Redação (Etapa 2)
/standardizer          # Formatação Rise Blocks (Etapa 3)
/reviewer              # QA e revisão (Etapa 4)
/copywriter            # Polimento final (Etapa 5)
/publisher             # Publicação (Etapa 6)
/devops                # Operações Git
/capitalizer           # Capitalização
/bimester-exam-builder
/bimester-review-builder
/image-generator
/design-thinking
/ui-designer
/vision-github-analyzer
/vision-progress-engine
/vision-bottleneck-detector
/performance-analytics
```

## Padrão Atual do Accordion

No hábito Definir, o `[+ACCORDION]` deve conter tema ou pergunta simples, `@link_png@`, MP3 e texto visual.

No 2º ano, o Definir usa um único `[+TABS]` no lugar de `[+ACCORDION]`, contendo título, `@link_png@`, definição, explicação, MP3, texto visual e conexão teológica, seguido diretamente de `[-TABS]`.

O bloco `[MP3/]...[MP3\]` narra a definição curta, a explicação completa da palavra-chave e a conexão teológica em texto narrável. O texto após `[MP3\]` repete o conteúdo do áudio, com negritos visuais permitidos. A definição curta permanece literalmente idêntica no cabeçalho do Definir, no Recordar, no Praticar e nas revisões.

O marcador de áudio de todas as aulas é a linha literal `#VOX:`, sem voice ID. Em aulas regulares com um único hotspot em `[+IMAGE_LABELED]`, usar a coordenada central `49 50`. Revisões `.4` podem usar vários hotspots com coordenadas próprias.

## Perspectiva de Belas Artes e Artes Visuais

Toda aula de Belas Artes deve tratar o tema pela observação dos elementos visuais da arte. Natureza, casa, igreja, objetos, histórias bíblicas e vida cotidiana podem entrar como exemplos, mas devem servir à leitura de imagem, desenho, forma, linha, cor, textura, espaço, composição, obra de arte e beleza visual.

No 1º ano, o foco é introduzir a linguagem visual e os elementos da arte. Cada aula deve mostrar como a criança observa um elemento visual em imagens, desenhos, obras ou composições artísticas.

## Padrão Atual da Progressão por Palavras-Chave

O tema e a definição curta de `x.1` geram as **palavras-chave estruturantes** da semana. As aulas `x.2` e `x.3` escolhem palavras desse eixo e as retomam no exemplo central, no Definir, no Perceber, no Praticar e no Narrar.

Exemplo, se `x.1` fixa "O ponto representa o começo de uma arte", `x.1` apresenta o tema de forma abrangente. `x.2` trabalha `ponto` e `começo`. `x.3` trabalha `ponto` e `arte`. A variação serve à repetição do vocabulário, sem criar tema paralelo.

## Conexão teológica semanal

No início do Definir, apresentar a definição curta, a explicação variável da palavra-chave e a conexão teológica ligada ao tema. A chamada "Veja o vídeo abaixo." deve ficar na mesma linha da conexão teológica. A conexão teológica é uma única formulação por semana e se repete literalmente nas aulas `x.1`, `x.2` e `x.3`.

O áudio do Accordion e do Narrar deve narrar os três trechos em uma única linha. O texto visual após `[MP3\]` e o bloco `[+IMAGE_TEXT_ASIDE]` repetem o mesmo conteúdo, com negritos permitidos apenas na definição e na explicação progressiva da palavra-chave.

## Padrão Atual da Revisão Bimestral

As revisões bimestrais `9.md`, `19.md`, `29.md` e `39.md` usam 8 blocos semanais. Cada bloco começa com `# [nome da aula .1]`, traz o parágrafo `Nesta semana estudamos que **...**`, o heading `Atividade` e um `[+IMAGE_TEXT_ON]` com `@link_png@`, `@link_mp3@` e o mesmo nome da aula `.1`.

O quiz final é `## [QUIZ] Questões` e contém exatamente 8 `[+FILL_IN]`, um por semana, copiados das revisões `.4`.

## Padrão Atual das Revisões Semanais

As revisões semanais `.4` usam uma única definição curta da semana. No `## [QUIZ] Praticar`, use 1 `[+FILL_IN]` com a definição curta e 3 `[+MULTIPLE]`, uma por aula `x.1`, `x.2` e `x.3`.

As perguntas devem ser copiadas ou derivadas diretamente do `Praticar` das três aulas. Pergunte sobre o tema, as palavras-chave e os exemplos estudados. Não use perguntas estruturais como "Qual frase resume a semana?", "Qual frase resume melhor a semana?", "Qual aula apresentou o coração da semana?", "Como podemos praticar o tema da semana?", "Como o aluno deve praticar o tema?", "Qual foi o termo da semana?" ou "O que a revisão da semana deve manter?".

## Padrão Atual das Provas Semanais

As provas semanais `.5` usam o `Praticar` das aulas `x.1`, `x.2` e `x.3` como referência direta. As questões retomam os `[+FILL_IN]` progressivos, as perguntas `[+MULTIPLE]` específicas, o tema, as palavras-chave e os exemplos da semana.

Não usar perguntas estruturais ou metapedagógicas sobre resumo da semana, termo da semana, coração da semana, foco da aula, modo genérico de praticar ou função da revisão. A prova deve perguntar sobre o conteúdo estudado, não sobre a arquitetura editorial da semana.

## Padrão Atual das Provas Bimestrais

As provas bimestrais `10.md`, `20.md`, `30.md` e `40.md` usam título obrigatório `# Prova`, nunca `# Provas` nem `# Prova bimestral`. O arquivo usa `[CANVAS_QUIZ]`, exatamente 10 questões de 10 pontos e 9 separadores `--`.

Cada prova cobre todo o conteúdo das 8 semanas do bimestre: 1–8, 11–18, 21–28 ou 31–38. Use a revisão bimestral, as revisões semanais `.4` e as provas semanais `.5` como fontes diretas. O padrão preferencial é 4 `FILL_IN`, 4 `MULTIPLE_CHOICE`, 1 `MATCHING` relacionando os 8 termos centrais às definições e 1 `TRUE_OR_FALSE` com definição literal estudada.

Perguntas estruturais ou metapedagógicas são proibidas. Não usar enunciados como "Qual termo pertence ao bloco estudado?", "Como a prova deve avaliar o aluno?", "Título inventado", "Assunto fora do Macro" ou "Qual foi o termo do bimestre?".

## Alinhamento entre Camadas

Este diretório é a fonte oficial do framework. Sempre que um padrão operacional mudar, alinhe também `AGENTS.md`, `CLAUDE.md`, `CLAUDE.local.md`, `CODEX.md`, `README.md`, `.claude/` e `.codex/`.

## Base de Conhecimento

| Arquivo | Finalidade |
|---------|-----------|
| `knowledge-base/guia-de-estilo.md` | Tom, métricas e pontuação |
| `knowledge-base/doutrina-pedagogica.md` | Cosmovisão reformada e Trivium |
| `knowledge-base/rise-blocks-reference.md` | Markdown → Rise 360 Blocks |
| `knowledge-base/visao-geral-fluxo-editorial.md` | Visão geral do pipeline |
| `templates/padrao_final_aula.md` | Golden template de aula |
