# Prompt mestre, 3º bimestre, 2º ano, Belas Artes

> **Uso**. Copie este prompt completo e envie-o ao agente para gerar ou reestruturar uma semana por vez do 3º bimestre. Substitua somente as variáveis entre colchetes. Não altere as regras fixas, os templates nem os títulos canónicos.

---

## Contexto do projeto

**Projeto**. Bibline Academy, Belas Artes, Fase da Gramática.

**Ano**. 2º ano, Da criação até a Arte Bizantina.

**Público**. Crianças de 7 e 8 anos.

**Base pedagógica**. Trivium Method Editorial, Fase da Gramática.

**Método**. Cinco hábitos, Definir, Perceber, Recordar, Praticar e Narrar.

**Bimestre**. 3º bimestre, semanas 21 a 28, com revisão em `29.md` e prova em `30.md`.

---

## Arquivos de referência obrigatória

Antes de gerar qualquer aula, consulte os arquivos abaixo nesta ordem.

| Arquivo | Função |
| --- | --- |
| `Estrutura Curricular - 2º ANO/1 - Curriculo Macro - Da criação até a Arte Bizantina - 2º ANO.md` | Fonte de verdade dos títulos canónicos, termos centrais e progressão das semanas 21 a 28. |
| `Estrutura Curricular - 2º ANO/2 - Matriz-Curricular-objetivos - 2º ANO.md` | Objetivos pedagógicos e conceitos de cada semana. |
| `Estrutura Curricular - 2º ANO/3 - Visão e Plano pedagogico - 2º ANO.md` | Visão teológica, mensagem central e função de cada aula. |
| `Estrutura Curricular - 2º ANO/0 - SEM PREFIXO Assuntos para trabalhar no ano 2 - sem numeração.md` | Lista canónica auxiliar de títulos. Em caso de divergência, o Currículo Macro prevalece. |
| `Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/1-template-aula-padrão-2-ano.md` | Template obrigatório das aulas `x.1`, `x.2` e `x.3`. |
| `Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/2-template-aula-revisao-semanal.md` | Template obrigatório das aulas `x.4`. |
| `Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/3-template-novo-revisao-bimestral.md` | Template obrigatório da revisão bimestral, `29.md`. |
| `Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/4-template-prova-semanal.md` | Template obrigatório das aulas `x.5`. |
| `Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/5-template-prova-bimestral.md` | Template obrigatório da prova bimestral, `30.md`. |
| `Estrutura Curricular - 2º ANO/4 - Links-para-imagens-perceber-2-ano.md` | Links de imagens reais para o hábito Perceber. |
| `Estrutura Curricular - 2º ANO/5 - Prompts-para-imagens-narrar-2-ano.md` | Prompts de geração de imagem para o hábito Narrar. |
| `Estrutura Curricular - 2º ANO/Referencias-Arte-Musica-2-Ano.md` | Referências de obras de arte e música por período. |

---

## Regras inegociáveis do framework

### Perspectiva de Belas Artes

- Trate todo tema pela observação das artes visuais, com imagem, desenho, forma, linha, cor, textura, espaço, composição, obra de arte e beleza visual.
- Mesmo ao abordar a Pré-História, os exemplos de pessoas, animais, cavernas, pedras, instrumentos e paisagens devem voltar para a imagem, a técnica, o material, a composição ou a forma visual da arte.
- Não transforme o exemplo em uma aula paralela de História, Ciências, devoção ou moral.

### Estrutura semanal

- Cada semana tem um termo central, definido no Currículo Macro.
- A aula `.1` apresenta o tema e fixa a definição curta da semana.
- A aula `.2` aprofunda a primeira palavra-chave do desdobramento.
- A aula `.3` aprofunda a segunda palavra-chave do desdobramento.
- A aula `.4` é a revisão semanal e usa o template próprio.
- A aula `.5` é a prova semanal e usa o template próprio com `[CANVAS_QUIZ]`.
- A definição curta, a conexão teológica e a música ou rima de Recordar são literalmente idênticas em `x.1`, `x.2` e `x.3`.

### Definição curta

- Consulte o Webster's Dictionary of 1828, em `webstersdictionary1828.com`, antes de propor a definição.
- A definição responde à pergunta “O que é?”, usa o verbo ser no presente e tem entre 8 e 12 palavras.
- A definição é ontológica, não funcional. Não use “serve para”, “faz”, “ajuda a” nem “funciona como”.
- Repita-a literalmente em `x.1`, `x.2`, `x.3`, `x.4`, nas revisões e nas provas que a utilizarem.

