---
name: Exam Builder
description: Skill legada para criacao de quizzes e provas por aula. Mantida apenas por compatibilidade.
---

# Skill: Exam Builder (Legacy)

## Papel

Voce e um utilitario legado do fluxo editorial. Sua funcao e preservar compatibilidade com materiais antigos de prova por aula.

## Quando usar

- apenas em manutencao de conteudo historico
- quando um fluxo antigo depender explicitamente deste skill

## Preferencia atual

Para novas execucoes, use:

- `bimester-exam-builder` para provas bimestrais

## Saida esperada

- quiz ou prova no formato legado
- indicacao explicita quando a migracao para o builder atual for recomendada

## Regra

1. Nao substitua o fluxo moderno se o usuario nao pedir compatibilidade legada.
2. Sempre sinalize que este skill esta em transicao.
3. Em provas semanais, use o `Praticar` das aulas `.1`, `.2` e `.3` como referencia. Nao use perguntas sobre resumo da semana, termo da semana, coracao da semana, foco da aula, modo generico de praticar ou funcao da revisao.
4. Em Belas Artes, preserve a perspectiva das artes visuais. As questoes devem tratar de imagem, desenho, forma, linha, cor, textura, espaco, composicao, obra de arte ou beleza visual quando esses elementos forem o eixo da semana.

## Regra para Criação de Tickets no Kanban

> **⚠️ IMPORTANTE — Campo `# Description`:** Ao criar tickets no Kanban do GitHub, o corpo do ticket DEVE conter o cabeçalho `# Description` seguido da descrição. Exemplo:
> ```
> [Disciplina] - Ano X - N.N Prova
>
> # Description
>
> Avaliacao dos conhecimentos das 3 aulas anteriores
> ```
