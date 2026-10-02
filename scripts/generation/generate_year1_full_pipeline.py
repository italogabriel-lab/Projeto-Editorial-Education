from pathlib import Path
import re


BASE = Path(
    "Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/"
    "1 Fase - Gramática/1º Ano - Introdução à Linguagem Visual e aos Elementos da Arte"
)
MACRO = BASE / "Estrutura Curricular - 1º ANO/1 - Curriculo Macro - Introdução à linguagem visual e aos elementos da arte - 1º ANO.md"

AUDIO_ID = "#VOX:"

WEEKS = {
    6: {
        "term": "Caminho",
        "definition": "Caminho é linha que conduz o olhar por onde o desenho passa.",
        "titles": ["A linha como caminho", "A linha que acompanha o som", "A linha que cria trilhas"],
        "explanation": "A linha como caminho ajuda a criança a seguir um percurso visual. Ela aprende a desenhar com atenção, movimento e gratidão pela ordem criada por Deus.",
        "fill_word": "passa",
        "focus": ["o percurso da linha", "a linha que acompanha o som", "a trilha criada pela linha"],
    },
    7: {
        "term": "Forma",
        "definition": "Forma organiza linhas fechadas para mostrar figuras no desenho.",
        "titles": ["As formas no desenho", "O círculo, o quadrado e o triângulo", "As formas que criam imagens"],
        "explanation": "A forma nasce quando a linha fecha um espaço no papel. A criança reconhece figuras simples e aprende a criar imagens com ordem e beleza.",
        "fill_word": "desenho",
        "focus": ["as formas no desenho", "o círculo, o quadrado e o triângulo", "as formas que criam imagens"],
    },
    8: {
        "term": "Forma natural",
        "definition": "Forma natural mostra figuras criadas por Deus na natureza.",
        "titles": ["As formas na natureza", "As formas em bichos", "As formas em figuras inventadas"],
        "explanation": "A forma natural aparece nas folhas, nos animais e em muitas partes da criação. A criança observa antes de inventar e desenha com gratidão.",
        "fill_word": "natureza",
        "focus": ["as formas na natureza", "as formas em bichos", "as figuras inventadas"],
    },
    11: {
        "term": "Cor primária",
        "definition": "Cor primária inicia misturas e ajuda outras cores a nascer.",
        "titles": ["As cores primárias", "O vermelho, o azul e o amarelo", "As cores que nascem da mistura"],
        "explanation": "A cor primária ajuda a criança a perceber começo, mistura e variedade. Ela observa vermelho, azul e amarelo como cores importantes na arte.",
        "fill_word": "nascer",
        "focus": ["as cores primárias", "o vermelho, o azul e o amarelo", "as cores que nascem da mistura"],
    },
    12: {
        "term": "Cor expressiva",
        "definition": "Cor expressiva mostra sentimentos com beleza, ordem e cuidado.",
        "titles": ["As cores e as emoções", "Cores que acalmam e agitam", "Cores quentes e frias"],
        "explanation": "A cor expressiva ajuda a criança a perceber alegria, calma e movimento. Ela aprende a escolher cores com cuidado e propósito.",
        "fill_word": "cuidado",
        "focus": ["as cores e as emoções", "as cores que acalmam e agitam", "as cores quentes e frias"],
    },
    13: {
        "term": "Cor musical",
        "definition": "Cor musical acompanha o som e expressa sentimento na arte.",
        "titles": ["A cor e a música", "A cor que acompanha o som", "A cor que expressa sentimento"],
        "explanation": "A cor musical une escuta e observação. A criança percebe que sons podem inspirar escolhas de cor, ritmo e expressão visual.",
        "fill_word": "arte",
        "focus": ["a cor e a música", "a cor que acompanha o som", "a cor que expressa sentimento"],
    },
    14: {
        "term": "Luz",
        "definition": "Luz muda as cores do dia e da noite com beleza.",
        "titles": ["As cores do dia e da noite", "As cores da luz do sol", "As cores da noite"],
        "explanation": "A luz ajuda a criança a perceber mudanças de cor no dia e na noite. Ela observa a criação com atenção e gratidão.",
        "fill_word": "beleza",
        "focus": ["as cores do dia e da noite", "as cores da luz do sol", "as cores da noite"],
    },
    15: {
        "term": "Textura",
        "definition": "Textura mostra se a superfície parece lisa, áspera ou marcada.",
        "titles": ["A textura na arte", "As texturas lisas e ásperas", "A textura marcada na arte"],
        "explanation": "A textura ajuda a criança a observar o que uma superfície parece ter ao toque. Ela aprende a representar marcas com cuidado.",
        "fill_word": "marcada",
        "focus": ["a textura na arte", "as texturas lisas e ásperas", "a textura marcada na arte"],
    },
    16: {
        "term": "Textura expressiva",
        "definition": "Textura expressiva comunica sentimento por marcas, massas e materiais.",
        "titles": ["A textura e o sentimento", "A textura feita com massa", "A textura feita com elementos naturais"],
        "explanation": "A textura expressiva usa marcas e materiais para comunicar sentimento. A criança cria com as mãos e observa a beleza das superfícies.",
        "fill_word": "materiais",
        "focus": ["a textura e o sentimento", "a textura feita com massa", "a textura feita com elementos naturais"],
    },
    17: {
        "term": "Espaço",
        "definition": "Espaço organiza fundo, borda e centro dentro do papel.",
        "titles": ["O espaço no papel", "O fundo e a borda no papel", "O centro no papel"],
        "explanation": "O espaço ajuda a criança a decidir onde colocar cada parte do desenho. Ela aprende a organizar fundo, borda e centro.",
        "fill_word": "papel",
        "focus": ["o espaço no papel", "o fundo e a borda no papel", "o centro no papel"],
    },
    18: {
        "term": "Tamanho",
        "definition": "Tamanho é a medida visual de uma forma na obra.",
        "titles": ["O tamanho na arte", "O grande e o pequeno", "O tamanho que chama atenção"],
        "explanation": "O tamanho mostra se uma forma aparece grande ou pequena na obra. A criança aprende a comparar medidas visuais e a perceber destaque.",
        "fill_word": "forma",
        "focus": ["o tamanho na arte", "o grande e o pequeno", "o tamanho que chama atenção"],
    },
    21: {
        "term": "Direção",
        "definition": "Direção guia o olhar e conduz a história na imagem.",
        "titles": ["A direção no olhar", "A seta que guia a história", "O caminho feito com pincel"],
        "explanation": "A direção ajuda a criança a entender para onde olhar primeiro. Ela usa setas, linhas e caminhos para organizar histórias visuais.",
        "fill_word": "imagem",
        "focus": ["a direção no olhar", "a seta que guia a história", "o caminho feito com pincel"],
    },
    22: {
        "term": "Equilíbrio",
        "definition": "Equilíbrio organiza partes diferentes para a obra ficar firme e bela.",
        "titles": ["O equilíbrio na arte", "O equilíbrio da dobradura", "O equilíbrio da simetria"],
        "explanation": "O equilíbrio ajuda a criança a perceber peso visual, dobra e simetria. Ela cria com ordem e cuidado diante da beleza.",
        "fill_word": "bela",
        "focus": ["o equilíbrio na arte", "o equilíbrio da dobradura", "o equilíbrio da simetria"],
    },
    23: {
        "term": "Composição",
        "definition": "Composição une ponto, linha, forma, cor e espaço com ordem.",
        "titles": ["A obra com os elementos da arte", "O quadro com formas e cores", "A obra com ponto, linha e espaço"],
        "explanation": "A composição reúne os elementos visuais em uma obra. A criança aprende a organizar ponto, linha, forma, cor e espaço.",
        "fill_word": "ordem",
        "focus": ["a obra com os elementos da arte", "o quadro com formas e cores", "a obra com ponto, linha e espaço"],
    },
    24: {
        "term": "Forma simples",
        "definition": "Forma simples ajuda o desenho a nascer com clareza e ordem.",
        "titles": ["O desenho com formas simples", "O círculo que dar origem a imagen", "O triângulo e o quadrado na casa"],
        "explanation": "A forma simples ajuda a criança a construir imagens reconhecíveis. Ela transforma círculo, triângulo e quadrado em desenhos organizados.",
        "fill_word": "ordem",
        "focus": ["o desenho com formas simples", "o círculo que vira gato", "o triângulo e o quadrado na casa"],
    },
    25: {
        "term": "Personagem",
        "definition": "Personagem transforma formas simples em figuras com expressão.",
        "titles": ["O personagem na obra de arte", "A figura que ganha rosto", "O personagem inventado"],
        "explanation": "O personagem ajuda a criança a criar figuras com expressão. Ela usa formas simples para desenhar animais, sol e seres inventados.",
        "fill_word": "expressão",
        "focus": ["os animais e personagens", "o sol como personagem", "o bicho inventado"],
    },
    26: {
        "term": "Mundo desenhado",
        "definition": "Mundo desenhado mostra lugares queridos com ordem, beleza e gratidão.",
        "titles": ["O meu mundo em desenho", "A minha casa no desenho", "O meu cantinho favorito"],
        "explanation": "O mundo desenhado ajuda a criança a representar lugares importantes. Ela observa casa, cantinho e memória com cuidado.",
        "fill_word": "gratidão",
        "focus": ["o meu mundo em desenho", "a minha casa no desenho", "o meu cantinho favorito"],
    },
    27: {
        "term": "Lugar",
        "definition": "Lugar desenhado mostra espaços e histórias com formas e cores.",
        "titles": ["Os lugares e histórias", "A igreja com torres", "O parquinho colorido"],
        "explanation": "O lugar desenhado une espaço, memória e história. A criança observa torres, caminhos e cores para organizar uma cena.",
        "fill_word": "cores",
        "focus": ["os lugares e histórias", "a igreja com torres", "o parquinho colorido"],
    },
    28: {
        "term": "História",
        "definition": "História inspira imagens que ajudam a lembrar fatos importantes.",
        "titles": ["As histórias que inspiram a arte", "A arca com muitos animais", "O jardim da criação"],
        "explanation": "A história inspira a criança a transformar lembranças em imagens. Ela desenha fatos importantes com ordem, beleza e reverência.",
        "fill_word": "importantes",
        "focus": ["as histórias que inspiram a arte", "a arca com muitos animais", "o jardim da criação"],
    },
    31: {
        "term": 'Composição',
        "definition": 'Composição é ordem e equilíbrio dos elementos visuais na imagem.',
        "titles": ['A composição na arte', 'O equilíbrio na imagem', 'A ordem na página'],
        "explanation": 'A composição organiza linhas, formas e cores para formar uma imagem clara. Ela usa equilíbrio e ordem para colocar cada parte no lugar certo da página.',
        "fill_word": 'Composição',
        "focus": ['a composição na arte', 'o equilíbrio na imagem', 'a ordem na página'],
    },
    32: {
        "term": 'Criação',
        "definition": 'Criação é obra de Deus com luz e brilho no céu.',
        "titles": ['A criação da luz, dos céus e das águas', 'A luz que nasce', 'O brilho do céu'],
        "explanation": 'A criação mostra a luz, os céus e as águas como obra boa de Deus. Ela permite observar claridade, trevas e brilho com cores luminosas.',
        "fill_word": 'Criação',
        "focus": ['a criação da luz, dos céus e das águas', 'a luz que nasce', 'o brilho do céu'],
    },
    33: {
        "term": 'Vida criada',
        "definition": 'Vida criada é ordem de terra, céu e movimento vivo.',
        "titles": ['A criação da terra, dos luminares e dos seres vivos', 'A terra e o céu', 'A vida em movimento'],
        "explanation": 'A vida criada mostra terra, céu e seres vivos em uma cena ordenada. Ela aparece em movimento nos peixes, aves e animais desenhados.',
        "fill_word": 'Vida criada',
        "focus": ['a criação da terra, dos luminares e dos seres vivos', 'a terra e o céu', 'a vida em movimento'],
    },
    34: {
        "term": 'Descanso',
        "definition": 'Descanso é paz depois da obra criada por Deus.',
        "titles": ['A criação dos animais, do homem e do descanso', 'O homem e a obra', 'O descanso e a paz'],
        "explanation": 'O descanso lembra animais, homem e criação como obra completa de Deus. Ele mostra paz quando a imagem apresenta a obra criada com cuidado.',
        "fill_word": 'Descanso',
        "focus": ['a criação dos animais, do homem e do descanso', 'o homem e a obra', 'o descanso e a paz'],
    },
    35: {
        "term": 'Arte e música',
        "definition": 'Arte e música é beleza em som, cor e imagem.',
        "titles": ['A arte e a música', 'O som que inspira', 'A música em imagem'],
        "explanation": 'A arte e música unem som, cor e movimento em uma expressão bela. Elas transformam a escuta em imagem com formas e cores.',
        "fill_word": 'Arte e música',
        "focus": ['a arte e a música', 'o som que inspira', 'a música em imagem'],
    },
    36: {
        "term": 'Imagem musical',
        "definition": 'Imagem musical é som transformado em movimento, cor e desenho.',
        "titles": ['A imagem que a música revela', 'O som que se transforma', 'A música em movimento'],
        "explanation": 'A imagem musical revela cores e formas que a música desperta na imaginação. Ela mostra movimento quando a mão acompanha a música no papel.',
        "fill_word": 'Imagem musical',
        "focus": ['a imagem que a música revela', 'o som que se transforma', 'a música em movimento'],
    },
    37: {
        "term": 'Encanto',
        "definition": 'Encanto é beleza percebida em forma, cor e obra.',
        "titles": ['As obras que encantam', 'O encanto da forma', 'A beleza na obra'],
        "explanation": 'O encanto ajuda o olhar a perceber beleza nas obras de arte. Ele aparece quando forma, cor e obra prendem o olhar com atenção.',
        "fill_word": 'Encanto',
        "focus": ['as obras que encantam', 'o encanto da forma', 'a beleza na obra'],
    },
    38: {
        "term": 'Observação',
        "definition": 'Observação é olhar atento que vê beleza na obra.',
        "titles": ['A observação com o coração', 'O olhar atento', 'A beleza que se vê'],
        "explanation": 'A observação com o coração vê detalhes da obra com atenção e gratidão. Ela educa o olhar para encontrar beleza em cores, formas e detalhes.',
        "fill_word": 'Observação',
        "focus": ['a observação com o coração', 'o olhar atento', 'a beleza que se vê'],
    },
}

