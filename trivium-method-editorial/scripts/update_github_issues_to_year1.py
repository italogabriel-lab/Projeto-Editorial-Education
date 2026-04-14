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
except Exception as e:
    pass

if env_token:
    os.environ["GITHUB_TOKEN"] = env_token

REPO = "bibline/curriculum"

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
        print(f"Error calling API {path}: {e.output}")
        return None

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

print(f"Found {len(target_tickets)} target tickets for Year 1.")

# Fetch existing issues
print("Fetching existing open issues...")
issues = []
page = 1
while True:
    data = run_gh_api(f"repos/{REPO}/issues?labels=&state=open&per_page=100&page={page}&creator=Italo-bibline")
    if not data:
        break
    issues.extend(data)
    if len(data) < 100:
        break
    page += 1

# Filter ONLY those that are either the already modified one or the Ano 3 ones
filtered_issues = []
for i in issues:
    t = i['title']
    if t.startswith("[Belas artes] - Ano 3 - ") or t == "[Belas artes] - Ano 1 - 1.1 A essência da arte":
        filtered_issues.append(i)

# Sort by issue number
filtered_issues = sorted(filtered_issues, key=lambda x: x['number'])

print(f"Found {len(filtered_issues)} existing Ano 3 issues (and the one Ano 1 already renamed).")
print("Mapping:")
for i in range(min(5, len(filtered_issues))):
    print(f"Issue #{filtered_issues[i]['number']}: '{filtered_issues[i]['title']}' -> '{target_tickets[i]['title']}'")

# Execute mapping
print("\nExecuting update...")
for i in range(min(len(target_tickets), len(filtered_issues))):
    target = target_tickets[i]
    existing = filtered_issues[i]
    
    # We will update title and body
    print(f"Updating #{existing['number']} to: {target['title']}")
    run_gh_api(f"repos/{REPO}/issues/{existing['number']}", method="PATCH", fields={
        "title": target['title'],
        "body": target['body']
    })
    time.sleep(1) # rate limit

print("Done.")
