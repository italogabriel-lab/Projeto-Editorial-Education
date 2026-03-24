---
description: Invocar o Diretor Editorial para diagnóstico de status e orientação sobre o projeto
---

# Orquestrar — Diretor Editorial

Atalho para ativar o Orquestrador da Squad e obter direção sobre o projeto.

**Uso**: `@orchestrator`, `/orchestrate` ou "O que devo fazer agora?"

---

## Passos

// turbo
1. Ler a skill do orquestrador: `editorial-squad/skills/orchestrator/SKILL.md`

// turbo
2. Identificar o ano em questão. Se o usuário não especificar, usar o contexto dos arquivos abertos ou perguntar.

// turbo
3. Ler o **Currículo Macro** do ano correspondente:
   - Caminho: `[Base do Ano]/Estrutura Curricular - [N]º ANO/1 - Curriculo Macro - *.md`

4. Executar o **Diagnóstico de Progresso** (seção 1 do SKILL.md):
   - Contar semanas ✅ completas
   - Identificar semana em andamento
   - Identificar próxima semana

5. Executar a **Priorização Inteligente** (seção 2 do SKILL.md):
   - Apresentar lista ordenada de próximas ações

6. Se o usuário tiver uma demanda específica, usar a **Tabela de Roteamento** (seção 3) para delegar ao skill/workflow correto.

7. Apresentar o relatório final ao usuário no formato:
   ```
   📊 STATUS — [Ano]
   ✅ Semanas completas: [range]
   🔄 Em andamento: Semana [N] (detalhes)
   ⏭️ Próxima: Semana [N]

   🎯 PRÓXIMAS AÇÕES:
   1. [ação prioritária]
   2. [ação secundária]
   3. [ação terciária]
   ```
