# 📝 Copywriter Agent - Documentação Completa

**Agente de Polimento Final e Otimização - Etapa 5 do Fluxo Editorial**

---

## Visão Geral

| Propriedade | Valor |
|-------------|-------|
| **Nome** | Copywriter |
| **Tipo** | Polidor Final |
| **Escopo** | Editorial Squad |
| **Status** | ✅ Ativo |
| **Versão** | 1.0 |
| **Etapa** | 5 |

---

## Objetivo

O **Copywriter** dá o acabamento final ao conteúdo revisado, otimizando títulos, enunciados e garantindo que o material esteja impecável para publicação.

**Quando usar:**
- Conteúdo já foi revisado e aprovado (Etapa 4)
- Precisa de polimento final antes da publicação
- Otimizar títulos e enunciados
- Garantir fluidez e tom consistente

---

## Comandos

### `/polish <arquivo>`

**Descrição:** Aplica polimento final em arquivo revisado.

**Sintaxe:**
```bash
/polish reviewed_class.md
```

**Exemplo:**
```bash
/polish "36.3_reviewed.md"
```

**Saída:**
```markdown
# 📝 Polimento Aplicado — Aula 36.3

## Ajustes Realizados

### 1. Título (H1)
- **Antes:** "A arte como linguagem da fé"
- **Depois:** "A Arte como Linguagem da Fé na Cosmovisão Cristã"
- ✅ Mais engajante e específico

### 2. Enunciados
- ✅ Todos em imperativo direto
- ✅ Variação de verbos aplicada
- ✅ Clareza otimizada

### 3. Reflexão Teológica
- ✅ Conectada à vida do aluno
- ✅ Começa com "Entenda que..."
- ✅ Profunda mas acessível

### 4. Trecho Literário
- ✅ Poético e elevado
- ✅ Atribuição formatada corretamente
- ✅ Conexão clara com tema

### 5. Perguntas (Narrar)
- ✅ 3 perguntas abertas
- ✅ Progressão em profundidade
- ✅ Estimulam articulação

## Output
Arquivo: `final_class.md` — Pronto para publicação!
```

---

## Checklist de Ajustes Finais

### **1. Título da Aula (H1)**
- [ ] Criativo e engajante
- [ ] Desperta curiosidade
- [ ] Reflete conteúdo sem ser literal
- [ ] Capitalização europeia

### **2. Enunciados**
- [ ] Claro e direto
- [ ] 100% imperativo
- [ ] Variação de verbos

### **3. Accordion — Reflexão**
- [ ] Profunda mas acessível
- [ ] Conecta à vida do aluno
- [ ] Começa com "Entenda que..."

### **4. Narrar — Trecho**
- [ ] Poético e elevado
- [ ] Atribuição completa
- [ ] Conexão com tema

### **5. Narrar — Perguntas**
- [ ] 3 perguntas abertas
- [ ] Reflexivas
- [ ] Progressão: observação → interpretação → aplicação

### **6. Fluidez Geral**
- [ ] Transição natural entre hábitos
- [ ] Tom consistente
- [ ] Ritmo agradável

### **7. Conformidade Final**
- [ ] Sem `;`, `:`, `—`
- [ ] Sem aspas curvas
- [ ] Sem emojis
- [ ] Sem separadores `---`
- [ ] Sem metadados
- [ ] Tags Rise fechadas

---

## Protocolo de Ajuste

### **Problemas Menores**
- Título, enunciado, fluidez
- **Ação:** Corrigir diretamente

### **Problemas Estruturais**
- Definições alteradas
- Blocos Rise faltando
- **Ação:** Retornar à Etapa 3 ou 4

### **NUNCA Alterar**
- ❌ Definição do termo (validada pelo Reviewer)
- ❌ Adicionar/remover blocos Rise

---

## Exemplo de Uso

### **Cenário: Polimento de Aula**

```bash
@copywriter "Polir aula 12.5 sobre Arte Islâmica"
```

**Resposta:**
```markdown
# ✅ Polimento Concluído — Aula 12.5

## Melhorias Aplicadas

### Título
- **Original:** "Arte Islâmica e Geometria"
- **Otimizado:** "A Geometria Sagrada na Arte Islâmica: Ordem e Beleza"

### Enunciados Otimizados
1. "Observe o padrão geométrico" → "Analise o padrão geométrico islâmico"
2. "Complete a atividade" → "Preencha as lacunas com os termos corretos"

### Reflexão Teológica
- ✅ Conectada à cosmovisão cristã
- ✅ Aplicação prática para o aluno

### Perguntas do Narrar
1. **Observação:** "O que você vê no padrão?"
2. **Interpretação:** "O que isso revela sobre a cosmovisão islâmica?"
3. **Aplicação:** "Como isso se relaciona com sua fé?"

## Status: ✅ Pronto para Publicação
```

---

## Links

- [Skill](SKILL.md)
- [Guia de Estilo](../../knowledge-base/guia-de-estilo.md)
- [Template](../../templates/padrao_final_aula.md)
