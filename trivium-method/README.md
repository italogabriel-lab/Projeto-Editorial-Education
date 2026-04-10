# Trivium Method

**Biblioteca canônica de métodos, agentes e workflows do TriviumOS**

---

## Visão Geral

O **Trivium Method** é a biblioteca-fonte que organiza agentes, workflows, templates e automações editoriais para o pacote `create-triviumos`.

---

## Estrutura

```text
trivium-method/
├── core/                 # Núcleo do framework
├── agents/               # 20 agentes documentados
├── workflows/            # Workflows editoriais
├── templates/            # Templates de conteúdo
├── knowledge-base/       # Base de conhecimento
└── scripts/              # Scripts de automação
```

---

## Agentes por Categoria

### **Core (6 agentes)**
- Orchestrator → Diagnóstico e delegação
- Researcher → Pesquisa
- Writer → Redação
- Standardizer → Padronização
- Reviewer → Revisão
- Publisher → Publicação

### **Specialized (4 agentes)**
- Copywriter → Polimento
- Design Thinking → UX
- UI Designer → Design System
- DevOps → GitHub/Infra

### **Analytics (4 agentes)**
- Performance Analytics → Métricas
- Vision Progress Engine → Progresso
- Vision Bottleneck Detector → Gargalos
- Vision GitHub Analyzer → Dados

### **Bimester (2 agentes)**
- Bimester Exam Builder → Provas
- Bimester Review Builder → Revisões

### **Legacy (4 agentes)**
- Capitalizer → Capitalização
- Exam Builder → Quizzes (legado)
- Image Link Extractor → Imagens (legado)
- Review Builder → Revisões (legado)

---

## Fluxo Principal

```
Orchestrator → Researcher → Writer → Standardizer → Reviewer → Copywriter → Publisher
   ↓              ↓           ↓           ↓             ↓           ↓            ↓
Diagnóstico   Pesquisa    Redação    Formatação    Revisão    Polimento   Publicação
```

---

## Links

- [Main README](../README.md)
- [Agents](agents/)
- [Workflows](workflows/)
- [Templates](templates/)
- [Knowledge Base](knowledge-base/)

---

**Versão:** 1.0  
**Status:** ✅ Production Ready