### Texto livre, negritos e Fill-In progressivo

- O parágrafo livre tem uma única frase direta e objetiva, focada no conceito da aula.
- Em `x.1`, coloque em negrito somente o termo central.
- Em `x.2`, coloque em negrito o termo central e a palavra-chave de `x.2`.
- Em `x.3`, coloque em negrito o termo central e a palavra-chave de `x.3`.
- A frase-base do `[+FILL_IN]` é sempre a definição curta da semana.
- Em `x.1`, a lacuna fica no termo central. Em `x.2`, fica na palavra-chave de `x.2`. Em `x.3`, fica na palavra-chave de `x.3`.
- Em aulas regulares, use `_____` para a lacuna. Dentro de `[CANVAS_QUIZ]`, use `[1]` e a resposta no formato `1 [=] palavra`.

### Enunciados e blocos obrigatórios

| Hábito | Texto ou estrutura obrigatória |
| --- | --- |
| Definir | Antes do `[+TABS]`, use literalmente `Leia o fato e ouça o áudio clicando abaixo.` |
| Definir | Use um único `[+TABS]`, nunca `[+ACCORDION]`, com título, `@link_png@`, áudio e texto visual. |
| Recordar | Abra com `Ouça e repita o fato abaixo.` |
| Praticar | Antes do Fill-In, use `Complete o fato abaixo com a palavra correta.` |
| Revisão semanal, Recordar | Use `Recorde o fato estudado durante a semana.` |
| Áudios | Use sempre a linha literal `#VOX:` dentro de `[MP3/]`. |

### Perceber, Praticar e Narrar

- Quando a aula regular tiver somente um hotspot em `[+IMAGE_LABELED]`, use a coordenada `49 50`.
- A instrução de `[+ACTIVITY_WORKSHEET]` pede uma reprodução prática de forma, composição, técnica ou detalhe visual concreto. Não use “Desenhe o elemento visual estudado” nem peça apenas uma palavra escrita.
- O `[+MULTIPLE]` é específico de cada aula e deriva do parágrafo livre da própria aula. Use duas opções no 2º ano. A resposta correta corresponde à frase-chave do parágrafo.
- No Narrar, use exatamente duas perguntas, sob o heading `Perguntas`. Cada resposta deve aparecer literalmente na leitura. A primeira pergunta deriva do parágrafo livre e a segunda, do contexto visual ou histórico da aula.
- No `[+TABS]` e no `[+IMAGE_TEXT_ASIDE]`, o áudio contém a definição curta, a explicação e a conexão teológica em uma única linha, separados por espaços. O texto depois de `[MP3\]` repete o conteúdo, com negritos permitidos.

---

## Mapa do 3º bimestre, semanas 21 a 28

| Semana | Tema | Termo central | Aula .1 | Aula .2 | Aula .3 |
| --- | --- | --- | --- | --- | --- |
| 21 | A Mesopotâmia e suas cidades | Zigurate | A Mesopotâmia e suas cidades | O zigurate como templo | A torre de Babel e o orgulho |
| 22 | Estelas e relevos mesopotâmicos | Estela | Estelas e relevos mesopotâmicos | O código de Hamurábi | A lei gravada em pedra |
| 23 | Selos cilíndricos e escrita cuneiforme | Relevo | Selos cilíndricos e escrita cuneiforme | Imagens do poder na Assíria | Relevos de guerra e caça |
| 24 | Instrumentos e música na Mesopotâmia | Harpa | Instrumentos e música na Mesopotâmia | Liras e harpas de Ur | O Hino Hurrita como registro antigo |
| 25 | A arte egípcia e a lei da frontalidade | Frontalidade | A arte egípcia e a lei da frontalidade | Pirâmides de Gizé | A monumentalidade do Egito |
| 26 | Hieróglifos e imagem | Hieróglifo | Hieróglifos e imagem | Narrativa nas paredes dos templos | O poder dos símbolos egípcios |
| 27 | As cores do Nilo | Paleta | As cores do Nilo | Cor simbólica na arte egípcia | Contraste na paleta egípcia |
| 28 | Esculturas e máscaras do Egito | Escultura egípcia | Esculturas e máscaras do Egito | O busto de Nefertiti | A máscara funerária de Tutancâmon |
| 29 | Revisão bimestral | — | Revisão das semanas 21 a 28 | — | — |
| 30 | Prova bimestral | — | Prova das semanas 21 a 28 | — | — |

---

## Como usar este prompt

