#!/usr/bin/env python3
"""
Reestruturação ontológica das definições do 1º ano — Bimestre 1 (semanas 1-8).
"""

import os
import re

BASE = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano - Introdução à Linguagem Visual e aos Elementos da Arte"

# Mapa completo: semana → dados de substituição
SEMANAS = {
    1: {
        "def_antiga": "Arte expressa a beleza criada por Deus com habilidade humana.",
        "def_nova":   "Arte é a expressão da beleza criada por Deus com habilidade humana.",
        # parágrafos livres por aula (plain / bold)
        "par_x1_plain": "O ser humano faz arte com a habilidade dada por Deus para expressar a beleza.",
        "par_x1_bold":  "O ser humano faz **arte** com a habilidade dada por Deus para expressar a beleza.",
        "par_x1_old_plain": "O ser humano expressa a beleza da criação ao fazer arte com a habilidade humana dada por Deus.",
        "par_x1_old_bold":  "O ser humano **expressa** a **beleza da criação** ao fazer arte com a **habilidade humana** dada por Deus.",
        # fill-ins: [sentença_antiga, sentença_nova]
        "fill": {
            "x1": ("Arte expressa a _____ criada por Deus com habilidade humana.", "_____ é a expressão da beleza criada por Deus com habilidade humana."),
            "x2": ("Arte expressa a _____ criada por Deus com habilidade humana.", "Arte é a expressão da _____ criada por Deus com habilidade humana."),
            "x3": ("Arte expressa a beleza criada por Deus com _____ humana.",      "Arte é a expressão da beleza criada por Deus com _____ humana."),
        },
        "fill_resp": {"x1": ("beleza", "Arte"), "x2": ("beleza", "beleza"), "x3": ("habilidade", "habilidade")},
    },
    2: {
        "def_antiga": "A arte está nos lugares da vida como resposta à beleza criada por Deus.",
        "def_nova":   "A arte é a beleza criada por Deus nos lugares da vida.",
        "par_x1_plain": "A arte é a beleza que a criança observa em casa, na igreja e na natureza.",
        "par_x1_bold":  "A **arte** é a beleza que a criança observa em casa, na igreja e na natureza.",
        "par_x1_old_plain": "O ser humano reconhece arte quando observa beleza em casa, na igreja, nos livros e na natureza.",
        "par_x1_old_bold":  "O ser humano reconhece arte quando observa beleza em casa, na igreja, nos livros e na natureza.",
        "fill": {
            "x1": ("A arte está _____ lugares da vida como resposta à beleza criada por Deus.", "A _____ é a beleza criada por Deus nos lugares da vida."),
            "x2": ("A arte está nos lugares da vida como resposta à _____ criada por Deus.", "A arte é a _____ criada por Deus nos lugares da vida."),
            "x3": ("A arte está nos lugares da vida como resposta à beleza _____ por Deus.", "A arte é a beleza criada por Deus nos _____ da vida."),
        },
        "fill_resp": {"x1": ("nos", "arte"), "x2": ("beleza", "beleza"), "x3": ("criada", "lugares")},
    },
    3: {
        "def_antiga": "O ponto representa o começo de uma obra de arte.",
        "def_nova":   "O ponto é o menor sinal que dá início a uma obra de arte.",
        "par_x1_plain": "Você observa pontos na obra de arte como sinais pequenos que iniciam uma imagem.",
        "par_x1_bold":  "Você observa **pontos** na obra de arte como sinais pequenos que iniciam uma imagem.",
        "par_x1_old_plain": "Você observa pontos na obra de arte e percebe como um pequeno sinal pode começar uma imagem.",
        "par_x1_old_bold":  "Você observa **pontos** na obra de arte e percebe como um pequeno sinal pode começar uma imagem.",
        "fill": {
            "x1": ("O _____ representa o começo de uma obra de arte.", "O _____ é o menor sinal que dá início a uma obra de arte."),
            "x2": ("O ponto representa o _____ de uma obra de arte.", "O ponto é o menor sinal que dá _____ a uma obra de arte."),
            "x3": ("O ponto representa o começo de uma _____.", "O ponto é o menor sinal que dá início a uma _____."),
        },
        "fill_resp": {"x1": ("ponto", "ponto"), "x2": ("começo", "início"), "x3": ("obra de arte", "obra de arte")},
    },
    4: {
        "def_antiga": "Pontilhismo organiza pontos repetidos para criar arte com beleza.",
        "def_nova":   "Pontilhismo é a arte feita com muitos pontos pequenos lado a lado.",
        "par_x1_plain": "O pontilhismo é a arte que nasce quando muitos pontos pequenos se juntam na imagem.",
        "par_x1_bold":  "O **pontilhismo** é a arte que nasce quando muitos pontos pequenos se juntam na imagem.",
        "par_x1_old_plain": "A arte feita com pontilhismo nasce de muitos pontos pequenos lado a lado.",
        "par_x1_old_bold":  "A arte feita com **pontilhismo** nasce de muitos pontos pequenos lado a lado.",
        "fill": {
            "x1": ("Pontilhismo organiza _____ repetidos para criar arte com beleza.", "_____ é a arte feita com muitos pontos pequenos lado a lado."),
            "x2": ("Pontilhismo organiza _____ repetidos para criar arte com beleza.", "Pontilhismo é a arte feita com muitos _____ pequenos lado a lado."),
            "x3": ("Pontilhismo organiza pontos repetidos para criar arte com _____.", "Pontilhismo é a arte feita com muitos pontos pequenos _____ a lado."),
        },
        "fill_resp": {"x1": ("pontos", "Pontilhismo"), "x2": ("pontos", "pontos"), "x3": ("beleza", "lado")},
    },
    5: {
        "def_antiga": "Linha guia o desenho e mostra caminho, forma e direção.",
        "def_nova":   "Linha é o sinal que nasce quando um ponto caminha pelo papel.",
        "par_x1_plain": "A linha é o traço que a criança vê no desenho quando um ponto se move pelo papel.",
        "par_x1_bold":  "A **linha** é o traço que a criança vê no desenho quando um ponto se move pelo papel.",
        "par_x1_old_plain": "A linha nasce quando um ponto caminha pelo papel.",
        "par_x1_old_bold":  "A **linha** nasce quando um ponto caminha pelo papel.",
        "fill": {
            "x1": ("Linha guia o desenho e mostra _____, forma e direção.", "_____ é o sinal que nasce quando um ponto caminha pelo papel."),
            "x2": ("Linha guia o desenho e mostra _____, forma e direção.", "Linha é o sinal que _____ quando um ponto caminha pelo papel."),
            "x3": ("Linha guia o desenho e mostra caminho, _____ e direção.", "Linha é o sinal que nasce quando um ponto caminha pelo _____."),
        },
        "fill_resp": {"x1": ("caminho", "Linha"), "x2": ("caminho", "nasce"), "x3": ("forma", "papel")},
    },
    # Semana 6 já está correta — pular
    7: {
        "def_antiga": "Forma organiza linhas fechadas para mostrar figuras no desenho.",
        "def_nova":   "Forma é o espaço fechado por linhas que mostra figuras no desenho.",
        "par_x1_plain": "A forma é o espaço que nasce quando uma linha fecha um lugar no papel.",
        "par_x1_bold":  "A **forma** é o espaço que nasce quando uma linha fecha um lugar no papel.",
        "par_x1_old_plain": "A forma nasce quando uma linha fecha um espaço no papel.",
        "par_x1_old_bold":  "A **forma** nasce quando uma linha fecha um espaço no papel.",
        "fill": {
            "x1": ("Forma organiza _____ fechadas para mostrar figuras no desenho.", "_____ é o espaço fechado por linhas que mostra figuras no desenho."),
            "x2": ("Forma organiza _____ fechadas para mostrar figuras no desenho.", "Forma é o espaço _____ por linhas que mostra figuras no desenho."),
            "x3": ("Forma organiza linhas fechadas para mostrar _____ no desenho.",  "Forma é o espaço fechado por linhas que mostra _____ no desenho."),
        },
        "fill_resp": {"x1": ("linhas", "Forma"), "x2": ("linhas", "fechado"), "x3": ("figuras", "figuras")},
    },
    8: {
        "def_antiga": "Forma natural mostra figuras da natureza que inspiram imagens na arte.",
        "def_nova":   "Forma natural é a figura criada por Deus na natureza que inspira a arte.",
        "par_x1_plain": "A forma natural é a figura das folhas e dos animais que o artista observa para criar imagens.",
        "par_x1_bold":  "A **forma natural** é a figura das folhas e dos animais que o artista observa para criar imagens.",
        "par_x1_old_plain": "A forma natural aparece nas folhas e nos animais para ajudar o artista a criar imagens belas.",
        "par_x1_old_bold":  "A **forma natural** aparece nas folhas e nos animais para ajudar o artista a criar imagens belas.",
        "fill": {
            "x1": ("Forma natural mostra _____ da natureza que inspiram imagens na arte.", "_____ é a figura criada por Deus na natureza que inspira a arte."),
            "x2": ("Forma natural mostra _____ da natureza que inspiram imagens na arte.", "Forma natural é a figura criada por Deus na _____ que inspira a arte."),
            "x3": ("Forma natural mostra figuras da natureza que inspiram imagens na _____.", "Forma natural é a figura criada por Deus na natureza que _____ a arte."),
        },
        "fill_resp": {"x1": ("figuras", "Forma natural"), "x2": ("figuras", "natureza"), "x3": ("arte", "inspira")},
    },
}


