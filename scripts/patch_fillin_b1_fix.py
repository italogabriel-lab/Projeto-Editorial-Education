#!/usr/bin/env python3
"""Patch final dos fill-ins restantes do bimestre 1."""
import os

BASE = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano - Introdução à Linguagem Visual e aos Elementos da Arte"

PATCHES = [
    # 2.1: sentença ok, resposta errada (nos → arte)
    ("2.1.md",
     "A _____ é a beleza criada por Deus nos lugares da vida.\r\n\r\nnos",
     "A _____ é a beleza criada por Deus nos lugares da vida.\r\n\r\narte"),
    # 7.1: sentença antiga ainda presente
    ("7.1.md",
     "_____ organiza linhas fechadas para mostrar figuras no desenho.\r\n\r\nForma",
     "_____ é o espaço fechado por linhas que mostra figuras no desenho.\r\n\r\nForma"),
]

for nome, old, new in PATCHES:
    caminho = os.path.join(BASE, nome)
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    if old in conteudo:
        conteudo = conteudo.replace(old, new)
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print(f"[ok] {nome}")
    else:
        print(f"[miss] {nome}")
