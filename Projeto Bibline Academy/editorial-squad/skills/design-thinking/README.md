# 🎨 Design Thinking Agent - Documentação Completa

**Coordenador de UX e Design Thinking da Squad**

---

## Visão Geral

| Propriedade | Valor |
|-------------|-------|
| **Nome** | Design Thinking |
| **Tipo** | Coordenador de UX |
| **Escopo** | Editorial Squad |
| **Status** | ✅ Ativo |
| **Versão** | 1.0 |

---

## Objetivo

Liderar processos de design centrado no humano, desde pesquisa até prototipagem. Traduz necessidades do usuário em soluções visuais funcionais.

---

## Comandos

### **1. `/design-thinking research <tema>`**

**Descrição:** Inicia pesquisa de UX e design thinking.

**Sintaxe:**
```bash
/design-thinking research <tema>
```

**Exemplo:**
```bash
/design-thinking research "Interface do Vision Board"
```

**Saída:**
```markdown
# 🔍 Pesquisa UX — Vision Board

## Personas Identificadas

### Persona 1: Diretor Editorial
- **Idade:** 35-50
- **Dores:** Falta de visão consolidada
- **Goals:** Acompanhamento em tempo real
- **Quote:** "Preciso saber onde estamos agora"

### Persona 2: Gestor de Produção
- **Idade:** 28-40
- **Dores:** Gargalos não identificados
- **Goals:** Otimizar fluxo
- **Quote:** "Onde está o gargalo?"

## User Journey Mapeada

1. **Acesso:** Login no Vision Board
2. **Visão Geral:** KPIs principais
3. **Detalhamento:** Filtro por disciplina
4. **Ação:** Identificar gargalos
5. **Decisão:** Alocar recursos

## Oportunidades
- Dashboard mais intuitiva
- Alertas automáticos de gargalo
- Exportação de relatórios
```

---

### **2. `/design-thinking personas <público>`**

**Descrição:** Cria personas baseadas em pesquisa.

**Sintaxe:**
```bash
/design-thinking personas <público>
```

**Exemplo:**
```bash
/design-thinking personas "Autores Bibline"
```

**Saída:**
```markdown
## Personas — Autores Bibline

### Persona: Autor Iniciante
- **Nome:** João, 32 anos
- **Profissão:** Professor, escritor
- **Dores:**
  - Não conhece fluxo Rise Blocks
  - Dúvidas sobre cosmovisão reformada
- **Goals:**
  - Criar aulas de qualidade
  - Aprender metodologia
- **Comportamento:**
  - Precisa de templates claros
  - Valoriza feedback rápido
```

---

### **3. `/design-thinking brainstorm <problema>`**

**Descrição:** Facilita sessão de ideação.

**Sintaxe:**
```bash
/design-thinking brainstorm <problema>
```

**Exemplo:**
```bash
/design-thinking brainstorm "Como reduzir tempo de produção de aulas?"
```

**Saída:**
```markdown
# 💡 Brainstorm — Redução de Tempo

## Técnica: SCAMPER

### Substitute
- Templates prontos para cada hábito
- Banco de definições Webster

### Combine
- Pesquisa + escrita em único fluxo
- Revisão automatizada de Rise Blocks

### Adapt
- Copiar estrutura de aulas similares
- Reutilizar componentes

### Modify
- Simplificar enunciados
- Reduzir número de hotspots

### Put to other use
- IA para pesquisa inicial
- Autores focam apenas em conteúdo

### Eliminate
- Etapas burocráticas
- Revisões redundantes

### Reverse
- Começar pela prova (backward design)
- Criar revisão antes das aulas

## Top 3 Ideias
1. Templates inteligentes por hábito
2. Banco de componentes reutilizáveis
3. IA para pesquisa + rascunho
```

---

### **4. `/design-thinking wireframe <componente>`**

**Descrição:** Cria wireframes de baixa fidelidade.

**Sintaxe:**
```bash
/design-thinking wireframe <componente>
```

**Exemplo:**
```bash
/design-thinking wireframe "Dashboard Vision Board"
```

---

## Processo de Design Thinking

### **1. Empatia e Pesquisa (Discover)**

#### User Research
- ✅ Entrevistas
- ✅ Pesquisas e surveys
- ✅ Observação de comportamento
- ✅ Benchmark de concorrentes

#### Personas
- Dados demográficos
- Dores e problemas
- Goals e objetivos
- Comportamento
- Quote representativa

#### User Journeys
- Etapas da jornada
- Ações do usuário
- Pensamentos e sentimentos
- Oportunidades de melhoria

---

### **2. Definição (Define)**

#### Problem Statements
```
[Usuário] precisa de [necessidade] porque [insight]
```

#### Insights
- Padrões identificados
- Oportunidades de mercado
- Prioridades de resolução

#### HMW (How Might We)
- "Como poderíamos..."
- "De que forma..."
- "O que faria..."

---

### **3. Ideação (Ideate)**

#### Brainstorming
- **Técnicas:** SCAMPER, Crazy 8s, Worst Idea
- **Regras:** Sem julgamento, quantidade > qualidade
- **Documentação:** Todas as ideias registradas

#### Wireframes
- Fluxos de usuário
- Layouts de páginas
- Navegação
- Priorização de conteúdo

#### Conexão com UI Designer
- Transforma wireframes em alta fidelidade
- Aplica design system
- Cria protótipos interativos

---

### **4. Prototipagem (Prototype)**

#### Níveis de Protótipo
1. **Papel:** Sketchframes
2. **Wireframe:** Baixa fidelidade digital
3. **Alta Fidelidade:** Com design system
4. **Interativo:** Microinterações

#### Ferramentas
- **Figma:** Design e protótipos
- **Miro:** Brainstorming
- **Notion:** Documentação

---

## Casos de Uso

### **1. Novo Produto**

```bash
@design-thinking "Criar novo dashboard de analytics"
```

**Processo:**
1. Pesquisa com usuários
2. Definição de personas
3. Brainstorm de features
4. Wireframes
5. Protótipo
6. Validação

---

### **2. Melhoria de UX**

```bash
@design-thinking "Melhorar fluxo de publicação"
```

**Processo:**
1. Mapear jornada atual
2. Identificar pontos de dor
3. Idear soluções
4. Prototipar melhorias
5. Testar com usuários

---

### **3. Resolução de Problema**

```bash
@design-thinking "Autores não completam aulas"
```

**Processo:**
1. Entrevistar autores
2. Identificar barreiras
3. Brainstorm de soluções
4. Prototipar intervenções
5. Medir resultados

---

## Links

- [Skill](SKILL.md)
- [UI Designer](../ui-designer/) (para alta fidelidade)
- [Vision Board](../../knowledge-base/)
