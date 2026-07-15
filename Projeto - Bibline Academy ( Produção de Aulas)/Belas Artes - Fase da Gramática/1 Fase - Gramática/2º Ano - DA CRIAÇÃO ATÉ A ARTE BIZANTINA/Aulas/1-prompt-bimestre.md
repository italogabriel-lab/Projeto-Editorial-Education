# Prompt Mestre — 1º Bimestre — 2º Ano — Belas Artes

> **Uso**: copie este prompt completo e envie ao agente para gerar ou reestruturar as aulas de uma semana por vez.
> Substitua apenas as variáveis marcadas com `[VARIÁVEL]` antes de enviar.
> Nunca altere as regras fixas, o template ou os blocos de referência.

---

## Contexto do Projeto

**Projeto**: Bibline Academy — Belas Artes — Fase da Gramática
**Ano**: 2º ano — Da criação até a Arte Bizantina
**Público**: crianças de 7 e 8 anos
**Base pedagógica**: Trivium Method Editorial — Fase da Gramática
**Método**: 5 hábitos — Definir, Perceber, Recordar, Praticar, Narrar

---

## Arquivos de Referência Obrigatória

Antes de gerar qualquer aula, consultar nesta ordem:

| Arquivo | Função |
| --- | --- |
| `Estrutura Curricular - 2º ANO/1 - Curriculo Macro - Da criação até a Arte Bizantina - 2º ANO.md` | Títulos canônicos, termos centrais e progressão das semanas |
| `Estrutura Curricular - 2º ANO/2 - Matriz-Curricular-objetivos - 2º ANO.md` | Objetivos pedagógicos e conceitos de cada semana |
| `Estrutura Curricular - 2º ANO/3 - Visão e Plano pedagogico - 2º ANO.md` | Visão teológica, mensagem central e função de cada aula |
| `Estrutura Curricular - 2º ANO/0 - SEM PREFIXO Assuntos para trabalhar no ano 2 - sem numeração.md` | Lista canônica de títulos — fonte de verdade para os títulos |
| `Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/1-template-aula-padrão-2-ano.md` | **Template obrigatório** para aulas x.1, x.2 e x.3 |
| `Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/2-template-aula-revisao-semanal.md` | **Template obrigatório** para aulas x.4 |
| `Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/3-template-novo-revisao-bimestral.md` | **Template obrigatório** para a revisão bimestral (aula 9) |
| `Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/4-template-prova-semanal.md` | **Template obrigatório** para aulas x.5 |
| `Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/5-template-prova-bimestral.md` | **Template obrigatório** para a prova bimestral (aula 10) |
| `Estrutura Curricular - 2º ANO/4 - Links-para-imagens-perceber-2-ano.md` | Links de imagens reais para o bloco Perceber |
| `Estrutura Curricular - 2º ANO/5 - Prompts-para-imagens-narrar-2-ano.md` | Prompts de geração de imagem para o bloco Narrar |
| `Estrutura Curricular - 2º ANO/Referencias-Arte-Musica-2-Ano.md` | Referências de obras de arte e música por período |

---

## Regras Inegociáveis do Framework

### Estrutura semanal
- Cada semana tem **1 termo central** fixado no Currículo Macro.
- A aula `.1` é o **coração pedagógico** — apresenta o tema e fixa a definição central.
- A aula `.2` aprofunda a **primeira palavra-chave** do desdobramento.
- A aula `.3` aprofunda a **segunda palavra-chave** do desdobramento.
- A aula `.4` é a **revisão semanal** (usa template x.4).
- A aula `.5` é a **prova semanal** (usa template x.5 com `[CANVAS_QUIZ]`).

### Definição curta
- Ontológica, responde "O que é?" com verbo ser no presente.
- Entre 8 e 12 palavras.
- **Literalmente idêntica** em x.1, x.2, x.3, x.4 e nas revisões.
- Referência obrigatória: Webster's Dictionary 1828 (webstersdictionary1828.com).

