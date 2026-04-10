import fs from "fs";
import path from "path";

export function ensureDir(dirPath) {
  fs.mkdirSync(dirPath, { recursive: true });
}

export function isDirectoryEmpty(dirPath) {
  return fs.existsSync(dirPath) ? fs.readdirSync(dirPath).length === 0 : true;
}

export function copyFileSafe(sourcePath, targetPath) {
  ensureDir(path.dirname(targetPath));
  fs.copyFileSync(sourcePath, targetPath);
}

export function copyDirSafe(sourcePath, targetPath) {
  ensureDir(path.dirname(targetPath));
  fs.cpSync(sourcePath, targetPath, { recursive: true });
}

export function renderTemplate(template, replacements) {
  return Object.entries(replacements).reduce((content, [key, value]) => {
    return content.replaceAll(`{{${key}}}`, String(value));
  }, template);
}

export function writeJson(targetPath, data) {
  ensureDir(path.dirname(targetPath));
  fs.writeFileSync(targetPath, `${JSON.stringify(data, null, 2)}\n`, "utf8");
}

export function readJson(sourcePath) {
  return JSON.parse(fs.readFileSync(sourcePath, "utf8"));
}

