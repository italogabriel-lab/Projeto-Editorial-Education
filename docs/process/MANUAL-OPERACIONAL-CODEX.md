# Manual operacional do framework editorial no Codex

Data de referência, 24 de abril de 2026.

Este documento é o mapa operacional do framework editorial deste repositório para uso com Codex. O objetivo é permitir que qualquer pessoa nova na equipe entenda:

- como o fluxo editorial funciona do início ao fim
- quais agentes e comandos existem
- quais workflows, templates e scripts sustentam o processo
- como acionar cada peça no Codex
- onde estão as fontes de verdade do projeto

## 1. Resumo executivo

O framework editorial deste projeto opera em cinco camadas conectadas:

1. `CODEX.md` e `AGENTS.md` definem as regras globais do ambiente.
2. `.codex/` organiza comandos, regras, skills e personas para uso diário no Codex.
3. `trivium-method-editorial/` guarda a base canônica do framework, com workflows, templates, knowledge base e scripts.
4. `Projeto - Bibline Academy ( Produção de Aulas)/` guarda o conteúdo curricular real, com aulas, currículo macro, matriz, visão pedagógica, links de imagens e tickets.
5. `scripts/`, `src/` e as páginas HTML do Vision Board sustentam automação, publicação e monitoramento operacional.

Em termos práticos, a operação editorial segue este raciocínio:

```text
Orquestração
  -> pesquisa
  -> redação
  -> padronização
  -> revisão
  -> polimento
  -> revisão semanal e prova
  -> publicação
  -> versionamento e monitoramento
```

## 2. Fontes de verdade

Antes de qualquer execução, a equipe precisa saber o que manda mais.

### 2.1 Regras principais

- `AGENTS.md`
- `CODEX.md`
- `.codex/rules/project-context.md`
- `.codex/rules/editorial-pipeline.md`
- `.codex/rules/writing-quality.md`
- `.codex/rules/title-synchronization.md`
- `.codex/rules/repo-operations.md`

### 2.2 Fonte oficial de títulos

A fonte absoluta dos títulos de aula é sempre o arquivo `1 - Curriculo Macro` de cada ano.

Se houver divergência entre:

- aula `.md`
- matriz curricular
- visão pedagógica
- descrições de tickets
- revisão semanal

o título correto é o do Currículo Macro.

### 2.3 Template oficial de aula

O golden template é:

- `trivium-method-editorial/templates/padrao_final_aula.md`

### 2.4 Base de conhecimento central

Os agentes e workflows devem consultar, quando necessário:

- `trivium-method-editorial/knowledge-base/doutrina-pedagogica.md`
- `trivium-method-editorial/knowledge-base/guia-de-estilo.md`
- `trivium-method-editorial/knowledge-base/rise-blocks-reference.md`
- `trivium-method-editorial/knowledge-base/visao-geral-fluxo-editorial.md`

## 3. Mapa das pastas

### 3.1 Camada Codex

```text
.codex/
├── CODEX.md
├── settings.json
├── settings.local.json
├── commands/
├── rules/
├── skills/
└── agents/
```

Função de cada pasta:

- `commands/` contém os playbooks operacionais usados como referência de execução no Codex
- `rules/` contém as regras que moldam comportamento e qualidade
- `skills/` contém fluxos reutilizáveis mais compactos
- `agents/` contém personas especializadas de apoio

### 3.2 Camada canônica do framework

```text
trivium-method-editorial/
├── knowledge-base/
├── templates/
├── workflows/
├── scripts/
└── reports/
```

Função de cada pasta:

- `knowledge-base/` guarda doutrina, estilo e regras de estrutura
- `templates/` define a forma final dos materiais
- `workflows/` descreve processos completos
- `scripts/` automatiza sincronização, auditoria e geração
- `reports/` registra diagnósticos e relatórios

### 3.3 Camada de conteúdo real

O conteúdo editorial vive principalmente em:

- `Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/`

Dentro de cada ano, a estrutura mais importante é:

```text
1 - Curriculo Macro
2 - Matriz-Curricular-objetivos
3 - Visão e Plano pedagogico
4 - Links-para-imagens-perceber
5 - Prompts-para-imagens-narrar
6 - Descrições para tickets
X.Y.md
```

## 4. Fluxo editorial completo

O fluxo editorial padrão tem sete etapas.

### 4.1 Fluxo macro

```text
Orchestrator
  -> Researcher
  -> Writer
  -> Standardizer
  -> Reviewer
  -> Copywriter
  -> Publisher
  -> DevOps
```

### 4.2 Função de cada etapa