BIMESTERS = {
    9: [1, 2, 3, 4, 5, 6, 7, 8],
    10: [6, 7, 8],
    19: [11, 12, 13, 14, 15, 16, 17, 18],
    20: [11, 12, 13, 14, 15, 16, 17, 18],
    29: [21, 22, 23, 24, 25, 26, 27, 28],
    30: [21, 22, 23, 24, 25, 26, 27, 28],
    39: [31, 32, 33, 34, 35, 36, 37, 38],
    40: [31, 32, 33, 34, 35, 36, 37, 38],
}


def title_in_sentence(title):
    if title.startswith(("A ", "As ", "O ", "Os ")):
        return title[0].lower() + title[1:]
    return title


def first_multiple_from_lesson(week, lesson_number):
    path = BASE / f"{week}.{lesson_number}.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    match = re.search(r"\[\+MULTIPLE\](.*?)\[-MULTIPLE\]", text, re.S)
    if not match:
        return None
    lines = [line.strip() for line in match.group(1).splitlines() if line.strip()]
    if len(lines) < 3:
        return None
    choices = lines[1:]
    while len(choices) < 3:
        choices.append("Uma folha vazia sem forma. [=]")
    return lines[0], choices[:3]


def review_multiple_sections(number, data):
    sections = []
    for lesson_number in (1, 2, 3):
        multiple = first_multiple_from_lesson(number, lesson_number)
        if multiple:
            question, choices = multiple
        else:
            title = data["titles"][lesson_number - 1]
            focus = data["focus"][lesson_number - 1]
            question = f"O que {title_in_sentence(title)} mostra no tema estudado?"
            choices = [
                f"{focus.capitalize()}. [=] true",
                "Uma imagem sem ordem nem cuidado. [=]",
                "Uma folha vazia sem forma. [=]",
            ]
        sections.append(
            "[+MULTIPLE]\n\n"
            f"{question}\n\n"
            + "\n".join(choices)
            + "\n\n[-MULTIPLE]"
        )
    return "\n\n".join(sections)


