---
description: Criar uma aula completa seguindo o plano pedagógico e controle de termos
---

# /create-lesson — Fluxo Completo de Criação de Aula

Este workflow cria uma aula do zero, seguindo o plano pedagógico, o controle de termos e executando o **Context Loop** editorial (Passos 4→5→6→7). Funciona para qualquer ano (1º ao 5º).

**Entrada**: O usuário informa o número da aula (ex: `36.3`) e o ano (ex: `5º ano`). Se o ano não for informado, pergunte.

**Tipo de Recordar**: O usuário pode especificar `rima` ou `música` na solicitação. Regra padrão:
- **3º ano** → Rima (padrão)
- **Todos os outros anos** → Música (padrão)
- Se o usuário especificar explicitamente, a escolha dele prevalece sobre o padrão.

---

## Resolução de Caminhos

Use a tabela abaixo para resolver os caminhos corretos com base no ano informado:

| Ano | Pasta do Ano | Pasta da Estrutura |
|-----|-------------|-------------------|
| 1º | `1º Ano` | `Estrutura Curricular` |
| 2º | `2º Ano - DA CRIAÇÃO ATÉ A ARTE BIZANTINA` | `Estrutura Curricular - 2º ANO` |
| 3º | `3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE` | `Estrutura Curricular - 3º ANO` |
| 4º | `4º Ano - IMPRESSIONISMO ATÉ A ARTE CONTEMPORÂNEA` | `Estrutura Curricular` |
| 5º | `5º Ano - MANEIRISMO ATÉ O REALISMO AMERICANO` | `Estrutura Curricular` |

**Caminho base:**
```
/home/italo.gabriel/Documents/Bibline Academy/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/[PASTA_DO_ANO]/
```

> **Dica:** Use `list_dir` na pasta da estrutura para descobrir os nomes exatos dos arquivos.

---

## Passo 1 — Ler o Plano Pedagógico

Abra o arquivo `3 - Visão e Plano pedagogico - [X]º ANO.md` do ano correspondente.

- Localize a **semana** e **aula** correspondente (ex: `36.3` → Semana 36, Aula 3).
- Extraia:
  - **Título da aula**
  - **Tema central**
  - **Versículo-chave**
  - **Progressão pedagógica**
  - **Objetivo geral do módulo**
  - **Visão teológica** da semana

Esses dados são a **base obrigatória** para todo o conteúdo da aula.

---

## Passo 2 — Verificar Termos Já Definidos

Abra o arquivo `1 - Curriculo Macro - ... - [X]º ANO.md` do ano correspondente.

- Compile **todos os termos já marcados com ✅** em todas as semanas.
- Esses termos estão **PROIBIDOS** de serem reutilizados como termo principal.
- Escolha um **novo termo** que:
  - Tenha relação direta com o tema da aula
  - **NÃO conste** na lista de termos já definidos
  - Seja adequado para crianças de 7 a 11 anos

---

## Passo 3 — Executar o Context Loop Editorial

Com o plano pedagógico e o termo escolhido, execute as 4 etapas do fluxo editorial em sequência. **Cada etapa recebe o output da anterior como input.**

### 3.1 — Passo 4: Writer (Redator Especialista)
// turbo
- Leia o skill: `.agent/skills/writer/SKILL.md`
- Consulte a base de conhecimento (`.agent/knowledge-base/`)
- Escreva a aula nos 5 Hábitos (Definir, Perceber, Recordar, Praticar, Narrar)
- Use o termo escolhido como conceito central
- Siga a progressão pedagógica extraída do plano
- **Output:** Rascunho em Rise Blocks → `[READY_FOR_STEP_5]`

### 3.2 — Passo 5: Standardizer (Editor de Estilo)
// turbo
- Leia o skill: `.agent/skills/standardizer/SKILL.md`
- Aplique os Rise Blocks conforme o template
- Corrija caracteres proibidos, voz passiva, formatação
- **Output:** Conteúdo padronizado → `[READY_FOR_STEP_6]`

### 3.3 — Passo 6: Reviewer (Revisor de Qualidade)
// turbo
- Leia o skill: `.agent/skills/reviewer/SKILL.md`
- Valide o checklist de auditoria completo
- **Verificação adicional**: confirme que o termo NÃO está na lista de termos já definidos
- Se `[APPROVED_FOR_STEP_7]` → prossiga
- Se `[REJECTED]` → retorne ao passo indicado e repita

### 3.4 — Passo 7: Copywriter Editorial
// turbo
- Leia o skill: `.agent/skills/copywriter/SKILL.md`
- Ajuste título, definição e perguntas finais
- **Output:** `[FINAL — READY FOR PUBLISH]`

---

## Passo 4 — Publicar

Execute o workflow `/publish`:
1. Salvar localmente no caminho correto do ano
2. Publicar no GitHub via MCP (se solicitado)

---

## Passo 5 — Criar Revisão Semanal (quando semana completa)

> **EXECUTAR SOMENTE** quando as 3 aulas da semana estiverem prontas (X.1, X.2, X.3).

// turbo
- Leia o skill: `.agent/skills/review-builder/SKILL.md`
- Extraia a definição curta do Recordar de cada aula (9-10 palavras)
- Crie o arquivo `[Semana].4.md` seguindo o padrão de revisão (revisão = 4ª aula da semana)
- **Output:** Arquivo de revisão semanal salvo localmente

## Passo 5.5 — Criar Prova Semanal (quando semana completa)

> **EXECUTAR SOMENTE** quando as 3 aulas + revisão da semana estiverem prontas (X.1, X.2, X.3, X.4).

// turbo
- Leia o skill: `.agent/skills/exam-builder/SKILL.md`
- Extraia definições completas do Definir e conteúdo das 3 aulas
- Crie o arquivo `[Semana].5.md` seguindo o padrão CANVAS_QUIZ (prova = 5ª aula da semana)
- **Output:** Arquivo de prova semanal salvo localmente

---

## Passo 6 — Registrar ✅ no Currículo Macro

> **OBRIGATÓRIO**: Executar automaticamente ao final de cada aula.

Abra o arquivo `1 - Curriculo Macro - ... - [X]º ANO.md`:

1. Localizar a linha `- Dia N: [Tema da aula]` e adicionar ` ✅`
2. **Quando a semana estiver completa (3 aulas):**
   - Adicionar ` ✅` ao título `## Semana N – **Tema**`
   - Adicionar bloco de termos logo após as 3 aulas:

```markdown
# Semana N
Termo1 ✅
Termo2 ✅
Termo3 ✅
```

3. Cada termo = termo principal do Accordion/Definir da aula

---

## Passo 7 — Confirmar ao Usuário

Reporte:
- ✅ Aula criada com base no plano pedagógico do **[X]º Ano**
- ✅ Termo novo: `[TERMO]` (não repetido)
- ✅ Context Loop: Writer → Standardizer → Reviewer → Copywriter
- ✅ Salvo localmente em `[caminho]`
- ✅ Currículo Macro: `Dia N` + termo marcado ✅

