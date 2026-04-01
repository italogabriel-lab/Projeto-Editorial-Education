# 📈 Vision Progress Engine - Documentação Completa

**Motor de Progresso e Atualização do Vision Board**

---

## Visão Geral

| Propriedade | Valor |
|-------------|-------|
| **Nome** | Vision Progress Engine |
| **Tipo** | Motor de Progresso |
| **Escopo** | Vision Board |
| **Status** | ✅ Ativo |
| **Versão** | 1.0 |

---

## Objetivo

Calcular e atualizar automaticamente o progresso das disciplinas no Vision Board com base nos dados do Kanban.

---

## Comandos

### `/progress calculate <disciplina> <ano>`

**Descrição:** Calcula progresso de uma disciplina.

**Sintaxe:**
```bash
/progress calculate <disciplina> <ano>
```

**Exemplo:**
```bash
/progress calculate "Matemática" 2
```

---

### `/progress update`

**Descrição:** Atualiza todos os painéis de progresso.

**Sintaxe:**
```bash
/progress update
```

---

## Métricas Calculadas

### 1. Progresso por Disciplina
```
Progress = (Produced / Goal) * 100
```

### 2. Progresso por Ano
```
Year Progress = (Year Produced / Year Goal) * 100
```

### 3. Meta da Equipe
```
Team Goal = 168 lessons/year * 5 years = 840 lessons
```

---

## Links

- [Skill](SKILL.md)
- [Performance Analytics](../performance-analytics/)