def lesson_text(number, index, data):
    title = data["titles"][index - 1]
    definition = data["definition"]
    term = data["term"]
    focus = data["focus"][index - 1]
    explanation = data["explanation"]
    audio_explanation = f"O termo da semana é {term}. {explanation}"
    visual_explanation = f"O termo da semana é **{term}**. {explanation}"
    fill_word = data["fill_word"]
    music = data["titles"][0]
    hotspot = ["38 48", "50 50", "62 48"][index - 1]
    worksheet = {
        1: f"Desenhe {focus} e mantenha a imagem simples e organizada.",
        2: f"Observe {focus} e destaque esse detalhe no desenho.",
        3: f"Crie uma imagem com {focus} e conte o que você fez.",
    }[index]
    return f"""# {title}

## Definir

[+PARAGRAPH]

**{definition}**

{visual_explanation}

Veja o vídeo abaixo.

[-PARAGRAPH]

[+VIDEO][-VIDEO]

[+HEADING]

Atividade

[-HEADING]

[+PARAGRAPH]

Leia a definição e ouça o áudio clicando abaixo.

[-PARAGRAPH]

[+ACCORDION]

{title}

@link_png@

[MP3/]

{AUDIO_ID}

{definition}

{audio_explanation}

[MP3\\]

**{definition}**

{visual_explanation}

[-ACCORDION]

## Perceber

[+PARAGRAPH]

Observe {focus} e veja como isso ajuda a imagem.

[-PARAGRAPH]

[+IMAGE_LABELED]

@link_png@

--

{hotspot}

{focus.capitalize()}

[-IMAGE_LABELED]

## Recordar

[+PARAGRAPH]

Ouça e repita a definição abaixo.

[-PARAGRAPH]

[+STATEMENT_D]

[MP3/]

{AUDIO_ID}

{definition}

[MP3\\]

{definition}

[-STATEMENT_D]

[+HEADING]

Hora de memorizar com música

[-HEADING]

[+PARAGRAPH]

Clique abaixo para ouvir a música.

[-PARAGRAPH]

[+IMAGE_TEXT_ON]

@link_png@

@link_mp3@

{music}

[-IMAGE_TEXT_ON]

## Praticar

[+HEADING]

Atividade 1

[-HEADING]

[+PARAGRAPH]

Complete a definição abaixo com a palavra correta.

[-PARAGRAPH]

[+FILL_IN]

{definition.replace(fill_word, "_____")}

{fill_word}

[-FILL_IN]

[+HEADING]

Atividade 2

[-HEADING]

[+MULTIPLE]

O que estudamos nesta aula?

{definition} [=] true
Uma imagem sem ordem e sem atenção. [=]

[-MULTIPLE]

[+HEADING]

Atividade Extra

[-HEADING]

[+PARAGRAPH]

Acesse o PDF abaixo para imprimir a atividade.

[-PARAGRAPH]

[+ACTIVITY_WORKSHEET]

INSTRUCTION={worksheet}

[-ACTIVITY_WORKSHEET]

## Narrar

[+HEADING]

Leitura

[-HEADING]

[+IMAGE_TEXT_ASIDE]

@link_png@

[MP3/]

{AUDIO_ID}

{definition}

{audio_explanation}

[MP3\\]

**{definition}**

{visual_explanation}

[-IMAGE_TEXT_ASIDE]

[+HEADING]

Pergunta

[-HEADING]

[+PARAGRAPH]

Responda oralmente a pergunta abaixo sobre o texto.

[-PARAGRAPH]

[+LIST_NUMBERED]

O que você percebeu sobre {focus}?

[-LIST_NUMBERED]
"""


