# Prompt mestre - 4º bimestre - 3º ano - Belas Artes

> **Uso:** copie o prompt de geração de uma semana ou o prompt bimestral e envie-o ao agente Writer. Não altere regras fixas, templates ou títulos canónicos.

## Contexto do projeto

**Projeto:** Bibline Academy - Belas Artes - Fase da Gramática
**Ano:** 3º ano - Arte Cristã Oriental até o Renascimento do Norte
**Público:** pais educadores e alunos entre 8 e 9 anos
**Método:** 5 hábitos - Definir, Perceber, Recordar, Praticar e Narrar

## Arquivos de referência obrigatória

Antes de gerar qualquer aula, consulte nesta ordem:

| Arquivo | Função |
| --- | --- |
| `Estrutura Curricular - 3º ANO/1 - Curriculo Macro - Arte Cristã Oriental até o Renascimento do Norte - 3º ANO.md` | Fonte de verdade para títulos, termos centrais e sequência semanal |
| `Estrutura Curricular - 3º ANO/2 - Matriz-Curricular-objetivos - 3º ANO.md` | Objetivos pedagógicos e conceitos de cada aula |
| `Estrutura Curricular - 3º ANO/3 - Visão e Plano pedagogico - 3º ANO.md` | Visão teológica, mensagem central e função na progressão |
| `Estrutura Curricular - 3º ANO/4 - Links-para-imagens-perceber-3-ano.md` | Referências visuais do Perceber |
| `Estrutura Curricular - 3º ANO/5 - Prompts-para-imagens-narrar-3-ano.md` | Prompts de imagem do Narrar |
| `Estrutura Curricular - 3º ANO/Referencias-Arte-Musica-3-Ano.md` | Obras, artistas, edifícios e referências musicais |
| `Estrutura Curricular - 3º ANO/Templates Novos - 3º ANO/1-template-aula-padrão-3-ano.md` | Template obrigatório para aulas x.1, x.2 e x.3 |
| `Estrutura Curricular - 3º ANO/Templates Novos - 3º ANO/2-template-aula-revisao-semanal.md` | Template obrigatório para a revisão x.4 |
| `Estrutura Curricular - 3º ANO/Templates Novos - 3º ANO/3-template-novo-revisao-bimestral.md` | Template obrigatório para a revisão bimestral 39.md |
| `Estrutura Curricular - 3º ANO/Templates Novos - 3º ANO/4-template-prova-semanal.md` | Template obrigatório para a prova semanal x.5 |
| `Estrutura Curricular - 3º ANO/Templates Novos - 3º ANO/5-template-prova-bimestral.md` | Template obrigatório para a prova bimestral 40.md |

## Regras inegociáveis

### Estrutura inicial dos arquivos

- Todo arquivo de aula regular e revisão semanal começa somente com o H1 canónico, uma linha em branco e o primeiro H2 do template.
- Não repita o título da aula, o tema semanal, o termo central nem qualquer subtítulo entre o H1 e `## Definir`.
- Exemplo obrigatório:

```md
# O Renascimento do Norte

## Definir
```

### Unidade pedagógica semanal

- Cada semana possui um único termo central, uma definição curta e um título de música compartilhado, igual ao título da aula x.1.
- A aula x.1 é o coração pedagógico e apresenta o tema central.
- A aula x.2 aprofunda a primeira palavra-chave de x.1.
- A aula x.3 aprofunda a segunda palavra-chave de x.1.
- Apenas a explicação da palavra-chave, as imagens e a Atividade Extra variam entre x.1, x.2 e x.3.
- A conexão teológica é ligada ao tema e literalmente idêntica em x.1, x.2 e x.3.
- No PDF da Atividade Extra, peça uma reprodução prática de forma, composição, técnica ou detalhe visual específico da aula. Não use enunciado genérico nem peça somente que a criança escreva uma palavra.
- A perspectiva é sempre de Belas Artes e artes visuais. Observe imagem, forma, linha, cor, textura, espaço, composição, obra, edifício ou beleza visual.

### Definição curta

- Consulte o Webster's Dictionary 1828 antes de propor a definição.
- Responda “O que é?” com o verbo ser no presente.
- Use de 8 a 12 palavras.
- Escreva uma definição ontológica, não funcional.
- Repita-a literalmente em x.1, x.2, x.3, x.4, revisões e provas.

### Fill-In progressivo

