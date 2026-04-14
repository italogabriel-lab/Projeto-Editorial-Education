#!/usr/bin/env node

import { main } from "../src/cli/create-trivium-method-editorial.mjs";

main().catch((error) => {
  console.error(`Trivium Method Editorial installer failed: ${error.message}`);
  process.exitCode = 1;
});