| Etapa | Agente principal | Entrada | Saída | Arquivos base |
|---|---|---|---|---|
| 0 | Orchestrator | pedido do usuário | diagnóstico e roteamento | `.codex/commands/orchestrator.md` |
| 1 | Researcher | tema, ano, aula | relatório de pesquisa | `.codex/commands/researcher.md` |
| 2 | Writer | pesquisa + plano pedagógico | rascunho da aula | `.codex/commands/writer.md` |
| 3 | Standardizer | rascunho | aula em Rise Blocks | `.codex/commands/standardizer.md` |
| 4 | Reviewer | aula formatada | aprovação ou rejeição | `.codex/commands/reviewer.md` |
| 5 | Copywriter | aula aprovada | versão polida | `.codex/commands/copywriter.md` |
| 6 | Registro | aula final | macro, matriz, visão e revisão alinhados | `trivium-method-editorial/scripts/sync_titles.py` |
| 7 | Publisher | aula final pronta | arquivo salvo e publicado | `.codex/commands/publisher.md` |

### 4.3 Fluxos de retorno

Se a revisão reprovar:

- erro de conteúdo volta para `Writer`
- erro de estrutura volta para `Standardizer`
- erro de título ou sincronização chama `sync_titles.py`

## 5. Como chamar no Codex

No Codex, a forma mais segura de uso é por linguagem natural. A pasta `.codex/commands/` funciona como catálogo de playbooks e personas operacionais. Ela orienta a execução, mas não depende de slash commands nativos.

### 5.1 Modo recomendado para a equipe

Use linguagem natural citando claramente o agente, o comando ou o workflow.

Exemplos:

- `Use o orchestrator para me dizer o status do 3º ano`
- `Use o researcher para pesquisar a aula 26.2 do 3º ano`
- `Use o writer para redigir a aula 26.2 do 3º ano`
- `Use o reviewer para auditar esta aula`
- `Use o publisher para salvar e publicar a aula 26.2`

Esse é o modo mais seguro porque funciona diretamente com o Codex usando `AGENTS.md`, `CODEX.md`, `.codex/rules/` e `.codex/commands/`.

### 5.2 Modo comando referenciado

Outra forma prática é citar explicitamente o arquivo ou a pasta de apoio.

Exemplos:

- `Siga .codex/commands/orchestrator.md e diagnostique o 3º ano`
- `Use .codex/commands/reviewer.md para revisar a aula 26.2`
- `Aplique .codex/skills/title-sync/SKILL.md e alinhe os títulos`

### 5.3 Modo workflow

Para processos maiores, a equipe pode chamar o workflow pelo nome e descrever a tarefa.

Exemplos:

- `Execute o workflow create-lesson para a aula 26.2 do 3º ano`
- `Execute o workflow full-pipeline para a semana 26 do 3º ano`
- `Execute o workflow create-macro para distribuir um movimento nas semanas 31 e 32`
- `Execute o workflow publish para salvar e publicar`

### 5.4 Diferença prática entre Codex e Claude Code

- no Claude Code, pode haver suporte a slash commands dependendo da interface
- no Codex deste repositório, o padrão operacional é usar pedidos em linguagem natural
- os arquivos em `.codex/commands/` funcionam como contratos operacionais de comportamento
- `CODEX.md` e `AGENTS.md` são o ponto de entrada para o agente entender o framework

## 6. Catálogo de agentes, comandos e relações

### 6.1 Núcleo editorial

| Comando | Papel | Quando usar | Usa quais peças |
|---|---|---|---|
| `orchestrator` | diagnosticar, priorizar, delegar | início de sessão, status, dúvidas de rota | macro, visão pedagógica, knowledge base, workflows |
| `researcher` | pesquisar conceito, versículos, obras e trecho literário | antes de escrever aula nova | knowledge base, plano pedagógico, currículo macro |
| `writer` | escrever a aula nos 5 hábitos | depois da pesquisa | golden template, guia de estilo, doutrina |
| `standardizer` | converter para formato final Rise Blocks | depois da redação | rise blocks reference, template, capitalização |
| `reviewer` | fazer QA editorial e teológico | antes de liberar aula | checklist, style guide, template |
| `copywriter` | polir ritmo, título e clareza | depois de aprovado | guia de estilo, template |
| `publisher` | salvar localmente e publicar | no fechamento da aula | macro, paths do ano, scripts de publicação |
| `devops` | versionar, sincronizar e proteger repositório | git, push, limpeza, erros de sync | `.gitignore`, workflow publish, GitHub |

### 6.2 Builders especializados

