#!/usr/bin/env python3
"""
patch_semanas_11_38.py
Aplica o novo padrão editorial às semanas 11–38 do 1º ano de Belas Artes.

Correções:
1. Capitalização do termo central no meio de frases → sentence-case (minúsculo).
2. Frase genérica do Perceber → frase específica por aula.
3. Frase genérica do Perceber nas revisões .4 → frase contextualizada ao tema.
"""

import os
import re

BASE = (
    "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/"
    "Projeto - Bibline Academy ( Produção de Aulas)/"
    "Belas Artes - Fase da Gramática/1 Fase - Gramática/"
    "1º Ano - Introdução à Linguagem Visual e aos Elementos da Arte"
)

# ─── FRASES DO PERCEBER POR AULA ─────────────────────────────────────────────
# Cada chave: nome do arquivo sem extensão. Valor: frase específica para o Perceber.
PERCEBER_FRASES = {
    # ── Semana 11 ──
    "11.1": "Observe as três cores primárias e veja como cada uma inicia o ciclo das cores.",
    "11.2": "Observe o vermelho, o azul e o amarelo e veja como eles iniciam misturas de novas cores.",
    "11.3": "Observe as cores que nascem quando duas cores primárias se combinam na mistura.",
    # ── Semana 12 ──
    "12.1": "Observe as cores expressivas e veja como cada escolha mostra sentimentos com beleza e ordem.",
    "12.2": "Observe como as cores comunicam sentimentos diferentes conforme a escolha do artista.",
    "12.3": "Observe as cores quentes e frias e veja como cada grupo mostra sentimentos com beleza.",
    # ── Semana 13 ──
    "13.1": "Observe a cor musical e veja como ela une escuta e observação ao conectar som e cor.",
    "13.2": "Observe como a cor acompanha o som e transforma a escuta em gesto e cor no papel.",
    "13.3": "Observe como a cor expressa sentimento quando nasce do que a música provoca.",
    # ── Semana 14 ──
    "14.1": "Observe como a luz muda as cores do dia e da noite ao iluminar a criação com beleza.",
    "14.2": "Observe as cores da luz do sol e veja como elas revelam tons diferentes durante o dia.",
    "14.3": "Observe as cores da noite com tons escuros e suaves que cobrem a criação.",
    # ── Semana 15 ──
    "15.1": "Observe a textura na arte e veja como a superfície parece diferente ao toque e à vista.",
    "15.2": "Observe a diferença entre superfícies lisas e ásperas e veja como cada uma aparece na arte.",
    "15.3": "Observe a textura da areia e das folhas e veja os padrões marcados que cada material deixa.",
    # ── Semana 16 ──
    "16.1": "Observe a textura expressiva e veja como marcas e materiais comunicam sentimento na arte.",
    "16.2": "Observe a textura feita com massa e veja as marcas espessas e com volume que ela cria.",
    "16.3": "Observe a textura feita com materiais naturais e veja as marcas únicas que eles deixam no papel.",
    # ── Semana 17 ──
    "17.1": "Observe como o espaço organiza o papel em fundo, borda e centro para que cada parte tenha lugar.",
    "17.2": "Observe como o fundo aparece atrás das figuras e a borda aparece ao redor do papel.",
    "17.3": "Observe como o centro ajuda a colocar o elemento principal no meio do papel.",
    # ── Semana 18 ──
    "18.1": "Observe como o tamanho mostra formas grandes e pequenas dentro da obra de arte.",
    "18.2": "Observe como formas grandes e pequenas aparecem juntas na mesma obra.",
    "18.3": "Observe como uma forma maior pode chamar atenção dentro da obra de arte.",
    # ── Semana 21 ──
    "21.1": "Observe como a direção guia o olhar e mostra para onde a história da imagem se move.",
    "21.2": "Observe como setas e linhas guiam o olhar e mostram para onde olhar primeiro na imagem.",
    "21.3": "Observe o caminho feito com pincel e veja como ele conduz a história pelos olhos.",
    # ── Semana 22 ──
    "22.1": "Observe como o equilíbrio organiza partes diferentes para que a obra fique firme e bela.",
    "22.2": "Observe como a dobradura cria equilíbrio ao repetir formas simétricas dos dois lados.",
    "22.3": "Observe a simetria e veja como as formas espelhadas deixam a obra equilibrada e firme.",
    # ── Semana 23 ──
    "23.1": "Observe a composição e veja como ela une todos os elementos visuais em uma obra com ordem.",
    "23.2": "Observe o quadro com formas e cores e veja como a composição cria equilíbrio e harmonia.",
    "23.3": "Observe como ponto, linha e espaço trabalham juntos para criar uma obra com ordem e sentido.",
    # ── Semana 24 ──
    "24.1": "Observe como as formas simples ajudam o desenho a nascer com clareza e organização.",
    "24.2": "Observe como o círculo se transforma em cabeça, olho ou corpo para criar um personagem.",
    "24.3": "Observe como o triângulo e o quadrado se unem para criar a forma de uma casa no papel.",
    # ── Semana 25 ──
    "25.1": "Observe como formas simples se transformam em personagens com expressão e vida.",
    "25.2": "Observe como o círculo ganha rosto, corpo e movimento para virar um personagem como o sol.",
    "25.3": "Observe o bicho inventado e veja como forma, cor e traço únicos dão expressão ao ser criado.",
    # ── Semana 26 ──
    "26.1": "Observe como o mundo desenhado mostra lugares queridos com ordem, beleza e cuidado no papel.",
    "26.2": "Observe como a casa aparece no desenho com lugares queridos retratados com carinho.",
    "26.3": "Observe como o cantinho favorito é desenhado com beleza e cuidado para expressar gratidão.",
    # ── Semana 27 ──
    "27.1": "Observe como os lugares e histórias aparecem com formas e cores que revelam a identidade do lugar.",
    "27.2": "Observe as formas verticais e horizontais que retratam a Igreja com torres e arcos.",
    "27.3": "Observe as cores vivas do parquinho colorido e veja como elas mostram alegria e brincadeira.",
    # ── Semana 28 ──
    "28.1": "Observe como a história inspira imagens que ajudam a criança a lembrar fatos importantes com beleza.",
    "28.2": "Observe a imagem da arca e dos animais de Noé e veja os detalhes visuais que a história revela.",
    "28.3": "Observe como o jardim da criação se transforma em imagem para lembrar fatos importantes.",
    # ── Semana 31 ──
    "31.1": 'Observe como a composição organiza linhas, formas e cores na arte.',
    "31.2": 'Observe como o equilíbrio distribui os elementos visuais na imagem.',
    "31.3": 'Observe como a ordem coloca cada parte no lugar certo da página.',
    # ── Semana 32 ──
    "32.1": 'Observe luz, céus e águas como formas visuais da criação.',
    "32.2": 'Observe como a luz nasce e separa a claridade das trevas.',
    "32.3": 'Observe o brilho do céu nas cores claras e luminosas.',
    # ── Semana 33 ──
    "33.1": 'Observe terra, céu e seres vivos em uma cena ordenada.',
    "33.2": 'Observe como terra e céu formam o lugar dos seres vivos.',
    "33.3": 'Observe o movimento dos peixes, aves e animais desenhados.',
    # ── Semana 34 ──
    "34.1": 'Observe animais, homem e criação como obra completa de Deus.',
    "34.2": 'Observe o homem diante da obra criada com cuidado e gratidão.',
    "34.3": 'Observe a paz em uma imagem da obra completa de Deus.',
    # ── Semana 35 ──
    "35.1": 'Observe como som, cor e movimento aparecem juntos na arte.',
    "35.2": 'Observe como o som inspira escolhas de cor e traço.',
    "35.3": 'Observe como a música vira imagem com formas e cores.',
    # ── Semana 36 ──
    "36.1": 'Observe cores e formas que a música desperta na imaginação.',
    "36.2": 'Observe o som transformado em traços e cores no papel.',
    "36.3": 'Observe o movimento da mão acompanhando a música no papel.',
    # ── Semana 37 ──
    "37.1": 'Observe como uma obra de arte encanta o olhar com beleza.',
    "37.2": 'Observe como a forma aparece em linhas e cores belas.',
    "37.3": 'Observe como a beleza da obra prende o olhar com atenção.',
    # ── Semana 38 ──
    "38.1": 'Observe detalhes da obra com atenção e gratidão.',
    "38.2": 'Observe como o olhar atento encontra detalhes pequenos no quadro.',
    "38.3": 'Observe a beleza visível em cores, formas e detalhes.',
}

