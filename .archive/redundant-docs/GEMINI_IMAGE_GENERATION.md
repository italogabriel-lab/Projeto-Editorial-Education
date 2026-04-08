# 🎨 Gemini Image Generation

Geração automática de imagens usando Google Gemini API para o Projeto Editorial Education (Bibline Academy).

## 📋 Pré-requisitos

- Python 3.8+
- Conta Google AI Studio com API Key (conta Pro)
- Dependências instaladas

## 🔧 Configuração

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar API Key

Edite o arquivo `.env` e adicione sua chave API do Gemini:

```env
GEMINI_API_KEY=sua_chave_api_aqui
```

**Como obter a API Key:**
1. Acesse [aistudio.google.com](https://aistudio.google.com)
2. Faça login com sua conta Pro
3. Clique em "Create API Key"
4. Selecione/crie um projeto Google Cloud
5. Copie a chave

## 🚀 Uso

### Gerar imagem da Aula 14.2

```bash
python generate_image.py
```

Ou especificamente:

```bash
python generate_image.py 14.2
```

## 📁 Estrutura de Pastas

As imagens são organizadas por semana e aula **dentro da pasta de cada ano**:

```
3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/
└── Semana 14/
    └── Aula 14.2 - A beleza sem estátuas/
        └── 1-r-image-a.png
```

### Convenção de Nomenclatura

- **Formato:** `1-r-image-a.png`
  - `1` = número da aula
  - `r` = seção "Narrar" (rise block)
  - `image-a` = primeira imagem do bloco

## 🎯 Configurações de Imagem

- **Modelo:** `gemini-2.5-flash-image`
- **Ratio:** 2:1 (formato horizontal)
- **Formato:** PNG
- **Estilo:** Aquarela clássica com fundo branco

## 📊 Limites da API (Free Tier)

| Limite | Valor |
|--------|-------|
| Requests por minuto | 10 |
| Requests por dia | 500 |
| Reset | Meia-noite (Pacific Time) |

## 🔧 Troubleshooting

### Erro: "GEMINI_API_KEY not found"
- Verifique se o arquivo `.env` existe e contém a chave
- Execute: `export GEMINI_API_KEY=sua_chave` (temporário)

### Erro: "RESOURCE_EXHAUSTED"
- Você atingiu o limite de requests
- Aguarde alguns minutos e tente novamente

### Erro: "Missing required packages"
- Execute: `pip install -r requirements.txt`

## 📝 Adicionando Novas Aulas

Para adicionar geração de outra aula:

1. Copie a função `generate_aula_14_2()`
2. Renomeie para `generate_aula_X_Y()`
3. Atualize o prompt e caminho de saída
4. Adicione a chamada no `if __name__ == "__main__"`

## 🎨 Estilo das Imagens

Todas as imagens seguem o padrão:
- Ilustração em aquarela detalhada
- Estilo livro ilustrado clássico
- Fundo branco com bordas difusas
- Textura de papel aquarelado
- Luz quente e dourada
- Paleta: dourado, marfim, azul profundo, vermelho suave, ocre

## 📖 Documentação Relacionada

- [Prompts para Imagens - 3º Ano](../Projeto%20Bibline%20Academy/Belas%20Artes%20-%20Fase%20da%20Gramática/1%20Fase%20-%20Gramática/3º%20Ano%20-%20ARTE%20CRISTÃ%20ORIENTAL%20ATÉ%20O%20RENASCIMENTO%20DO%20NORTE/Estrutura%20Curricular%20-%203º%20ANO/5%20-%20Prompts-para-imagens-narrar-3-ano.md)
- [AI Image Generation Setup](../Projeto%20Bibline%20Academy/setup-playbook/02-integrations/ai-image-generation.md)
