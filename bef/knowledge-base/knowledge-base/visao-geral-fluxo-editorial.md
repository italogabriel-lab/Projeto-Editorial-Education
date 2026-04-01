# Visao Geral do Fluxo Editorial (Editorial Squad)

Este documento serve como mapa central de todo o ecossistema de producao de conteudo da Bibline Academy (Editorial Squad). Ele detalha as funcoes, os arquivos de referencia, o fluxo de trabalho passo a passo, as regras de manutencao e sincronizacao curricular, os scripts de automacao e as conexoes entre cada setor.

Sempre que o fluxo ou as regras mudarem, este documento deve ser atualizado para refletir o estado real da operacao.

---

## 1. Arquitetura Geral do Ecossistema

O ecossistema editorial e composto por 5 camadas interdependentes:

```
+------------------------------------------------------------------+
|                      ORQUESTRACAO                                |
|          orchestrator/SKILL.md  +  orchestrate.md                |
|    (Diagnostico de progresso, priorizacao, delegacao)            |
+------------------------------------------------------------------+
         |                    |                    |
         v                    v                    v
+------------------+  +------------------+  +------------------+
|   PRODUCAO       |  |  POS-PRODUCAO    |  |  PUBLICACAO      |
|  (Pipeline 7     |  | (Revisoes        |  | (Versionamento   |
|   etapas)        |  |  Bimestrais +    |  |  e GitHub)       |
|                  |  |  Provas)         |  |                  |
|  produce_class   |  | bimester-review  |  |  publisher +     |
|  .md             |  | bimester-exam    |  |  devops +        |
+------------------+  +------------------+  |  publish.md      |
                                            +------------------+
         |                    |                    |
         v                    v                    v
+------------------------------------------------------------------+
|                   AUTOMACAO (Scripts Python)                      |
|   sync_titles.py  |  check_matriz.py  |  generate_descriptions   |
|   align_titles.py |  fix_accordion.py |  convert_recordar.py     |
+------------------------------------------------------------------+
         |
         v
+------------------------------------------------------------------+
|                   BASE DE CONHECIMENTO                           |
|   doutrina-pedagogica  |  guia-de-estilo  |  rise-blocks-ref     |
|   Golden Template      |  Templates por Habito                   |
+------------------------------------------------------------------+
```

---

## 2. O Pipeline Principal (`produce_class.md`)

O coracao da producao e o arquivo de fluxo `editorial-squad/workflows/produce_class.md`. A criacao de uma aula segue o modelo de linha de montagem em 7 etapas, onde o output de um agente e o input do proximo.

### Etapas do Pipeline

| Etapa | Agente | Input | Output | Regra principal |
| :--- | :--- | :--- | :--- | :--- |
| **1. Pesquisa** | Researcher | Tema + Plano Pedagogico | `research_report.md` | Fontes primarias: Webster 1828, ARA/ARC, obras classicas |
| **2. Redacao** | Writer | Relatorio de pesquisa | `draft_class.md` | 5 Habitos, voz ativa, imperativo, max 30 palavras/frase |
| **3. Formatacao** | Standardizer + Capitalizer | Rascunho | `formatted_class.md` | Rise Blocks, capitalizacao europeia, remocao de pontuacao proibida |
| **4. Revisao** | Reviewer | Aula formatada | `reviewed_class.md` ou rejeicao | Checklist 13 categorias, 10 erros da IA, validacao Golden Template |
| **5. Polimento** | Copywriter | Aula aprovada | `final_class.md` | Otimizar titulos, ritmo, clareza, cadencia |
| **6. Registro** | (Manual/Automatico) | Aula finalizada | Curriculo Macro atualizado | Marcar ✅, registrar termos, sincronizar 5 arquivos estruturais |
| **7. Publicacao** | Publisher | Aula final | Arquivo local + commit GitHub | Salvar como `X.Y.md`, commit com mensagem padrao |

### Fluxo de Rejeicao (Feedback Loops)