- A frase-base é a definição curta da semana.
- Em x.1, deixe lacuna no termo central.
- Em x.2, deixe lacuna na palavra-chave do primeiro desdobramento.
- Em x.3, deixe lacuna na palavra-chave do segundo desdobramento.
- Em `[+FILL_IN]`, use `_____`.
- Em `[CANVAS_QUIZ]`, use `[1]` e escreva a resposta como `1 [=] palavra`.

### Regras fixas dos hábitos

| Hábito | Regra |
| --- | --- |
| Definir | No `[+PARAGRAPH]` inicial, use a definição curta, a explicação da palavra-chave e “Veja o vídeo abaixo.”. Não inclua conexão teológica. |
| Definir | Use um único `[+TABS]` com o título canónico, `@link_png@`, definição, explicação, MP3 e texto visual. Não use Accordion nem conexão teológica. |
| Definir | Antes de TABS, escreva literalmente “Leia o fato e ouça o áudio clicando abaixo.” |
| Perceber | Use um único hotspot em `49 50` nas aulas regulares. |
| Recordar | Abra com “Ouça e repita o fato abaixo.” |
| Praticar | Abra o Fill-In com “Complete o fato abaixo com a palavra correta.” |
| Narrar | Use um único `[+IMAGE_TEXT_ASIDE]`. Na linha de `@link_png@`, coloque a conexão teológica semanal. Não use `[+PARAGRAPH]` seguido de `[+IMAGE]`. |
| Narrar | Use exatamente três perguntas diretas. Todas as respostas devem estar explicitamente na leitura. |
| Revisão x.4 | Abra o Recordar com “Recorde o fato estudado durante a semana.” |

### Áudio e texto visual

- No TABS, mantenha somente definição curta e explicação da palavra-chave na mesma linha antes de `[MP3\]`.
- No Narrar, mantenha definição curta, explicação e conexão teológica na mesma linha antes de `[MP3\]`.
- Depois de `[MP3\]`, o TABS e o Narrar mostram somente definição e explicação, com os negritos progressivos necessários.
- Use o marcador literal `#VOX:`.
- A conexão teológica da semana fica na linha de `@link_png@` do Narrar e é idêntica em x.1, x.2 e x.3.

## Mapa do 4º bimestre

| Semana | Tema | Termo central | Aula x.1 | Aula x.2 | Aula x.3 |
| --- | --- | --- | --- | --- | --- |
| 31 | O Renascimento do Norte | Renascimento do Norte | O Renascimento do Norte | Cidades comerciais, oficinas e pintura flamenga | O Norte europeu e o Renascimento italiano |
| 32 | A pintura a óleo flamenga | Pintura a óleo | A pintura a óleo flamenga | Camadas transparentes, cor e luz | Texturas e detalhes na pintura sobre madeira |
| 33 | Jan van Eyck e o detalhe simbólico | Detalhe simbólico | Jan van Eyck e o detalhe simbólico | O Casal Arnolfini e o retrato | Objetos, espelho e luz na pintura flamenga |
| 34 | A gravura no Renascimento do Norte | Gravura | A gravura no Renascimento do Norte | Xilogravura e gravura em metal | Imagens reproduzidas e circulação de ideias |
| 35 | Albrecht Dürer e o desenho gravado | Gravura de Dürer | Albrecht Dürer e o desenho gravado | Lebre Jovem e a observação da natureza | Melancolia I e os símbolos na gravura |
| 36 | Hans Holbein e o retrato do Norte | Retrato | Hans Holbein e o retrato do Norte | Os Embaixadores e os objetos simbólicos | Precisão, textura e presença no retrato |
| 37 | A Reforma e as imagens no Norte europeu | Reforma | A Reforma e as imagens no Norte europeu | Arte, culto e circulação de gravuras | O coral luterano e o canto comunitário |
| 38 | O legado dos Renascimentos | Renascimento | O legado dos Renascimentos | Equilíbrio italiano e detalhe do Norte | A transição do Renascimento para o Maneirismo |
| 39 | Revisão bimestral | - | Revisão das semanas 31 a 38 | - | - |
| 40 | Prova bimestral | - | Prova das semanas 31 a 38 | - | - |

## Prompt de geração de uma semana

