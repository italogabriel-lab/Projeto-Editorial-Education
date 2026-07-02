---
name: Guia de Estilo Editorial
description: Regras de escrita, tom de voz, formatação e Rise Blocks para todas as aulas
---

# Guia de Estilo Editorial — Bibline Academy

## Tom de Voz

- **Virtuoso e elevado, porém acessível** para crianças de 7 a 11 anos (fase da Gramática).
- Didático sem ser infantilizado. Respeitoso sem ser inacessível.
- Use analogias ricas e referências a grandes autores ou obras de arte.
- Dirija-se ao aluno usando **"você"** ou **"seu"** para tom direto e pessoal.
- Proibido: linguagem excessivamente infantilizada, gírias modernas, ironia.
- Obrigatório: clareza na exposição e beleza na forma.
- Tom bíblico, robusto, respeitoso. Zero traços de passiva, gerúndio excessivo ou comandos indiretos.
- Em Belas Artes, mantenha sempre a perspectiva das artes visuais. Use exemplos de natureza, casa, igreja, objetos e histórias bíblicas para observar imagem, desenho, forma, linha, cor, textura, espaço, composição, obra de arte e beleza visual.
- No 1º ano, escreva como introdução à linguagem visual e aos elementos da arte.

## Regras de Escrita Obrigatórias

### Voz e Tempo Verbal
- Escreva **no tempo presente** e **na voz ativa**. NUNCA use voz passiva.
- Todos os **enunciados** devem estar no **imperativo direto e objetivo**: "Observe", "Complete", "Leia", "Ouça", "Reconheça", "Desenhe", "Narre".
- Exemplos corretos: "Clique em Iniciar atividade para começar o exercício" (NUNCA "A atividade deve ser iniciada pelo aluno").

### Sinais Proibidos
- **NUNCA usar** `;` (ponto e vírgula) — substituir por vírgula ou ponto
- **NUNCA usar** `:` (dois pontos) no corpo do texto — substituir por vírgula ou ponto
- **NUNCA usar** `—` (travessão) — substituir por vírgula ou ponto
- **NUNCA usar** aspas curvas `" "` — usar apenas aspas retas `" "`
- Aspas retas usadas **somente** no trecho literário do Narrar
- **NUNCA usar** emojis no corpo do texto

### Limites de Texto
- Frases com no máximo **30 palavras**
- Parágrafos com no máximo **70 palavras**
- Primeiro parágrafo **NUNCA** repete o conteúdo do título ou subtítulo

### Capitalização (padrão europeu — Acordo Ortográfico 1990)

> **Referência completa**: `editorial-squad/skills/capitalizer/SKILL.md`

- **Sentence-case** como padrão: maiúscula apenas na primeira palavra e nomes próprios
- **Nomes próprios** (Constantinopla, Bizâncio, Justiniano) → sempre maiúscula
- **Nomes institucionais consolidados** (Império Bizantino, Igreja Católica) → maiúscula
- **Termos descritivos/genéricos** (império romano, oriente, ocidente, arte bizantina) → minúscula no corpo
- **Preposições e artigos** (de, da, do, em, o, a, e) → minúscula no meio de títulos
- **Consistência obrigatória**: o mesmo termo deve ter a mesma capitalização em todas as seções
- **Não** usar maiúscula após dois-pontos (exceto nomes próprios, siglas, itens de lista)

### Negrito
- Usar negrito (`**texto**`) apenas para destacar termos-chave na terceira repetição do accordion
- Cada `[+FILL_IN]` deve ter exatamente 3-4 lacunas com `_____`

### Versículos
- Preferencialmente ARA ou ARC
- Formato completo: "Texto do versículo" — Referência (ex: Provérbios 22:29)
- No [+IMAGE_TEXT_ON], formato curto: "Texto resumido — Referência"

## Estrutura de Aula (5 Hábitos)

Toda aula é organizada nos **5 Hábitos** da Pedagogia do Belo:

