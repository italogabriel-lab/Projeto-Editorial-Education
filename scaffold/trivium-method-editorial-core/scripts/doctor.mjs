import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const registry = JSON.parse(fs.readFileSync(path.join(ROOT, ".trivium-method-editorial-core/data/asset-registry.json"), "utf8"));
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

  assertExists(".trivium-method-editorial-core/constitution.md");
  assertExists(".trivium-method-editorial-core/core-config.yaml");
  assertExists(".trivium-method-editorial-core/install-manifest.json");
  assertExists("trivium-method-editorial/agents/skills");
  assertExists("trivium-method-editorial/workflows/workflows");
  assertExists("trivium-method-editorial/templates/templates");
  assertExists("trivium-method-editorial/knowledge-base/knowledge-base");
  assertExists("trivium-method-editorial/scripts");
  assertExists("docs/framework/ARCHITECTURE.md");
  assertExists("docs/framework/HIERARCHY.md");
  assertExists("docs/framework/ADJUSTMENTS.md");

  for (const agent of registry.agents) {
    assertExists(`.trivium-method-editorial-core/development/agents/${agent.id}.md`);
    assertExists(`trivium-method-editorial/agents/skills/${agent.id}/README.md`);
    assertExists(`trivium-method-editorial/agents/skills/${agent.id}/SKILL.md`);
  }

  for (const group of registry.scriptGroups) {
    for (const item of group.items) {
      assertExists(path.join("trivium-method-editorial", path.relative(sourceLibraryRoot, path.join(group.root, item))));
    }
  }

  const label = mode === "doctor" ? "doctor" : mode;
  console.log(`trivium-method-editorial:${label}: OK`);
}

try {
  run();
} catch (error) {
  console.error(error.message);
  process.exit(1);
}
