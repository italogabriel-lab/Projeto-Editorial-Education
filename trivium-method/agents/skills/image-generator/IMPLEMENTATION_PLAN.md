# 🎨 Plano de Implementação - Text-to-Image

## 📊 Análise de Modelos Gratuitos

### **Melhores Opções Gratuitas (2026)**

| Rank | Modelo | Provider | Qualidade | Velocidade | Limite | API Key |
|------|--------|----------|-----------|------------|--------|---------|
| **1** | **FLUX.1-schnell** | Black Forest Labs | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Unlimited | ❌ Não |
| **2** | **SDXL Turbo** | Stability AI | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 1000/day | ✅ Sim |
| **3** | **Pollinations (Flux)** | Pollinations.ai | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Unlimited | ✅ Sim |
| **4** | **Z-Image-Turbo** | Tongyi-MAI | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 500/day | ✅ Sim |

---

## 🏆 **RECOMENDAÇÃO: Pollinations.ai com FLUX.1**

### **Por que Pollinations?**

✅ **Vantagens:**
- **100% Gratuito** - Sem limites diários
- **Modelo FLUX.1** - Estado da arte em qualidade
- **Sem API Key necessária** - Já configurada
- **Rápido** - ~10-20 segundos por imagem
- **Simples** - API REST via GET
- **Alta Resolução** - Até 2048x2048

❌ **Desvantagens:**
- Menos controle de parâmetros vs HuggingFace

---

## 📋 **Plano de Implementação**

### **Fase 1: Configuração (✅ COMPLETO)**

- [x] API Key no .env
- [x] Scripts Python criados
- [x] Documentação completa

### **Fase 2: Testes (PRÓXIMO)**

- [ ] Testar geração de 1 imagem
- [ ] Testar geração de 1 semana (3 imagens)
- [ ] Validar qualidade
- [ ] Ajustar prompts se necessário

### **Fase 3: Produção**

- [ ] Gerar todas as imagens do 3º ano
- [ ] Organizar na hierarquia
- [ ] Gerar log completo

---

## 🔧 **Configuração Necessária**

### **1. API Keys (JÁ CONFIGURADAS)**

```bash
# .env file
POLLINATIONS_KEY=sk_XYebI51eWx0LmXAFnRvDQyCCNn2t9yMU
```

### **2. Instalar Dependências**

```bash
cd trivium-method/agents/skills/image-generator/
pip install -r requirements.txt
```

### **3. Testar API**

```bash
# Teste rápido
python scripts/test_api.py
```

---

## 🚀 **Comandos de Teste**

### **Teste 1: Gerar Única Imagem**

```bash
cd trivium-method/agents/skills/image-generator/

python scripts/generate_images.py \
  "Ilustração em aquarela, império bizantino, luz dourada" \
  test_output.png \
  pollinations
```

**Resultado Esperado:**
- ✅ Arquivo `test_output.png` criado
- ✅ Qualidade alta (1024x1024)
- ✅ Tempo: ~15 segundos

---

### **Teste 2: Gerar Semana Completa**

```bash
python scripts/main.py generate-week 3 1 \
  --output test_semana1/
```

**Resultado Esperado:**
- ✅ 3 imagens geradas (1.1, 1.2, 1.3)
- ✅ Prompts salvos em .txt
- ✅ Hierarquia correta

---

### **Teste 3: Gerar Ano Completo**

```bash
python scripts/main.py generate 3 \
  --output generated/imagens-narrar/3-ano/
```

**Resultado Esperado:**
- ✅ 120 imagens (40 semanas × 3 aulas)
- ✅ LOG.md gerado
- ✅ Tempo: ~45-60 minutos

---

## 📊 **Cronograma Estimado**

| Tarefa | Tempo | Status |
|--------|-------|--------|
| Configuração | 5 min | ✅ Completo |
| Teste 1 imagem | 1 min | ⏳ Pendente |
| Teste 1 semana | 5 min | ⏳ Pendente |
| Teste ano completo | 60 min | ⏳ Pendente |
| **Total** | **~70 min** | - |

---

## 🎯 **Próximos Passos Imediatos**

### **1. Instalar Dependências**
```bash
cd trivium-method/agents/skills/image-generator/
pip install -r requirements.txt
```

### **2. Rodar Teste Rápido**
```bash
python scripts/test_api.py
```

### **3. Validar Qualidade**
- Abrir imagem gerada
- Verificar estilo aquarela
- Validar resolução

### **4. Ajustar se Necessário**
- Modificar prompts
- Ajustar parâmetros
- Re-testar

---

## 🔗 **Links Úteis**

- [Pollinations.ai Docs](https://pollinations.ai/docs)
- [FLUX.1 Model](https://blackforestlabs.ai/flux/)
- [HuggingFace Inference API](https://huggingface.co/docs/api-inference)
- [Stability AI SDXL](https://stability.ai/stable-diffusion)

---

## 💡 **Dicas de Uso**

### **Para Melhor Qualidade:**

1. **Prompts Detalhados**
   - Adicionar estilo: "watercolor painting"
   - Adicionar iluminação: "warm golden light"
   - Adicionar época: "classical book illustration"

2. **Parâmetros Ótimos**
   ```
   width: 1024
   height: 1024
   seed: [número da aula]
   model: flux
   ```

3. **Fallback**
   - Se Pollinations falhar → HuggingFace SDXL
   - Se HuggingFace falhar → DeepAI

---

## ⚠️ **Solução de Problemas**

### **Imagem Não Gera**
1. Verificar conexão internet
2. Testar URL no browser
3. Verificar timeout (120s)

### **Qualidade Baixa**
1. Aumentar resolução para 2048x2048
2. Adicionar mais detalhes ao prompt
3. Tentar seed diferente

### **API Limit Exceeded**
1. Aguardar reset (24h)
2. Usar plataforma alternativa
3. Dividir geração em lotes

---

**Status:** ✅ **PRONTO PARA TESTAR**  
**Versão:** 1.0.0  
**Data:** 2026-04-01
