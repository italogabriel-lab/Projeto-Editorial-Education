---
description: Pipeline completo de criação de conteúdo (7 etapas) para uma semana inteira
---

# /full-pipeline — Pipeline Completo de Criação de Conteúdo

Este workflow executa **todas as 7 etapas** do fluxo editorial para uma semana inteira (3 aulas), do Currículo Macro até a publicação final.

---

## Entrada

O usuário informa:
- O **ano** (ex: "5º ano") — se não informado, pergunte
- O **número da semana** (ex: "semana 38")
- O **movimento artístico** (se a semana ainda não existir no Currículo Macro)

---

## Etapa 1 — Currículo Macro

Verifique se a semana já existe no arquivo `1 - Curriculo Macro`.

- **Se NÃO existe**: Execute `/create-macro` para distribuir o movimento na semana.
- **Se JÁ existe**: Pule para a Etapa 2.

---

## Etapa 2 — Matriz Curricular

Verifique se a semana já existe no arquivo `2 - Matriz-Curricular-objetivos`.

- **Se NÃO existe**: Execute `/create-matriz` para gerar objetivos e conceitos.
- **Se JÁ existe**: Pule para a Etapa 3.

---

## Etapa 3 — Visão e Plano Pedagógico

Verifique se a semana já existe no arquivo `3 - Visão e Plano pedagogico`.

- **Se NÃO existe**: Execute `/create-vision` para gerar o plano completo.
- **Se JÁ existe**: Pule para a Etapa 4.

---

## Etapas 4-7 — Criação das 3 Aulas

Para cada uma das 3 aulas da semana (X.1, X.2, X.3):

// turbo
Execute `/create-lesson` com o número da aula e o ano.

Isso dispara internamente o **Context Loop**:
- **Passo 4** (Writer) → Redação do conteúdo
- **Passo 5** (Standardizer) → Padronização Rise Blocks
- **Passo 6** (Reviewer) → Revisão de qualidade
- **Passo 7** (Copywriter) → Ajustes finais

---

## Etapa 5 — Registro no Currículo Macro

> **AUTOMÁTICO**: Executar sempre ao final das 3 aulas da semana.

1. Abrir `[Base]/Estrutura Curricular - [Nº] ANO/1 - Curriculo Macro - *.md`
2. Para cada aula finalizada, localizar `- Dia N: [Tema]` e adicionar ` ✅`
3. Adicionar ` ✅` ao título `## Semana N – **Tema**`
4. Adicionar bloco de termos:

```markdown
# Semana N
Termo1 ✅
Termo2 ✅
Termo3 ✅
```

---

## Confirmação Final

Ao concluir as 3 aulas, reporte:

```
✅ PIPELINE COMPLETO — Semana [X], [Y]º Ano

📋 Etapas executadas:
  1. Currículo Macro: [criado/já existia]
  2. Matriz Curricular: [criada/já existia]
  3. Visão Pedagógica: [criada/já existia]
  4. Aulas criadas:
    - X.1 — [Título] | Termo: [TERMO1] ✅
    - X.2 — [Título] | Termo: [TERMO2] ✅
    - X.3 — [Título] | Termo: [TERMO3] ✅
  5. Currículo Macro: 3/3 aulas + 3 termos marcados ✅

📁 Arquivos salvos em: [caminho]
```

---

## Notas

- Este workflow é **idempotente**: se uma etapa já foi executada, ele a pula.
- Cada etapa valida os outputs da anterior antes de prosseguir.
- Se qualquer etapa falhar, o pipeline para e reporta o erro.
- O usuário pode executar etapas individuais separadamente usando os workflows `/create-macro`, `/create-matriz`, `/create-vision`, `/create-lesson`.