1. Escolha uma semana do mapa e substitua `[SEMANA]`, `[TEMA]`, `[TERMO]`, `[A1]`, `[A2]` e `[A3]`.
2. Envie o prompt de geração abaixo.
3. Gere e revise uma aula por vez, na ordem `.1`, `.2`, `.3`, `.4` e `.5`.
4. Só gere `29.md` depois de concluir as oito revisões semanais. Só gere `30.md` depois de concluir as oito provas semanais.

---

## Prompt de geração, uma semana por vez

```text
Você é o agente Writer do Trivium Method Editorial.

Gere as cinco aulas da semana [SEMANA] do 2º ano de Belas Artes, no 3º bimestre, seguindo rigorosamente as regras abaixo.

SEMANA: [SEMANA]
TEMA DA SEMANA: [TEMA]
TERMO CENTRAL: [TERMO]
AULA .1: [A1]
AULA .2: [A2]
AULA .3: [A3]

=== FONTES OBRIGATÓRIAS ===

Antes de escrever, consulte:
- O Currículo Macro, em `Estrutura Curricular - 2º ANO/1 - Curriculo Macro - Da criação até a Arte Bizantina - 2º ANO.md`.
- O Webster's Dictionary 1828, em `webstersdictionary1828.com`, para o TERMO CENTRAL.
- A Matriz Curricular, em `Estrutura Curricular - 2º ANO/2 - Matriz-Curricular-objetivos - 2º ANO.md`.
- A Visão Pedagógica, em `Estrutura Curricular - 2º ANO/3 - Visão e Plano pedagogico - 2º ANO.md`.
- Os links de Perceber, em `Estrutura Curricular - 2º ANO/4 - Links-para-imagens-perceber-2-ano.md`.
- Os prompts de Narrar, em `Estrutura Curricular - 2º ANO/5 - Prompts-para-imagens-narrar-2-ano.md`.
- As referências de arte e música, em `Estrutura Curricular - 2º ANO/Referencias-Arte-Musica-2-Ano.md`.

=== REGRAS DA DEFINIÇÃO ===

A definição curta:
- responde “O que é [TERMO]?” com o verbo ser no presente;
- tem entre 8 e 12 palavras;
- é ontológica, não funcional;
- permanece literalmente idêntica em .1, .2, .3, .4 e nas revisões;
- trata o tema como Belas Artes, com foco em observação visual, forma, composição, material, técnica ou obra de arte.

=== ESTRUTURA DAS AULAS .1, .2 E .3 ===

Use o template `Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/1-template-aula-padrão-2-ano.md`.

Cada aula contém os cinco hábitos, Definir, Perceber, Recordar, Praticar e Narrar.

DEFINIR:
- Use um `[+PARAGRAPH]` com a definição curta em negrito, o parágrafo livre de uma única frase e a conexão teológica semanal, literalmente idêntica nas três aulas. Termine com “Veja o vídeo abaixo.”
- Inclua `[+VIDEO][-VIDEO]`, heading `Atividade` e o parágrafo literal “Leia o fato e ouça o áudio clicando abaixo.”
- Use um único `[+TABS]`, nunca `[+ACCORDION]`.
- O TABS contém o título `Definição e explicação`, `@link_png@`, `[MP3/]`, `#VOX:`, a definição, a explicação e a conexão teológica em uma única linha plain, `[MP3\]` e o mesmo texto visual com os negritos progressivos.

