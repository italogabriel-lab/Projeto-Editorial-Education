import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { copyDirSafe, copyFileSafe, ensureDir, isDirectoryEmpty, readJson, renderTemplate, writeJson } from "./fs-utils.mjs";

const SOURCE_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const REGISTRY_PATH = path.join(SOURCE_ROOT, "src/data/editorial-registry.json");
const REGISTRY = readJson(REGISTRY_PATH);

const COPY_MAPPINGS = [
  { type: "dir", source: "trivium-method", target: "triviumos" },
  { type: "dir", source: "scaffold/triviumos-core", target: ".triviumos-core" },
  { type: "dir", source: "scaffold/disciplines", target: "disciplines" },
  { type: "dir", source: "public", target: "public" },
  { type: "file", source: "scaffold/public/data.json", target: "public/data.json" },
  { type: "dir", source: "src", target: "src" },
  { type: "file", source: "agent-command-center.html", target: "agent-command-center.html" },
  { type: "file", source: "index.html", target: "index.html" },
  { type: "file", source: "metas.html", target: "metas.html" },
  { type: "file", source: "metas-disciplinas.html", target: "metas-disciplinas.html" },
  { type: "file", source: "videos.html", target: "videos.html" },
  { type: "file", source: "vercel.json", target: "vercel.json" },
  { type: "file", source: "docs/framework/TRIVIUMOS-ARCHITECTURE.md", target: "docs/framework/ARCHITECTURE.md" },
  { type: "file", source: "docs/framework/TRIVIUMOS-HIERARCHY.md", target: "docs/framework/HIERARCHY.md" },
  { type: "file", source: "docs/framework/TRIVIUMOS-ADJUSTMENTS.md", target: "docs/framework/ADJUSTMENTS.md" },
  { type: "file", source: "docs/guides/TRIVIUMOS-INSTALLATION.md", target: "docs/guides/INSTALLATION.md" },
  { type: "file", source: "docs/guides/TRIVIUMOS-DISCIPLINE-ONBOARDING.md", target: "docs/guides/DISCIPLINE-ONBOARDING.md" },
  { type: "file", source: "docs/stories/README.md", target: "docs/stories/README.md" },
  { type: "dir", source: "scaffold/github", target: ".github" },
  { type: "file", source: "scaffold/gitignore", target: ".gitignore" },
  { type: "file", source: "scaffold/README.installed.md", target: "README.md" }
];

function normalizePackageName(name) {
  return name
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9-_]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function copyMapping(projectRoot, mapping) {
  const sourcePath = path.join(SOURCE_ROOT, mapping.source);
  const targetPath = path.join(projectRoot, mapping.target);

  if (mapping.type === "dir") {
    copyDirSafe(sourcePath, targetPath);
  } else {
    copyFileSafe(sourcePath, targetPath);
  }

  return mapping.target;
}

function writePackageJson(projectRoot, projectName) {
  const templatePath = path.join(SOURCE_ROOT, "scaffold/package.json.template");
  const template = fs.readFileSync(templatePath, "utf8");
  const content = renderTemplate(template, {
    PROJECT_NAME: normalizePackageName(projectName) || "triviumos-workspace"
  });

  fs.writeFileSync(path.join(projectRoot, "package.json"), content, "utf8");
}

function writeInstallManifest(projectRoot, projectName, copiedFiles) {
  const manifest = {
    framework: REGISTRY.framework.name,
    version: REGISTRY.framework.version,
    installerCommand: REGISTRY.framework.installerCommand,
    installedAt: new Date().toISOString(),
    projectName,
    copiedArtifacts: copiedFiles,
    inventory: REGISTRY.counts
  };

  writeJson(path.join(projectRoot, ".triviumos-core/install-manifest.json"), manifest);
}

export function installProject(targetDir, options = {}) {
  const projectRoot = path.resolve(targetDir);
  const projectName = options.projectName || path.basename(projectRoot);

  ensureDir(projectRoot);

  if (!options.force && !isDirectoryEmpty(projectRoot)) {
    throw new Error(`Target directory is not empty: ${projectRoot}. Use --force to continue.`);
  }

  const copiedFiles = COPY_MAPPINGS.map((mapping) => copyMapping(projectRoot, mapping));

  writePackageJson(projectRoot, projectName);
  copiedFiles.push("package.json");

  writeInstallManifest(projectRoot, projectName, copiedFiles);
  copiedFiles.push(".triviumos-core/install-manifest.json");

  return {
    projectRoot,
    projectName,
    copiedFiles,
    counts: REGISTRY.counts
  };
}

export function getRegistry() {
  return REGISTRY;
}
