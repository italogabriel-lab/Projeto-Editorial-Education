---
description: Gerar Matriz Curricular a partir do Currículo Macro semanal
---

# /create-matriz — Gerar Matriz Curricular

Este workflow gera a entrada detalhada da **Matriz Curricular** (arquivo 2) a partir dos dados de uma semana no **Currículo Macro** (arquivo 1). Funciona para qualquer ano (1º ao 5º).

---

## Entrada

O usuário informa:
- O **ano** (ex: "5º ano") — se não informado, pergunte
- O **número da semana** (ex: "semana 38")

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

## Passo 1 — Ler o Currículo Macro

Abra o arquivo `1 - Curriculo Macro - ... - [X]º ANO.md` do ano correspondente.

Localize a seção `## Semana [X]` correspondente ao número informado.

Extraia:
- **Título da semana** (ex: "Arte Bizantina")
- **Títulos dos 3 dias** (Dia 1, Dia 2, Dia 3)

---

## Passo 2 — Gerar a entrada da Matriz Curricular

Com os dados extraídos, gere um bloco seguindo **exatamente** o formato das semanas existentes no arquivo `2 - Matriz-Curricular-objetivos - [X]º ANO.md`.

### Formato obrigatório:

```markdown
## 📗 Semana [X] – **[Título da semana]**

**Tema central:** [Frase que conecta o conteúdo artístico à cosmovisão cristã reformada.]

| Aula | Título                         | Objetivo Teológico-Pedagógico                                      |
| ---- | ------------------------------ | ------------------------------------------------------------------ |
| X.1  | **[Título do Dia 1]**          | [Objetivo em 1 frase, começando com verbo no infinitivo.]          |
| X.2  | **[Título do Dia 2]**          | [Objetivo em 1 frase, começando com verbo no infinitivo.]          |
| X.3  | **[Título do Dia 3]**          | [Objetivo em 1 frase, começando com verbo no infinitivo.]          |

**Conceitos da semana:** [Termo1], [Termo2], [Termo3]
```

### Regras de geração:

1. **Emoji do cabeçalho**: use o ciclo 📗, 📘, 📙, 📕 (repetindo a cada 4 semanas de conteúdo, pulando revisão/prova).
2. **Tema central**: 1 frase conectando conteúdo artístico à fé cristã reformada.
3. **Títulos das aulas**: conforme aparecem no Currículo Macro, em negrito.
4. **Objetivos Teológico-Pedagógicos**: verbo no infinitivo + conexão bíblica/teológica, máximo 1 frase.
5. **Conceitos da semana**: 3 termos-chave substantivos concisos.
6. **Separador**: adicionar `---` após o bloco.

---

## Passo 3 — Salvar na Matriz Curricular

Anexe o conteúdo gerado **ao final** do arquivo `2 - Matriz-Curricular-objetivos - [X]º ANO.md`.

---

## Passo 4 — Confirmar ao usuário

Reporte:

- ✅ Matriz Curricular da **Semana [X] — [Título]** gerada para o **[X]º Ano**
- ✅ Salva em `[nome do arquivo]`
- 📋 Aulas: X.1, X.2, X.3
- 📋 Conceitos: [Termo1], [Termo2], [Termo3]

---

## Referência de emojis por semana

O ciclo de emojis repete a cada 4 semanas de conteúdo:

| Posição no ciclo | Emoji |
|------------------|-------|
| 1ª               | 📗    |
| 2ª               | 📘    |
| 3ª               | 📙    |
| 4ª               | 📕    |