| Comando | Papel | Quando usar | Dependências |
|---|---|---|---|
| `review-builder` | revisão semanal legada | manter fluxo antigo | aulas `.1`, `.2`, `.3` |
| `exam-builder` | prova semanal legada | manter fluxo antigo | aulas e revisão |
| `bimester-review-builder` | revisão bimestral | semanas 9, 19, 29, 39 | revisões `.4`, currículo macro |
| `bimester-exam-builder` | prova bimestral | semanas 10, 20, 30, 40 | provas `.5`, revisões `.4` |

### 6.3 Ferramentas transversais

| Comando | Papel | Quando usar | Relação com o fluxo |
|---|---|---|---|
| `capitalizer` | capitalização europeia | padronização fina | subetapa do Standardizer e Reviewer |
| `image-generator` | apoiar imagens | quando precisar gerar imagem nova | alimenta Perceber e Narrar |
| `image-link-extractor` | coletar links de imagens | quando montar `Links-para-imagens-perceber` | apoio editorial |
| `design-thinking` | UX, descoberta, estrutura de produto | desenho de ferramentas e sistemas | apoio a interface e operação |
| `ui-designer` | design de interface | páginas HTML e dashboards | apoio ao Vision Board |

### 6.4 Vision Board e analytics

| Comando | Papel | Quando usar | Arquivos principais |
|---|---|---|---|
| `vision-github-analyzer` | analisar GitHub Projects | diagnóstico de dados | `src/sync.js`, `public/data.json` |
| `vision-progress-engine` | medir progresso por ano e disciplina | leitura de metas e execução | `metas.html`, `metas-disciplinas.html` |
| `vision-bottleneck-detector` | localizar gargalos | quando números não batem ou há travas | GitHub Projects, `public/data.json` |
| `performance-analytics` | consolidar produtividade | relatórios de gestão | `trivium-method-editorial/reports/` |

## 7. Personas em `.codex/agents/`

As personas atuais são camadas de comportamento complementar. Elas não substituem os comandos principais.

| Persona | Arquivo | Papel operacional |
|---|---|---|
| `editorial-orchestrator` | `.codex/agents/editorial-orchestrator.md` | coordenação editorial e priorização |
| `publishing-operator` | `.codex/agents/publishing-operator.md` | apoio à publicação e operação de saída |
| `qa-reviewer` | `.codex/agents/qa-reviewer.md` | reforço de QA e revisão final |

Regra prática:

- use `commands/` para executar
- use `agents/` para orientar a postura do agente
- use `workflows/` para processos completos

## 8. Workflows e quando usar

Os workflows canônicos ficam em `trivium-method-editorial/workflows/`.

| Workflow | Arquivo | Função | Quando usar |
|---|---|---|---|
| `orchestrate` | `trivium-method-editorial/workflows/orchestrate.md` | sessão de orquestração | quando a equipe está sem direção |
| `create-lesson` | `trivium-method-editorial/workflows/create-lesson.md` | criar uma aula completa | aula individual |
| `produce_class` | `trivium-method-editorial/workflows/produce_class.md` | pipeline editorial de 7 etapas | produção padrão |
| `full-pipeline` | `trivium-method-editorial/workflows/full-pipeline.md` | criar uma semana completa | da semana ao publish |
| `create-macro` | `trivium-method-editorial/workflows/create-macro.md` | distribuir movimento no macro | novo bloco curricular |
| `create-matriz` | `trivium-method-editorial/workflows/create-matriz.md` | gerar matriz da semana | após macro |
| `create-vision` | `trivium-method-editorial/workflows/create-vision.md` | gerar visão pedagógica | após matriz |
| `publish` | `trivium-method-editorial/workflows/publish.md` | versionamento e sincronização | commit, push, limpeza |

### Relação entre workflows

```text
create-macro
  -> create-matriz
  -> create-vision
  -> create-lesson
  -> publish

full-pipeline
  = create-macro? + create-matriz? + create-vision? + 3x create-lesson + revisão + prova + publish

produce_class
  = pipeline interno da aula
```

## 9. Templates e para que servem

| Template | Arquivo | Uso |
|---|---|---|
| golden template | `trivium-method-editorial/templates/padrao_final_aula.md` | esqueleto final obrigatório da aula |
| exemplo final | `trivium-method-editorial/templates/exemplo_aula_final.md` | exemplo concreto de saída |
| defining | `trivium-method-editorial/templates/defining.md` | orientar o hábito Definir |
| perceiving | `trivium-method-editorial/templates/perceiving.md` | orientar o hábito Perceber |
| remembering | `trivium-method-editorial/templates/remembering.md` | orientar o hábito Recordar |
| practicing | `trivium-method-editorial/templates/practicing.md` | orientar o hábito Praticar |
| narrating | `trivium-method-editorial/templates/narrating.md` | orientar o hábito Narrar |