```
Etapa 4 (Reviewer) --[erro de conteudo]--> volta para Etapa 2 (Writer)
Etapa 4 (Reviewer) --[erro de formato]---> volta para Etapa 3 (Standardizer)
Etapa 5 (Copywriter) --[problema grave]---> volta para Etapa 3 ou 4
```

> **Regra de Idempotencia**: O pipeline pode ser re-executado quantas vezes for necessario sem efeitos colaterais.

---

## 3. Estrutura Semanal de Producao

Cada semana de conteudo segue um padrao fixo de 5 arquivos:

| Arquivo | Tipo | Descricao |
| :--- | :--- | :--- |
| `X.1.md` | Aula regular (Dia 1) | Primeira aula da semana |
| `X.2.md` | Aula regular (Dia 2) | Segunda aula da semana |
| `X.3.md` | Aula regular (Dia 3) | Terceira aula da semana |
| `X.4.md` | Revisao semanal | Flashcards, matching e questoes das 3 aulas |
| `X.5.md` | Prova semanal | Quiz CANVAS com questoes das 3 aulas |

### Estrutura Bimestral (10 semanas)

| Semanas | Tipo | Conteudo |
| :--- | :--- | :--- |
| 1-8 (ou 11-18, 21-28, 31-38) | Conteudo | 8 semanas com 5 arquivos cada |
| 9 (ou 19, 29, 39) | Revisao Bimestral | Compilacao das 8 revisoes semanais (.4) |
| 10 (ou 20, 30, 40) | Prova Bimestral | CANVAS_QUIZ de 10 questoes (8 das .5 + 2 autorais) |

### Ciclo Completo por Semana

```
Aula X.1 --> Aula X.2 --> Aula X.3 --> Revisao X.4 --> Prova X.5
    |             |             |             |              |
    | (Pipeline   | (Pipeline   | (Pipeline   | (review-     | (bimester-
    |  7 etapas)  |  7 etapas)  |  7 etapas)  |  builder)    |  exam-builder)
    v             v             v             v              v
  Publicar      Publicar      Publicar     Publicar       Publicar
```

> **Regra de Completude**: Uma semana so e considerada completa quando possui os 5 arquivos (.1, .2, .3, .4, .5) publicados.

---

## 4. Catalogo de Especialistas e Skills (`/skills`)

Cada etapa do pipeline e dominada por um perfil de agente configurado via arquivos markdown na pasta `skills/`.

### 4.1 Agentes do Pipeline Principal

| Skill | Arquivo | Funcao | Etapa |
| :--- | :--- | :--- | :--- |
| **Researcher** | `researcher/SKILL.md` | Curadoria de conteudo historico/biblico com metodologia Ad Fontes | Etapa 1 |
| **Writer** | `writer/SKILL.md` | Redacao didatica nos 5 Habitos da Gramatica | Etapa 2 |
| **Standardizer** | `standardizer/SKILL.md` | Formatacao Rise 360 e validacao estrutural | Etapa 3 |
| **Capitalizer** | `capitalizer/SKILL.md` | Capitalizacao europeia (Acordo Ortografico 1990) | Etapa 3 (sub-passo) |
| **Reviewer** | `reviewer/SKILL.md` | Auditoria de qualidade, 13 categorias, 10 erros da IA | Etapa 4 |
| **Copywriter** | `copywriter/SKILL.md` | Polimento final de ritmo, titulos e clareza | Etapa 5 |
| **Publisher** | `publisher/SKILL.md` | Salvamento local e commit GitHub | Etapa 7 |

### 4.2 Agentes de Pos-Producao

| Skill | Arquivo | Funcao | Quando usar |
| :--- | :--- | :--- | :--- |
| **Bimester Review Builder** | `bimester-review-builder/SKILL.md` | Monta revisao bimestral a partir das .4 | Semanas 9, 19, 29, 39 |
| **Bimester Exam Builder** | `bimester-exam-builder/SKILL.md` | Monta prova CANVAS_QUIZ de 10 questoes | Semanas 10, 20, 30, 40 |

