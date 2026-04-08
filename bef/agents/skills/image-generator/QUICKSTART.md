# 🚀 Quick Start — Image Generator

**Guia Rápido para Começar a Gerar Imagens**

---

## ⚡ Passo 1: Instalar Dependências (5 min)

```bash
cd bef/agents/skills/image-generator/
pip install -r requirements.txt
```

**O que será instalado:**
- `requests` — HTTP requests
- `Pillow` — Processamento de imagens
- `tqdm` — Barra de progresso
- `python-dotenv` — Carregar .env

---

## ⚡ Passo 2: Testar API (2 min)

```bash
python scripts/test_api.py
```

**Resultado Esperado:**
```
🎨 TESTE POLLINATIONS.AI
==================================================
🔄 Gerando imagem...
✅ SUCESSO!
   Arquivo: test_pollinations_output.png
   Tamanho: 245.3 KB
```

**Se funcionar:** ✅ Vá para Passo 3  
**Se falhar:** Veja [Solução de Problemas](#solução-de-problemas)

---

## ⚡ Passo 3: Gerar Semana de Teste (5 min)

```bash
python scripts/main.py generate-week 3 1 --output test_semana1/
```

**Resultado Esperado:**
```
🎨 Image Generator — Ano 3, Semana 1
==================================================
✅ Semana 1
   ✅ 1.1 — Império Bizantino...
   ✅ 1.2 — Constantinopla...
   ✅ 1.3 — Cristianismo...

📊 ESTATÍSTICAS
==================================================
Total: 3
✅ Sucesso: 3 (100.0%)
```

**Validar:**
```bash
ls -lh test_semana1/semana-1/
# Deve mostrar:
# 1.1_narrar.png
# 1.1_narrar_prompt.txt
# 1.2_narrar.png
# 1.2_narrar_prompt.txt
# 1.3_narrar.png
# 1.3_narrar_prompt.txt
```

---

## ⚡ Passo 4: Gerar Ano Completo (60 min)

```bash
python scripts/main.py generate 3 --output assets/imagens-narrar/3-ano/
```

**Resultado Esperado:**
```
🎨 Image Generator — Ano 3
==================================================
📋 Extraindo prompts...
✅ 120 prompts encontrados

🔄 Gerando 120 imagens...

✅ Semana 1
   ✅ 1.1, 1.2, 1.3
✅ Semana 2
   ✅ 2.1, 2.2, 2.3
...

📊 ESTATÍSTICAS
==================================================
Total: 120
✅ Sucesso: 118 (98.3%)
❌ Falhas: 2 (1.7%)
==================================================
```

---

## ⚡ Passo 5: Validar Resultado

```bash
# Ver estrutura
tree assets/imagens-narrar/3-ano/ -L 2

# Ver log
cat assets/imagens-narrar/3-ano/LOG.md
```

**Estrutura Esperada:**
```
assets/imagens-narrar/3-ano/
├── semana-1/
│   ├── 1.1_narrar.png
│   ├── 1.1_narrar_prompt.txt
│   └── ...
├── semana-2/
├── ...
└── LOG.md
```

---

## 🎨 Parâmetros Opcionais

### **Mudar Resolução**

```bash
python scripts/main.py generate 3 \
  --width 2048 \
  --height 2048
```

### **Usar Plataforma Diferente**

```bash
# HuggingFace (requer token)
python scripts/main.py generate 3 --platform huggingface

# DeepAI
python scripts/main.py generate 3 --platform deepai
```

### **Seed Específica**

```bash
python scripts/main.py generate 3 --seed 123
```

---

## 🔧 Solução de Problemas

### **❌ "ModuleNotFoundError: No module named 'requests'"**

**Solução:**
```bash
pip install -r requirements.txt --user
```

---

### **❌ "Timeout (120s)"**

**Causa:** Conexão lenta com API

**Solução:**
```bash
# Tentar novamente
python scripts/main.py generate-week 3 1

# Ou usar seed diferente
python scripts/main.py generate-week 3 1 --seed 99
```

---

### **❌ "HUGGINGFACE_TOKEN not set"**

**Solução:**

1. **Obter Token:**
   - Acesse: https://huggingface.co/settings/tokens
   - Clique em "Create new token"
   - Nome: `image-generator`
   - Permissão: `read`
   - Copie o token

2. **Adicionar ao .env:**
   ```bash
   # .env file
   HUGGINGFACE_TOKEN=hf_xxx...
   ```

3. **Ou exportar:**
   ```bash
   export HUGGINGFACE_TOKEN=hf_xxx...
   ```

---

### **❌ "Imagem muito pequena"**

**Causa:** API retornou erro em vez de imagem

**Solução:**
```bash
# Verificar URL no browser
# A URL é mostrada no output do teste

# Se URL não funcionar, tentar plataforma alternativa
python scripts/main.py generate 3 --platform huggingface
```

---

### **❌ "PermissionError: [Errno 13] Permission denied"**

**Causa:** Sem permissão para escrever no diretório

**Solução:**
```bash
# Criar diretório com permissões corretas
mkdir -p assets/imagens-narrar/3-ano
chmod 755 assets/imagens-narrar/3-ano

# Ou usar diretório diferente
python scripts/main.py generate 3 --output ~/images/
```

---

## 📊 Comandos Úteis

### **Ver Status**
```bash
python scripts/main.py status 3
```

### **Regenerar Imagem Específica**
```bash
python scripts/main.py regenerate 1.1 3 --seed 123
```

### **Organizar Imagens Existentes**
```bash
python scripts/main.py organize downloads/
```

### **Ver Log**
```bash
cat assets/imagens-narrar/3-ano/LOG.md
```

---

## 🎯 Dicas de Uso

### **1. Comece Pequeno**
- Teste com 1 imagem primeiro
- Depois teste 1 semana
- Só então gere o ano completo

### **2. Valide Qualidade**
- Abra algumas imagens aleatórias
- Verifique se estilo está consistente
- Confira se prompts estão corretos

### **3. Use Log**
- LOG.md mostra status completo
- Útil para retomar geração interrompida
- Documenta todo o processo

### **4. Faça Backup**
```bash
# Após gerar tudo
cp -r assets/imagens-narrar/3-ano/ backup/imagens-narrar-3-ano/
```

---

## 📞 Suporte

Se encontrar problemas não listados:

1. **Verifique logs:**
   ```bash
   cat test_*.log 2>/dev/null || echo "No logs found"
   ```

2. **Teste conexão:**
   ```bash
   curl -I https://image.pollinations.ai/
   ```

3. **Documentação completa:**
   - [README.md](README.md)
   - [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md)

---

## ✅ Checklist de Sucesso

- [ ] Dependências instaladas
- [ ] Teste de API funcionou
- [ ] Semana de teste gerada
- [ ] Imagens validadas
- [ ] Estrutura de pastas correta
- [ ] LOG.md gerado

**Se tudo marcado:** ✅ **PRONTO PARA PRODUÇÃO!**

---

**Versão:** 1.0.0  
**Última atualização:** 2026-04-01  
**Status:** ✅ Production Ready