### Fill-In progressivo

> [!CAUTION]
> **FILL_IN em CANVAS_QUIZ usa `[1]` na frase — nunca `_____`.**
> - Dentro de `[+FILL_IN]` (aulas regulares): usa `_____` → `O _____ é a obra de Deus.`
> - Dentro de `CANVAS_QUIZ` (provas x.5, 9, 10): usa `[1]` → `A [1] é a obra de Deus.`
> - A resposta em ambos os casos: `1 [=] palavra`
- A frase-base é sempre a definição curta da semana.
- x.1 → lacuna no **TERMO central**.
- x.2 → lacuna na **palavra-chave de x.2**.
- x.3 → lacuna na **palavra-chave de x.3**.

### Negritos progressivos no parágrafo livre
- x.1 → negrito apenas no **TERMO**.
- x.2 → negrito no **TERMO** e na **KW2**.
- x.3 → negrito no **TERMO** e na **KW3**.

### Narrar — padrão do 2º ano (2 perguntas)
- Heading: `Perguntas` (plural).
- `[+LIST_NUMBERED]` com **2 perguntas**.
- Pergunta 1 — derivada do parágrafo livre.
- Pergunta 2 — derivada do contexto histórico ou visual da aula.
- A resposta de cada pergunta deve aparecer explicitamente no texto do Narrar.

### Enunciados fixos obrigatórios
| Hábito | Enunciado fixo |
| --- | --- |
| Definir (antes do Accordion) | `Leia o fato e ouça o áudio clicando abaixo.` |
| Recordar (parágrafo de abertura) | `Ouça e repita a definição abaixo.` |
| Praticar (antes do Fill-In) | `Complete o fato abaixo com a palavra correta.` |
| Revisão semanal — Recordar | `Recorde o fato estudado durante a semana.` |

### Áudio em linha única
- Dentro do `[+ACCORDION]` e do `[+IMAGE_TEXT_ASIDE]`, a definição curta e o parágrafo livre ficam **na mesma linha**, separados por espaço, antes de `[MP3\]`.

### Pergunta do [+MULTIPLE]
- Derivada do parágrafo livre da aula específica.
- Nunca genérica (proibido: "Qual frase resume a semana?").
- 2 opções para o 2º ano.
- Resposta correta = frase-chave do parágrafo livre.

---

## Mapa do 1º Bimestre — Semanas 1 a 8

| Semana | Tema | Termo central | Aula .1 | Aula .2 | Aula .3 |
| --- | --- | --- | --- | --- | --- |
| 1 | A arte vem de Deus | Criação | A arte vem de Deus | A criação é bela | Feitos à imagem do Criador |
| 2 | Arte nos primeiros dias | Ofício | Arte nos primeiros dias | Jubal e o som da música | Tubalcaim e o ofício do metal |
| 3 | A arte como louvor | Louvor | A arte como louvor | Cores que expressam sentimentos | O som da alegria |
| 4 | Imagens que contam histórias | Imagem | Imagens que contam histórias | Luz nas pinturas | O que a arte revela sobre Deus |
| 5 | O dom criativo em Gênesis | Dom criativo | O dom criativo em Gênesis | No princípio, Deus criou | O homem criador |
| 6 | A cor na criação de Deus | Cor | A cor na criação de Deus | O arco da aliança | O círculo cromático |
| 7 | Cores primárias e secundárias | Matiz | Cores primárias e secundárias | O poder do matiz e da luz | O céu como tela divina |
| 8 | Sons que tocam o coração | Som | Sons que tocam o coração | Ritmo e melodia | Vozes dos instrumentos |
| 9 | Revisão bimestral | — | Revisão das semanas 1 a 8 | — | — |
| 10 | Prova bimestral | — | Prova das semanas 1 a 8 | — | — |

---

## Como Usar Este Prompt

