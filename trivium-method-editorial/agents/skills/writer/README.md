# ✍️ Writer Agent - Documentação Completa

**Agente de Redação de Conteúdo Didático - Etapa 2 do Fluxo Editorial**

---

## Visão Geral

| Propriedade | Valor |
|-------------|-------|
| **Nome** | Writer |
| **Tipo** | Redator |
| **Escopo** | Editorial Squad |
| **Status** | ✅ Ativo |
| **Versão** | 1.0 |
| **Etapa** | 2 |

---

## Objetivo

O **Writer** (Escriba) transforma pesquisa bruta em conteúdo pedagógico usando os 5 Hábitos da Gramática, seguindo rigorosamente o golden template.
Ele preserva a progressão por palavras-chave: `x.1` define o eixo lexical da semana, e `x.2` e `x.3` retomam essas palavras nos exemplos e atividades.

**Quando usar:**
- Recebeu relatório de pesquisa do Researcher
- Precisa criar conteúdo de aula
- Segue progressão pedagógica do Plano
- Precisa manter `x.2` e `x.3` ligados às palavras-chave de `x.1`

---

## Comandos

### `/write <aula> <ano> <pesquisa>`

**Descrição:** Redige aula baseada em pesquisa.

**Sintaxe:**
```bash
/write <aula> <ano> <pesquisa.md>
```

**Exemplo:**
```bash
/write 3.2 3 "research_3.2.md"
```

---

## Estrutura da Aula

### 5 Hábitos da Gramática

1. **Definir** - Webster 1828, etimologia
2. **Perceber** - Imagens, obras de arte
3. **Recordar** - Versículo, poema, música
4. **Praticar** - Atividades, exercícios
5. **Narrar** - Trecho literário

---

## Regras de Escrita

- ✅ Voz ativa sempre
- ✅ Imperativo direto
- ✅ Frases ≤ 30 palavras
- ✅ Parágrafos ≤ 70 palavras
- ✅ Sem ponto e vírgula
- ✅ Aspas retas apenas

---

## Links

- [Skill](SKILL.md)
- [Template](../../templates/padrao_final_aula.md)
