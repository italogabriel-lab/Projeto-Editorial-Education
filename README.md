# Trivium Method Editorial

Framework de produção de conteúdo didático com agentes de IA especializados, projetado para equipes editoriais de Educação Clássica Cristã Reformada.

## O que é

O **Trivium Method Editorial** combina três camadas em um único repositório:

| Camada | O que faz |
|---|---|
| Framework de agentes | 21 skills especializadas espelhadas para Claude Code e Codex |
| Pipeline editorial | Fluxo de 7 etapas: pesquisa → redação → formatação → revisão → polimento → publicação |
| Dashboard de observabilidade | Painel web que consome o Kanban do GitHub Projects para monitorar metas e progresso |

O conteúdo segue os **5 Hábitos do Trivium** (Definir, Perceber, Recordar, Praticar, Narrar) e é formatado para publicação no Rise 360.

---

## Começar

### Pré-requisitos

- Node.js 18+
- Claude Code CLI configurado no repositório
- Git + GitHub CLI (`gh`)

### Instalação do scaffolder em novo projeto

```bash
npx create-trivium-method-editorial meu-projeto-editorial
```

O scaffolder gera a estrutura base com framework, templates e configuração dos agentes.

### Uso direto neste repositório

```bash
git clone <repo>
cd Projeto-Editorial-Education
npm install
```

---

## Framework de agentes (`trivium-method-editorial/`)

### Estrutura

```
trivium-method-editorial/
├── agents/skills/       Skills especializadas (fonte de verdade dos agentes)
├── knowledge-base/      Guia de estilo, doutrina pedagógica, referência Rise Blocks
├── templates/           Golden template + templates dos 5 hábitos
├── workflows/           produce_class, full-pipeline, publish e mais
└── scripts/
    ├── generation/      Gerador de aulas em massa (generate_lessons.py)
    ├── sync/            Sincronização de títulos (sync_titles.py e afins)
    ├── github/          Criação e atualização de issues e tickets
    ├── validation/      Auditoria curricular sem alterações
    ├── converters/      Conversão de formatos de blocos
    ├── formatters/      Correção de formatação Markdown
    ├── image-generation/ Geração de imagens via API
    └── examples/        Dados de exemplo (semana_exemplo.yaml)
```

### Pipeline de produção

```
/orchestrator → /researcher → /writer → /standardizer → /reviewer → /copywriter → /publisher
      0               1            2             3              4             5             6
  Diagnóstico     Pesquisa     Redação      Rise Blocks      QA         Polimento    Publicação
```

### Padrão da semana como unidade pedagógica

A unidade pedagógica é a semana inteira, não a aula isolada. Cada semana tem:

- 1 tema central, definido em `x.1`
- 1 definição curta única, literalmente idêntica em `x.1`, `x.2` e `x.3`
- 1 termo principal compartilhado pelas 3 aulas
- 1 música ou rima no Recordar, comum às 3 aulas

Entre `x.1`, `x.2` e `x.3` variam apenas o parágrafo livre do Definir, a explicação do Accordion, as imagens e a Atividade Extra. A revisão `.4` usa essa mesma definição única.

No Perceber da revisão `.4`, os textos de legenda dos hotspots no `[+IMAGE_LABELED]` são cópias literais dos textos das aulas `x.1`, `x.2` e `x.3`.

### Perspectiva de Belas Artes e artes visuais

Toda aula de Belas Artes deve tratar o tema pela observação dos elementos visuais da arte. Natureza, casa, igreja, objetos, histórias bíblicas e vida cotidiana podem entrar como exemplos, mas devem servir à leitura de imagem, desenho, forma, linha, cor, textura, espaço, composição, obra de arte e beleza visual.

No 1º ano, o foco é introduzir a linguagem visual e os elementos da arte. Cada aula deve mostrar como a criança observa um elemento visual em imagens, desenhos, obras ou composições artísticas.

### Conceituação clássica — regra inegociável

Toda definição produzida neste framework é **ontológica**: responde à pergunta "O que é?" usando o verbo ser no presente. Proibido definir pela função ("serve para", "faz", "permite").

- Definição correta: "A linha é o caminho que conduz o olhar por onde o desenho passa."
- Definição incorreta: "A linha serve para delimitar formas e organizar o espaço visual."

O **Webster's Dictionary of 1828** é o dicionário de referência obrigatório. Researcher e Writer devem consultá-lo antes de propor qualquer definição. Acesso: webstersdictionary1828.com.

Hierarquia de fontes: (1) Webster 1828, (2) Breve Catecismo de Westminster, (3) fontes primárias da disciplina, (4) enciclopédias clássicas e teológicas.

Referente canônico: `docs-estratégicos-funcionamento-framework/1-Projeto plataforma Editorial Bibline/Abordagem pedagógica por fase do Trivium e fundamentos de conceituação.md`.

### Padrão da progressão por palavras-chave