| Hábito | Função | Seção no Rise |
|--------|--------|---------------|
| **Definir** | Apresentar o conceito central | `## Definir` |
| **Perceber** | Observar visualmente o conceito | `## Perceber` |
| **Recordar** | Memorizar a definição | `## Recordar` |
| **Praticar** | Exercitar o conceito | `## Praticar` |
| **Narrar** | Contextualizar narrativamente | `## Narrar` |

## Repetição Obrigatória da Definição

A definição do termo principal deve aparecer **idêntica** em:

1. Cabeçalho do Definir, primeira linha em negrito
2. No Recordar (Statement_D)
3. Na Revisão semanal (tabela + Recordar)

O Accordion usa a definição curta e a explicação completa em texto narrável. O texto após MP3\ repete o conteúdo do áudio, podendo manter negritos para leitura visual.

## Repetição Obrigatória das Palavras-Chave

O tema e a definição de `x.1` geram palavras-chave estruturantes. Em `x.2` e `x.3`, essas palavras devem aparecer no parágrafo livre do Definir, no Perceber, na Atividade Extra do Praticar e no texto do Narrar.

Use a repetição lexical para manter a criança em contato com o mesmo eixo da semana. Não substitua palavras centrais por sinônimos quando a intenção for fixação.

Exemplo:

```markdown
A arte nos lugares da vida

@link_png@

[MP3/]

#FSH:0b12d715e4c741399594fccb12d4bbe2

A arte está nos lugares da vida como resposta à beleza criada por Deus.

O ser humano reconhece arte quando observa beleza em casa, na igreja, nos livros e na natureza.

[MP3\]

**A arte está nos lugares da vida como resposta à beleza criada por Deus.**

O ser humano reconhece **arte** quando observa beleza em casa, na igreja, nos livros e na natureza.
```

## Regras por Bloco

### Accordion
- Tema ou pergunta simples da aula.
- Manter `@link_png@` logo abaixo do tema.
- O áudio contém a definição curta e a explicação completa em texto narrável.
- O texto após MP3\ repete o conteúdo do áudio, podendo manter negritos para leitura visual.
- Voice ID obrigatório: `#11L:XXXXXXXXXXXXXXXXX`

### Fill_In
- SEMPRE com parágrafo de enunciado ANTES: `[+PARAGRAPH] Complete as lacunas... [-PARAGRAPH]`
- O bloco contém SOMENTE o conceito (NUNCA instrução)
- 3-4 lacunas com `_____` (5 underscores)
- Respostas na última linha, separadas por vírgula e espaço, na ordem das lacunas

### Praticar
- Manter sempre a sequência `[+FILL_IN]`, `[+MULTIPLE]`, `[+ACTIVITY_WORKSHEET]`.
- O `[+MULTIPLE]` vem depois do Fill_In, com heading `Atividade 2`.
- A resposta correta do `[+MULTIPLE]` é a definição curta completa e literal.
- A Atividade Extra usa `[+ACTIVITY_WORKSHEET]` com `INSTRUCTION=`.
- Não usar `[+ATTACHMENT]` com `@link_pdf@`.

