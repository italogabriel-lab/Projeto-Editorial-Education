# 4. Praticar (Hábito 4 de 5)

## Princípio pedagógico

Este é o **quarto contato da criança com o tema da aula**, agora pela via da aplicação e exercício. O Fill_In reproduz a definição com lacunas para a criança completar de memória. A múltipla escolha testa o reconhecimento da definição. A atividade extra (PDF) propõe uma experiência prática relacionada ao conceito. A criança deve sair deste hábito tendo aplicado o conceito ativamente.

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

- O Fill_In usa EXATAMENTE a definição do Recordar com lacunas nas palavras-chave.
- O bloco `[+MULTIPLE]` é obrigatório e permanece entre o Fill_In e a Atividade Extra.
- A múltipla escolha tem a definição correta como resposta certa.
- Os distratores devem ser plausíveis mas claramente errados para quem estudou o conceito.
- A Atividade Extra DEVE ter relação direta com o conceito — não pode ser atividade genérica.
- Não usar `[+ATTACHMENT]` com `@link_pdf@` (padrão descontinuado).
- Sem `;`, `:`, `—` — usar `,` ou `.`.
- Voz ativa, imperativo.