### Passo 1 — Escolha a semana a gerar
Substitua `[SEMANA]`, `[TEMA]`, `[TERMO]`, `[A1]`, `[A2]`, `[A3]` pelos valores da tabela acima.

### Passo 2 — Cole o prompt de geração abaixo

---

## Prompt de Geração — Uma Semana por Vez

```
Você é o agente Writer do Trivium Method Editorial.

Gere as 5 aulas da semana [SEMANA] do 2º ano de Belas Artes, seguindo rigorosamente as regras abaixo.

SEMANA: [SEMANA]
TEMA DA SEMANA: [TEMA]
TERMO CENTRAL: [TERMO]
AULA .1: [A1]
AULA .2: [A2]
AULA .3: [A3]

=== FONTES OBRIGATÓRIAS ===

Antes de escrever qualquer definição, consultar:
- Webster's Dictionary 1828 em webstersdictionary1828.com para o TERMO CENTRAL.
- Matriz Curricular: Estrutura Curricular - 2º ANO/2 - Matriz-Curricular-objetivos - 2º ANO.md
- Visão Pedagógica: Estrutura Curricular - 2º ANO/3 - Visão e Plano pedagogico - 2º ANO.md
- Links de imagem do Perceber: Estrutura Curricular - 2º ANO/4 - Links-para-imagens-perceber-2-ano.md
- Prompts de imagem do Narrar: Estrutura Curricular - 2º ANO/5 - Prompts-para-imagens-narrar-2-ano.md

=== REGRAS DE DEFINIÇÃO ===

A definição curta:
- Responde "O que é [TERMO]?" com verbo ser no presente.
- Tem entre 8 e 12 palavras.
- É ontológica, não funcional (não usa "serve para", "funciona como").
- É literalmente idêntica nas 3 aulas e na revisão semanal.

=== ESTRUTURA DE CADA AULA ===

Use o template: Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/1-template-aula-padrão-2-ano.md

Cada aula tem 5 hábitos: Definir, Perceber, Recordar, Praticar, Narrar.

DEFINIR:
- [+PARAGRAPH]: negrito na definição curta + parágrafo livre (1 frase, negritos progressivos) + "Veja o vídeo abaixo."
- [+VIDEO][-VIDEO]
- [+HEADING] Atividade [-HEADING]
- [+PARAGRAPH] "Leia o fato e ouça o áudio clicando abaixo." [-PARAGRAPH]
- [+ACCORDION]: pergunta simples, @link_png@, [MP3/], #FSH:..., definição+parágrafo (plain, 1 linha), [MP3\], definição bold + parágrafo bold
- [-ACCORDION]

PERCEBER:
- [+PARAGRAPH]: frase de orientação
- [+IMAGE_LABELED]: @link_png@, --, coordenadas, rótulo [-IMAGE_LABELED]
- Use os links em: 4 - Links-para-imagens-perceber-2-ano.md, seção Semana [SEMANA], aula [SEMANA].[N]

RECORDAR:
- [+PARAGRAPH] "Ouça e repita a definição abaixo." [-PARAGRAPH]
- [+STATEMENT_D]: [MP3/], #FSH:..., definição plain, [MP3\], definição plain [-STATEMENT_D]
- [+HEADING] Hora de memorizar com música [-HEADING]
- [+PARAGRAPH] "Clique abaixo para ouvir a música." [-PARAGRAPH]
- [+IMAGE_TEXT_ON]: @link_png@, @link_mp3@, [nome da música] [-IMAGE_TEXT_ON]

PRATICAR:
- [+HEADING] Atividade 1 [-HEADING]
- [+PARAGRAPH] "Complete o fato abaixo com a palavra correta." [-PARAGRAPH]
- [+FILL_IN]: definição com _____ na KW da aula, resposta [-FILL_IN]
- [+HEADING] Atividade 2 [-HEADING]
- [+MULTIPLE]: pergunta específica da aula, 2 opções [-MULTIPLE]
- [+HEADING] Atividade Extra [-HEADING]
- [+PARAGRAPH] "Acesse o PDF abaixo e faça a atividade com atenção." [-PARAGRAPH]
- [+ACTIVITY_WORKSHEET]: INSTRUCTION=[instrução prática] [-ACTIVITY_WORKSHEET]

NARRAR (padrão 2º ano — 2 perguntas):
- [+HEADING] Leitura [-HEADING]
- [+IMAGE_TEXT_ASIDE]: @link_png@, [MP3/], #FSH:..., definição+parágrafo (plain, 1 linha), [MP3\], definição bold + parágrafo bold [-IMAGE_TEXT_ASIDE]
- Use o prompt de imagem em: 5 - Prompts-para-imagens-narrar-2-ano.md, seção Semana [SEMANA], Aula [SEMANA].[N]
- [+HEADING] Perguntas [-HEADING]
- [+PARAGRAPH] "Responda oralmente as perguntas abaixo sobre o texto." [-PARAGRAPH]
- [+LIST_NUMBERED]: Pergunta 1 (do parágrafo livre), Pergunta 2 (do contexto visual/histórico) [-LIST_NUMBERED]

=== FILL-IN PROGRESSIVO ===

A frase-base é a definição curta da semana.
- Aula .1: lacuna no TERMO → _____ [restante da definição].
- Aula .2: lacuna na palavra-chave de .2.
- Aula .3: lacuna na palavra-chave de .3.

=== REVISÃO SEMANAL x.4 ===

Use o template: Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/2-template-aula-revisao-semanal.md

Estrutura:
- Título: # Revisão
- Definir: parágrafo "Nesta semana estudamos que **[definição curta].**" + [+IMAGE_TEXT_ON] com a música da semana
- Perceber: parágrafo de observação + [+IMAGE_LABELED] com 3 hotspots (títulos x.1, x.2, x.3)
- Recordar: "Recorde o fato estudado durante a semana." + [+HEADING]Atividade + [+STATEMENT_D] com a definição
- [QUIZ] Praticar: 1 [+FILL_IN] + 3 [+MULTIPLE] (copiadas ou derivadas do Praticar de x.1, x.2 e x.3)
- Narrar: "Agora é hora de contar exatamente o fato que você aprendeu esta semana."

=== PROVA SEMANAL x.5 ===

Use o template: Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/4-template-prova-semanal.md

Estrutura: # Provas, [CANVAS_QUIZ], 9 questões de 10 pontos separadas por --
Padrão: 3 FILL_IN (progressivos) + 3 MULTIPLE_CHOICE + 1 MATCHING + 1 TRUE_OR_FALSE + 1 MULTIPLE_CHOICE

=== SAÍDA ESPERADA ===

Gere os arquivos nesta ordem:
1. [SEMANA].1.md — aula x.1
2. [SEMANA].2.md — aula x.2
3. [SEMANA].3.md — aula x.3
4. [SEMANA].4.md — revisão semanal
5. [SEMANA].5.md — prova semanal

Salvar em: Aulas/

Comece pela aula [SEMANA].1.md. Aguarde confirmação antes de prosseguir para a próxima aula.
```

