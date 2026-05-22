---
description: Fluxo completo de criação de uma aula (7 etapas editoriais)
---

# Produzir Aula — Editorial Squad

Pipeline completo de criação de conteúdo em 7 etapas.

**Uso**: `Crie a aula 36.3, 2º ano` ou `Produza a semana 15, 3º ano`

---

## Resolver Caminhos

| Ano | Diretório |
|-----|-----------|
| 1º | `1º Ano - ARTE CRISTÃ PRIMITIVA E ÍCONES BIZANTINOS/` |
| 2º | `2º Ano - DA CRIAÇÃO ATÉ A ARTE BIZANTINA/` |
| 3º | `3º Ano - RENASCIMENTO E REFORMA/` |
| 4º | `4º Ano - BARROCO ATÉ O NEOCLASSICISMO/` |
| 5º | `5º Ano - MANEIRISMO ATÉ O REALISMO AMERICANO/` |

Base: `Belas Artes - Fase da Gramática/1 Fase - Gramática/[Diretório]/`
Estrutura: `[Base]/Estrutura Curricular/`

---

## ETAPA 1 — PESQUISA (Researcher) — por SEMANA

1. Ler a skill `editorial-squad/skills/researcher/SKILL.md`
2. Consultar o **Plano Pedagógico** do ano para localizar a semana (não a aula isolada)
3. Consultar o **Currículo Macro** para identificar termos proibidos em semanas anteriores (✅)
4. Pesquisar **uma vez por semana** (resultado serve para `x.1`, `x.2` e `x.3`):
   - Definição Webster 1828 para o termo central da semana
   - Definição curta de 9-10 palavras (compartilhada pelas 3 aulas)
   - 1 versículo eixo + 2 versículos de apoio (para `x.2` e `x.3`)
   - 3 obras de arte para o Perceber (uma por aula, todas dentro do tema)
   - 1 música ou rima para o Recordar (compartilhada pelas 3 aulas)
   - 3 trechos literários para o Narrar (um por aula, usar DB de autores da skill)
5. **Output**: relatório de pesquisa organizado pelos 5 hábitos e por aula da semana

---

## ETAPA 2 — REDAÇÃO (Writer)

1. Ler a skill `editorial-squad/skills/writer/SKILL.md`
2. Consultar o **golden template** `editorial-squad/templates/padrao_final_aula.md`
3. Consultar a **knowledge base**:
   - `editorial-squad/knowledge-base/guia-de-estilo.md`
   - `editorial-squad/knowledge-base/doutrina-pedagogica.md`
4. Se a aula é `x.2` ou `x.3`, **ler primeiro `x.1`** da mesma semana e copiar literalmente: definição curta, termo principal e música/rima do Recordar
5. Redigir conteúdo completo dos 5 hábitos baseado no relatório de pesquisa
6. Garantir: voz ativa, imperativo, frases ≤ 30 palavras, sem `;` `:` `—`
7. Garantir que Praticar tenha Fill_In, `[+MULTIPLE]` e Atividade Extra, nessa ordem
8. No 3º ano, garantir que Narrar tenha `[+PARAGRAPH]` para a leitura e `[+IMAGE]` com `@link_png@` antes das perguntas
9. **Output**: rascunho da aula

---

## ETAPA 3 — FORMATAÇÃO (Standardizer)

1. Ler a skill `editorial-squad/skills/standardizer/SKILL.md`
2. Consultar `editorial-squad/knowledge-base/rise-blocks-reference.md`
3. Aplicar correções editoriais proativas (sinais proibidos, voz passiva, aspas)
4. **Aplicar capitalização padrão europeu** conforme `editorial-squad/skills/capitalizer/SKILL.md`
5. Formatar com Rise Blocks seguindo o mapeamento exato dos 5 hábitos
6. Remover metadados, emojis de seção, separadores `---`
7. Verificar definição curta literalmente idêntica no cabeçalho do Definir e no Recordar, inclusive capitalização. No Accordion, o MP3 contém definição curta e explicação completa, e o texto após `[MP3\]` mantém conteúdo equivalente com negritos permitidos
8. **Consistência semanal**: se for `x.2` ou `x.3`, comparar com `x.1` e garantir que definição curta, termo e música/rima são idênticos. Apenas o parágrafo livre do Definir, a explicação do Accordion, as imagens, o texto do Narrar e a Atividade Extra devem variar
9. Verificar que o `[+MULTIPLE]` permanece no Praticar e que a imagem do Narrar segue o padrão do ano
10. **Output**: aula formatada com Rise Blocks

---

## ETAPA 4 — REVISÃO (Reviewer)

1. Ler a skill `editorial-squad/skills/reviewer/SKILL.md`
2. Executar o **checklist de 13 categorias** completo
3. Verificar os **10 erros conhecidos da IA** (prioritário)
4. Validar conformidade com o **golden template**
5. **Se APROVADO** → marcar `[APPROVED_FOR_STEP_5]` e seguir para Etapa 5
6. **Se REJEITADO** → identificar se o erro é de conteúdo (volta Etapa 2) ou formatação (volta Etapa 3)

> **LOOP**: Se rejeitado, corrigir e resubmeter até aprovação.

---

