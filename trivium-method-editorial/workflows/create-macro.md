---
description: Distribuir movimentos artísticos no Currículo Macro semanal
---

# /create-macro — Distribuir Movimento Artístico no Currículo Macro

Este workflow distribui os tópicos de um **movimento artístico** em **semanas** no formato do Currículo Macro. Funciona para qualquer ano (1º ao 5º).

---

## Entrada

O usuário informa:
- O **ano** (ex: "5º ano") — se não informado, pergunte
- O **movimento artístico** (ex: "Arte Bizantina")
- O **intervalo de semanas** (ex: "semanas 37 e 38")

Se o intervalo não for informado, pergunte ao usuário.

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

**Arquivos:**
- Movimentos: `[PASTA_ESTRUTURA]/0 - Movimentos Artisticos trabalhados.md` (ou equivalente `0 - Assuntos...`)
- Macro: `[PASTA_ESTRUTURA]/1 - Curriculo Macro - ... - [X]º ANO.md`

> **Dica:** Se os nomes exatos dos arquivos forem diferentes, use `list_dir` para descobrir os nomes reais.

---

## Passo 1 — Ler o Movimento Artístico

Abra o arquivo de movimentos artísticos do ano correspondente.

Localize a seção correspondente ao movimento informado.

Extraia todos os **tópicos** listados (contexto histórico, cosmovisão, materiais e técnicas, etc).

---

## Passo 2 — Distribuir em semanas

Distribua os tópicos extraídos nas semanas informadas, **3 dias por semana**, seguindo o formato:

```markdown
## Semana [X] – **[Título do Movimento]**

- Dia 1: [Tópico/título da aula 1]

- Dia 2: [Tópico/título da aula 2]

- Dia 3: [Tópico/título da aula 3]
```

### Regras de distribuição:

- Cada semana tem **exatamente 3 dias** (3 aulas).
- Os títulos de cada dia devem ser **curtos e didáticos**.
- A distribuição deve seguir uma **progressão lógica**: contexto → técnica → forma → legado.
- Semanas de **Revisão** e **Provas** seguem o padrão existente.

---

## Passo 3 — Anexar ao Currículo Macro

Anexe o conteúdo gerado **ao final** do arquivo de Currículo Macro do ano correspondente.

- **Não** preencha os termos com ✅ — isso é feito pelo workflow `/publish`.
- Mantenha o formato consistente com as semanas já existentes.

---

## Passo 4 — Confirmar ao usuário

Reporte:

- ✅ Movimento **[Nome]** distribuído nas semanas **[X–Y]** do **[X]º Ano**
- ✅ Salvo em `[nome do arquivo]`
- 📋 Semanas geradas: [lista de semanas com títulos dos dias]

---

## Referência de ciclo de semanas

| Semanas   | Tipo               |
|-----------|---------------------|
| 1–8       | Conteúdo (8 sem.)  |
| 9         | Revisão            |
| 10        | Provas             |
| 11–18     | Conteúdo (8 sem.)  |
| 19        | Revisão            |
| 20        | Provas             |
| 21–28     | Conteúdo (8 sem.)  |
| 29        | Revisão            |
| 30        | Provas             |
| 31–38     | Conteúdo (8 sem.)  |
| 39        | Revisão            |
| 40        | Provas             |
