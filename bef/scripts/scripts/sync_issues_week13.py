import os
import re
import subprocess
import json
import time
import sys

PROJECT_ID = "PVT_kwDODLv1ac4BH1XW"
STATUS_FIELD_ID = "PVTSSF_lADODLv1ac4BH1XWzg4eN1w"
BACKLOG_OPTION_ID = "f75ad846"
ASSIGNEE = "Italo-bibline"
REPO = "bibline/curriculum"

env_token = ""
env_path = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/.env"
try:
    with open(env_path) as f:
        for line in f:
            if line.startswith("GITHUB_TOKEN="):
                env_token = line.split("=", 1)[1].strip()
except Exception:
    pass
    
if env_token:
    os.environ["GITHUB_TOKEN"] = env_token

# 1. Parse Tickets from Markdown
tickets = []
desc_path = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/Estrutura Curricular - 3º ANO/6 - Descrições para tickets - 3º ANO.md"

with open(desc_path, "r", encoding="utf-8") as f:
    content = f.read()

blocks = re.split(r'\n---\n', content)
for block in blocks:
    lines = block.strip().split('\n')
    title = None
    body_lines = []
    in_description = False
    
    for line in lines:
        if line.startswith("[Belas artes] - Ano 3 - "):
            title = line.strip()
        elif line.startswith("# Description"):
            in_description = True
        elif in_description:
            body_lines.append(line)
            
    if title:
        match = re.search(r'Ano 3 - (\d+)(?:\.\d+)?', title)
        if match:
            week = int(match.group(1))
            if week >= 13:
                body = '\n'.join(body_lines).strip()
                tickets.append({"title": title, "body": body})

print(f"Found {len(tickets)} target tickets for week 13 onwards.")

# 2. Get issues to recycle (created today)
def run_gh_api(path, method="GET", fields=None):
    cmd = ["gh", "api", path, "-X", method]
    if fields:
        for k, v in fields.items():
            if isinstance(v, list):
                for item in v:
                    cmd.extend(["-f", f"{k}[]={item}"])
            else:
                cmd.extend(["-f", f"{k}={v}"])
    try:
        res = subprocess.check_output(cmd, env=os.environ).decode()
        return json.loads(res) if res else {}
    except subprocess.CalledProcessError as e:
        print(f"Error calling API {path}: {e.output.decode()}")
        return None

issues_to_recycle = []
# Fetch page 1 and page 2 to ensure we get all the ~72 issues
for page in [1, 2]:
    page_data = run_gh_api(f"repos/{REPO}/issues?state=open&per_page=100&creator=italogabriel-lab&page={page}", method="GET")
    if page_data:
        for issue in page_data:
            if issue['title'].startswith('[Belas artes] - Ano 3 -'):
                if "2026-03-25" in issue["created_at"]:
                    issues_to_recycle.append((issue["number"], issue["node_id"], issue["title"]))

# Sort by issue number so we recycle them in order
issues_to_recycle.sort(key=lambda x: x[0])
print(f"Found {len(issues_to_recycle)} issues to recycle from today's batch.")

def run_graphql(query, variables=None):
    cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
    if variables:
        for k, v in variables.items():
             cmd.extend(["-F", f"{k}={v}"])
    try:
        res = subprocess.check_output(cmd, env=os.environ).decode()
        return json.loads(res) if res else {}
    except subprocess.CalledProcessError as e:
        print(f"Error calling GraphQL: {e.output.decode()}")
        return None

# 3. Process tickets
import time
processed = 0

for ticket in tickets:
    processed += 1
    t_title = ticket["title"]
    t_body = ticket["body"]
    
    print(f"[{processed}/{len(tickets)}] Processing: {t_title}")
    sys.stdout.flush()
    
    if issues_to_recycle:
        issue_number, node_id, old_title = issues_to_recycle.pop(0)
        print(f"  -> Recycling #{issue_number} (was: {old_title})")
        sys.stdout.flush()
        
        # Patch issue
        run_gh_api(f"repos/{REPO}/issues/{issue_number}", method="PATCH", fields={
            "title": t_title,
            "body": t_body,
            "assignees": [ASSIGNEE]
        })
        time.sleep(1.2)
    else:
        print(f"  -> Creating NEW issue")
        issue_data = run_gh_api(f"repos/{REPO}/issues", method="POST", fields={
            "title": t_title,
            "body": t_body,
            "assignees": [ASSIGNEE]
        })
        
        if not issue_data or "node_id" not in issue_data:
            print(f"  -> Failed to create new issue.")
            continue
            
        issue_node_id = issue_data["node_id"]
        issue_number = issue_data["number"]
        
        query_add = """
        mutation($project: ID!, $issue: ID!) {
          addProjectV2ItemById(input: {projectId: $project, contentId: $issue}) {
            item { id }
          }
        }
        """
        add_res = run_graphql(query_add, variables={"project": PROJECT_ID, "issue": issue_node_id})
        if not add_res or "data" not in add_res or "errors" in add_res:
            print(f"  -> Failed to add to Project")
            continue
            
        item_node_id = add_res["data"]["addProjectV2ItemById"]["item"]["id"]
        
        query_status = """
        mutation($project: ID!, $item: ID!, $field: ID!, $value: String!) {
          updateProjectV2ItemFieldValue(input: {
            projectId: $project,
            itemId: $item,
            fieldId: $field,
            value: { singleSelectOptionId: $value }
          }) {
            projectV2Item { id }
          }
        }
        """
        run_graphql(query_status, variables={
            "project": PROJECT_ID, "item": item_node_id, "field": STATUS_FIELD_ID, "value": BACKLOG_OPTION_ID
        })
        print(f"  -> Added to project Backlog")
        sys.stdout.flush()
        time.sleep(1.5)

# If any issues are leftover, we can optionally close them (unlikely since we need ~130 and only have ~70)
for left_issue in issues_to_recycle:
    print(f"Leftover issue #{left_issue[0]} - you may want to close it manually.")
    sys.stdout.flush()

print("All done!")
sys.stdout.flush()
