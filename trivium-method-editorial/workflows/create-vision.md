---
description: Criar Visão e Plano Pedagógico a partir da Matriz Curricular
---

# /create-vision — Desenvolver Visão e Plano Pedagógico

Este workflow gera a **Visão e Plano Pedagógico** de uma semana a partir dos dados da Matriz Curricular. Funciona para qualquer ano (1º ao 5º).

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

## Passo 1 — Ler a Matriz Curricular

Abra o arquivo `2 - Matriz-Curricular-objetivos - [X]º ANO.md` do ano correspondente.

Localize a seção `## Semana [X]` correspondente ao número informado.

Extraia:
- **Título da semana**
- **Tema central**
- **Tabela de aulas** (número, título, objetivo teológico-pedagógico)
- **Conceitos da semana**

---

## Passo 2 — Gerar a Visão e Plano Pedagógico

Com os dados extraídos, gere um bloco completo seguindo **exatamente** o formato das semanas já existentes no arquivo `3 - Visão e Plano pedagogico - [X]º ANO.md`.

### Seções obrigatórias (nesta ordem):

1. **Cabeçalho**
   ```
   ## 📗 Semana [X] – **[Título]**
   ## 📖 **visão teológica**
   ```
   Emoji: usar o ciclo 📗, 📘, 📙, 📕.

2. **📖 visão teológica**
   - Citação bíblica de abertura (blockquote)
   - Contexto teológico (2–4 parágrafos)
   - 📜 **bases bíblicas fundamentais** (3–4 versículos)
   - 📖 **síntese doutrinária** (blockquote de 1–2 linhas)

3. **🎯 objetivo geral do módulo**
   - Lista de 4–5 pontos.

4. **🧱 estrutura do módulo [X]**
   - Tabela: Aula, Título, Tema central, Versículo-chave.
   - 3 aulas (X.1, X.2, X.3).

5. **🔁 progressão pedagógica**
   - 3 blocos numerados (um por aula), cada um com 3 linhas de setas (→).
   - **Transição para o módulo seguinte** (1–2 linhas).

6. **🕊️ mensagem central do módulo**
   - Blockquote poético de 3–4 linhas.

7. **🪶 resumo pedagógico (para rise ou canvas)**
   - eixo temático | virtude principal | habilidade formativa | símbolo-chave | resultado esperado.

---

## Passo 3 — Salvar no arquivo

Anexe o conteúdo gerado **ao final** do arquivo `3 - Visão e Plano pedagogico - [X]º ANO.md`.

---

## Passo 4 — Confirmar ao usuário

Reporte:

- ✅ Visão e Plano Pedagógico da **Semana [X] — [Título]** desenvolvido para o **[X]º Ano**
- ✅ Salvo em `[nome do arquivo]`
- 📋 Seções geradas: visão teológica, objetivos, estrutura, progressão, mensagem, resumo

---

## Regras de estilo

- Tom **teológico-pedagógico**, cosmovisão **cristã reformada**.
- Versículos preferencialmente **ARA ou ARC**.
- Linguagem **clara, didática e reverente**.
- **Consistência** com semanas anteriores.
- Caixa baixa nos títulos de seção.
