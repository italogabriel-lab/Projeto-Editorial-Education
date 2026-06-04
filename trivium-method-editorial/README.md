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

O bloco `[MP3/]...[MP3\]` narra a definição curta e a explicação completa em texto narrável. O texto após `[MP3\]` repete o conteúdo do áudio, com negritos visuais permitidos. A definição curta permanece literalmente idêntica no cabeçalho do Definir, no Recordar, no Praticar e nas revisões.

## Perspectiva de Belas Artes e Artes Visuais

Toda aula de Belas Artes deve tratar o tema pela observação dos elementos visuais da arte. Natureza, casa, igreja, objetos, histórias bíblicas e vida cotidiana podem entrar como exemplos, mas devem servir à leitura de imagem, desenho, forma, linha, cor, textura, espaço, composição, obra de arte e beleza visual.

No 1º ano, o foco é introduzir a linguagem visual e os elementos da arte. Cada aula deve mostrar como a criança observa um elemento visual em imagens, desenhos, obras ou composições artísticas.

## Padrão Atual da Progressão por Palavras-Chave

O tema e a definição curta de `x.1` geram as **palavras-chave estruturantes** da semana. As aulas `x.2` e `x.3` escolhem palavras desse eixo e as retomam no exemplo central, no Definir, no Perceber, no Praticar e no Narrar.

Exemplo, se `x.1` fixa "O ponto representa o começo de uma arte", `x.1` apresenta o tema de forma abrangente. `x.2` trabalha `ponto` e `começo`. `x.3` trabalha `ponto` e `arte`. A variação serve à repetição do vocabulário, sem criar tema paralelo.

## Padrão Atual da Revisão Bimestral

As revisões bimestrais `9.md`, `19.md`, `29.md` e `39.md` usam 8 blocos semanais. Cada bloco começa com `# [nome da aula .1]`, traz o parágrafo `Nesta semana estudamos que **...**`, o heading `Atividade` e um `[+IMAGE_TEXT_ON]` com `@link_png@`, `@link_mp3@` e o mesmo nome da aula `.1`.

O quiz final é `## [QUIZ] Questões` e contém exatamente 8 `[+FILL_IN]`, um por semana, copiados das revisões `.4`.

## Padrão Atual das Revisões Semanais

As revisões semanais `.4` usam uma única definição curta da semana. No `## [QUIZ] Praticar`, use 1 `[+FILL_IN]` com a definição curta e 3 `[+MULTIPLE]`, uma por aula `x.1`, `x.2` e `x.3`.

As perguntas devem ser copiadas ou derivadas diretamente do `Praticar` das três aulas. Pergunte sobre o tema, as palavras-chave e os exemplos estudados. Não use perguntas estruturais como "Qual frase resume a semana?", "Qual frase resume melhor a semana?", "Qual aula apresentou o coração da semana?", "Como podemos praticar o tema da semana?", "Como o aluno deve praticar o tema?", "Qual foi o termo da semana?" ou "O que a revisão da semana deve manter?".

## Padrão Atual das Provas Semanais

As provas semanais `.5` usam o `Praticar` das aulas `x.1`, `x.2` e `x.3` como referência direta. As questões retomam os `[+FILL_IN]` progressivos, as perguntas `[+MULTIPLE]` específicas, o tema, as palavras-chave e os exemplos da semana.

Não usar perguntas estruturais ou metapedagógicas sobre resumo da semana, termo da semana, coração da semana, foco da aula, modo genérico de praticar ou função da revisão. A prova deve perguntar sobre o conteúdo estudado, não sobre a arquitetura editorial da semana.

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