```
Você é o agente Writer do Trivium Method Editorial.

Gere as cinco aulas da semana [SEMANA] do 3º ano de Belas Artes.

SEMANA: [SEMANA]
TEMA DA SEMANA: [TEMA]
TERMO CENTRAL: [TERMO]
AULA x.1: [A1]
AULA x.2: [A2]
AULA x.3: [A3]

Consulte o Currículo Macro, a Matriz, a Visão e Plano Pedagógico, os Links do Perceber, os Prompts do Narrar, as Referências de Arte e Música e todos os templates do 3º ano antes de escrever.

Respeite estas regras:

1. Use o título do Currículo Macro literalmente no H1 de cada aula.
2. Depois do H1, deixe uma linha em branco e escreva diretamente `## Definir`. Não repita título, tema, termo ou subtítulo nesse intervalo. Aplique a mesma regra em x.4.
3. Consulte Webster's Dictionary 1828 e produza uma definição curta ontológica de 8 a 12 palavras.
4. Repita a mesma definição curta e a mesma conexão teológica em x.1, x.2 e x.3.
5. No `[+PARAGRAPH]` inicial do Definir, escreva definição, explicação e “Veja o vídeo abaixo.”. Não inclua conexão teológica.
6. No Definir, use um único `[+TABS]` com título canónico, `@link_png@`, definição, explicação, MP3 e texto visual. Não inclua conexão teológica nem use Accordion.
7. Use `#VOX:`. No TABS, mantenha definição e explicação em uma linha. No Narrar, mantenha definição, explicação e conexão teológica em uma linha.
8. Em Perceber, use um único `[+IMAGE_LABELED]` com `@link_png@` e hotspot em `49 50`.
9. Em Recordar, use literalmente “Ouça e repita o fato abaixo.” e use o título da aula x.1 como título da música em x.1, x.2, x.3 e x.4.
10. Em Praticar, use Fill-In progressivo e uma pergunta `[+MULTIPLE]` específica por aula, derivada do parágrafo livre.
11. Em Narrar, use um único `[+IMAGE_TEXT_ASIDE]`. Coloque a conexão teológica na linha de `@link_png@`. Após `[MP3\]`, mostre apenas definição e explicação. Use exatamente três perguntas diretas, com respostas literais no texto.
12. Na revisão x.4, use uma única definição, um Fill-In e três questões Multiple, uma para cada aula. No Recordar, use literalmente “Recorde o fato estudado durante a semana.”.
13. Na prova semanal x.5, use o template do 3º ano. Gere dez questões de 10 pontos a partir do Praticar das aulas x.1, x.2 e x.3.
14. Use linguagem visual, frases diretas, voz ativa, imperativo e capitalização sentence-case.

Gere nesta ordem:
1. [SEMANA].1.md
2. [SEMANA].2.md
3. [SEMANA].3.md
4. [SEMANA].4.md
5. [SEMANA].5.md

Salve em Aulas/. Gere uma aula por vez e aguarde confirmação antes de passar ao próximo arquivo.
```

## Prompt de revisão e prova bimestral

```
Você é o agente Writer do Trivium Method Editorial.

Gere a revisão bimestral 39.md e a prova bimestral 40.md do 4º bimestre do 3º ano de Belas Artes.

ESCOPO: semanas 31 a 38.
REVISÃO: 39.md.
PROVA: 40.md.

Consulte as aulas x.1, x.2, x.3, x.4 e x.5 das semanas 31 a 38, o Currículo Macro e os templates bimestrais do 3º ano.

Para 39.md:
- Use o título `# Revisão`.
- Crie oito blocos, um para cada semana.
- Em cada bloco, use o nome da aula x.1, o parágrafo “Nesta semana estudamos que **...**”, uma Atividade e uma imagem com `@link_png@` e `@link_mp3@`.
- Finalize com oito questões, alternando quatro Fill-In e quatro Multiple, derivados das revisões semanais.

Para 40.md:
- Use o título `# Prova`.
- Use `[CANVAS_QUIZ]`.
- Crie exatamente 10 questões de 10 pontos, separadas por nove linhas `--`.
- Cubra todas as semanas 31 a 38.
- Prefira quatro FILL_IN, quatro MULTIPLE_CHOICE, um MATCHING dos oito termos e um TRUE_OR_FALSE.
- Em FILL_IN, use `[1]`, nunca `_____`.
- Faça a primeira linha não vazia depois de MULTIPLE_CHOICE 10 terminar com `?`.
- Não use perguntas estruturais ou metapedagógicas.

Salve 39.md e 40.md em Aulas/. Gere 39.md primeiro e aguarde confirmação antes de gerar 40.md.
```

## Ordem de execução

1. Gere 31.1.md até 31.5.md.
2. Repita o processo, uma semana por vez, até 38.5.md.
3. Gere 39.md com a revisão bimestral.
4. Gere 40.md com a prova bimestral.
