# Processos e padrões do fluxo editorial — Belas Artes

Este arquivo documenta os processos operacionais definidos para o fluxo de produção das aulas de Belas Artes. Use como referência ao executar cada etapa.

---

## 1. Sincronização de títulos

**Quando usar:** sempre que houver divergência entre títulos no currículo macro e nos arquivos de aula, matriz ou visão pedagógica.

**Objetivo:** garantir que todos os arquivos do ano estejam com títulos sincronizados a partir do currículo macro como fonte de verdade.

**Prompt**

```
Rodar uma sincronização local baseada no currículo macro do ano. Trocar apenas campos de título identificados por número de aula, em matriz, visão pedagógica e H1 dos arquivos de aula existentes.

Faça isso para os arquivos do 1º ANO:

/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano/Estrutura Curricular - 1º ANO/0 - Assuntos para trabalhar no ano - novo padrão.md
/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano/Estrutura Curricular - 1º ANO/1 - Curriculo Macro - 1º ANO.md
/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano/Estrutura Curricular - 1º ANO/2 - Matriz-Curricular-objetivos - 1º ANO.md
/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano/Estrutura Curricular - 1º ANO/3 - Visão e Plano pedagogico - 1º ANO.md
/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano/Estrutura Curricular - 1º ANO/4 - Links-para-imagens-perceber-1-ano.md
/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano/Estrutura Curricular - 1º ANO/5 - Prompts-para-imagens-narrar-1-ano.md
/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano/Estrutura Curricular - 1º ANO/6 - Descrições para tickets - 1º ANO.md
```

---

## 2. Atualização dos arquivos curriculares

**Quando usar:** após qualquer atualização no currículo macro que impacte objetivos, progressão pedagógica ou abordagem de aula.

**Objetivo:** manter a matriz curricular-objetivos e a visão e plano pedagógico alinhados com a nova abordagem das aulas.

**Lógica da semana**

- `x.1` é o coração da semana: define o tema principal, o termo e a abordagem.
- `x.2` é o subtópico 1: desdobramento do tema definido em `x.1`.
- `x.3` é o subtópico 2: fechamento da progressão pedagógica da semana.

**Prompt**

```
Usando o arquivo [1 - Curriculo Macro - 1º ANO.md] como fonte de verdade, ajuste todo o arquivo de matriz curricular-objetivos e visão e plano pedagógico tendo como referência a aula e a nova abordagem.

Analise os arquivos da semana 1 para ter a noção de como é a nova abordagem da aula.

A aula 1.1 é o coração da semana.
As aulas 1.2 e 1.3 são o desdobramento do tópico principal definido no dia 1.1.
A aula 1.2 é o subtópico 1 e a aula 1.3 é o subtópico 2, fechando a progressão pedagógica da semana com o tema principal do dia 1.1 sendo desenvolvido por toda a semana.

Arquivos de referência da semana 1:

/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano - Introdução à Linguagem Visual e aos Elementos da Arte/1.1.md
/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano - Introdução à Linguagem Visual e aos Elementos da Arte/1.2.md
/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano - Introdução à Linguagem Visual e aos Elementos da Arte/1.3.md
```

---

## 3. Geração de imagens

### 3.1 Estilo visual padrão (pintura a óleo)

Use este prompt de estilo em toda imagem gerada para o 1º ano.

**Prompt de estilo**

```
Crie uma ilustração em estilo pintura digital com aparência de óleo sobre tela, inspirada em ilustrações clássicas de livros infantis e cenas educativas acolhedoras. A imagem deve ter composição narrativa, emocional e delicada, com foco na relação entre os personagens e na atmosfera da cena.

Use iluminação quente e suave, com luz dourada lateral ou ambiente, criando sensação de acolhimento, afeto e atenção. A paleta deve ter tons terrosos, sépia, creme, dourado, marrom suave, vinho, bege e pequenos detalhes de cor discreta quando necessário.

A pintura deve apresentar pinceladas visíveis, textura artística, bordas levemente difusas, fundo simples e atmosférico, sem excesso de elementos. O fundo deve parecer pintado à mão, com manchas suaves, camadas de tinta, luz espalhada e profundidade sutil.

Estilo visual: pintura digital artística, óleo sobre tela, pinceladas soltas e refinadas, textura visível, luz quente, atmosfera poética, ilustração editorial, livro infantil clássico, cena educativa acolhedora, realismo suave, detalhes delicados, fundo minimalista e difuso.

Evite aparência de foto, 3D, cartoon exagerado, anime, cores muito saturadas, traços duros, excesso de detalhes no fundo, rostos artificiais ou expressões rígidas.
```

### 3.2 Criação dos arquivos de imagens do 1º ano

**Quando usar:** ao iniciar um novo ano que ainda não tem os arquivos de links de imagens do Perceber e de prompts do Narrar.

**Objetivo:** replicar a estrutura dos arquivos do 3º ano para o contexto do 1º ano.

**Prompt**

```
Existem dois arquivos que preciso replicar para o contexto do 1º ano:

4 - Links-para-imagens-perceber-3-ano
5 - Prompts-para-imagens-narrar-3-ano

Use a mesma abordagem para replicar com o contexto do 1º ANO.
Use os arquivos de referência do currículo para saber o tema das aulas e linkar as imagens e gerar os prompts.
```

### 3.3 Geração das imagens das aulas 1, 2 e 3

**Proporção:** 16:9 horizontal.

**Fluxo:** pegar a imagem de referência de cada aula e gerar uma versão original no ChatGPT com o prompt abaixo.

**Prompt**

```
Recrie uma versão original semelhante à imagem em anexo.
```

### 3.4 Geração da imagem da revisão (aula 4)

**Proporção:** 3:4 retrato — para comportar as 3 imagens da semana em um único frame com 3 pontos de interação.

**Fluxo:** pegar a imagem 16:9 gerada na etapa anterior e refazer na proporção 3:4.

**Prompt**

```
Refaça exatamente a mesma imagem, mudando apenas a proporção. Defina a proporção como 3:4.
```

---

## 4. Música — SUNO 5.5

O nome da música se repete nas aulas 1, 2, 3 e 4 da mesma semana.

### 4.1 Estrutura da letra

```
[start]

[Verse 1]
[Definição curta da semana — uma frase.]
[Verse 1]

[Verse 2]
[Definição curta da semana — uma frase.]
[Verse 2]

[Verse 3]
[Definição curta da semana — uma frase.]
[Verse 3]

[end]
```

**Regra:** quanto menos letra, mais curta a música. Use frases secas e diretas. O Suno interpreta volume de texto como duração.

### 4.2 Estilo

```
Educational kids song, nursery rhyme style, playful clapping rhythm, cheerful vocals, simple melody, catchy repetition, minimal lyrics, repetitive structure, ultra short educational song, designed as a very short children's learning song lasting around 30 to 35 seconds.
```

### 4.3 Configurações recomendadas no Suno

| Parâmetro       | Valor recomendado |
| --------------- | ----------------- |
| Weirdness       | 20–30%            |
| Style Influence | 80–90%            |

Essas configurações mantêm a música curta, simples e evitam que o Suno adicione partes extras.