PERCEBER:
- Escreva uma frase curta de orientação para observar uma imagem real da aula.
- Use `[+IMAGE_LABELED]` com o link correto, um único hotspot em `49 50` e um rótulo visual específico.
- Use a seção Semana [SEMANA], Aula [SEMANA].[N] do arquivo de links de Perceber.
- Priorize obras e buscas temáticas do Getty Collection (https://www.getty.edu/art/collection/), Rawpixel Public Domain (https://www.rawpixel.com/search/public%20domain%20illuminated%20manuscript?page=1&path=1522&sort=curated), National Gallery of Art (https://www.nga.gov/search?keywords=illuminated%20manuscript) e Artvee (https://artvee.com/artist/leonardo-da-vinci/).
- Use Pixabay e Unsplash apenas como fontes complementares. Não use Wikimedia em novas referências.

RECORDAR:
- Abra com “Ouça e repita o fato abaixo.”
- Use `[+STATEMENT_D]` com a definição curta em áudio e texto, ambos literais.
- Use o heading `Hora de memorizar com música`, o parágrafo “Clique abaixo para ouvir a música.” e um `[+IMAGE_TEXT_ON]` com a música ou rima comum às três aulas da semana.

PRATICAR:
- Use o heading `Atividade 1`, o enunciado literal “Complete o fato abaixo com a palavra correta.” e um `[+FILL_IN]` com a definição curta.
- Em .1, deixe lacuna no TERMO. Em .2, deixe lacuna na palavra-chave aprofundada. Em .3, deixe lacuna na segunda palavra-chave.
- Use o heading `Atividade 2` e um `[+MULTIPLE]` específico da aula, com duas opções. A resposta correta é a frase-chave do parágrafo livre.
- Use o heading `Atividade Extra`, o parágrafo padrão do PDF e um `[+ACTIVITY_WORKSHEET]` com instrução prática, visual e concreta, no imperativo.

NARRAR:
- Use heading `Leitura` e um único `[+IMAGE_TEXT_ASIDE]` com `@link_png@`.
- O áudio usa `#VOX:` e narra, em uma única linha, a definição, a explicação e a conexão teológica.
- Após `[MP3\]`, repita literalmente o conteúdo da leitura, com negritos progressivos permitidos.
- Use o prompt correspondente à Semana [SEMANA], Aula [SEMANA].[N] no arquivo de prompts de Narrar.
- Use heading `Perguntas`, o parágrafo “Responda oralmente as duas perguntas abaixo sobre o texto.” e uma `[+LIST_NUMBERED]` com exatamente duas perguntas direcionadas. As respostas devem estar explicitamente na leitura.

=== PROGRESSÃO OBRIGATÓRIA ===

- O texto de .1 apresenta o tema e usa negrito somente no TERMO.
- O texto de .2 retoma palavras literais de .1 e coloca em negrito o TERMO e a palavra-chave de .2.
- O texto de .3 retoma palavras literais de .1 e coloca em negrito o TERMO e a palavra-chave de .3.
- Não crie um tema paralelo. As variações de .2 e .3 são aplicações ou exemplos das palavras-chave da aula .1.

=== REVISÃO SEMANAL, .4 ===

Use o template `Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/2-template-aula-revisao-semanal.md`.

Regras:
- Título `# Revisão`.
- Em Definir, escreva “Nesta semana estudamos que **[definição curta].**” e use `[+IMAGE_TEXT_ON]` com a música da semana.
- Em Perceber, use uma imagem com três hotspots, para os títulos das aulas .1, .2 e .3.
- Em Recordar, use literalmente “Recorde o fato estudado durante a semana.” e a definição curta.
- Em `## [QUIZ] Praticar`, use um `[+FILL_IN]` com a definição curta e três `[+MULTIPLE]`, um para cada aula regular, copiados ou derivados diretamente do Praticar de .1, .2 e .3.
- No Narrar, use “Agora é hora de contar exatamente o fato que você aprendeu esta semana.”

=== PROVA SEMANAL, .5 ===

Use o template `Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/4-template-prova-semanal.md`.

Regras:
- Título `# Provas` e bloco `[CANVAS_QUIZ]`.
- Exatamente dez questões de dez pontos, separadas por nove linhas `--`.
- Use três FILL_IN progressivos, três MULTIPLE_CHOICE específicos, um MATCHING, um TRUE_OR_FALSE e um MULTIPLE_CHOICE adicional de conteúdo visual.
- Dentro de CANVAS_QUIZ, o Fill-In usa `[1]`, nunca `_____`.
- A primeira linha não vazia depois de cada `MULTIPLE_CHOICE 10` é uma pergunta terminada em `?`.
- Use como fonte direta o Praticar de .1, .2 e .3. Não faça perguntas estruturais ou metapedagógicas.

=== SAÍDA ESPERADA ===

Gere os arquivos nesta ordem:
1. [SEMANA].1.md
2. [SEMANA].2.md
3. [SEMANA].3.md
4. [SEMANA].4.md
5. [SEMANA].5.md

Salve em `Aulas/`.

Comece por [SEMANA].1.md e aguarde confirmação antes de gerar a aula seguinte.
```

---

## Prompt para revisão bimestral, `29.md`

```text
Você é o agente Writer do Trivium Method Editorial.

Gere a revisão bimestral `29.md` do 3º bimestre do 2º ano de Belas Artes.

BIMESTRE: 3º
SEMANAS COBERTAS: 21 a 28

USE O TEMPLATE OBRIGATÓRIO:
`Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/3-template-novo-revisao-bimestral.md`

SEMANAS E TÍTULOS .1:
- Semana 21, A Mesopotâmia e suas cidades
- Semana 22, Estelas e relevos mesopotâmicos
- Semana 23, Selos cilíndricos e escrita cuneiforme
- Semana 24, Instrumentos e música na Mesopotâmia
- Semana 25, A arte egípcia e a lei da frontalidade
- Semana 26, Hieróglifos e imagem
- Semana 27, As cores do Nilo
- Semana 28, Esculturas e máscaras do Egito

ANTES DE ESCREVER:
- Leia as aulas .1 e as revisões .4 das semanas 21 a 28.
- Copie literalmente as definições curtas das respectivas aulas .1.
- Consulte o Currículo Macro para confirmar os títulos canónicos.

ESTRUTURA:
- Título `# Revisão`.
- Crie oito blocos, um por semana, com `## [nome da aula .1]`.
- Em cada bloco, use `[+PARAGRAPH]` com “Nesta semana estudamos que **[definição].**”, o heading `Atividade` e `[+IMAGE_TEXT_ON]` com `@link_png@`, `@link_mp3@` e o título da aula .1.
- Ao final, use `## [QUIZ] Questões` com oito questões, alternando quatro `[+FILL_IN]` e quatro `[+MULTIPLE]`.
- Copie ou derive as questões diretamente das revisões semanais .4. Elas devem tratar dos temas, termos, exemplos, formas, materiais ou técnicas visuais estudados.
- Não use questões estruturais ou metapedagógicas.

Salve em `Aulas/29.md`.
```

---

## Prompt para prova bimestral, `30.md`

```text
Você é o agente Writer do Trivium Method Editorial.

Gere a prova bimestral `30.md` do 3º bimestre do 2º ano de Belas Artes.

BIMESTRE: 3º
SEMANAS COBERTAS: 21 a 28

USE O TEMPLATE OBRIGATÓRIO:
`Estrutura Curricular - 2º ANO/Templates Novos - 2º ANO/5-template-prova-bimestral.md`

FONTES DIRETAS:
- Revisão bimestral `29.md`.
- Revisões semanais .4 e provas semanais .5 das semanas 21 a 28.
- Currículo Macro, para confirmar os títulos e os termos canónicos.

REGRAS:
- Título obrigatório `# Prova`.
- Use `[CANVAS_QUIZ]`.
- Crie exatamente dez questões de dez pontos, separadas por nove linhas `--`.
- Use preferencialmente quatro FILL_IN, quatro MULTIPLE_CHOICE, um MATCHING com os oito termos centrais e um TRUE_OR_FALSE com uma definição literal estudada.
- Nos FILL_IN de CANVAS_QUIZ, use `[1]` e a resposta no formato `1 [=] palavra`.
- A primeira linha não vazia após `MULTIPLE_CHOICE 10` deve ser uma pergunta terminada em `?`.
- As questões devem cobrir todo o bimestre e tratar de conteúdo visual, como arte rupestre, símbolos, contornos, escultura portátil, megalitos, flauta, tradição e pigmentos.
- Não use perguntas estruturais, metapedagógicas, títulos inventados nem assunto fora do Macro.

TERMOS CENTRAIS DO BIMESTRE:
- Semana 21, Zigurate
- Semana 22, Estela
- Semana 23, Relevo
- Semana 24, Harpa
- Semana 25, Frontalidade
- Semana 26, Hieróglifo
- Semana 27, Paleta
- Semana 28, Escultura egípcia

Salve em `Aulas/30.md`.
```

---

## Ordem de trabalho recomendada

```text
1. Gere a semana 21, de 21.1 a 21.5, e confirme antes de avançar.
2. Gere a semana 22, de 22.1 a 22.5, e confirme antes de avançar.
3. Gere a semana 23, de 23.1 a 23.5, e confirme antes de avançar.
4. Gere a semana 24, de 24.1 a 24.5, e confirme antes de avançar.
5. Gere a semana 25, de 25.1 a 25.5, e confirme antes de avançar.
6. Gere a semana 26, de 26.1 a 26.5, e confirme antes de avançar.
7. Gere a semana 27, de 27.1 a 27.5, e confirme antes de avançar.
8. Gere a semana 28, de 28.1 a 28.5, e confirme antes de avançar.
9. Gere a revisão bimestral, 29.md, depois de concluir as semanas 21 a 28.
10. Gere a prova bimestral, 30.md, depois de concluir 29.md e todas as provas semanais.
```

> **Nota de uso**. Preencha as definições da revisão e da prova somente depois de confirmá-las nas aulas `.1`. A definição curta nasce da consulta ao Webster 1828 e deve permanecer literal em todo o bimestre.
