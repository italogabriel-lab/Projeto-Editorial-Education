#!/usr/bin/env python3
"""Gera, em sequência, o terceiro bimestre do 2º ano de Belas Artes."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / (
    "Projeto - Bibline Academy ( Produção de Aulas)/"
    "Belas Artes - Fase da Gramática/1 Fase - Gramática/"
    "2º Ano - DA CRIAÇÃO ATÉ A ARTE BIZANTINA/Aulas"
)


def lesson(
    title: str,
    keyword: str,
    paragraph_bold: str,
    perceive: str,
    hotspot: str,
    multiple_question: str,
    multiple_correct: str,
    multiple_distractor: str,
    activity: str,
    narrar_question: str,
) -> dict:
    return {
        "title": title,
        "keyword": keyword,
        "paragraph": paragraph_bold.replace("**", ""),
        "paragraph_bold": paragraph_bold,
        "perceive": perceive,
        "hotspot": hotspot,
        "multiple_question": multiple_question,
        "multiple_correct": multiple_correct,
        "multiple_distractor": multiple_distractor,
        "activity": activity,
        "narrar_question": narrar_question,
    }


WEEKS = {
    21: {
        "title": "A Mesopotâmia e suas cidades",
        "term": "zigurate",
        "definition": "O zigurate é uma torre escalonada que forma um templo antigo.",
        "music": "Ritmos antigos e sons da natureza",
        "lessons": [
            lesson(
                "A Mesopotâmia e suas cidades",
                "zigurate",
                "O **zigurate** aparece como uma torre escalonada que domina a cidade mesopotâmica.",
                "Observe a imagem de uma cidade mesopotâmica e identifique o zigurate como torre escalonada central.",
                "Zigurate no centro da cidade",
                "Onde o zigurate aparece?",
                "Na cidade mesopotâmica como torre escalonada central.",
                "Em uma pintura moderna sem templo.",
                "Desenhe uma cidade mesopotâmica e destaque o zigurate.",
                "Como o zigurate aparece?",
            ),
            lesson(
                "O zigurate como templo",
                "templo",
                "O **zigurate** eleva o **templo** em níveis visuais e o destaca no centro da cidade mesopotâmica.",
                "Observe os níveis do zigurate e veja como o templo se destaca no centro da cidade mesopotâmica.",
                "Níveis do zigurate e templo",
                "Onde o zigurate eleva o templo?",
                "No centro da cidade mesopotâmica.",
                "No fundo de uma pintura moderna.",
                "Desenhe os níveis do zigurate e destaque o templo no alto.",
                "Como o zigurate destaca o templo?",
            ),
            lesson(
                "A torre de Babel e o orgulho",
                "antigo",
                "O **zigurate** e a torre de Babel mostram construções **antigas** marcadas pelo orgulho humano.",
                "Observe a torre de Babel em uma imagem e identifique sua forma antiga ligada ao orgulho humano.",
                "Torre antiga ligada ao orgulho",
                "O que a torre de Babel expressa?",
                "Orgulho humano diante da grandeza da torre.",
                "Humildade diante de uma paisagem sem construção.",
                "Desenhe uma torre antiga e mostre sua altura na composição.",
                "O que a torre de Babel expressa?",
            ),
        ],
    },
    22: {
        "title": "Estelas e relevos mesopotâmicos",
        "term": "estela",
        "definition": "A estela é uma pedra erguida que preserva lei, poder e memória.",
        "music": "Cantos antigos da Mesopotâmia",
        "lessons": [
            lesson(
                "Estelas e relevos mesopotâmicos",
                "estela",
                "A **estela** aparece como uma pedra erguida com relevo, lei, poder e memória.",
                "Observe uma estela mesopotâmica e identifique a pedra erguida com figuras e inscrições.",
                "Estela erguida com relevo",
                "O que aparece na estela?",
                "Uma pedra erguida com relevo, lei, poder e memória.",
                "Uma folha lisa sem figuras nem inscrições.",
                "Desenhe uma estela erguida e acrescente um relevo simples.",
                "Como a estela aparece?",
            ),
            lesson(
                "O código de Hamurábi",
                "lei",
                "A **estela** apresenta a **lei** gravada entre figuras e sinais do poder mesopotâmico.",
                "Observe o código de Hamurábi e veja como a lei aparece gravada na pedra.",
                "Lei gravada no código de Hamurábi",
                "O que a estela apresenta?",
                "A lei gravada entre figuras e sinais do poder.",
                "Uma paisagem sem escrita nem figuras.",
                "Desenhe uma pedra com uma lei representada por sinais visuais.",
                "Como a estela apresenta a lei?",
            ),
            lesson(
                "A lei gravada em pedra",
                "memória",
                "A **estela** guarda a lei como **memória** visível em uma pedra erguida.",
                "Observe a inscrição na pedra e perceba como a lei permanece visível como memória.",
                "Lei visível como memória",
                "O que a estela guarda?",
                "A lei como memória visível em uma pedra erguida.",
                "Cores misturadas sem inscrição em uma tela.",
                "Desenhe uma inscrição simples e mostre como a pedra guarda memória.",
                "Como a estela guarda a lei?",
            ),
        ],
    },
    23: {
        "title": "Selos cilíndricos e escrita cuneiforme",
        "term": "relevo",
        "definition": "O relevo é uma imagem elevada que mostra poder em superfície plana.",
        "music": "Ritmos antigos e sons da natureza",
        "lessons": [
            lesson(
                "Selos cilíndricos e escrita cuneiforme",
                "relevo",
                "O **relevo** aparece nos selos cilíndricos como imagem elevada em uma superfície plana.",
                "Observe um selo cilíndrico e identifique o relevo formado por figuras e sinais.",
                "Relevo no selo cilíndrico",
                "Onde o relevo aparece?",
                "Nos selos cilíndricos como imagem elevada.",
                "Em uma folha sem figuras nem marcas.",
                "Desenhe um selo cilíndrico e crie nele um relevo com sinais.",
                "Onde o relevo aparece?",
            ),
            lesson(
                "Imagens do poder na Assíria",
                "poder",
                "O **relevo** mostra o **poder** assírio em figuras de reis, animais e palácios.",
                "Observe um relevo assírio e veja como reis e animais representam o poder na imagem.",
                "Figuras do poder assírio",
                "O que o relevo mostra na Assíria?",
                "O poder em figuras de reis, animais e palácios.",
                "Uma cena doméstica sem figuras de autoridade.",
                "Desenhe uma figura de autoridade e organize-a em um relevo imaginário.",
                "Como o relevo mostra o poder?",
            ),
            lesson(
                "Relevos de guerra e caça",
                "superfície",
                "O **relevo** reúne cenas de guerra e caça em uma **superfície** plana de pedra.",
                "Observe um relevo de guerra e caça e identifique as cenas organizadas na superfície da pedra.",
                "Guerra e caça na superfície da pedra",
                "Onde as cenas aparecem?",
                "Na superfície plana de pedra do relevo.",
                "Em um espaço vazio sem pedra ou imagem.",
                "Desenhe uma cena de caça em uma superfície plana e organize seus elementos.",
                "Onde as cenas aparecem?",
            ),
        ],
    },
    24: {
        "title": "Instrumentos e música na Mesopotâmia",
        "term": "harpa",
        "definition": "A harpa é um instrumento musical de cordas e forma triangular.",
        "music": "Hinos antigos da Mesopotâmia",
        "lessons": [
            lesson(
                "Instrumentos e música na Mesopotâmia",
                "harpa",
                "A **harpa** aparece como instrumento musical de cordas e forma triangular.",
                "Observe uma harpa antiga e identifique suas cordas e sua forma triangular.",
                "Harpa de forma triangular",
                "O que aparece na harpa?",
                "Cordas e forma triangular em um instrumento musical.",
                "Uma superfície plana sem cordas nem forma triangular.",
                "Desenhe uma harpa e represente suas cordas com linhas.",
                "Como a harpa aparece?",
            ),
            lesson(
                "Liras e harpas de Ur",
                "cordas",
                "A **harpa** produz sons por meio de suas **cordas** organizadas na forma triangular.",
                "Observe as liras e harpas de Ur e conte as cordas organizadas no instrumento.",
                "Cordas organizadas na harpa",
                "O que produz sons na harpa?",
                "As cordas organizadas na forma triangular.",
                "A moldura sem cordas e sem instrumento.",
                "Desenhe uma harpa de Ur e trace suas cordas em sequência.",
                "Como a harpa produz sons?",
            ),
            lesson(
                "O Hino Hurrita como registro antigo",
                "forma",
                "A **harpa** mantém sua **forma** triangular ao acompanhar o hino antigo.",
                "Observe uma representação da harpa e identifique a forma triangular ligada ao hino antigo.",
                "Forma triangular da harpa",
                "Qual é a forma da harpa?",
                "Triangular, com cordas organizadas no instrumento.",
                "Circular, sem cordas organizadas.",
                "Desenhe a forma triangular de uma harpa e acrescente suas cordas.",
                "Qual é a forma da harpa?",
            ),
        ],
    },
    25: {
        "title": "A arte egípcia e a lei da frontalidade",
        "term": "frontalidade",
        "definition": "A frontalidade é a apresentação frontal de uma figura na arte.",
        "music": "Cantos antigos do Egito",
        "lessons": [
            lesson(
                "A arte egípcia e a lei da frontalidade",
                "frontalidade",
                "A **frontalidade** aparece na apresentação frontal de uma figura na arte egípcia.",
                "Observe uma pintura egípcia e identifique a apresentação frontal da figura na composição.",
                "Figura frontal na arte egípcia",
                "O que aparece na frontalidade?",
                "A apresentação frontal de uma figura na arte egípcia.",
                "Uma figura sem posição definida na composição.",
                "Desenhe uma figura egípcia de frente e organize-a em uma composição.",
                "Como a frontalidade aparece?",
            ),
            lesson(
                "Pirâmides de Gizé",
                "figura",
                "A **frontalidade** organiza a **figura** egípcia diante das pirâmides de Gizé.",
                "Observe uma imagem das pirâmides e compare sua face frontal com a figura egípcia.",
                "Face frontal das pirâmides",
                "O que a frontalidade organiza?",
                "A figura egípcia diante das pirâmides de Gizé.",
                "Uma sombra sem figura ou construção.",
                "Desenhe uma pirâmide de frente e coloque uma figura ao lado.",
                "O que a frontalidade organiza?",
            ),
            lesson(
                "A monumentalidade do Egito",
                "arte",
                "A **frontalidade** permanece na **arte** egípcia em figuras, pirâmides e monumentos.",
                "Observe um monumento egípcio e identifique a posição frontal que permanece na arte.",
                "Frontalidade em monumentos egípcios",
                "Onde a frontalidade permanece?",
                "Na arte egípcia em figuras, pirâmides e monumentos.",
                "Somente em paisagens sem formas construídas.",
                "Desenhe um monumento egípcio de frente e destaque sua forma estável.",
                "Onde a frontalidade permanece?",
            ),
        ],
    },
    26: {
        "title": "Hieróglifos e imagem",
        "term": "hieróglifo",
        "definition": "O hieróglifo é um símbolo sagrado que une imagem e escrita.",
        "music": "Cantos antigos do Egito",
        "lessons": [
            lesson(
                "Hieróglifos e imagem",
                "hieróglifo",
                "O **hieróglifo** aparece como símbolo sagrado que une imagem e escrita egípcia.",
                "Observe um hieróglifo e identifique a união entre imagem, sinal e escrita.",
                "Imagem e escrita no hieróglifo",
                "O que o hieróglifo une?",
                "Imagem e escrita em um símbolo sagrado.",
                "Cores misturadas sem sinal ou imagem.",
                "Desenhe um símbolo e acrescente uma imagem que represente sua ideia.",
                "Como o hieróglifo aparece?",
            ),
            lesson(
                "Narrativa nas paredes dos templos",
                "imagem",
                "O **hieróglifo** transforma a **imagem** em narrativa nas paredes dos templos egípcios.",
                "Observe uma parede de templo e veja como a imagem organiza uma narrativa visual.",
                "Imagem narrativa na parede do templo",
                "O que o hieróglifo transforma em narrativa?",
                "A imagem nas paredes dos templos egípcios.",
                "Uma parede lisa sem imagens ou sinais.",
                "Desenhe uma parede com três imagens em sequência para formar uma narrativa.",
                "Como o hieróglifo transforma a imagem?",
            ),
            lesson(
                "O poder dos símbolos egípcios",
                "escrita",
                "O **hieróglifo** une imagem e **escrita** para representar o poder egípcio.",
                "Observe símbolos egípcios e identifique como imagem e escrita aparecem juntas.",
                "Símbolos de imagem e escrita",
                "O que o hieróglifo une para representar o poder?",
                "Imagem e escrita em símbolos egípcios.",
                "Uma paisagem sem símbolos ou escrita.",
                "Desenhe um símbolo egípcio e escreva ao lado a ideia que ele representa.",
                "Como o hieróglifo representa o poder?",
            ),
        ],
    },
    27: {
        "title": "As cores do Nilo",
        "term": "paleta",
        "definition": "A paleta é um conjunto de cores que apresenta contraste na obra.",
        "music": "Cantos antigos do Egito",
        "lessons": [
            lesson(
                "As cores do Nilo",
                "paleta",
                "A **paleta** egípcia reúne cores contrastantes nas imagens do Nilo e do deserto.",
                "Observe uma paisagem do Nilo e identifique as cores reunidas na paleta egípcia.",
                "Paleta do Nilo e do deserto",
                "O que a paleta egípcia reúne?",
                "Cores contrastantes nas imagens do Nilo e do deserto.",
                "Uma única cor sem variação na imagem.",
                "Desenhe o Nilo e escolha cores contrastantes para a água e o deserto.",
                "Como a paleta egípcia aparece?",
            ),
            lesson(
                "Cor simbólica na arte egípcia",
                "cores",
                "A **paleta** reúne **cores** que representam água, vegetação, areia e vida egípcia.",
                "Observe uma pintura egípcia e identifique as cores usadas para representar a paisagem.",
                "Cores da paisagem egípcia",
                "O que a paleta reúne?",
                "Cores que representam água, vegetação, areia e vida.",
                "Linhas sem cor para representar a paisagem.",
                "Pinte uma paisagem egípcia e use uma cor para cada elemento.",
                "Como as cores representam a paisagem?",
            ),
            lesson(
                "Contraste na paleta egípcia",
                "contraste",
                "A **paleta** organiza o **contraste** entre cores claras e escuras na arte egípcia.",
                "Observe uma imagem egípcia e compare o contraste entre as cores claras e escuras.",
                "Contraste entre cores claras e escuras",
                "O que a paleta organiza?",
                "O contraste entre cores claras e escuras na arte.",
                "A repetição de uma cor sem diferença de tom.",
                "Crie uma composição egípcia usando uma cor clara e outra escura.",
                "Como a paleta organiza o contraste?",
            ),
        ],
    },
    28: {
        "title": "Esculturas e máscaras do Egito",
        "term": "escultura egípcia",
        "definition": "A escultura egípcia é uma imagem talhada em pedra ou metal.",
        "music": "Cantos antigos do Egito",
        "lessons": [
            lesson(
                "Esculturas e máscaras do Egito",
                "escultura egípcia",
                "A **escultura egípcia** aparece como imagem talhada em pedra ou metal.",
                "Observe uma escultura egípcia e identifique a imagem talhada em um material sólido.",
                "Imagem talhada na escultura egípcia",
                "O que é a escultura egípcia?",
                "Uma imagem talhada em pedra ou metal.",
                "Uma pintura feita somente com água no papel.",
                "Desenhe uma escultura egípcia e indique o material que ela representa.",
                "Como a escultura egípcia aparece?",
            ),
            lesson(
                "O busto de Nefertiti",
                "pedra",
                "A **escultura egípcia** apresenta o busto de Nefertiti como imagem talhada em **pedra**.",
                "Observe o busto de Nefertiti e identifique o rosto esculpido na pedra.",
                "Busto de Nefertiti em pedra",
                "Onde aparece o busto de Nefertiti?",
                "Na escultura egípcia talhada em pedra.",
                "Em uma pintura sem rosto ou material sólido.",
                "Desenhe um busto de frente e represente sua forma como escultura.",
                "Como o busto de Nefertiti aparece?",
            ),
            lesson(
                "A máscara funerária de Tutancâmon",
                "metal",
                "A **escultura egípcia** apresenta a máscara funerária como imagem dourada de **metal**.",
                "Observe a máscara de Tutancâmon e identifique sua imagem dourada feita de metal.",
                "Máscara dourada de Tutancâmon",
                "De que é feita a máscara funerária?",
                "De metal dourado como imagem da escultura egípcia.",
                "De papel sem brilho ou material resistente.",
                "Desenhe uma máscara frontal e use linhas para indicar seu brilho metálico.",
                "De que é feita a máscara funerária?",
            ),
        ],
    },
}


def fill_sentence(definition: str, keyword: str, quiz: bool = False) -> str:
    marker = "[1]" if quiz else "_____"
    result = definition.replace(keyword, marker, 1)
    if result == definition:
        raise ValueError(f"palavra-chave ausente na definição: {keyword}")
    return result


def regular_lesson(week: dict, item: dict) -> str:
    definition = week["definition"]
    paragraph = item["paragraph"]
    paragraph_bold = item["paragraph_bold"]
    audio_line = f"{definition} {paragraph}"
    visual_definition = f"**{definition}**"
    lines = [
        f"# {item['title']}", "", "## Definir", "", "[+PARAGRAPH]", "",
        visual_definition, "", paragraph_bold, "Veja o vídeo abaixo.", "",
        "[-PARAGRAPH]", "", "[+VIDEO][-VIDEO]", "", "[+HEADING]", "",
        "Atividade", "", "[-HEADING]", "", "[+PARAGRAPH]", "",
        "Leia o fato e ouça o áudio clicando abaixo.", "", "[-PARAGRAPH]", "",
        "[+ACCORDION]", "", item["title"], "", "@link_png@", "", "[MP3/]", "",
        "#VOX:", "", audio_line, "", "[MP3\\]", "", visual_definition, "",
        paragraph_bold, "", "[-ACCORDION]", "", "## Perceber", "", "[+PARAGRAPH]", "",
        item["perceive"], "", "[-PARAGRAPH]", "", "[+IMAGE_LABELED]", "",
        "@link_png@", "", "--", "", "49 50", "", item["hotspot"], "",
        "[-IMAGE_LABELED]", "", "## Recordar", "", "[+PARAGRAPH]", "",
        "Ouça e repita o fato abaixo.", "", "[-PARAGRAPH]", "", "[+STATEMENT_D]", "",
        "[MP3/]", "", "#VOX:", "", definition, "", "[MP3\\]", "", definition,
        "", "[-STATEMENT_D]", "", "[+HEADING]", "", "Hora de memorizar com música",
        "", "[-HEADING]", "", "[+PARAGRAPH]", "", "Clique abaixo para ouvir a música.",
        "", "[-PARAGRAPH]", "", "[+IMAGE_TEXT_ON]", "", "@link_png@", "", "@link_mp3@",
        "", week["music"], "", "[-IMAGE_TEXT_ON]", "", "## Praticar", "", "[+HEADING]", "",
        "Atividade 1", "", "[-HEADING]", "", "[+PARAGRAPH]", "",
        "Complete o fato abaixo com a palavra correta.", "", "[-PARAGRAPH]", "", "[+FILL_IN]", "",
        fill_sentence(definition, item["keyword"]), "", item["keyword"], "", "[-FILL_IN]", "",
        "[+HEADING]", "", "Atividade 2", "", "[-HEADING]", "", "[+MULTIPLE]", "",
        item["multiple_question"], "", f"{item['multiple_correct']} [=] true",
        f"{item['multiple_distractor']} [=]", "", "[-MULTIPLE]", "", "[+HEADING]", "",
        "Atividade Extra", "", "[-HEADING]", "", "[+PARAGRAPH]", "",
        "Acesse o PDF abaixo e faça a atividade com atenção.", "", "[-PARAGRAPH]", "",
        "[+ACTIVITY_WORKSHEET]", "", f"INSTRUCTION={item['activity']}", "", "[-ACTIVITY_WORKSHEET]", "",
        "## Narrar", "", "[+HEADING]", "", "Leitura", "", "[-HEADING]", "",
        "[+IMAGE_TEXT_ASIDE]", "", "@link_png@", "", "[MP3/]", "", "#VOX:", "",
        audio_line, "", "[MP3\\]", "", visual_definition, "", paragraph_bold, "",
        "[-IMAGE_TEXT_ASIDE]", "", "[+HEADING]", "", "Pergunta", "", "[-HEADING]", "",
        "[+PARAGRAPH]", "", "Responda oralmente à pergunta abaixo sobre o texto.", "",
        "[-PARAGRAPH]", "", "[+LIST_NUMBERED]", "", item["narrar_question"], "",
        "[-LIST_NUMBERED]", "",
    ]
    return "\n".join(lines)


def weekly_review(week: dict) -> str:
    definition = week["definition"]
    lessons = week["lessons"]
    lines = [
        "# Revisão", "", "## Definir", "", "[+PARAGRAPH]", "",
        f"Nesta semana estudamos que **{definition}**", "", "[-PARAGRAPH]", "",
        "[+HEADING]", "", "Atividade", "", "[-HEADING]", "", "[+IMAGE_TEXT_ON]", "",
        "@link_png@", "", "@link_mp3@", "", lessons[0]["title"], "", "[-IMAGE_TEXT_ON]", "",
        "## Perceber", "", "[+PARAGRAPH]", "",
        f"Observe as imagens da semana e veja como {week['term']} aparece em formas, imagens ou obras.",
        "", "[-PARAGRAPH]", "", "[+HEADING]", "", "Atividade", "", "[-HEADING]", "",
        "[+IMAGE_LABELED]", "", "@link_png@", "", "--", "", "20 50", "", lessons[0]["title"],
        "", "--", "", "50 50", "", lessons[1]["title"], "", "--", "", "80 50", "",
        lessons[2]["title"], "", "[-IMAGE_LABELED]", "", "## Recordar", "", "[+PARAGRAPH]", "",
        "Recorde o fato estudado durante a semana.", "", "[-PARAGRAPH]", "", "[+HEADING]", "",
        "Atividade", "", "[-HEADING]", "", "[+STATEMENT_D]", "", "[MP3/]", "", "#VOX:", "",
        definition, "", "[MP3\\]", "", definition, "", "[-STATEMENT_D]", "",
        "## [QUIZ] Praticar", "", "[+FILL_IN]", "", fill_sentence(definition, week["term"]), "",
        week["term"], "", "[-FILL_IN]", "",
    ]
    for item in lessons:
        lines += [
            "[+MULTIPLE]", "", item["multiple_question"], "",
            f"{item['multiple_correct']} [=] true", f"{item['multiple_distractor']} [=]", "",
            "[-MULTIPLE]", "",
        ]
    lines += [
        "## Narrar", "", "[+PARAGRAPH]", "",
        "Agora é hora de contar exatamente o fato que você aprendeu esta semana.", "",
        "[-PARAGRAPH]", "",
    ]
    return "\n".join(lines)


def weekly_exam(week: dict) -> str:
    definition = week["definition"]
    lessons = week["lessons"]
    lines = ["# Prova", "", "[CANVAS_QUIZ]", ""]
    for item in lessons:
        lines += [
            "FILL_IN 10", "", fill_sentence(definition, item["keyword"], quiz=True), "",
            f"1 [=] {item['keyword']}", "", "--", "",
        ]
    for item in lessons:
        lines += [
            "MULTIPLE_CHOICE 10", "", item["multiple_question"], "",
            f"{item['multiple_correct']} [=] true", f"{item['multiple_distractor']} [=]", "",
            "--", "",
        ]
    lines += [
        "MATCHING 10", "", "Relacione cada palavra ao aspecto visual estudado.", "",
        f"{week['term']} [=] {definition[0].lower() + definition[1:]}",
        f"{lessons[1]['keyword']} [=] {lessons[1]['title']}",
        f"{lessons[2]['keyword']} [=] {lessons[2]['title']}", "", "--", "",
        "TRUE_OR_FALSE 10", "", definition, "", "true", "", "--", "",
        "MULTIPLE_CHOICE 10", "", lessons[0]["multiple_question"], "",
        f"{lessons[0]['multiple_correct']} [=] true", f"{lessons[0]['multiple_distractor']} [=]", "",
    ]
    return "\n".join(lines)


def bimonthly_review() -> str:
    lines = ["# Revisão", ""]
    for week in WEEKS.values():
        lines += [
            f"## {week['lessons'][0]['title']}", "", "[+PARAGRAPH]", "",
            f"Nesta semana estudamos que **{week['definition']}**", "", "[-PARAGRAPH]", "",
            "[+HEADING]", "", "Atividade", "", "[-HEADING]", "", "[+IMAGE_TEXT_ON]", "",
            "@link_png@", "", "@link_mp3@", "", week["lessons"][0]["title"], "", "[-IMAGE_TEXT_ON]", "",
        ]
    lines += ["## [QUIZ] Questões", ""]
    for index, week in enumerate(WEEKS.values()):
        if index % 2 == 0:
            lines += [
                "[+FILL_IN]", "", fill_sentence(week["definition"], week["term"]), "",
                week["term"], "", "[-FILL_IN]", "",
            ]
        else:
            item = week["lessons"][0]
            lines += [
                "[+MULTIPLE]", "", item["multiple_question"], "",
                f"{item['multiple_correct']} [=] true", f"{item['multiple_distractor']} [=]", "",
                "[-MULTIPLE]", "",
            ]
    return "\n".join(lines)


def bimonthly_exam() -> str:
    weeks = list(WEEKS.values())
    lines = ["# Prova", "", "[CANVAS_QUIZ]", ""]
    for week in weeks[:4]:
        lines += [
            "FILL_IN 10", "", fill_sentence(week["definition"], week["term"], quiz=True), "",
            f"1 [=] {week['term']}", "", "--", "",
        ]
    for week in weeks[4:]:
        item = week["lessons"][0]
        lines += [
            "MULTIPLE_CHOICE 10", "", item["multiple_question"], "",
            f"{item['multiple_correct']} [=] true", f"{item['multiple_distractor']} [=]", "",
            "--", "",
        ]
    lines += ["MATCHING 10", "", "Relacione cada termo à definição estudada.", ""]
    for week in weeks:
        lines.append(f"{week['term']} [=] {week['definition']}")
    lines += ["", "--", "", "TRUE_OR_FALSE 10", "", weeks[-1]["definition"], "", "true", ""]
    return "\n".join(lines)


def validate_week(week: dict) -> None:
    definition_words = week["definition"].rstrip(".").split()
    if not 8 <= len(definition_words) <= 12:
        raise ValueError(f"semana com definição fora do limite: {week['title']}")
    if len(week["lessons"]) != 3:
        raise ValueError(f"semana sem três aulas: {week['title']}")
    for item in week["lessons"]:
        if week["definition"].replace(item["keyword"], "", 1) == week["definition"]:
            raise ValueError(f"palavra-chave ausente na definição: {item['title']}")


def write_all() -> None:
    BASE.mkdir(parents=True, exist_ok=True)
    for number, week in WEEKS.items():
        validate_week(week)
        for index, item in enumerate(week["lessons"], start=1):
            (BASE / f"{number}.{index}.md").write_text(regular_lesson(week, item), encoding="utf-8")
        (BASE / f"{number}.4.md").write_text(weekly_review(week), encoding="utf-8")
        (BASE / f"{number}.5.md").write_text(weekly_exam(week), encoding="utf-8")
    (BASE / "29.md").write_text(bimonthly_review(), encoding="utf-8")
    (BASE / "30.md").write_text(bimonthly_exam(), encoding="utf-8")
    print("Geradas as semanas 21–28 e os arquivos 29.md e 30.md.")


if __name__ == "__main__":
    write_all()
