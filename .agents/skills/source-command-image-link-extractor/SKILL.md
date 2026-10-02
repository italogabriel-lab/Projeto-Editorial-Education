---
name: "source-command-image-link-extractor"
description: "Skill legada para extrair e organizar links de imagem usados no habito Perceber."
---

# source-command-image-link-extractor

Use this skill when the user asks to run the migrated source command `image-link-extractor`.

## Command Template

# Skill: Image Link Extractor (Legacy)

## Papel

Voce e um utilitario legado especializado em coletar e normalizar links de imagem para materiais existentes.

## Quando usar

- manutencao de aulas antigas
- atualizacao de listas de imagem sem regenerar todo o fluxo visual

## Preferencia atual

Para fluxos novos, priorize:

- `researcher` para curadoria
- `image-generator` para criacao e organizacao de ativos

## Saida esperada

- lista de links organizada por aula, semana ou tema
- apontamento claro do arquivo de destino

## Regra

1. Trabalhe apenas sobre o habito Perceber.
2. Se o caso pedir geracao de imagem, encaminhe para `image-generator`.

## Curadoria e licenciamento

- Use palavras-chave em inglês e uma busca específica por aula.
- Priorize Getty Collection, Rawpixel Public Domain, National Gallery of Art e Artvee para localizar obras relacionadas ao tema.
- Inclua World History Encyclopedia, PICRYL e PublicDomainPictures como buscas adicionais com palavras-chave em inglês. Verifique a licença e os direitos específicos na página individual.
- Inclua Openverse com filtro `CC0/PDM` e confirme a licença na página individual antes do download.
- Wikimedia Commons é fonte complementar. Na página individual, selecione somente CC0 ou Domínio Público/PDM sem obrigação de atribuição; prefira CC0. Exclua CC BY, CC BY-SA e qualquer condição de crédito ou reutilização. A busca não comprova licença; use o link direto ao item.
- Use Pixabay e Unsplash como complementos, verificando suas licenças próprias.
- Registre internamente título, autor, instituição, licença e URL para rastreabilidade. PDM é informativo, não garantia universal; descarte status ambíguo e verifique possíveis direitos não autorais. Pixabay e Unsplash são complementares, sujeitos à verificação por item.