---

## Prompt para Revisão Bimestral (Aula 9)

```
Você é o agente Writer do Trivium Method Editorial.

Gere a revisão bimestral — aula 9.md — do 1º bimestre do 2º ano de Belas Artes.

BIMESTRE: 1º
SEMANAS COBERTAS: 1 a 8

USE O TEMPLATE OBRIGATÓRIO:
Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/3-template-novo-revisao-bimestral.md

SEMANAS E TÍTULOS .1:
- Semana 1 → A arte vem de Deus
- Semana 2 → Arte nos primeiros dias
- Semana 3 → A arte como louvor
- Semana 4 → Imagens que contam histórias
- Semana 5 → O dom criativo em Gênesis
- Semana 6 → A cor na criação de Deus
- Semana 7 → Cores primárias e secundárias
- Semana 8 → Sons que tocam o coração

DEFINIÇÕES CURTAS (literais, buscar nas aulas .1 de cada semana):
- Semana 1: [definição da semana 1]
- Semana 2: [definição da semana 2]
- Semana 3: [definição da semana 3]
- Semana 4: [definição da semana 4]
- Semana 5: [definição da semana 5]
- Semana 6: [definição da semana 6]
- Semana 7: [definição da semana 7]
- Semana 8: [definição da semana 8]

ESTRUTURA DA REVISÃO BIMESTRAL:
- Título: # Revisão
- 8 blocos de semana (## [Nome da aula .1]) com:
  - [+PARAGRAPH] "Nesta semana estudamos que **[definição].**"
  - [+HEADING] Atividade [-HEADING]
  - [+IMAGE_TEXT_ON]: @link_png@, @link_mp3@, [nome da aula .1] [-IMAGE_TEXT_ON]
- ## [QUIZ] Questões — 8 questões alternando 4 [+FILL_IN] e 4 [+MULTIPLE]
  - Copiadas das revisões semanais .4 de cada semana

Salvar em: Aulas/9.md
```

