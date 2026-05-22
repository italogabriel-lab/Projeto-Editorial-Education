# 4. Praticar (Hábito 4 de 5)

## Princípio pedagógico

Este é o **quarto contato da criança com o tema da semana**, agora pela via da aplicação e exercício. O Fill_In reproduz a definição curta (a mesma de `x.1`, `x.2` e `x.3`) com lacunas para a criança completar de memória. A múltipla escolha testa o reconhecimento da definição. A atividade extra (PDF) propõe uma experiência prática relacionada ao ângulo daquela aula dentro do tema da semana. A criança deve sair deste hábito tendo aplicado o tema ativamente.

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

Qual é o significado de [TERMO]?

[Distrator — conceito errado relacionado ao tema] [=]
[Definição correta do Definir — palavras idênticas] [=] true
[Distrator — conceito errado relacionado ao tema] [=]

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
- A múltipla escolha tem a definição correta como resposta certa.
- Os distratores devem ser plausíveis mas claramente errados para quem estudou o tema.
- A Atividade Extra DEVE ter relação direta com o ângulo da aula dentro do tema da semana — não pode ser atividade genérica.
- Não usar `[+ATTACHMENT]` com `@link_pdf@` (padrão descontinuado).
- Sem `;`, `:`, `—` — usar `,` ou `.`.
- Voz ativa, imperativo.
