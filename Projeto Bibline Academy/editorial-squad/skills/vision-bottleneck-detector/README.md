# ⚠️ Vision Bottleneck Detector - Documentação Completa

**Detector de Gargalos e Alertas do Pipeline Editorial**

---

## Visão Geral

| Propriedade | Valor |
|-------------|-------|
| **Nome** | Vision Bottleneck Detector |
| **Tipo** | Detector de Gargalos |
| **Escopo** | Vision Board |
| **Status** | ✅ Ativo |
| **Versão** | 1.0 |

---

## Objetivo

Identificar automaticamente gargalos no pipeline de produção editorial e gerar alertas acionáveis.

---

## Comandos

### `/bottleneck detect [disciplina]`

**Descrição:** Detecta gargalos no pipeline.

**Sintaxe:**
```bash
/bottleneck detect [disciplina]
```

**Exemplo:**
```bash
/bottleneck detect
/bottleneck detect "História"
```

---

### `/bottleneck alert <threshold>`

**Descrição:** Configura threshold para alertas.

**Sintaxe:**
```bash
/bottleneck alert <percentage>
```

**Exemplo:**
```bash
/bottleneck alert 20
```

---

## Tipos de Gargalos Detectados

### 1. Acúmulo por Status
- **In Review > 20 tickets** → Gargalo de revisão
- **Video > 30 tickets** → Gargalo de produção de vídeo
- **Backlog > 50 tickets** → Atraso na produção

### 2. Disciplina Atrasada
- **Progress < 50%** da meta → Atenção
- **Progress < 25%** da meta → Crítico

### 3. Semana Incompleta
- **Semana com < 3 aulas** → Incompleta
- **Semana sem revisão** → Pendente

---

## Links

- [Skill](SKILL.md)
- [Performance Analytics](../performance-analytics/)
