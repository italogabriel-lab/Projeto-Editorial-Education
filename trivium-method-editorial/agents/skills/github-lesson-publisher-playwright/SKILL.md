---
name: github-lesson-publisher-playwright
description: Use esta skill quando o usuário quiser publicar uma aula local do projeto editorial no GitHub via interface web (UI). Ela copia o conteúdo de um arquivo como 24.1.md, resolve o caminho remoto no formato br/_/3-belas-artes-24.1/README.md, e commita via interface web do GitHub usando Playwright.
---

# Skill: Publicação de aula no GitHub via Playwright (UI)

Use esta skill para publicar aulas Markdown no repositório `bibline/curriculum` via gh CLI.

Ela foi desenhada para o fluxo do usuário no 3º ano, mas aceita anos de `1` a `5`.

## Quando usar

- Quando o usuário pedir para publicar uma aula local como `24.1.md`
- Quando o destino no GitHub for uma pasta com `README.md`
- Quando a publicação precisar ser confiável e recurrente

## O que esta skill faz

1. Resolve o arquivo local da aula
2. Extrai o título do Markdown para a mensagem de commit
3. Abre navegador Playwright na página de edição do arquivo no GitHub
4. Preenche o conteúdo do arquivo via UI
5. Clica no botão "Commit changes" na interface web
6. Faz push automaticamente (via GitHub)

## Regra de caminhos

### Origem local

Base:

`Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/`

Exemplo do 3º ano:

`3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/24.1.md`

### Destino GitHub

Padrão:

`br/_/[N]-belas-artes-[AULA]/README.md`

Exemplo:

`br/_/3-belas-artes-24.1/README.md`

## Comando principal (via UI - interface web)

```bash
npm run publish:lesson:github:ui -- --lesson 24.1 --year 3
```

## Via gh CLI (alternativo)

```bash
npm run publish:lesson:github -- --lesson 24.1 --year 3
```

## Comando de validação antes de publicar

```bash
npm run publish:lesson:github -- --lesson 24.1 --year 3 --check-only
```

Use `--check-only` para confirmar:

- caminho local
- caminho remoto
- mensagem de commit extraída do título

## Pré-requisitos

- Playwright instalado (`npm run playwright:install`)
- Autenticado no navegador GitHub (sessão ativa)
- Acesso de escrita ao repositório `bibline/curriculum`

## Observações operacionais

- O script clona o repositório com depth 1 para ser rápido
- Usa um diretório temporário que é limpo depois
- O título da aula (primeiro `#`) vira mensagem de commit
- Push direto na branch master

## Parâmetros úteis

- `--lesson 24.1` - Número da aula
- `--year 3` - Ano escolar
- `--check-only` - Só valida caminhos
- `--headless` - Executar navegador sem interface visual
- `--owner` (padrão: bibline) - Owner do repo
- `--repo` (padrão: curriculum) - Nome do repo

## Script desta skill

Use:

`scripts/publish-lesson-github.mjs`

## Validação mínima após publicar

Confirme:

1. a URL final do GitHub
2. se o `README.md` remoto mostra o conteúdo esperado

## Quando não usar

- Publicação em lote de várias aulas
- Publicação em branches diferentes da master
- Alterações estruturais no currículo macro
