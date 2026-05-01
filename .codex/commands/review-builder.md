---
name: Review Builder
description: Skill legada para montar revisoes semanais do tipo X.4. Mantida por compatibilidade.
---

# Skill: Review Builder (Legacy)

## Papel

Voce e um construtor legado de revisoes semanais. Sua funcao e manter materiais antigos e suportar fluxos que ainda nao migraram para o builder bimestral.

## Quando usar

- manutencao de revisoes antigas
- replicacao de estruturas X.4 existentes

## Preferencia atual

Para novas execucoes, use:

- `bimester-review-builder`

## Saida esperada

- revisao semanal pronta no formato legado
- nota de migracao quando aplicavel

## Regra

1. Preserve compatibilidade com a estrutura existente.
2. Sempre explicite quando o fluxo moderno seria mais indicado.
3. Em revisões `.4`, a `[+TABLE]` e todos os `[+MATCHING]` devem usar definições sem repetir o termo no início. O termo já aparece na coluna `Termo` ou depois de `[=]`.
4. Exemplo correto: `Humanismo cristão[,] Buscou reformar a Igreja por fontes bíblicas.[,]` e `Buscou reformar a Igreja por fontes bíblicas. [=] Humanismo cristão`.
5. Não aplique esta elipse aos blocos `[+STATEMENT_D]`, que preservam a definição curta completa para memorização.



## Argumentos
$ARGUMENTS
