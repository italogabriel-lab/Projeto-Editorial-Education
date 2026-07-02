#!/usr/bin/env python3
"""
Atualiza tickets de [Matemática] - Ano 5 no GitHub Projects.

Por padrão executa apenas diagnóstico. Use --apply para gravar as mudanças.
O script lê o token GITHUB_TOKEN_CLASSIC_KANBAN_BIBLINE_AULAS do .env da raiz.

Uso:
    python3 update_matematica5_tickets.py           # dry-run
    python3 update_matematica5_tickets.py --apply   # aplica as atualizações
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
ENV_PATH = ROOT / ".env"
REFERENCE_FILE = (
    ROOT
    / "Projeto - Bibline Academy ( Produção de Aulas)"
    / "Criação de tickets Equipe - Kanban Github"
    / "Em-Progresso"
    / "matematica-5-ano-tickets.md"
)

TOKEN_NAME       = "GITHUB_TOKEN_CLASSIC_KANBAN_BIBLINE_AULAS"
PROJECT_ID       = "PVT_kwDODLv1ac4BH1XW"
PROJECT_OWNER    = "bibline"
PROJECT_NUMBER   = 2
DEFAULT_ASSIGNEE = "deborafeijo-gif"
REPO_FALLBACK    = "bibline/curriculum"


@dataclass(frozen=True)
class ReferenceTicket:
    code: str
    title: str
    body: str


@dataclass(frozen=True)
class ProjectIssue:
    item_id: str
    number: int
    title: str
    body: str
    state: str
    url: str
    repository: str
    assignees: list[str]
    status: str | None
    code: str


def load_token() -> str:
    if not ENV_PATH.exists():
        raise SystemExit(f"Arquivo .env não encontrado: {ENV_PATH}")
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith(f"{TOKEN_NAME}="):
            token = line.split("=", 1)[1].strip()
            if token:
                return token
    raise SystemExit(f"Token {TOKEN_NAME} não encontrado em {ENV_PATH}")


def gh(args: list[str], env: dict, payload: dict | None = None, retries: int = 4) -> dict:
    cmd = ["gh", *args]
    input_text = None
    if payload is not None:
        cmd.extend(["--input", "-"])
        input_text = json.dumps(payload)

    last_error = ""
    for attempt in range(1, retries + 1):
        result = subprocess.run(
            cmd, input=input_text, text=True, capture_output=True, env=env, check=False,
        )
        if result.returncode == 0:
            return json.loads(result.stdout) if result.stdout.strip() else {}

        last_error = result.stderr.strip() or result.stdout.strip()
        transient = any(m in last_error for m in ("EOF", "HTTP 502", "HTTP 503", "HTTP 504"))
        if not transient or attempt == retries:
            break
        time.sleep(2 * attempt)

    raise RuntimeError(last_error)


def parse_reference() -> dict[str, ReferenceTicket]:
    text = REFERENCE_FILE.read_text(encoding="utf-8")
    pattern = re.compile(
        r"^\[Matemática\] - Ano 5 - (\d+(?:\.\d+)?)\s+(.+?)\n\n"
        r"# Description\n\n([\s\S]*?)(?=\n---\n|$)",
        re.MULTILINE,
    )

    tickets: dict[str, ReferenceTicket] = {}
    for match in pattern.finditer(text):
        code  = match.group(1).strip()
        title = f"[Matemática] - Ano 5 - {code} {match.group(2).strip()}"
        body  = f"# Description\n\n{match.group(3).strip()}"
        tickets[code] = ReferenceTicket(code=code, title=title, body=body)

    print(f"Tickets no arquivo de referência: {len(tickets)}")
    return tickets


def issue_code(title: str) -> str | None:
    match = re.match(r"^\[Matemática\] - Ano 5 -\s*(\d+(?:\.\d+)?)", title, re.IGNORECASE)
    return match.group(1) if match else None


def fetch_project_issues(env: dict) -> list[ProjectIssue]:
    query = """
    query($cursor: String) {
      organization(login: "bibline") {
        projectV2(number: 2) {
          items(first: 100, after: $cursor) {
            pageInfo { hasNextPage endCursor }
            nodes {
              id
              content {
                __typename
                ... on Issue {
                  number title body state url
                  repository { nameWithOwner }
                  assignees(first: 20) { nodes { login } }
                }
              }
              fieldValues(first: 20) {
                nodes {
                  ... on ProjectV2ItemFieldSingleSelectValue {
                    name
                    field { ... on ProjectV2SingleSelectField { name } }
                  }
                }
              }
            }
          }
        }
      }
    }
    """

    issues: list[ProjectIssue] = []
    cursor: str | None = None
    while True:
        args = ["api", "graphql", "-f", f"query={query}"]
        if cursor:
            args.extend(["-F", f"cursor={cursor}"])
        data = gh(args, env)
        items = data["data"]["organization"]["projectV2"]["items"]

        for node in items["nodes"]:
            content = node.get("content")
            if not content or content.get("__typename") != "Issue":
                continue
            code = issue_code(content.get("title", ""))
            if not code:
                continue

            status = None
            for fv in node.get("fieldValues", {}).get("nodes", []):
                field = fv.get("field") if fv else None
                if field and field.get("name") == "Status":
                    status = fv.get("name")

            issues.append(ProjectIssue(
                item_id=node["id"],
                number=content["number"],
                title=content["title"],
                body=content.get("body") or "",
                state=content["state"],
                url=content["url"],
                repository=content["repository"]["nameWithOwner"],
                assignees=[a["login"] for a in content["assignees"]["nodes"]],
                status=status,
                code=code,
            ))

        if not items["pageInfo"]["hasNextPage"]:
            break
        cursor = items["pageInfo"]["endCursor"]

    # Filtra apenas tickets do Ano 5
    ano4 = [i for i in issues if re.match(r"^\[Matemática\] - Ano 5", i.title, re.IGNORECASE)]
    print(f"Tickets do Ano 5 encontrados no Project: {len(ano4)}")
    return ano4


def update_issue(env: dict, issue: ProjectIssue, ticket: ReferenceTicket) -> None:
    gh(
        ["api", f"repos/{issue.repository}/issues/{issue.number}", "-X", "PATCH"],
        env,
        {"title": ticket.title, "body": ticket.body, "assignees": [DEFAULT_ASSIGNEE]},
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Atualiza tickets de Matemática Ano 5 no Kanban Bibline."
    )
    parser.add_argument("--apply", action="store_true", help="Aplica as atualizações no GitHub.")
    parser.add_argument("--sleep", type=float, default=0.4, help="Pausa entre updates (seg).")
    args = parser.parse_args()

    env = os.environ.copy()
    env["GITHUB_TOKEN"] = load_token()

    references = parse_reference()
    issues     = fetch_project_issues(env)

    by_code: dict[str, list[ProjectIssue]] = {}
    for issue in issues:
        by_code.setdefault(issue.code, []).append(issue)

    # Tickets no Project que têm referência e precisam de update
    planned: list[tuple[ProjectIssue, ReferenceTicket]] = []
    for issue in issues:
        ticket = references.get(issue.code)
        if not ticket:
            continue
        title_changed    = issue.title != ticket.title
        body_changed     = issue.body.strip() != ticket.body.strip()
        assignee_changed = issue.assignees != [DEFAULT_ASSIGNEE]
        if title_changed or body_changed or assignee_changed:
            planned.append((issue, ticket))

    # Códigos da referência que não existem no Project
    missing = [c for c in references if c not in by_code]

    print(f"\nArquivo de referência : {REFERENCE_FILE.name}")
    print(f"Updates planejados    : {len(planned)}")
    print(f"Códigos sem issue     : {len(missing)}" + (f" → {', '.join(missing[:10])}" if missing else ""))

    if not args.apply:
        print("\nModo dry-run. Use --apply para gravar no GitHub.")
        # Mostra preview dos primeiros 10
        for issue, ticket in planned[:10]:
            print(f"\n  #{issue.number}: {issue.title}")
            print(f"       → {ticket.title}")
        if len(planned) > 10:
            print(f"  ... e mais {len(planned) - 10} atualizações.")
        return 0

    print("\n🚀 Aplicando atualizações...\n")
    updated = 0
    failed: list[str] = []

    for issue, ticket in planned:
        try:
            print(f"Atualizando #{issue.number}: {ticket.title}", flush=True)
            update_issue(env, issue, ticket)
            updated += 1
            time.sleep(args.sleep)
        except Exception as exc:
            failed.append(f"#{issue.number} {issue.code}: {exc}")

    print(f"\n{'='*60}")
    print(f"✅ Atualizados: {updated}/{len(planned)}")
    if failed:
        print(f"❌ Falhas ({len(failed)}):")
        for f in failed:
            print(f"  - {f}")
    print("="*60)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
