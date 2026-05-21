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

Bloco expansível com tema, imagem, áudio e texto visual. Estrutura fixa:

```markdown
[+ACCORDION]

Tema ou pergunta simples da aula.

@link_png@

[MP3/]

#11L:VOICE_ID_AQUI

Definição curta da aula.

Explicação breve em texto narrável.

[MP3\]

**Definição curta da aula.**

Explicação breve com **termos-chave** em **negrito**.

[-ACCORDION]
```

**Regras:**
- O MP3 contém a definição curta e a explicação completa.
- O texto visual após `[MP3\]` repete o conteúdo do áudio, com negritos permitidos.
- O voice ID (`#11L:xxx`) é obrigatório e consistente por ano.
- O `@link_png@` permanece dentro do Accordion.

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

## ACTIVITY_WORKSHEET

Bloco de atividade com PDF. O enunciado da tarefa fica dentro do campo `INSTRUCTION=`.

```markdown
[+ACTIVITY_WORKSHEET]

INSTRUCTION=Enunciado da tarefa prática no imperativo.

[-ACTIVITY_WORKSHEET]
```

**Regras:**
- O parágrafo ANTES deste bloco deve conter o texto fixo: "Acesse o PDF abaixo e faça a atividade com atenção."
- O campo `INSTRUCTION=` contém o enunciado específico da atividade.
- O bloco `[+ATTACHMENT]` com `@link_pdf@` foi **descontinuado** e NÃO deve ser usado.

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

## TABS

Bloco com abas nomeadas, cada aba contendo uma imagem e um texto descritivo. Usado no Perceber de aulas de revisão para apresentar imagens lado a lado com análise.

```markdown
[+TABS]

Título descritivo da aba 1

@link_png@

Texto de observação da imagem 1.

--

Título descritivo da aba 2

@link_png@

Texto de observação da imagem 2.

[-TABS]
```

**Regras:**
- Sempre 2 abas por bloco.
- Cada aba tem: título, imagem e texto descritivo.
- Separador entre abas: `--`

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
  [+PARAGRAPH] Acesse o PDF abaixo e faça a atividade com atenção. [-PARAGRAPH]
  [+ACTIVITY_WORKSHEET] INSTRUCTION=... [-ACTIVITY_WORKSHEET]

## Narrar
  [+HEADING] Leitura [-HEADING]
  [+IMAGE_TEXT_ASIDE] ... [-IMAGE_TEXT_ASIDE]
  [+HEADING] Perguntas [-HEADING]
  [+LIST_NUMBERED] ... [-LIST_NUMBERED]
```
