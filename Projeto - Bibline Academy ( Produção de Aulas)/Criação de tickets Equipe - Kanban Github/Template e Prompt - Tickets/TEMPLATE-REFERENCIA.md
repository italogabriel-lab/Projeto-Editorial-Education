# 📋 Template Padrão para Descrições de Tickets

> **Padrão Oficial do Projeto Editorial Education**
> 
> Este documento define o formato padrão para criação de descrições de tickets (GitHub Issues) para todas as disciplinas e anos.

---

## 🎯 Estrutura do Arquivo

### **Cabeçalho (Metadados)**

As informações de atribuição e status ficam **APENAS no cabeçalho**, aplicando-se a **TODOS** os tickets do arquivo:

```markdown
# [Disciplina] - [Ano] Ano

**Disciplina:** [Nome da Disciplina]
**Ano Escolar:** [N]º Ano
**Assignee:** @username-github
**Status:** Backlog
**Total de Tickets:** [quantidade]
**Última Atualização:** YYYY-MM-DD

---
```

### **Corpo (Tickets)**

Cada ticket segue o formato:

```markdown
[Nome da Disciplina] - Ano [N] - [N.N] [Título da Aula]

# Description

[Descrição objetiva do conteúdo em 1 frase, começando com substantivo ou verbo no gerúndio]

---
```

---

## 📝 **Exemplo Completo**

```markdown
# Matemática - 4º Ano

**Disciplina:** Matemática
**Ano Escolar:** 4º Ano
**Assignee:** @deborafeijo-gif
**Status:** Backlog
**Total de Tickets:** 200
**Última Atualização:** 2026-04-02

---

[Matemática] - Ano 4 - 1.1 Números até 10.000

# Description

Reconhecimento e leitura de números naturais até 10.000.

---

[Matemática] - Ano 4 - 1.2 Decompor números de quatro ordens

# Description

Decomposição de números de quatro ordens em unidades, dezenas, centenas e milhares.

---

[Matemática] - Ano 4 - 1.3 Números na reta

# Description

Localização de números naturais em reta numérica.

---

[Matemática] - Ano 4 - 1.4 Revisão

# Description

Revisão dos conhecimentos das três semanas anteriores.

---

[Matemática] - Ano 4 - 1.5 Prova

# Description

Avaliação dos conhecimentos das três semanas anteriores.

---
```

---

## 📊 **Regras de Formatação**

### **1. Cabeçalho**

| Campo | Formato | Exemplo |
|-------|---------|---------|
| **Título** | `# [Disciplina] - [N]º Ano` | `# Matemática - 4º Ano` |
| **Disciplina** | `**Disciplina:** [Nome]` | `**Disciplina:** Matemática` |
| **Ano Escolar** | `**Ano Escolar:** [N]º Ano` | `**Ano Escolar:** 4º Ano` |
| **Assignee** | `**Assignee:** @username` | `**Assignee:** @deborafeijo-gif` |
| **Status** | `**Status:** Backlog` | `**Status:** Backlog` |
| **Total de Tickets** | `**Total de Tickets:** [qty]` | `**Total de Tickets:** 200` |
| **Última Atualização** | `**Última Atualização:** YYYY-MM-DD` | `**Última Atualização:** 2026-04-02` |

### **2. Tickets**

#### **Aulas Base (.1, .2, .3)**
```
[Disciplina] - Ano [N] - [N.N] [Título]

# Description

[Descrição com verbo no gerúndio ou substantivo]
```

**Exemplos:**
- ✅ "Reconhecimento e leitura de números..."
- ✅ "Decomposição de números de quatro ordens..."
- ✅ "Localização de números naturais..."
- ❌ "O aluno vai aprender..." (muito longo)
- ❌ "Ensinar números..." (verbo no infinitivo)

#### **Revisão (.4)**
```
[Disciplina] - Ano [N] - [N].4 Revisão

# Description

Revisão dos conhecimentos das 3 aulas anteriores
```

**Regra:**
- **Semanas 1-8, 11-18, 21-28, 31-38:** "3 aulas anteriores" (revisão semanal)
- **Semanas 9, 19, 29, 39:** "oito semanas anteriores" (revisão bimestral)

#### **Prova (.5)**
```
[Disciplina] - Ano [N] - [N].5 Prova

# Description

Avaliação dos conhecimentos das 3 aulas anteriores
```

**Regra:**
- **Semanas 1-8, 11-18, 21-28, 31-38:** "3 aulas anteriores" (prova semanal)
- **Semanas 10, 20, 30, 40:** "oito semanas anteriores" (prova bimestral)

---

## 🗂️ **Estrutura de Pastas**

```
0-Descrições e criação de tickets para as disciplinas/
├── TEMPLATE-REFERENCIA.md      # Este arquivo
├── ciencias-4-ano.md            # ✅ Template original
├── matematica-4-ano.md          # ✅ Atualizado
├── geografia-3-ano.md           # ⏳ Pendente atualizar
└── [outras disciplinas]/
    └── [disciplina]-[ano].md
```

---

## 🔄 **Fluxo de Criação de Tickets**

### **Passo 1: Copiar Template**
```bash
cp TEMPLATE-REFERENCIA.md [disciplina]-[ano].md
```

### **Passo 2: Preencher Cabeçalho**
```markdown
# [Disciplina] - [N]º Ano

**Disciplina:** [Nome]
**Ano Escolar:** [N]º Ano
**Assignee:** @username
**Status:** Backlog
**Total de Tickets:** [calcular]
**Última Atualização:** YYYY-MM-DD
```

