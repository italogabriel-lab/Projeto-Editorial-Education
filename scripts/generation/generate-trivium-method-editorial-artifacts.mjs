import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const registryPath = path.join(ROOT, "src/data/editorial-registry.json");
const hierarchyPath = path.join(ROOT, "src/data/trivium-method-editorial-hierarchy.json");
const registry = JSON.parse(fs.readFileSync(registryPath, "utf8"));
const hierarchy = JSON.parse(fs.readFileSync(hierarchyPath, "utf8"));

const agentsDir = path.join(ROOT, "scaffold/trivium-method-editorial-core/development/agents");
const dataDir = path.join(ROOT, "scaffold/trivium-method-editorial-core/data");

fs.mkdirSync(agentsDir, { recursive: true });
fs.mkdirSync(dataDir, { recursive: true });

for (const agent of registry.agents) {
  const content = `# ${agent.id}

ACTIVATION-NOTICE: This file is the Trivium Method Editorial wrapper for the canonical editorial skill. Use it to understand role, authority, dependencies and handoff boundaries before loading the source skill.

\`\`\`yaml
agent:
  name: "${agent.name}"
  id: "${agent.id}"
  title: "${agent.title}"
  category: "${agent.category}"
  status: "${agent.status}"
  whenToUse: "${agent.whenToUse}"

persona:
  role: "${agent.title}"
  style: "Direto, orientado a processo e alinhado a qualidade editorial"
  identity: "Wrapper do Trivium Method Editorial para o skill canônico ${agent.name}"
  focus: "Executar sua autoridade específica sem invadir a responsabilidade de outros agentes"

authority:
${agent.authority.map((item) => `  - "${item}"`).join("\n")}

commands:
${agent.commands.map((item) => `  - "${item}"`).join("\n")}

dependencies:
  canonical_skill: "trivium-method-editorial/agents/skills/${agent.id}/SKILL.md"
  canonical_docs: "trivium-method-editorial/agents/skills/${agent.id}/README.md"
  workflows:
${agent.workflows.map((item) => `    - "${item}"`).join("\n")}
  handoff:
${agent.handoff.map((item) => `    - "${item}"`).join("\n")}
  registry: ".trivium-method-editorial-core/data/asset-registry.json"
\`\`\`

## Purpose

- Category: \`${agent.category}\`
- Status: \`${agent.status}\`
- Canonical source: \`trivium-method-editorial/agents/skills/${agent.id}/SKILL.md\`

## Operational Rule

Use the canonical skill for detailed execution. This wrapper exists to keep the AIOX-style hierarchy explicit inside \`.trivium-method-editorial-core\`.
`;

  fs.writeFileSync(path.join(agentsDir, `${agent.id}.md`), content, "utf8");
}

fs.writeFileSync(path.join(dataDir, "asset-registry.json"), `${JSON.stringify(registry, null, 2)}\n`, "utf8");
fs.writeFileSync(path.join(dataDir, "hierarchy.json"), `${JSON.stringify(hierarchy, null, 2)}\n`, "utf8");

console.log(`Generated ${registry.agents.length} Trivium Method Editorial agent wrappers.`);