### Regra operacional dos templates

- o `padrao_final_aula.md` manda na estrutura total
- os templates por hábito refinam a construção interna
- o Reviewer valida conformidade contra esse conjunto

## 10. Scripts e relações com os agentes

### 10.1 Scripts canônicos do framework

| Script | Papel | Quem mais usa |
|---|---|---|
| `trivium-method-editorial/scripts/sync_titles.py` | sincronizar títulos entre macro, matriz, visão, tickets e H1 | orchestrator, devops, publisher |
| `trivium-method-editorial/scripts/check_matriz.py` | auditar divergências entre macro e matriz | orchestrator, reviewer |
| `trivium-method-editorial/scripts/align_titles.py` | alinhar títulos em arquivos específicos | devops |
| `trivium-method-editorial/scripts/align_review_titles.py` | alinhar referências de revisão | devops, reviewer |
| `trivium-method-editorial/scripts/fix_lesson_h1.py` | corrigir títulos H1 nas aulas | devops |
| `trivium-method-editorial/scripts/fix_titles.py` | limpeza cosmética de títulos | devops |
| `trivium-method-editorial/scripts/generate_descriptions.py` | regenerar descrições de tickets | orchestrator, devops |
| `trivium-method-editorial/scripts/check_project_items.py` | auditar itens de projeto | vision, devops |
| `trivium-method-editorial/scripts/create_issues*.py` | criar issues em massa | devops |
| `trivium-method-editorial/scripts/image-generation/*` | suporte à geração de imagens | image-generator |

### 10.2 Scripts operacionais do repositório

| Script | Papel | Área |
|---|---|---|
| `src/sync.js` | lê GitHub Projects e gera `public/data.json` | Vision Board |
| `scripts/publish-lesson-github.mjs` | publicação automatizada de aula no GitHub | Publisher |
| `scripts/publish-lesson-github-ui.mjs` | variante guiada de publicação | Publisher |
| `scripts/validation/check_titles.py` | validação rápida de títulos | QA editorial |
| `scripts/diagnostics/diagnose_kanban.py` | diagnóstico do Kanban | Vision Board |
| `scripts/quality/lint.mjs` | verificação de qualidade JS | app e tooling |
| `scripts/quality/typecheck.mjs` | typecheck | app e tooling |
| `scripts/generate-trivium-method-editorial-artifacts.mjs` | gerar artefatos do framework | manutenção |

### Regra prática dos scripts

- se o problema é sincronização de títulos, chame `sync_titles.py`
- se o problema é divergência estrutural, audite primeiro com `check_matriz.py`
- se o problema é Vision Board, olhe `src/sync.js` e `public/data.json`
- se o problema é publicação, olhe `publisher`, `devops` e os scripts `publish-lesson-github*.mjs`

## 11. Fluxos operacionais mais comuns

### 11.1 Criar uma aula nova

Fluxo recomendado:

1. `orchestrator`
2. `researcher`
3. `writer`
4. `standardizer`
5. `reviewer`
6. `copywriter`
7. `publisher`

Prompt recomendado:

```text
Use o workflow create-lesson para criar a aula 26.2 do 3º ano.
```

### 11.2 Criar uma semana inteira

Fluxo recomendado:

1. `orchestrator`
2. `full-pipeline`
3. `review-builder` ou builder equivalente
4. `exam-builder` ou builder equivalente
5. `publisher`
6. `devops`

Prompt recomendado:

```text
Execute o full-pipeline da semana 26 do 3º ano.
```

### 11.3 Ajustar aula existente e refletir em toda a estrutura

Fluxo recomendado:

1. editar a aula
2. alinhar `4 - Links-para-imagens-perceber` se o Perceber mudou
3. alinhar `6 - Descrições para tickets`
4. alinhar `2 - Matriz` e `3 - Visão` se o foco pedagógico mudou
5. atualizar revisão `.4` e prova `.5` se o conceito central mudou
6. rodar `sync_titles.py` se houve troca de título

Prompt recomendado:

```text
Ajuste a aula 26.2 do 3º ano e reflita a mudança na revisão, na prova, na matriz, na visão e nos links.
```

### 11.4 Montar revisão bimestral

Prompt recomendado:

```text
Use o bimester-review-builder para montar a revisão do 2º bimestre do 3º ano.
```

### 11.5 Montar prova bimestral

Prompt recomendado:

```text
Use o bimester-exam-builder para montar a prova do 2º bimestre do 3º ano.
```

### 11.6 Fazer commit e push

Prompt recomendado:

