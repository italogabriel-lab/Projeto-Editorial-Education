from pathlib import Path
import re


BASE = Path(
    "Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/"
    "1 Fase - Gramática/1º Ano - Introdução à Linguagem Visual e aos Elementos da Arte"
)
MACRO = BASE / "Estrutura Curricular - 1º ANO/1 - Curriculo Macro - Introdução à linguagem visual e aos elementos da arte - 1º ANO.md"

AUDIO_ID = "#FSH:0b12d715e4c741399594fccb12d4bbe2"

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
        "titles": ["A textura na arte", "As texturas lisas e ásperas", "As texturas da areia e das folhas"],
        "explanation": "A textura ajuda a criança a observar o que uma superfície parece ter ao toque. Ela aprende a representar marcas com cuidado.",
        "fill_word": "marcada",
        "focus": ["a textura na arte", "as texturas lisas e ásperas", "as texturas da areia e das folhas"],
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
        "titles": ["O espaço no papel", "O fundo, a borda e o centro", "O grande e o pequeno"],
        "explanation": "O espaço ajuda a criança a decidir onde colocar cada parte do desenho. Ela aprende a organizar tamanho, centro e borda.",
        "fill_word": "papel",
        "focus": ["o espaço no papel", "o fundo, a borda e o centro", "o grande e o pequeno"],
    },
    18: {
        "term": "Respiro",
        "definition": "Respiro equilibra espaço cheio e vazio para ordenar o desenho.",
        "titles": ["O espaço cheio e vazio", "O espaço com respiro", "O espaço da cidade no papel"],
        "explanation": "O respiro mostra que o vazio também ajuda a organizar a imagem. A criança aprende a equilibrar partes cheias e livres.",
        "fill_word": "desenho",
        "focus": ["o espaço cheio e vazio", "o espaço com respiro", "o espaço da cidade no papel"],
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
        "titles": ["O desenho com formas simples", "O círculo que vira gato", "O triângulo e o quadrado na casa"],
        "explanation": "A forma simples ajuda a criança a construir imagens reconhecíveis. Ela transforma círculo, triângulo e quadrado em desenhos organizados.",
        "fill_word": "ordem",
        "focus": ["o desenho com formas simples", "o círculo que vira gato", "o triângulo e o quadrado na casa"],
    },
    25: {
        "term": "Personagem",
        "definition": "Personagem transforma formas simples em figuras com expressão.",
        "titles": ["Os animais e personagens", "O sol como personagem", "O bicho inventado"],
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
        "term": "Esperança",
        "definition": "Esperança olha para a beleza prometida por Deus com alegria.",
        "titles": ["O céu e a esperança", "Os anjos com tinta e papel", "A visão do céu"],
        "explanation": "A esperança ajuda a criança a contemplar a beleza prometida por Deus. Ela desenha com alegria, reverência e cuidado.",
        "fill_word": "alegria",
        "focus": ["o céu e a esperança", "os anjos com tinta e papel", "a visão do céu"],
    },
    32: {
        "term": "Criação",
        "definition": "Criação mostra Deus formando luz, céus e águas com poder.",
        "titles": ["A criação da luz, dos céus e das águas", "A luz e as trevas", "Os céus e as águas"],
        "explanation": "A criação revela a ordem e o poder de Deus. A criança observa luz, céus e águas como obras boas do Criador.",
        "fill_word": "poder",
        "focus": ["a criação da luz, dos céus e das águas", "a luz e as trevas", "os céus e as águas"],
    },
    33: {
        "term": "Vida criada",
        "definition": "Vida criada mostra terra, luminares e seres vivos em ordem.",
        "titles": ["A criação da terra, dos luminares e dos seres vivos", "A terra, o sol, a lua e as estrelas", "Os peixes e as aves"],
        "explanation": "A vida criada aponta para a bondade de Deus. A criança observa terra, luminares, peixes e aves com gratidão.",
        "fill_word": "ordem",
        "focus": ["a criação da terra, dos luminares e dos seres vivos", "a terra, o sol, a lua e as estrelas", "os peixes e as aves"],
    },
    34: {
        "term": "Descanso",
        "definition": "Descanso lembra que Deus completou sua obra com perfeição.",
        "titles": ["A criação dos animais, do homem e do descanso", "Os animais e o ser humano", "O dia de Deus e o painel completo"],
        "explanation": "O descanso mostra que Deus completou sua obra de modo perfeito. A criança reúne animais, ser humano e criação em painel.",
        "fill_word": "perfeição",
        "focus": ["a criação dos animais, do homem e do descanso", "os animais e o ser humano", "o dia de Deus e o painel completo"],
    },
    35: {
        "term": "Arte e música",
        "definition": "Arte e música expressam beleza com som, cor e movimento.",
        "titles": ["A arte e a música", "A música que cria cores", "O som que dança com o pincel"],
        "explanation": "Arte e música ajudam a criança a unir escuta, cor e gesto. Ela percebe ritmo, movimento e beleza na criação artística.",
        "fill_word": "movimento",
        "focus": ["a arte e a música", "a música que cria cores", "o som que dança com o pincel"],
    },
    36: {
        "term": "Imagem musical",
        "definition": "Imagem musical mostra o que o som faz nascer na imaginação.",
        "titles": ["A imagem que a música revela", "Os olhos que escutam", "A música favorita em imagem"],
        "explanation": "A imagem musical transforma escuta em desenho. A criança aprende a imaginar com ordem e a representar sons por cores.",
        "fill_word": "imaginação",
        "focus": ["a imagem que a música revela", "os olhos que escutam", "a música favorita em imagem"],
    },
    37: {
        "term": "Encanto",
        "definition": "Encanto ajuda o olhar a perceber beleza nas obras de arte.",
        "titles": ["As obras que encantam", "Van Gogh e os girassóis", "Paul Klee e as cores da alegria"],
        "explanation": "O encanto conduz a criança a observar obras com atenção. Ela percebe cor, forma e alegria sem perder a gratidão.",
        "fill_word": "arte",
        "focus": ["as obras que encantam", "Van Gogh e os girassóis", "Paul Klee e as cores da alegria"],
    },
    38: {
        "term": "Observação",
        "definition": "Observação atenta vê detalhes e responde com gratidão.",
        "titles": ["A observação com o coração", "Os detalhes no quadro", "A obra que tocou o coração"],
        "explanation": "A observação atenta ajuda a criança a ver detalhes e narrar o que percebeu. Ela responde à beleza com gratidão.",
        "fill_word": "gratidão",
        "focus": ["a observação com o coração", "os detalhes no quadro", "a obra que tocou o coração"],
    },
}