def weekly_review_text(number, data):
    definition = data["definition"]
    titles = data["titles"]
    fill_word = data["fill_word"]
    multiples = review_multiple_sections(number, data)
    return f"""# Revisão

## Definir

[+PARAGRAPH]

Nesta semana estudamos que **{definition.lower()}**

[-PARAGRAPH]

[+HEADING]

Atividade

[-HEADING]

[+IMAGE_TEXT_ON]

@link_png@

@link_mp3@

{titles[0]}

[-IMAGE_TEXT_ON]

## Perceber

[+PARAGRAPH]

Observe as imagens que estudamos durante a semana.

[-PARAGRAPH]

[+HEADING]

Atividade

[-HEADING]

[+IMAGE_LABELED]

@link_png@

--

20 50

{titles[0]}

--

50 50

{titles[1]}

--

80 50

{titles[2]}

[-IMAGE_LABELED]

## Recordar

[+PARAGRAPH]

Recorde agora o fato aprendido durante a semana.

[-PARAGRAPH]

[+HEADING]

Atividade

[-HEADING]

[+STATEMENT_D]

[MP3/]

{AUDIO_ID}

{definition}

[MP3\\]

{definition}

[-STATEMENT_D]

## [QUIZ] Praticar

[+FILL_IN]

{definition.replace(fill_word, "_____")}

{fill_word}

[-FILL_IN]

{multiples}

## Narrar

[+PARAGRAPH]

Agora é hora de contar exatamente o fato que você aprendeu esta semana.

[-PARAGRAPH]
"""