def substituir_fill(conteudo, old_sent, new_sent, old_resp, new_resp):
    """Substitui sentença do fill-in e opcionalmente a resposta."""
    # Substitui a sentença
    conteudo = conteudo.replace(old_sent, new_sent)
    # Substitui a resposta se mudou
    if old_resp != new_resp:
        # Busca a resposta logo após o fill-in (linha isolada após sentença)
        padrao = re.compile(
            r'(\[+FILL_IN\]\s+' + re.escape(new_sent) + r'\s+)' + re.escape(old_resp) + r'(\s+\[-FILL_IN\])',
            re.DOTALL
        )
        conteudo = padrao.sub(r'\g<1>' + new_resp + r'\g<2>', conteudo)
    return conteudo


def processar_arquivo(caminho, semana_data, numero_aula):
    """Processa um arquivo de aula aplicando as substituições."""
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    d = semana_data
    old_def = d["def_antiga"]
    new_def = d["def_nova"]

    # 1. Substituição direta da definição curta em todo o arquivo
    conteudo = conteudo.replace(old_def, new_def)
    conteudo = conteudo.replace(f"**{old_def}**", f"**{new_def}**")

    # 2. Para x.1: atualizar parágrafo livre
    if numero_aula == 1:
        conteudo = conteudo.replace(d["par_x1_old_plain"], d["par_x1_plain"])
        conteudo = conteudo.replace(d["par_x1_old_bold"],  d["par_x1_bold"])

    # 3. Atualizar fill-in
    aula_key = f"x{numero_aula}"
    if aula_key in d["fill"]:
        old_fill, new_fill = d["fill"][aula_key]
        old_resp, new_resp = d["fill_resp"][aula_key]
        conteudo = substituir_fill(conteudo, old_fill, new_fill, old_resp, new_resp)

    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(conteudo)

    return True


def main():
    alterados = []
    erros = []

    for semana, dados in SEMANAS.items():
        # Processar x.1, x.2, x.3, x.4, x.5
        for aula in [1, 2, 3, 4, 5]:
            if aula <= 3:
                nome = f"{semana}.{aula}.md"
            elif aula == 4:
                nome = f"{semana}.4.md"
            else:
                nome = f"{semana}.5.md"

            caminho = os.path.join(BASE, nome)
            if not os.path.exists(caminho):
                print(f"  [skip] {nome} não encontrado")
                continue

            try:
                processar_arquivo(caminho, dados, aula)
                print(f"  [ok] {nome}")
                alterados.append(nome)
            except Exception as e:
                print(f"  [erro] {nome}: {e}")
                erros.append((nome, str(e)))

    print(f"\nTotal alterados: {len(alterados)}")
    print(f"Total erros: {len(erros)}")
    if erros:
        for nome, msg in erros:
            print(f"  ERRO {nome}: {msg}")


if __name__ == "__main__":
    main()
