#!/usr/bin/env node

import { main } from "../src/cli/create-triviumos.mjs";

main().catch((error) => {
  console.error(`TriviumOS installer failed: ${error.message}`);
  process.exitCode = 1;
});

