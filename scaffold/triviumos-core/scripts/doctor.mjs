import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const registry = JSON.parse(fs.readFileSync(path.join(ROOT, ".triviumos-core/data/asset-registry.json"), "utf8"));
const mode = process.argv.includes("--mode")
  ? process.argv[process.argv.indexOf("--mode") + 1]
  : "doctor";

function assertExists(relativePath) {
  const fullPath = path.join(ROOT, relativePath);
  if (!fs.existsSync(fullPath)) {
    throw new Error(`Missing required path: ${relativePath}`);
  }
}

function run() {
  const sourceLibraryRoot = registry.framework.sourceLibraryRoot || "trivium-method";

  assertExists(".triviumos-core/constitution.md");
  assertExists(".triviumos-core/core-config.yaml");
  assertExists(".triviumos-core/install-manifest.json");
  assertExists("triviumos/agents/skills");
  assertExists("triviumos/workflows/workflows");
  assertExists("triviumos/templates/templates");
  assertExists("triviumos/knowledge-base/knowledge-base");
  assertExists("triviumos/scripts");
  assertExists("docs/framework/ARCHITECTURE.md");
  assertExists("docs/framework/HIERARCHY.md");
  assertExists("docs/framework/ADJUSTMENTS.md");

  for (const agent of registry.agents) {
    assertExists(`.triviumos-core/development/agents/${agent.id}.md`);
    assertExists(`triviumos/agents/skills/${agent.id}/README.md`);
    assertExists(`triviumos/agents/skills/${agent.id}/SKILL.md`);
  }

  for (const group of registry.scriptGroups) {
    for (const item of group.items) {
      assertExists(path.join("triviumos", path.relative(sourceLibraryRoot, path.join(group.root, item))));
    }
  }

  const label = mode === "doctor" ? "doctor" : mode;
  console.log(`triviumos:${label}: OK`);
}

try {
  run();
} catch (error) {
  console.error(error.message);
  process.exit(1);
}