BIMESTERS = {
    9: [6, 7, 8],
    10: [6, 7, 8],
    19: [11, 12, 13, 14, 15, 16, 17, 18],
    20: [11, 12, 13, 14, 15, 16, 17, 18],
    29: [21, 22, 23, 24, 25, 26, 27, 28],
    30: [21, 22, 23, 24, 25, 26, 27, 28],
    39: [31, 32, 33, 34, 35, 36, 37, 38],
    40: [31, 32, 33, 34, 35, 36, 37, 38],
}


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

[+MULTIPLE]

Qual frase resume a semana?

{definition} [=] true
Uma imagem não precisa de ordem nem atenção. [=]
A arte desta semana não usa observação. [=]

[-MULTIPLE]

[+MULTIPLE]

Qual aula apresentou o coração da semana?

{titles[0]} [=] true
{titles[1]} [=]
{titles[2]} [=]

[-MULTIPLE]

[+MULTIPLE]

Como podemos praticar o tema da semana?

Observando, repetindo e criando uma imagem simples. [=] true
Pulando a definição e copiando sem olhar. [=]
Deixando o papel vazio até o final. [=]

[-MULTIPLE]

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
    return f"""# Provas

[CANVAS_QUIZ]

FILL_IN 10

{definition.replace(fill_word, "[1]")}

1 [=] {fill_word}

--

MULTIPLE_CHOICE 10

Qual frase resume melhor a semana

{definition} [=] true
Uma imagem sem ordem e sem atenção. [=]
Uma atividade sem observação. [=]

--

MULTIPLE_CHOICE 10

Qual foi o termo da semana

{term} [=] true
Papel vazio. [=]
Barulho solto. [=]

--

FILL_IN 10

O termo da semana foi [1].

1 [=] {term}

--

MULTIPLE_CHOICE 10

Qual aula apresentou o coração da semana

{titles[0]} [=] true
{titles[1]} [=]
{titles[2]} [=]

--

MATCHING 10

Relacione cada aula ao foco estudado nesta semana.

{titles[0]} [=] Coração da semana
{titles[1]} [=] Primeiro desdobramento
{titles[2]} [=] Segundo desdobramento

--

TRUE_OR_FALSE 10

{definition}

true

--

MULTIPLE_CHOICE 10

Como o aluno deve praticar o tema

Com observação, repetição e uma imagem simples. [=] true
Sem olhar para o tema da semana. [=]
Com pressa e sem cuidado. [=]

--

FILL_IN 10

Complete a palavra principal da semana, [1].

1 [=] {term}

--

MULTIPLE_CHOICE 10

O que a revisão da semana deve manter

A mesma definição central da semana. [=] true
Três definições sem ligação. [=]
Títulos inventados fora do Macro. [=]
"""


def bimestral_review_text(number, weeks):
    lines = []
    for week in weeks:
        data = WEEKS[week]
        lines.append(f"- Semana {week}, {data['definition']}")
    joined = "\n".join(lines)
    first = WEEKS[weeks[0]]
    last = WEEKS[weeks[-1]]
    return f"""# Revisão bimestral

## Definir

[+PARAGRAPH]

Retome as definições do bloco e repita cada uma com atenção.

[-PARAGRAPH]

[+LIST]

{joined}

[-LIST]

## Perceber

[+PARAGRAPH]

Observe imagens das semanas estudadas e reconheça os termos principais.

[-PARAGRAPH]

[+IMAGE_LABELED]

@link_png@

--

25 50

{first['term']}

--

75 50

{last['term']}

[-IMAGE_LABELED]

## Recordar

[+STATEMENT_D]

[MP3/]

{AUDIO_ID}

{first['definition']}

[MP3\\]

{first['definition']}

[-STATEMENT_D]

## [QUIZ] Praticar

[+MULTIPLE]

Qual atitude ajuda a revisar bem?

Ouvir, repetir, observar e narrar com atenção. [=] true
Trocar os títulos do Macro por novos títulos. [=]
Esquecer as definições das semanas. [=]

[-MULTIPLE]

[+FILL_IN]

{last['definition'].replace(last['fill_word'], "_____")}

{last['fill_word']}

[-FILL_IN]

## Narrar

[+PARAGRAPH]

Conte uma definição do bloco e explique uma imagem que você observou.

[-PARAGRAPH]
"""


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

Qual termo pertence ao bloco estudado

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

Como a prova deve avaliar o aluno

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
