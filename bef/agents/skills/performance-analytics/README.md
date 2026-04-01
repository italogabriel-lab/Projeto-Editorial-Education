# 📊 Performance Analytics Agent - Documentação Completa

**Agente de Análise de Performance e Produtividade da Equipe Editorial**

---

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Objetivo](#objetivo)
3. [Arquitetura](#arquitetura)
4. [Comandos Disponíveis](#comandos-disponíveis)
5. [Exemplos de Uso](#exemplos-de-uso)
6. [Métricas Analisadas](#métricas-analisadas)
7. [Estrutura de Relatórios](#estrutura-de-relatórios)
8. [Casos de Uso](#casos-de-uso)
9. [Integrações](#integrações)
10. [FAQ](#faq)

---

## Visão Geral

O **Performance Analytics Agent** é um agente especializado em analisar dados de produção do Kanban do GitHub Projects para gerar relatórios de performance individual e da equipe.

| Propriedade | Valor |
|-------------|-------|
| **Nome** | Performance Analytics |
| **Tipo** | Analytics & Reporting |
| **Escopo** | Editorial Squad |
| **Status** | ✅ Ativo |
| **Versão** | 1.0 |

---

## Objetivo

Analisar a produção de tickets no Kanban para:

- ✅ Gerar relatórios de performance individual
- ✅ Acompanhar produtividade da equipe
- ✅ Identificar gargalos no pipeline
- ✅ Fornecer insights para melhoria contínua
- ✅ Direcionar membros com base em dados reais

---

## Arquitetura

```
┌─────────────────────────────────────────────────────────┐
│              Performance Analytics Agent                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  📥 Entrada de Dados                                    │
│     └─ GitHub Projects (GraphQL)                        │
│     └─ public/data.json                                 │
│                                                         │
│  📊 Processamento                                       │
│     └─ Filtro por usuário/disciplina/ano                │
│     └─ Cálculo de métricas                              │
│     └─ Análise de tendências                            │
│                                                         │
│  📤 Saída                                               │
│     └─ Relatórios em Markdown                           │
│     └─ Métricas em tempo real                           │
│     └─ Insights acionáveis                              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Comandos Disponíveis

### **1. `/performance user`**

**Descrição:** Gera relatório de performance individual do usuário.

**Sintaxe:**
```bash
/performance user <username> [disciplina] [ano]
```

**Parâmetros:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `username` | string | ✅ | Username do GitHub (ex: `Italo-bibline`) |
| `disciplina` | string | ❌ | Filtrar por disciplina (ex: `Belas Artes`) |
| `ano` | number | ❌ | Filtrar por ano (1-5) |

**Exemplo:**
```bash
/performance user Italo-bibline Belas Artes 2
```

**Saída:**
- Total de tickets do usuário
- Distribuição por status
- Percentual da meta
- Ritmo de produção
- Ranking na disciplina

---

### **2. `/performance discipline`**

**Descrição:** Gera relatório de performance por disciplina.

**Sintaxe:**
```bash
/performance discipline <disciplina> [ano]
```

**Parâmetros:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `disciplina` | string | ✅ | Nome da disciplina |
| `ano` | number | ❌ | Ano escolar (1-5) |

**Exemplo:**
```bash
/performance discipline Matemática 2
```

**Saída:**
- Total de tickets da disciplina
- Produção por responsável
- Status do pipeline
- Meta vs Realizado

---

### **3. `/performance team`**

**Descrição:** Gera relatório consolidado da equipe.

**Sintaxe:**
```bash
/performance team [disciplina] [ano]
```

**Parâmetros:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `disciplina` | string | ❌ | Filtrar por disciplina |
| `ano` | number | ❌ | Filtrar por ano |

**Exemplo:**
```bash
/performance team
/performance team Ciências 3
```

**Saída:**
- Ranking de produção por membro
- Total geral de tickets
- Percentual concluído
- Gargalos identificados

---

### **4. `/performance velocity`**

**Descrição:** Analisa velocidade de produção nas últimas semanas.

**Sintaxe:**
```bash
/performance velocity <username> [weeks]
```

**Parâmetros:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `username` | string | ✅ | Username do GitHub |
| `weeks` | number | ❌ | Número de semanas (default: 4) |

**Exemplo:**
```bash
/performance velocity Italo-bibline 4
```

**Saída:**
- Tickets por semana
- Tendência (crescente/decrescente)
- Média de produção
- Projeção

---

### **5. `/performance bottleneck`**

**Descrição:** Identifica gargalos no pipeline de produção.

**Sintaxe:**
```bash
/performance bottleneck [disciplina] [ano]
```

**Parâmetros:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `disciplina` | string | ❌ | Filtrar por disciplina |
| `ano` | number | ❌ | Filtrar por ano |

**Exemplo:**
```bash
/performance bottleneck
```

**Saída:**
- Status com maior acúmulo
- Tickets parados há mais tempo
- Responsáveis com gargalos
- Ações recomendadas

---

### **6. `/performance compare`**

**Descrição:** Compara performance entre usuários ou disciplinas.

**Sintaxe:**
```bash
/performance compare <user1> <user2> [disciplina]
```

**Parâmetros:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `user1` | string | ✅ | Primeiro usuário |
| `user2` | string | ✅ | Segundo usuário |
| `disciplina` | string | ❌ | Filtrar por disciplina |

**Exemplo:**
```bash
/performance compare Italo-bibline Fabiomorais87 Belas Artes
```

**Saída:**
- Comparativo lado a lado
- Vantagens de cada um
- Áreas de melhoria

---

## Exemplos de Uso

### **Relatório Individual Completo**

```bash
/performance user Italo-bibline Belas Artes 2
```

**Resultado:**
```markdown
# 📊 Relatório de Performance - Italo-bibline

## 📚 Belas Artes - Ano 2

### Visão Geral
- Total de tickets: 36
- Meta da disciplina: 168
- Contribuição: 21.4%
- Status: ✅ 100% Concluído

### Distribuição por Status
| Status | Quantidade | % |
|--------|-----------|---|
| Done/Published | 20 | 55.6% |
| Video | 12 | 33.3% |
| In Review | 4 | 11.1% |

### Produtividade
- Taxa de conclusão: 100%
- Tickets/semana: ~9
- Lead time médio: 2.3 dias
```

---

### **Relatório de Disciplina**

```bash
/performance discipline Matemática 2
```

**Resultado:**
```markdown
# 📊 Matemática - Ano 2

### Visão Geral
- Total: 168/168 ✅
- Produzidos: 168 (100%)
- Pendentes: 0 (0%)

### Distribuição por Responsável
| Usuário | Tickets | % |
|---------|---------|---|
| Fabiomorais87 | 132 | 78.6% |
| Italo-bibline | 36 | 21.4% |
```

---

### **Relatório de Equipe**

```bash
/performance team
```

**Resultado:**
```markdown
# 📊 Relatório Consolidado - Equipe

### Ranking de Produção
1. Fabiomorais87: 1320 tickets
2. Italo-bibline: 360 tickets
3. User3: 250 tickets

### Disciplinas Concluídas
- Português: 268/168 ✅
- Matemática: 504/168 ✅
- Ciências: 503/168 ✅
```

---

## Métricas Analisadas

### **1. Produção Individual**

| Métrica | Descrição | Cálculo |
|---------|-----------|---------|
| `total_tickets` | Total de tickets atribuídos | `COUNT(tickets)` |
| `produced_tickets` | Tickets produzidos | `COUNT(status IN ['In Review', 'Video', 'Done'])` |
| `completion_rate` | Taxa de conclusão | `(produced / total) * 100` |
| `velocity` | Ritmo de produção | `tickets / weeks` |

---

### **2. Performance por Disciplina**

| Métrica | Descrição | Cálculo |
|---------|-----------|---------|
| `discipline_total` | Total de tickets da disciplina | `COUNT(subject = X)` |
| `discipline_goal` | Meta da disciplina | `168 * years` |
| `completion_pct` | Percentual concluído | `(total / goal) * 100` |
| `coverage` | Cobertura por semana | `weeks_with_production / total_weeks` |

---

### **3. Status do Pipeline**

| Status | Descrição | Ação |
|--------|-----------|------|
| `Backlog` | Não iniciado | Priorizar |
| `In Progress` | Em produção | Acompanhar |
| `In Review` | Em revisão | Aprovar/Rejeitar |
| `Video` | Em produção de vídeo | Aguardar |
| `Done/Published` | Concluído | Celebrar ✅ |

---

### **4. Ritmo e Velocidade**

| Métrica | Descrição | Fórmula |
|---------|-----------|---------|
| `lead_time` | Tempo médio de produção | `(closed_at - created_at) / tickets` |
| `throughput` | Tickets por semana | `tickets / weeks` |
| `capacity_remaining` | Capacidade restante | `goal - produced` |
| `projection` | Projeção de conclusão | `remaining / velocity` |

---

## Estrutura de Relatórios

### **Cabeçalho Padrão**

```markdown
# 📊 Relatório de Performance - [USERNAME/DISCIPLINA]

**Data do Relatório:** YYYY-MM-DD  
**Período Analisado:** [período]  
**Fonte:** GitHub Projects - Kanban Geral
```

---

### **Seções Obrigatórias**

1. **Visão Geral**
   - Total de tickets
   - Meta
   - Percentual concluído
   - Status geral

2. **Distribuição por Status**
   - Tabela com quantidade e %
   - Cores semânticas (🟢🟠)

3. **Métricas de Produtividade**
   - Taxa de conclusão
   - Ritmo de produção
   - Lead time

4. **Ranking/Comparativo**
   - Posicionamento na equipe
   - Comparativo com média

5. **Insights e Ações**
   - Pontos fortes ✅
   - Pontos de atenção ⚠️
   - Ações recomendadas 🎯

---

### **Rodrigo Padrão**

```markdown
---
**Gerado por:** Performance Analytics Agent  
**Data:** YYYY-MM-DD HH:MM:SS UTC  
**Versão:** 1.0

🔗 Links Úteis:
- Kanban: [URL]
- Vision Board: [URL]
```

---

## Casos de Uso

### **1. Diretoria Editorial**

**Objetivo:** Visão estratégica de andamento

**Comandos:**
```bash
/performance team
/performance bottleneck
```

**Benefícios:**
- Identifica disciplinas atrasadas
- Aloca recursos baseado em performance
- Toma decisões baseadas em dados

---

### **2. Gestores de Equipe**

**Objetivo:** Acompanhamento individual

**Comandos:**
```bash
/performance user <username>
/performance velocity <username> 4
```

**Benefícios:**
- Feedbacks baseados em dados
- Identifica necessidades de treinamento
- Direciona tarefas por capacidade

---

### **3. Autores/Revisores**

**Objetivo:** Auto-avaliação

**Comandos:**
```bash
/performance user <me>
/performance compare <me> <peer>
```

**Benefícios:**
- Visualiza própria produtividade
- Compara com média da equipe
- Identifica pontos de melhoria

---

### **4. Planejamento**

**Objetivo:** Projeção de cronograma

**Comandos:**
```bash
/performance discipline <subject>
/performance velocity <team> 8
```

**Benefícios:**
- Projeta conclusão baseado em ritmo
- Ajusta cronograma com dados reais
- Identifica riscos antecipadamente

---

## Integrações

### **GitHub Projects**

| Recurso | Descrição |
|---------|-----------|
| GraphQL API | Extração de tickets em tempo real |
| ProjectV2 | Acesso a campos customizados |
| Assignees | Rastreamento por responsável |
| Labels | Filtros adicionais |

---

### **Vision Board**

| Recurso | Descrição |
|---------|-----------|
| Dashboard | Visualização de métricas |
| Gráficos | Progresso por disciplina |
| Alertas | Gargalos em tempo real |

---

### **GitHub Actions**

| Recurso | Descrição |
|---------|-----------|
| Auto Sync | Sync a cada 5 minutos |
| Scheduled Reports | Relatórios agendados |
| Notifications | Alertas de milestone |

---

## FAQ

### **P: Como o agente obtém os dados?**
**R:** Via GraphQL API do GitHub Projects, lendo o arquivo `public/data.json` que é sincronizado a cada 5 minutos.

---

### **P: Qual a frequência de atualização?**
**R:** Dados são atualizados a cada 5 minutos via GitHub Actions. Relatórios são gerados sob demanda.

---

### **P: Posso exportar os relatórios?**
**R:** Sim! Os relatórios são gerados em Markdown e podem ser convertidos para PDF, HTML, ou compartilhados como arquivo.

---

### **P: Como adiciono um novo usuário?**
**R:** O agente automaticamente detecta todos os usuários com tickets atribuídos no Kanban. Não é necessário cadastro.

---

### **P: Posso personalizar as métricas?**
**R:** Sim! Edite o arquivo `SKILL.md` para adicionar novas métricas ou ajustar cálculos.

---

### **P: O que fazer se um ticket estiver parado?**
**R:** Use `/performance bottleneck` para identificar. O agente sugerirá ações para desbloquear.

---

## Anexos

### **A. Template de Relatório**

[Ver template em: `editorial-squad/reports/performance/template.md`]

---

### **B. Histórico de Versões**

| Versão | Data | Mudanças |
|--------|------|----------|
| 1.0 | 2026-04-01 | Versão inicial |

---

### **C. Contato e Suporte**

- **Responsável:** Editorial Squad
- **Slack:** #performance-analytics
- **Email:** editorial@bibline.com

---

**Última atualização:** 2026-04-01  
**Próxima revisão:** 2026-05-01