# ─── FRASES DO PERCEBER PARA AS REVISÕES .4 ─────────────────────────────────
PERCEBER_REVISOES = {
    "11.4": "Observe as imagens da semana e veja como as cores primárias iniciam misturas com beleza.",
    "12.4": "Observe as imagens da semana e veja como as cores expressivas mostram sentimentos com beleza.",
    "13.4": "Observe as imagens da semana e veja como a cor musical acompanha o som na arte.",
    "14.4": "Observe as imagens da semana e veja como a luz muda as cores do dia e da noite.",
    "15.4": "Observe as imagens da semana e veja como a textura mostra diferentes superfícies na arte.",
    "16.4": "Observe as imagens da semana e veja como a textura expressiva comunica sentimento na arte.",
    "17.4": "Observe as imagens da semana e veja como o espaço organiza fundo, borda e centro no papel.",
    "18.4": "Observe as imagens da semana e veja como o tamanho mostra formas grandes, pequenas e formas que chamam atenção.",
    "21.4": "Observe as imagens da semana e veja como a direção guia o olhar nas imagens.",
    "22.4": "Observe as imagens da semana e veja como o equilíbrio organiza cada obra com firmeza.",
    "23.4": "Observe as imagens da semana e veja como a composição une os elementos com ordem e beleza.",
    "24.4": "Observe as imagens da semana e veja como as formas simples criam desenhos com clareza.",
    "25.4": "Observe as imagens da semana e veja como os personagens ganham expressão e vida.",
    "26.4": "Observe as imagens da semana e veja como o mundo desenhado mostra lugares com beleza e cuidado.",
    "27.4": "Observe as imagens da semana e veja como o lugar desenhado revela espaços com formas e cores.",
    "28.4": "Observe as imagens da semana e veja como a história inspira imagens com beleza e detalhes.",
    "31.4": 'Observe as imagens da semana e veja como a composição organiza equilíbrio e ordem na arte.',
    "32.4": 'Observe as imagens da semana e veja como a criação mostra luz e brilho no céu.',
    "33.4": 'Observe as imagens da semana e veja como a vida criada une terra, céu e movimento.',
    "34.4": 'Observe as imagens da semana e veja como o descanso mostra obra completa e paz.',
    "35.4": 'Observe as imagens da semana e veja como arte e música unem som, cor e imagem.',
    "36.4": 'Observe as imagens da semana e veja como a imagem musical transforma som em movimento.',
    "37.4": 'Observe as imagens da semana e veja como o encanto aparece em forma, cor e obra.',
    "38.4": 'Observe as imagens da semana e veja como a observação encontra beleza nos detalhes.',
}