### 4.3 Agentes Transversais (Cross-cutting)

| Skill | Arquivo | Funcao | Quando usar |
| :--- | :--- | :--- | :--- |
| **Orchestrator** | `orchestrator/SKILL.md` | Diagnostico de progresso, priorizacao e delegacao | Inicio de sessao ou quando perdido |
| **DevOps** | `devops/SKILL.md` | Gestao de repositorio, .gitignore, limpeza de cache | Problemas de Git ou publicacao |

### 4.4 Mapa de Dependencias entre Skills

```
Orchestrator (diagnostica e delega)
    |
    +--> Researcher --> Writer --> Standardizer --> Reviewer --> Copywriter --> Publisher
              |              |           |              |
              |              |           |              +--> (rejeicao) --> Writer ou Standardizer
              |              |           |
              |              |           +--> Capitalizer (sub-passo obrigatorio)
              |              |
              |              +--> Golden Template (padrao_final_aula.md)
              |
              +--> Doutrina Pedagogica + Guia de Estilo
    |
    +--> Bimester Review Builder (pos X.4 completas)
    |
    +--> Bimester Exam Builder (pos X.5 completas)
    |
    +--> DevOps (quando necessario)
```

---

## 5. Base de Conhecimento (`/knowledge-base`)

Para que o editorial fale a mesma lingua ideologica e estetica, os agentes consultam passivamente:

| Documento | Arquivo | Funcao |
| :--- | :--- | :--- |
| **Doutrina Pedagogica** | `doutrina-pedagogica.md` | Base teologica e filosofica (Educacao Classica Crista, Trivium, Fase da Gramatica) |
| **Guia de Estilo** | `guia-de-estilo.md` | Tom de voz, metricas (max 30 palavras/frase, 70/paragrafo), pontuacao proibida, regras de capitalizacao |
| **Rise Blocks Reference** | `rise-blocks-reference.md` | Dicionario de 12 blocos Rise 360 com sintaxe exata |
| **Golden Template** | `templates/padrao_final_aula.md` | Esqueleto oficial de toda aula — validado na Etapa 4 |
| **Exemplo Final** | `templates/exemplo_aula_final.md` | Implementacao concreta do Golden Template (referencia, nao padrao) |

### 5.1 Templates por Habito (`/templates`)

Guias leves que orientam a estrutura de cada secao da aula:

| Template | Habito | Orienta |
| :--- | :--- | :--- |
| `defining.md` | Definir | Introducao ao conceito, definicao Webster, etimologia |
| `perceiving.md` | Perceber | Observacao visual, perguntas de analise |
| `remembering.md` | Recordar | Frase de memorizacao, conexao poetica/musical |
| `practicing.md` | Praticar | Atividade pratica, exercicio de fixacao |
| `narrating.md` | Narrar | Trecho literario, momento de narracao, perguntas |

---

## 6. Os 5 Habitos da Gramatica (Estrutura de Cada Aula)

Toda aula regular (.1, .2, .3) segue obrigatoriamente esta estrutura:

### 6.1 Definir (`## Definir`)

| Bloco | Conteudo |
| :--- | :--- |
| `[+PARAGRAPH]` | Contexto ("Reconheca que..."), argumento ("Observe que..."), definicao (9-10 palavras), "Veja o video abaixo" |
| `[+VIDEO]` | Placeholder vazio |
| `[+HEADING]` | "Atividade" |
| `[+PARAGRAPH]` | Instrucao no imperativo |
| `[+ACCORDION]` | Pergunta ("O que e [Termo]?") + Definicao (3 repeticoes: texto, audio, negrito) + Reflexao ("Entenda que...") |

### 6.2 Perceber (`## Perceber`)

| Bloco | Conteudo |
| :--- | :--- |
| `[+PARAGRAPH]` | 3-4 frases no imperativo descrevendo o que observar |
| `[+IMAGE_LABELED]` | Imagem com 2 hotspots (coordenadas percentuais, titulo, descricao imperativa) |

