# 🚀 Bibline Editorial Framework (BEF)

**Framework de Produção Editorial para Educação Cristã Clássica**

> *"Excelência em produção de conteúdo educacional alinhada à cosmovisão cristã reformada"*

---

## 📋 Visão Geral

O **Bibline Editorial Framework (BEF)** é um framework completo de produção editorial que orquestra agentes especializados, workflows automatizados e templates padronizados para criar conteúdo educacional de alta qualidade baseado na metodologia do Trivium e Educação Clássica Cristã.

---

## 🎯 Objetivo

Prover uma estrutura escalável e reproduzível para:

- ✅ Produção de aulas no formato Rise 360
- ✅ Revisão e padronização de conteúdo
- ✅ Gestão de pipeline editorial
- ✅ Analytics e acompanhamento de produção
- ✅ Automação de workflows via GitHub Actions

---

## 🏗️ Arquitetura do Framework

```
bef/ (Bibline Editorial Framework)
│
├── core/                    # Núcleo do framework
│   ├── README.md           # Documentação do core
│   └── constants.js        # Constantes e configurações
│
├── agents/                  # Todos os 20 agentes
│   ├── core/               # 6 agentes do fluxo principal
│   │   ├── orchestrator/
│   │   ├── researcher/
│   │   ├── writer/
│   │   ├── standardizer/
│   │   ├── reviewer/
│   │   └── publisher/
│   │
│   ├── specialized/        # 4 agentes especializados
│   │   ├── copywriter/
│   │   ├── design-thinking/
│   │   ├── ui-designer/
│   │   └── devops/
│   │
│   ├── analytics/          # 4 agentes de analytics (Vision Board)
│   │   ├── performance-analytics/
│   │   ├── vision-progress-engine/
│   │   ├── vision-bottleneck-detector/
│   │   └── vision-github-analyzer/
│   │
│   ├── bimester/           # 2 agentes bimestrais
│   │   ├── bimester-exam-builder/
│   │   └── bimester-review-builder/
│   │
│   └── legacy/             # 4 agentes legados
│       ├── capitalizer/
│       ├── exam-builder/
│       ├── image-link-extractor/
│       └── review-builder/
│
├── workflows/              # Workflows editoriais
│   ├── produce_class.md    # Workflow de produção de aula
│   ├── publish.md          # Workflow de publicação
│   └── sync.md             # Workflow de sincronização
│
├── templates/              # Templates de conteúdo
│   ├── padrao_final_aula.md
│   ├── provas-bimestrais.md
│   └── revisoes.md
│
├── knowledge-base/         # Base de conhecimento
│   ├── visao-geral-fluxo-editorial.md
│   ├── doutrina-pedagogica.md
│   ├── guia-de-estilo.md
│   └── rise-blocks-reference.md
│
└── scripts/                # Scripts de automação
    ├── sync_titles.py
    └── generate_descriptions.py
```

---

## 🔄 Fluxo Editorial Principal

O BEF opera em **7 etapas** sequenciais:

