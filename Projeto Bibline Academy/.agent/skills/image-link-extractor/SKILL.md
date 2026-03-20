---
name: Image Link Extractor
description: Agente de extração de links de referência para imagens do hábito Perceber
---

# Image Link Extractor — Skill de Extração de Links para Imagens do Perceber

## Objetivo

Extrair os enunciados do hábito **Perceber** de todas as aulas de um determinado ano e gerar um arquivo markdown com links de referência para as obras de arte e imagens necessárias, organizados por semana e aula.

## Quando Usar

- Após todas as aulas de um ano terem sido criadas e padronizadas
- Quando o usuário solicitar links para imagens do Perceber de um ano específico
- Aplica-se a **todos os anos**: 1º, 2º, 3º, 4º e 5º ano

## Processo Passo a Passo

### Etapa 1 — Extrair conteúdo do Perceber

Leia todas as aulas (`.1.md`, `.2.md`, `.3.md`) do ano solicitado e extraia:

1. **Nome do arquivo** (ex: `5.1.md`)
2. **Título da aula** (H1 no topo do arquivo)
3. **Enunciado do Perceber** — o texto dentro de `[+PARAGRAPH]..[-PARAGRAPH]` na seção `## Perceber`
4. **Hotspots** — os títulos das marcações dentro de `[+IMAGE_LABELED]`, se existirem

Usar script Python para automatizar a extração:

```python
# Padrão de extração:
# 1. Título: re.match(r'^# (.+)', content)
# 2. Perceber: re.search(r'## Perceber\n(.*?)(?=\n## )', content, re.DOTALL)
# 3. Parágrafo: re.search(r'\[\+PARAGRAPH\]\n\n(.+?)\n\n\[-PARAGRAPH\]', perceber, re.DOTALL)
# 4. Hotspots: re.findall(r'\d+ \d+\n\n(.+?)\n\n', perceber)
```

### Etapa 2 — Identificar obras e temas

Para cada aula, analisar o enunciado e identificar:

- **Obras específicas mencionadas** (ex: "Retábulo de Gand", "Cristo Pantocrator")
- **Artistas mencionados** (ex: "Jan van Eyck", "Giotto")
- **Locais mencionados** (ex: "Ravena", "Sainte-Chapelle")
- **Conceitos visuais** (ex: "mosaico bizantino", "arco ogival", "caligrafia árabe")

### Etapa 3 — Pesquisar links

Para cada obra/tema identificado, buscar links nas seguintes fontes prioritárias:

| Prioridade | Fonte | Tipo |
|---|---|---|
| 1 | Wikipedia | Artigo da obra/artista com imagens de domínio público |
| 2 | Wikimedia Commons | Categorias com várias imagens de alta resolução |
| 3 | Khan Academy | Análises detalhadas com imagens contextualizadas |
| 4 | Google Arts & Culture | Imagens de alta resolução de museus parceiros |
| 5 | Sites de museus | National Gallery, Museo del Prado, Met Museum, WGA |
| 6 | Closer to Van Eyck / similares | Detalhes em altíssima resolução |

**Regra:** Sempre fornecer pelo menos **2 links** por aula. Para obras específicas (ex: Retrato dos Arnolfini), fornecer o **link direto** para a página da obra.

### Etapa 4 — Gerar o arquivo de links

Criar o arquivo na pasta do ano com o nome:

```
links-para-imagens-perceber-[X]-ano.md
```

Onde `[X]` é o número do ano (1, 2, 3, 4, 5).

#### Estrutura do arquivo

```markdown
# Links para Imagens — Hábito Perceber — [X]º Ano

> Referências de imagens organizadas por semana e aula.
> Busque a obra pelo nome nos links abaixo.

---

## Semana [N] — [Tema geral da semana]

### [N].1 — [Descrição curta do que a imagem deve mostrar]
- [Nome da obra/fonte (Plataforma)](URL)
- [Nome da obra/fonte (Plataforma)](URL)

### [N].2 — [Descrição curta]
- [Link](URL)
- [Link](URL)

### [N].3 — [Descrição curta]
- [Link](URL)
- [Link](URL)

---
```

### Etapa 5 — Verificação

Após gerar o arquivo:

1. Confirmar que **todas as semanas e aulas** estão listadas
2. Confirmar que cada aula tem **pelo menos 2 links**
3. Confirmar que os links são **relevantes** ao enunciado do Perceber

## Diretórios por Ano

| Ano | Diretório |
|---|---|
| 1º | `1º Ano - [NOME DO TEMA]` |
| 2º | `2º Ano - DA CRIAÇÃO ATÉ A ARTE BIZANTINA` |
| 3º | `3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE` |
| 4º | `4º Ano - IMPRESSIONISMO ATÉ A ARTE CONTEMPORÂNEA` |
| 5º | `5º Ano - [NOME DO TEMA]` |

Todos dentro de:
```
Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/
```

## Exemplo de Referência

O arquivo `links-para-imagens-perceber-3-ano.md` no 3º Ano serve como modelo padrão para os demais anos. Consulte-o para verificar o formato e nível de detalhe esperado.

## Observações

- Agrupar buscas por **módulo temático** para eficiência (ex: todas as obras bizantinas numa busca)
- Para semanas de **revisão/encerramento** (últimas semanas), indicar reuso de imagens anteriores
- Para **comparações** entre estilos, indicar obras de ambos os estilos lado a lado
- Os links são referências para o usuário localizar as imagens — não são URLs de download direto
