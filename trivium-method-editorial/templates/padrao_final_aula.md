# Padrão Final da Aula em Markdown

Este arquivo define a estrutura definitiva que toda aula publicada deve seguir.
Todas as aulas geradas pelo Editorial Squad devem usar EXATAMENTE este esqueleto.

---

## Princípio Pedagógico — Memorização por Repetição com Variação

Cada aula ensina **1 conceito central** (o TERMO definido no Definir). Os 5 hábitos são 5 abordagens diferentes do mesmo conceito, criando repetição variada para fixar o tema na memória da criança.

| Hábito | Abordagem | Objetivo |
|--------|-----------|----------|
| **Definir** | Apresentação da definição | Nomear e conhecer o conceito |
| **Perceber** | Imagem que ilustra o conceito | Reconhecer visualmente o conceito |
| **Recordar** | Definição curta + rima ou música | Fixar o conceito pela memória auditiva |
| **Praticar** | Exercícios sobre o conceito | Aplicar e consolidar o conceito ativamente |
| **Narrar** | Texto literário que toca o conceito + perguntas | Reconhecer o conceito em contexto narrativo |

**Regra de ouro**: se um hábito não reforça o conceito central do Definir, ele está errado.

**Regra da definição curta**: a frase curta do Recordar é a fonte textual obrigatória da aula. Ela deve abrir o hábito Definir em negrito, aparecer completa no texto do Accordion após `[MP3\]` e aparecer completa no Statement_D do Recordar. O áudio do Accordion NÃO repete o termo, pois o termo já aparece na pergunta. O Praticar usa a mesma frase com lacunas.

---

## Esqueleto

```markdown
# [Título da Aula]

## Definir

[+PARAGRAPH]

**[Definição curta do Recordar, EXATAMENTE a mesma frase.]**

[Frase começando com 'Reconheça que...' e o contexto principal. Frase começando com 'Observe que...' e um argumento extra. As duas frases ficam na MESMA linha, separadas por ponto e espaço, sem linha em branco entre elas.]

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

[MP3/]

#XAI:rex

[Definição curta sem repetir o termo da pergunta, ex: "é o que representa o mundo interior das pessoas."]

[MP3\]

[Definição curta do Recordar, EXATAMENTE a mesma frase.]

[-ACCORDION]

## Perceber

[+PARAGRAPH]

[1 frase curta e direta. Observe a imagem, nomeie a obra ou cena principal e indique o elemento visual central.]

[-PARAGRAPH]

[+IMAGE_LABELED]

@link_png@

--

[X1] [Y1]

[Título curto do hotspot 1]

[Uma frase curta no imperativo, apontando o que observar.]

--

[X2] [Y2]

[Título curto do hotspot 2]

[Uma frase curta no imperativo, apontando o que observar.]

[-IMAGE_LABELED]

## Recordar

[+PARAGRAPH]

Ouça e repita a definição abaixo.

[-PARAGRAPH]

[+STATEMENT_D]

[MP3/]

#XAI:rex

[Definição CURTA, 9 a 10 palavras, EXATAMENTE a mesma frase usada no cabeçalho do Definir e no Accordion]

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

#XAI:rex

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

Atividade 2

[-HEADING]

[+MULTIPLE]

Qual é o significado de [termo]?

[Distrator curto e plausível.] [=]
[Distrator curto e plausível.] [=]
[Definição curta completa, literalmente idêntica ao Definir, ao Accordion e ao Recordar.] [=] true

[-MULTIPLE]

[+HEADING]

Atividade Extra

[-HEADING]

[+PARAGRAPH]

Acesse o PDF abaixo e faça a atividade com atenção.

[-PARAGRAPH]

[+ACTIVITY_WORKSHEET]

INSTRUCTION=[Instrução de atividade prática no imperativo.]

[-ACTIVITY_WORKSHEET]

## Narrar

[+HEADING]

Leitura

[-HEADING]

### Variante A — IMAGE_TEXT_ASIDE (padrão para 1º, 2º, 4º e 5º ano)

[+IMAGE_TEXT_ASIDE]

@link_png@

"[Primeiro parágrafo do trecho literário, em prosa corrida, com elementos explícitos do tema da aula e do conceito definido.]

[Segundo parágrafo do trecho literário, com frases claras que tragam as respostas diretas às perguntas.]"

Trecho inspirado em **[Referência Bíblica]** e nas reflexões de **[Autor Cristão]**, *[Nome da Obra]* ([Contexto da obra]), [Século].

[-IMAGE_TEXT_ASIDE]

### Variante B — PARAGRAPH (padrão para 3º ano)

> Use esta variante NO LUGAR da Variante A acima.

[+PARAGRAPH]

"[Primeiro parágrafo do trecho literário, em prosa corrida, com elementos explícitos do tema da aula e do conceito definido.]

[Segundo parágrafo do trecho literário, com frases claras que tragam as respostas diretas às perguntas.]"

Trecho inspirado em **[Referência Bíblica]** e nas reflexões de **[Autor Cristão]**, *[Nome da Obra]* ([Contexto da obra]), [Século].

[-PARAGRAPH]

[+IMAGE]

@link_png@

[-IMAGE]

[+HEADING]

Perguntas

[-HEADING]

[+PARAGRAPH]

Responda oralmente às perguntas abaixo sobre o texto.

[-PARAGRAPH]

[+LIST_NUMBERED]

[Pergunta 1 — fato explícito que aparece no texto?]

[Pergunta 2 — detalhe visual, ação ou objeto mencionado no texto?]

[Pergunta 3 — tema da aula dito ou mostrado no texto?]

[-LIST_NUMBERED]
```

