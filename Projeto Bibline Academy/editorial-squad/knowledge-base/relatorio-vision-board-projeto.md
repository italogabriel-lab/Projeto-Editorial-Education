# 📊 PRODUCT REQUIREMENTS DOCUMENT (PRD)

## 🧭 Nome do Produto
Vision Board de Produção Educacional (Real-Time GitHub Intelligence)

---

## 🎯 Objetivo

Criar um sistema de visualização estratégica, hospedado no GitHub Pages, que:

- Consome dados do GitHub Projects (Kanban) em tempo real
- Apresenta o progresso da produção de aulas
- Analisa performance da equipe
- Compara execução vs metas por ano
- Identifica gargalos operacionais automaticamente

---

## 🧠 Visão Estratégica

Transformar o GitHub Projects em:

→ Sistema de gestão educacional  
→ Painel executivo em tempo real  
→ Motor de inteligência operacional  

---

## 🧩 Princípio Fundamental

🚫 O sistema NÃO altera o Kanban  
✅ Apenas lê e interpreta os dados (read-only)

---

## 👥 Usuários

- Diretor do projeto
- Gestor educacional
- Equipe de produção de conteúdo

---

## 📊 Fonte de Dados

GitHub Projects (Kanban)

### Dados utilizados:

- Issues (tarefas)
- Status (To Do, In Progress, Done)
- Assignees (usuários)
- Labels:
  - disciplina
  - ano
- Datas:
  - createdAt
  - closedAt

---

## 🧱 Estrutura de Dados Esperada

Cada issue deve conter:

- 👤 Usuário responsável (assignee)
- 📘 Disciplina (label: disciplina:xxx)
- 🎓 Ano (label: ano:x)
- 📌 Status (kanban)
- 📅 Datas (automáticas do GitHub)

---

## 🎯 Sistema de Metas (Core do Projeto)

### Metas definidas por ano:

| Ano Escolar | Prazo |
|------------|------|
| 2º ano     | Março |
| 3º ano     | Abril |
| 1º ano     | Maio |
| 4º ano     | Junho |
| 5º ano     | Julho |

---

## 📈 Lógica de Comparação de Metas

Para cada ano:

- Total de tarefas planejadas
- Tarefas concluídas
- % de progresso
- Comparação com prazo

### Saída esperada:

- ✅ Dentro da meta
- ⚠️ Risco de atraso
- ❌ Atrasado

---

## ⏱️ Métricas de Tempo

Para cada tarefa:

- Tempo total = closedAt - createdAt
- Tempo médio por usuário
- Tempo médio por disciplina

---

## ⚙️ Funcionalidades

---

### 1. 🔄 Sincronização Automática

- Via GitHub Actions
- Frequência: a cada 5 minutos
- Geração de `data.json`

---

### 2. 📊 Dashboard Geral

- Total de tarefas
- % concluído
- Em andamento
- Distribuição por status

---

### 3. 👤 Performance por Usuário

Para cada usuário:

- Nº de tarefas
- Tarefas concluídas
- Tempo médio por tarefa
- Ranking de produtividade

---

### 4. 📘 Progresso por Disciplina

- Total de tarefas
- % concluído
- Identificação de gargalos

---

### 5. 🎯 Comparação Meta vs Real

Para cada ano:

- Meta definida (prazo)
- Progresso atual
- % atingido
- Gap de execução

---

### 6. 🚨 Identificação de Gargalos

Detectar automaticamente:

- Usuários com baixa performance
- Tarefas com tempo acima da média
- Disciplinas atrasadas
- Etapas travadas

---

### 7. 🧠 Motor de Inteligência

Gerar insights automáticos como:

- "Usuário X está 35% mais lento que a média"
- "Disciplina Y está atrasada"
- "Equipe precisa acelerar 20% para cumprir meta"

---

### 8. 📊 Visualizações

#### Cards
- Progresso geral
- Meta atual
- Status geral

#### Gráficos
- Barras → disciplinas
- Barras → usuários
- Linha → progresso no tempo

#### Tabelas
- Usuário vs performance
- Disciplina vs progresso

#### Insights
- Lista automática de alertas e análises

---

## 🧠 Regras de Negócio

- 1 issue = 1 tarefa
- Status "Done" = concluído
- Tempo = createdAt → closedAt
- Labels definem contexto (disciplina / ano)
- Assignee define responsável

---

## 🔄 Fluxo de Dados

GitHub Projects
        ↓
GitHub API (read-only)
        ↓
Script (sync.js)
        ↓
data.json
        ↓
Dashboard (GitHub Pages)

---

## 🧩 Arquitetura Técnica

### Frontend
- HTML + JS
- Chart.js (gráficos)
- Hospedagem: GitHub Pages

---

### Backend (serverless)

- GitHub Actions:
  - coleta dados
  - processa métricas
  - gera JSON

---

## 📁 Estrutura do Projeto

/docs
  ├── index.html
  ├── app.js
  ├── styles.css
  └── data.json

/scripts
  └── sync.js

/.github/workflows
  └── sync.yml

---

## 🔐 Segurança

- Uso de GITHUB_TOKEN (read-only)
- Token nunca exposto no frontend
- Processamento via Actions

---

## 📊 KPIs

- % de conclusão por ano
- Tempo médio por tarefa
- Produtividade por usuário
- Aderência às metas
- Gargalos identificados

---

## 🚀 Roadmap

### Fase 1 — MVP
- Integração com GitHub
- Dashboard básico
- Metas por ano

---

### Fase 2
- Análise por usuário
- Tempo por tarefa
- Comparação meta vs real

---

### Fase 3
- Insights automáticos
- Detecção de gargalos
- Alertas inteligentes

---

## 🧭 Resultado Esperado

- Visão executiva clara
- Controle total da operação
- Identificação rápida de problemas
- Aceleração da produção de aulas
- Base para decisões estratégicas

---

## 🔥 Diferencial do Sistema

Este sistema atua como:

→ Um analista automático da operação  
→ Um radar de produtividade  
→ Um motor de decisão baseado em dados  

---

## ✅ Pronto para Antigravity

Este PRD pode ser usado para:

- Criar skills de análise
- Alimentar pipelines de IA
- Gerar automações
- Criar dashboards inteligentes