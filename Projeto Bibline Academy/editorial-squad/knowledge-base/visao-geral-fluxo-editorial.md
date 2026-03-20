# Visão Geral do Fluxo Editorial (Editorial Squad)

Este documento serve como mapa central de todo o ecossistema de produção de conteúdo (Editorial Squad). Ele detalha as funções, os arquivos de referência, o fluxo de trabalho passo a passo e, crucialmente, as **regras de manutenção e sincronização curricular**.

Sempre que o fluxo ou as regras mudarem, este documento deve ser atualizado para refletir o estado real da operação.

---

## 1. O Pipeline Principal (`produce_class.md`)

O coração da produção é o arquivo de fluxo `editorial-squad/workflows/produce_class.md`. A criação de uma aula segue o modelo de linha de montagem em 7 etapas, onde o output de um agente é o input do próximo.

1. **ETAPA 1 — PESQUISA (Researcher)**: Levanta definições (Webster 1828), versículos, obras de arte e trechos literários com base no Plano Pedagógico.
2. **ETAPA 2 — REDAÇÃO (Writer)**: Transforma a pesquisa em uma aula estruturada nos 5 Hábitos (Definir, Perceber, Recordar, Praticar, Narrar), aplicando as regras de estilo e tom.
3. **ETAPA 3 — FORMATAÇÃO (Standardizer & Capitalizer)**: Aplica blocos do Rise 360, remove Markdown residual, padroniza as aspas e aplica a rígida **Capitalização Europeia** (apenas a primeira letra maiúscula em títulos, preservando topônimos).
4. **ETAPA 4 — REVISÃO (Reviewer)**: Passa a aula por um checklist de 13 categorias e previne os "10 erros comuns da IA". Se rejeitada, o fluxo volta para Redação ou Formatação.
5. **ETAPA 5 — POLIMENTO (Copywriter)**: Otimiza títulas, ritmo de leitura, clareza dos enunciados e cadência geral da aula.
6. **ETAPA 6 — REGISTRO & SINCRONIZAÇÃO CURRICULAR**: *[Exige atualização manual ou automatizada dos arquivos estruturais. Veja a seção 4]*
7. **ETAPA 7 — PUBLICAÇÃO (Publisher)**: Salva no repositório local e no GitHub.

> **Regra de Aula de Revisão**: Ao fim de 3 aulas regulares, usa-se a skill `review-builder` para criar a 4ª aula da semana, integrando flashcards, cruzamentos (matching) e questões baseadas estritamente nas definições das 3 aulas anteriores.

---

## 2. Especialistas e Skills (`/skills`)

Cada etapa do pipeline é dominada por um perfil de agente, configurado via arquivos markdown na pasta `skills/`:

- **`researcher/SKILL.md`**: Especialista em curadoria de conteúdo histórico/bíblico.
- **`writer/SKILL.md`**: Especialista em didática clássica e redação concisa.
- **`standardizer/SKILL.md`**: Especialista em formatação Rise 360 e validação estrutural.
- **`capitalizer/SKILL.md`**: Especialista filológico focado no Acordo Ortográfico de 1990 (PT-PT) para garantir o "Sentence-case" europeu.
- **`reviewer/SKILL.md`**: Auditor de qualidade rigoroso e protetor do "Golden Template".
- **`copywriter/SKILL.md`**: Lapidador de textos, focado no engajamento e ritmo.
- **`publisher/SKILL.md`**: Especialista em versionamento (Git) e salvamento de arquivos.
- **`review-builder/SKILL.md`**: Construtor lógico de aulas de revisão usando componentes interativos.

---

## 3. Base de Conhecimento (`/knowledge-base`)

Para que o editorial fale a mesma língua ideológica e estética, os agentes consultam passivamente:

- **`doutrina-pedagogica.md`**: A base teológica e filosófica (Educação Clássica Cristã).
- **`guia-de-estilo.md`**: Regras de tom de voz, métricas de frases (max 30 palavras) e pontuação.
- **`rise-blocks-reference.md`**: O dicionário de correspondência entre o Markdown local e os blocos virtuais da plataforma Rise 360 (ex: `[+ACCORDION]`, `[+IMAGE_LABELED]`).
- **`templates/padrao_final_aula.md`**: O **Golden Template**, arquivo de ouro contra o qual todas as aulas criadas são testadas para garantir uniformidade.

---

## 4. Estrutura Curricular e Regras de Sincronização

A organização de longo prazo do conteúdo vive dentro da pasta de cada ano (ex: `Belas Artes - Fase da Gramática/1 Fase - Gramática/[ANO]/Estrutura Curricular/`).

