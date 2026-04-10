import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const registry = JSON.parse(fs.readFileSync(path.join(ROOT, "data/asset-registry.json"), "utf8"));
const section = process.argv.includes("--section")
  ? process.argv[process.argv.indexOf("--section") + 1]
  : null;

function printAgents() {
  console.log(`Agents (${registry.agents.length})`);
  for (const agent of registry.agents) {
    console.log(`- ${agent.id} [${agent.category}] (${agent.status})`);
  }
}

function printTemplates() {
  console.log(`Templates (${registry.templates.length})`);
  for (const item of registry.templates) {
    console.log(`- ${item.id}: ${item.path}`);
  }
}

function printWorkflows() {
  console.log(`Framework workflows (${registry.workflows.length})`);
  for (const item of registry.workflows) {
    console.log(`- ${item.id}: ${item.wrapperPath}`);
  }
}

function printScripts() {
  console.log(`Script groups (${registry.scriptGroups.length})`);
  for (const group of registry.scriptGroups) {
    console.log(`- ${group.id}: ${group.items.length} files`);
  }
}

if (!section) {
  console.log(`${registry.framework.name} v${registry.framework.version}`);
  console.log(
    `Inventory: ${registry.counts.agents} agents, ${registry.counts.frameworkWorkflows} workflows, ${registry.counts.templates} templates, ${registry.counts.scriptFiles} scripts`
  );
  printAgents();
  printWorkflows();
  printTemplates();
  printScripts();
  process.exit(0);
}

if (section === "agents") printAgents();
if (section === "workflows") printWorkflows();
if (section === "templates") printTemplates();
if (section === "scripts") printScripts();

