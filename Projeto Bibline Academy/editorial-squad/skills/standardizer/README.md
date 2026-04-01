# 📏 Standardizer Agent - Documentação Completa

**Agente de Padronização e Formatação Rise Blocks - Etapa 3**

---

## Visão Geral

| Propriedade | Valor |
|-------------|-------|
| **Nome** | Standardizer |
| **Tipo** | Editor de Estilo |
| **Escopo** | Editorial Squad |
| **Status** | ✅ Ativo |
| **Versão** | 1.0 |
| **Etapa** | 3 |

---

## Objetivo

Transforma rascunho do Writer em conteúdo formatado com Rise Blocks, aplicando correções editoriais.

---

## Comandos

### `/standardize <arquivo>`

**Descrição:** Formata arquivo em Rise Blocks.

**Sintaxe:**
```bash
/standardize draft_class.md
```

---

## Rise Blocks Tags

| Tag | Uso |
|-----|-----|
| `[+PARAGRAPH]` | Texto corrido |
| `[+HEADING]` | Subtítulos |
| `[+ACCORDION]` | Definição expandível |
| `[+VIDEO]` | Placeholder vídeo |
| `[+IMAGE_LABELED]` | Imagem com hotspots |
| `[+FILL_IN]` | Lacunas |

---

## Correções Proativas

1. Remover `;`, `:`, `—`
2. Converter aspas curvas → retas
3. Voz passiva → ativa
4. Imperativo direto
5. Sentence-case europeu

---

## Links

- [Skill](SKILL.md)
- [Rise Blocks](../../knowledge-base/rise-blocks-reference.md)
