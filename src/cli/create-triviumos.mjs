import path from "path";
import { installProject } from "../lib/install.mjs";

function parseArgs(argv) {
  const args = argv.slice(2);
  const options = {
    force: false,
    targetDir: null
  };

  for (const arg of args) {
    if (arg === "--force") {
      options.force = true;
      continue;
    }

    if (!options.targetDir) {
      options.targetDir = arg;
    }
  }

  options.targetDir = options.targetDir || "triviumos-workspace";
  return options;
}

export async function main() {
  const options = parseArgs(process.argv);
  const targetDir = path.resolve(process.cwd(), options.targetDir);
  const result = installProject(targetDir, {
    force: options.force,
    projectName: path.basename(targetDir)
  });
  const nextStepDir = result.projectRoot.startsWith(process.cwd())
    ? path.relative(process.cwd(), result.projectRoot) || "."
    : result.projectRoot;

  console.log("TriviumOS");
  console.log(`Scaffolded at: ${result.projectRoot}`);
  console.log(
    `Inventory: ${result.counts.agents} agents, ${result.counts.frameworkWorkflows} workflows, ${result.counts.templates} templates, ${result.counts.scriptFiles} scripts`
  );
  console.log("Next steps:");
  console.log(`  cd ${nextStepDir}`);
  console.log("  npm run triviumos:inventory");
  console.log("  npm run triviumos:doctor");
}