def weekly_test_text(number, data):
    definition = data["definition"]
    titles = data["titles"]
    fill_word = data["fill_word"]
    term = data["term"]
    focus = data["focus"]
    term_fill = definition.replace(term, "[1]", 1)
    if term_fill == definition:
        term_fill = definition.replace(fill_word, "[1]", 1)
    return f"""# Provas

[CANVAS_QUIZ]

FILL_IN 10

{definition.replace(fill_word, "[1]")}

1 [=] {fill_word}

--

MULTIPLE_CHOICE 10

O que aparece em {title_in_sentence(titles[0])}?

{focus[0].capitalize()}. [=] true
Uma imagem sem ordem e sem atenção. [=]
Uma atividade sem observar o conteúdo estudado. [=]

--

MULTIPLE_CHOICE 10

O que aparece em {title_in_sentence(titles[1])}?

{focus[1].capitalize()}. [=] true
Uma folha vazia sem relação com o tema. [=]
Um desenho feito sem atenção ao conteúdo. [=]

--

FILL_IN 10

{term_fill}

1 [=] {term}

--

MULTIPLE_CHOICE 10

O que aparece em {title_in_sentence(titles[2])}?

{focus[2].capitalize()}. [=] true
Uma atividade feita sem observar o tema. [=]
Uma figura sem ordem nem cuidado. [=]

--

MATCHING 10

Relacione cada assunto ao que ele mostra.

{titles[0]} [=] {focus[0].capitalize()}.
{titles[1]} [=] {focus[1].capitalize()}.
{titles[2]} [=] {focus[2].capitalize()}.

--

TRUE_OR_FALSE 10

{definition}

true

--

MULTIPLE_CHOICE 10

Qual ideia combina com {title_in_sentence(titles[1])}?

{focus[1].capitalize()}. [=] true
Uma folha vazia sem relação com o tema. [=]
Um desenho feito sem atenção ao conteúdo. [=]

--

FILL_IN 10

{definition.replace(fill_word, "[1]")}

1 [=] {fill_word}

--

MULTIPLE_CHOICE 10

Qual ideia combina com {title_in_sentence(titles[2])}?

{focus[2].capitalize()}. [=] true
Uma atividade feita sem observar o tema. [=]
Uma figura sem ordem nem cuidado. [=]
"""


