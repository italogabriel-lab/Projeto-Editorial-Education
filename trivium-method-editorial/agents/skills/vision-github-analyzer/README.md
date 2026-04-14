# 🔬 Vision GitHub Analyzer - Documentação Completa

**Analisador de Dados do GitHub Projects para o Vision Board**

---

## Visão Geral

| Propriedade | Valor |
|-------------|-------|
| **Nome** | Vision GitHub Analyzer |
| **Tipo** | Analista de Dados |
| **Escopo** | Vision Board |
| **Status** | ✅ Ativo |
| **Versão** | 1.0 |

---

## Objetivo

Extrair, transformar e analisar dados do GitHub Projects para alimentar o Vision Board com métricas em tempo real.

---

## Comandos

### `/github sync`

**Descrição:** Sincroniza dados do GitHub Projects.

**Sintaxe:**
```bash
/github sync
```

**Exemplo:**
```bash
/github sync
```

---

### `/github analyze <projeto>`

**Descrição:** Analisa projeto específico.

**Sintaxe:**
```bash
/github analyze <projeto>
```

**Exemplo:**
```bash
/github analyze "Bibline Aulas"
```

---

## Dados Extraídos

### 1. Tickets
- Título
- Status (Backlog, In Progress, Review, Video, Done)
- Assignee
- Labels (disciplina, ano)
- Created/Closed dates

### 2. Métricas
- Total por status
- Total por disciplina
- Total por ano
- Lead time médio
- Throughput semanal

---

## Links

- [Skill](SKILL.md)
- [GitHub Actions](../../.github/workflows/)
