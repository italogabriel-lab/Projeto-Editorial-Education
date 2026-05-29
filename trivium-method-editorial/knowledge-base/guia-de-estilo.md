---
name: Guia de Estilo Editorial
description: Regras de escrita, tom de voz, formatação e Rise Blocks para todas as aulas
---

# Guia de Estilo Editorial — Bibline Academy

## Tom de Voz

- **Virtuoso e elevado, porém acessível** para crianças de 7 a 11 anos (fase da Gramática).
- Didático sem ser infantilizado. Respeitoso sem ser inacessível.
- Use analogias ricas e referências a grandes autores ou obras de arte.
- Dirija-se ao aluno usando **"você"** ou **"seu"** para tom direto e pessoal.
- Proibido: linguagem excessivamente infantilizada, gírias modernas, ironia.
- Obrigatório: clareza na exposição e beleza na forma.
- Tom bíblico, robusto, respeitoso. Zero traços de passiva, gerúndio excessivo ou comandos indiretos.

## Regras de Escrita Obrigatórias

### Voz e Tempo Verbal
- Escreva **no tempo presente** e **na voz ativa**. NUNCA use voz passiva.
- Todos os **enunciados** devem estar no **imperativo direto e objetivo**: "Observe", "Complete", "Leia", "Ouça", "Reconheça", "Desenhe", "Narre".
- Exemplos corretos: "Clique em Iniciar atividade para começar o exercício" (NUNCA "A atividade deve ser iniciada pelo aluno").

### Sinais Proibidos
- **NUNCA usar** `;` (ponto e vírgula) — substituir por vírgula ou ponto
- **NUNCA usar** `:` (dois pontos) no corpo do texto — substituir por vírgula ou ponto
- **NUNCA usar** `—` (travessão) — substituir por vírgula ou ponto
- **NUNCA usar** aspas curvas `" "` — usar apenas aspas retas `" "`
- Aspas retas usadas **somente** no trecho literário do Narrar
- **NUNCA usar** emojis no corpo do texto

### Limites de Texto
- Frases com no máximo **30 palavras**
- Parágrafos com no máximo **70 palavras**
- Primeiro parágrafo **NUNCA** repete o conteúdo do título ou subtítulo

### Capitalização (padrão europeu — Acordo Ortográfico 1990)

> **Referência completa**: `editorial-squad/skills/capitalizer/SKILL.md`

- **Sentence-case** como padrão: maiúscula apenas na primeira palavra e nomes próprios
- **Nomes próprios** (Constantinopla, Bizâncio, Justiniano) → sempre maiúscula
- **Nomes institucionais consolidados** (Império Bizantino, Igreja Católica) → maiúscula
- **Termos descritivos/genéricos** (império romano, oriente, ocidente, arte bizantina) → minúscula no corpo
- **Preposições e artigos** (de, da, do, em, o, a, e) → minúscula no meio de títulos
- **Consistência obrigatória**: o mesmo termo deve ter a mesma capitalização em todas as seções
- **Não** usar maiúscula após dois-pontos (exceto nomes próprios, siglas, itens de lista)

### Negrito
- Usar negrito (`**texto**`) apenas para destacar termos-chave na terceira repetição do accordion
- Cada `[+FILL_IN]` deve ter exatamente 3-4 lacunas com `_____`

### Versículos
- Preferencialmente ARA ou ARC
- Formato completo: "Texto do versículo" — Referência (ex: Provérbios 22:29)
- No [+IMAGE_TEXT_ON], formato curto: "Texto resumido — Referência"

## Estrutura de Aula (5 Hábitos)

Toda aula é organizada nos **5 Hábitos** da Pedagogia do Belo:

| Hábito | Função | Seção no Rise |
|--------|--------|---------------|
| **Definir** | Apresentar o conceito central | `## Definir` |
| **Perceber** | Observar visualmente o conceito | `## Perceber` |
| **Recordar** | Memorizar a definição | `## Recordar` |
| **Praticar** | Exercitar o conceito | `## Praticar` |
| **Narrar** | Contextualizar narrativamente | `## Narrar` |

