# 🔍 Researcher Agent - Documentação Completa

**Agente de Pesquisa e Coleta de Informações - Etapa 1 do Fluxo Editorial**

---

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Objetivo](#objetivo)
3. [Comandos Disponíveis](#comandos-disponíveis)
4. [Exemplos de Uso](#exemplos-de-uso)
5. [Metodologia de Pesquisa](#metodologia-de-pesquisa)
6. [Banco de Autores](#banco-de-autores)
7. [Estrutura do Relatório](#estrutura-do-relatório)
8. [Casos de Uso](#casos-de-uso)
9. [FAQ](#faq)

---

## Visão Geral

| Propriedade | Valor |
|-------------|-------|
| **Nome** | Researcher |
| **Tipo** | Pesquisador |
| **Escopo** | Editorial Squad |
| **Status** | ✅ Ativo |
| **Versão** | 1.0 |
| **Etapa** | 1 (primeira) |

---

## Objetivo

O **Researcher** é o **Investigador** da Squad Editorial. Sua missão é coletar informações profundas, autoritárias e alinhadas à metodologia da Educação Clássica Cristã Reformada para a criação de uma nova aula.

**Quando usar:**
- Criando uma aula nova (Etapa 1 do fluxo)
- Precisa de pesquisa de conteúdo
- Busca definições, obras de arte, referências literárias
- Necessita de versículos bíblicos e recursos multimídia

---

## Comandos Disponíveis

### **1. `/research <tema> <ano> <semana>`**

**Descrição:** Inicia pesquisa completa para uma aula específica.

**Sintaxe:**
```bash
/research <tema> <ano> <semana>
```

**Parâmetros:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `tema` | string | ✅ | Tema da aula (ex: "Arte Barroca") |
| `ano` | number | ✅ | Ano escolar (1-5) |
| `semana` | number | ✅ | Número da semana (1-40) |

**Exemplo:**
```bash
/research "Arte Barroca" 4 12
```

**Saída:**
```markdown
# 🔍 Relatório de Pesquisa — Semana 12, 4º Ano

## Tema: Arte Barroca

### 1. Definir
- **Termo:** Barroco
- **Webster 1828:** "Irregular, bizarre, unequal"
- **Etimologia:** Português "barroco" = pérola irregular
- **Definição:** Estilo artístico do século XVII caracterizado por...

### 2. Perceber
- **Obras sugeridas:**
  - Caravaggio: "A Vocação de São Mateus"
  - Bernini: "Êxtase de Santa Teresa"
  - Rembrandt: "A Ronda Noturna"

### 3. Recordar
- **Versículo:** Salmos 96:9 "Adorai o Senhor na beleza da santidade"
- **Poema:** George Herbert - "The Beauty"
- **Música:** Bach - "Toccata and Fugue in D minor"

### 4. Praticar
- Atividade: Comparar arte renascentista vs barroca
- Exercício: Identificar características do Barroco

### 5. Narrar
- **Autor:** John Ruskin
- **Trecho:** "The Stones of Venice" (cap. sobre Barroco)
```

---

### **2. `/research definition <termo>`**

**Descrição:** Pesquisa definição Webster 1828 para um termo específico.

**Sintaxe:**
```bash
/research definition <termo>
```

**Parâmetros:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `termo` | string | ✅ | Termo a definir |

**Exemplo:**
```bash
/research definition "Barroco"
```

**Saída:**
```markdown
## Definição — Barroco

**Webster's 1828 Dictionary:**
> Baroque: Irregular, bizarre, unequal, said of a style of art

**Etimologia:**
- Português: "barroco" = pérola irregular
- Francês: "baroque" = estranho, extravagante

**Definição Pedagógica:**
Estilo artístico do século XVII caracterizado por dramaticidade, contraste, movimento e ornamentação elaborada.
```

---

### **3. `/research artwork <tema>`**

**Descrição:** Encontra obras de arte relacionadas ao tema.

**Sintaxe:**
```bash
/research artwork <tema>
```

**Parâmetros:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `tema` | string | ✅ | Tema para busca de arte |

**Exemplo:**
```bash
/research artwork "Arte Cristã Primitiva"
```

**Saída:**
```markdown
## Obras de Arte — Arte Cristã Primitiva

### Catacumbas
- **Catacomb of Priscilla**: Frescos do século II
- **Catacomb of Callixtus**: Símbolos cristãos primitivos

### Mosaicos Bizantinos
- **Hagia Sophia**: Cristo Pantocrator
- **San Vitale, Ravenna**: Imperador Justiniano

### Ícones
- **Saint Catherine's Monastery**: Ícones do século VI
- **Ícone da Virgem de Vladimir**: Século XII
```

---

### **4. `/research scripture <tema>`**

**Descrição:** Encontra versículos bíblicos relacionados ao tema.

**Sintaxe:**
```bash
/research scripture <tema>
```

**Exemplo:**
```bash
/research scripture "Beleza"
```

**Saída:**
```markdown
## Versículos — Beleza

### Antigo Testamento
- **Salmos 27:4** "Contemplar a beleza do Senhor"
- **Salmos 96:9** "Adorai na beleza da santidade"
- **Provérbios 31:30** "Enganosa é a beleza, mas a mulher que teme ao Senhor será louvada"

### Novo Testamento
- **1 Pedro 3:3-4** "Não o enfeite exterior... mas o homem interior do coração"
- **Filipenses 4:8** "Tudo o que é belo, nisso pensai"
```

---

## Metodologia de Pesquisa

### **1. Ad Fontes (Às Fontes)**

Priorize sempre:
- ✅ Fontes primárias
- ✅ Referências clássicas
- ✅ Autores originais
- ❌ Interpretações secundárias
- ❌ Resumos modernos

---

### **2. Trivium (Fase Gramática)**

Foco em:
- **Definições** precisas
- **Fatos** verificáveis
- **Memorização** de conteúdo essencial

---

### **3. Cosmovisão Cristã Reformada**

Todo conteúdo deve estar alinhado a:
- ✅ Perspectiva bíblica
- ✅ Teologia reformada
- ✅ Valores cristãos clássicos

---

## Banco de Autores

### **1. Pais da Igreja**

Use para: **fundamento, criação, ordem, beleza e verdade**

| Autor | Obras | Temas |
|-------|-------|-------|
| **Agostinho** | Confissões, Cidade de Deus | Memória, tempo, interioridade |
| **Basílio** | Homilias sobre a Criação | Natureza, harmonia |
| **Gregório de Nissa** | A Vida de Moisés | Ascensão espiritual |
| **João Crisóstomo** | Homilias | Retórica, clareza visual |
| **Irineu** | Contra as Heresias | Encarnação, forma |

---

### **2. Puritanos**

Use para: **disciplina, forma interior, contraste moral**

| Autor | Estilo |
|-------|--------|
| **John Owen** | Profundo, introspectivo |
| **Richard Baxter** | Imagens pastorais |
| **Thomas Watson** | Metáforas claras, didático |
| **John Bunyan** | O Peregrino — alegoria |

---

### **3. Poetas Cristãos**

Use para: **imagem, sensibilidade, emoção**

| Autor | Estilo |
|-------|--------|
| **George Herbert** | Metáforas visuais precisas |
| **John Milton** | Paraíso Perdido — épico |
| **Christina Rossetti** | Delicadeza, simbolismo |
| **Gerard Manley Hopkins** | Ritmo, natureza |

---

### **4. Artistas Visuais**

Use para: **composição, luz, materialidade**

| Autor | Estilo |
|-------|--------|
| **Giotto** | Narrativa visual |
| **Caravaggio** | Contraste, drama |
| **Rembrandt** | Interioridade, sombra |
| **Caspar David Friedrich** | Paisagem, transcendência |

---

## Estrutura do Relatório

### **Template Padrão**

```markdown
# 🔍 Relatório de Pesquisa — [Tema]

## 1. Definir
- **Termo:** [nome]
- **Webster 1828:** [definição]
- **Etimologia:** [origem]
- **Definição Pedagógica:** [paráfrase]

## 2. Perceber
- **Obras de arte:** [lista com links]
- **Imagens sugeridas:** [descrição]

## 3. Recordar
- **Versículo-chave:** [citação]
- **Poema/Hino:** [nome + autor]
- **Música:** [compositor + obra]

## 4. Praticar
- **Atividade 1:** [descrição]
- **Atividade 2:** [descrição]

## 5. Narrar
- **Autor:** [nome]
- **Obra:** [título]
- **Trecho:** [citação]
```

---

## Exemplos de Uso

### **Cenário 1: Pesquisa Completa**

```bash
@researcher "Pesquise para a aula 3.2 sobre Renascimento, 3º ano"
```

**Resposta:**
```markdown
# 🔍 Pesquisa — Renascimento, Semana 3

## 1. Definir
- **Termo:** Renascimento
- **Webster 1828:** "Rebirth, revival"
- **Etimologia:** Francês "re-" + "naissance" = nascer de novo

## 2. Perceber
- **Obras:**
  - Da Vinci: "Mona Lisa", "Última Ceia"
  - Michelangelo: "Davi", "Teto da Capela Sistina"
  - Rafael: "Escola de Atenas"

## 3. Recordar
- **Versículo:** 2 Coríntios 5:17 "Eis que faço novas todas as coisas"
- **Poema:** Dante Alighieri - "Divina Comédia"

## 4. Praticar
- Compare arte medieval vs renascentista
- Identifique características humanistas

## 5. Narrar
- **Autor:** Giorgio Vasari
- **Obra:** "Vidas dos Artistas"
- **Trecho:** Sobre Michelangelo...
```

---

### **Cenário 2: Apenas Definição**

```bash
@researcher "Preciso da definição Webster de 'Simetria'"
```

**Resposta:**
```markdown
## Definição — Simetria

**Webster's 1828:**
> Symmetry: Just proportion of parts; harmony; agreement

**Etimologia:**
- Grego: "syn-" (junto) + "metron" (medida)

**Definição Pedagógica:**
Proporção justa e harmoniosa entre as partes de um todo.
```

---

### **Cenário 3: Obras de Arte**

```bash
@researcher "Quais obras de arte usar para Arte Bizantina?"
```

**Resposta:**
```markdown
## Obras — Arte Bizantina

### Mosaicos
1. **Hagia Sophia, Istambul**
   - Cristo Pantocrator (cúpula)
   - Imperatriz Teodora (San Vitale)

### Ícones
2. **Ícone da Virgem de Vladimir**
   - Século XII, Constantinopla

3. **Ícones do Monte Sinai**
   - Século VI, mais antigos existentes

### Arquitetura
4. **Basílica de São Marcos, Veneza**
   - Cúpulas bizantinas

5. **San Vitale, Ravenna**
   - Mosaicos de Justiniano
```

---

## Casos de Uso

### **1. Writer (Etapa 2)**

**Objetivo:** Receber pesquisa pronta para redação

**Comando:**
```bash
@researcher "Pesquise para aula 5.4 sobre Barroco, 5º ano"
```

**Benefícios:**
- Recebe conteúdo estruturado
- Economiza tempo de pesquisa
- Garante qualidade das fontes

---

### **2. Planner Curricular**

**Objetivo:** Planejar conteúdo do bimestre

**Comando:**
```bash
@researcher "Quais autores usar para todo o Bimestre 3?"
```

**Benefícios:**
- Visão consolidada
- Evita repetição
- Garante diversidade

---

### **3. Revisão de Conteúdo**

**Objetivo:** Verificar precisão de definições

**Comando:**
```bash
@researcher "Confirme a definição de 'Gótico' no Webster 1828"
```

**Benefícios:**
- Validação de fontes
- Precisão terminológica
- Consistência doutrinária

---

## FAQ

### **P: Qual a diferença entre Researcher e Writer?**
**R:** O **Researcher** coleta informações. O **Writer** transforma em conteúdo pedagógico.

---

### **P: O Researcher formata em Rise Blocks?**
**R:** Não! Ele gera um relatório em Markdown puro. O **Standardizer** (Etapa 3) faz a formatação Rise.

---

### **P: Como sei quais autores usar?**
**R:** Consulte o **Banco de Autores** nesta documentação. Cada categoria tem autores específicos por tema.

---

### **P: O que é Webster 1828?**
**R:** Dicionário de Noah Webster (1828), valorizado por definições com referências bíblicas e morais.

---

### **P: Posso usar fontes modernas?**
**R:** Sim, mas priorize fontes clássicas. Fontes modernas devem ser complementares, não primárias.

---

## Links Úteis

- [Skill Definition](SKILL.md)
- [Webster's 1828 Dictionary](https://webstersdictionary1828.com/)
- [Knowledge Base](../knowledge-base/)
- [Workflow de Aula](../workflows/produce_class.md)

---

**Gerado por:** Editorial Squad  
**Data:** 2026-04-01  
**Versão:** 1.0

---

> "Ad Fontes — Às fontes! Volte sempre às fontes originais para encontrar a verdade."
