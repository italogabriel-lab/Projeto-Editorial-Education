# Padrão Final da Aula em Markdown

Este arquivo define a estrutura definitiva que toda aula publicada deve seguir.
Todas as aulas geradas pelo Editorial Squad devem usar EXATAMENTE este esqueleto.

---

## Princípio Pedagógico — Memorização por Repetição com Variação

A unidade pedagógica é a **semana**, não a aula. Cada semana ensina **1 tema central** (definido em `x.1`) e o explora por 3 ângulos complementares (`x.1`, `x.2`, `x.3`). Os 5 hábitos dentro de cada aula são 5 abordagens diferentes do mesmo tema, criando repetição variada para fixar o conteúdo na memória da criança.

| Hábito | Abordagem | Objetivo |
|--------|-----------|----------|
| **Definir** | Apresentação da definição | Nomear e conhecer o tema |
| **Perceber** | Imagem que ilustra o tema | Reconhecer visualmente o tema |
| **Recordar** | Definição curta + rima ou música | Fixar o tema pela memória auditiva |
| **Praticar** | Exercícios sobre o tema | Aplicar e consolidar o tema ativamente |
| **Narrar** | Texto literário que toca o tema + perguntas | Reconhecer o tema em contexto narrativo |

**Regra de ouro**: se um hábito não reforça o tema central da semana, ele está errado.

**Regra da perspectiva de Belas Artes**: toda aula deve tratar o tema pela observação dos elementos visuais da arte. Natureza, casa, igreja, objetos, histórias bíblicas e vida cotidiana podem aparecer como exemplos, mas devem servir à leitura de imagem, desenho, forma, linha, cor, textura, espaço, composição, obra de arte e beleza visual.

**Regra do 1º ano**: toda aula do 1º ano é introdução à linguagem visual e aos elementos da arte. A criança deve observar como o tema aparece em imagens, desenhos, obras ou composições artísticas.

**Regra da progressão por palavras-chave**: o tema e a definição de `x.1` geram palavras-chave estruturantes. A aula `x.1` apresenta o tema de forma abrangente. As aulas `x.2` e `x.3` retomam palavras literais desse tema no exemplo central, no Definir, no Perceber, no Praticar e no Narrar. Exemplo: "O ponto representa o começo de uma arte" gera `ponto` e `começo` em `x.2`, e `ponto` e `arte` em `x.3`.

**Regra da semana como unidade**:
- A aula `x.1` apresenta o tema central da semana e fixa a **definição curta oficial**.
- As aulas `x.2` e `x.3` são **desdobramentos** do mesmo tema e mantêm a **mesma definição curta** literal de `x.1`.
- Cada aula adapta apenas a **explicação da palavra-chave no Definir** e os exemplos ao ângulo específico que está sendo trabalhado. A conexão teológica é única e idêntica nas três aulas da semana.
- Cada adaptação deve usar palavras-chave do eixo de `x.1`, sem abrir tema paralelo.
- A música ou rima do Recordar é **a mesma nas três aulas** da semana.
- O termo principal é da **semana**, não da aula. As três aulas compartilham o mesmo termo, abordando-o por ângulos diferentes.

**Regra da definição curta**: a frase curta nasce em `x.1` e se repete literalmente em `x.2` e `x.3`. Dentro de cada aula, ela abre o hábito Definir em negrito e aparece completa no Statement_D do Recordar e no Praticar com lacunas. No Accordion, o MP3 narra a definição curta, a explicação completa e a conexão teológica, sendo esta última idêntica na semana. O texto após `[MP3\]` repete o conteúdo do áudio e pode manter negritos para leitura visual.

---

## Esqueleto