```
┌─────────────────────────────────────────────────────────────┐
│                    FLUXO EDITORIAL                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1️⃣  Orchestrator   → Diagnóstico e delegação              │
│       ↓                                                     │
│  2️⃣  Researcher     → Pesquisa de conteúdo                 │
│       ↓                                                     │
│  3️⃣  Writer         → Redação da aula                      │
│       ↓                                                     │
│  4️⃣  Standardizer   → Padronização Rise Blocks             │
│       ↓                                                     │
│  5️⃣  Reviewer       → Revisão e QA                         │
│       ↓                                                     │
│  6️⃣  Copywriter     → Polimento final                      │
│       ↓                                                     │
│  7️⃣  Publisher      → Publicação no GitHub                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Agentes do Framework

### **Core Agents (Fluxo Principal)**

| Agente | Etapa | Função | Status |
|--------|-------|--------|--------|
| **Orchestrator** | Transversal | Diretor editorial, diagnostica e delega | ✅ Ativo |
| **Researcher** | 1 | Pesquisa e coleta de informações | ✅ Ativo |
| **Writer** | 2 | Redação de conteúdo didático | ✅ Ativo |
| **Standardizer** | 3 | Padronização e formatação Rise Blocks | ✅ Ativo |
| **Reviewer** | 4 | Revisão e QA editorial | ✅ Ativo |
| **Publisher** | 7 | Publicação e distribuição | ✅ Ativo |

---

### **Specialized Agents**

| Agente | Função | Status |
|--------|--------|--------|
| **Copywriter** | Polimento final e otimização (Etapa 5) | ✅ Ativo |
| **Design Thinking** | Coordenador de UX e pesquisa | ✅ Ativo |
| **UI Designer** | Design systems premium e responsivo | ✅ Ativo |
| **DevOps** | Gatekeeper de repositório e GitHub | ✅ Ativo |

---

### **Analytics Agents (Vision Board)**

| Agente | Função | Status |
|--------|--------|--------|
| **Performance Analytics** | Análise de performance da equipe | ✅ Ativo |
| **Vision Progress Engine** | Motor de progresso do Vision Board | ✅ Ativo |
| **Vision Bottleneck Detector** | Detector de gargalos | ✅ Ativo |
| **Vision GitHub Analyzer** | Análise de dados do GitHub | ✅ Ativo |

---

### **Bimester Agents**

| Agente | Função | Status |
|--------|--------|--------|
| **Bimester Exam Builder** | Construtor de provas bimestrais | ✅ Ativo |
| **Bimester Review Builder** | Construtor de revisões bimestrais | ✅ Ativo |

---

### **Legacy Agents**

| Agente | Função | Status | Substituído Por |
|--------|--------|--------|-----------------|
| **Capitalizer** | Especialista em capitalização | ⚠️ Legacy | - |
| **Exam Builder** | Construtor de quizzes | ⚠️ Legacy | Bimester Exam Builder |
| **Image Link Extractor** | Extrator de imagens | ⚠️ Legacy | - |
| **Review Builder** | Construtor de revisões | ⚠️ Legacy | Bimester Review Builder |

---

## 🎓 Metodologia Pedagógica

O BEF é fundamentado em:

### **1. Trivium Clássico**
- **Gramática:** Fatos, definições, memorização
- **Lógica:** Relações, raciocínio, entendimento
- **Retórica:** Expressão, aplicação, sabedoria

### **2. Cosmovisão Cristã Reformada**
- Centralidade de Deus
- Autoridade das Escrituras
- Educação como discipulado
- Excelência como adoração

### **3. 5 Hábitos da Gramática**
1. **Definir** - Webster 1828, etimologia
2. **Perceber** - Imagens, obras de arte
3. **Recordar** - Versículo, poema, música
4. **Praticar** - Atividades, exercícios
5. **Narrar** - Trecho literário

---

## 🛠️ Como Usar o Framework

### **1. Iniciar Produção de Aula**

```bash
# Passo 1: Diagnosticar com Orchestrator
@orchestrator "Status do 3º ano"

# Passo 2: Pesquisar com Researcher
@researcher "Pesquise para aula 5.3 sobre Barroco, 5º ano"

# Passo 3: Redigir com Writer
@writer "Crie aula 5.3 sobre Barroco, 5º ano"

# Passo 4: Padronizar com Standardizer
@standardizer "formate aula 5.3"

# Passo 5: Revisar com Reviewer
@reviewer "revise aula 5.3"

# Passo 6: Polir com Copywriter
@copywriter "polir aula 5.3"

# Passo 7: Publicar com Publisher
@publisher "publicar aula 5.3, 5º ano"
```

---

### **2. Analytics e Performance**

```bash
# Relatório de performance individual
/performance user Italo-bibline Belas Artes 2

# Relatório de disciplina
/performance discipline Matemática 2

# Relatório de equipe
/performance team

# Detectar gargalos
/bottleneck detect
```

---

### **3. Workflows Automatizados**

```bash
# Sincronizar Vision Board (automático a cada 5min)
GitHub Actions → data-sync.yml

# Publicar no GitHub
@devops publish

