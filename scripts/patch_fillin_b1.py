#!/usr/bin/env python3
"""
Patch fill-ins dos x.1 do bimestre 1 — substitui direto por conteúdo exato.
"""
import os

BASE = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano - Introdução à Linguagem Visual e aos Elementos da Arte"

# Cada entrada: (arquivo, bloco_antigo, bloco_novo)
PATCHES = [
    # Semana 1 — x.1
    ("1.1.md",
     "[+FILL_IN]\n\nArte _____ a beleza criada por Deus com habilidade humana.\n\nexpressa\n\n[-FILL_IN]",
     "[+FILL_IN]\n\n_____ é a expressão da beleza criada por Deus com habilidade humana.\n\nArte\n\n[-FILL_IN]"),
    # Semana 2 — x.1
    ("2.1.md",
     "[+FILL_IN]\n\nA arte está _____ lugares da vida como resposta à beleza criada por Deus.\n\nnos\n\n[-FILL_IN]",
     "[+FILL_IN]\n\nA _____ é a beleza criada por Deus nos lugares da vida.\n\narte\n\n[-FILL_IN]"),
    # Semana 3 — x.1
    ("3.1.md",
     "[+FILL_IN]\n\nO _____ representa o começo de uma obra de arte.\n\nponto\n\n[-FILL_IN]",
     "[+FILL_IN]\n\nO _____ é o menor sinal que dá início a uma obra de arte.\n\nponto\n\n[-FILL_IN]"),
    # Semana 3 — x.2 (resposta desatualizada: começo → início)
    ("3.2.md",
     "[+FILL_IN]\n\nO ponto é o menor sinal que dá _____ a uma obra de arte.\n\ncomeço\n\n[-FILL_IN]",
     "[+FILL_IN]\n\nO ponto é o menor sinal que dá _____ a uma obra de arte.\n\ninício\n\n[-FILL_IN]"),
    # Semana 4 — x.1
    ("4.1.md",
     "[+FILL_IN]\n\n_____ organiza pontos repetidos para criar arte com beleza.\n\nPontilhismo\n\n[-FILL_IN]",
     "[+FILL_IN]\n\n_____ é a arte feita com muitos pontos pequenos lado a lado.\n\nPontilhismo\n\n[-FILL_IN]"),
    # Semana 5 — x.1
    ("5.1.md",
     "[+FILL_IN]\n\n_____ guia o desenho e mostra caminho, forma e direção.\n\nLinha\n\n[-FILL_IN]",
     "[+FILL_IN]\n\n_____ é o sinal que nasce quando um ponto caminha pelo papel.\n\nLinha\n\n[-FILL_IN]"),
    # Semana 7 — x.1
    ("7.1.md",
     "[+FILL_IN]\n\nForma organiza _____ fechadas para mostrar figuras no desenho.\n\nlinhas\n\n[-FILL_IN]",
     "[+FILL_IN]\n\n_____ é o espaço fechado por linhas que mostra figuras no desenho.\n\nForma\n\n[-FILL_IN]"),
    # Semana 8 — x.1
    ("8.1.md",
     "[+FILL_IN]\n\nForma _____ mostra figuras da natureza que inspiram imagens na arte.\n\nnatural\n\n[-FILL_IN]",
     "[+FILL_IN]\n\n_____ é a figura criada por Deus na natureza que inspira a arte.\n\nForma natural\n\n[-FILL_IN]"),
]

# Patches CRLF — os arquivos têm \r\n
def normalizar(s):
    return s.replace('\n', '\r\n')

for nome, bloco_old, bloco_new in PATCHES:
    caminho = os.path.join(BASE, nome)
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    old_crlf = normalizar(bloco_old)
    new_crlf = normalizar(bloco_new)

    if old_crlf in conteudo:
        conteudo = conteudo.replace(old_crlf, new_crlf)
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print(f"[ok] {nome}")
    elif bloco_old in conteudo:
        conteudo = conteudo.replace(bloco_old, bloco_new)
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print(f"[ok-lf] {nome}")
    else:
        print(f"[miss] {nome} — padrão não encontrado")
