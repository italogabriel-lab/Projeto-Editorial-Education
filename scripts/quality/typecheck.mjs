import fs from "fs";
import path from "path";

const ROOT = process.cwd();

function readJson(relativePath) {
  return JSON.parse(fs.readFileSync(path.join(ROOT, relativePath), "utf8"));
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

const registry = readJson("src/data/editorial-registry.json");
const hierarchy = readJson("src/data/triviumos-hierarchy.json");
const scaffoldRegistry = readJson("scaffold/triviumos-core/data/asset-registry.json");
const scaffoldHierarchy = readJson("scaffold/triviumos-core/data/hierarchy.json");

assert(registry.framework.name === "TriviumOS", "Registry framework name must be TriviumOS");
assert(registry.agents.length === registry.counts.agents, "Agent count mismatch");
assert(registry.templates.length === registry.counts.templates, "Template count mismatch");
assert(registry.knowledgeBase.length === registry.counts.knowledgeBaseFiles, "Knowledge base count mismatch");

const scriptCount = registry.scriptGroups.reduce((sum, group) => sum + group.items.length, 0);
assert(scriptCount === registry.counts.scriptFiles, "Script count mismatch");

assert(
  JSON.stringify(registry) === JSON.stringify(scaffoldRegistry),
  "Scaffold asset registry is out of date. Run npm run build:artifacts"
);
assert(
  JSON.stringify(hierarchy) === JSON.stringify(scaffoldHierarchy),
  "Scaffold hierarchy is out of date. Run npm run build:artifacts"
);

for (const agent of registry.agents) {
  assert(fs.existsSync(path.join(ROOT, agent.sourceSkill)), `Missing source skill: ${agent.sourceSkill}`);
  assert(fs.existsSync(path.join(ROOT, agent.sourceReadme)), `Missing source readme: ${agent.sourceReadme}`);
  assert(
    fs.existsSync(path.join(ROOT, "scaffold/triviumos-core/development/agents", `${agent.id}.md`)),
    `Missing generated wrapper for agent ${agent.id}`
  );
}

for (const item of registry.templates) {
  assert(fs.existsSync(path.join(ROOT, item.path)), `Missing template: ${item.path}`);
}

for (const item of registry.knowledgeBase) {
  assert(fs.existsSync(path.join(ROOT, item.path)), `Missing knowledge file: ${item.path}`);
}

for (const group of registry.scriptGroups) {
  for (const item of group.items) {
    assert(fs.existsSync(path.join(ROOT, group.root, item)), `Missing script: ${group.root}/${item}`);
  }
}

console.log("typecheck: registry, hierarchy and generated artifacts are consistent");

