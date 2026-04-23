#!/usr/bin/env node

import { readFile, writeFile, mkdir, rm } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import { chromium } from 'playwright';

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
  node scripts/publish-lesson-github-ui.mjs --lesson 24.1 [opções]

Opções:
  --lesson <numero>              Número da aula. Exemplo: 24.1
  --year <ano>                   Ano escolar de 1 a 5. Padrão: 3
  --owner <owner>                Owner do repositório. Padrão: bibline
  --repo <repo>                  Repositório GitHub. Padrão: curriculum
  --branch <branch>              Branch de destino. Padrão: master
  --check-only                   Só valida caminhos e mostra o alvo
  --headless                     Ejecutar navegador en modo headless. Padrão: false
  --help                         Mostra esta ajuda

Exemplos:
  node scripts/publish-lesson-github-ui.mjs --lesson 24.1 --check-only
  node scripts/publish-lesson-github-ui.mjs --lesson 24.1 --year 3
  npm run publish:lesson:github:ui -- --lesson 24.1 --year 3
`);
}

function parseArgs(argv) {
  const options = { ...DEFAULTS };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];

    if (arg === '--help') { options.help = true; continue; }
    if (arg === '--check-only') { options.checkOnly = true; continue; }
    if (arg === '--headless') { options.headless = true; continue; }

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

function extractTitle(content) {
  const match = content.match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : 'Atualização de aula';
}

async function publishWithPlaywright(options, sourcePath, targetPath, fileContent) {
  const { owner, repo, branch, headless } = options;
  const commitMessage = extractTitle(fileContent);
  const fileUrl = `https://github.com/${owner}/${repo}/edit/${branch}/${targetPath}`;

  console.log(`Iniciando navegador...`);
  console.log(`-url do arquivo: ${fileUrl}`);

  const profilePath = path.join(process.cwd(), '.playwright', 'github-bibline-profile');

  const context = await chromium.launchPersistentContext(profilePath, {
    headless,
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
    viewport: { width: 1280, height: 720 },
    ignoreHTTPSErrors: true,
  });

  let page;
  if (context.pages().length > 0) {
    page = context.pages()[0];
  } else {
    page = await context.newPage();
  }

  try {
    console.log(`Navegando até o arquivo no GitHub...`);
    await page.goto(fileUrl, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForTimeout(2000);

    const loginSelector = 'input[name="login"][type="text"], input#login_field';
    const isLoginPage = await page.locator(loginSelector).count() > 0;

    if (isLoginPage) {
      throw new Error(' login necessários no navegador. Faça login no GitHub manualmente e tente novamente.');
    }

    console.log('Preenchendo conteúdo via JavaScript...');
    await page.evaluate((content) => {
      const editor = document.querySelector('.cm-content');
      if (editor) {
        editor.textContent = content;
        editor.dispatchEvent(new Event('input', { bubbles: true }));
        editor.dispatchEvent(new Event('change', { bubbles: true }));
      }
    }, fileContent);

    const commitTitleSelector = 'input[name="summary"], input[name="commit.title"], input#commit-summary';
    const commitDescSelector = 'textarea[name="description"], textarea[name="commit.message"], #commit-description';

    const hasCommitForm = await page.locator(commitTitleSelector).count() > 0 ||
                          await page.locator(commitDescSelector).count() > 0;

    if (hasCommitForm) {
      if (await page.locator(commitTitleSelector).count() > 0) {
        await page.locator(commitTitleSelector).fill(commitMessage);
      }

      console.log(`Clicando em "Commit changes"...`);
      const commitButtonSelector = 'button[type="submit"][name="commit"], button:has-text("Commit changes")';
      await page.locator(commitButtonSelector).click();
      await page.waitForLoadState('networkidle');
    } else {
      throw new Error('Formulário de commit não encontrado. Verifique se o arquivo existe.');
    }

    console.log(`Commit realizado com sucesso.`);
    console.log(`Publicação concluída: https://github.com/${owner}/${repo}/blob/${branch}/${targetPath}`);

  } catch (error) {
    throw new Error(`Erro ao publicar via UI: ${error.message}`);
  }
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
  await publishWithPlaywright(options, sourcePath, targetPath, fileContent);
}

main().catch((error) => {
  console.error(`Erro: ${error.message}`);
  process.exitCode = 1;
});