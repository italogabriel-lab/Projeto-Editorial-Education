#!/usr/bin/env python3
"""Gera o 4º bimestre do 3º ano no padrão editorial vigente."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).parent))
from generate_lessons import gerar_aula, gerar_revisao

DESTINO = ROOT / "Projeto - Bibline Academy ( Produção de Aulas)" / "Belas Artes - Fase da Gramática" / "1 Fase - Gramática" / "3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE" / "Aulas"


def aula(titulo, paragrafo, negritos, perceber, legenda, fill, resposta, pergunta, correta, instrucao, perguntas):
    paragrafo = paragrafo.replace("**", "")
    return {
        "titulo": titulo,
        "accordion_titulo": titulo,
        "paragrafo_plain": paragrafo,
        "palavras_negrito": negritos,
        "perceber_frase": perceber,
        "perceber_hotspot_coords": "49 50",
        "perceber_hotspot_legenda": legenda,
        "fill_in_frase": fill,
        "fill_in_resposta": resposta,
        "multiple_pergunta": pergunta,
        "multiple_resposta_correta": correta,
        "multiple_distratores": ["Apenas formas sem observação.", "Uma imagem sem ordem visual."],
        "atividade_instrucao": instrucao,
        "narrar_pergunta": perguntas[0],
        "narrar_perguntas": perguntas,
    }


SEMANAS = [
    {
        "numero": 31,
        "definicao_curta": "O Renascimento do Norte é arte europeia de detalhe e luz.",
        "conexao_teologica": "Deus cria pessoas e lugares diversos, e a arte pode observar essa diversidade com verdade e gratidão.",
        "aulas": [
            aula("O Renascimento do Norte", "O **Renascimento do Norte** reúne **detalhe** e luz em imagens observadas com cuidado.", ["Renascimento do Norte"], "Observe a pintura e encontre detalhes iluminados com cuidado.", "Detalhes iluminados", "O _____ é arte europeia de detalhe e luz.", "Renascimento do Norte", "O que é o Renascimento do Norte?", "Arte europeia de detalhe e luz.", "Desenhe uma cena simples com três detalhes visíveis e uma área de luz.", ["O que é o Renascimento do Norte?", "O que o Renascimento do Norte reúne nas imagens?", "O que a arte pode observar com verdade e gratidão?"]),
            aula("Cidades comerciais, oficinas e pintura flamenga", "O **Renascimento do Norte** cresce em **oficinas** que pintam detalhes para cidades comerciais.", ["Renascimento do Norte", "oficinas"], "Observe a oficina e veja os artistas preparando uma pintura flamenga.", "Oficina de pintura", "O Renascimento do Norte é arte europeia de _____ e luz.", "detalhe", "Onde artistas produziam pinturas flamengas?", "Em oficinas das cidades comerciais.", "Desenhe uma oficina com mesa, pincéis e uma pequena pintura com detalhes.", ["O que é o Renascimento do Norte?", "Onde artistas produziam pinturas flamengas?", "Quais lugares Deus cria com diversidade?"]),
            aula("O Norte europeu e o Renascimento italiano", "O **Renascimento do Norte** usa **luz** e detalhe de modo diferente da arte italiana.", ["Renascimento do Norte", "luz"], "Observe duas pinturas e compare a luz do Norte com a composição italiana.", "Luz e detalhe", "O Renascimento do Norte é arte europeia de detalhe e _____.", "luz", "Como o Renascimento do Norte aparece nas pinturas?", "Com detalhe e luz.", "Divida a folha em duas partes e desenhe uma cena com detalhe e outra com composição equilibrada.", ["O que é o Renascimento do Norte?", "Como ele aparece nas pinturas?", "Como a arte pode observar a diversidade criada por Deus?"]),
        ],
    },
    {
        "numero": 32,
        "definicao_curta": "A pintura a óleo é cor misturada com óleo.",
        "conexao_teologica": "Deus criou a luz e as cores, e o artista observa seus efeitos com cuidado.",
        "aulas": [
            aula("A pintura a óleo flamenga", "A **pintura a óleo** mistura cor e óleo para mostrar luz com profundidade.", ["pintura a óleo"], "Observe a pintura flamenga e veja cores profundas na superfície.", "Cores profundas", "A pintura a _____ é cor misturada com óleo.", "óleo", "O que é a pintura a óleo?", "Cor misturada com óleo.", "Pinte uma faixa de cores claras e escuras para mostrar profundidade.", ["O que é a pintura a óleo?", "O que a pintura a óleo mistura?", "Quem criou a luz e as cores?"]),
            aula("Camadas transparentes, cor e luz", "A **pintura a óleo** usa **camadas** transparentes para tornar cor e luz mais profundas.", ["pintura a óleo", "camadas"], "Observe as camadas de cor que fazem a luz parecer brilhante.", "Camadas de luz", "A pintura a óleo é _____ misturada com óleo.", "cor", "O que as camadas transparentes tornam mais profundas?", "A cor e a luz.", "Sobreponha lápis de cor em três camadas para formar uma área de luz.", ["O que é a pintura a óleo?", "O que as camadas transparentes tornam mais profundas?", "Quais efeitos o artista observa com cuidado?"]),
            aula("Texturas e detalhes na pintura sobre madeira", "A **pintura a óleo** mostra **texturas** e detalhes sobre a madeira com cor cuidadosa.", ["pintura a óleo", "texturas"], "Observe a superfície e encontre tecido, madeira e metal pintados com textura.", "Texturas pintadas", "A pintura a óleo é cor misturada com _____.", "óleo", "O que a pintura a óleo mostra sobre a madeira?", "Texturas e detalhes.", "Desenhe três pequenos quadrados com textura de madeira, tecido e metal.", ["O que é a pintura a óleo?", "O que ela mostra sobre a madeira?", "O que Deus criou para o artista observar?"]),
        ],
    },
    {
        "numero": 33,
        "definicao_curta": "O detalhe simbólico é imagem pequena que comunica um significado.",
        "conexao_teologica": "Deus conhece cada detalhe de sua criação, e as imagens podem apontar para significados visíveis.",
        "aulas": [
            aula("Jan van Eyck e o detalhe simbólico", "O **detalhe simbólico** em Jan van Eyck usa objetos pequenos para comunicar significado.", ["detalhe simbólico"], "Observe objetos pequenos que recebem luz na pintura de Jan van Eyck.", "Objeto com significado", "O _____ é imagem pequena que comunica um significado.", "detalhe simbólico", "O que é o detalhe simbólico?", "Imagem pequena que comunica um significado.", "Desenhe um objeto pequeno e acrescente um detalhe que ajude a comunicar uma ideia.", ["O que é o detalhe simbólico?", "Como Jan van Eyck usa objetos pequenos?", "Quem conhece cada detalhe da criação?"]),
            aula("O Casal Arnolfini e o retrato", "O **detalhe simbólico** aparece no **retrato** do Casal Arnolfini por meio de objetos observados.", ["detalhe simbólico", "retrato"], "Observe o retrato e localize objetos pequenos perto das figuras.", "Objetos do retrato", "O detalhe simbólico é imagem _____ que comunica um significado.", "pequena", "Onde o detalhe simbólico aparece no Casal Arnolfini?", "Em objetos pequenos do retrato.", "Desenhe duas figuras e acrescente um objeto pequeno entre elas.", ["O que é o detalhe simbólico?", "Onde ele aparece no Casal Arnolfini?", "Para que as imagens podem apontar?"]),
            aula("Objetos, espelho e luz na pintura flamenga", "O **detalhe simbólico** usa **espelho** e luz para tornar objetos pequenos visíveis.", ["detalhe simbólico", "espelho"], "Observe o espelho e a luz refletida entre os objetos da pintura.", "Espelho e luz", "O detalhe simbólico é imagem pequena que comunica um _____.", "significado", "O que o espelho e a luz tornam visíveis?", "Objetos pequenos.", "Desenhe um espelho circular e mostre nele o reflexo de um objeto.", ["O que é o detalhe simbólico?", "O que o espelho e a luz tornam visíveis?", "Que detalhes Deus conhece em sua criação?"]),
        ],
    },
    {
        "numero": 34,
        "definicao_curta": "A gravura é imagem impressa a partir de superfície gravada.",
        "conexao_teologica": "Deus permite que imagens e palavras circulem, e devemos usá-las para comunicar a verdade.",
        "aulas": [
            aula("A gravura no Renascimento do Norte", "A **gravura** transforma desenho gravado em imagem impressa que pode circular.", ["gravura"], "Observe as linhas gravadas que formam uma imagem impressa.", "Linhas gravadas", "A _____ é imagem impressa a partir de superfície gravada.", "gravura", "O que é a gravura?", "Imagem impressa a partir de superfície gravada.", "Faça linhas em uma placa de isopor e pressione-a sobre papel para formar uma impressão.", ["O que é a gravura?", "O que a gravura transforma em imagem impressa?", "Como devemos usar imagens e palavras?"]),
            aula("Xilogravura e gravura em metal", "A **gravura** usa **madeira** ou metal para receber linhas que serão impressas.", ["gravura", "madeira"], "Observe a matriz de madeira e a chapa de metal com linhas gravadas.", "Matrizes gravadas", "A gravura é imagem impressa a partir de superfície _____.", "gravada", "Quais materiais podem receber linhas na gravura?", "Madeira ou metal.", "Crie linhas em uma matriz simples de papelão e faça uma impressão com tinta.", ["O que é a gravura?", "Quais materiais podem receber linhas na gravura?", "O que deve circular com as imagens?"]),
            aula("Imagens reproduzidas e circulação de ideias", "A **gravura** permite **reproduzir** imagens para que ideias circulem por muitos lugares.", ["gravura", "reproduzir"], "Observe várias folhas impressas e veja uma mesma imagem repetida.", "Imagem repetida", "A gravura é imagem _____ a partir de superfície gravada.", "impressa", "Para que a gravura permite reproduzir imagens?", "Para que ideias circulem por muitos lugares.", "Faça duas impressões iguais de uma matriz simples e compare as imagens.", ["O que é a gravura?", "Para que ela permite reproduzir imagens?", "O que devemos comunicar quando imagens circulam?"]),
        ],
    },
    {
        "numero": 35,
        "definicao_curta": "A gravura de Dürer é imagem gravada de observação precisa.",
        "conexao_teologica": "Deus criou a natureza com ordem, e o artista pode observá-la com paciência e gratidão.",
        "aulas": [
            aula("Albrecht Dürer e o desenho gravado", "A **gravura de Dürer** reúne linha e observação para mostrar formas com precisão.", ["gravura de Dürer"], "Observe as linhas finas que constroem a forma na gravura de Dürer.", "Linhas precisas", "A _____ é imagem gravada de observação precisa.", "gravura de Dürer", "O que é a gravura de Dürer?", "Imagem gravada de observação precisa.", "Desenhe uma folha usando linhas curtas para mostrar contorno e textura.", ["O que é a gravura de Dürer?", "O que ela reúne para mostrar formas?", "Como Deus criou a natureza?"]),
            aula("Lebre Jovem e a observação da natureza", "A **gravura de Dürer** observa a **natureza** com linha, textura e atenção à forma.", ["gravura de Dürer", "natureza"], "Observe os pelos e as sombras da Lebre Jovem de Dürer.", "Pelos da lebre", "A gravura de Dürer é imagem gravada de observação _____.", "precisa", "O que Dürer observa na Lebre Jovem?", "Pelos, sombras e forma.", "Desenhe um animal pequeno e use linhas curtas para mostrar seus pelos.", ["O que é a gravura de Dürer?", "O que Dürer observa na Lebre Jovem?", "Como o artista pode observar a natureza?"]),
            aula("Melancolia I e os símbolos na gravura", "A **gravura de Dürer** usa **símbolos** e linhas para organizar uma imagem observada.", ["gravura de Dürer", "símbolos"], "Observe os objetos e as linhas que organizam Melancolia I.", "Símbolos gravados", "A gravura de Dürer é imagem _____ de observação precisa.", "gravada", "O que organiza a imagem em Melancolia I?", "Símbolos e linhas.", "Desenhe três objetos simples e organize-os com linhas em uma composição.", ["O que é a gravura de Dürer?", "O que organiza a imagem em Melancolia I?", "O que a natureza criada por Deus possui?"]),
        ],
    },
    {
        "numero": 36,
        "definicao_curta": "O retrato é imagem que mostra uma pessoa reconhecível.",
        "conexao_teologica": "Cada pessoa é criada à imagem de Deus, e o retrato pode observar sua presença com dignidade.",
        "aulas": [
            aula("Hans Holbein e o retrato do Norte", "O **retrato** de Hans Holbein mostra uma pessoa com rosto, roupa e objetos precisos.", ["retrato"], "Observe o rosto e a roupa que tornam a pessoa reconhecível.", "Rosto reconhecível", "O _____ é imagem que mostra uma pessoa reconhecível.", "retrato", "O que é o retrato?", "Imagem que mostra uma pessoa reconhecível.", "Desenhe o rosto de uma pessoa usando olhos, nariz e boca em posições observáveis.", ["O que é o retrato?", "O que o retrato de Holbein mostra com precisão?", "À imagem de quem cada pessoa é criada?"]),
            aula("Os Embaixadores e os objetos simbólicos", "O **retrato** de Os Embaixadores inclui **objetos** que ajudam a mostrar as pessoas retratadas.", ["retrato", "objetos"], "Observe os instrumentos e livros que aparecem perto das pessoas retratadas.", "Objetos dos embaixadores", "O retrato é imagem que mostra uma pessoa _____.", "reconhecível", "O que os objetos ajudam a mostrar em Os Embaixadores?", "As pessoas retratadas.", "Desenhe uma pessoa e acrescente dois objetos que mostrem algo sobre ela.", ["O que é o retrato?", "O que os objetos ajudam a mostrar em Os Embaixadores?", "Como o retrato pode observar cada pessoa?"]),
            aula("Precisão, textura e presença no retrato", "O **retrato** usa **textura** e precisão para tornar a presença da pessoa mais visível.", ["retrato", "textura"], "Observe a textura da roupa e o rosto pintado com cuidado.", "Textura da roupa", "O retrato é imagem que mostra uma _____ reconhecível.", "pessoa", "O que torna a presença da pessoa mais visível?", "Textura e precisão.", "Desenhe uma roupa com duas texturas diferentes e acrescente um rosto reconhecível.", ["O que é o retrato?", "O que torna a presença mais visível?", "Com que dignidade o retrato pode observar uma pessoa?"]),
        ],
    },
    {
        "numero": 37,
        "definicao_curta": "A Reforma é renovação da Igreja pela Palavra de Deus.",
        "conexao_teologica": "A Palavra de Deus orienta o culto, e a arte deve servir à verdade e à edificação da Igreja.",
        "aulas": [
            aula("A Reforma e as imagens no Norte europeu", "A **Reforma** muda imagens e práticas de culto pela **Palavra** de Deus.", ["Reforma"], "Observe gravuras e livros que mostram mudanças no culto do Norte europeu.", "Gravura e livro", "A _____ é renovação da Igreja pela Palavra de Deus.", "Reforma", "O que é a Reforma?", "Renovação da Igreja pela Palavra de Deus.", "Desenhe um livro aberto e uma gravura simples que mostrem a Palavra no culto.", ["O que é a Reforma?", "O que a Reforma muda no culto?", "O que orienta o culto?"]),
            aula("Arte, culto e circulação de gravuras", "A **Reforma** usa **gravuras** para levar imagens e palavras a muitos lugares.", ["Reforma", "gravuras"], "Observe as folhas impressas que fazem imagens e palavras circularem.", "Folhas impressas", "A Reforma é renovação da Igreja pela _____ de Deus.", "Palavra", "O que as gravuras levam a muitos lugares?", "Imagens e palavras.", "Faça uma pequena gravura de uma página aberta e repita-a em duas folhas.", ["O que é a Reforma?", "O que as gravuras levam a muitos lugares?", "A que a arte deve servir?"]),
            aula("O coral luterano e o canto comunitário", "A **Reforma** reúne a Igreja em **canto** comunitário que ensina a Palavra.", ["Reforma", "canto"], "Observe um grupo reunido ao redor de um livro de música.", "Canto comunitário", "A Reforma é _____ da Igreja pela Palavra de Deus.", "renovação", "O que o canto comunitário ensina?", "A Palavra de Deus.", "Desenhe pessoas reunidas ao redor de um livro de música e mostre linhas de canto.", ["O que é a Reforma?", "O que o canto comunitário ensina?", "Para que a arte deve servir na Igreja?"]),
        ],
    },
    {
        "numero": 38,
        "definicao_curta": "O Renascimento é renovação artística inspirada na observação e ordem.",
        "conexao_teologica": "Deus é fonte de toda beleza e ordem, e a arte pode refletir sua criação com gratidão.",
        "aulas": [
            aula("O legado dos Renascimentos", "O **Renascimento** deixa um legado de observação, composição e **ordem** visual.", ["Renascimento"], "Observe obras italianas e do Norte que usam observação e ordem.", "Legado visual", "O _____ é renovação artística inspirada na observação e ordem.", "Renascimento", "O que é o Renascimento?", "Renovação artística inspirada na observação e ordem.", "Desenhe uma composição com uma figura central e detalhes organizados ao redor.", ["O que é o Renascimento?", "Que legado o Renascimento deixa na arte?", "Quem é fonte de toda beleza e ordem?"]),
            aula("Equilíbrio italiano e detalhe do Norte", "O **Renascimento** une **equilíbrio** italiano e detalhe do Norte em diferentes composições.", ["Renascimento", "equilíbrio"], "Observe uma composição equilibrada e outra com muitos detalhes visíveis.", "Equilíbrio e detalhe", "O Renascimento é renovação artística inspirada na _____ e ordem.", "observação", "O que o Renascimento une em diferentes composições?", "Equilíbrio italiano e detalhe do Norte.", "Desenhe uma figura central equilibrada e acrescente quatro detalhes nas bordas.", ["O que é o Renascimento?", "O que ele une em diferentes composições?", "O que a arte pode refletir com gratidão?"]),
            aula("A transição do Renascimento para o Maneirismo", "O **Renascimento** prepara uma nova **transição** visual da ordem para formas mais alongadas.", ["Renascimento", "transição"], "Observe figuras alongadas e posições que se afastam do equilíbrio renascentista.", "Figuras alongadas", "O Renascimento é renovação artística inspirada na observação e _____.", "ordem", "O que a transição visual prepara?", "Formas mais alongadas.", "Desenhe uma figura com proporções alongadas e compare-a com uma figura equilibrada.", ["O que é o Renascimento?", "O que a transição visual prepara?", "Como a arte pode refletir a criação de Deus?"]),
        ],
    },
]


def semana_para_config(dados):
    aulas = {f"x{i + 1}": item for i, item in enumerate(dados["aulas"])}
    revisao = {
        "fill_in_frase": dados["aulas"][2]["fill_in_frase"],
        "fill_in_resposta": dados["aulas"][2]["fill_in_resposta"],
        "multiples": [
            {"pergunta": item["multiple_pergunta"], "resposta_correta": item["multiple_resposta_correta"], "distratores": item["multiple_distratores"]}
            for item in dados["aulas"]
        ],
    }
    return {"config": {"ano": 3}, "semana": {**dados, "nome_musica": dados["aulas"][0]["titulo"], "aulas": aulas, "revisao": revisao}}


def prova_semanal(dados):
    definicao = dados["definicao_curta"]
    aulas = list(dados["aulas"].values())
    blocos = []
    for item in aulas:
        blocos.extend([
            "FILL_IN 10", "", item["fill_in_frase"].replace("_____", "[1]"), "", f"1 [=] {item['fill_in_resposta']}", "",
            "MULTIPLE_CHOICE 10", "", item["multiple_pergunta"], "", f"{item['multiple_resposta_correta']} [=] true", *[f"{d} [=]" for d in item["multiple_distratores"]], "",
        ])
    blocos.extend([
        "MATCHING 10", "", "Relacione cada palavra ao que ela ensina nesta semana.", "",
        f"{aulas[0]['fill_in_resposta']} [=] {definicao}",
        f"{aulas[1]['fill_in_resposta']} [=] {aulas[1]['multiple_resposta_correta']}",
        f"{aulas[2]['fill_in_resposta']} [=] {aulas[2]['multiple_resposta_correta']}", "",
        "TRUE_OR_FALSE 10", "", definicao, "", "true", "",
        "MULTIPLE_CHOICE 10", "", f"Qual elemento visual aparece na semana sobre {aulas[0]['titulo']}?", "", f"{aulas[0]['multiple_resposta_correta']} [=] true", "Uma forma sem relação com a aula. [=]", "Uma imagem sem observação. [=]",
    ])
    return "# Prova\n\n[CANVAS_QUIZ]\n\n" + "\n--\n\n".join("\n".join(blocos[i:j]).strip() for i, j in _separar_blocos(blocos)) + "\n"


def _separar_blocos(linhas):
    inicios = [i for i, linha in enumerate(linhas) if linha.endswith(" 10")]
    return [(inicio, inicios[idx + 1] if idx + 1 < len(inicios) else len(linhas)) for idx, inicio in enumerate(inicios)]


def revisao_bimestral(configs):
    linhas = ["# Revisão", ""]
    for config in configs:
        semana = config["semana"]
        titulo = semana["aulas"]["x1"]["titulo"]
        linhas.extend([f"## {titulo}", "", "[+PARAGRAPH]", "", f"Nesta semana estudamos que **{semana['definicao_curta'][0].lower() + semana['definicao_curta'][1:]}**", "", "[-PARAGRAPH]", "", "[+HEADING]", "", "Atividade", "", "[-HEADING]", "", "[+IMAGE_TEXT_ON]", "", "@link_png@", "", "@link_mp3@", "", titulo, "", "[-IMAGE_TEXT_ON]", ""])
    linhas.extend(["## [QUIZ] Questões", ""])
    for idx, config in enumerate(configs):
        semana = config["semana"]
        if idx % 2 == 0:
            item = semana["aulas"]["x1"]
            linhas.extend(["[+FILL_IN]", "", item["fill_in_frase"], "", item["fill_in_resposta"], "", "[-FILL_IN]", ""])
        else:
            item = semana["aulas"]["x2"]
            linhas.extend(["[+MULTIPLE]", "", item["multiple_pergunta"], "", f"{item['multiple_resposta_correta']} [=] true", *[f"{d} [=]" for d in item["multiple_distratores"]], "", "[-MULTIPLE]", ""])
    return "\n".join(linhas) + "\n"


def prova_bimestral(configs):
    blocos = []
    for indice in (0, 2, 4, 6):
        item = configs[indice]["semana"]["aulas"]["x1"]
        blocos.append("\n".join(["FILL_IN 10", "", item["fill_in_frase"].replace("_____", "[1]"), "", f"1 [=] {item['fill_in_resposta']}"]))
    for indice in (1, 3, 5, 7):
        item = configs[indice]["semana"]["aulas"]["x2"]
        blocos.append("\n".join(["MULTIPLE_CHOICE 10", "", item["multiple_pergunta"], "", f"{item['multiple_resposta_correta']} [=] true", *[f"{d} [=]" for d in item["multiple_distratores"]]]))
    pares = []
    for config in configs:
        semana = config["semana"]
        pares.append(f"{semana['aulas']['x1']['fill_in_resposta']} [=] {semana['definicao_curta']}")
    blocos.append("\n".join(["MATCHING 10", "", "Relacione cada termo à definição estudada.", "", *pares]))
    blocos.append("\n".join(["TRUE_OR_FALSE 10", "", configs[0]["semana"]["definicao_curta"], "", "true"]))
    return "# Prova\n\n[CANVAS_QUIZ]\n\n" + "\n\n--\n\n".join(blocos) + "\n"


def main():
    DESTINO.mkdir(parents=True, exist_ok=True)
    configs = [semana_para_config(semana) for semana in SEMANAS]
    for config in configs:
        semana = config["semana"]
        numero = semana["numero"]
        for chave in ("x1", "x2", "x3"):
            (DESTINO / f"{numero}.{chave[-1]}.md").write_text(gerar_aula(config["config"], semana, chave), encoding="utf-8")
        (DESTINO / f"{numero}.4.md").write_text(gerar_revisao(config["config"], semana), encoding="utf-8")
        (DESTINO / f"{numero}.5.md").write_text(prova_semanal(semana), encoding="utf-8")
    (DESTINO / "39.md").write_text(revisao_bimestral(configs), encoding="utf-8")
    (DESTINO / "40.md").write_text(prova_bimestral(configs), encoding="utf-8")
    print("Gerados 42 arquivos, semanas 31 a 40.")


if __name__ == "__main__":
    main()