# ─── TERMOS COM CAPITALIZAÇÃO INCORRETA ──────────────────────────────────────
# Mapeamento: (texto com maiúscula errada) → (texto correto com sentence-case)
# Padrão: quando aparece após artigo (A, O, As, Os, Uma, Um) antes de ** ou espaço
CAPITALIZACOES = [
    # Semana 11
    ("A **Cor primária**",          "A **cor primária**"),
    ("A Cor primária",              "A cor primária"),
    # Semana 12
    ("A **Cor expressiva**",        "A **cor expressiva**"),
    ("A Cor expressiva",            "A cor expressiva"),
    # Semana 13
    ("A **Cor musical**",           "A **cor musical**"),
    ("A Cor musical",               "A cor musical"),
    # Semana 14
    ("A **Luz**",                   "A **luz**"),
    ("A Luz",                       "A luz"),
    # Semana 15
    ("A **Textura**",               "A **textura**"),
    ("A Textura",                   "A textura"),
    # Semana 16
    ("A **Textura expressiva**",    "A **textura expressiva**"),
    ("A Textura expressiva",        "A textura expressiva"),
    # Semana 17
    ("O **Espaço**",                "O **espaço**"),
    ("O Espaço",                    "O espaço"),
    # Semana 18
    ("O **Tamanho**",               "O **tamanho**"),
    ("O Tamanho",                   "O tamanho"),
    # Semana 21
    ("A **Direção**",               "A **direção**"),
    ("A Direção",                   "A direção"),
    # Semana 22
    ("O **Equilíbrio**",            "O **equilíbrio**"),
    ("O Equilíbrio",                "O equilíbrio"),
    # Semana 23
    ("A **Composição**",            "A **composição**"),
    ("A Composição",                "A composição"),
    # Semana 24
    ("A **Forma simples**",         "A **forma simples**"),
    ("A Forma simples",             "A forma simples"),
    # Semana 25
    ("O **Personagem**",            "O **personagem**"),
    ("O Personagem",                "O personagem"),
    # Semana 26
    ("O **Mundo desenhado**",       "O **mundo desenhado**"),
    ("O Mundo desenhado",           "O mundo desenhado"),
    # Semana 27
    ("O **Lugar desenhado**",       "O **lugar desenhado**"),
    ("O Lugar desenhado",           "O lugar desenhado"),
    # Semana 28
    ("A **História**",              "A **história**"),
    ("A História",                  "A história"),
    # Semana 31
    ("A **Esperança**",             "A **esperança**"),
    ("A Esperança",                 "A esperança"),
    # Semana 32
    ("A **Criação**",               "A **criação**"),
    ("A Criação",                   "A criação"),
    # Semana 33
    ("A **Vida criada**",           "A **vida criada**"),
    ("A Vida criada",               "A vida criada"),
    # Semana 34
    ("O **Descanso**",              "O **descanso**"),
    ("O Descanso",                  "O descanso"),
    # Semana 35
    ("A **Arte e música**",         "A **arte e música**"),
    ("A Arte e música",             "A arte e música"),
    # Semana 36
    ("A **Imagem musical**",        "A **imagem musical**"),
    ("A Imagem musical",            "A imagem musical"),
    # Semana 37
    ("O **Encanto**",               "O **encanto**"),
    ("O Encanto",                   "O encanto"),
    # Semana 38
    ("A **Observação**",            "A **observação**"),
    ("A Observação",                "A observação"),
]

