#!/usr/bin/env node

import { readFile, writeFile, mkdir, rm } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import { execSync } from 'node:child_process';

const YEAR_CONFIG = {
  '1': { sourceFolder: '1º Ano', repoPrefix: '1-belas-artes' },
  '2': { sourceFolder: '2º Ano - DA CRIAÇÃO ATÉ A ARTE BIZANTINA', repoPrefix: '2-belas-artes' },
  '3': { sourceFolder: '3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE', repoPrefix: '3-belas-artes' },
  '4': { sourceFolder: '4º Ano - IMPRESSIONISMO ATÉ A ARTE CONTEMPORÂNEA', repoPrefix: '4-belas-artes' },
  '5': { sourceFolder: '5º Ano - MANEIRISMO ATÉ O REALISMO AMERICANO', repoPrefix: '5-belas-artes' },
};

const DEFAULTS = {
  year: '3',
  owner: 'bibline',
  repo: 'curriculum',
  branch: 'master',
  checkOnly: false,
};

function printHelp() {
  console.log(`
Uso:
  node scripts/publish-lesson-github.mjs --lesson 24.1 [opções]

Opções:
  --lesson <numero>              Número da aula. Exemplo: 24.1
  --year <ano>                   Ano escolar de 1 a 5. Padrão: 3
  --owner <owner>                Owner do repositório. Padrão: bibline
  --repo <repo>                  Repositório GitHub. Padrão: curriculum
  --branch <branch>              Branch de destino. Padrão: master
  --check-only                   Só valida caminhos e mostra o alvo
  --help                         Mostra esta ajuda

Exemplos:
  node scripts/publish-lesson-github.mjs --lesson 24.1 --check-only
  node scripts/publish-lesson-github.mjs --lesson 24.1 --year 3
  npm run publish:lesson:github -- --lesson 24.1 --year 3
`);
}

function parseArgs(argv) {
  const options = { ...DEFAULTS };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];

    if (arg === '--help') { options.help = true; continue; }
    if (arg === '--check-only') { options.checkOnly = true; continue; }

    if (arg.startsWith('--')) {
      const key = arg.slice(2);
      const value = argv[index + 1];

      if (!value || value.startsWith('--')) {
        throw new Error(`Valor ausente para ${arg}.`);
      }

      options[key.replace(/-([a-z])/g, (_, letter) => letter.toUpperCase())] = value;
      index += 1;
      continue;
    }

    throw new Error(`Argumento desconhecido: ${arg}`);
  }

  return options;
}

function normalizeLessonNumber(lesson) {
  if (!lesson) { throw new Error('Informe --lesson com o número da aula.'); }
  if (!/^\d+(\.\d+)?$/.test(lesson)) { throw new Error(`Número de aula inválido: ${lesson}`); }
  return lesson;
}

function getYearConfig(year) {
  const config = YEAR_CONFIG[String(year)];
  if (!config) { throw new Error(`Ano inválido: ${year}. Use 1, 2, 3, 4 ou 5.`); }
  return config;
}

function buildPaths(rootDir, year, lesson) {
  const yearConfig = getYearConfig(year);
  const sourcePath = path.join(
    rootDir,
    'Projeto - Bibline Academy ( Produção de Aulas)',
    'Belas Artes - Fase da Gramática',
    '1 Fase - Gramática',
    yearConfig.sourceFolder,
    `${lesson}.md`,
  );
  const targetPath = `br/_/${yearConfig.repoPrefix}-${lesson}/README.md`;
  return { sourcePath, targetPath };
}

function git(cwd, command) {
  const fullCmd = `git ${command}`;
  try {
    return execSync(fullCmd, { cwd, encoding: 'utf-8', stdio: 'pipe' });
  } catch (error) {
    throw new Error(`git falhou: ${fullCmd}\n${error.message}`);
  }
}

function extractTitle(content) {
  const match = content.match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : 'Atualização de aula';
}

async function publishWithGit(options, sourcePath, targetPath, fileContent, tempDir) {
  const { owner, repo, branch } = options;
  const repoUrl = `https://github.com/${owner}/${repo}.git`;
  const targetDir = path.join(tempDir, 'repo');
  const commitMessage = extractTitle(fileContent);

  console.log(`Clonando ${repoUrl} (shallow)...`);
  git(process.cwd(), `clone --depth 1 ${repoUrl} "${targetDir}"`);

  const targetFilePath = path.join(targetDir, targetPath);
  const targetDirPath = path.dirname(targetFilePath);

  await mkdir(targetDirPath, { recursive: true });
  await writeFile(targetFilePath, fileContent, 'utf-8');

  console.log(`Arquivo escrito em: ${targetPath}`);
  console.log(`Mensagem de commit: ${commitMessage}`);

  git(targetDir, `add "${targetPath}"`);
  try {
    git(targetDir, `commit -m "${commitMessage}"`);
  } catch {
    console.log('Nenhuma alteração para commitar.');
  }

  try {
    git(targetDir, `push origin ${branch}`);
  } catch (error) {
    if (/rejected/i.test(error.message)) {
      throw new Error(`Push recusado. Pode precisar de pull primeiro: git pull origin ${branch}`);
    }
    throw error;
  }

  console.log(`Publicação concluída: https://github.com/${owner}/${repo}/blob/${branch}/${targetPath}`);
}

async function main() {
  const options = parseArgs(process.argv.slice(2));

  if (options.help) { printHelp(); return; }

  const lesson = normalizeLessonNumber(options.lesson);
  const year = String(options.year);
  const rootDir = process.cwd();
  const { sourcePath, targetPath } = buildPaths(rootDir, year, lesson);

  console.log(`Aula local: ${sourcePath}`);
  console.log(`Destino GitHub: ${targetPath}`);

  if (options.checkOnly) {
    console.log('Modo check-only.');
    return;
  }

  const fileContent = await readFile(sourcePath, 'utf-8');
  const tempDir = path.join(rootDir, '.tmp-gh-publish');

  try {
    await rm(tempDir, { recursive: true, force: true });
    await publishWithGit(options, sourcePath, targetPath, fileContent, tempDir);
  } finally {
    await rm(tempDir, { recursive: true, force: true }).catch(() => {});
  }
}

main().catch((error) => {
  console.error(`Erro: ${error.message}`);
  process.exitCode = 1;
});