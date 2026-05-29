---
description: Pipeline completo de criação de conteúdo (7 etapas) para uma semana inteira
---

# /full-pipeline — Pipeline Completo de Criação de Conteúdo

Este workflow executa **todas as etapas** do fluxo editorial para uma semana inteira (3 aulas), da adequação curricular até a publicação final.

---

## Entrada

O usuário informa:
- O **ano** (ex: "5º ano") — se não informado, pergunte
- O **número da semana** (ex: "semana 38")
- O **movimento artístico** (se a semana ainda não existir no Currículo Macro)

---

## Etapa 0 — Adequação Curricular

Use esta etapa quando o usuário trouxer uma lista de temas, um arquivo `0 - Assuntos para trabalhar no ano` ou pedir uma versão em `novo padrão`.

- Execute `/curriculum-macro-adapter`.
- Garanta que cada semana tenha `x.1`, `x.2` e `x.3`.
- Use `x.1` como tema central.
- Use `x.2` e `x.3` como desdobramentos diretos.
- Extraia palavras-chave de `x.1` e confirme que `x.2` e `x.3` nascem delas.
- Não crie plano de aula nesta etapa.

Se o Currículo Macro já estiver aprovado e não houver pedido de adequação, pule para a Etapa 1.

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
2. Para cada aula finalizada, localizar `- N.M [Título]` e adicionar ` ✅`
3. Adicionar ` ✅` ao título `## Semana N - **Tema central**`
4. Adicionar bloco de **termo da semana** (um único termo, compartilhado pelas 3 aulas):

```markdown
# Semana N
[TermoCentral] ✅
```

> **Padrão antigo (descontinuado)**: blocos com 3 termos por semana não são mais utilizados.

---

## Confirmação Final

Ao concluir as 3 aulas, reporte:

```
✅ PIPELINE COMPLETO — Semana [X], [Y]º Ano

📋 Etapas executadas:
  0. Adequação curricular: [criada/já existia/não solicitada]
  1. Currículo Macro: [criado/já existia]
  2. Matriz Curricular: [criada/já existia]
  3. Visão Pedagógica: [criada/já existia]
  4. Aulas criadas (tema central: [TEMA] | termo da semana: [TERMO]):
    - X.1 — [Título] ✅
    - X.2 — [Título] ✅
    - X.3 — [Título] ✅
  5. Currículo Macro: 3/3 aulas + termo da semana marcado ✅

📁 Arquivos salvos em: [caminho]
```

---

## Notas

- Este workflow é **idempotente**: se uma etapa já foi executada, ele a pula.
- Cada etapa valida os outputs da anterior antes de prosseguir.
- Se qualquer etapa falhar, o pipeline para e reporta o erro.
- O usuário pode executar etapas individuais separadamente usando os workflows `/create-macro`, `/create-matriz`, `/create-vision`, `/create-lesson`.
