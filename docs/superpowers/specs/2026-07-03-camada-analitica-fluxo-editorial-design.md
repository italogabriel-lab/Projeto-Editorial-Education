# Camada analítica do fluxo editorial

Data, 3 de julho de 2026.

## Objetivo

Criar uma camada analítica read-only sobre o Kanban atual do GitHub Projects para identificar gargalos reais dentro do fluxo editorial, especialmente dentro da coluna `In Review`, sem alterar as colunas usadas pela equipe.

O sistema deve ajudar a equipe a responder quatro perguntas.

- O que está em peer review agora?
- O que está parado esperando ação?
- Qual etapa precisa de reforço nesta semana?
- Quais aulas estão prontas para avançar até vídeo e `Done`?

## Decisão aprovada

Manter as colunas atuais do Kanban.

Colunas preservadas.

- `Backlog`
- `In Progress`
- `In Review`
- `Video`
- `Done/Published`

Criar, por cima delas, subestados analíticos calculados pelo dashboard e pelos scripts de leitura.

## Diagnóstico de base

Snapshot analisado em 3 de julho de 2026.

- Total de tarefas válidas, `3.936`
- Itens ignorados por título fora do padrão, `363`
- Duplicatas descartadas, `67`

Distribuição operacional.

| Status | Cards | Peso |
|---|---:|---:|
| `In Review` | 2.007 | 51,0% |
| `Done/Published` | 602 | 15,3% |
| `Video` | 592 | 15,0% |
| `Backlog` | 453 | 11,5% |
| `In Progress` | 282 | 7,2% |

Conclusão.

O principal gargalo não está na produção inicial. Está na conversão de aulas revisadas em vídeo e de vídeo em `Done`. A coluna `In Review` acumula etapas diferentes, por isso precisa de leitura analítica mais fina.

## Subestados analíticos

O sistema deve classificar cada card em um subestado calculado. Essa classificação não altera o GitHub Projects.

| Status real | Subestado analítico | Sentido operacional |
|---|---|---|
| `Backlog` | `Não iniciado` | Aula planejada, sem produção ativa |
| `In Progress` | `Em produção editorial` | Aula em escrita, padronização ou ajuste inicial |
| `In Review` | `Peer review` | Aula aguardando primeira revisão por par |
| `In Review` | `Ajustes do autor` | Aula voltou da revisão e precisa de correção |
| `In Review` | `Review final` | Aula revisada, aguardando aprovação final |
| `In Review` | `Pronto para vídeo` | Aula aprovada editorialmente e aguardando entrada em vídeo |
| `In Review` | `Review sem classificação` | Falta sinal suficiente para inferir a etapa |
| `Video` | `Em produção de vídeo` | Aula em gravação, edição ou publicação audiovisual |
| `Done/Published` | `Done` | Aula finalizada no fluxo completo |

## Regras de classificação

### Fase 1, regras sem mudar o Kanban

Usar apenas dados já disponíveis em `public/data.json`.

- `status`
- `assignee`
- `subject`
- `year`
- `lesson_code`
- `lesson_title`
- `created_at`
- `closed_at`
- `labels`
- `title`

Classificação mínima.

- `Backlog` vira `Não iniciado`.
- `In Progress` vira `Em produção editorial`.
- `Video` vira `Em produção de vídeo`.
- `Done/Published` vira `Done`.
- `In Review` vira `Review sem classificação`, quando não houver sinais adicionais.

### Fase 2, sinais leves

Usar labels ou convenções de título quando existirem.

Labels sugeridas.

- `review:peer`
- `review:ajustes-autor`
- `review:final`
- `review:video-ready`

Essas labels não mudam coluna, apenas qualificam a leitura do dashboard.

Mapeamento.

- `status = In Review` e label `review:peer` vira `Peer review`.
- `status = In Review` e label `review:ajustes-autor` vira `Ajustes do autor`.
- `status = In Review` e label `review:final` vira `Review final`.
- `status = In Review` e label `review:video-ready` vira `Pronto para vídeo`.

### Fase 3, sinais por responsável

Quando a equipe confirmar papéis fixos, o sistema pode inferir subestado por responsável.

Exemplo.

- Responsável de revisão textual, provável `Peer review`.
- Responsável de revisão final, provável `Review final`.
- Responsável de vídeo com card ainda em `In Review`, provável `Pronto para vídeo`.

Essa inferência deve ser marcada como inferida, nunca como fato absoluto.

## Métricas principais

### Métricas de fila

- Total por status real.
- Total por subestado analítico.
- Total por disciplina.
- Total por ano.
- Total por responsável.
- Total por combinação disciplina, ano e subestado.

### Métricas de envelhecimento

Como o snapshot atual não guarda data de transição entre colunas, a primeira versão usa idade desde `created_at`.

Métricas.

