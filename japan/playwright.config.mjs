import { defineConfig, devices } from '@playwright/test'
import { existsSync } from 'node:fs'

const chrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
export default defineConfig({
  testDir: './e2e',
  outputDir: '../.private/japan/qa/playwright',
  reporter: [['list']],
  timeout: 45000,
  expect: { timeout: 12000 },
  workers: 1,
  use: {
    baseURL: 'http://localhost:8789',
    trace: 'off',
    screenshot: 'off',
    video: 'off',
    launchOptions: existsSync(chrome) ? { executablePath: chrome } : {},
  },
  webServer: {
    cwd: new URL('..', import.meta.url).pathname,
    command: `JAPAN_TEST_PORT=8789 JAPAN_TEST_PREFIX=japan-playwright-${Date.now()} node scripts/japan/dev.mjs`,
    url: 'http://localhost:8789/japan',
    reuseExistingServer: !process.env.CI,
  },
  projects: [
    { name: 'desktop', use: { viewport: { width: 1365, height: 900 } } },
    { name: 'mobile', use: { ...devices['iPhone 13'], defaultBrowserType: 'chromium' } },
  ],
})
