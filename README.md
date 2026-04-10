# TriviumOS

Framework editorial inspirado na metodologia e na arquitetura do AIOX.

## Objetivo

Transformar o fluxo editorial atual em um framework replicavel para toda a equipe, com:

- governanca explicita
- instalacao via `npx`
- catalogo unico de agentes, workflows, templates e scripts
- separacao entre core do framework, biblioteca editorial e bases por disciplina

## Estrutura

```text
.
├── .triviumos-core/            # instalado pelo scaffolder
├── triviumos/                  # biblioteca editorial instalada
├── disciplines/                # conhecimento especifico por disciplina
├── docs/                       # arquitetura, hierarquia e guias
├── trivium-method/             # fonte editorial canonica do empacotamento
├── public/ src/ *.html         # camada atual de observabilidade
└── package.json                # pacote create-triviumos
```

## Instalador

```bash
npx create-triviumos meu-framework-editorial
```

O comando acima passa a funcionar publicamente depois da publicacao do pacote `create-triviumos` no npm. Antes disso, a validacao real pode ser feita com `npm pack` + `npm exec --package`.

O CLI gera:

- `.triviumos-core` com constitution, config, registries, wrappers de agentes, workflows e checklists
- `triviumos/` com a biblioteca editorial instalada
- `docs/` com arquitetura, ajustes e guias operacionais
- `disciplines/` para cada membro plugar sua propria base de conhecimento
- `public/data.json` inicial neutro, pronto para ser populado pelo sync da operacao

## Artefatos principais

- `src/data/editorial-registry.json`: inventario canonico do framework
- `src/lib/install.mjs`: motor de scaffolding do instalador
- `scaffold/triviumos-core/`: runtime instalado no projeto destino
- `docs/framework/TRIVIUMOS-ARCHITECTURE.md`: leitura arquitetural do AIOX e adaptacao para o TriviumOS
- `docs/framework/TRIVIUMOS-HIERARCHY.md`: hierarquia de camadas e agentes
- `docs/framework/TRIVIUMOS-ADJUSTMENTS.md`: lacunas corrigidas e configuracoes ainda necessarias

## Qualidade

```bash
npm run lint
npm run typecheck
npm test
```

## Estado atual

- pacote `create-triviumos` funcional
- smoke test do instalador validado em `/tmp/triviumos-smoke-2`
- tarball do npm isolado de snapshots operacionais, relatorios e artefatos gerados
- `npx create-triviumos` publico ainda depende de publicacao no npm
- 21 agentes catalogados
- 5 workflows do framework
- 7 templates canonicos
- 35 scripts inventariados
