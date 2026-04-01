# Padrão Final da Aula em Markdown

Este arquivo define a estrutura definitiva que toda aula publicada deve seguir.
Todas as aulas geradas pelo Editorial Squad devem usar EXATAMENTE este esqueleto.

---

## Esqueleto

```markdown
# [Título da Aula]

## Definir

[+PARAGRAPH]

[Frase curta começando com 'Reconheça que...' e o contexto principal]

[Frase curta começando com 'Observe que...' e um argumento extra]

[Definição extremamente curta e direta ao assunto do termo (Ex: X é Y)]

Veja o vídeo abaixo.

[-PARAGRAPH]

[+VIDEO][-VIDEO]

[+HEADING]

Atividade

[-HEADING]

[+PARAGRAPH]

Leia a definição e ouça o áudio. [Instrução no imperativo].

[-PARAGRAPH]

[+ACCORDION]

[Pergunta sobre o termo, ex: "O que é Função Didática?"]

@link_png@

[MP3/]

#11L:9pDzHy2OpOgeXM8SeL0t

[Definição em português — EXATAMENTE a mesma usada no Recordar e Praticar]

[MP3\]

[Definição em português — com negrito nas palavras-chave]

**Reflexão**

[Reflexão teológica curta no imperativo.]

[-ACCORDION]

## Perceber

[+PARAGRAPH]

[3-4 frases no imperativo descrevendo o que o aluno deve observar na imagem.]

[-PARAGRAPH]

[+IMAGE_LABELED]

@link_png@

--

[X1] [Y1]

[Título do hotspot 1]

[Descrição do hotspot 1 no imperativo.]

--

[X2] [Y2]

[Título do hotspot 2]

[Descrição do hotspot 2 no imperativo.]

[-IMAGE_LABELED]

## Recordar

[+PARAGRAPH]

Ouça e repita a definição abaixo.

[-PARAGRAPH]

[+STATEMENT_D]

[MP3/]

#11L:9pDzHy2OpOgeXM8SeL0t

[Definição CURTA — 9 a 10 palavras]

[MP3\]

[Definição CURTA — mesma frase]

[-STATEMENT_D]

[+HEADING]

Hora de memorizar com música

[-HEADING]

[+PARAGRAPH]

Clique abaixo para ouvir a música sobre o tema da aula e reforçar o aprendizado.

[-PARAGRAPH]

[+IMAGE_TEXT_ON]

@link_png@

@link_mp3@

[Nome da música]

[-IMAGE_TEXT_ON]

### Variante B — RIMA (quando especificado ou 3º ano)

> Use esta variante NO LUGAR da Variante A acima.

[+HEADING]

Hora de memorizar com rima

[-HEADING]

[+PARAGRAPH]

Clique abaixo para ouvir a rima e reforçar o aprendizado sobre [tema da aula].

[-PARAGRAPH]

[+STATEMENT_A]

[MP3/]

#11L:9pDzHy2OpOgeXM8SeL0t

*[Título da rima]*

[Verso 1 rimando com o tema da aula]

[Verso 2]

[Verso 3]

[Verso 4]

[MP3\]

*[Título da rima]*

[Verso 1]

[Verso 2]

[Verso 3]

[Verso 4]

[-STATEMENT_A]

## Praticar

[+HEADING]

Atividade

[-HEADING]

[+PARAGRAPH]

Complete as lacunas para [instrução no imperativo].

[-PARAGRAPH]

[+FILL_IN]

[Definição do Recordar com _____ nas lacunas.]

[resposta1, resposta2]

[-FILL_IN]

[+HEADING]

Atividade Extra

[-HEADING]

[+PARAGRAPH]

[Instrução de atividade prática no imperativo.]

[-PARAGRAPH]

[+ATTACHMENT]

@link_pdf@

[-ATTACHMENT]

## Narrar

[+HEADING]

Leitura

[-HEADING]

### Variante A — IMAGE_TEXT_ASIDE (padrão para 1º, 2º, 4º e 5º ano)

[+IMAGE_TEXT_ASIDE]

@link_png@

"[Primeiro parágrafo do trecho literário, em prosa corrida, conectando o tema da aula à verdade bíblica.]

[Segundo parágrafo do trecho literário, aprofundando a reflexão com linguagem elevada e poética.]"

Trecho inspirado em **[Referência Bíblica]** e nas reflexões de **[Autor Cristão]**, *[Nome da Obra]* ([Contexto da obra]), [Século] ([Breve descrição da conexão com o tema da aula])

[-IMAGE_TEXT_ASIDE]

### Variante B — PARAGRAPH (padrão para 3º ano)

> Use esta variante NO LUGAR da Variante A acima.

[+PARAGRAPH]

"[Primeiro parágrafo do trecho literário, em prosa corrida, conectando o tema da aula à verdade bíblica.]

[Segundo parágrafo do trecho literário, aprofundando a reflexão com linguagem elevada e poética.]"

Trecho inspirado em **[Referência Bíblica]** e nas reflexões de **[Autor Cristão]**, *[Nome da Obra]* ([Contexto da obra]), [Século] ([Breve descrição da conexão com o tema da aula])

[-PARAGRAPH]

[+HEADING]

Perguntas

[-HEADING]

[+PARAGRAPH]

Responda oralmente às perguntas abaixo sobre o texto.

[-PARAGRAPH]

[+LIST_NUMBERED]

[Pergunta 1 com interrogação?]

[Pergunta 2 com interrogação?]

[Pergunta 3 com interrogação?]

[-LIST_NUMBERED]
```

---

## Regras Fixas

1. **Sem cabeçalhos de metadados** — não usar disciplina, módulo, base, fontes, faixa etária, estrutura.
2. **Sem emojis de seção** — não usar 🟥🟧🟨🟩🟦📌.
3. **Sem separadores `---`** entre seções.
4. **Título** começa com `#` seguido do nome criativo da aula.
5. **Seções** são `## Definir`, `## Perceber`, `## Recordar`, `## Praticar`, `## Narrar`.
6. **Definição consistente** — o mesmo conceito aparece no Accordion, no Recordar (Statement D) e no Praticar (Fill In).
7. **Recordar** — definição curta de 9-10 palavras.
8. **Praticar** — Fill In usa a definição do Recordar com `_____`.
9. **Narrar** — aspas retas `"`, trecho literário dividido em **2 parágrafos** (separados por linha em branco), atribuição em **linha única** com negrito e itálico.
10. **Sem `;`, `:`, `—`** — usar `,` ou `.`.
11. **Voz ativa e imperativo** em todas as instruções.
12. **Sem termos em inglês** na versão final — o inglês é usado apenas na pesquisa (Researcher). O Accordion começa com uma pergunta sobre o termo em português.
13. **Narrar** — sempre trazer trechos literários/poéticos de autores bíblicos, artistas cristãos, puritanos, poetas ou escritores importantes de cada época, com obra relacionada ao tema da aula.