```markdown
# [Título da Aula]

## Definir

[+PARAGRAPH]

**[Definição curta do Recordar, EXATAMENTE a mesma frase.]**

[Uma frase em prosa direta, sem "Reconheça que" nem "Observe que", usando palavras-chave de x.1 e conectando o tema à observação visual da arte.]

[Conexão teológica da semana, ligada ao tema e literalmente idêntica em x.1, x.2 e x.3. Veja o vídeo abaixo.]

[-PARAGRAPH]

[+VIDEO][-VIDEO]

[+HEADING]

Atividade

[-HEADING]

[+PARAGRAPH]

Leia o fato e ouça o áudio clicando abaixo.

[-PARAGRAPH]

[+ACCORDION]

[Tema ou pergunta simples sobre a aula.]

@link_png@

[MP3/]

#VOX:

[Definição curta da aula, igual ao Recordar.] [Explicação breve da aula e conexão teológica da semana em texto narrável, retomando palavras-chave do tema central.]

[MP3\]

**[Definição curta da aula, igual ao Recordar.]**

[Explicação breve da aula com destaques visuais quando necessário, retomando palavras-chave do tema central.]

[Conexão teológica da semana, literalmente idêntica nas três aulas.]

[-ACCORDION]

## Perceber

[+PARAGRAPH]

[1 frase curta e direta. Observe a imagem, nomeie a obra ou cena principal e indique o elemento visual central ligado às palavras-chave da semana.]

[-PARAGRAPH]

[+IMAGE_LABELED]

@link_png@

--

49 50

[Título curto do hotspot central]

[Uma frase curta no imperativo, apontando o que observar.]

[-IMAGE_LABELED]

## Recordar

[+PARAGRAPH]

Ouça e repita o fato abaixo.

[-PARAGRAPH]

[+STATEMENT_D]

[MP3/]

#VOX:

[Definição CURTA, 8 a 10 palavras, EXATAMENTE a mesma frase usada no cabeçalho do Definir]

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

#VOX:

*[Título da rima]* [Verso 1 rimando com o tema da aula] [Verso 2] [Verso 3] [Verso 4]

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

Complete o fato abaixo com a palavra correta.

[-PARAGRAPH]

[+FILL_IN]

[Definição curta da semana com _____ na palavra-chave específica desta aula. x.1: lacuna no termo central. x.2: lacuna na palavra-chave do desdobramento. x.3: lacuna na palavra-chave do contexto.]

[palavra-chave desta aula]

[-FILL_IN]

[+HEADING]

Atividade 2

[-HEADING]

[+MULTIPLE]

[Pergunta derivada do parágrafo livre desta aula. Formatos: "O que [TERMO] [VERBO]?", "Como [TERMO] [VERBO]?", "Onde [TERMO] aparece?", "Para que [TERMO] [VERBO]?", "Quando [TERMO] [VERBO]?", "Quais [ELEMENTOS]?". Deve diferir entre x.1, x.2 e x.3.]

[Frase-chave do parágrafo livre — resposta correta] [=] true
[Distrator — temático mas conceitualmente errado] [=]

[-MULTIPLE]

[+HEADING]

Atividade Extra

[-HEADING]

[+PARAGRAPH]

Acesse o PDF abaixo e faça a atividade com atenção.

[-PARAGRAPH]

[+ACTIVITY_WORKSHEET]

INSTRUCTION=[Instrução de atividade prática no imperativo, aplicando palavras-chave da semana.]

[-ACTIVITY_WORKSHEET]

## Narrar

[+HEADING]

Leitura

[-HEADING]

### Variante A — IMAGE_TEXT_ASIDE com áudio (padrão para todas as aulas)

> O Narrar repete LITERALMENTE o conteúdo do Definir daquela aula. Não inventar texto novo. Não adicionar frases.

[+IMAGE_TEXT_ASIDE]

@link_png@

[MP3/]

#VOX:

[Definição curta — plain, sem negrito, literalmente idêntica ao Definir.] [Explicação da palavra-chave e conexão teológica — plain, literalmente idênticas ao Definir.]

[MP3\]

**[Definição curta — bold, literalmente idêntica ao Definir.]**

[Parágrafo livre — com negritos progressivos, literalmente idêntico ao texto visual do Accordion.]

[Conexão teológica da semana, literalmente idêntica ao Definir e ao Accordion.]

[-IMAGE_TEXT_ASIDE]

### Variante B — PARAGRAPH (padrão para 3º ano)

> Use esta variante NO LUGAR da Variante A acima. O conteúdo repete LITERALMENTE o Definir daquela aula.

[+PARAGRAPH]

[Definição curta — plain, sem negrito, literalmente idêntica ao Definir.]

[Parágrafo livre — plain, sem negrito, literalmente idêntico ao parágrafo livre do Definir.]

[-PARAGRAPH]

[+IMAGE]

@link_png@

[-IMAGE]

[+HEADING]

Pergunta

[-HEADING]

[+PARAGRAPH]

Responda oralmente a pergunta abaixo sobre o texto.

[-PARAGRAPH]

[+LIST_NUMBERED]

[Uma única pergunta derivada do vocabulário do parágrafo livre. Ex: "O que [TERMO] [VERBO]?", "Como [TERMO] [VERBO]?", "Para que [TERMO] [VERBO]?"]

[-LIST_NUMBERED]
```