---

## Prompt para Prova Bimestral (Aula 10)

```
Você é o agente Writer do Trivium Method Editorial.

Gere a prova bimestral — aula 10.md — do 1º bimestre do 2º ano de Belas Artes.

BIMESTRE: 1º
SEMANAS COBERTAS: 1 a 8

USE O TEMPLATE OBRIGATÓRIO:
Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/5-template-prova-bimestral.md

REGRAS:
- Título: # Prova (nunca # Provas nem # Prova bimestral)
- [CANVAS_QUIZ]
- 10 questões de 10 pontos, separadas por 9 linhas --
- Padrão: 4 FILL_IN + 4 MULTIPLE_CHOICE + 1 MATCHING (8 termos) + 1 TRUE_OR_FALSE
- Fontes: revisões semanais .4 e provas semanais .5 das semanas 1 a 8
- Proibido: perguntas estruturais, metapedagógicas ou títulos inventados

TERMOS CENTRAIS DO BIMESTRE:
- Semana 1: Criação
- Semana 2: Ofício
- Semana 3: Louvor
- Semana 4: Imagem
- Semana 5: Dom criativo
- Semana 6: Cor
- Semana 7: Matiz
- Semana 8: Som

Salvar em: Aulas/10.md
```

---

## Ordem de Trabalho Recomendada

```
1. Gere semana 1 (1.1 → 1.2 → 1.3 → 1.4 → 1.5) — confirme antes de avançar
2. Gere semana 2 (2.1 → 2.2 → 2.3 → 2.4 → 2.5) — confirme antes de avançar
3. Gere semana 3 (3.1 → 3.2 → 3.3 → 3.4 → 3.5) — confirme antes de avançar
4. Gere semana 4 (4.1 → 4.2 → 4.3 → 4.4 → 4.5) — confirme antes de avançar
5. Gere semana 5 (5.1 → 5.2 → 5.3 → 5.4 → 5.5) — confirme antes de avançar
6. Gere semana 6 (6.1 → 6.2 → 6.3 → 6.4 → 6.5) — confirme antes de avançar
7. Gere semana 7 (7.1 → 7.2 → 7.3 → 7.4 → 7.5) — confirme antes de avançar
8. Gere semana 8 (8.1 → 8.2 → 8.3 → 8.4 → 8.5) — confirme antes de avançar
9. Gere revisão bimestral (9.md) — após ter todas as definições das semanas 1-8
10. Gere prova bimestral (10.md) — após ter todas as provas semanais .5
```

---

> **Nota de uso**: preencha os campos em branco (`[definição da semana N]`) após gerar as aulas .1 de cada semana. A definição curta nasce do Webster 1828 e deve ser confirmada antes de usá-la na revisão e na prova bimestral.
