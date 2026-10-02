#!/usr/bin/env python3
"""Gera aulas do 2º ano em etapas, conforme os dados editoriais aprovados."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / (
    "Projeto - Bibline Academy ( Produção de Aulas)/"
    "Belas Artes - Fase da Gramática/1 Fase - Gramática/"
    "2º Ano - DA CRIAÇÃO ATÉ A ARTE BIZANTINA/Aulas"
)


LESSONS = {
    (21, 1): {
        "titulo": "A Mesopotâmia e suas cidades",
        "definicao": "O zigurate é uma torre escalonada que forma um templo antigo.",
        "paragrafo": "O zigurate aparece como uma torre escalonada que domina a cidade mesopotâmica.",
        "paragrafo_bold": "O **zigurate** aparece como uma torre escalonada que domina a cidade mesopotâmica.",
        "perceber": "Observe a imagem de uma cidade mesopotâmica e identifique o zigurate como torre escalonada central.",
        "hotspot": "Zigurate no centro da cidade",
        "musica": "Ritmos antigos e sons da natureza",
        "fill_in": "O _____ é uma torre escalonada que forma um templo antigo.",
        "fill_resposta": "zigurate",
        "multiple_pergunta": "Onde o zigurate aparece?",
        "multiple_correta": "Na cidade mesopotâmica como torre escalonada central.",
        "multiple_distrator": "Em uma pintura moderna sem templo.",
        "atividade": "Desenhe uma cidade mesopotâmica e destaque o zigurate.",
        "narrar_pergunta": "Como o zigurate aparece?",
    },
    (21, 2): {
        "titulo": "O zigurate como templo",
        "definicao": "O zigurate é uma torre escalonada que forma um templo antigo.",
        "paragrafo": "O zigurate eleva o templo em níveis visuais e o destaca no centro da cidade mesopotâmica.",
        "paragrafo_bold": "O **zigurate** eleva o **templo** em níveis visuais e o destaca no centro da cidade mesopotâmica.",
        "perceber": "Observe os níveis do zigurate e veja como o templo se destaca no centro da cidade mesopotâmica.",
        "hotspot": "Níveis do zigurate e templo",
        "musica": "Ritmos antigos e sons da natureza",
        "fill_in": "O zigurate é uma torre escalonada que forma um _____ antigo.",
        "fill_resposta": "templo",
        "multiple_pergunta": "Onde o zigurate eleva o templo?",
        "multiple_correta": "No centro da cidade mesopotâmica.",
        "multiple_distrator": "No fundo de uma pintura moderna.",
        "atividade": "Desenhe os níveis do zigurate e destaque o templo no alto.",
        "narrar_pergunta": "Como o zigurate destaca o templo?",
    },
}


def render_lesson(data: dict) -> str:
    title = data["titulo"]
    definition = data["definicao"]
    paragraph = data["paragrafo"]
    paragraph_bold = data["paragrafo_bold"]
    audio_line = f"{definition} {paragraph}"
    visual_line = f"**{definition}**"

    lines = [
        f"# {title}",
        "",
        "## Definir",
        "",
        "[+PARAGRAPH]",
        "",
        f"**{definition}**",
        "",
        paragraph_bold,
        "Veja o vídeo abaixo.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+VIDEO][-VIDEO]",
        "",
        "[+HEADING]",
        "",
        "Atividade",
        "",
        "[-HEADING]",
        "",
        "[+PARAGRAPH]",
        "",
        "Leia o fato e ouça o áudio clicando abaixo.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+ACCORDION]",
        "",
        title,
        "",
        "@link_png@",
        "",
        "[MP3/]",
        "",
        "#VOX:",
        "",
        audio_line,
        "",
        "[MP3\\]",
        "",
        visual_line,
        "",
        paragraph_bold,
        "",
        "[-ACCORDION]",
        "",
        "## Perceber",
        "",
        "[+PARAGRAPH]",
        "",
        data["perceber"],
        "",
        "[-PARAGRAPH]",
        "",
        "[+IMAGE_LABELED]",
        "",
        "@link_png@",
        "",
        "--",
        "",
        "49 50",
        "",
        data["hotspot"],
        "",
        "[-IMAGE_LABELED]",
        "",
        "## Recordar",
        "",
        "[+PARAGRAPH]",
        "",
        "Ouça e repita o fato abaixo.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+STATEMENT_D]",
        "",
        "[MP3/]",
        "",
        "#VOX:",
        "",
        definition,
        "",
        "[MP3\\]",
        "",
        definition,
        "",
        "[-STATEMENT_D]",
        "",
        "[+HEADING]",
        "",
        "Hora de memorizar com música",
        "",
        "[-HEADING]",
        "",
        "[+PARAGRAPH]",
        "",
        "Clique abaixo para ouvir a música.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+IMAGE_TEXT_ON]",
        "",
        "@link_png@",
        "",
        "@link_mp3@",
        "",
        data["musica"],
        "",
        "[-IMAGE_TEXT_ON]",
        "",
        "## Praticar",
        "",
        "[+HEADING]",
        "",
        "Atividade 1",
        "",
        "[-HEADING]",
        "",
        "[+PARAGRAPH]",
        "",
        "Complete o fato abaixo com a palavra correta.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+FILL_IN]",
        "",
        data["fill_in"],
        "",
        data["fill_resposta"],
        "",
        "[-FILL_IN]",
        "",
        "[+HEADING]",
        "",
        "Atividade 2",
        "",
        "[-HEADING]",
        "",
        "[+MULTIPLE]",
        "",
        data["multiple_pergunta"],
        "",
        f"{data['multiple_correta']} [=] true",
        f"{data['multiple_distrator']} [=]",
        "",
        "[-MULTIPLE]",
        "",
        "[+HEADING]",
        "",
        "Atividade Extra",
        "",
        "[-HEADING]",
        "",
        "[+PARAGRAPH]",
        "",
        "Acesse o PDF abaixo e faça a atividade com atenção.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+ACTIVITY_WORKSHEET]",
        "",
        f"INSTRUCTION={data['atividade']}",
        "",
        "[-ACTIVITY_WORKSHEET]",
        "",
        "## Narrar",
        "",
        "[+HEADING]",
        "",
        "Leitura",
        "",
        "[-HEADING]",
        "",
        "[+IMAGE_TEXT_ASIDE]",
        "",
        "@link_png@",
        "",
        "[MP3/]",
        "",
        "#VOX:",
        "",
        audio_line,
        "",
        "[MP3\\]",
        "",
        visual_line,
        "",
        paragraph_bold,
        "",
        "[-IMAGE_TEXT_ASIDE]",
        "",
        "[+HEADING]",
        "",
        "Pergunta",
        "",
        "[-HEADING]",
        "",
        "[+PARAGRAPH]",
        "",
        "Responda oralmente à pergunta abaixo sobre o texto.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+LIST_NUMBERED]",
        "",
        data["narrar_pergunta"],
        "",
        "[-LIST_NUMBERED]",
        "",
    ]
    return "\n".join(lines)


def validate(data: dict, rendered: str) -> None:
    words = data["definicao"].rstrip(".").split()
    if not 8 <= len(words) <= 12:
        raise ValueError(f"definição fora do limite de 8 a 12 palavras: {len(words)}")
    if f"# {data['titulo']}" not in rendered:
        raise ValueError("título ausente")
    if f"[+ACCORDION]\n\n{data['titulo']}" not in rendered:
        raise ValueError("título do Accordion divergente")
    if rendered.count("[+IMAGE_TEXT_ASIDE]") != 1:
        raise ValueError("Narrar deve conter um único IMAGE_TEXT_ASIDE")
    if rendered.count("#VOX:") != 3:
        raise ValueError("a aula deve conter três marcadores #VOX:")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--semana", type=int, required=True)
    parser.add_argument("--aula", type=int, required=True)
    args = parser.parse_args()

    key = (args.semana, args.aula)
    if key not in LESSONS:
        raise SystemExit(f"dados ainda não cadastrados para {args.semana}.{args.aula}")

    data = LESSONS[key]
    rendered = render_lesson(data)
    validate(data, rendered)
    output = BASE / f"{args.semana}.{args.aula}.md"
    output.write_text(rendered, encoding="utf-8")
    print(f"Aula gerada: {output}")


if __name__ == "__main__":
    main()
