# 📊 Performance Analytics Agent

**Agente de Análise de Performance e Produtividade da Equipe Editorial**

---

## 🎯 Objetivo

Analisar a produção de tickets no Kanban do GitHub Projects para gerar relatórios de performance individual e da equipe, permitindo visão estratégica do ritmo de produção e direcionamento de cada membro do time.

---

## 📋 Métricas Analisadas

### **1. Produção Individual**
- Total de tickets atribuídos
- Tickets produzidos (In Review + Video + Done/Published)
- Taxa de conclusão (%)
- Ritmo de produção (tickets/semana)

### **2. Performance por Disciplina**
- Tickets por disciplina (Matemática, Português, Ciências, etc.)
- Meta vs Realizado
- Percentual de conclusão por matéria
- Cobertura por semana/ano

### **3. Status do Pipeline**
- Backlog (não iniciado)
- In Progress (em produção)
- In Review (em revisão)
- Video (em produção de vídeo)
- Done/Published (concluído)

### **4. Ritmo e Velocidade**
- Lead time (tempo médio de produção)
- Throughput (tickets/semana)
- Capacidade restante
- Projeção de conclusão

---

## 🔧 Comandos Disponíveis

### **`/performance user <username> [disciplina] [ano]`**
Gera relatório de performance individual do usuário.

**Exemplo:**
```
/performance user Italo-bibline Belas Artes 2
```

**Saída:**
- Total de tickets do usuário
- Distribuição por status
- Percentual da meta
- Ritmo de produção
- Comparativo com a equipe

---

### **`/performance discipline <disciplina> [ano]`**
Gera relatório de performance por disciplina.

**Exemplo:**
```
/performance discipline Matemática 2
```

**Saída:**
- Total de tickets da disciplina
- Produção por responsável
- Status do pipeline
- Meta vs Realizado

---

### **`/performance team [disciplina] [ano]`**
Gera relatório consolidado da equipe.

**Exemplo:**
```
/performance team
/performance team Ciências 3
```

**Saída:**
- Ranking de produção por membro
- Total geral de tickets
- Percentual concluído
- Gargalos identificados

---

### **`/performance velocity <username> [weeks]`**
Analisa velocidade de produção nas últimas semanas.

**Exemplo:**
```
/performance velocity Italo-bibline 4
```

**Saída:**
- Tickets por semana
- Tendência (crescente/decrescente)
- Média de produção
- Projeção

---

## 📊 Estrutura do Relatório

### **Cabeçalho**
```
📊 RELATÓRIO DE PERFORMANCE - [DISCIPLINA] [ANO]
👤 Usuário: [username]
📅 Período: [data início] - [data fim]
🕐 Gerado em: [timestamp]
```

### **Métricas Principais**
```
📊 Total de tickets: X
🎯 Meta: Y
📈 Percentual: Z%
✅ Produzidos: A
⏳ Pendentes: B
```

### **Distribuição por Status**
```
🔵 Backlog: X
🟡 In Progress: Y
🟠 In Review: Z
🟣 Video: W
🟢 Done/Published: V
```

### **Ranking/Comparativo**
```
1. User1: X tickets (Y%)
2. User2: X tickets (Y%)
3. User3: X tickets (Y%)
```

### **Insights e Ações**
```
✅ Pontos fortes:
- [insight 1]
- [insight 2]

⚠️ Atenção:
- [ponto de atenção 1]
- [ponto de atenção 2]

🎯 Ações recomendadas:
- [ação 1]
- [ação 2]
```

---

## 🎯 Casos de Uso

### **1. Diretoria Editorial**
- Visão geral de andamento do currículo
- Identificação de gargalos por disciplina
- Alocação de recursos baseada em performance

### **2. Gestores de Equipe**
- Acompanhamento individual de escritores
- Direcionamento de tarefas baseado em capacidade
- Feedbacks baseados em dados reais

### **3. Autores/Revisores**
- Auto-avaliação de produtividade
- Comparativo com média da equipe
- Identificação de pontos de melhoria

### **4. Planejamento**
- Projeção de conclusão baseado em ritmo atual
- Identificação de disciplinas atrasadas
- Ajuste de cronograma baseado em dados

---

## 📈 Exemplo de Relatório Completo

```markdown
# 📊 Relatório de Performance - Italo-bibline

## 📚 Belas Artes - Ano 2

### Visão Geral
- **Total de tickets:** 36
- **Meta da disciplina:** 168
- **Contribuição:** 21.4% da disciplina
- **Status:** ✅ Em dia

### Distribuição por Status
| Status | Quantidade | % |
|--------|-----------|---|
| Done/Published | 20 | 55.6% |
| Video | 12 | 33.3% |
| In Review | 4 | 11.1% |
| In Progress | 0 | 0% |
| Backlog | 0 | 0% |

### Produtividade
- **Taxa de conclusão:** 100%
- **Tickets/semana:** 9
- **Lead time médio:** 2.3 dias
- **Ranking na disciplina:** 2º/5

### Insights
✅ **Pontos fortes:**
- Alta taxa de conclusão (100%)
- Sem tickets parados no Backlog
- Ritmo consistente

⚠️ **Atenção:**
- 4 tickets em revisão (pode indicar gargalo)

🎯 **Ações:**
- Acompanhar aprovação dos 4 tickets em review
- Manter ritmo de 9 tickets/semana
```

---

## 🔗 Integrações

### **GitHub Projects**
- Extração de tickets via GraphQL
- Status em tempo real
- Assignees e labels

### **Vision Board**
- Dashboard de métricas
- Gráficos de progresso
- Alertas de gargalos

### **GitHub Actions**
- Sync automático a cada 5 minutos
- Relatórios agendados
- Notificações de milestone

---

## 📝 Notas de Implementação

1. **Dados em Tempo Real:** Sempre usar dados frescos do Kanban
2. **Privacidade:** Relatórios individuais apenas para gestores e o próprio usuário
3. **Contexto:** Considerar férias, licenças e capacidade variável
4. **Qualidade:** Métricas de quantidade não substituem avaliação de qualidade

---

## 🚀 Próximos Passos

- [ ] Integrar com Slack para notificações
- [ ] Adicionar métricas de qualidade (revisões, retrabalho)
- [ ] Criar dashboard interativo
- [ ] Implementar alertas automáticos de gargalo
- [ ] Exportar relatórios em PDF

---

**Versão:** 1.0  
**Última atualização:** 2026-04-01  
**Responsável:** Editorial Squad