### 6.3 Recordar (`## Recordar`)

| Bloco | Conteudo |
| :--- | :--- |
| `[+PARAGRAPH]` | "Ouca e repita a definicao abaixo" |
| `[+STATEMENT_D]` | Audio + Definicao (9-10 palavras, repetida) |
| `[+HEADING]` | **Variante A**: "Hora de memorizar com musica" / **Variante B**: "Hora de memorizar com rima" |
| Variante A: `[+IMAGE_TEXT_ON]` | Imagem + Audio + Nome da musica |
| Variante B: `[+STATEMENT_A]` | Audio + Rima de 4 versos |

### 6.4 Praticar (`## Praticar`)

| Ordem | Bloco | Conteudo |
| :--- | :--- | :--- |
| Atividade 1 | `[+FILL_IN]` | Completar definicao de 9 palavras com 2 lacunas (`_____`) |
| Atividade 2 | `[+MULTIPLE]` | Pergunta sobre significado do termo (posicao da correta alterna: .1=1a, .2=2a, .3=3a) |
| Atividade Extra | `[+PARAGRAPH]` + `[+ATTACHMENT]` | Descricao da atividade manual + PDF (`@link_pdf@`) |

> **Regras do Praticar**:
> - Atividade 1 sempre comeca com: "Complete as lacunas para reafirmar a definicao que voce aprendeu."
> - Alternativas erradas devem ser plausiveis mas claramente incorretas.
> - A resposta correta e extraida da definicao de 9 palavras (sem o nome do termo e o "e").

### 6.5 Narrar (`## Narrar`)

| Bloco | Conteudo |
| :--- | :--- |
| `[+HEADING]` | "Leitura" |
| **Variante A** (1o, 2o, 4o, 5o ano): `[+IMAGE_TEXT_ASIDE]` | Imagem + Trecho literario (2 paragrafos, aspas retas) + Atribuicao com referencia biblica e autor cristao |
| **Variante B** (3o ano): `[+PARAGRAPH]` | Mesmo conteudo da Variante A em formato paragrafo |
| `[+HEADING]` | "Perguntas" |
| `[+PARAGRAPH]` | "Responda oralmente as perguntas abaixo sobre o texto" |
| `[+LIST_NUMBERED]` | 3 perguntas com ponto de interrogacao |

---

## 7. Regra de Repeticao Obrigatoria da Definicao

A definicao central de cada aula (9-10 palavras) deve aparecer **identicamente** em 6 locais:

| Local | Secao | Formato |
| :--- | :--- | :--- |
| 1. Paragrafo introdutorio | Definir | Texto corrido |
| 2. Accordion (texto simples) | Definir | Sem formatacao |
| 3. Accordion (audio) | Definir | Entre `[MP3/]` e `[MP3\]` |
| 4. Accordion (negrito) | Definir | **Negrito** |
| 5. Statement_D | Recordar | Audio + Texto repetido |
| 6. Revisao semanal (.4) | Definir (tabela + Recordar) | Tabela e flashcard |

> **Violacao desta regra e motivo de rejeicao automatica na Etapa 4 (Reviewer).**

---

## 8. Estrutura Curricular e Regras de Sincronizacao

A organizacao de longo prazo do conteudo vive dentro da pasta de cada ano:
`Belas Artes - Fase da Gramatica/1 Fase - Gramatica/[ANO]/Estrutura Curricular/`

### 8.1 Arquivos Estruturais por Ano

