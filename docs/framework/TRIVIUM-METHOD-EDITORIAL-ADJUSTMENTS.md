# Trivium Method Editorial Adjustments

## Ajustes realizados

1. O fluxo editorial foi reorganizado em uma arquitetura inspirada no AIOX.
2. Foi criado o pacote `create-trivium-method-editorial`; o comando publico `npx create-trivium-method-editorial` ainda depende de publicacao no npm.
3. Os ativos editoriais foram inventariados em um registry central.
4. Foram gerados wrappers de agentes em `.trivium-method-editorial-core/development/agents/`.
5. Foram criados workflows machine-readable para orquestração principal.
6. Três skills legados que estavam incompletos receberam `SKILL.md`.

## Ajustes ainda exigidos por projeto

1. `src/sync.js` depende de credenciais e do ID do projeto no GitHub Projects.
2. `public/app.js` ainda carrega metas e disciplina padrão da operação atual.
3. Os workflows do GitHub exigem:
   - secret `TRIVIUM-METHOD-EDITORIAL_GITHUB_TOKEN`
   - variable `TRIVIUM-METHOD-EDITORIAL_PROJECT_ID`
4. Cada time precisa plugar sua disciplina dentro de `disciplines/`.

## Decisão de empacotamento

- `trivium-method/` virou a fonte editorial canonica do pacote
- `Projeto Bibline Academy/.agent` e `Projeto Bibline Academy/editorial-squad` ficam como histórico e referência
- o smoke test real foi validado localmente via tarball do pacote

## Ganho estrutural

Antes:

- ativos editoriais distribuídos em múltiplos diretórios
- nenhuma instalação replicável
- ausência de camada de governança no estilo AIOX

Depois:

- governança explícita
- inventário único
- instalador empacotado e pronto para publicacao
- biblioteca editorial replicável
- separação clara entre core, library, docs e observability
