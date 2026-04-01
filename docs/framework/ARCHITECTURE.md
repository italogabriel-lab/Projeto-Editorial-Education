# 🏗️ BEF Architecture

**Arquitetura do Bibline Editorial Framework**

---

## Visão Geral da Arquitetura

```
┌────────────────────────────────────────────────────────────────┐
│                    Bibline Editorial Framework                  │
│                           (BEF)                                 │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Agents     │  │  Workflows   │  │  Templates   │         │
│  │   (20)       │  │   (7)        │  │   (3)        │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ Knowledge    │  │   Scripts    │  │   Vision     │         │
│  │   Base       │  │   (Auto)     │  │   Board      │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                 │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  GitHub Projects ←→ GitHub Actions ←→ GitHub Pages             │
│     (Kanban)         (Auto-Sync)      (Dashboard)               │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

---

## Componentes Principais

### **1. Agents Layer**

Camada de agentes especializados que executam tarefas específicas.

**Categorias:**
- **Core:** 6 agentes do fluxo principal
- **Specialized:** 4 agentes de suporte
- **Analytics:** 4 agentes de análise
- **Bimester:** 2 agentes bimestrais
- **Legacy:** 4 agentes legados

**Responsabilidades:**
- Cada agente tem uma responsabilidade única
- Comunicação via comandos padronizados
- Documentação completa em README.md

---

### **2. Workflows Layer**

Orquestração dos agentes em sequências de produção.

**Workflows Principais:**
1. **produce_class.md:** 7 etapas de produção
2. **publish.md:** Publicação no GitHub
3. **sync.md:** Sincronização de dados

**Características:**
- Sequenciais e paralelizáveis
- Gatilhos manuais e automáticos
- Rollback em caso de erro

---

### **3. Templates Layer**

Estruturas padronizadas de conteúdo.

**Templates:**
- **padrao_final_aula.md:** Golden Template
- **provas-bimestrais.md:** Provas
- **revisoes.md:** Revisões

**Benefícios:**
- Consistência de conteúdo
- Redução de tempo de produção
- Qualidade padronizada

---

### **4. Knowledge Base Layer**

Base de conhecimento e regras do framework.

**Documentos:**
- **visao-geral-fluxo-editorial.md:** Pipeline
- **doutrina-pedagogica.md:** Fundamentos
- **guia-de-estilo.md:** Estilo e tom
- **rise-blocks-reference.md:** Rise 360

---

### **5. Scripts Layer**

Automação de tarefas repetitivas.

**Scripts:**
- **sync_titles.py:** Sincroniza títulos
- **generate_descriptions.py:** Gera descrições

**Execução:**
- Manual via terminal
- Automática via GitHub Actions
- Agendada por cron

---

### **6. Analytics Layer (Vision Board)**

Dashboard de métricas e acompanhamento.

**Componentes:**
- **public/data.json:** Dados do Kanban
- **public/app.js:** Lógica do dashboard
- **public/metas.js:** Metas e progresso
- **public/sidebar.js:** Sidebar colapsável

**Métricas:**
- Produção por autor
- Progresso por disciplina
- Gargalos no pipeline
- Lead time e throughput

---

## Fluxo de Dados

```
┌─────────────┐
│   GitHub    │
│   Projects  │
└──────┬──────┘
       │
       ↓ (GraphQL API)
┌─────────────┐
│  data-sync  │
│   (Action)  │
└──────┬──────┘
       │
       ↓ (Write)
┌─────────────┐
│  data.json  │
└──────┬──────┘
       │
       ↓ (Read)
┌─────────────┐
│   Vision    │
│   Board     │
└─────────────┘
```

---

## Padrões de Projeto

### **1. Agent Pattern**

Cada agente segue o padrão:

```
agent-name/
├── SKILL.md      # Definição do agente
├── README.md     # Documentação completa
└── examples/     # Exemplos (opcional)
```

### **2. Command Pattern**

Comandos padronizados:

```bash
/agent-name <command> <parameters>
```

### **3. Workflow Pattern**

Workflows em Markdown:

```markdown
# Workflow Name

## Steps
1. Step 1
2. Step 2
3. Step 3

## Output
- Result
```

---

## Integrações

### **GitHub Integration**

- **Projects:** Kanban board
- **Actions:** CI/CD pipeline
- **Pages:** Static hosting
- **API:** GraphQL para dados

### **Rise 360 Integration**

- **Blocks:** Tags Markdown → Rise
- **Export:** HTML/SCORM
- **Import:** Atualização de conteúdo

---

## Segurança

### **Access Control**

- **GitHub Token:** PAT com escopos limitados
- **Secrets:** Variáveis de ambiente criptografadas
- **Permissions:** Least privilege principle

### **Data Protection**

- **Backup:** Git versionamento
- **Recovery:** Rollback via git revert
- **Audit:** Git history completo

---

## Performance

### **Otimizações**

- **Cache:** Node modules e dados
- **Parallel:** Workflows paralelizáveis
- **Incremental:** Sync apenas de mudanças

### **SLA**

- **Sync:** 5 minutos (automático)
- **Deploy:** 1-2 minutos
- **Dashboard:** < 3 segundos

---

## Escalabilidade

### **Horizontal**

- Mais autores → Mais produção
- Agents stateless → Paralelização
- GitHub Actions → Auto-scaling

### **Vertical**

- Agents especializados → Melhor qualidade
- Templates → Consistência
- Knowledge Base → Aprendizado

---

## Monitoramento

### **Metrics**

- **Production:** Aulas/semana
- **Quality:** Revisões/approved
- **Velocity:** Lead time
- **Bottlenecks:** Status com acúmulo

### **Alerts**

- **Atraso:** < 50% da meta
- **Gargalo:** > 20 tickets em review
- **Erro:** Workflow failure

---

## Versionamento

### **Semantic Versioning**

```
MAJOR.MINOR.PATCH
   │      │      │
   │      │      └─ Bug fixes (backward compatible)
   │      └─ New features (backward compatible)
   └─ Breaking changes
```

### **Release Cycle**

- **Major:** Quarterly
- **Minor:** Monthly
- **Patch:** Weekly

---

## Roadmap

### **Q2 2026**
- [ ] 100% documentation coverage ✅
- [ ] Automated testing
- [ ] Performance optimization

### **Q3 2026**
- [ ] New agents (Video, Audio)
- [ ] Mobile dashboard
- [ ] Integration with LMS

### **Q4 2026**
- [ ] AI-assisted production
- [ ] Multi-language support
- [ ] Advanced analytics

---

**Versão:** 1.0  
**Última atualização:** 2026-04-01  
**Status:** ✅ Production Ready