### Provas CANVAS_QUIZ
- Em todo `MULTIPLE_CHOICE`, a primeira linha não vazia depois de `MULTIPLE_CHOICE 10` é o enunciado.
- Esse enunciado deve terminar com `?`.
- Em provas semanais `.5`, gerar as questões a partir do `Praticar` das aulas `x.1`, `x.2` e `x.3`.
- Usar os `[+FILL_IN]` progressivos e as perguntas `[+MULTIPLE]` específicas como referência direta.
- As perguntas devem tratar do tema, das palavras-chave e dos exemplos da semana.
- Proibido usar perguntas estruturais ou metapedagógicas como "Qual frase resume melhor a semana?", "Qual foi o termo da semana?", "Qual aula apresentou o coração da semana?", "Relacione cada aula ao foco estudado nesta semana.", "Como o aluno deve praticar o tema?" e "O que a revisão da semana deve manter?".
- Em provas bimestrais `10.md`, `20.md`, `30.md` e `40.md`, o título é sempre `# Prova`.
- Nunca usar `# Provas` nem `# Prova bimestral` como título de prova bimestral.
- A prova bimestral usa `[CANVAS_QUIZ]`, exatamente 10 questões de 10 pontos e 9 separadores `--`.
- A prova bimestral cobre as 8 semanas do bimestre: 1–8, 11–18, 21–28 ou 31–38.
- Usar revisão bimestral, revisões semanais `.4` e provas semanais `.5` como fontes diretas.
- Padrão preferencial: 4 `FILL_IN`, 4 `MULTIPLE_CHOICE`, 1 `MATCHING` com os 8 termos centrais e 1 `TRUE_OR_FALSE`.
- Proibido usar perguntas estruturais ou metapedagógicas como "Qual termo pertence ao bloco estudado?", "Como a prova deve avaliar o aluno?", "Título inventado", "Assunto fora do Macro" ou "Qual foi o termo do bimestre?".

### Revisão semanal
- No `## [QUIZ] Praticar` das revisões `.4`, usar 1 `[+FILL_IN]` com a definição curta da semana.
- Em seguida, usar 3 `[+MULTIPLE]`, uma por aula `x.1`, `x.2` e `x.3`.
- As perguntas devem ser copiadas ou derivadas diretamente do `Praticar` das três aulas.
- As perguntas tratam do tema, das palavras-chave e dos exemplos estudados.
- Proibido usar perguntas estruturais ou metapedagógicas como "Qual frase resume a semana?", "Qual frase resume melhor a semana?", "Qual aula apresentou o coração da semana?", "Como podemos praticar o tema da semana?", "Como o aluno deve praticar o tema?", "Qual foi o termo da semana?" e "O que a revisão da semana deve manter?".

### Revisão bimestral
- Arquivos `9.md`, `19.md`, `29.md` e `39.md` têm título `# Revisão`. Usam 8 blocos semanais.
- Cada bloco começa com `## [nome da aula .1]`.
- O parágrafo usa `Nesta semana estudamos que **...**`.
- Cada bloco traz `[+HEADING] Atividade` e `[+IMAGE_TEXT_ON]` com `@link_png@`, `@link_mp3@` e o nome da aula `.1`.
- O quiz final é `## [QUIZ] Questões` com 8 questões alternando 4 `[+FILL_IN]` e 4 `[+MULTIPLE]`.

### Matching
- SEMPRE a definição primeiro, termo depois do `[=]`
- SEMPRE com enunciado antes

### Narrar
- Trecho literário cristão, puritano ou poético entre aspas retas
- No 3º ano, usar `[+PARAGRAPH]` para a leitura e manter `[+IMAGE]` com `@link_png@` antes das perguntas
- Nos demais anos, usar `[+IMAGE_TEXT_ASIDE]` conforme o template
- 3 perguntas com interrogação e espaçamento entre elas
- Perguntas curtas, diretas e fáceis de compreender
- Cada resposta deve aparecer explicitamente no texto lido
- O trecho deve trazer elementos claros do tema da aula

## Placeholders de Mídia

| Placeholder | Significado |
|-------------|-------------|
| `@link_png@` | Imagem a ser inserida |
| `@link_mp3@` | Áudio a ser inserido |
| `@link_pdf@` | PDF de atividade |
| `[+VIDEO][-VIDEO]` | Vídeo (sem conteúdo entre tags) |

## Estrutura de Arquivo

- Título: `# Título da Aula` (H1)
- Seções: `## Definir`, `## Perceber`, `## Recordar`, `## Praticar`, `## Narrar` (H2)
- Sub-headings: usar Rise Block `[+HEADING]` (NUNCA H3)
- Nome do arquivo: `X.Y.md` (ex: `36.3.md`)
- Duração máxima: 10 minutos por aula