```text
Use o devops para criar commits rastreáveis e fazer push para o remote.
```

## 12. Mapa de relações entre ferramentas

```text
CODEX.md
  -> carrega regras de .codex/rules/
  -> orienta uso de .codex/commands/
  -> aponta para trivium-method-editorial/

.codex/commands/
  -> define comportamento dos agentes operacionais
  -> chama workflows, templates, scripts e knowledge base

.codex/agents/
  -> reforça personas de coordenação, QA e publicação

trivium-method-editorial/workflows/
  -> orquestra execução de ponta a ponta

trivium-method-editorial/templates/
  -> define estrutura de aula

trivium-method-editorial/knowledge-base/
  -> define cosmovisão, escrita e sintaxe

trivium-method-editorial/scripts/
  -> corrige, audita e sincroniza

Projeto - Bibline Academy (...)/
  -> recebe o conteúdo final produzido pelo framework

src/sync.js + public/data.json + metas*.html
  -> monitoram a operação editorial no Vision Board
```

## 13. Como treinar novos membros da equipe

### 13.1 Trilha mínima de onboarding

Sugestão de leitura nesta ordem:

1. `AGENTS.md`
2. `CODEX.md`
3. `docs/process/MANUAL-OPERACIONAL-CODEX.md`
4. `trivium-method-editorial/knowledge-base/visao-geral-fluxo-editorial.md`
5. `trivium-method-editorial/knowledge-base/guia-de-estilo.md`
6. `trivium-method-editorial/templates/padrao_final_aula.md`
7. `trivium-method-editorial/workflows/create-lesson.md`
8. `trivium-method-editorial/scripts/README.md`

### 13.2 Primeiros exercícios recomendados

1. Pedir ao `orchestrator` o status de um ano.
2. Pesquisar uma aula com o `researcher`.
3. Revisar uma aula pronta com o `reviewer`.
4. Ajustar links do `Perceber` em uma aula existente.
5. Fazer commit e push com `devops`.

## 14. Convenções de operação

- responder sempre em português
- nunca inventar títulos de aula
- tratar Currículo Macro como fonte absoluta
- manter revisão `.4` coerente com as aulas `.1`, `.2`, `.3`
- manter prova `.5` coerente com a revisão
- não usar Git para mídia pesada
- manter commits com prefixos convencionais

## 15. Alertas importantes

### 15.1 Mistura de nomenclaturas legadas

Alguns documentos antigos ainda citam caminhos como `editorial-squad/`, `.agent/` ou `.claude/`.
O estado operacional atual do repositório para uso com Codex usa:

- `CODEX.md`
- `.codex/commands/`
- `.codex/rules/`
- `.codex/skills/`
- `.codex/agents/`
- `trivium-method-editorial/`

Se houver divergência entre documentação antiga e estrutura atual do Codex, a estrutura atual prevalece.

### 15.2 Vision Board

O Vision Board é parte do framework operacional, mas não substitui o fluxo editorial.
Ele serve para:

- monitorar progresso
- detectar gargalos
- validar coerência com o GitHub Projects

Arquivos principais:

- `src/sync.js`
- `public/data.json`
- `metas.html`
- `metas-disciplinas.html`

### 15.3 Publicação

Publicar não é só salvar a aula. O fechamento correto costuma incluir:

- aula atualizada
- links atualizados
- descrições de ticket atualizadas
- revisão e prova alinhadas
- commit e push

## 16. Comandos prontos para copiar no Codex

### Diagnóstico

```text
Use o orchestrator para mapear o status do 3º ano e me dizer a próxima prioridade.
```

### Criar aula

```text
Execute o workflow create-lesson para a aula 26.2 do 3º ano.
```

### Ajustar aula existente

```text
Revise a aula 26.3 do 3º ano, alinhe o Perceber, atualize links, revisão e prova se necessário.
```

### Sincronizar títulos

```text
Use o devops e rode o script sync_titles.py para alinhar os títulos com o Currículo Macro.
```

### Revisão bimestral

```text
Use o bimester-review-builder para montar a revisão do 1º bimestre do 3º ano.
```

### Prova bimestral

```text
Use o bimester-exam-builder para montar a prova do 1º bimestre do 3º ano.
```

### Versionamento

```text
Use o devops para criar commits rastreáveis e fazer push no origin/main.
```

## 17. Encerramento

Se a equipe memorizar quatro princípios, já opera bem:

1. o Currículo Macro manda
2. o golden template organiza a aula
3. o Orchestrator decide a rota
4. o DevOps fecha e protege o progresso

Este manual deve ser atualizado sempre que novos agentes, workflows, scripts ou convenções forem adicionados ao framework.
