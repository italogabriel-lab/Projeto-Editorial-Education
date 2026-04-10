import fs from "fs";
import path from "path";
import test from "node:test";
import assert from "node:assert/strict";

const ROOT = process.cwd();
const registry = JSON.parse(fs.readFileSync(path.join(ROOT, "src/data/editorial-registry.json"), "utf8"));

test("legacy skills now expose SKILL.md", () => {
  const legacyTargets = [
    "trivium-method/agents/skills/exam-builder/SKILL.md",
    "trivium-method/agents/skills/image-link-extractor/SKILL.md",
    "trivium-method/agents/skills/review-builder/SKILL.md"
  ];

  for (const relativePath of legacyTargets) {
    assert.ok(fs.existsSync(path.join(ROOT, relativePath)), relativePath);
  }
});

test("registry count matches agent list", () => {
  assert.equal(registry.agents.length, registry.counts.agents);
});
