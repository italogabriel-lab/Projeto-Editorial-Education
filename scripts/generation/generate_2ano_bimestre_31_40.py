#!/usr/bin/env python3
"""Gera as semanas 31–38 e as revisões 39–40 do 2º ano de Belas Artes."""

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
    31: {
        "title": "A arte egeia e suas ilhas",
        "term": "arte cicládica",
        "definition": "A arte cicládica é uma expressão visual das ilhas do Egeu.",
        "music": "Cantos antigos do mar Egeu",
        "lessons": [
            lesson(
                "A arte egeia e suas ilhas",
                "arte cicládica",
                "A **arte cicládica** aparece em figuras simples ligadas às ilhas do Egeu.",
                "Observe uma imagem egeia e identifique figuras simples ligadas às ilhas do Egeu.",
                "Figuras simples das ilhas do Egeu",
                "Onde aparece a arte cicládica?",
                "Nas figuras simples ligadas às ilhas do Egeu.",
                "Em retratos romanos realistas.",
                "Desenhe uma figura cicládica usando linhas simples e formas reduzidas.",
                "Onde aparece a arte cicládica?",
            ),
            lesson(
                "Figuras das Cíclades",
                "ilhas",
                "A **arte cicládica** mostra **ilhas** e figuras humanas de formas claras e reduzidas.",
                "Observe uma figura das Cíclades e perceba suas formas claras, reduzidas e ligadas às ilhas.",
                "Figura humana das ilhas Cíclades",
                "O que a arte cicládica mostra?",
                "Ilhas e figuras humanas de formas claras e reduzidas.",
                "Palácios romanos com retratos realistas.",
                "Desenhe uma figura das Cíclades e reduza seu corpo a formas claras.",
                "O que a arte cicládica mostra?",
            ),
            lesson(
                "Formas simplificadas da arte cicládica",
                "visual",
                "A **arte cicládica** usa formas **visuais** simplificadas para representar figuras humanas.",
                "Observe uma figura cicládica e identifique como linhas e formas visuais reduzem o corpo humano.",
                "Formas visuais simplificadas",
                "Como a arte cicládica representa figuras?",
                "Com formas visuais simplificadas.",
                "Com detalhes realistas e sombras fotográficas.",
                "Crie uma figura humana simplificada com linhas e formas geométricas.",
                "Como a arte cicládica representa figuras?",
            ),
        ],
    },
    32: {
        "title": "A arte minoica e Cnossos",
        "term": "fresco minoico",
        "definition": "O fresco minoico é uma pintura mural que representa movimento e natureza.",
        "music": "Cantos antigos do mar Egeu",
        "lessons": [
            lesson(
                "A arte minoica e Cnossos",
                "fresco minoico",
                "O **fresco minoico** aparece em paredes com cores, figuras e movimento.",
                "Observe uma imagem de Cnossos e identifique cores, figuras e movimento na parede pintada.",
                "Fresco colorido do palácio de Cnossos",
                "O que aparece no fresco minoico?",
                "Cores, figuras e movimento em paredes pintadas.",
                "Uma parede sem cores, figuras ou movimento.",
                "Desenhe uma parede de Cnossos com cores e figuras em movimento.",
                "O que aparece no fresco minoico?",
            ),
            lesson(
                "Frescos do palácio de Cnossos",
                "mural",
                "O **fresco minoico** forma uma pintura **mural** colorida no palácio de Cnossos.",
                "Observe um fresco do palácio e veja como a pintura mural ocupa a parede com cores vivas.",
                "Pintura mural colorida de Cnossos",
                "Onde aparece a pintura mural?",
                "No palácio de Cnossos, formada pelo fresco minoico.",
                "Em uma folha sem parede e sem pintura.",
                "Pinte uma composição mural com figuras coloridas inspiradas em Cnossos.",
                "Onde aparece a pintura mural?",
            ),
            lesson(
                "Movimento e natureza na arte minoica",
                "movimento",
                "O **fresco minoico** apresenta **movimento** e natureza em figuras leves de Cnossos.",
                "Observe as figuras minoicas e identifique movimento, plantas e animais na composição.",
                "Movimento e natureza no fresco minoico",
                "O que o fresco minoico apresenta?",
                "Movimento e natureza em figuras leves de Cnossos.",
                "Figuras imóveis em uma composição sem natureza.",
                "Desenhe uma figura minoica em movimento junto de uma planta ou animal.",
                "O que o fresco minoico apresenta?",
            ),
        ],
    },
    33: {
        "title": "A arte grega e suas ordens",
        "term": "ordem grega",
        "definition": "A ordem grega é um sistema de proporção para colunas e templos.",
        "music": "Hinos gregos antigos",
        "lessons": [
            lesson(
                "A arte grega e suas ordens",
                "ordem grega",
                "A **ordem grega** aparece em templos com colunas organizadas e proporções regulares.",
                "Observe um templo grego e identifique colunas organizadas por proporções regulares.",
                "Colunas organizadas no templo grego",
                "Onde aparece a ordem grega?",
                "Em templos com colunas organizadas e proporções regulares.",
                "Em uma paisagem sem colunas ou proporções.",
                "Desenhe um templo grego e organize suas colunas em sequência.",
                "Onde aparece a ordem grega?",
            ),
            lesson(
                "O Partenon e as colunas gregas",
                "colunas",
                "A **ordem grega** organiza **colunas** com base, eixo e capitel em um templo.",
                "Observe o Partenon e identifique a base, o eixo e o capitel de suas colunas.",
                "Colunas do Partenon",
                "O que a ordem grega organiza?",
                "Colunas com base, eixo e capitel em um templo.",
                "Janelas sem colunas, base ou capitel.",
                "Desenhe uma coluna com base, eixo e capitel diante de um templo.",
                "O que a ordem grega organiza?",
            ),
            lesson(
                "A ordem na arquitetura grega",
                "proporção",
                "A **ordem grega** relaciona **proporção** e beleza na arquitetura dos templos.",
                "Observe a arquitetura grega e compare a proporção das colunas com a beleza do templo.",
                "Proporção e beleza na arquitetura grega",
                "O que a ordem grega relaciona?",
                "Proporção e beleza na arquitetura dos templos.",
                "Cores aleatórias sem relação entre as partes.",
                "Desenhe um templo e ajuste a proporção entre suas colunas e o frontão.",
                "O que a ordem grega relaciona?",
            ),
        ],
    },
    34: {
        "title": "Vasos gregos e narrativa",
        "term": "vaso grego",
        "definition": "O vaso grego é um recipiente decorado com imagens narrativas.",
        "music": "Hinos gregos antigos",
        "lessons": [
            lesson(
                "Vasos gregos e narrativa",
                "vaso grego",
                "O **vaso grego** aparece como recipiente decorado com imagens narrativas.",
                "Observe um vaso grego e identifique o recipiente decorado com uma cena narrativa.",
                "Recipiente decorado com cena narrativa",
                "O que aparece no vaso grego?",
                "Um recipiente decorado com imagens narrativas.",
                "Uma pedra sem recipiente, decoração ou imagens.",
                "Desenhe um vaso grego e organize uma cena em sua superfície.",
                "O que aparece no vaso grego?",
            ),
            lesson(
                "Figuras negras e figuras vermelhas",
                "imagens",
                "O **vaso grego** reúne **imagens** negras e vermelhas em faixas pintadas.",
                "Observe um vaso grego e compare as imagens negras e vermelhas distribuídas em faixas.",
                "Imagens negras e vermelhas no vaso",
                "O que o vaso grego reúne?",
                "Imagens negras e vermelhas em faixas pintadas.",
                "Uma superfície branca sem imagens ou faixas.",
                "Crie duas faixas decoradas, uma com figuras negras e outra com figuras vermelhas.",
                "O que o vaso grego reúne?",
            ),
            lesson(
                "Cenas da mitologia nos vasos",
                "narrativas",
                "O **vaso grego** apresenta **narrativas** de heróis e deuses em sua superfície.",
                "Observe a superfície do vaso e identifique heróis e deuses organizados em uma narrativa visual.",
                "Narrativas de heróis e deuses no vaso",
                "O que o vaso grego apresenta?",
                "Narrativas de heróis e deuses em sua superfície.",
                "Uma superfície sem personagens ou narrativa.",
                "Desenhe uma cena narrativa com dois personagens em uma faixa de vaso.",
                "O que o vaso grego apresenta?",
            ),
        ],
    },
    35: {
        "title": "Escultura grega e proporção",
        "term": "proporção",
        "definition": "A proporção é a relação de medida entre partes de uma figura.",
        "music": "Hinos gregos antigos",
        "lessons": [
            lesson(
                "Escultura grega e proporção",
                "proporção",
                "A **proporção** aparece na escultura grega como relação entre partes do corpo.",
                "Observe uma escultura grega e compare a relação entre as partes do corpo.",
                "Relação entre partes do corpo",
                "Onde aparece a proporção?",
                "Na escultura grega como relação entre partes do corpo.",
                "Em uma figura sem relação entre suas partes.",
                "Desenhe uma figura humana e compare a medida de suas partes.",
                "Onde aparece a proporção?",
            ),
            lesson(
                "O Doríforo de Policleto",
                "medida",
                "A **proporção** organiza a **medida** do corpo no Doríforo de Policleto.",
                "Observe o Doríforo e identifique como a medida de cada parte organiza o corpo esculpido.",
                "Medida do corpo no Doríforo",
                "O que a proporção organiza?",
                "A medida do corpo no Doríforo de Policleto.",
                "A cor do fundo em uma pintura sem corpo.",
                "Desenhe uma figura e marque medidas comparáveis entre cabeça, tronco e pernas.",
                "O que a proporção organiza?",
            ),
            lesson(
                "A proporção do corpo humano na Grécia",
                "partes",
                "A **proporção** relaciona as **partes** do corpo humano na escultura grega.",
                "Observe uma escultura grega e perceba como cabeça, tronco e membros formam um conjunto proporcional.",
                "Partes proporcionais do corpo humano",
                "O que a proporção relaciona?",
                "As partes do corpo humano na escultura grega.",
                "Somente o contorno externo sem partes relacionadas.",
                "Desenhe um corpo humano e ajuste as partes para formar um conjunto proporcional.",
                "O que a proporção relaciona?",
            ),
        ],
    },
    36: {
        "title": "A lira e a música grega",
        "term": "lira",
        "definition": "A lira é um instrumento musical de cordas e forma curva.",
        "music": "Epitáfio de Sícilo",
        "lessons": [
            lesson(
                "A lira e a música grega",
                "lira",
                "A **lira** aparece como instrumento grego de cordas e forma curva.",
                "Observe uma representação grega e identifique as cordas e a forma curva da lira.",
                "Lira grega de forma curva",
                "Como aparece a lira?",
                "Como instrumento grego de cordas e forma curva.",
                "Como instrumento sem cordas e com forma reta.",
                "Desenhe uma lira e represente suas cordas com linhas paralelas.",
                "Como aparece a lira?",
            ),
            lesson(
                "Música no teatro e na educação",
                "cordas",
                "A **lira** reúne **cordas** que acompanham música no teatro e na educação.",
                "Observe a lira em uma cena grega e conte as cordas que acompanham a música.",
                "Cordas da lira na música grega",
                "O que a lira reúne?",
                "Cordas que acompanham música no teatro e na educação.",
                "Uma moldura sem cordas em uma cena sem música.",
                "Desenhe uma lira em uma cena de teatro e destaque suas cordas.",
                "O que a lira reúne?",
            ),
            lesson(
                "O Epitáfio de Sícilo",
                "forma",
                "A **lira** mantém sua **forma** curva nas imagens da música grega.",
                "Observe uma imagem da música grega e identifique a forma curva da lira junto da notação antiga.",
                "Forma curva da lira na música grega",
                "Qual é a forma da lira?",
                "Curva, com cordas organizadas no instrumento.",
                "Reta, sem cordas organizadas no instrumento.",
                "Desenhe a forma curva de uma lira ao lado de sinais musicais antigos.",
                "Qual é a forma da lira?",
            ),
        ],
    },
    37: {
        "title": "Arte cristã primitiva e catacumbas",
        "term": "catacumba",
        "definition": "A catacumba é uma galeria subterrânea com câmaras para sepultamento.",
        "music": "Canto cristão primitivo",
        "lessons": [
            lesson(
                "Arte cristã primitiva e catacumbas",
                "catacumba",
                "A **catacumba** aparece como galeria subterrânea da arte cristã primitiva.",
                "Observe uma planta ou imagem de catacumba e identifique a galeria subterrânea da arte cristã.",
                "Galeria subterrânea da catacumba",
                "O que aparece na catacumba?",
                "Uma galeria subterrânea da arte cristã primitiva.",
                "Um palácio aberto sem galerias subterrâneas.",
                "Desenhe uma galeria subterrânea e marque suas paredes com imagens cristãs.",
                "O que aparece na catacumba?",
            ),
            lesson(
                "O Bom Pastor nas catacumbas",
                "galeria",
                "A **catacumba** reúne uma **galeria** com pinturas simples e sinais da fé cristã.",
                "Observe uma pintura do Bom Pastor e localize a galeria onde imagens cristãs foram pintadas.",
                "Galeria pintada com o Bom Pastor",
                "O que a catacumba reúne?",
                "Uma galeria com pinturas simples e sinais da fé cristã.",
                "Uma praça sem galeria, pinturas ou sinais cristãos.",
                "Desenhe o Bom Pastor em uma parede de galeria subterrânea.",
                "O que a catacumba reúne?",
            ),
            lesson(
                "Símbolos cristãos nas pinturas",
                "câmaras",
                "A **catacumba** apresenta **câmaras** com imagens do Bom Pastor e símbolos cristãos.",
                "Observe as pinturas das câmaras e identifique o Bom Pastor e outros símbolos cristãos.",
                "Câmaras com imagens e símbolos cristãos",
                "O que a catacumba apresenta?",
                "Câmaras com imagens do Bom Pastor e símbolos cristãos.",
                "Câmaras vazias sem imagens ou símbolos.",
                "Desenhe uma câmara com o Bom Pastor e um símbolo cristão na parede.",
                "O que a catacumba apresenta?",
            ),
        ],
    },
    38: {
        "title": "Arte Bizantina e ícones",
        "term": "ícone",
        "definition": "O ícone é uma imagem sagrada pintada para representar uma pessoa.",
        "music": "Canto bizantino antigo",
        "lessons": [
            lesson(
                "Arte Bizantina e ícones",
                "ícone",
                "O **ícone** aparece como imagem sagrada frontal na arte bizantina.",
                "Observe um ícone bizantino e identifique a imagem frontal, sagrada e cuidadosamente composta.",
                "Imagem frontal do ícone bizantino",
                "Como aparece o ícone?",
                "Como imagem sagrada frontal na arte bizantina.",
                "Como paisagem sem figura frontal ou sentido sagrado.",
                "Pinte uma figura frontal com fundo dourado, mantendo uma composição estável.",
                "Como aparece o ícone?",
            ),
            lesson(
                "O Cristo Pantocrator",
                "imagem",
                "O **ícone** apresenta a **imagem** de Cristo Pantocrator sobre fundo dourado.",
                "Observe o Cristo Pantocrator e identifique sua imagem frontal sobre o fundo dourado.",
                "Imagem de Cristo Pantocrator",
                "O que o ícone apresenta?",
                "A imagem de Cristo Pantocrator sobre fundo dourado.",
                "Uma paisagem sem pessoa, fundo dourado ou composição frontal.",
                "Desenhe uma imagem frontal com fundo dourado e organize seus elementos com simetria.",
                "O que o ícone apresenta?",
            ),
            lesson(
                "A Basílica de Santa Sofia",
                "sagrada",
                "O **ícone** integra a arte **sagrada** ligada à Basílica de Santa Sofia.",
                "Observe imagens da Basílica de Santa Sofia e relacione o ícone ao espaço da arte sagrada.",
                "Arte sagrada ligada a Santa Sofia",
                "A que arte o ícone pertence?",
                "À arte sagrada ligada à Basílica de Santa Sofia.",
                "À decoração secular sem espaço religioso.",
                "Desenhe um espaço sagrado com uma imagem frontal inspirada na arte bizantina.",
                "A que arte o ícone pertence?",
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
    audio_line = f"{definition} {item['paragraph']}"
    lines = [
        f"# {item['title']}", "", "## Definir", "", "[+PARAGRAPH]", "",
        f"**{definition}**", "", item["paragraph_bold"], "Veja o vídeo abaixo.", "",
        "[-PARAGRAPH]", "", "[+VIDEO][-VIDEO]", "", "[+HEADING]", "", "Atividade", "",
        "[-HEADING]", "", "[+PARAGRAPH]", "", "Leia o fato e ouça o áudio clicando abaixo.", "",
        "[-PARAGRAPH]", "", "[+ACCORDION]", "", item["title"], "", "@link_png@", "",
        "[MP3/]", "", "#VOX:", "", audio_line, "", "[MP3\\]", "", f"**{definition}**", "",
        item["paragraph_bold"], "", "[-ACCORDION]", "", "## Perceber", "", "[+PARAGRAPH]", "",
        item["perceive"], "", "[-PARAGRAPH]", "", "[+IMAGE_LABELED]", "", "@link_png@", "",
        "--", "", "49 50", "", item["hotspot"], "", "[-IMAGE_LABELED]", "", "## Recordar", "",
        "[+PARAGRAPH]", "", "Ouça e repita o fato abaixo.", "", "[-PARAGRAPH]", "", "[+STATEMENT_D]", "",
        "[MP3/]", "", "#VOX:", "", definition, "", "[MP3\\]", "", definition, "", "[-STATEMENT_D]", "",
        "[+HEADING]", "", "Hora de memorizar com música", "", "[-HEADING]", "", "[+PARAGRAPH]", "",
        "Clique abaixo para ouvir a música.", "", "[-PARAGRAPH]", "", "[+IMAGE_TEXT_ON]", "", "@link_png@", "",
        "@link_mp3@", "", week["music"], "", "[-IMAGE_TEXT_ON]", "", "## Praticar", "", "[+HEADING]", "",
        "Atividade 1", "", "[-HEADING]", "", "[+PARAGRAPH]", "", "Complete o fato abaixo com a palavra correta.", "",
        "[-PARAGRAPH]", "", "[+FILL_IN]", "", fill_sentence(definition, item["keyword"]), "", item["keyword"], "",
        "[-FILL_IN]", "", "[+HEADING]", "", "Atividade 2", "", "[-HEADING]", "", "[+MULTIPLE]", "",
        item["multiple_question"], "", f"{item['multiple_correct']} [=] true", f"{item['multiple_distractor']} [=]", "",
        "[-MULTIPLE]", "", "[+HEADING]", "", "Atividade Extra", "", "[-HEADING]", "", "[+PARAGRAPH]", "",
        "Acesse o PDF abaixo e faça a atividade com atenção.", "", "[-PARAGRAPH]", "", "[+ACTIVITY_WORKSHEET]", "",
        f"INSTRUCTION={item['activity']}", "", "[-ACTIVITY_WORKSHEET]", "", "## Narrar", "", "[+HEADING]", "",
        "Leitura", "", "[-HEADING]", "", "[+IMAGE_TEXT_ASIDE]", "", "@link_png@", "", "[MP3/]", "",
        "#VOX:", "", audio_line, "", "[MP3\\]", "", f"**{definition}**", "", item["paragraph_bold"], "",
        "[-IMAGE_TEXT_ASIDE]", "", "[+HEADING]", "", "Pergunta", "", "[-HEADING]", "", "[+PARAGRAPH]", "",
        "Responda oralmente à pergunta abaixo sobre o texto.", "", "[-PARAGRAPH]", "", "[+LIST_NUMBERED]", "",
        item["narrar_question"], "", "[-LIST_NUMBERED]",
    ]
    return "\n".join(lines)


def weekly_review(week: dict) -> str:
    lessons = week["lessons"]
    lines = [
        "# Revisão", "", "## Definir", "", "[+PARAGRAPH]", "",
        f"Nesta semana estudamos que **{week['definition']}**", "", "[-PARAGRAPH]", "", "[+HEADING]", "",
        "Atividade", "", "[-HEADING]", "", "[+IMAGE_TEXT_ON]", "", "@link_png@", "", "@link_mp3@", "",
        lessons[0]["title"], "", "[-IMAGE_TEXT_ON]", "", "## Perceber", "", "[+PARAGRAPH]", "",
        f"Observe as imagens da semana e veja como {week['term']} aparece em formas, imagens ou obras.", "",
        "[-PARAGRAPH]", "", "[+HEADING]", "", "Atividade", "", "[-HEADING]", "", "[+IMAGE_LABELED]", "",
        "@link_png@", "", "--", "", "20 50", "", lessons[0]["title"], "", "--", "", "50 50", "",
        lessons[1]["title"], "", "--", "", "80 50", "", lessons[2]["title"], "", "[-IMAGE_LABELED]", "",
        "## Recordar", "", "[+PARAGRAPH]", "", "Recorde o fato estudado durante a semana.", "", "[-PARAGRAPH]", "",
        "[+HEADING]", "", "Atividade", "", "[-HEADING]", "", "[+STATEMENT_D]", "", "[MP3/]", "", "#VOX:", "",
        week["definition"], "", "[MP3\\]", "", week["definition"], "", "[-STATEMENT_D]", "", "## [QUIZ] Praticar", "",
        "[+FILL_IN]", "", fill_sentence(week["definition"], week["term"]), "", week["term"], "", "[-FILL_IN]", "",
    ]
    for item in lessons:
        lines += [
            "[+MULTIPLE]", "", item["multiple_question"], "", f"{item['multiple_correct']} [=] true",
            f"{item['multiple_distractor']} [=]", "", "[-MULTIPLE]", "",
        ]
    return "\n".join(lines)


def weekly_exam(week: dict) -> str:
    lessons = week["lessons"]
    lines = ["# Prova", "", "[CANVAS_QUIZ]", ""]
    for item in lessons:
        lines += [
            "FILL_IN 10", "", fill_sentence(week["definition"], item["keyword"], quiz=True), "",
            f"1 [=] {item['keyword']}", "", "--", "",
        ]
    for item in lessons:
        lines += [
            "MULTIPLE_CHOICE 10", "", item["multiple_question"], "",
            f"{item['multiple_correct']} [=] true", f"{item['multiple_distractor']} [=]", "", "--", "",
        ]
    lines += [
        "MATCHING 10", "", "Relacione cada palavra ao aspecto visual estudado.", "",
        f"{week['term']} [=] {week['definition']}", f"{lessons[1]['keyword']} [=] {lessons[1]['title']}",
        f"{lessons[2]['keyword']} [=] {lessons[2]['title']}", "", "--", "", "TRUE_OR_FALSE 10", "",
        week["definition"], "", "true", "",
    ]
    return "\n".join(lines)


def bimonthly_review() -> str:
    lines = ["# Revisão", ""]
    for week in WEEKS.values():
        lines += [
            f"## {week['lessons'][0]['title']}", "", "[+PARAGRAPH]", "",
            f"Nesta semana estudamos que **{week['definition']}**", "", "[-PARAGRAPH]", "", "[+HEADING]", "",
            "Atividade", "", "[-HEADING]", "", "[+IMAGE_TEXT_ON]", "", "@link_png@", "", "@link_mp3@", "",
            week["lessons"][0]["title"], "", "[-IMAGE_TEXT_ON]", "",
        ]
    lines += ["## [QUIZ] Questões", ""]
    for index, week in enumerate(WEEKS.values()):
        if index % 2 == 0:
            lines += [
                "[+FILL_IN]", "", fill_sentence(week["definition"], week["term"]), "", week["term"], "",
                "[-FILL_IN]", "",
            ]
        else:
            item = week["lessons"][0]
            lines += [
                "[+MULTIPLE]", "", item["multiple_question"], "", f"{item['multiple_correct']} [=] true",
                f"{item['multiple_distractor']} [=]", "", "[-MULTIPLE]", "",
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
            "MULTIPLE_CHOICE 10", "", item["multiple_question"], "", f"{item['multiple_correct']} [=] true",
            f"{item['multiple_distractor']} [=]", "", "--", "",
        ]
    lines += ["MATCHING 10", "", "Relacione cada termo à definição estudada.", ""]
    for week in weeks:
        lines.append(f"{week['term']} [=] {week['definition']}")
    lines += ["", "--", "", "TRUE_OR_FALSE 10", "", weeks[-1]["definition"], "", "true", ""]
    return "\n".join(lines)


def validate() -> None:
    if list(WEEKS) != list(range(31, 39)):
        raise ValueError("as semanas devem cobrir 31 a 38")
    for number, week in WEEKS.items():
        words = week["definition"].rstrip(".").split()
        if not 8 <= len(words) <= 12:
            raise ValueError(f"definição fora do limite na semana {number}")
        if len(week["lessons"]) != 3:
            raise ValueError(f"semana sem três aulas na semana {number}")
        for item in week["lessons"]:
            if week["definition"].replace(item["keyword"], "", 1) == week["definition"]:
                raise ValueError(f"palavra-chave ausente na semana {number}: {item['keyword']}")
            if item["title"] not in item["title"]:
                raise ValueError("título inválido")


def write_all() -> None:
    validate()
    BASE.mkdir(parents=True, exist_ok=True)
    for number, week in WEEKS.items():
        for index, item in enumerate(week["lessons"], start=1):
            (BASE / f"{number}.{index}.md").write_text(regular_lesson(week, item), encoding="utf-8")
        (BASE / f"{number}.4.md").write_text(weekly_review(week), encoding="utf-8")
        (BASE / f"{number}.5.md").write_text(weekly_exam(week), encoding="utf-8")
    (BASE / "39.md").write_text(bimonthly_review(), encoding="utf-8")
    (BASE / "40.md").write_text(bimonthly_exam(), encoding="utf-8")
    print("Geradas as semanas 31–38 e os arquivos 39.md e 40.md.")


if __name__ == "__main__":
    write_all()
