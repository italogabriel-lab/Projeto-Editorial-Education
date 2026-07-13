# 5. Narrar (Hábito 5 de 5)

## Princípio pedagógico

Este é o **quinto e último contato da criança com o tema da semana**, agora pela via da repetição com imagem. O Narrar repete LITERALMENTE o conteúdo do Definir daquela aula — definição curta e parágrafo livre — apresentado com imagem e áudio. As perguntas conduzem a criança a localizar na leitura o que ouviu e leu no Definir. A criança deve narrar com as próprias palavras o que compreendeu.

**Regra absoluta**: o texto do Narrar é literalmente idêntico ao Definir daquela aula. Não inventar texto novo. Não adicionar frases.

Em Belas Artes, o Narrar deve preservar o vocabulário visual da aula. A criança deve responder com base em imagem, desenho, forma, linha, cor, textura, espaço, composição, obra de arte ou beleza visual quando esses termos forem o foco.

## Estrutura obrigatória

```markdown
[+HEADING]
Leitura
[-HEADING]
```

### Variante A — IMAGE_TEXT_ASIDE com áudio (padrão para todas as aulas)

```markdown
[+IMAGE_TEXT_ASIDE]

@link_png@

[MP3/]

#FSH:0b12d715e4c741399594fccb12d4bbe2

[Definição curta — plain, sem negrito, literalmente idêntica ao Definir.] [Parágrafo livre — plain, sem negrito, literalmente idêntico ao parágrafo livre do Definir.]

[MP3\]

**[Definição curta — bold, literalmente idêntica ao Definir.]**

[Parágrafo livre — com negritos progressivos, literalmente idêntico ao texto visual do Accordion.]

[-IMAGE_TEXT_ASIDE]
```

### Variante B — PARAGRAPH (3º ano)

Use esta variante para o 3º ano. O bloco `[+IMAGE]` é obrigatório e permanece depois da leitura, antes das perguntas. O conteúdo do `[+PARAGRAPH]` repete literalmente o Definir daquela aula.

```markdown
[+PARAGRAPH]

[Definição curta — plain, sem negrito, literalmente idêntica ao Definir.]

[Parágrafo livre — plain, sem negrito, literalmente idêntico ao parágrafo livre do Definir.]

[-PARAGRAPH]

[+IMAGE]
@link_png@
[-IMAGE]
```

### Pergunta

```markdown
[+HEADING]
Pergunta
[-HEADING]

[+PARAGRAPH]
Responda oralmente a pergunta abaixo sobre o texto.
[-PARAGRAPH]

[+LIST_NUMBERED]

[Uma única pergunta derivada do vocabulário do parágrafo livre. Formatos: "O que [TERMO] [VERBO]?", "Como [TERMO] [VERBO]?", "Onde [TERMO] aparece?", "Para que [TERMO] [VERBO]?"]

[-LIST_NUMBERED]
```

## Regras da pergunta — obrigatórias

- **Uma única pergunta** por aula. Heading `Pergunta` (singular).
- A pergunta é derivada diretamente do vocabulário do parágrafo livre daquela aula.
- A resposta aparece explicitamente no texto (definição + parágrafo livre). Não requer inferência.
- Formatos válidos: "O que [TERMO] [VERBO]?", "Como [TERMO] [VERBO]?", "Onde [TERMO] aparece?", "Para que [TERMO] [VERBO]?".
- Proibido: "O que você percebeu sobre...", perguntas abertas, reflexivas, abstratas ou inferenciais.
- Proibido: perguntas que exijam conhecimento prévio ou contexto externo ao texto.

## Regras do texto

- O texto do Narrar é LITERALMENTE IDÊNTICO ao Definir daquela aula. Não inventar, não adicionar, não resumir.
- Antes de `[MP3\]`: definição curta e parágrafo livre plain, em uma única linha e separados por espaço, igual ao áudio do Accordion do Definir.
- Após `[MP3\]`: texto com negritos progressivos, igual ao texto visual do Accordion do Definir.
- Proibido adicionar frases do tipo "A criança aprende a...", "A criança percebe que...", "A criança cria..." ou qualquer variação — são genéricas e violam o padrão.
- Sem `;`, `:`, `—` — usar `,` ou `.`.
