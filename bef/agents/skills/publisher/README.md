# 🚀 Publisher Agent - Documentação Completa

**Agente de Publicação e Distribuição - Etapa 7**

---

## Visão Geral

| Propriedade | Valor |
|-------------|-------|
| **Nome** | Publisher |
| **Tipo** | Publicador |
| **Escopo** | Editorial Squad |
| **Status** | ✅ Ativo |
| **Versão** | 1.0 |
| **Etapa** | 7 |

---

## Objetivo

Salvar aula finalizada localmente e publicar no GitHub.

---

## Comandos

### `/publish <arquivo> <ano> <aula>`

**Descrição:** Publica aula no repositório.

**Sintaxe:**
```bash
/publish final_class.md 3 36.3
```

---

## Etapas

1. **Salvar Localmente**
   ```
   [BASE]/[NUMERO_AULA].md
   ```

2. **Registrar Termo**
   - Marcar ✅ no Currículo Macro

3. **Push GitHub**
   ```
   owner: bibline
   repo: curriculum
   branch: master
   ```

4. **Confirmar**
   - ✅ Local
   - ✅ Macro
   - ✅ GitHub

---

## Links

- [Skill](SKILL.md)
- [Workflow Publish](../../workflows/publish.md)
