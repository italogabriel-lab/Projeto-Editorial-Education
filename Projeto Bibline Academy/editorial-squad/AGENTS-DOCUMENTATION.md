# 📚 Editorial Squad - Agentes & Skills

**Documentação Centralizada de Todos os Agentes da Squad Editorial Bibline**

---

## 🎯 Visão Geral

A **Editorial Squad** é composta por agentes especializados que atuam em diferentes etapas do fluxo de produção de conteúdo didático. Cada agente possui skills, comandos e responsabilidades específicas.

---

## 📋 Índice de Agentes

### **Fluxo Editorial Principal**

| # | Agente | Skill | Status | Descrição |
|---|--------|-------|--------|-----------|
| 1 | **Orchestrator** | [📋](#orchestrator) | ✅ Ativo | Diretor editorial — diagnostica e delega |
| 2 | **Researcher** | [🔍](#researcher) | ✅ Ativo | Pesquisa conteúdo e fontes |
| 3 | **Writer** | [✍️](#writer) | ✅ Ativo | Redação de conteúdo didático |
| 4 | **Standardizer** | [📏](#standardizer) | ✅ Ativo | Padronização e formatação |
| 5 | **Reviewer** | [✅](#reviewer) | ✅ Ativo | Revisão e QA editorial |
| 6 | **Publisher** | [🚀](#publisher) | ✅ Ativo | Publicação e deploy |

---

### **Skills Especializados**

| # | Agente | Skill | Status | Descrição |
|---|--------|-------|--------|-----------|
| 7 | **Copywriter** | [📝](#copywriter) | ✅ Ativo | Copy e comunicação |
| 8 | **Designer Thinking** | [🎨](#designer-thinking) | ✅ Ativo | Design pedagógico |
| 9 | **UI Designer** | [🖼️](#ui-designer) | ✅ Ativo | Design de interface |
| 10 | **DevOps** | [⚙️](#devops) | ✅ Ativo | Infra e automação |

---

### **Vision Board Analytics**

| # | Agente | Skill | Status | Descrição |
|---|--------|-------|--------|-----------|
| 11 | **Performance Analytics** | [📊](#performance-analytics) | ✅ Ativo | Análise de performance |
| 12 | **Vision Progress Engine** | [📈](#vision-progress-engine) | ✅ Ativo | Motor de progresso |
| 13 | **Vision Bottleneck Detector** | [⚠️](#vision-bottleneck-detector) | ✅ Ativo | Detector de gargalos |
| 14 | **Vision GitHub Analyzer** | [🔬](#vision-github-analyzer) | ✅ Ativo | Análise do GitHub |

---

### **Bimester Skills**

| # | Agente | Skill | Status | Descrição |
|---|--------|-------|--------|-----------|
| 15 | **Bimester Exam Builder** | [📝](#bimester-exam-builder) | ✅ Ativo | Construtor de provas |
| 16 | **Bimester Review Builder** | [](#bimester-review-builder) | ✅ Ativo | Construtor de revisão |

---

### **Legacy Skills**

| # | Agente | Skill | Status | Descrição |
|---|--------|-------|--------|-----------|
| 17 | **Capitalizer** | [🔠](#capitalizer) | ⚠️ Legacy | Capitalização de termos |
| 18 | **Exam Builder** | [📝](#exam-builder) | ⚠️ Legacy | Construtor de quizzes |
| 19 | **Image Link Extractor** | [🖼️](#image-link-extractor) | ⚠️ Legacy | Extração de imagens |
| 20 | **Review Builder** | [📋](#review-builder) | ⚠️ Legacy | Construtor de revisão |

---

## 📖 Como Usar Esta Documentação

### **Para Usuários Novos**

1. **Entenda o Fluxo:** Comece lendo sobre o **Orchestrator** (agente principal)
2. **Escolha por Função:** Use o índice para encontrar o agente certo para sua necessidade
3. **Siga os Comandos:** Cada agente tem comandos específicos — use os exemplos

---

### **Para Desenvolvedores**

1. **Estrutura de Skills:** Todas as skills seguem o padrão `SKILL.md`
2. **Documentação:** Cada skill deve ter um `README.md` com comandos detalhados
3. **Localização:** `editorial-squad/skills/[nome-da-skill]/`

---

### **Para Gestores**

1. **Visão Geral:** Use esta documentação para entender capacidades da equipe
2. **Métricas:** Consulte **Performance Analytics** para relatórios
3. **Gargalos:** Use **Vision Bottleneck Detector** para identificar problemas

---

## 🎓 Estrutura de Documentação por Agente

Cada agente deve ter:

```
skills/[nome-do-agente]/
├── SKILL.md          # Definição da skill (obrigatório)
├── README.md         # Documentação completa (obrigatório)
├── examples/         # Exemplos de uso (opcional)
└── tests/            # Testes e validações (opcional)
```

---

## 🔗 Links Rápidos

### **Documentação dos Agentes**

- [Orchestrator](#orchestrator) — Diretor editorial
- [Performance Analytics](#performance-analytics) — Análise de performance
- [Writer](#writer) — Redator de conteúdo
- [Reviewer](#reviewer) — Revisor de qualidade
- [Researcher](#researcher) — Pesquisador
- [Standardizer](#standardizer) — Padronizador
- [Publisher](#publisher) — Publicador

---

### **Knowledge Base**

- [Guia de Estilo](../knowledge-base/guia-de-estilo.md)
- [Doutrina Pedagógica](../knowledge-base/doutrina-pedagogica.md)
- [Rise Blocks Reference](../knowledge-base/rise-blocks-reference.md)
- [Visão Geral do Fluxo](../knowledge-base/visao-geral-fluxo-editorial.md)

---

### **Templates**

- [Padrão Final de Aula](../templates/padrao_final_aula.md)
- [Provas Bimestrais](../templates/provas-bimestrais.md)
- [Revisões](../templates/revisoes.md)

---

## 📊 Matriz de Responsabilidades

| Etapa | Agente | Input | Output | Qualidade |
|-------|--------|-------|--------|-----------|
| 1. Diagnóstico | Orchestrator | Pedido do usuário | Plano de ação | ✅ |
| 2. Pesquisa | Researcher | Tema da aula | Relatório de pesquisa | ✅ |
| 3. Redação | Writer | Relatório de pesquisa | Conteúdo formatado | ✅ |
| 4. Padronização | Standardizer | Conteúdo bruto | Conteúdo padronizado | ✅ |
| 5. Revisão | Reviewer | Conteúdo padronizado | Conteúdo revisado | ✅ |
| 6. Publicação | Publisher | Conteúdo final | Aula publicada | ✅ |

---

## 🚀 Primeiros Passos

### **1. Identifique Sua Necessidade**

| Você precisa de... | Use o agente... |
|--------------------|-----------------|
| Direção do projeto | Orchestrator |
| Conteúdo novo | Writer + Researcher |
| Revisão de qualidade | Reviewer |
| Relatório de performance | Performance Analytics |
| Identificar gargalos | Vision Bottleneck Detector |

---

### **2. Consulte a Documentação**

Cada agente tem uma página de documentação completa com:
- Comandos disponíveis
- Exemplos de uso
- Métricas e outputs
- Integrações

---

### **3. Execute o Comando**

Siga a sintaxe exata de cada comando. Exemplo:

```bash
/performance user Italo-bibline Belas Artes 2
```

---

### **4. Analise o Resultado**

Os relatórios são gerados em Markdown e incluem:
- Métricas principais
- Insights acionáveis
- Recomendações
- Links úteis

---

## 📞 Suporte

### **Canais de Comunicação**

- **Slack:** #editorial-squad
- **GitHub:** [Issues do Projeto](https://github.com/italogabriel-lab/Projeto-Editorial-Education/issues)
- **Email:** editorial@bibline.com

---

### **Horário de Atendimento**

- **Segunda a Sexta:** 9h às 18h (BRT)
- **Sábado:** 9h às 12h (BRT)
- **Domingo:** Fechado

---

### **Tempo de Resposta**

- **Urgente:** < 1 hora
- **Normal:** < 4 horas
- **Baixa prioridade:** < 24 horas

---

##  Roadmap de Documentação

### **Fase 1: Foundation** (✅ Completa)
- [x] Criar documentação mestre
- [x] Documentar Performance Analytics
- [x] Estruturar template de documentação

### **Fase 2: Core Agents** (Em andamento)
- [ ] Documentar Orchestrator
- [ ] Documentar Writer
- [ ] Documentar Reviewer
- [ ] Documentar Researcher

### **Fase 3: Specialized Skills** (Planejado)
- [ ] Documentar Vision Board agents
- [ ] Documentar Bimester skills
- [ ] Documentar Legacy skills

### **Fase 4: Integration** (Planejado)
- [ ] Criar índice remissivo
- [ ] Adicionar exemplos interativos
- [ ] Integrar com Slack bot

---

## 🎯 Próximos Passos

1. **Para Usuários:** Escolha um agente do índice e consulte a documentação
2. **Para Desenvolvedores:** Use o template abaixo para documentar novas skills
3. **Para Gestores:** Acompanhe o roadmap e priorize documentações

---

## 📝 Template para Documentação de Agentes

```markdown
# 🎯 [Nome do Agente] - Documentação

## Visão Geral
[Descrição breve do agente]

## Comandos Disponíveis
### `/comando <parametro>`
**Descrição:** [O que faz]
**Sintaxe:** [Como usar]
**Exemplo:** [Exemplo de uso]
**Saída:** [O que retorna]

## Métricas
[Quais métricas o agente usa/gera]

## Integrações
[Com quais sistemas o agente se integra]

## Exemplos de Uso
[Exemplos práticos e casos de uso]

## FAQ
[Perguntas frequentes]
```

---

**Versão:** 1.0  
**Última atualização:** 2026-04-01  
**Próxima revisão:** 2026-05-01  
**Responsável:** Editorial Squad

---

> "Documentação é amor para seu eu do futuro."
