#!/usr/bin/env python3
"""
Atualiza tickets de [Matematica] - Ano 2 no GitHub Projects.

Por padrao, executa apenas diagnostico. Use --apply para gravar as mudancas.
O script le o token GITHUB_TOKEN_CLASSIC_KANBAN_BIBLINE_AULAS do .env da raiz.
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
    / "Finalizados"
    / "matematica-2-ano.md"
)

TOKEN_NAME = "GITHUB_TOKEN_CLASSIC_KANBAN_BIBLINE_AULAS"
PROJECT_ID = "PVT_kwDODLv1ac4BH1XW"
PROJECT_OWNER = "bibline"
PROJECT_NUMBER = 2
DEFAULT_ASSIGNEE = "walmirfeijo"
REPO_FALLBACK = "bibline/curriculum"


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
        raise SystemExit(f"Arquivo .env nao encontrado: {ENV_PATH}")

    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith(f"{TOKEN_NAME}="):
            token = line.split("=", 1)[1].strip()
            if token:
                return token

    raise SystemExit(f"Token {TOKEN_NAME} nao encontrado em {ENV_PATH}")


def gh(args: list[str], env: dict[str, str], payload: dict | None = None, retries: int = 4) -> dict:
    cmd = ["gh", *args]
    input_text = None
    if payload is not None:
        cmd.extend(["--input", "-"])
        input_text = json.dumps(payload)

    last_error = ""
    for attempt in range(1, retries + 1):
        result = subprocess.run(
            cmd,
            input=input_text,
            text=True,
            capture_output=True,
            env=env,
            check=False,
        )
        if result.returncode == 0:
            if not result.stdout.strip():
                return {}
            return json.loads(result.stdout)

        last_error = result.stderr.strip() or result.stdout.strip()
        transient = any(marker in last_error for marker in ("EOF", "HTTP 502", "HTTP 503", "HTTP 504"))
        if not transient or attempt == retries:
            break

        time.sleep(2 * attempt)

    raise RuntimeError(last_error)


def parse_reference() -> dict[str, ReferenceTicket]:
    text = REFERENCE_FILE.read_text(encoding="utf-8")
    pattern = re.compile(
        r"^\[Matemática\] - Ano 2 - (\d+(?:\.\d+)?)\s+(.+?)\n\n"
        r"# Description\n\n([\s\S]*?)(?=\n---\n|$)",
        re.MULTILINE,
    )

    tickets: dict[str, ReferenceTicket] = {}
    for match in pattern.finditer(text):
        code = match.group(1).strip()
        title = f"[Matemática] - Ano 2 - {code} {match.group(2).strip()}"
        body = f"# Description\n\n{match.group(3).strip()}"
        tickets[code] = ReferenceTicket(code=code, title=title, body=body)

    if len(tickets) != 168:
        raise SystemExit(f"Esperava 168 tickets no arquivo de referencia, encontrei {len(tickets)}")

    return tickets


def issue_code(title: str) -> str | None:
    match = re.match(r"^\[Matemática\] - ANO 2 -\s*(\d+(?:\.\d+)?)", title, re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.match(r"^\[Matemática\] - Ano 2 -\s*(\d+(?:\.\d+)?)", title)
    if match:
        return match.group(1)
    return None


def fetch_project_issues(env: dict[str, str]) -> list[ProjectIssue]:
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
                  number
                  title
                  body
                  state
                  url
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
            for field_value in node.get("fieldValues", {}).get("nodes", []):
                field = field_value.get("field") if field_value else None
                if field and field.get("name") == "Status":
                    status = field_value.get("name")

            issues.append(
                ProjectIssue(
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
                )
            )

        if not items["pageInfo"]["hasNextPage"]:
            break
        cursor = items["pageInfo"]["endCursor"]

    return issues


def expected_codes() -> list[str]:
    codes: list[str] = []
    for start in (1, 11, 21, 31):
        for week in range(start, start + 8):
            for day in range(1, 6):
                codes.append(f"{week}.{day}")
        codes.extend([str(start + 8), str(start + 9)])
    return codes


def create_issue(env: dict[str, str], ticket: ReferenceTicket) -> dict:
    issue = gh(
        ["api", f"repos/{REPO_FALLBACK}/issues", "-X", "POST"],
        env,
        {
            "title": ticket.title,
            "body": ticket.body,
            "assignees": [DEFAULT_ASSIGNEE],
        },
    )

    add_query = """
    mutation($project: ID!, $issue: ID!) {
      addProjectV2ItemById(input: {projectId: $project, contentId: $issue}) {
        item { id }
      }
    }
    """
    gh(
        [
            "api",
            "graphql",
            "-f",
            f"query={add_query}",
            "-F",
            f"project={PROJECT_ID}",
            "-F",
            f"issue={issue['node_id']}",
        ],
        env,
    )
    return issue


def update_issue(env: dict[str, str], issue: ProjectIssue, ticket: ReferenceTicket) -> None:
    gh(
        ["api", f"repos/{issue.repository}/issues/{issue.number}", "-X", "PATCH"],
        env,
        {
            "title": ticket.title,
            "body": ticket.body,
            "assignees": [DEFAULT_ASSIGNEE],
        },
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="aplica as atualizacoes no GitHub")
    parser.add_argument(
        "--create-missing",
        action="store_true",
        help="cria tickets faltantes no repo bibline/curriculum e adiciona ao Project",
    )
    parser.add_argument("--sleep", type=float, default=0.4, help="pausa entre updates")
    args = parser.parse_args()

    env = os.environ.copy()
    env["GITHUB_TOKEN"] = load_token()

    references = parse_reference()
    issues = fetch_project_issues(env)

    by_code: dict[str, list[ProjectIssue]] = {}
    for issue in issues:
        by_code.setdefault(issue.code, []).append(issue)

    missing = [code for code in expected_codes() if code not in by_code]
    duplicates = {code: items for code, items in by_code.items() if len(items) > 1}

    planned_updates: list[tuple[ProjectIssue, ReferenceTicket]] = []
    for issue in issues:
        ticket = references.get(issue.code)
        if not ticket:
            continue
        title_changed = issue.title != ticket.title
        body_changed = issue.body.strip() != ticket.body.strip()
        assignee_changed = issue.assignees != [DEFAULT_ASSIGNEE]
        if title_changed or body_changed or assignee_changed:
            planned_updates.append((issue, ticket))

    print(f"Arquivo de referencia: {REFERENCE_FILE}")
    print(f"Tickets no arquivo: {len(references)}")
    print(f"Itens no Project para Ano 2: {len(issues)}")
    print(f"Codigos unicos no Project: {len(by_code)}")
    print(f"Faltando: {', '.join(missing) if missing else 'nenhum'}")
    if duplicates:
        duplicate_text = " | ".join(
            f"{code}: {', '.join('#' + str(item.number) for item in items)}"
            for code, items in sorted(duplicates.items())
        )
        print(f"Duplicidades: {duplicate_text}")
    else:
        print("Duplicidades: nenhuma")
    print(f"Updates planejados: {len(planned_updates)}")

    if not args.apply:
        print("Modo dry-run. Use --apply para gravar no GitHub.")
        return 0

    updated = 0
    failed: list[str] = []
    for issue, ticket in planned_updates:
        try:
            print(f"Atualizando #{issue.number}: {ticket.title}", flush=True)
            update_issue(env, issue, ticket)
            updated += 1
            time.sleep(args.sleep)
        except Exception as exc:  # noqa: BLE001
            failed.append(f"#{issue.number} {issue.code}: {exc}")

    created = 0
    if args.create_missing:
        for code in missing:
            ticket = references[code]
            try:
                print(f"Criando {code}: {ticket.title}", flush=True)
                create_issue(env, ticket)
                created += 1
                time.sleep(args.sleep)
            except Exception as exc:  # noqa: BLE001
                failed.append(f"create {code}: {exc}")

    print(f"Atualizados: {updated}")
    print(f"Criados: {created}")
    print(f"Falhas: {len(failed)}")
    for item in failed:
        print(f"  - {item}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
