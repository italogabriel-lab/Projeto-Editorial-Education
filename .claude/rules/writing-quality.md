# Qualidade de escrita

## Regras obrigatórias

- Voz ativa.
- Enunciados no imperativo.
- Frases com até 30 palavras.
- Parágrafos com até 70 palavras.
- Capitalização sentence-case no padrão europeu.
- Sem emojis no corpo do texto.

## Sinais a evitar

- `;`
- `:`
- `—`

Substitua por vírgula ou ponto quando estiver escrevendo conteúdo didático.

## Referências

- Guia de estilo, `trivium-method-editorial/knowledge-base/guia-de-estilo.md`
- Doutrina pedagógica, `trivium-method-editorial/knowledge-base/doutrina-pedagogica.md`
- Rise Blocks, `trivium-method-editorial/knowledge-base/rise-blocks-reference.md`
- Golden template, `trivium-method-editorial/templates/padrao_final_aula.md`

## Verificação mínima antes de concluir

- O título bate com o Currículo Macro.
- A definição curta está literalmente idêntica no cabeçalho do Definir, no Recordar e na Revisão.
- **Consistência semanal**: a definição curta de `x.1` é literalmente idêntica em `x.2` e `x.3` da mesma semana. O termo principal e a música/rima do Recordar também são compartilhados pelas 3 aulas. Só variam o parágrafo livre do Definir, a explicação no Accordion, as imagens e a Atividade Extra.
- **Narrar = espelho literal do Definir**: o bloco `[+IMAGE_TEXT_ASIDE]` do Narrar repete literalmente a definição curta e o parágrafo livre do Definir daquela aula. Antes de `[MP3\]`, texto plain. Após `[MP3\]`, texto com negritos progressivos idênticos ao Accordion. Nenhuma frase adicional é permitida — em especial proibidas frases do tipo "A criança aprende a...", "A criança percebe que...".
- **Pergunta do Narrar**: uma única pergunta por aula, heading `Pergunta` (singular). Derivada diretamente do vocabulário do parágrafo livre. Formatos válidos: "O que [TERMO] [VERBO]?", "Como [TERMO] [VERBO]?", "Onde [TERMO] aparece?", "Para que [TERMO] [VERBO]?". A resposta aparece explicitamente no texto. Proibido: "O que você percebeu sobre...", perguntas abertas, reflexivas, abstratas ou inferenciais.
- O áudio do Accordion contém a definição curta e a explicação completa em texto narrável.
- O texto após `[MP3\]` repete o mesmo conteúdo do áudio, podendo manter negritos para leitura visual.
- O Praticar mantém `[+FILL_IN]`, `[+MULTIPLE]` e `[+ACTIVITY_WORKSHEET]`, nessa ordem.
- **[+MULTIPLE] — pergunta específica por aula**: a pergunta é derivada do parágrafo livre daquela aula, não é fixa entre x.1, x.2 e x.3. Formatos válidos: "O que [TERMO] [VERBO]?", "Como [TERMO] [VERBO]?", "Onde [TERMO] aparece?", "Para que [TERMO] [VERBO]?", "Quando [TERMO] [VERBO]?", "Quais [ELEMENTOS]?". Resposta correta = frase-chave do parágrafo livre. Distrator = temático mas conceitualmente errado. 2 opções para o 1º ano. Proibido: "Qual é o significado de [TERMO]?" como pergunta genérica fixa.
- **Fill-In progressivo**: a frase do `[+FILL_IN]` é sempre a definição curta da semana. A posição da lacuna (`_____`) muda em cada aula para cobrir a palavra-chave específica daquela aula. Em `x.1`, a lacuna fica no termo central da semana. Em `x.2`, a lacuna fica na palavra-chave do desdobramento de `x.2`. Em `x.3`, a lacuna fica na palavra-chave do contexto de `x.3`. Exemplo com "O ponto representa o começo de uma arte": `x.1` → `O _____ representa o começo de uma arte.` (ponto); `x.2` → `O ponto representa o _____ de uma arte.` (começo); `x.3` → `O ponto representa o começo de uma _____.` (arte).
- **Progressão de negritos no parágrafo livre**: em `x.1`, o parágrafo livre coloca em negrito somente o TERMO. Em `x.2`, coloca em negrito o TERMO e a KW2 (mesma resposta do fill-in de `x.2`). Em `x.3`, coloca em negrito o TERMO e a KW3 (mesma resposta do fill-in de `x.3`). A palavra-chave em negrito no parágrafo deve ser sempre a mesma do fill-in daquela aula. Exemplo (semana 3): `x.1` → 'Você observa **pontos** na arte'; `x.2` → 'o **ponto** pode ser o **começo** de um desenho'; `x.3` → 'Você usa o **ponto** na **arte** para marcar lugares'. O Accordion replica o parágrafo: plain (sem negrito) no bloco de áudio, bold (com negrito) no texto visual após `[MP3\]`.
- **Parágrafo livre = uma frase única**: o parágrafo livre do Definir contém UMA ÚNICA FRASE direta e objetiva. Nunca escrever segunda frase do tipo "A criança aprende a...", "A criança percebe que...", "A criança cria..." — são genéricas e proibidas. Modelo: `x.1` → 'Você observa **pontos** na arte e percebe como um pequeno sinal pode começar uma imagem.'
- No 3º ano, o Narrar mantém `[+PARAGRAPH]` para a leitura e `[+IMAGE]` com `@link_png@` antes das perguntas.
- Em revisões `.4`, usar **uma definição curta única da semana** (a mesma de `x.1`, `x.2`, `x.3`), não três definições distintas. Quando opcionais, tabelas e matchings não repetem o termo no início da definição.
- **Legendas do `[+IMAGE_LABELED]` na revisão `.4`**: os textos de legenda dos hotspots devem ser literalmente idênticos aos das aulas `x.1`, `x.2` e `x.3` correspondentes — mesmas palavras, mesma capitalização. As coordenadas podem variar conforme a imagem de revisão; os textos, não. Copie os textos diretamente dos arquivos de aula, nunca reescreva de memória.
- A estrutura segue os 5 hábitos.
- O markdown está compatível com o template final.
