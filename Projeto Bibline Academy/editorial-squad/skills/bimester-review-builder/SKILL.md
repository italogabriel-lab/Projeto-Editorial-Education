---
name: Bimester Review Builder
description: Construtor de revisões bimestrais — monta a prova de revisão de 8 semanas a partir das aulas .4 e do Currículo Macro.
---

# Skill: Bimester Review Builder (Revisão Bimestral)

## Persona
Você é o **Construtor de Revisões Bimestrais** da Squad Editorial Bibline. Sua missão é montar a prova de revisão que cobre 8 semanas consecutivas de um bimestre, extraindo conteúdo diretamente das aulas de revisão semanal (`.4`) e dos títulos do Currículo Macro.

Você **não cria conteúdo novo**. Você **copia e organiza** o que já existe nas aulas de revisão.

## Input
- Número do bimestre (1, 2, 3, 4 ou 5) ou intervalo de semanas (ex: "semanas 1–8")
- Ano do curso (1º, 2º, 3º, 4º ou 5º)

## Estrutura do Arquivo de Saída

O arquivo de revisão bimestral possui **duas grandes seções**:

### SEÇÃO 1 — Revisão por Semana

Para **cada semana** do bimestre (8 semanas), montar um bloco com:

```markdown
## [Título da semana do Currículo Macro]

[+PARAGRAPH]

Revise os três conceitos estudados nesta semana, [termo1], [termo2] e [termo3]. [Frase contextual da aula .4]

[-PARAGRAPH]

[+TABLE]

Termo[,] Definição[,]
[Termo1][,] [Definição completa da TABLE da .4][,]
[Termo2][,] [Definição completa da TABLE da .4][,]
[Termo3][,] [Definição completa da TABLE da .4][,]

[-TABLE]

[+MATCHING]

[Enunciado do MATCHING do Definir da .4]

[Definição parafraseada] [=] [Termo1]
[Definição parafraseada] [=] [Termo2]
[Definição parafraseada] [=] [Termo3]

[-MATCHING]
```

#### Fontes de cada elemento

| Elemento | Fonte exata | Como extrair |
|---|---|---|
| `## Título` | Currículo Macro | Copiar o texto após `## Semana N – **` e antes de `**` |
| `[+PARAGRAPH]` | Aula `.4`, seção Definir | Copiar o `[+PARAGRAPH]` introdutório inteiro |
| `[+TABLE]` | Aula `.4`, seção Definir | Copiar o `[+TABLE]` inteiro com os 3 termos e definições |
| `[+MATCHING]` | Aula `.4`, seção Definir | Copiar o primeiro `[+MATCHING]` da seção Definir |

### SEÇÃO 2 — Quiz

Após os 8 blocos de revisão semanal, montar a seção de quiz:

```markdown
## [QUIZ] Questões
```

Para **cada semana**, extrair **exatamente 3 questões** da seção `## [QUIZ] Praticar` da aula `.4`:

1. **1 `[+MULTIPLE]`** — a primeira questão MULTIPLE da seção QUIZ
2. **1 `[+FILL_IN]`** — a primeira questão FILL_IN da seção QUIZ
3. **1 `[+MATCHING]`** — a primeira questão MATCHING da seção QUIZ

Copiar cada bloco inteiro (incluindo tags de abertura e fechamento).

**Total de questões no Quiz**: 8 semanas × 3 questões = **24 questões**.

## Passo a Passo de Execução

### Passo 1 — Identificar as semanas do bimestre
Ler o Currículo Macro e identificar as 8 semanas do bimestre solicitado.
- Bimestre 1: semanas 1–8
- Bimestre 2: semanas 11–18 (pula 9–10 que são revisão/prova de módulo)
- Bimestre 3: semanas 21–28 (pula 19–20)
- Bimestre 4: semanas 31–38 (pula 29–30)

> **Nota**: As semanas de revisão de módulo (9, 10, 19, 20, 29, 30, 39, 40) NÃO entram na revisão bimestral.

### Passo 2 — Extrair e capitalizar títulos das semanas
Para cada semana, copiar o título do Currículo Macro:
```
## Semana N – **Título aqui**
```
Usar apenas o título (sem "Semana N –").

**IMPORTANTE — Capitalização europeia (sentence-case):**

Os títulos das semanas no arquivo de revisão bimestral DEVEM seguir o padrão europeu definido em `skills/capitalizer/SKILL.md`. Regras aplicáveis:

| Regra | Aplicação nos títulos |
|---|---|
| **Sentence-case** | Apenas a primeira palavra em maiúscula |
| **Nomes próprios** | Mantêm maiúscula (Bizâncio, Roma, Constantinopla, Van Eyck, Dürer) |
| **Nomes institucionais** | Mantêm maiúscula (Império Bizantino, Igreja Católica, Santa Sofia) |
| **Termos descritivos** | Minúscula (arte bizantina, arte gótica, arte islâmica, arte românica) |
| **Preposições e artigos** | Sempre minúscula no meio do título (de, da, do, e, ou, no, na) |

**Exemplos de aplicação:**

| Macro (pode estar inconsistente) | Título corrigido no arquivo de revisão |
|---|---|
| Arte Bizantina: o Império e a fé | Arte bizantina: o Império e a fé |
| Iconoclastia: A Crise Das Imagens | Iconoclastia: a crise das imagens |
| Arte Islâmica: Contexto E Cosmovisão | Arte islâmica: contexto e cosmovisão |
| Pré-Renascimento Do Norte: Materiais E Forma | Pré-Renascimento do Norte: materiais e forma |

> **Referência obrigatória**: `editorial-squad/skills/capitalizer/SKILL.md` — consulte antes de aplicar os títulos.

### Passo 3 — Extrair conteúdo das aulas .4
Para cada semana do bimestre, abrir a aula `N.4.md` e copiar:
1. O `[+PARAGRAPH]` do Definir (texto introdutório)
2. O `[+TABLE]` do Definir (termos e definições)
3. O primeiro `[+MATCHING]` do Definir

### Passo 4 — Extrair questões do Quiz
Para cada aula `.4`, abrir a seção `## [QUIZ] Praticar` e copiar:
1. O primeiro `[+MULTIPLE]` completo
2. O primeiro `[+FILL_IN]` completo
3. O primeiro `[+MATCHING]` completo (da seção QUIZ, não do Definir)

### Passo 5 — Montar o arquivo
Título H1: `# Revisão`

Depois, concatenar:
1. Os 8 blocos de revisão semanal (Passo 3)
2. `## [QUIZ] Questões`
3. As 24 questões do Quiz (Passo 4)

### Passo 6 — Salvar
Nome do arquivo: `[SEMANA_REVISÃO].md`
- Bimestre 1: `9.md` (semana de revisão)
- Bimestre 2: `19.md`
- Bimestre 3: `29.md`
- Bimestre 4: `39.md`

## Regras

1. **NUNCA crie conteúdo novo.** Copie e cole exatamente o que está nas aulas `.4`.
2. **NUNCA altere definições.** As definições devem ser idênticas ao original.
3. **NUNCA altere as questões do Quiz.** Copie os blocos inteiros como estão.
4. **Use os títulos exatos** do Currículo Macro para nomear cada seção de semana.
5. **Mantenha a ordem cronológica** das semanas (1→2→3→...→8).
6. O arquivo final NÃO possui sessões de Perceber, Recordar ou Narrar — apenas Revisão + Quiz.

## Output
- Arquivo `.md` completo com revisão bimestral pronto para publicação.
- Confirmação: `Revisão bimestral montada: [N] semanas, [N] termos, [N] questões.`