## ETAPA 5 — POLIMENTO (Copywriter)

1. Ler a skill `editorial-squad/skills/copywriter/SKILL.md`
2. Otimizar título da aula (criativo e engajante)
3. Polir enunciados (variação de verbos, clareza)
4. Revisar fluidez geral e transições
5. Checagem final de conformidade
6. **Output**: aula final polida

---

## ETAPA 6 — REGISTRO NO CURRÍCULO MACRO

> **OBRIGATÓRIO**: Executar automaticamente ao final de cada semana completa (3 aulas).

1. Abrir o **Currículo Macro** do ano correspondente:
   - Localizar `[Base]/Estrutura Curricular - [Nº] ANO/1 - Curriculo Macro - *.md`
2. Para **cada aula finalizada** na semana:
   - Localizar a linha `- N.M [Título da aula]`
   - Adicionar ` ✅` ao final da linha (se ainda não tiver)
3. Adicionar ` ✅` ao final do título `## Semana N - **Tema central**`
4. **Adicionar bloco de termo da semana** logo após as 3 aulas, seguindo o padrão novo:

```markdown
# Semana N
[TermoCentral] ✅
```

5. O `[TermoCentral]` é o **termo principal compartilhado** pelas 3 aulas (o mesmo do Accordion/Definir de `x.1`, `x.2` e `x.3`)
6. Confirmar ao usuário: `Semana X: 3/3 aulas + termo central marcado ✅`

> **Padrão antigo (descontinuado)**: blocos com `Termo1 ✅ / Termo2 ✅ / Termo3 ✅` (um termo por aula) **não** são mais utilizados. Se encontrar uma semana legada com esse formato, refatore-a quando for atualizar as aulas.

> **REGRA DE SINCRONIZAÇÃO CURRICULAR (MANUTENÇÃO)**:
> Se você estiver **modificando/atualizando** uma aula já existente (em vez de criar uma nova), você DEVE obrigatoriamente refletir as mudanças nestes arquivos:
> 1. `1 - Curriculo Macro *.md`: Se o título (H1) da aula mudar ou se o termo central da semana mudar.
> 2. `2 - Matriz-Curricular-objetivos *.md`: Se o objetivo teológico-pedagógico, o tema central ou os conceitos da semana mudarem.
> 3. `3 - Visão e Plano pedagogico *.md`: Se a abordagem da aula (Definir/Perceber), a visão teológica ou a progressão pedagógica mudarem.
> 4. `4 - Links-para-imagens-perceber *.md`: Se a seção **Perceber** mudar (especialmente se o contexto, a cena ou a arte sugerida no texto mudar, exigindo links novos).
> 5. **Outras aulas da mesma semana**: Se alterar a definição curta de `x.1`, atualizar `x.2`, `x.3` e `x.4` (revisão) para manter a mesma frase literal.
> 6. **Aula de Revisão (`X.4.md`)**: Usa a definição curta única da semana (não três). Se alterar conteúdo das aulas, atualizar a revisão correspondente.

> **Formato completo de referência** (novo padrão, 1º ano):
> ```
> ## Semana 1 - A arte e a expressão ✅
>
> - 1.1 A arte e a expressão ✅
> - 1.2 A arte e a beleza ✅
> - 1.3 A arte e a habilidade ✅
>
> # Semana 1
> Arte ✅
> ```


---

## ETAPA 7 — PUBLICAÇÃO (Publisher)

1. Ler a skill `editorial-squad/skills/publisher/SKILL.md`
2. Salvar a aula final no diretório local: `[Base]/[NUMERO].md`
3. Push para GitHub via MCP (se disponível):
   - Repo: `bibline/curriculum`
   - Branch: `master`
   - Path: `br/_/[ANO]-belas-artes/[NUMERO].md`
4. Confirmar ao usuário: local ✅, termo ✅, GitHub ✅

---

## Fluxo Visual

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ 1. PESQUISA │────→│ 2. REDAÇÃO  │────→│3. FORMATAÇÃO│
│ (Researcher)│     │  (Writer)   │     │(Standardizer│
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                    ┌──────────────┐            │
                    │              │◄───────────┘
                    │  4. REVISÃO  │
                    │  (Reviewer)  │──── REJECTED? ──→ volta 2 ou 3
                    │              │
                    └──────┬───────┘
                           │ APPROVED
                    ┌──────┴───────┐
                    │ 5. POLIMENTO │
                    │ (Copywriter) │
                    └──────┬───────┘
                           │
                    ┌──────┴───────┐     ┌─────────────┐
                    │ 6. REGISTRO  │────→│7. PUBLICAÇÃO│
                    │  (Termo ✅)  │     │ (Publisher)  │
                    └──────────────┘     └─────────────┘
```

---

## Notas

- Cada etapa consome o output da anterior (Context Loop)
- O fluxo é **idempotente**: pode ser re-executado sem efeitos colaterais
- Para uma **semana inteira**, executar 3x (aulas X.1, X.2, X.3) + revisão (X.4) + prova (X.5)
- Como a unidade pedagógica é a **semana**, a Pesquisa (Etapa 1) pode ser feita **uma vez** e reaproveitada nas 3 redações. Definição curta, termo principal e música/rima são comuns às 3 aulas