| Arquivo | Funcao | Status |
| :--- | :--- | :--- |
| `0 - Movimentos Artisticos trabalhados` | Lista de movimentos cobertos no ano | Todos os anos |
| `1 - Curriculo Macro` | Fonte de verdade para titulos e sequencia | Todos os anos |
| `2 - Matriz-Curricular-objetivos` | Objetivos pedagogicos por aula | Todos os anos |
| `3 - Visao e Plano pedagogico` | Narrativa e progressao pedagogica | Todos os anos |
| `4 - Links-para-imagens-perceber` | Links de banco de imagens para secao Perceber | Apenas 3o ano |
| `5 - Prompts-para-imagens-narrar` | Prompts de geracao de imagem para secao Narrar | Apenas 3o ano |
| `6 - Descricoes para tickets` | Descricoes de tarefas para gestao de projetos (em transicao/legado) | Apenas Arte |

### 8.1.1 Arquivos Multi-Disciplinares (Novos Tickets)

A nova estrutura de gestao de operacoes agora suporta as demais disciplinas do Trivium. Os arquivos descritivos estao centralizados em:
`Belas Artes - Fase da Gramatica/0-Descricoes e criacao de tickets para as disciplinas/`

| Disciplina/Ano | Arquivo de Tickets | Status |
| :--- | :--- | :--- |
| **Ciencias (4o Ano)** | `ciencias-4-ano.md` | Ativo |
| **Geografia (3o Ano)** | `geografia-3-ano.md` | Ativo |
| **Arte (Todos)** | Em processo de migracao para o padrao centralizado | Em transicao |

### 8.2 REGRA DE OURO (Fonte de Verdade para Titulos)

> **O arquivo `1 - Curriculo Macro` e a UNICA FONTE OFICIAL dos titulos de cada aula.**
> Todos os demais arquivos devem usar **exatamente** os mesmos titulos do Macro.

| Arquivo | O que deve ser identico ao Curriculo Macro |
| :--- | :--- |
| **Arquivo de aula (`.md`)** | O **H1 (`# Titulo`)** deve ser identico ao titulo no Macro |
| **`2 - Matriz-Curricular-objetivos`** | Os titulos nas **tabelas de aulas** (`**Titulo**`) |
| **`3 - Visao e Plano pedagogico`** | Os titulos nas **tabelas de estrutura** e **progressao** |
| **`6 - Descricoes para tickets`** | Os titulos nas linhas de tarefa e listagens de revisao/prova |

> **Se um titulo precisa ser alterado**, a mudanca deve ser feita **primeiro no Curriculo Macro** e depois propagada para todos os demais arquivos (manualmente ou via `sync_titles.py`).

### 8.3 Regra de Sincronizacao (Alteracoes de Conteudo)

Se uma aula existente sofrer alteracoes significativas, o agente DEVE OBRIGATORIAMENTE sincronizar:

| Arquivo a atualizar | Gatilho |
| :--- | :--- |
| **`1 - Curriculo Macro`** | Mudanca no Titulo Principal (H1) |
| **`2 - Matriz-Curricular-objetivos`** | Mudanca na abordagem pedagogica ou teologica |
| **`3 - Visao e Plano pedagogico`** | Mudanca no tema central ou na progressao |
| **`4 - Links-para-imagens-perceber`** | Mudanca na secao Perceber (troca de obra analisada) |
| **`5 - Prompts-para-imagens-narrar`** | Mudanca na secao Narrar (novo texto literario) |
| **`6 - Descricoes para tickets`** | Mudanca no titulo ou estrutura da semana |
| **Aula de Revisao (`X.4.md`)** | Mudanca em definicoes, abordagens ou atividades do Perceber |

### 8.4 Registro de Progresso no Curriculo Macro (Etapa 6)

Ao finalizar uma semana completa (3 aulas), o Publisher deve:

1. Localizar cada linha `- Dia N: [Tema]` e adicionar ` ✅`
2. Adicionar ` ✅` ao titulo da semana `## Semana N`
3. Inserir bloco de termos apos a semana:

```markdown
# Semana N
Termo1 ✅
Termo2 ✅
Termo3 ✅
```

Cada termo corresponde ao termo principal do Accordion/Definir daquela aula.

---

## 9. Automacao: Scripts Python (`/scripts`)

