# 4. Praticar (Hábito 4 de 5)

## Princípio pedagógico

Este é o **quarto contato da criança com o tema da semana**, agora pela via da aplicação e exercício. O Fill_In reproduz a definição curta com lacunas para a criança completar de memória. A múltipla escolha testa o reconhecimento do conceito específico daquela aula, com pergunta derivada do parágrafo livre. A atividade extra (PDF) propõe uma experiência prática relacionada ao ângulo daquela aula. A criança deve sair deste hábito tendo aplicado o tema ativamente.

Em `x.2` e `x.3`, a aplicação deve usar palavras-chave de `x.1` dentro do ângulo da aula.

## Estrutura obrigatória

```markdown
[+HEADING]
Atividade
[-HEADING]

[+PARAGRAPH]
Complete as lacunas para reafirmar a definição que você aprendeu.
[-PARAGRAPH]

[+FILL_IN]

[Definição do Recordar com _____ nas lacunas — 2 a 4 lacunas]

[resposta1, resposta2]

[-FILL_IN]

[+HEADING]
Atividade 2
[-HEADING]

[+MULTIPLE]

[Pergunta derivada do parágrafo livre desta aula. Formatos válidos: "O que [TERMO] [VERBO]?", "Como [TERMO] [VERBO]?", "Onde [TERMO] aparece?", "Para que [TERMO] [VERBO]?", "Quando [TERMO] [VERBO]?", "Quais [ELEMENTOS]?". A pergunta deve diferir entre x.1, x.2 e x.3.]

[Frase-chave do parágrafo livre — resposta correta] [=] true
[Distrator — temático mas conceitualmente errado] [=]

[-MULTIPLE]

[+HEADING]
Atividade Extra
[-HEADING]

[+PARAGRAPH]
Acesse o PDF abaixo e faça a atividade com atenção.
[-PARAGRAPH]

[+ACTIVITY_WORKSHEET]

INSTRUCTION=[Instrução de atividade prática no imperativo. A atividade DEVE envolver o conceito definido no Definir de forma concreta e sensorial.]

[-ACTIVITY_WORKSHEET]
```

## Regras

- O Fill_In usa EXATAMENTE a definição do Recordar com lacunas nas palavras-chave (a mesma frase em `x.1`, `x.2` e `x.3`).
- A lacuna escolhida pode variar entre as aulas da semana para destacar palavras diferentes do mesmo enunciado.
- O bloco `[+MULTIPLE]` é obrigatório e permanece entre o Fill_In e a Atividade Extra.
- **Pergunta do [+MULTIPLE]**: derivada do parágrafo livre daquela aula específica. Formatos válidos: "O que [TERMO] [VERBO]?", "Como [TERMO] [VERBO]?", "Onde [TERMO] aparece?", "Para que [TERMO] [VERBO]?", "Quando [TERMO] [VERBO]?", "Quais [ELEMENTOS]?". A pergunta deve ser diferente em x.1, x.2 e x.3 do mesmo trio semanal.
- **Resposta correta**: frase-chave do parágrafo livre, extraível diretamente do texto.
- **Distrator**: relacionado ao tema mas conceitualmente errado. Plausível mas claramente incorreto para quem estudou.
- **2 opções** para o 1º ano (1 correta + 1 distratora). A resposta correta vem primeiro no bloco.
- Proibido: "Qual é o significado de [TERMO]?" como pergunta fixa para todas as aulas — viola a diferenciação entre x.1, x.2 e x.3.
- A Atividade Extra DEVE ter relação direta com o ângulo da aula dentro do tema da semana — não pode ser atividade genérica.
- A Atividade Extra deve aplicar palavras-chave estruturantes do tema central.
- Não usar `[+ATTACHMENT]` com `@link_pdf@` (padrão descontinuado).
- Sem `;`, `:`, `—` — usar `,` ou `.`.
- Voz ativa, imperativo.