Existem 4 arquivos fundamentais que **sustentam a coerência** de todo o ano letivo.

### REGRA DE OURO (Manutenção Editorial)
Se uma aula **existente** sofrer alterações *significativas*, o agente **DEVE OBRIGATORIAMENTE** sincronizar as edições com os seguintes arquivos:

| Arquivo que deve ser atualizado | Gatilho: Quando a aula é modificada gerando... |
| :--- | :--- |
| **`1 - Curriculo Macro`** | ...mudança no **Título Principal (H1)** da aula. O título no Macro deve ser um espelho exato do arquivo da aula. |
| **`2 - Matriz-Curricular-objetivos`** | ...mudança na **abordagem pedagógica ou teológica**. Se a aula focava em "Guerra" e passou a focar em "Arte", o objetivo na Matriz deve ser reescrito. |
| **`3 - Visão e Plano pedagogico`** | ...mudança no **tema central** ou na **progressão pedagógica**. O texto deste arquivo deve prever e amarrar a narrativa exata que a nova aula ensina. |
| **`4 - Links-para-imagens-perceber`** | ...mudança na seção **Perceber**. Se a aula troca de análise arquitetônica para pintura de mosaico, os links de pesquisa em banco de imagens devem ser trocados neste arquivo. |
| **`5 - Prompts-para-imagens-narrar`** | ...mudança na seção **Narrar**. Se o texto literário da Leitura for alterado, o prompt de geração de imagem deve ser regenerado com base no novo texto. |
| **Aula de Revisão (`X.4.md`)** | ...mudança em **definições principais, abordagens ou atividades do Perceber**. Flashcards, quizzes, tabelas e textos da revisão devem ser sempre idênticos à aula base. |

### Fluxo de Evolução Contínua
Sempre que o usuário solicitar uma alteração de "Lente Teórica" (ex: "Revise com foco em História da Arte"), os agentes devem primeiramente ajustar a aula `.md` referida e, imediatamente após, auditar esses 5 documentos estruturais, mantendo o ecossistema perfeitamente sincronizado.

---

## 5. Alternância de Blocos (Variantes Permitidas)

Alguns hábitos possuem mais de uma opção de bloco Rise permitida. O agente pode (e deve) alternar entre elas conforme a orientação do usuário ou do contexto pedagógico.

| Hábito | Contexto | Opção A (padrão) | Opção B (alternativa) |
| :--- | :--- | :--- | :--- |
| **Perceber** (Revisão `.4`) | 3 atividades visuais por semana | `FLASHCARD_GRID` / `FLASHCARD_STACK` / `IMAGE` | `TABS` (2 abas nomeadas com imagem + texto descritivo por assunto) |
| **Narrar** (Aula regular) | Texto literário + perguntas | `IMAGE_TEXT_ASIDE` + `LIST_NUMBERED` | `PARAGRAPH` + `LIST_NUMBERED` |

> O usuário pode solicitar a troca a qualquer momento. O agente deve aplicar a variante escolhida e manter a consistência ao longo de toda a semana.

---

## 6. Estrutura Padrão do Hábito Praticar (Aulas Regulares)

Toda aula regular (`.1`, `.2`, `.3`) segue a seguinte estrutura obrigatória no hábito **Praticar**:

| Ordem | Bloco | Conteúdo |
| :--- | :--- | :--- |
| **Atividade 1** | `FILL_IN` | Completar a definição de 9 palavras com 2 lacunas |
| **Atividade 2** | `MULTIPLE` | Pergunta sobre o significado do termo (alternativa correta baseada na definição) |
| **Atividade Extra** | `PARAGRAPH` + `ATTACHMENT` | Parágrafo descritivo da atividade manual + Link para PDF (`@link_pdf@`) |

### Regras:
- A **Atividade 1** sempre começa com o parágrafo introdutório: `Complete as lacunas para reafirmar a definição que você aprendeu.`
- As alternativas erradas na Atividade 2 devem ser **plausíveis mas claramente incorretas**.
- A resposta correta da Atividade 2 é extraída da **definição de 9 palavras** (sem o nome do termo e o "é").
- A posição da alternativa correta da Atividade 2 deve alternar de acordo com o número da aula: na aula `.1` é a primeira posição; na aula `.2` é a segunda posição; na aula `.3` é a terceira posição.
- Cada atividade é precedida por um `[+HEADING]` com o rótulo `Atividade 1`, `Atividade 2` ou `Atividade Extra`.

> **Importante**: Ao criar ou modificar uma aula, a seção Praticar deve **sempre** seguir este padrão obrigatório.