Os scripts automatizam tarefas de sincronizacao e manutencao que seriam propensas a erro se feitas manualmente.

### 9.1 Script Master

| Script | Funcao | Le | Modifica |
| :--- | :--- | :--- | :--- |
| **`sync_titles.py`** | Propagacao completa de titulos do Macro para todos os arquivos downstream | Curriculo Macro (Arquivo 1) | Arquivo 2, Arquivo 3, Arquivo 6 e todos os H1 de aulas |

> **Este e o script mais importante.** Deve ser executado apos QUALQUER mudanca no Curriculo Macro.

### 9.2 Scripts de Auditoria

| Script | Funcao | Le | Modifica |
| :--- | :--- | :--- | :--- |
| **`check_matriz.py`** | Compara Matriz (Arquivo 2) com Macro (Arquivo 1) e reporta divergencias | Arquivos 1 e 2 | Nenhum (somente leitura) |
| **`converters/convert_recordar_to_rhyme.py`** | Identifica quais aulas ainda possuem blocos de musica (pre-conversao) | Aulas do 3o ano | Nenhum (somente leitura) |

### 9.3 Scripts Modulares de Sincronizacao

| Script | Funcao | Escopo |
| :--- | :--- | :--- |
| **`align_titles.py`** | Sincroniza titulos de aulas no Arquivo 6 (tickets) | Apenas linhas de aula X.1, X.2, X.3 |
| **`align_review_titles.py`** | Sincroniza titulos referenciados dentro de blocos de revisao/prova no Arquivo 6 | Apenas referencias internas |
| **`fix_lesson_h1.py`** | Sincroniza H1 dos arquivos de aula individuais com o Macro | Apenas headers H1 |
| **`fix_titles.py`** | Remove sufixos cosmeticos indesejados de titulos de revisao/prova no Arquivo 6 | Formatacao do Arquivo 6 |

### 9.4 Gerador Massivo

| Script | Funcao | Atencao |
| :--- | :--- | :--- |
| **`generate_descriptions.py`** | Regenera completamente o Arquivo 6 (Descricoes para tickets) a partir de dados hardcoded | **DESTRUTIVO**: sobrescreve todo o arquivo. Usar apenas para reconstrucao total ou recuperacao |

### 9.5 Scripts de Conversao e Formatacao

| Script | Funcao | Escopo |
| :--- | :--- | :--- |
| **`converters/convert_recordar.py`** | Converte blocos "musica" para "rima" na secao Recordar | Aulas .1, .2, .3 do 3o ano |
| **`formatters/fix_accordion.py`** | Remove repeticao redundante do nome do termo nas linhas de definicao do Accordion | Aulas do 4o ano (linhas 39 e 43) |

### 9.6 Fluxo de Execucao dos Scripts

**Fluxo padrao (apos mudanca no Macro):**
```
1. Alterar Curriculo Macro (Arquivo 1)
2. Executar sync_titles.py --> propaga para Arquivos 2, 3, 6 e H1s
3. (Opcional) Executar check_matriz.py --> verificar alinhamento
4. Commitar e publicar
```

**Fluxo de emergencia (Arquivo 6 corrompido):**
```
1. Executar generate_descriptions.py --> reconstroi Arquivo 6 do zero
2. Executar align_titles.py + align_review_titles.py --> sincronizar titulos
3. Executar fix_titles.py --> limpar formatacao
```

**Fluxo de conversao (mudanca de formato):**
```
1. Executar convert_recordar_to_rhyme.py --> auditar escopo
2. Executar convert_recordar.py --> converter musica para rima
3. Executar fix_accordion.py --> normalizar definicoes
```

### 9.7 Automacao de Carga e Gestao de Tickets no GitHub (GitHub API)