def existing_lesson_title(week):
    path = BASE / f"{week}.1.md"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line.replace("# ", "", 1).strip()
    return WEEKS[week]["titles"][0]


def existing_week_definition(week):
    path = BASE / f"{week}.1.md"
    if path.exists():
        lines = path.read_text(encoding="utf-8").splitlines()
        try:
            start = lines.index("## Definir")
        except ValueError:
            start = 0
        for line in lines[start : start + 30]:
            match = re.match(r"^\*\*(.+)\*\*$", line.strip())
            if match:
                return match.group(1).strip()
    return WEEKS[week]["definition"]


def embedded_definition(week):
    definition = existing_week_definition(week)
    return definition[:1].lower() + definition[1:]


def existing_review_fill_in(week):
    path = BASE / f"{week}.4.md"
    if path.exists():
        lines = path.read_text(encoding="utf-8").splitlines()
        try:
            start = lines.index("[+FILL_IN]")
            end = lines.index("[-FILL_IN]", start)
            return "\n".join(lines[start : end + 1])
        except ValueError:
            pass
    data = WEEKS[week]
    return f"""[+FILL_IN]

{data['definition'].replace(data['fill_word'], "_____")}

{data['fill_word']}

[-FILL_IN]"""


def existing_review_multiple(week):
    path = BASE / f"{week}.4.md"
    if path.exists():
        lines = path.read_text(encoding="utf-8").splitlines()
        try:
            start = lines.index("[+MULTIPLE]")
            end = lines.index("[-MULTIPLE]", start)
            return "\n".join(lines[start : end + 1])
        except ValueError:
            pass
    data = WEEKS[week]
    return f"""[+MULTIPLE]

O que {data['term']} representa?

{data['definition']} [=] true
Título inventado fora do Macro. [=]

[-MULTIPLE]"""


