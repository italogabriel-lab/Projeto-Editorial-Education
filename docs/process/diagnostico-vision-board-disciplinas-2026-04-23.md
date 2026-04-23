# Diagnóstico do Vision Board por disciplina

Data da análise, 23 de abril de 2026.

Fonte analisada, `public/data.json`, gerado pelo sync publicado no commit `7debec2`.

Critério de comparação, cada disciplina por ano deveria refletir `168` aulas no Vision Board.

## Resumo executivo

As diferenças encontradas nestas disciplinas não vieram de tickets ignorados pelo parser.

Os desvios atuais vieram de dois tipos de problema.

- Falta real de tickets no GitHub Projects
- Duplicidade lógica, quando o mesmo código aparece com dois títulos diferentes

## Resultado por disciplina

### Belas Artes, 2º ano

- Total atual no `data.json`, `159`
- Tickets ignorados, `0`
- Duplicatas técnicas no snapshot, `0`
- Código faltando, `35.3`

Diagnóstico.

O Projects está com um buraco real no código `35.3`. Não é problema de parser nem de bimestre.

Ação sugerida.

- Criar ou restaurar o ticket `35.3`

### Matemática, 1º ano

- Total atual no `data.json`, `158`
- Tickets ignorados, `0`
- Duplicatas técnicas no snapshot, `0`
- Códigos faltando, `5.1`, `17.1`

Diagnóstico.

O Projects está sem dois tickets regulares. Não há sinal de erro de leitura do Vision Board aqui.

Ação sugerida.

- Criar ou restaurar o ticket `5.1`
- Criar ou restaurar o ticket `17.1`

### Geografia, 2º ano

- Total atual no `data.json`, `158`
- Tickets ignorados, `0`
- Duplicatas técnicas no snapshot, `0`
- Códigos faltando, `31.2`, `35.1`

Diagnóstico.

O Projects está sem dois tickets regulares desta disciplina. A contagem está baixa por ausência real de cards.

Ação sugerida.

- Criar ou restaurar o ticket `31.2`
- Criar ou restaurar o ticket `35.1`

### Geografia, 3º ano

- Total atual no `data.json`, `167`
- Todos os `160` códigos regulares estão presentes
- O excesso vem de `7` duplicidades lógicas por código

Diagnóstico.

O problema aqui não é falta de tickets. O problema é que existem códigos repetidos com títulos diferentes, então o Vision Board conta os dois porque a chave canônica ainda considera `lesson_code` e `lesson_title`.

Duplicidades encontradas.

- `21.5`, `Prova` e `Provas`
- `37.1`, `Energias fósseis` e `O universo`
- `37.2`, `Energias renováveis` e `Galáxias`
- `37.3`, `Produção de energia` e `Sistema solar`
- `38.1`, `A criação de Deus` e `Planeta Terra`
- `38.2`, `O domínio responsável` e `Movimentos da Terra`
- `38.3`, `Cuidado com a Terra` e `Estações do ano`

Ação sugerida.

- Revisar `21.5` e manter apenas um ticket
- Revisar `37.1` e manter apenas um ticket
- Revisar `37.2` e manter apenas um ticket
- Revisar `37.3` e manter apenas um ticket
- Revisar `38.1` e manter apenas um ticket
- Revisar `38.2` e manter apenas um ticket
- Revisar `38.3` e manter apenas um ticket

### História, 3º ano

- Total atual no `data.json`, `160`
- Tickets ignorados, `0`
- Falta `1` código regular
- Existe `1` duplicidade lógica

Diagnóstico.

O cenário desta disciplina é misto. Falta o código `2.1`, mas ao mesmo tempo existe duplicidade no código `17.4`.

Duplicidade encontrada.

- `17.4`, `Revisao` e `Revisão`

Ação sugerida.

- Criar ou restaurar o ticket `2.1`
- Revisar `17.4` e manter apenas um ticket

## Checklist operacional

- `Belas Artes - 2º ano`
  - Criar ou restaurar `35.3`
- `Matemática - 1º ano`
  - Criar ou restaurar `5.1`
  - Criar ou restaurar `17.1`
- `Geografia - 2º ano`
  - Criar ou restaurar `31.2`
  - Criar ou restaurar `35.1`
- `Geografia - 3º ano`
  - Revisar `21.5` e manter apenas um ticket
  - Revisar `37.1` e manter apenas um ticket
  - Revisar `37.2` e manter apenas um ticket
  - Revisar `37.3` e manter apenas um ticket
  - Revisar `38.1` e manter apenas um ticket
  - Revisar `38.2` e manter apenas um ticket
  - Revisar `38.3` e manter apenas um ticket
- `História - 3º ano`
  - Criar ou restaurar `2.1`
  - Revisar `17.4` e manter apenas um ticket

## Observação técnica

O parser atual já está aceitando `Revisão`, `Prova`, semanas bimestrais `9`, `10`, `19`, `20`, `39`, `40`, e também exclui qualquer ticket com `update`.

Nestas cinco disciplinas analisadas, o desvio não veio do parser. Veio da estrutura atual do próprio GitHub Projects.