| Script | Funcao | Escopo |
| :--- | :--- | :--- |
| **`update_fast.py`** | Atualiza os titulos e bodys das Issues que estao na coluna `Backlog` do GitHub Projects via GraphQL | Projetos e Issues remotas (Single Source of Truth -> Cloud) |
| **`check_project_items.py`** | Audita e lista os itens ativos em um ProjectV2 do GitHub | Leitura remota |
| **`build_year1_tickets.py`** | Constroi a base local estruturada de tickets para carga massiva (Ano 1) | Geracao local |

---

## 10. Alternancia de Blocos (Variantes Permitidas)

Alguns habitos possuem mais de uma opcao de bloco Rise permitida:

| Habito | Contexto | Opcao A (padrao) | Opcao B (alternativa) |
| :--- | :--- | :--- | :--- |
| **Perceber** (Revisao `.4`) | 3 atividades visuais por semana | `FLASHCARD_GRID` / `FLASHCARD_STACK` / `IMAGE` | `TABS` (2 abas com imagem + texto descritivo) |
| **Narrar** (Aula regular) | Texto literario + perguntas | `IMAGE_TEXT_ASIDE` + `LIST_NUMBERED` | `PARAGRAPH` + `LIST_NUMBERED` |
| **Recordar** (Aula regular) | Memorizacao apos definicao | `IMAGE_TEXT_ON` (musica) | `STATEMENT_A` (rima de 4 versos) |

> O usuario pode solicitar a troca a qualquer momento. O agente deve aplicar a variante escolhida e manter a consistencia ao longo de toda a semana.

---

## 11. Gestao de Repositorio (`publish.md` + DevOps)

### 11.1 Regra de Ouro do Git

> **Git NAO e para midia pesada. Git e exclusivamente para texto, historico de revisao e gestao pura de conhecimento.**

### 11.2 Extensoes Proibidas no Repositorio

| Proibido | Motivo |
| :--- | :--- |
| `.mp4`, `.mp3`, `.wav` | Midia pesada |
| `.pdf`, `.zip`, `.rar` | Arquivos binarios |
| `.png`, `.jpg`, `.webp` (opcional) | Imagens pesadas |
| `.DS_Store`, `.obsidian/` | Cache de sistema |

### 11.3 Nomenclatura de Commits

| Prefixo | Uso |
| :--- | :--- |
| `content:` | Novo conteudo editorial (aulas, revisoes, provas) |
| `fix:` | Correcao de erros em conteudo existente |
| `chore:` | Manutencao tecnica (scripts, .gitignore, limpeza) |

### 11.4 Limpeza de Emergencia

Quando o repositorio esta contaminado com arquivos pesados:

```bash
git rm -r --cached .
git add .
git commit -m "chore: Limpeza profissional - removendo arquivos pesados"
git push origin main --force
```

---

## 12. Progressao Curricular por Ano

| Ano | Volume | Periodo Artistico | Semanas | Status atual |
| :--- | :--- | :--- | :--- | :--- |
| **1o Ano** | - | Introducao a Linguagem Visual e Elementos da Arte | 40 | Nao iniciado |
| **2o Ano** | Vol. 1 | Da Criacao ate a Arte Bizantina | 38 | Producao completa (sem .4/.5 para maioria) |
| **3o Ano** | Vol. 2 | Arte Crista Oriental ate o Renascimento do Norte | 38 + revisoes/provas | Producao completa (.4 e .5 inclusos) |
| **4o Ano** | Vol. 3 | Impressionismo ate a Arte Contemporanea | 40 | Producao completa (.4 inclusos, sem .5) |
| **5o Ano** | Vol. 4 | Maneirismo ate o Realismo Americano | 40 | Parcialmente produzido (gaps nas semanas 29-30) |

### Fase do Trivium: Gramatica (todos os anos)
- Memorizacao e a atividade cognitiva central
- Observacao precede analise
- Repeticao e virtude, nao redundancia
- Narrativa e forma natural de aprendizado
- Vocabulario construido progressivamente (1 novo termo por aula)

---

## 13. Mapa Completo de Conexoes

