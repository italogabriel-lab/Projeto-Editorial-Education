import fs from "fs";
import os from "os";
import path from "path";
import test from "node:test";
import assert from "node:assert/strict";
import { installProject, getRegistry } from "../src/lib/install.mjs";

test("installer scaffolds a TriviumOS workspace", () => {
  const tempRoot = fs.mkdtempSync(path.join(os.tmpdir(), "triviumos-"));
  const target = path.join(tempRoot, "workspace");

  const result = installProject(target, { projectName: "workspace" });
  const registry = getRegistry();

  assert.equal(result.counts.agents, registry.counts.agents);
  assert.equal(result.counts.templates, registry.counts.templates);
  assert.ok(fs.existsSync(path.join(target, ".triviumos-core/install-manifest.json")));
  assert.ok(fs.existsSync(path.join(target, ".triviumos-core/data/asset-registry.json")));
  assert.ok(fs.existsSync(path.join(target, ".triviumos-core/development/agents/orchestrator.md")));
  assert.ok(fs.existsSync(path.join(target, "triviumos/agents/skills/orchestrator/SKILL.md")));
  assert.ok(fs.existsSync(path.join(target, "public/data.json")));
  const observabilitySeed = JSON.parse(fs.readFileSync(path.join(target, "public/data.json"), "utf8"));
  assert.equal(observabilitySeed.total_items, 0);
  assert.deepEqual(observabilitySeed.items, []);
  assert.equal(fs.existsSync(path.join(target, "assets")), false);
  assert.ok(fs.existsSync(path.join(target, "docs/framework/ARCHITECTURE.md")));
  assert.ok(fs.existsSync(path.join(target, "package.json")));
});
