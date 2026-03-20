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

1. Final do parágrafo introdutório (Definir)
2. Dentro do Accordion — texto plano
3. Dentro do Accordion — áudio (entre MP3/ e MP3\)
4. Dentro do Accordion — com negrito (após MP3\)
5. No Recordar (Statement_D)
6. Na Revisão semanal (tabela + Recordar)

## Regras por Bloco

### Accordion
- Pergunta: "O que é [Termo]?" (com o nome exato do termo)
- Definição direta ao ponto, SEM repetir o termo como prefixo
- A mesma definição 3x: texto plano, áudio, negrito
- Reflexão começa com "Entenda que..."
- Voice ID obrigatório: `#11L:XXXXXXXXXXXXXXXXX`

### Fill_In
- SEMPRE com parágrafo de enunciado ANTES: `[+PARAGRAPH] Complete as lacunas... [-PARAGRAPH]`
- O bloco contém SOMENTE o conceito (NUNCA instrução)
- 3-4 lacunas com `_____` (5 underscores)
- Respostas na última linha, separadas por vírgula e espaço, na ordem das lacunas

### Matching
- SEMPRE a definição primeiro, termo depois do `[=]`
- SEMPRE com enunciado antes

### Narrar
- Trecho literário cristão, puritano ou poético entre aspas retas
- 3 perguntas com interrogação e espaçamento entre elas
- Perguntas sempre relacionadas ao conteúdo da aula

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
