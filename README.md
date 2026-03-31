# 📊 Vision Board - Bibline Academy

**Visão Geral do Projeto**
O **Vision Board de Produção Educacional** é uma solução de inteligência de nível SaaS que transforma o Kanban bruto do GitHub Projects em um Dashboard analítico e preditivo.

## Objetivo do Sistema
Extrair métricas, predizer gargalos, monitorar SLAs do time de escritores e calcular de forma automática e visual se o projeto será entregue dentro do cronograma anual do Currículo Escolar.

## Público-Alvo
- **Diretor Editorial:** Visão estratégica de andamento.
- **Gestores Executivos:** Medir vazão e capacidade do time.
- **Autores & Revisores:** Acompanhamento de fila e pendências individuais.

## 🔗 Live Demo
Acesse o Dashboard em Tempo Real:
👉 **[Abrir Vision Board](https://italogabriel-lab.github.io/Projeto-Editorial-Education/)**

## Como Rodar Localmente
1. Certifique-se de ter o `node` >= 18 e o GitHub CLI `gh` ou Token de API configurado em `Projeto Bibline Academy/.env`.
2. Para gerar os dados locais:
   ```bash
   node src/sync.js
   ```
3. Para visualizar a interface:
   ```bash
   python3 -m http.server 3000
   ```
   Acesse: `http://localhost:3000`

## Estrutura do Projeto
```text
/docs        → PRD, Roadmap, Documentação Técnica, LLMs e Opencode
/llms        → Documentação completa de LLMs (GLM, OpenRouter, Groq)
/src         → Backend Serverless em Node.js (`sync.js`)
/public      → Assets estáticos (`app.js`, `styles.css`, `data.json`)
/assets      → Recursos visuais
index.html   → Interface HTML baseada em Glassmorphism
.github/     → Rotinas CI/CD de sincronização (cada 5m)
```

## Documentação de LLMs e Opencode

A documentação completa das LLMs configuradas está em: [docs/llms/](docs/llms/)

### Principais Documentos:
- **[README.md](docs/llms/README.md)** - Índice geral de LLMs
- **[glm-config.md](docs/llms/glm-config.md)** - Configuração detalhada do GLM
- **[llms.md](docs/llms/llms.md)** - Documentação de todos os provedores

### Provedores Configurados:
- ✅ **GLM (Zhipu AI)** - Modelo padrão: z-ai/glm-4.7-flash
- ✅ OpenRouter - Multi-model routing
- ✅ Groq - Inferência rápida

### Comandos Úteis:
```bash
# Ver provedores configurados
opencode providers list

# Ver estatísticas de uso
opencode stats

# Usar GLM automaticamente
opencode run "Minha tarefa"
```
