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

## Passo 2 — Identificar o Tema Central da Semana

Abra o arquivo `1 - Curriculo Macro - ... - [X]º ANO.md` do ano correspondente.

- Compile **todos os termos já marcados com ✅** em **semanas anteriores**. Eles estão **PROIBIDOS** como termo de uma nova semana.
- Identifique o **tema central da semana** (o título de `x.1`) e o **termo principal** que será compartilhado pelas 3 aulas.
- Se você está criando `x.2` ou `x.3`, **leia primeiro `x.1`** da mesma semana e extraia:
  - A **definição curta literal** de 9-10 palavras (vai ser repetida sem alteração)
  - O **termo principal** (vai ser o mesmo)
  - O **nome da música ou rima** do Recordar (vai ser o mesmo)
- Se você está criando `x.1`, escolha um termo que:
  - Tenha relação direta com o tema central da semana
  - **NÃO conste** na lista de termos de semanas anteriores
  - Seja adequado para crianças de 7 a 11 anos

---

## Passo 3 — Executar o Context Loop Editorial

Com o plano pedagógico e o tema central da semana definidos, execute as 4 etapas do fluxo editorial em sequência. **Cada etapa recebe o output da anterior como input.**

### 3.1 — Passo 4: Writer (Redator Especialista)
// turbo
- Leia o skill: `.agent/skills/writer/SKILL.md`
- Consulte a base de conhecimento (`.agent/knowledge-base/`)
- Escreva a aula nos 5 Hábitos (Definir, Perceber, Recordar, Praticar, Narrar)
- Use o **termo da semana** (compartilhado pelas 3 aulas) como conceito central
- Em `x.2` e `x.3`, mantenha a **mesma definição curta literal** de `x.1`. Apenas o parágrafo livre do Definir, a explicação no Accordion, as imagens, o texto do Narrar e a Atividade Extra variam
- Siga a progressão pedagógica extraída do plano
- Use a definição curta do Recordar literalmente no cabeçalho do Definir e no Statement_D. No Accordion, inclua `@link_png@`, narre definição curta e explicação completa no MP3, e mantenha texto visual equivalente após `[MP3\]`
- Em Praticar, mantenha sempre Fill_In, depois `[+MULTIPLE]`, depois Atividade Extra com `[+ACTIVITY_WORKSHEET]`
- No 3º ano, em Narrar, mantenha `[+PARAGRAPH]` para a leitura e `[+IMAGE]` com `@link_png@` antes das perguntas
- **Output:** Rascunho em Rise Blocks → `[READY_FOR_STEP_5]`

### 3.2 — Passo 5: Standardizer (Editor de Estilo)
// turbo
- Leia o skill: `.agent/skills/standardizer/SKILL.md`
- Aplique os Rise Blocks conforme o template
- Corrija caracteres proibidos, voz passiva, formatação
- Confirme que a definição curta está literalmente idêntica no Definir e no Recordar. Confirme também que o MP3 do Accordion contém definição curta e explicação completa
- Se for `x.2` ou `x.3`, **abra `x.1`** e compare definição curta, termo principal e música/rima. Devem ser literais
- Confirme que o `[+MULTIPLE]` permanece no Praticar e que a imagem do Narrar permanece no padrão do ano
- **Output:** Conteúdo padronizado → `[READY_FOR_STEP_6]`

### 3.3 — Passo 6: Reviewer (Revisor de Qualidade)
// turbo
- Leia o skill: `.agent/skills/reviewer/SKILL.md`
- Valide o checklist de auditoria completo
- **Verificação adicional**: confirme que o termo da semana NÃO está na lista de termos de semanas anteriores
- **Verificação adicional**: se for `x.2` ou `x.3`, confirme que definição curta, termo e música/rima são literais a `x.1`
- **Verificação adicional**: confirme que a definição curta do Recordar aparece literalmente no cabeçalho do Definir. No Accordion, confirme que MP3 e texto visível têm conteúdo equivalente
- **Verificação adicional**: confirme que Praticar contém `[+MULTIPLE]` e, no 3º ano, Narrar contém `[+IMAGE]` após a leitura
- Se `[APPROVED_FOR_STEP_7]` → prossiga
- Se `[REJECTED]` → retorne ao passo indicado e repita

### 3.4 — Passo 7: Copywriter Editorial
// turbo
- Leia o skill: `.agent/skills/copywriter/SKILL.md`
- Ajuste títulos internos e perguntas finais, sem alterar a definição curta validada
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
- Extraia a **única definição curta da semana** (idêntica em x.1, x.2, x.3)
- Use o template novo `Templates Novos - Nº ANO/2-template-aula-revisao-semanal.md`
- Crie o arquivo `[Semana].4.md` com:
  - **Definir**: a definição curta única da semana + `[+IMAGE_TEXT_ON]` com a música da semana
  - **Perceber**: `[+IMAGE_LABELED]` com 3 hotspots (um por aula) mostrando os títulos das aulas
  - **Recordar**: `[+STATEMENT_D]` com a definição curta da semana
  - **Praticar**: 1 `[+FILL_IN]` com a definição da semana + 3 `[+MULTIPLE]` (um por aula)
  - **Narrar**: parágrafo introdutório para narração oral
- **Output:** Arquivo de revisão semanal salvo localmente

## Passo 5.5 — Criar Prova Semanal (quando semana completa)

> **EXECUTAR SOMENTE** quando as 3 aulas + revisão da semana estiverem prontas (X.1, X.2, X.3, X.4).

// turbo
- Leia o skill: `.agent/skills/exam-builder/SKILL.md`
- Extraia as definições curtas validadas e o conteúdo das 3 aulas
- Crie o arquivo `[Semana].5.md` seguindo o padrão CANVAS_QUIZ (prova = 5ª aula da semana)
- **Output:** Arquivo de prova semanal salvo localmente

---

## Passo 6 — Registrar ✅ no Currículo Macro

> **OBRIGATÓRIO**: Executar automaticamente ao final de cada aula.

Abra o arquivo `1 - Curriculo Macro - ... - [X]º ANO.md`:

1. Localizar a linha `- N.M [Título da aula]` e adicionar ` ✅`
2. **Quando a semana estiver completa (3 aulas):**
   - Adicionar ` ✅` ao título `## Semana N - **Tema central**`
   - Adicionar bloco de **termo da semana** logo após as 3 aulas:

```markdown
# Semana N
[TermoCentral] ✅
```

3. O `[TermoCentral]` é o termo principal compartilhado pelas 3 aulas (o mesmo do Accordion/Definir de x.1, x.2 e x.3)

> **Padrão antigo (descontinuado)**: blocos com 3 termos por semana não são mais utilizados.

---

## Passo 7 — Confirmar ao Usuário

Reporte:
- ✅ Aula criada com base no plano pedagógico do **[X]º Ano**
- ✅ Termo da semana: `[TermoCentral]` (compartilhado com x.1, x.2, x.3)
- ✅ Context Loop: Writer → Standardizer → Reviewer → Copywriter
- ✅ Salvo localmente em `[caminho]`
- ✅ Currículo Macro: aula marcada ✅ (termo da semana registrado quando completar 3/3)