# Frase genérica do Perceber nas aulas regulares (para identificar e substituir)
FRASE_GENERICA_PADRAO = re.compile(
    r"(Observe\s+.+?\s+e\s+veja\s+como\s+isso\s+ajuda\s+a\s+imagem\.)"
)

# Frase genérica do Perceber nas revisões .4
FRASE_GENERICA_REVISAO = "Observe as imagens que estudamos durante a semana."


def aplicar_capitalizacao(texto):
    """Aplica correções de capitalização sentence-case ao texto."""
    for errado, correto in CAPITALIZACOES:
        texto = texto.replace(errado, correto)
    return texto


def corrigir_perceber_aula(conteudo, nome_arquivo):
    """Substitui a frase genérica do Perceber pela frase específica da aula."""
    chave = nome_arquivo.replace(".md", "")
    if chave not in PERCEBER_FRASES:
        return conteudo
    frase_nova = PERCEBER_FRASES[chave]
    conteudo = FRASE_GENERICA_PADRAO.sub(frase_nova, conteudo)
    return conteudo


def corrigir_perceber_revisao(conteudo, nome_arquivo):
    """Substitui a frase genérica do Perceber nas revisões .4."""
    chave = nome_arquivo.replace(".md", "")
    if chave not in PERCEBER_REVISOES:
        return conteudo
    frase_nova = PERCEBER_REVISOES[chave]
    conteudo = conteudo.replace(FRASE_GENERICA_REVISAO, frase_nova)
    return conteudo