- Idade média por status.
- Idade média por subestado.
- Cards com mais de 7 dias.
- Cards com mais de 14 dias.
- Cards com mais de 30 dias.
- Cards com mais de 60 dias.

Limitação explícita.

Idade desde criação não é igual a tempo na coluna. Para medir tempo real por etapa, será necessário capturar histórico de status em snapshots diários.

### Métricas de entrega

- Produzidas editorialmente, `In Review + Video + Done/Published`.
- Finalizadas, `Done/Published`.
- Prontas para vídeo, subestado `Pronto para vídeo`.
- Vazão de `Done` nos últimos 7, 14, 30 e 60 dias.
- Gap entre produzido editorialmente e `Done`.

## Alertas estratégicos

O sistema deve gerar alertas acionáveis.

Exemplos.

- `In Review concentra mais de 45% do Kanban. Priorizar revisão antes de abrir novos lotes.`
- `Matemática tem 437 cards em In Review. Criar mutirão de revisão por ano.`
- `Ano 1 tem 926 aulas produzidas, mas apenas 66 em Done. O gargalo está depois da produção textual.`
- `Há 592 cards em Video. Revisar capacidade de edição e publicação audiovisual.`
- `Cards em Review sem classificação impedem diagnóstico fino. Aplicar labels review:* nos próximos lotes.`

## Telas propostas

### 1. Fluxo editorial

Painel principal para decisão semanal.

Componentes.

- Funil por status real.
- Funil por subestado analítico.
- Cards de gargalo crítico.
- Ranking de filas por disciplina e ano.
- Lista de próximos cards a destravar.

### 2. Peer review

Painel específico para a fila de revisão.

Componentes.

- Total em `Peer review`.
- Total em `Ajustes do autor`.
- Total em `Review final`.
- Total em `Pronto para vídeo`.
- Cards sem classificação.
- Responsável atual.
- Idade do card.
- Disciplina, ano e código da aula.

### 3. Vídeo e Done

Painel para conversão final.

Componentes.

- Cards em `Pronto para vídeo`.
- Cards em `Video`.
- Cards concluídos nos últimos 7, 14, 30 e 60 dias.
- Gap entre `Video` e `Done`.
- Ranking de disciplinas mais represadas.

### 4. Decisões da semana

Resumo executivo para reunião.

Componentes.

- Top 5 gargalos.
- Top 5 ações recomendadas.
- Responsável sugerido pela próxima ação.
- Meta de redução de fila para a semana.

## Dados e arquitetura

Fonte primária.

- GitHub Projects, via GraphQL.

Arquivo atual.

- `public/data.json`

Camada proposta.

- `public/flow-analytics.json`, gerado a partir de `public/data.json`.
- `public/flow-analytics.js`, para renderizar a nova tela ou seção.
- `src/flow-editorial.html`, se a equipe preferir uma tela separada.

Alternativa simples.

- Calcular tudo no navegador a partir de `public/data.json`, sem novo JSON.

Recomendação.

Começar com cálculo no navegador para validar leitura com a equipe. Depois, se o processamento crescer, extrair para `flow-analytics.json`.

## Critérios de sucesso

O sistema será útil quando permitir que a equipe faça estas decisões em menos de 10 minutos.

- Escolher qual fila atacar primeiro.
- Identificar quais disciplinas precisam de reforço.
- Separar cards em peer review dos cards em review final.
- Distinguir gargalo editorial de gargalo de vídeo.
- Definir meta semanal de conversão para `Done`.

## Escopo fora desta fase

- Alterar colunas do GitHub Projects.
- Automatizar movimentação de cards.
- Criar novas issues.
- Escrever comentários automáticos no GitHub.
- Substituir revisão humana.
- Medir tempo real por coluna sem histórico de snapshots.

## Plano de implantação sugerido

### Etapa 1

Adicionar cálculo de subestados analíticos e painel de diagnóstico sobre o `data.json` atual.

### Etapa 2

Padronizar labels leves `review:*` para melhorar a precisão da classificação.

### Etapa 3

Adicionar snapshots históricos para medir tempo real em cada etapa.

### Etapa 4

Gerar recomendações semanais e relatórios exportáveis.

## Riscos

### Classificação imprecisa

Se a equipe não usar labels ou sinais claros, muito `In Review` ficará como `Review sem classificação`.

Mitigação.

Começar com classificação mínima e medir quantos cards precisam de label.

### Dashboard virar burocracia

Se a camada exigir preenchimento pesado, a equipe pode abandonar.

Mitigação.

Usar labels pequenas e opcionais no início. A primeira versão deve funcionar mesmo sem labels.

### Métrica de idade ser interpretada errado

Idade desde criação pode parecer tempo na coluna.

Mitigação.

Mostrar o rótulo como `idade desde criação` até existir histórico real de transição.

## Aprovação

Direção aprovada pelo usuário.

Manter as colunas atuais do Kanban e criar uma camada analítica por cima para entender o que está em peer review e onde o fluxo está travado.
