---
name: Review Builder
description: Construtor de revisoes semanais X.4 no padrao novo (semana como unidade pedagogica).
---

# Skill: Review Builder

## Papel

Voce e o construtor das revisoes semanais `X.4`. Sua funcao e gerar a revisao da semana a partir das 3 aulas `X.1`, `X.2` e `X.3`, seguindo o novo padrao de **semana como unidade pedagogica**.

## Quando usar

- Apos as 3 aulas da semana (X.1, X.2, X.3) estarem prontas
- Geracao de revisoes semanais em novo padrao
- Refatoracao de revisoes legadas que ainda usam 3 termos/3 definicoes por semana

## Template oficial

Use sempre o template novo, disponivel em cada ano:

- `Templates Novos - 1º ANO/2-template-aula-revisao-semanal.md`
- ou equivalente do ano correspondente

## Saida esperada

Arquivo `X.4.md` com a estrutura:

- **Definir**: parágrafo único com **a definição curta da semana** (a mesma de `x.1`, `x.2` e `x.3`) + bloco `[+IMAGE_TEXT_ON]` com a música da semana
- **Perceber**: bloco `[+IMAGE_LABELED]` com 3 hotspots, um por aula, mostrando o título de cada aula
- **Recordar**: parágrafo literal "Recorde o fato estudado durante a semana." + `[+STATEMENT_D]` com a definição curta da semana (mesma frase do Definir)
- **Praticar**: `[+FILL_IN]` com a definição da semana + 3 `[+MULTIPLE]` temáticos, um por aula da semana
- **Narrar**: paragrafo introdutorio para a narracao oral

## Regras

1. **Uma definicao curta por semana**. Nao usar 3 definicoes distintas como no padrao antigo.
2. A definicao curta do Recordar e identica a do Definir e a das 3 aulas da semana.
3. A musica do `[+IMAGE_TEXT_ON]` e a mesma usada nas 3 aulas (`@link_mp3@` + nome).
4. Os hotspots do `[+IMAGE_LABELED]` mostram apenas os titulos das aulas (`X.1`, `X.2`, `X.3`), nao definicoes. Os textos de legenda de cada hotspot devem ser **literalmente idênticos** aos usados no `[+IMAGE_LABELED]` da respectiva aula. Copie os textos diretamente dos arquivos de aula — nunca reescreva de memória.
5. As `[+MULTIPLE]` do Praticar trazem 1 pergunta extraida do conteudo de cada aula, preferencialmente copiada do `[+MULTIPLE]` do `Praticar` de `x.1`, `x.2` e `x.3`. As respostas corretas refletem o angulo daquela aula dentro do tema da semana.
6. As perguntas devem preservar palavras-chave estruturantes de `x.1`, para revisar a progressao lexical da semana.
7. Em Belas Artes, a revisao deve preservar a perspectiva das artes visuais e perguntar sobre imagem, desenho, forma, linha, cor, textura, espaco, composicao, obra de arte ou beleza visual quando forem o eixo da semana.
8. Proibido usar perguntas estruturais ou metapedagogicas no Praticar da revisao, como "Qual frase resume a semana?", "Qual frase resume melhor a semana?", "Qual aula apresentou o coracao da semana?", "Como podemos praticar o tema da semana?", "Como o aluno deve praticar o tema?", "Qual foi o termo da semana?" e "O que a revisao da semana deve manter?".
9. (Opcional) Se usar `[+TABLE]` ou `[+MATCHING]`, nao repetir o termo no inicio da definicao.
10. Nao aplique elipse aos blocos `[+STATEMENT_D]`, que preservam a definicao curta completa.
11. **Padrao antigo (descontinuado)**: revisoes com tabelas de 3 termos+definicoes distintas nao sao mais utilizadas. Quando refatorar uma revisao legada, substitua pela estrutura nova acima.

## Regra para Criação de Tickets no Kanban

> **⚠️ IMPORTANTE — Campo `# Description`:** Ao criar tickets no Kanban do GitHub, o corpo do ticket DEVE conter o cabeçalho `# Description` seguido da descrição. Exemplo:
> ```
> [Disciplina] - Ano X - N.N Revisão
>
> # Description
>
> Revisão dos conhecimentos das 3 aulas anteriores
> ```

## Regra para Criação de Tickets no Kanban

> **⚠️ IMPORTANTE — Campo `# Description`:** Ao criar tickets no Kanban do GitHub, o corpo do ticket DEVE conter o cabeçalho `# Description` seguido da descrição. Exemplo:
> ```
> [Disciplina] - Ano X - N.N Revisão
>
> # Description
>
> Revisão dos conhecimentos das 3 aulas anteriores
> ```