# Limpar repositório
@devops cleanup
```

---

## 📁 Estrutura de Arquivos

### **Templates**

| Template | Uso |
|----------|-----|
| `padrao_final_aula.md` | Template padrão de aula (Golden Template) |
| `provas-bimestrais.md` | Template de provas bimestrais |
| `revisoes.md` | Template de revisões |

---

### **Knowledge Base**

| Arquivo | Conteúdo |
|---------|----------|
| `visao-geral-fluxo-editorial.md` | Regras de pipeline e sincronização |
| `doutrina-pedagogica.md` | Base teológica e filosófica |
| `guia-de-estilo.md` | Tom de voz, métricas, pontuação |
| `rise-blocks-reference.md` | Mapeamento Markdown → Rise 360 |

---

### **Scripts**

| Script | Função |
|--------|--------|
| `sync_titles.py` | Sincroniza títulos entre documentos |
| `generate_descriptions.py` | Gera descrições para tickets |

---

## 🔗 Integrações

### **GitHub Projects**
- Kanban board para gestão de produção
- Issues como tickets de aula
- Labels para disciplina e ano
- Status para estágio no pipeline

### **GitHub Actions**
- Sync automático a cada 5 minutos
- Deploy para GitHub Pages
- Vision Board atualizado em tempo real

### **Rise 360**
- Blocos Rise mapeados para Markdown
- Tags específicas para cada tipo de bloco
- Exportação e importação automatizada

---

## 📊 Métricas do Framework

### **Produção**
- **Meta por disciplina:** 168 aulas/ano
- **Meta por ano:** 840 aulas (5 anos × 168)
- **Meta total:** 4,200 aulas (5 disciplinas × 5 anos × 168)

### **Qualidade**
- **Revisão:** 100% das aulas revisadas
- **Padronização:** 100% em Rise Blocks
- **Conformidade:** 100% com guia de estilo

### **Velocidade**
- **Lead time:** 2-3 dias por aula
- **Throughput:** ~9 aulas/semana por autor
- **Sync:** 5 minutos (automático)

---

##  Princípios de Design

### **1. Modularidade**
- Agentes independentes e especializados
- Cada agente faz uma coisa bem feita
- Fácil substituição e melhoria

### **2. Automatização**
- Workflows repetíveis
- Scripts de automação
- GitHub Actions para deploy

### **3. Documentação**
- 100% dos agentes documentados
- README para cada skill
- Exemplos de uso

### **4. Qualidade**
- Revisão em múltiplas etapas
- QA rigoroso
- Padrões consistentes

### **5. Escalabilidade**
- Estrutura que cresce com a equipe
- Novos agentes podem ser adicionados
- Workflows paralelizáveis

---

## 🚀 Quick Start

### **Para Novos Membros**

1. **Leia a documentação**
   - [AGENTS-DOCUMENTATION.md](docs/agents/AGENTS-DOCUMENTATION.md)
   - [DOCUMENTATION-PLAN.md](docs/agents/DOCUMENTATION-PLAN.md)

2. **Entenda o fluxo**
   - [visao-geral-fluxo-editorial.md](bef/knowledge-base/visao-geral-fluxo-editorial.md)

3. **Configure o ambiente**
   - GitHub CLI
   - Obsidian (opcional)
   - Node.js 20+

4. **Primeira aula**
   ```bash
   @orchestrator "Quero começar uma aula nova"
   ```

---

### **Para Gestores**

1. **Acesse o Vision Board**
   - https://italogabriel-lab.github.io/Projeto-Editorial-Education/

2. **Gere relatórios**
   ```bash
   /performance team
   /bottleneck detect
   ```

3. **Acompanhe métricas**
   - Produção por autor
   - Gargalos no pipeline
   - Progresso por disciplina

---

## 📚 Documentação Completa

### **Framework**
- [Framework Overview](bef/README.md)
- [Architecture](docs/framework/ARCHITECTURE.md)
- [Getting Started](docs/guides/GETTING-STARTED.md)

### **Agentes**
- [Core Agents](bef/agents/core/)
- [Specialized Agents](bef/agents/skills/)
- [Analytics Agents](bef/agents/analytics/)
- [Bimester Agents](bef/agents/bimester/)
- [Legacy Agents](bef/agents/legacy/)

### **Workflows**
- [Produce Class](bef/workflows/produce_class.md)
- [Publish](bef/workflows/publish.md)
- [Sync](bef/workflows/sync.md)

### **Templates**
- [Golden Template](bef/templates/padrao_final_aula.md)
- [Exams](bef/templates/provas-bimestrais.md)
- [Reviews](bef/templates/revisoes.md)

---

## 🤝 Contribuição

### **Como Contribuir**

1. Fork o repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

### **Padrões de Commit**

```
feat: nova funcionalidade
fix: correção de bug
docs: documentação
style: formatação
refactor: refatoração
test: testes
chore: manutenção
```

---

## 👥 Equipe

- **Diretor Editorial:** Orchestrator Agent
- **Autores:** Writer + Researcher
- **Revisores:** Reviewer + Standardizer
- **Designers:** UI Designer + Design Thinking
- **DevOps:** DevOps Agent
- **Analytics:** Performance Analytics

---

## 📞 Suporte

- **Slack:** #editorial-squad
- **GitHub Issues:** https://github.com/italogabriel-lab/Projeto-Editorial-Education/issues
- **Email:** editorial@bibline.com

---

## 📄 Licença

Copyright © 2026 Bibline Academy. Todos os direitos reservados.

---

## 🙏 Agradecimentos

- **Deus** por toda sabedoria e conhecimento
- **Equipe Editorial** por dedicação e excelência
- **Comunidade** por feedback e contribuições

---

> *"Portanto, meus amados irmãos, sede firmes, inabaláveis e sempre abundantes na obra do Senhor, sabendo que o vosso trabalho não é vão no Senhor."* - 1 Coríntios 15:58

---

**Versão:** 1.0  
**Última atualização:** 2026-04-01  
**Status:** ✅ Production Ready

---

## 🔗 Links Rápidos

- [Vision Board](https://italogabriel-lab.github.io/Projeto-Editorial-Education/)
- [GitHub Projects](https://github.com/orgs/bibline/projects/2)
- [Documentation Index](docs/README.md)
- [Agent Commands](docs/agents/COMMANDS.md)
