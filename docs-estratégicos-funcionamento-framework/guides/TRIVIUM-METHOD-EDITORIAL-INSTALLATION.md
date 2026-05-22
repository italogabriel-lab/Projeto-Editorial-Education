# Instalação do Trivium Method Editorial

## Comando

```bash
npx create-trivium-method-editorial meu-framework-editorial
```

Enquanto o pacote `create-trivium-method-editorial` nao for publicado no npm, valide localmente com um tarball gerado por `npm pack`.

## Depois da instalação

```bash
cd meu-framework-editorial
npm run trivium-method-editorial:inventory
npm run trivium-method-editorial:doctor
```

## O que o instalador cria

- `.trivium-method-editorial-core/`
- `trivium-method-editorial/`
- `disciplines/`
- `docs/`
- camada atual de observabilidade
- `public/data.json` com seed neutro para o dashboard

## Configurações obrigatórias

1. Ajuste os dados da sua disciplina em `disciplines/`
2. Configure `TRIVIUM-METHOD-EDITORIAL_GITHUB_TOKEN`
3. Configure `TRIVIUM-METHOD-EDITORIAL_PROJECT_ID`
4. Revise `docs/framework/ADJUSTMENTS.md`
5. Execute o sync para trocar o seed inicial de `public/data.json` pelos dados reais da sua operacao
