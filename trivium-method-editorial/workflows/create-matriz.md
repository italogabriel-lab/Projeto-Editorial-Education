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

### Formato obrigatório (novo padrão — semana como unidade):

```markdown
## Semana [X] - [Tema central da semana]

**Tema central**, [Tema da semana, idêntico ao título de x.1]. A aula [X].1 apresenta o coração do tema. As aulas [X].2 e [X].3 desenvolvem seus dois desdobramentos.

| Aula | Título | Objetivo teológico-pedagógico |
| --- | --- | --- |
| X.1 | [Título do Dia 1 — idêntico ao de x.1] | Apresentar [tema central] como coração da semana e eixo da definição. |
| X.2 | [Título do Dia 2] | Reconhecer [tema de x.2] como primeiro desdobramento do tema principal. |
| X.3 | [Título do Dia 3] | Praticar [tema de x.3] como segundo desdobramento do tema principal. |

**Conceitos da semana**, [Título de x.1], [Título de x.2], [Título de x.3]

**Palavras-chave estruturantes**, [2 a 5 palavras literais do tema central e da definição curta esperada]

---
```

### Regras de geração:

1. **Cabeçalho sem emoji** (limpo, sentence-case): `## Semana [X] - [Tema]`.
2. **Tema central**: a frase de abertura usa o template "A aula X.1 apresenta o coração do tema. As aulas X.2 e X.3 desenvolvem seus dois desdobramentos."
3. **Títulos das aulas**: conforme aparecem no Currículo Macro, **sem negrito**, alinhados ao tema central.
4. **Objetivos**: padrão `Apresentar / Reconhecer / Praticar` para x.1, x.2 e x.3 respectivamente.
5. **Conceitos da semana**: lista dos 3 títulos das aulas (não três termos distintos).
6. **Palavras-chave estruturantes**: listar palavras que devem reaparecer em `x.2` e `x.3` nos exemplos e atividades.
7. **Separador**: adicionar `---` após o bloco.
8. **Importante**: o `[Tema central da semana]` precisa ser idêntico ao título de `x.1`. A definição curta de `x.1`, `x.2` e `x.3` é a mesma, derivada deste tema.

---

## Passo 3 — Salvar na Matriz Curricular

Anexe o conteúdo gerado **ao final** do arquivo `2 - Matriz-Curricular-objetivos - [X]º ANO.md`.

---

## Passo 4 — Confirmar ao usuário

Reporte:

- ✅ Matriz Curricular da **Semana [X] — [Tema central]** gerada para o **[X]º Ano**
- ✅ Salva em `[nome do arquivo]`
- 📋 Aulas: X.1 (coração), X.2 (subtópico 1), X.3 (subtópico 2)
- 📋 Tema central da semana: [Tema]
