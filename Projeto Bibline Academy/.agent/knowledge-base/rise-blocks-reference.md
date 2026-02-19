---
name: Referência de Rise Blocks
description: Referência completa de todos os Rise Blocks com sintaxe e exemplos
---

# Referência de Rise Blocks

Rise Blocks são os componentes de formatação utilizados nas aulas. Cada bloco é aberto com `[+NOME]` e fechado com `[-NOME]`.

---

## PARAGRAPH

Bloco de texto livre. Pode conter negrito, itálico e links.

```markdown
[+PARAGRAPH]

Texto do parágrafo aqui. Pode ter **negrito** e *itálico*.

[-PARAGRAPH]
```

---

## HEADING

Título de seção dentro de um hábito.

```markdown
[+HEADING]

Atividade

[-HEADING]
```

---

## VIDEO

Placeholder para vídeo. Sempre vazio (sem conteúdo entre tags).

```markdown
[+VIDEO][-VIDEO]
```

---

## ACCORDION

Bloco expansível com definição, imagem, áudio e reflexão. Estrutura fixa:

```markdown
[+ACCORDION]

Pergunta sobre o termo? (ex: "O que é Catequese?")

Definição em 1 frase.

@link_png@

[MP3/]

#11L:VOICE_ID_AQUI

Definição repetida (idêntica à de cima).

[MP3\]

Definição com **termos-chave** em **negrito**.

**Reflexão**

Texto conectando o conceito à cosmovisão cristã. Deve começar com "Entenda que...".

[-ACCORDION]
```

**Regras:**
- A definição aparece 3 vezes: texto plano, texto de áudio, texto com negrito.
- O voice ID (`#11L:xxx`) é obrigatório e consistente por ano.
- A reflexão sempre começa com "Entenda que...".

---

## IMAGE_LABELED

Imagem com pontos de interesse rotulados. Formato:

```markdown
[+IMAGE_LABELED]

@link_png@

--

X1 Y1

Título do ponto 1

Descrição do ponto 1.

--

X2 Y2

Título do ponto 2

Descrição do ponto 2.

[-IMAGE_LABELED]
```

**Regras:**
- `X Y` são coordenadas percentuais (0-100) da posição do label na imagem.
- Sempre 2 pontos de interesse.

---

## STATEMENT_D

Bloco de declaração com áudio para memorização.

```markdown
[+STATEMENT_D]

[MP3/]

#11L:VOICE_ID_AQUI

Frase para memorizar.

[MP3\]

Frase repetida (idêntica).

[-STATEMENT_D]
```

---

## IMAGE_TEXT_ON

Imagem com texto sobreposto e áudio (usado para versículos musicais).

```markdown
[+IMAGE_TEXT_ON]

@link_png@

@link_mp3@

Texto do versículo ou frase — Referência

[-IMAGE_TEXT_ON]
```

---

## FILL_IN

Exercício de completar lacunas.

```markdown
[+FILL_IN]

Frase com _____ para completar. Outra frase com _____ aqui.

palavra1, palavra2

[-FILL_IN]
```

**Regras:**
- As lacunas são marcadas com `_____` (5 underscores).
- As respostas vêm na última linha, separadas por vírgula.
- Exatamente 3-4 lacunas por exercício.

---

## ATTACHMENT

Placeholder para arquivo anexo (PDF de atividade).

```markdown
[+ATTACHMENT]

@link_pdf@

[-ATTACHMENT]
```

---

## IMAGE_TEXT_ASIDE

Imagem com texto narrativo ao lado (usado na seção Narrar).

```markdown
[+IMAGE_TEXT_ASIDE]

@link_png@

"Texto narrativo poético
com múltiplas linhas
que conta uma história
e conecta à cosmovisão cristã."

Trecho inspirado em **Versículo** e na verdade
de que [conexão temática].

[-IMAGE_TEXT_ASIDE]
```

**Regras:**
- O texto deve ser poético/narrativo, entre aspas.
- Sempre termina com referência bíblica em negrito.

---

## LIST_NUMBERED

Lista numerada de perguntas (usado ao final da seção Narrar).

```markdown
[+LIST_NUMBERED]

Primeira pergunta?

Segunda pergunta?

Terceira pergunta?

[-LIST_NUMBERED]
```

**Regras:**
- Sempre 3 perguntas.
- Sem numeração explícita (o Rise numera automaticamente).

---

## Estrutura Completa de uma Aula

```
# Título da Aula

## Definir
  [+PARAGRAPH] ... [-PARAGRAPH]
  [+VIDEO][-VIDEO]
  [+HEADING] Atividade [-HEADING]
  [+PARAGRAPH] ... [-PARAGRAPH]
  [+ACCORDION] ... [-ACCORDION]

## Perceber
  [+PARAGRAPH] ... [-PARAGRAPH]
  [+IMAGE_LABELED] ... [-IMAGE_LABELED]

## Recordar
  [+PARAGRAPH] ... [-PARAGRAPH]
  [+STATEMENT_D] ... [-STATEMENT_D]
  [+HEADING] Hora de memorizar com música [-HEADING]
  [+IMAGE_TEXT_ON] ... [-IMAGE_TEXT_ON]

## Praticar
  [+HEADING] Atividade [-HEADING]
  [+PARAGRAPH] ... [-PARAGRAPH]
  [+FILL_IN] ... [-FILL_IN]
  [+HEADING] Atividade Extra [-HEADING]
  [+PARAGRAPH] ... [-PARAGRAPH]
  [+ATTACHMENT] ... [-ATTACHMENT]

## Narrar
  [+HEADING] Leitura [-HEADING]
  [+IMAGE_TEXT_ASIDE] ... [-IMAGE_TEXT_ASIDE]
  [+HEADING] Perguntas [-HEADING]
  [+LIST_NUMBERED] ... [-LIST_NUMBERED]
```