def bimestral_review_text(number, weeks):
    blocks = []
    for week in weeks:
        title = existing_lesson_title(week)
        blocks.append(f"""# {title}

[+PARAGRAPH]

Nesta semana estudamos que **{embedded_definition(week)}**

[-PARAGRAPH]

[+HEADING]

Atividade

[-HEADING]

[+IMAGE_TEXT_ON]

@link_png@

@link_mp3@

{title}

[-IMAGE_TEXT_ON]""")
    # Quiz alterna por semana: posição ímpar (1ª, 3ª, 5ª, 7ª) usa FILL_IN,
    # posição par (2ª, 4ª, 6ª, 8ª) usa MULTIPLE. Sempre começa com FILL_IN.
    # Resultado: 4 FILL_IN + 4 MULTIPLE, uma questão por semana.
    questions = []
    for position, week in enumerate(weeks):
        if position % 2 == 0:
            questions.append(existing_review_fill_in(week))
        else:
            questions.append(existing_review_multiple(week))
    return "\n\n".join(["# Revisão bimestral", *blocks, "## [QUIZ] Questões", *questions]) + "\n"


def bimestral_test_text(number, weeks):
    items = []
    for week in weeks[:3]:
        data = WEEKS[week]
        items.append(f"{data['term']} [=] {data['definition']}")
    matching = "\n".join(items)
    first = WEEKS[weeks[0]]
    second = WEEKS[weeks[1]]
    last = WEEKS[weeks[-1]]
    return f"""# Prova bimestral

[CANVAS_QUIZ]

FILL_IN 10

{first['definition'].replace(first['fill_word'], "[1]")}

1 [=] {first['fill_word']}

--

MULTIPLE_CHOICE 10

Qual termo pertence ao bloco estudado?

{second['term']} [=] true
Título inventado. [=]
Assunto fora do Macro. [=]

--

MATCHING 10

Relacione cada termo à definição estudada.

{matching}

--

TRUE_OR_FALSE 10

{last['definition']}

true

--

MULTIPLE_CHOICE 10

Como a prova deve avaliar o aluno?

Com definições, observação visual e narração simples. [=] true
Com temas fora do currículo Macro. [=]
Com frases longas e confusas. [=]
"""


def write_regular_weeks():
    for week, data in WEEKS.items():
        for index in (1, 2, 3):
            (BASE / f"{week}.{index}.md").write_text(lesson_text(week, index, data), encoding="utf-8")
        (BASE / f"{week}.4.md").write_text(weekly_review_text(week, data), encoding="utf-8")
        (BASE / f"{week}.5.md").write_text(weekly_test_text(week, data), encoding="utf-8")


def write_bimestral_weeks():
    for week, weeks in BIMESTERS.items():
        if week in (9, 19, 29, 39):
            (BASE / f"{week}.md").write_text(bimestral_review_text(week, weeks), encoding="utf-8")
        else:
            (BASE / f"{week}.md").write_text(bimestral_test_text(week, weeks), encoding="utf-8")


def update_macro():
    text = MACRO.read_text(encoding="utf-8")
    for week, data in WEEKS.items():
        text = re.sub(rf"(## Semana {week} - .+?)( ✅)?$", r"\1 ✅", text, flags=re.MULTILINE)
        for index, title in enumerate(data["titles"], start=1):
            text = re.sub(rf"(- {week}\.{index} {re.escape(title)})( ✅)?$", r"\1 ✅", text, flags=re.MULTILINE)
        block = f"# Semana {week}\n{data['term']} ✅"
        if block not in text:
            pattern = rf"(## Semana {week} - .+? ✅\n\n(?:- {week}\.[123] .+? ✅\n)+)"
            text = re.sub(pattern, rf"\1\n{block}\n", text, flags=re.MULTILINE)
    review_labels = {
        9: "9 Revisão",
        10: "10 Provas",
        19: "19\tRevisão",
        20: "20\tProvas",
        29: "29\tRevisão",
        30: "30\tProvas",
        39: "39\tRevisão",
        40: "40\tProvas",
    }
    for label in review_labels.values():
        text = text.replace(label, f"{label} ✅")
        text = text.replace(f"{label} ✅ ✅", f"{label} ✅")
    MACRO.write_text(text, encoding="utf-8")


def main():
    write_regular_weeks()
    write_bimestral_weeks()
    update_macro()
    print(f"Generated {len(WEEKS) * 5 + len(BIMESTERS)} files")


if __name__ == "__main__":
    main()