---

## Regras Fixas

1. **Sem cabeçalhos de metadados** — não usar disciplina, módulo, base, fontes, faixa etária, estrutura.
2. **Sem emojis de seção** — não usar 🟥🟧🟨🟩🟦📌.
3. **Sem separadores `---`** entre seções.
4. **Título** começa com `#` seguido do nome criativo da aula.
5. **Seções** são `## Definir`, `## Perceber`, `## Recordar`, `## Praticar`, `## Narrar`.
6. **Definição literalmente idêntica** — a frase curta do Recordar aparece sem alteração no cabeçalho do Definir, no texto do Accordion após `[MP3\]` e no Statement_D. O áudio do Accordion usa a mesma definição sem repetir o termo da pergunta. O Praticar usa a mesma frase com `_____`.
7. **Recordar** — definição curta de 9-10 palavras.
8. **Praticar** — manter sempre `[+FILL_IN]`, depois `[+MULTIPLE]`, depois `[+ACTIVITY_WORKSHEET]`.
9. **Praticar** — Fill In usa a definição do Recordar com `_____`. A múltipla escolha pergunta o significado do termo e traz a definição curta completa como resposta correta.
10. **Praticar** — Atividade Extra usa `[+PARAGRAPH]` com texto fixo "Acesse o PDF abaixo e faça a atividade com atenção." seguido de `[+ACTIVITY_WORKSHEET]` com `INSTRUCTION=` contendo o enunciado da tarefa. O bloco `[+ATTACHMENT]` com `@link_pdf@` **NÃO é mais utilizado**.
11. **Narrar** — aspas retas `"`, trecho literário dividido em **2 parágrafos** (separados por linha em branco), atribuição em **linha única** com negrito e itálico. O texto do Narrar DEVE conter elementos explícitos do tema da aula e respostas diretas para as 3 perguntas.
12. **Narrar no 3º ano** — manter sempre `[+PARAGRAPH]` para a leitura e, logo depois, `[+IMAGE]` com `@link_png@` antes de `Perguntas`.
13. **Sem `;`, `:`, `—`** — usar `,` ou `.`.
14. **Voz ativa e imperativo** em todas as instruções.
15. **Sem termos em inglês** na versão final — o inglês é usado apenas na pesquisa (Researcher). O Accordion começa com uma pergunta sobre o termo em português.
16. **Narrar** — sempre trazer trechos literários/poéticos de autores bíblicos, artistas cristãos, puritanos, poetas ou escritores importantes de cada época, com obra relacionada ao tema da aula.
17. **Parágrafo inicial do Definir** — iniciar com a definição curta em negrito, literalmente idêntica ao Recordar. Depois, as frases "Reconheça que..." e "Observe que..." ficam na MESMA linha de texto, separadas por ponto e espaço.
18. **Accordion do Definir** — conter apenas pergunta, MP3 e definição textual. O áudio dentro de `[MP3/]...[MP3\]` NÃO repete o termo da pergunta. O texto após `[MP3\]` repete literalmente a definição curta completa. Não incluir imagem nem reflexão.
19. **Atribuição do Narrar** — terminar SEMPRE com **ponto final após o Século**. NÃO adicionar o trecho de conexão entre parênteses. Formato correto: `Trecho inspirado em **[Ref]** e nas reflexões de **[Autor]**, *[Obra]* ([Contexto]), [Século].`
20. **Perguntas do Narrar** — as 3 perguntas devem ser curtas, diretas e de fácil compreensão. Cada resposta deve aparecer explicitamente no texto lido. As perguntas devem ajudar a criança a narrar com suas palavras o que compreendeu. Proibido usar perguntas abertas, reflexivas, abstratas, inferenciais ou dependentes de contexto prévio.
21. **Revisões `.4`** — em tabelas e matchings, não repetir o termo no início da definição. Correto: `Imprensa[,] É sistema mecânico que multiplica livros rápida acessivelmente.[,]` e `É sistema mecânico que multiplica livros rápida acessivelmente. [=] Imprensa`. Manter a definição completa somente no `[+STATEMENT_D]`.
22. **Perceber** — usar 1 frase curta e direta no enunciado. As observações e explicações ficam nos hotspots, também de forma curta. Hotspots devem ter títulos de 2 a 5 palavras e descrições com 1 frase curta. Evitar explicações longas e análise extensa.