### **Passo 3: Listar Aulas do Currículo Macro**
Para cada semana do Currículo Macro:
- Copiar título da aula (exatamente como está)
- Manter numeração (1.1, 1.2, 1.3, etc.)

### **Passo 4: Escrever Descrições**
- **Aulas base:** 1 frase objetiva
- **Revisão:** "Revisão dos conhecimentos das X semanas anteriores"
- **Prova:** "Avaliação dos conhecimentos das X semanas anteriores"

### **Passo 5: Validar**
- [ ] Todos os tickets têm descrição
- [ ] Descrições começam com substantivo/gerúndio
- [ ] Revisões e provas seguem padrão
- [ ] Separador `---` entre todos os tickets
- [ ] **NÃO** tem `assignees:` ou `status:` no corpo dos tickets

---

## 📊 **Estrutura Semanal Padrão**

| Semana | Tickets | Descrição |
|--------|---------|-----------|
| **1-8** | .1, .2, .3, .4, .5 | 3 aulas + revisão + prova |
| **9** | Revisão | Revisão bimestral |
| **10** | Provas | Prova bimestral |
| **11-18** | .1, .2, .3, .4, .5 | 3 aulas + revisão + prova |
| **19** | Revisão | Revisão bimestral |
| **20** | Provas | Prova bimestral |
| **21-28** | .1, .2, .3, .4, .5 | 3 aulas + revisão + prova |
| **29** | Revisão | Revisão bimestral |
| **30** | Provas | Prova bimestral |
| **31-38** | .1, .2, .3, .4, .5 | 3 aulas + revisão + prova |
| **39** | Revisão | Revisão bimestral |
| **40** | Provas | Prova bimestral |

**Total por ano:** 200 tickets (40 semanas × 5 tickets/semana média)

---

## 🎯 **Exemplos por Disciplina**

### **Ciências**
```markdown
# Ciência - 4º Ano

**Disciplina:** Ciência
**Ano Escolar:** 4º Ano
**Assignee:** @leticiaoliveira09
**Status:** Backlog

---

[Ciência] - Ano 4 - 8.1 Reações químicas

# Description

Característica da classificação da maioria dos elementos químicos: os metais.

---
```

### **Matemática**
```markdown
# Matemática - 4º Ano

**Disciplina:** Matemática
**Ano Escolar:** 4º Ano
**Assignee:** @deborafeijo-gif
**Status:** Backlog

---

[Matemática] - Ano 4 - 1.1 Números até 10.000

# Description

Reconhecimento e leitura de números naturais até 10.000.

---
```

### **Geografia**
```markdown
# Geografia - 3º Ano

**Disciplina:** Geografia
**Ano Escolar:** 3º Ano
**Assignee:** @username-github
**Status:** Backlog

---

[Geografia] - Ano 3 - 1.1 [Título]

# Description

[Descrição objetiva]

---
```

---

## ✅ **Checklist de Validação**

Antes de commitar, verifique:

### **Cabeçalho**
- [ ] Título no formato `# [Disciplina] - [N]º Ano`
- [ ] Todos os metadados preenchidos
- [ ] Assignee com `@` (ex: `@username-github`)
- [ ] Status como `Backlog`
- [ ] Total de tickets calculado corretamente
- [ ] Data de atualização no formato `YYYY-MM-DD`

### **Corpo**
- [ ] **NÃO** tem `assignees:` ou `status:` nos tickets
- [ ] Todos os tickets começam com `[Disciplina] - Ano [N] -`
- [ ] Títulos das aulas batem com Currículo Macro
- [ ] Descrições com 1 frase objetiva
- [ ] Descrições começam com substantivo ou gerúndio
- [ ] Separador `---` entre todos os tickets
- [ ] Revisões (.4) seguem padrão
- [ ] Provas (.5) seguem padrão

---

## 🔗 **Integração com GitHub**

### **Para Criar Issues:**

#### **Opção 1: Script Python**
```bash
python bef/scripts/scripts/create_issues.py --file [disciplina]-[ano].md
```

#### **Opção 2: GitHub MCP**
```
@github create issues from [disciplina]-[ano].md
```

#### **Opção 3: Manual**
1. Extrair cada ticket do arquivo
2. Título: `[Disciplina] - Ano [N] - [N.N] [Título]`
3. Description: Conteúdo após `# Description`
4. Labels: `ano:[N]`, `[disciplina]`, `status:backlog`
5. Assignee: Definido no cabeçalho do arquivo

---

## 📚 **Arquivos de Referência**

| Arquivo | Propósito |
|---------|-----------|
| `TEMPLATE-REFERENCIA.md` | Este arquivo - padrão geral |
| `ciencias-4-ano.md` | Template original (Ciências 4º) |
| `matematica-4-ano.md` | Template atualizado (Matemática 4º) |
| `1 - Curriculo Macro - [N]º ANO.md` | Fonte dos títulos das aulas |

---

## 🔄 **Histórico de Atualizações**

| Data | Versão | Mudança | Responsável |
|------|--------|---------|-------------|
| 2026-04-02 | 1.0 | Criação do template padrão | Editorial Squad |
| 2026-04-02 | 1.1 | Remoção de assignees/status do corpo | Editorial Squad |

---

## 📞 **Dúvidas**

Para dúvidas sobre este template:
1. Consulte `ciencias-4-ano.md` (exemplo original)
2. Verifique `matematica-4-ano.md` (exemplo atualizado)
3. Acesse `bef/scripts/scripts/generate_descriptions.py` (script de geração)

---

**Versão:** 1.1  
**Última atualização:** 2026-04-02  
**Status:** ✅ Padrão Oficial
