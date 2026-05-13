---
description: Adequar currículo macro ou assuntos do ano para semanas com tema central e dois desdobramentos
---

# /curriculum-macro-adapter

Use este comando para reorganizar uma grade de Belas Artes em semanas com três aulas conectadas.

## Entrada

O usuário deve informar, ou o agente deve identificar pelo contexto:

- O ano escolar.
- O arquivo de origem, normalmente `0 - Assuntos para trabalhar no ano.md`.
- Se deve criar cópia com `novo padrão` no nome.

## Passos

1. Ler `trivium-method-editorial/agents/skills/curriculum-macro-adapter/SKILL.md`.
2. Localizar o `1 - Curriculo Macro` do ano correspondente.
3. Localizar o arquivo `0 - Assuntos para trabalhar no ano.md`.
4. Criar cópia com `novo padrão` no nome quando solicitado.
5. Reorganizar cada bloco em `x.1`, `x.2` e `x.3`.
6. Remover revisão e provas quando o pedido for apenas a nova lista de aulas.
7. Validar que cada semana tem exatamente três aulas conectadas.

## Saída

Entregar apenas a lista organizada quando o usuário pedir o material final.

## Argumentos

$ARGUMENTS
