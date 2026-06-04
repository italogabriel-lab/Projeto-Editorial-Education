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
- **Palavras-chave estruturantes** do tema central, quando existirem na Matriz

---

## Passo 2 — Gerar a Visão e Plano Pedagógico

Com os dados extraídos, gere um bloco completo seguindo **exatamente** o formato das semanas já existentes no arquivo `3 - Visão e Plano pedagogico - [X]º ANO.md`.

### Seções obrigatórias (novo padrão — semana como unidade):

1. **Cabeçalho** (sentence-case, sem emoji)
   ```
   ## Semana [X] - [Tema central da semana]

   ## Visão teológica
   ```

2. **Visão teológica**
   - Trate o tema central da semana à luz da cosmovisão cristã reformada
   - Lembre que a semana é uma unidade: a aula `x.1` define o coração, `x.2` desenvolve o subtópico 1, `x.3` desenvolve o subtópico 2
   - Mantenha a perspectiva de Belas Artes e artes visuais
   - Use natureza, casa, igreja, objetos ou histórias bíblicas como exemplos apenas quando conduzirem à observação de imagem, desenho, forma, linha, cor, textura, espaço, composição, obra de arte ou beleza visual

3. **Objetivo geral do módulo**
   - 2–3 parágrafos descrevendo como a semana leva o aluno a reconhecer o tema central e percorrer os dois desdobramentos

4. **Estrutura do módulo [X]**
   - Tabela: `Aula | Título | Função pedagógica | Versículo de apoio`
   - 3 linhas (x.1, x.2, x.3) com funções `Coração da semana`, `Subtópico 1` e `Subtópico 2`

5. **Progressão pedagógica**
   - 3 blocos numerados (um por aula):
     - `x.1` — apresenta o tema, fixa a definição central
     - `x.2` — retoma a definição de `x.1` e aplica ao primeiro recorte
     - `x.3` — retoma a definição de `x.1` e fecha o segundo recorte
   - Cada bloco deve declarar quais palavras-chave de `x.1` serão retomadas no exemplo central da aula

6. **Mensagem central do módulo**
   - 1 parágrafo que sintetiza o eixo da semana

7. **Resumo pedagógico**
   - eixo temático | palavras-chave | aula coração | subtópico 1 | subtópico 2 | resultado esperado

8. **Transição para a semana seguinte**
   - 1–2 linhas conectando ao tema central da próxima semana

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
