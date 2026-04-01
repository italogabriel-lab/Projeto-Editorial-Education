import os
import re
import subprocess
import json
import time

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

def run_graphql(query, variables=None):
    cmd = ["gh", "api", "graphql"]
    if variables:
        cmd.extend(["-f", f"query={query}", "-F", f"variables={json.dumps(variables)}"])
    else:
        cmd.extend(["-f", f"query={query}"])
    for attempt in range(3):
        try:
            res = subprocess.check_output(cmd, env=os.environ, stderr=subprocess.STDOUT).decode()
            return json.loads(res) if res else {}
        except subprocess.CalledProcessError as e:
            time.sleep(2)
    return {}

def run_gh_api(path, method="GET", fields=None):
    cmd = ["gh", "api", path, "-X", method]
    if fields:
        for k, v in fields.items():
            if isinstance(v, list):
                for item in v:
                    cmd.extend(["-f", f"{k}[]={item}"])
            else:
                cmd.extend(["-f", f"{k}={v}"])
    for attempt in range(3):
        try:
            res = subprocess.check_output(cmd, env=os.environ, stderr=subprocess.STDOUT).decode()
            return json.loads(res) if res else {}
        except subprocess.CalledProcessError as e:
            time.sleep(2)
    return None

query = """
query($cursor: String) {
  node(id: "PVT_kwDODLv1ac4BH1XW") {
    ... on ProjectV2 {
      items(first: 100, after: $cursor) {
        nodes {
          content {
            ... on Issue {
              id
              number
              title
              repository {
                nameWithOwner
              }
            }
          }
          fieldValues(first: 20) {
            nodes {
              ... on ProjectV2ItemFieldSingleSelectValue {
                name
                field {
                  ... on ProjectV2SingleSelectField {
                    name
                  }
                }
              }
            }
          }
        }
        pageInfo {
          hasNextPage
          endCursor
        }
      }
    }
  }
}
"""

print("Starting execution...", flush=True)

all_backlog_issues = []
cursor = None
print("Fetching project items from GitHub...", flush=True)
while True:
    data = run_graphql(query, {"cursor": cursor} if cursor else None)
    project = data.get('data', {}).get('node', {})
    if not project:
        break
    items_conn = project.get('items', {})
    nodes = items_conn.get('nodes', [])
    for item in nodes:
        if not item or not item.get('content') or 'number' not in item['content']:
            continue
        issue_node = item['content']
        status = None
        for fv in item.get('fieldValues', {}).get('nodes', []):
            if not fv: continue
            if 'field' in fv and fv['field'] and fv['field'].get('name') == 'Status':
                status = fv.get('name')
        if status == 'Backlog':
            t = issue_node.get('title', '')
            repo_owner = issue_node.get('repository', {}).get('nameWithOwner', '')
            if t.startswith("[Belas artes]") or "Revisão do 1º Bimestre" in t:
                all_backlog_issues.append({
                    'id': issue_node['id'],
                    'number': issue_node['number'],
                    'title': t,
                    'repo': repo_owner
                })
    page_info = items_conn.get('pageInfo', {})
    if page_info.get('hasNextPage'):
        cursor = page_info.get('endCursor')
        print(f"Fetched page, fetching next...", flush=True)
    else:
        break

all_backlog_issues.sort(key=lambda x: x['number'])
print(f"Total Backlog [Belas artes] issues found: {len(all_backlog_issues)}", flush=True)

tickets_file = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano/Estrutura Curricular - 1º ANO/6 - Descrições para tickets - 1º ANO.md"
with open(tickets_file, 'r', encoding='utf-8') as f:
    content = f.read()

blocks = re.split(r'\[Belas artes\] - Ano 1 - ', content)
target_tickets = []
for block in blocks[1:]:
    lines = block.strip().split('\n')
    title = "[Belas artes] - Ano 1 - " + lines[0].strip()
    
    desc = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        desc.append(line)
        
    description = "\n".join(desc).strip()
    if description.startswith("# Description"):
        description = description[len("# Description"):].strip()
        
    target_tickets.append({"title": title, "body": description})

print(f"Total target tickets parsed from 1º ANO: {len(target_tickets)}", flush=True)

start_idx = -1
for i, issue in enumerate(all_backlog_issues):
    if issue['number'] == 1957:
        start_idx = i
        break

if start_idx == -1:
    print("Could not find issue #1957 in the Backlog!", flush=True)
    for iss in all_backlog_issues[:5]:
        print(iss, flush=True)
    exit(1)

issues_to_update = all_backlog_issues[start_idx:]
num_updates = min(len(issues_to_update), len(target_tickets))

print(f"Will update {num_updates} issues starting from #{issues_to_update[0]['number']}.", flush=True)
print("\nExecuting updates now...", flush=True)
for i in range(min(num_updates, 3)): # Just do 3 as a test first to avoid locking
    existing = issues_to_update[i]
    target = target_tickets[i]
    
    print(f"Updating #{existing['number']} to {target['title']}", flush=True)
    run_gh_api(f"repos/{existing['repo']}/issues/{existing['number']}", method="PATCH", fields={
        "title": target['title'],
        "body": target['body']
    })
    time.sleep(1)

print("Test complete.", flush=True)