---

## Regras Fixas

1. **Sem cabeçalhos de metadados** — não usar disciplina, módulo, base, fontes, faixa etária, estrutura.
2. **Sem emojis de seção** — não usar 🟥🟧🟨🟩🟦📌.
3. **Sem separadores `---`** entre seções.
4. **Título** começa com `#` seguido do nome criativo da aula.
5. **Seções** são `## Definir`, `## Perceber`, `## Recordar`, `## Praticar`, `## Narrar`.
6. **Texto do MP3 em linha única** — todo conteúdo textual entre `#VOX:` e `[MP3\]` fica em uma única linha, com os trechos separados por espaço. Isso inclui definição, explicação e conexão teológica no Accordion e no Narrar, além da rima do Recordar. O texto visual após `[MP3\]` repete o conteúdo e pode manter negritos, versos e parágrafos. A frase curta do Recordar aparece sem alteração no cabeçalho do Definir e no Statement_D. O Praticar usa a frase do Recordar com `_____`. O marcador deve ser exatamente `#VOX:`, sem voice ID.
7. **Recordar** — definição curta de 8-10 palavras.
8. **Praticar** — manter sempre `[+FILL_IN]`, depois `[+MULTIPLE]`, depois `[+ACTIVITY_WORKSHEET]`.
9. **Praticar** — Fill In usa a definição curta da semana com a lacuna (`_____`) na palavra-chave específica da aula. Em `x.1`, a lacuna fica no termo central da semana. Em `x.2`, a lacuna fica na palavra-chave do desdobramento de `x.2`. Em `x.3`, a lacuna fica na palavra-chave do contexto de `x.3`. Exemplo com "O ponto representa o começo de uma arte": `x.1` → `O _____ representa o começo de uma arte.` (ponto); `x.2` → `O ponto representa o _____ de uma arte.` (começo); `x.3` → `O ponto representa o começo de uma _____.` (arte). **[+MULTIPLE]**: a pergunta é derivada do parágrafo livre daquela aula — não é fixa nem igual para x.1, x.2 e x.3. Formatos válidos: "O que [TERMO] [VERBO]?", "Como [TERMO] [VERBO]?", "Onde [TERMO] aparece?", "Para que [TERMO] [VERBO]?", "Quando [TERMO] [VERBO]?", "Quais [ELEMENTOS]?". A resposta correta é uma frase-chave do parágrafo livre. O distrator é temático mas conceitualmente errado. 2 opções para o 1º ano. Proibido usar "Qual é o significado de [TERMO]?" como pergunta fixa.
10. **Praticar** — Atividade Extra usa `[+PARAGRAPH]` com texto fixo "Acesse o PDF abaixo e faça a atividade com atenção." seguido de `[+ACTIVITY_WORKSHEET]` com `INSTRUCTION=` contendo o enunciado da tarefa. O bloco `[+ATTACHMENT]` com `@link_pdf@` **NÃO é mais utilizado**.
11. **Narrar = espelho literal do Definir** — o bloco `[+IMAGE_TEXT_ASIDE]` do Narrar repete literalmente a definição curta, a explicação da palavra-chave e a conexão teológica do Definir daquela aula. Antes de `[MP3\]`, os três trechos ficam em uma única linha plain, separados por espaço. Após `[MP3\]`, o texto usa negritos progressivos idênticos ao texto visual do Accordion e pode permanecer em parágrafos. Nenhuma frase adicional é permitida — em especial proibidas frases do tipo "A criança aprende a...", "A criança percebe que...".
12. **Narrar no 3º ano** — manter sempre `[+PARAGRAPH]` para a leitura e, logo depois, `[+IMAGE]` com `@link_png@` antes de `Perguntas`.
13. **Sem `;`, `:`, `—`** — usar `,` ou `.`.
14. **Voz ativa e imperativo** em todas as instruções.
15. **Sem termos em inglês** na versão final — o inglês é usado apenas na pesquisa (Researcher). O Accordion começa com uma pergunta sobre o termo em português.
16. **Perguntas do Narrar** — no 2º ano, usar exatamente 2 perguntas direcionadas, heading `Perguntas` (plural), derivadas do vocabulário do texto. Cada resposta deve aparecer explicitamente no texto. Nos demais anos, seguir a quantidade do template específico. Proibido: "O que você percebeu sobre...", perguntas abertas, reflexivas, abstratas ou inferenciais.
17. **Parágrafo inicial do Definir** — iniciar com a definição curta em negrito, literalmente idêntica ao Recordar. Depois, usar **UMA ÚNICA FRASE** para explicar a palavra-chave, seguida pela conexão teológica da semana e de "Veja o vídeo abaixo." na mesma linha. A conexão teológica é literalmente idêntica em `x.1`, `x.2` e `x.3`. **Progressão de negritos obrigatória**: em `x.1`, a explicação coloca em negrito somente o TERMO; em `x.2`, coloca em negrito o TERMO e a KW2 (= resposta do fill-in de `x.2`); em `x.3`, coloca em negrito o TERMO e a KW3 (= resposta do fill-in de `x.3`). O Accordion espelha os dois trechos, plain no áudio (após `#VOX:`) e com negritos progressivos no texto visual (após `[MP3\]`).
18. **Bloco do Definir** — nos demais anos, usar Accordion com tema ou pergunta simples, `@link_png@`, MP3 e texto visual. No 2º ano, usar um único TABS com título, `@link_png@`, definição, explicação, áudio, texto visual e conexão teológica, seguido diretamente de `[-TABS]`. O áudio dentro de `[MP3/]...[MP3\]` narra a definição curta, a explicação completa e a conexão teológica em uma única linha, separadas por espaço. O texto após `[MP3\]` repete o conteúdo, com negritos e parágrafos permitidos.
19. **Perguntas do Narrar — verificação mínima** — no 2º ano, confirmar que há exatamente 2 perguntas no `[+LIST_NUMBERED]`, que o heading é `Perguntas` (plural) e que cada resposta está literalmente no texto. Nos demais anos, confirmar a quantidade definida pelo template específico.
21. **Revisões `.4`** — usam **uma única definição curta da semana** (a mesma de `x.1`, `x.2` e `x.3`), não três definições distintas. Em flashcards visuais por aula, mostre apenas o título de cada aula. Em tabelas e matchings opcionais, não repetir o termo no início da definição. A definição completa fica somente no `[+STATEMENT_D]`.
22. **Perceber** — usar 1 frase curta e direta no enunciado. Em aula regular, usar um único hotspot central em `49 50`. As observações e explicações ficam no hotspot, também de forma curta. Revisões `.4` podem usar vários hotspots. Títulos devem ter 2 a 5 palavras e descrições 1 frase curta. Evitar explicações longas e análise extensa.
23. **Semana como unidade** — a definição curta e a conexão teológica de `x.1` devem aparecer literalmente em `x.2` e `x.3`. O termo principal é compartilhado pelas 3 aulas. A música/rima do Recordar é a mesma na semana inteira. Só varia a explicação da palavra-chave e os exemplos de cada aula.