```
CURRICULO MACRO (Fonte de Verdade)
    |
    |-- sync_titles.py --> Matriz (Arq. 2) + Visao (Arq. 3) + Tickets (Arq. 6) + H1 das aulas
    |
    |-- Orchestrator --> le Macro para diagnostico de progresso
    |
    |-- Writer --> le Macro para titulo exato (H1) da aula
    |
    |-- Publisher --> marca ✅ no Macro apos publicacao
    |
    |-- Bimester Review Builder --> le titulos das semanas do Macro
    |
    |-- Bimester Exam Builder --> le titulos para cabecalho da prova

GOLDEN TEMPLATE (padrao_final_aula.md)
    |
    |-- Writer --> segue como esqueleto ao redigir
    |
    |-- Standardizer --> formata seguindo a estrutura
    |
    |-- Reviewer --> valida contra o template (rejeita se divergir)

GUIA DE ESTILO (guia-de-estilo.md)
    |
    |-- Writer --> aplica tom, metricas, regras de pontuacao
    |
    |-- Standardizer --> aplica capitalizacao e remocao de proibidos
    |
    |-- Reviewer --> verifica conformidade total
    |
    |-- Capitalizer --> aplica regras de capitalizacao europeia

DOUTRINA PEDAGOGICA (doutrina-pedagogica.md)
    |
    |-- Researcher --> orienta selecao de fontes e cosmovisao
    |
    |-- Writer --> fundamenta abordagem teologica
    |
    |-- Reviewer --> verifica alinhamento doutrinario

RISE BLOCKS REFERENCE (rise-blocks-reference.md)
    |
    |-- Standardizer --> consulta sintaxe exata de cada bloco
    |
    |-- Reviewer --> verifica formatacao dos blocos
```

---

## 14. Tabela de Roteamento (Quem faz o que)

| Demanda do Usuario | Skill/Workflow | Invocacao |
| :--- | :--- | :--- |
| Criar uma aula nova | `workflows/produce_class.md` | "Crie a aula X.Y, No ano" |
| Criar aula de revisao (X.4) | `skills/review-builder/SKILL.md` | "Crie a revisao da semana X" |
| Criar revisao bimestral | `skills/bimester-review-builder/SKILL.md` | "Crie a revisao do bimestre N" |
| Criar prova bimestral | `skills/bimester-exam-builder/SKILL.md` | "Crie a prova do bimestre N" |
| Corrigir formatacao Rise | `skills/standardizer/SKILL.md` | @standardizer |
| Corrigir capitalizacao | `skills/capitalizer/SKILL.md` | @capitalizer |
| Revisar qualidade | `skills/reviewer/SKILL.md` | @reviewer |
| Polir texto | `skills/copywriter/SKILL.md` | @copywriter |
| Subir no GitHub | `skills/devops/SKILL.md` | @devops |
| Pesquisar conteudo | `skills/researcher/SKILL.md` | @researcher |
| Publicar arquivo | `skills/publisher/SKILL.md` | @publisher |
| Status geral do projeto | `skills/orchestrator/SKILL.md` | @orchestrator |
| Sincronizar titulos | `scripts/sync_titles.py` | Executar via terminal |
| Auditar alinhamento | `scripts/check_matriz.py` | Executar via terminal |
| Atualizar Tickets Github | `scripts/update_fast.py` | Executar via terminal |

---

## 15. Placeholders de Midia

| Placeholder | Significado | Onde aparece |
| :--- | :--- | :--- |
| `@link_png@` | Imagem a inserir | Perceber, Accordion, Narrar |
| `@link_mp3@` | Audio a inserir | Accordion, Recordar |
| `@link_pdf@` | PDF de atividade | Praticar (Atividade Extra) |
| `[+VIDEO][-VIDEO]` | Video (tags vazias) | Definir |
| `#11L:XXXXXXXXX` | Voice ID (ElevenLabs) | Accordion, Statement_D, Statement_A |

---

*Ultima atualizacao: 2026-03-24*
*Documento atualizado com base na analise completa do ecossistema editorial-squad.*