O tema e a definição de `x.1` geram as palavras-chave estruturantes da semana. As aulas `x.2` e `x.3` não abrem temas paralelos: retomam palavras do eixo de `x.1` no exemplo central, no Definir, no Perceber, no Praticar e no Narrar.

Exemplo com o tema "O ponto representa o começo de uma obra de arte": `x.1` coloca em negrito somente `pontos`. `x.2` coloca em negrito `ponto` e `começo`. `x.3` coloca em negrito `ponto` e `obra de arte`. O Fill-In de cada aula tem a lacuna na palavra em negrito daquela aula.

### Padrão das provas CANVAS_QUIZ

Em provas semanais `.5` e provas bimestrais `10.md`, `20.md`, `30.md` e `40.md`, todo bloco `MULTIPLE_CHOICE` deve ter enunciado com `?`.

As provas semanais `.5` devem usar o `Praticar` das aulas `x.1`, `x.2` e `x.3` como referência direta. Copie a lógica dos `[+FILL_IN]` progressivos e das perguntas `[+MULTIPLE]` específicas. Pergunte sobre o tema, as palavras-chave e os exemplos da semana. Não use perguntas estruturais como "Qual frase resume melhor a semana?", "Qual foi o termo da semana?", "Qual aula apresentou o coração da semana?", "Relacione cada aula ao foco estudado nesta semana.", "Como o aluno deve praticar o tema?" ou "O que a revisão da semana deve manter?".

```text
MULTIPLE_CHOICE 10

Como a linha nasce no desenho?

Quando um ponto caminha pelo papel. [=] true
Quando a imagem some do papel. [=]
Quando a folha fica vazia. [=]
```

### Padrão da revisão semanal

As revisões semanais `.4` usam uma única definição curta da semana. No `## [QUIZ] Praticar`, use 1 `[+FILL_IN]` com a definição curta e 3 `[+MULTIPLE]`, uma por aula `x.1`, `x.2` e `x.3`.

As perguntas devem ser copiadas ou derivadas diretamente do `Praticar` das três aulas. Pergunte sobre o tema, as palavras-chave e os exemplos estudados. Não use perguntas estruturais como "Qual frase resume a semana?", "Qual frase resume melhor a semana?", "Qual aula apresentou o coração da semana?", "Como podemos praticar o tema da semana?", "Como o aluno deve praticar o tema?", "Qual foi o termo da semana?" ou "O que a revisão da semana deve manter?".

### Padrão da revisão bimestral

As revisões bimestrais `9.md`, `19.md`, `29.md` e `39.md` têm 8 blocos semanais. Cada bloco usa o nome da aula `.1`, o parágrafo `Nesta semana estudamos que **...**`, o heading `Atividade` e um `[+IMAGE_TEXT_ON]` com `@link_png@`, `@link_mp3@` e o mesmo nome da aula `.1`.

O quiz final é `## [QUIZ] Questões` e contém exatamente 8 `[+FILL_IN]`, uma questão por semana, copiadas das revisões semanais `.4`.

### Comandos e skills disponíveis

Pipeline editorial:

| Comando | Etapa | Função |
|---|---|---|
| `/orchestrator` | 0 | Diagnostica o projeto e delega ao skill correto |
| `/researcher` | 1 | Pesquisa acadêmica e teológica (Ad Fontes) |
| `/writer` | 2 | Redação pelos 5 Hábitos da Gramática |
| `/standardizer` | 3 | Formatação Rise Blocks + capitalização europeia |
| `/reviewer` | 4 | QA: precisão doutrinária, estilo e conformidade |
| `/copywriter` | 5 | Polimento final de títulos e enunciados |
| `/publisher` | 6 | Salva a aula e publica no GitHub |

Skills de apoio:

| Comando | Função |
|---|---|
| `/curriculum-macro-adapter` | Adequa a grade curricular ao padrão do framework |
| `/review-builder` | Monta revisões semanais `x.4` a partir das aulas `x.1`, `x.2`, `x.3` |
| `/bimester-exam-builder` | Monta provas bimestrais com 10 questões CANVAS_QUIZ |
| `/bimester-review-builder` | Monta revisões bimestrais a partir das aulas `.4` |
| `/capitalizer` | Revisão de capitalização (padrão europeu / AO 1990) |
| `/image-generator` | Gera ilustrações aquarela via APIs de IA (Pollinations.ai) |
| `/devops` | Gestão de Git, GitHub e configurações |

Vision board:

| Comando | Função |
|---|---|
| `/vision-github-analyzer` | Extrai e modela dados brutos do GitHub Projects |
| `/vision-progress-engine` | Compara volume produzido com metas do calendário escolar |
| `/vision-bottleneck-detector` | Detecta gargalos operacionais e alertas de SLA |
| `/performance-analytics` | Relatórios de produtividade da equipe |

### Gerador de aulas em massa

