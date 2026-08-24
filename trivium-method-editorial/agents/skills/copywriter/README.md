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

### 3. Accordion
- ✅ MP3 com definição curta e explicação completa
- ✅ Texto visual equivalente ao áudio
- ✅ `@link_png@` preservado dentro do bloco

### 4. Trecho Literário
- ✅ Claro, narrativo e acessível
- ✅ Respostas explícitas para as perguntas
- ✅ Atribuição formatada corretamente
- ✅ Conexão clara com tema

### 5. Perguntas (Narrar)
- ✅ 2 perguntas curtas e diretas no 2º ano
- ✅ Respostas explícitas no texto
- ✅ Ajudam a criança a narrar com suas palavras

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

### **3. Accordion — Definição**
- [ ] Contém tema, `@link_png@`, MP3 e texto visual
- [ ] MP3 narra definição curta e explicação completa
- [ ] Texto após `[MP3\]` repete o conteúdo do áudio com negritos permitidos

### **4. Narrar — Trecho**
- [ ] Claro, narrativo e acessível
- [ ] Respostas explícitas para as perguntas
- [ ] Atribuição completa
- [ ] Conexão com tema

### **5. Narrar — Perguntas**
- [ ] 2 perguntas curtas e diretas no 2º ano
- [ ] Respostas explícitas no texto
- [ ] Sem perguntas abertas, reflexivas ou inferenciais

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

### Perguntas do Narrar
1. "O que aparece no padrão?"
2. "Que formas se repetem no desenho?"
3. "Como o padrão mostra ordem?"

## Status: ✅ Pronto para Publicação
```

---

## Links

- [Skill](SKILL.md)
- [Guia de Estilo](../../knowledge-base/guia-de-estilo.md)
- [Template](../../templates/padrao_final_aula.md)
