---
description: Salvar aula localmente e, opcionalmente, publicar no GitHub via MCP
---

# /publish — Salvar Aula Localmente (e opcionalmente publicar no GitHub)

Este workflow salva a aula finalizada localmente. A publicação no GitHub é **opcional**. Funciona para qualquer ano (1º ao 5º).

---

## Pré-requisitos

- O conteúdo da aula deve estar **finalizado e revisado**.
- O número da aula (ex: `36.3`), o título e o **ano** devem ser conhecidos.

---

## Resolução de Caminhos

| Ano | Pasta do Ano | GitHub Path |
|-----|-------------|-------------|
| 1º | `1º Ano` | `br/_/1-belas-artes/` |
| 2º | `2º Ano - DA CRIAÇÃO ATÉ A ARTE BIZANTINA` | `br/_/2-belas-artes/` |
| 3º | `3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE` | `br/_/3-belas-artes/` |
| 4º | `4º Ano - IMPRESSIONISMO ATÉ A ARTE CONTEMPORÂNEA` | `br/_/4-belas-artes/` |
| 5º | `5º Ano - MANEIRISMO ATÉ O REALISMO AMERICANO` | `br/_/5-belas-artes/` |

**Caminho local:**
```
/home/italo.gabriel/Documents/Bibline Academy/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/[PASTA_DO_ANO]/[NUMERO_AULA].md
```

---

## Passo 1 — Salvar localmente (obrigatório)

Salve o conteúdo markdown da aula no caminho local do ano correspondente.

- Use `write_to_file` com `Overwrite: true` caso o arquivo já exista.
- O conteúdo deve ser o markdown final da aula (formato Rise Blocks).

---

## Passo 2 — Registrar Termo no Currículo Macro (obrigatório)

Abra o arquivo `1 - Curriculo Macro - ... - [X]º ANO.md`:

- Na seção `# Semana [X]` correspondente, adicione o termo principal com ✅
- Se a seção não existir, crie-a

---

## Passo 3 — Confirmar ao usuário (obrigatório)

Reporte:
- ✅ Salvo localmente em `[caminho completo]`
- ✅ Termo `[TERMO]` registrado no Currículo Macro

---

## Passo 4 — Publicar no GitHub via MCP (OPCIONAL — somente se solicitado)

> **Execute este passo APENAS se o usuário pedir explicitamente.**

Use o MCP tool `create_or_update_file` do server `github` com:

```
owner: bibline
repo: curriculum
branch: master
path: [GITHUB_PATH]/[NUMERO_AULA].md
content: [conteúdo completo do arquivo markdown]
message: Aula [NUMERO_AULA] — [Título da Aula]
```

Após publicar, adicione à confirmação:
- ✅ Publicado no GitHub em `bibline/curriculum` → `[GITHUB_PATH]/[NUMERO_AULA].md`

---

## Referência rápida de numeração

Cada semana segue o padrão:
- `X.1` — Aula 1
- `X.2` — Aula 2
- `X.3` — Aula 3