```bash
# Gerar todas as aulas de uma semana (x.1, x.2, x.3, x.4)
python trivium-method-editorial/scripts/generation/generate_lessons.py dados_semana.yaml

# Gerar arquivo de dados de exemplo
python trivium-method-editorial/scripts/generation/generate_lessons.py --exemplo > dados_semana.yaml
```

---

## Dashboard de observabilidade

Painel web para acompanhamento de metas, disciplinas e progresso editorial.

```bash
# Desenvolvimento local
npx serve . -p 3000
# Acesse: http://localhost:3000
```

Páginas (em `src/`):

| Arquivo | Conteúdo |
|---|---|
| `src/index.html` | Kanban e visão geral do projeto |
| `src/metas.html` | Metas por ano escolar |
| `src/metas-disciplinas.html` | Progresso por disciplina |
| `src/videos.html` | Biblioteca de vídeos |
| `src/agent-command-center.html` | Central de controle dos agentes |

Deploy configurado para Vercel via `vercel.json`. As rotas `/metas.html`, `/videos.html` etc. continuam funcionando e redirecionam para os arquivos em `src/`.

---

## Conteúdo educacional (`Projeto - Bibline Academy/`)

```
Projeto - Bibline Academy ( Produção de Aulas)/
├── Belas Artes - Fase da Gramática/
│   ├── 0 Processos e Padrões do Novo Fluxo Editorial/
│   └── 1 Fase - Gramática/
│       └── 1º Ano - Introdução à Linguagem Visual/
│           ├── Estrutura Curricular - 1º ANO/   Currículo macro, matriz, visão, links de imagens, prompts Narrar
│           ├── 1.1.md … 38.4.md                 Aulas e revisões semanais
│           └── Templates Novos - 1º ANO/         Templates de aula e revisão
├── Base de Conhecimento/
└── setup-playbook/
```

---

## Estrutura do repositório

```
.
├── .claude/                   Configuração operacional do Claude Code
│   ├── rules/                 Regras editoriais (editorial-pipeline, writing-quality)
│   ├── commands/              Slash commands (/.claude/commands/*.md)
│   ├── skills/                Skills reutilizáveis (lesson-production, quality-gate)
│   └── agents/                Personas especializadas
│
├── .codex/                    Espelho operacional para Codex (mesma estrutura do .claude/)
│
├── trivium-method-editorial/  Framework de agentes (fonte canônica)
│
├── Projeto - Bibline Academy/ Conteúdo educacional produzido
│
├── src/                       Dashboard web + scaffolder
│   ├── index.html / metas.html / metas-disciplinas.html / videos.html
│   ├── agent-command-center.html
│   ├── assets/                Ícones e imagens do dashboard
│   ├── cli/                   CLI do scaffolder
│   ├── lib/                   Biblioteca do scaffolder
│   └── data/                  Dados gerados (graphql_fields.json, query.graphql)
│
├── public/                    JavaScript e CSS do dashboard (app.js, styles.css)
├── scaffold/                  Template instalado pelo npx create-trivium-method-editorial
├── bin/                       Entrypoint do CLI
├── tests/                     Testes do scaffolder
│
├── scripts/                   Automações do projeto
│   ├── generation/            Geradores de pipeline e artefatos
│   ├── publishing/            Publicação de aulas no GitHub
│   ├── diagnostics/           Diagnóstico do kanban
│   ├── quality/               Lint e typecheck
│   ├── tests/                 Testes de API e GraphQL
│   ├── validation/            Verificação de títulos
│   ├── hooks/                 Git hooks (pre-commit)
│   └── misc/                  Utilitários avulsos
│
└── docs/                      Documentação de segurança e arquitetura
```

---

## Qualidade

```bash
npm run lint            # Verificação de estilo
npm run typecheck       # Verificação de tipos
npm test                # Suite de testes
npm run build:artifacts # Gera artefatos do framework
```

---

## Convenções

- **Commits:** `feat:`, `fix:`, `content:`, `docs:`, `chore:`
- **Títulos de aula:** somente o que consta no `1 - Curriculo Macro` de cada ano (fonte oficial)
- **Sincronização de títulos:** `trivium-method-editorial/scripts/sync/sync_titles.py` ao detectar divergências
- **Legendas IMAGE_LABELED na revisão x.4:** cópia literal dos textos das aulas `x.1`, `x.2` e `x.3`
- **Idioma:** todas as interações com agentes em português
- **Conceituação ontológica:** toda definição responde "O que é?" com o verbo ser no presente. Proibido definir pela função.
- **Webster 1828:** dicionário de referência obrigatório para todos os termos. Consultar antes de propor qualquer definição (webstersdictionary1828.com).
- **Alinhamento documental:** ao alterar qualquer padrão operacional, atualizar `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, `README.md`, `.claude/`, `.codex/` e `trivium-method-editorial/`

---

## Licença

MIT — Italo Gabriel
