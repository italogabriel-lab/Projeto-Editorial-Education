# 🎯 Orchestrator Agent - Documentação Completa

**Diretor Editorial da Squad Editorial Bibline**

---

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Objetivo](#objetivo)
3. [Comandos Disponíveis](#comandos-disponíveis)
4. [Exemplos de Uso](#exemplos-de-uso)
5. [Matriz de Delegação](#matriz-de-delegação)
6. [Auditoria de Consistência](#auditoria-de-consistência)
7. [Casos de Uso](#casos-de-uso)
8. [FAQ](#faq)

---

## Visão Geral

| Propriedade | Valor |
|-------------|-------|
| **Nome** | Orchestrator |
| **Tipo** | Diretor Editorial |
| **Escopo** | Editorial Squad |
| **Status** | ✅ Ativo |
| **Versão** | 1.0 |
| **Etapa** | Transversal (todas) |

---

## Objetivo

O **Orchestrator** é o ponto central de orientação do projeto. Ele não executa o trabalho dos outros agentes — ele **diagnostica, prioriza e delega**.

**Quando usar:**
- Precisa de direção sobre o que fazer agora
- Quer saber o status do projeto
- Tem dúvidas sobre qual agente/workflow usar
- Solicita auditoria de consistência

---

## Comandos Disponíveis

### **1. `/orchestrator status <ano>`**

**Descrição:** Diagnostica o progresso de um ano específico.

**Sintaxe:**
```bash
/orchestrator status <ano>
```

**Parâmetros:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `ano` | number | ✅ | Ano escolar (1-5) |

**Exemplo:**
```bash
/orchestrator status 3
```

**Saída:**
```
📊 STATUS — 3º Ano
✅ Semanas completas: 1–6 (18 aulas + 6 revisões)
🔄 Em andamento: Semana 7 (7.1 ✅ | 7.2 pendente | 7.3 pendente)
⏭️ Próxima: Semana 8
```

---

### **2. `/orchestrator next <ano>`**

**Descrição:** Sugere as próximas ações priorizadas.

**Sintaxe:**
```bash
/orchestrator next <ano>
```

**Parâmetros:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `ano` | number | ✅ | Ano escolar (1-5) |

**Exemplo:**
```bash
/orchestrator next 2
```

**Saída:**
```
🎯 PRÓXIMAS AÇÕES — 2º Ano

1. Completar Semana 7
   - 7.2 ✅ Concluída
   - 7.3 ⏳ Pendente → @writer
   - 7.4 Revisão → @review-builder
   - 7.5 Prova → @exam-builder

2. Sincronizar documentos
   - Matriz Curricular → @standardizer
   - Tickets GitHub → @devops

3. Publicar no GitHub
   - 3 aulas pendentes → @publisher
```

---

### **3. `/orchestrator delegate <tarefa>`**

**Descrição:** Direciona para o agente/workflow correto.

**Sintaxe:**
```bash
/orchestrator delegate <tarefa>
```

**Parâmetros:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `tarefa` | string | ✅ | Descrição da tarefa |

**Exemplo:**
```bash
/orchestrator delegate "Criar aula 5.3 sobre Arte Barroca"
```

**Saída:**
```
🔀 DELEGAÇÃO

Tarefa: Criar aula 5.3 sobre Arte Barroca

Agente recomendado: @writer
Workflow: produce_class.md

Comando:
@writer "Crie a aula 5.3 sobre Arte Barroca, 5º ano"

Próximos passos:
1. @researcher → Pesquisar conteúdo
2. @writer → Redigir aula
3. @standardizer → Formatar Rise Blocks
4. @reviewer → Revisar qualidade
5. @copywriter → Polir texto
6. @publisher → Publicar
```

---

### **4. `/orchestrator audit <ano> <semana>`**

**Descrição:** Auditoria de consistência entre documentos.

**Sintaxe:**
```bash
/orchestrator audit <ano> <semana>
```

**Parâmetros:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `ano` | number | ✅ | Ano escolar (1-5) |
| `semana` | number | ✅ | Número da semana |

**Exemplo:**
```bash
/orchestrator audit 3 7
```

**Saída:**
```
🔍 AUDITORIA — 3º Ano, Semana 7

✅ Títulos: OK (todos batem com Currículo Macro)
❌ Definições: DIVERGÊNCIA
   - Aula 7.1: "Arte = expressão humana"
   - Revisão 7.4: "Arte = linguagem da fé"
   → Executar: python scripts/sync_titles.py

✅ Perceber: OK (links atualizados)
⚠️ Imagens: 2 links desatualizados
   → Atualizar em: 4 - Links-para-imagens-perceber.md
```

---

## Matriz de Delegação

| Demanda | Agente/Workflow | Comando |
|---------|-----------------|---------|
| Criar aula nova | `workflows/produce_class` | "Crie a aula X.X, Nº ano" |
| Criar revisão (X.4) | `skills/review-builder` | "Crie a revisão da semana X" |
| Criar revisão bimestral | `skills/bimester-review-builder` | "Crie a revisão do bimestre N" |
| Criar prova bimestral | `skills/bimester-exam-builder` | "Crie a prova do bimestre N" |
| Corrigir formatação Rise | `skills/standardizer` | @standardizer |
| Corrigir capitalização | `skills/capitalizer` | @capitalizer |
| Revisar qualidade | `skills/reviewer` | @reviewer |
| Polir texto | `skills/copywriter` | @copywriter |
| Subir no GitHub | `skills/devops` | @devops |
| Pesquisar conteúdo | `skills/researcher` | @researcher |
| Publicar arquivo | `skills/publisher` | @publisher |
| Status geral | `orchestrator` | @orchestrator |
| Design Thinking | `skills/design-thinking` | @design-thinking |
| UI Designer | `skills/ui-designer` | @ui-designer |

---

## Auditoria de Consistência

### **Checklist de Verificação**

1. **Títulos (H1)**
   - [ ] Batem com o Currículo Macro?
   - [ ] São idênticos em todos os documentos?

2. **Definições**
   - [ ] 9 palavras são idênticas em Definir, Recordar e Revisão?
   - [ ] MP3 do Recordar bate com Accordion do Definir?

3. **Seção Perceber**
   - [ ] Aulas base batem com Revisão correspondente?
   - [ ] Links de imagens estão atualizados?

4. **Sincronização**
   - [ ] Matriz Curricular usa mesmos títulos?
   - [ ] Visão e Plano Pedagógico está sincronizado?
   - [ ] Descrições de tickets estão atualizadas?

### **Mecanismo de Correção**

Sempre que detectar divergência:

```bash
# Executar script de sincronização
python scripts/sync_titles.py
```

Este script:
1. Lê o Currículo Macro
2. Corrige automaticamente todos os outros arquivos
3. Garante consistência total

---

## Exemplos de Uso

### **Cenário 1: Início de Produção**

```bash
@orchestrator "Quero começar a produzir o 3º ano"
```

**Resposta:**
```
📊 DIAGNÓSTICO — 3º Ano

Status atual:
✅ Semanas 1-6: 100% concluídas
⏳ Semana 7: 33% (1/3 aulas)
⏭️ Próxima: Semana 8

🎯 AÇÕES PRIORITÁRIAS

1. Completar Semana 7
   - 7.2 ✅ Concluída
   - 7.3 ⏳ Pendente → @writer "Crie 7.3, 3º ano"
   - 7.4 Revisão → @review-builder "Semana 7"
   - 7.5 Prova → @exam-builder "Semana 7"

2. Após concluir Semana 7, iniciar Semana 8
```

---

### **Cenário 2: Dúvida de Fluxo**

```bash
@orchestrator "Qual a diferença entre review-builder e bimester-review-builder?"
```

**Resposta:**
```
📚 DIFERENÇA ENTRE REVISÕES

Review Builder (semanal):
- Revisão X.4 de cada semana
- 3 aulas + revisão + prova
- Ex: "Revisão da Semana 5"

Bimester Review Builder (bimestral):
- Revisão geral do bimestre
- 8-10 semanas de conteúdo
- Ex: "Revisão do 2º Bimestre"

Use:
- Semanal → @review-builder "Semana 5"
- Bimestral → @bimester-review-builder "Bimestre 2, 3º ano"
```

---

### **Cenário 3: Auditoria Solicitada**

```bash
@orchestrator "As aulas da Semana 12 estão consistentes?"
```

**Resposta:**
```
🔍 AUDITORIA — Semana 12

✅ Títulos: OK
✅ Definições: OK (9 palavras idênticas)
✅ Perceber: OK
⚠️ Imagens: 1 link desatualizado
   → Atualizar: imagem 12.2 em "4 - Links-para-imagens"

📊 CONFIANÇA: 95%

Ação recomendada:
@devops "Atualizar links de imagem da Semana 12"
```

---

## Casos de Uso

### **1. Diretor Editorial**

**Objetivo:** Visão estratégica de andamento

**Comandos:**
```bash
/orchestrator status 1
/orchestrator status 2
/orchestrator status 3
/orchestrator status 4
/orchestrator status 5
```

**Benefícios:**
- Visão consolidada de todos os anos
- Identifica gargalos
- Aloca recursos baseado em prioridades

---

### **2. Gestor de Produção**

**Objetivo:** Acompanhamento diário

**Comandos:**
```bash
/orchestrator next 3
/orchestrator delegate "Criar revisão Semana 8"
/orchestrator audit 3 8
```

**Benefícios:**
- Sabe exatamente o que fazer agora
- Delega corretamente
- Garante qualidade com auditoria

---

### **3. Novo Membro da Equipe**

**Objetivo:** Entender o fluxo

**Comandos:**
```bash
@orchestrator "Como funciona o fluxo de produção?"
@orchestrator "Qual agente uso para criar uma prova?"
```

**Benefícios:**
- Aprende o fluxo rapidamente
- Sabe qual agente usar
- Evita erros de processo

---

## FAQ

### **P: O Orchestrator executa tarefas?**
**R:** Não! Ele apenas diagnostica, prioriza e delega. Para executar, use os agentes específicos.

---

### **P: Como sei se devo usar review-builder ou bimester-review-builder?**
**R:** 
- **Review Builder:** Revisões semanais (X.4)
- **Bimester Review Builder:** Revisões do bimestre inteiro

---

### **P: O que fazer se detectar inconsistência de títulos?**
**R:** Execute o script de sincronização:
```bash
python scripts/sync_titles.py
```

---

### **P: Qual a prioridade: completar semana ou iniciar nova?**
**R:** Sempre complete a semana em andamento primeiro. Uma semana parcial tem prioridade sobre começar uma nova.

---

### **P: Como o Orchestrator sabe o status?**
**R:** Ele lê o **Currículo Macro** de cada ano, que é a fonte oficial de verdade. As semanas completas estão marcadas com ✅.

---

## Links Úteis

- [Skill Definition](SKILL.md)
- [Workflow de Aula](../workflows/produce_class.md)
- [Currículo Macro](../../Belas%20Artes%20-%20Fase%20da%20Gramática/1%20Fase%20-%20Gramática/)
- [Knowledge Base](../knowledge-base/)

---

**Gerado por:** Editorial Squad  
**Data:** 2026-04-01  
**Versão:** 1.0

---

> "Orquestrar é fazer com que cada parte toque no momento certo, na intensidade certa, para criar uma sinfonia."
