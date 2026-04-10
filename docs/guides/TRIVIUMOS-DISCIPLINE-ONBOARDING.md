# Onboarding de Disciplina no TriviumOS

## Objetivo

Permitir que cada membro da equipe replique o mesmo framework-base, mudando apenas a base de conhecimento da sua disciplina.

## Passos

1. Crie `disciplines/<nome-da-disciplina>/`
2. Adicione:
   - `knowledge-base/`
   - `curriculum/`
   - `reports/`
3. Defina nomenclatura e calendário da disciplina
4. Escolha quais agentes e workflows usar primeiro
5. Teste o fluxo com `npm run triviumos:doctor`

## Regra prática

Nao customize `triviumos/` por disciplina.  
Customizações disciplinares devem viver em `disciplines/`.