def processar_arquivo(caminho_arquivo):
    nome = os.path.basename(caminho_arquivo)
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        original = f.read()

    modificado = original

    # 1. Corrigir capitalização
    modificado = aplicar_capitalizacao(modificado)

    # 2. Corrigir frase do Perceber
    if nome.endswith(".4.md"):
        modificado = corrigir_perceber_revisao(modificado, nome)
    elif any(nome.endswith(f"{s}.md") for s in [".1", ".2", ".3"]):
        modificado = corrigir_perceber_aula(modificado, nome)

    if modificado != original:
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(modificado)
        return True
    return False


def main():
    # Lista de todos os arquivos a processar (semanas 11–38, exceto bimestrais)
    semanas = [11, 12, 13, 14, 15, 16, 17, 18,
               21, 22, 23, 24, 25, 26, 27, 28,
               31, 32, 33, 34, 35, 36, 37, 38]

    total = 0
    modificados = 0
    erros = []

    for semana in semanas:
        # Aulas .1, .2, .3
        for aula in [1, 2, 3]:
            nome = f"{semana}.{aula}.md"
            caminho = os.path.join(BASE, nome)
            if os.path.exists(caminho):
                total += 1
                try:
                    if processar_arquivo(caminho):
                        modificados += 1
                        print(f"  ✔ {nome}")
                    else:
                        print(f"  · {nome} (sem alterações)")
                except Exception as e:
                    erros.append((nome, str(e)))
                    print(f"  ✗ {nome}: {e}")
            else:
                print(f"  ! {nome} não encontrado")

        # Revisão semanal .4
        nome4 = f"{semana}.4.md"
        caminho4 = os.path.join(BASE, nome4)
        if os.path.exists(caminho4):
            total += 1
            try:
                if processar_arquivo(caminho4):
                    modificados += 1
                    print(f"  ✔ {nome4}")
                else:
                    print(f"  · {nome4} (sem alterações)")
            except Exception as e:
                erros.append((nome4, str(e)))
                print(f"  ✗ {nome4}: {e}")

        # Prova semanal .5 — apenas capitalização
        nome5 = f"{semana}.5.md"
        caminho5 = os.path.join(BASE, nome5)
        if os.path.exists(caminho5):
            total += 1
            try:
                if processar_arquivo(caminho5):
                    modificados += 1
                    print(f"  ✔ {nome5}")
                else:
                    print(f"  · {nome5} (sem alterações)")
            except Exception as e:
                erros.append((nome5, str(e)))
                print(f"  ✗ {nome5}: {e}")

    # Revisões bimestrais
    for bim in ["19.md", "29.md", "39.md"]:
        caminho = os.path.join(BASE, bim)
        if os.path.exists(caminho):
            total += 1
            try:
                if processar_arquivo(caminho):
                    modificados += 1
                    print(f"  ✔ {bim}")
                else:
                    print(f"  · {bim} (sem alterações)")
            except Exception as e:
                erros.append((bim, str(e)))
                print(f"  ✗ {bim}: {e}")

    print(f"\n{'='*50}")
    print(f"Total: {total} arquivos | Modificados: {modificados} | Erros: {len(erros)}")
    if erros:
        print("Erros:")
        for nome, msg in erros:
            print(f"  {nome}: {msg}")


if __name__ == "__main__":
    main()
