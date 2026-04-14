import fs from "fs";
import path from "path";
import { spawnSync } from "child_process";

const ROOT = process.cwd();
const targets = [];

function walk(currentPath) {
  for (const entry of fs.readdirSync(currentPath, { withFileTypes: true })) {
    if (entry.name === "node_modules" || entry.name === ".git") {
      continue;
    }

    const fullPath = path.join(currentPath, entry.name);
    if (entry.isDirectory()) {
      walk(fullPath);
      continue;
    }

    if (/\.(js|mjs)$/.test(entry.name)) {
      targets.push(fullPath);
    }
  }
}

walk(path.join(ROOT, "bin"));
walk(path.join(ROOT, "src"));
walk(path.join(ROOT, "scripts"));
walk(path.join(ROOT, "tests"));
walk(path.join(ROOT, "scaffold/trivium-method-editorial-core/scripts"));

for (const target of targets) {
  const result = spawnSync(process.execPath, ["--check", target], { stdio: "inherit" });
  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }
}

console.log(`lint: checked ${targets.length} JavaScript files`);

