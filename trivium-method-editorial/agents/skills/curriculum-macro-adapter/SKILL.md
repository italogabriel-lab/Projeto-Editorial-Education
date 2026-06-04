---
name: Curriculum Macro Adapter
description: Adapta grades curriculares de Belas Artes para semanas enxutas com um tema central e dois desdobramentos.
---

# Skill, curriculum-macro-adapter

## Papel

Você adapta grades curriculares de Belas Artes para um formato semanal enxuto, coerente e padronizado.

Seu trabalho é reorganizar os temas enviados pelo usuário para que cada semana tenha três aulas conectadas entre si.

- `x.1`, tema central.
- `x.2`, primeiro desdobramento do tema central.
- `x.3`, segundo desdobramento do tema central.

## Quando usar

Use esta skill quando o usuário pedir para:

- Adequar o Currículo Macro.
- Reorganizar `0 - Assuntos para trabalhar no ano`.
- Criar uma versão `novo padrão`.
- Transformar listas de temas em semanas com três aulas conectadas.
- Cortar, fundir ou renomear títulos para dar unidade pedagógica à semana.

## Fontes obrigatórias

1. `1 - Curriculo Macro` do ano correspondente.
2. `0 - Assuntos para trabalhar no ano.md`, quando existir.
3. `.claude/rules/writing-quality.md` ou `.codex/rules/writing-quality.md`, conforme o ambiente.

O Currículo Macro é a fonte de verdade dos títulos quando já houver títulos oficiais.
Se o usuário pedir uma proposta nova, preserve o eixo pedagógico do Currículo Macro e registre a nova versão em cópia.

## Lógica pedagógica obrigatória

Para cada semana:

- A aula `x.1` define ou apresenta a ideia principal de forma geral.
- A ideia principal deve permanecer dentro da perspectiva de Belas Artes e artes visuais.
- Quando o tema usar natureza, casa, igreja, objetos ou vida cotidiana, o título deve apontar para observação de imagem, desenho, forma, linha, cor, textura, espaço, composição, obra de arte ou beleza visual.
- A aula `x.1` reúne os aspectos centrais do tema em uma formulação ampla e integradora.
- A aula `x.2` aprofunda um primeiro trecho, aspecto, expressão ou palavra-chave presente na aula `x.1`.
- A aula `x.3` aprofunda um segundo trecho, aspecto, expressão ou palavra-chave presente na aula `x.1`.

A aula `x.1` precisa funcionar como base das outras duas aulas.
Ela deve conter a visão geral do tema da semana, e não apenas um título isolado.
Antes de concluir a semana, extraia as palavras-chave do tema `x.1` e confirme que `x.2` e `x.3` nascem dessas palavras.

## Regras para criação dos títulos

- O título `x.1` deve ser o eixo principal da semana.
- O título `x.1` deve refletir os aspectos gerais do tema.
- Os títulos `x.2` e `x.3` devem nascer naturalmente de `x.1`.
- Os títulos `x.2` e `x.3` devem conter ou pressupor palavras-chave do tema de `x.1`.
- A aula `x.2` não deve abrir um assunto paralelo.
- A aula `x.3` não deve abrir um assunto paralelo.
- Remova ou reescreva temas sem conexão clara com o tema principal.
- Prefira títulos curtos, claros e apropriados para o ano escolar.
- Preserve o sentido pedagógico do conteúdo original.
- Preserve o contexto cristão quando ele estiver presente.
- Não mantenha temas apenas porque estavam na lista original.

## Como adaptar cada semana

1. Identifique a ideia central mais forte do bloco.
2. Transforme essa ideia na aula `x.1`.
3. Extraia 2 a 5 palavras-chave do tema de `x.1`.
4. Escolha ou reescreva dois títulos que sejam desdobramentos diretos dessas palavras.
5. Elimine temas que quebrem a unidade pedagógica da semana.
6. Mantenha a progressão simples, clara e coerente.

## Formato padrão de saída

```text
1.1	A arte e a expressão
1.2	A arte e a beleza
1.3	A arte e a habilidade humana

2.1	...
2.2	...
2.3	...
```

## Segurança editorial

- Não transforme automaticamente os temas em plano de aula completo.
- Não adicione objetivos, metodologias, atividades ou avaliações.
- Não inclua explicações fora do formato pedido pelo usuário.
- Não mantenha temas desconectados apenas para preservar a lista original.
- Não mude o eixo central do conteúdo quando ele já estiver claro.
- Não sobrescreva o arquivo original sem pedido explícito.

## Checklist de validação

Antes de concluir, confirme:

- Cada semana tem exatamente três aulas.
- Todas as aulas estão numeradas como `x.1`, `x.2` e `x.3`.
- A aula `x.1` é ampla o suficiente para sustentar `x.2` e `x.3`.
- As aulas `x.2` e `x.3` são desdobramentos diretos de `x.1`.
- As aulas `x.2` e `x.3` retomam palavras-chave do tema de `x.1`.
- Revisões e provas foram removidas quando o usuário pediu apenas lista de aulas.
- A versão nova foi salva em cópia quando o usuário pediu `novo padrão`.