## Repetição Obrigatória da Definição

A definição do termo principal deve aparecer **idêntica** em:

1. Cabeçalho do Definir, primeira linha em negrito
2. No Recordar (Statement_D)
3. Na Revisão semanal (tabela + Recordar)

O Accordion usa a definição curta e a explicação completa em texto narrável. O texto após MP3\ repete o conteúdo do áudio, podendo manter negritos para leitura visual.

## Repetição Obrigatória das Palavras-Chave

O tema e a definição de `x.1` geram palavras-chave estruturantes. Em `x.2` e `x.3`, essas palavras devem aparecer no parágrafo livre do Definir, no Perceber, na Atividade Extra do Praticar e no texto do Narrar.

Use a repetição lexical para manter a criança em contato com o mesmo eixo da semana. Não substitua palavras centrais por sinônimos quando a intenção for fixação.

Exemplo:

```markdown
A arte nos lugares da vida

@link_png@

[MP3/]

#FSH:0b12d715e4c741399594fccb12d4bbe2

A arte está nos lugares da vida como resposta à beleza criada por Deus.

O ser humano reconhece arte quando observa beleza em casa, na igreja, nos livros e na natureza.

[MP3\]

**A arte está nos lugares da vida como resposta à beleza criada por Deus.**

O ser humano reconhece **arte** quando observa beleza em casa, na igreja, nos livros e na natureza.
```

## Regras por Bloco

### Accordion
- Tema ou pergunta simples da aula.
- Manter `@link_png@` logo abaixo do tema.
- O áudio contém a definição curta e a explicação completa em texto narrável.
- O texto após MP3\ repete o conteúdo do áudio, podendo manter negritos para leitura visual.
- Voice ID obrigatório: `#11L:XXXXXXXXXXXXXXXXX`

### Fill_In
- SEMPRE com parágrafo de enunciado ANTES: `[+PARAGRAPH] Complete as lacunas... [-PARAGRAPH]`
- O bloco contém SOMENTE o conceito (NUNCA instrução)
- 3-4 lacunas com `_____` (5 underscores)
- Respostas na última linha, separadas por vírgula e espaço, na ordem das lacunas

### Praticar
- Manter sempre a sequência `[+FILL_IN]`, `[+MULTIPLE]`, `[+ACTIVITY_WORKSHEET]`.
- O `[+MULTIPLE]` vem depois do Fill_In, com heading `Atividade 2`.
- A resposta correta do `[+MULTIPLE]` é a definição curta completa e literal.
- A Atividade Extra usa `[+ACTIVITY_WORKSHEET]` com `INSTRUCTION=`.
- Não usar `[+ATTACHMENT]` com `@link_pdf@`.

### Matching
- SEMPRE a definição primeiro, termo depois do `[=]`
- SEMPRE com enunciado antes

### Narrar
- Trecho literário cristão, puritano ou poético entre aspas retas
- No 3º ano, usar `[+PARAGRAPH]` para a leitura e manter `[+IMAGE]` com `@link_png@` antes das perguntas
- Nos demais anos, usar `[+IMAGE_TEXT_ASIDE]` conforme o template
- 3 perguntas com interrogação e espaçamento entre elas
- Perguntas curtas, diretas e fáceis de compreender
- Cada resposta deve aparecer explicitamente no texto lido
- O trecho deve trazer elementos claros do tema da aula

## Placeholders de Mídia

| Placeholder | Significado |
|-------------|-------------|
| `@link_png@` | Imagem a ser inserida |
| `@link_mp3@` | Áudio a ser inserido |
| `@link_pdf@` | PDF de atividade |
| `[+VIDEO][-VIDEO]` | Vídeo (sem conteúdo entre tags) |

## Estrutura de Arquivo

- Título: `# Título da Aula` (H1)
- Seções: `## Definir`, `## Perceber`, `## Recordar`, `## Praticar`, `## Narrar` (H2)
- Sub-headings: usar Rise Block `[+HEADING]` (NUNCA H3)
- Nome do arquivo: `X.Y.md` (ex: `36.3.md`)
- Duração máxima: 10 minutos por aula
