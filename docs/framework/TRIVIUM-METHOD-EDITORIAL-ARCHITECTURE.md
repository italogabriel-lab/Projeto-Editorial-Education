# Trivium Method Editorial Architecture

## Leitura do AIOX

Ao analisar o AIOX neste repositório, os padrões estruturais mais importantes ficaram claros:

1. Existe uma camada de governança explícita (`constitution`, `core-config`, `install-manifest`).
2. Agentes, workflows, checklists e templates vivem em árvores separadas, com responsabilidade distinta.
3. A instalação é orientada por manifesto e inventário, não por conhecimento implícito.
4. O sistema assume `CLI First`, deixando observabilidade e UI em camadas secundárias.
5. Mudanças relevantes são story-driven.

## Adaptação para o Trivium Method Editorial

O Trivium Method Editorial replica essa lógica em cinco camadas:

1. **Governança**: `.trivium-method-editorial-core/constitution.md`, `.trivium-method-editorial-core/core-config.yaml`, `.trivium-method-editorial-core/install-manifest.json`
2. **Registry Runtime**: `.trivium-method-editorial-core/data/asset-registry.json`, `.trivium-method-editorial-core/data/hierarchy.json`, scripts de inventory e doctor
3. **Orquestração**: wrappers em `.trivium-method-editorial-core/development/agents/`, workflows YAML e checklists
4. **Biblioteca Editorial**: `trivium-method-editorial/` com agents, workflows, templates, knowledge base e scripts
5. **Observabilidade**: `public/`, `src/sync.js`, `*.html` e `.github/workflows/`

## Fonte Canônica

Para o empacotamento do framework, a fonte editorial escolhida foi `trivium-method/`.

Motivos:

- já possui a biblioteca mais organizada do fluxo editorial
- reúne skills, templates, workflows e automações em um único lugar
- reduz o problema atual de ter a mesma estrutura replicada em mais de um diretório

## Resultado Prático

O pacote `create-trivium-method-editorial` instala uma workspace com:

- `.trivium-method-editorial-core` no estilo AIOX
- `trivium-method-editorial/` como biblioteca editorial pronta para replicação
- documentação operacional em `docs/`
- diretório `disciplines/` para bases específicas da equipe
- camada de dashboard herdada da operação atual
