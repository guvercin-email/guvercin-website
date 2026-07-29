// Re-capture the screenshots on the site from the running app.
//
//   npm i -D playwright && node tools/capture_shots.mjs
//
// Shoots try.guvercin.email — the real interface over an in-memory backend —
// in both themes at 1600x1000 @2x, and writes PNGs to tools/shots/. Convert
// them with tools/shots_to_webp.py, which is what assets/img/ actually holds.
//
// The data in these is invented. The pixels are the app.
import { chromium } from 'playwright'
import { mkdirSync } from 'node:fs'

const URL = process.env.GUVERCIN_TRY || 'https://try.guvercin.email'
const THEME = process.argv[2]
if (!['light', 'dark'].includes(THEME)) {
  console.error('usage: node tools/capture_shots.mjs <light|dark>')
  process.exit(1)
}
const OUT = `tools/shots/${THEME}`
mkdirSync(OUT, { recursive: true })

const browser = await chromium.launch({ channel: 'chrome' })

async function open({ offline = false } = {}) {
  const ctx = await browser.newContext({
    viewport: { width: 1600, height: 1000 },
    deviceScaleFactor: 2,
  })
  const page = await ctx.newPage()
  // The root path seeds a demo account and redirects. Going straight to
  // /dashboard hits the auth guard and lands on the account setup instead.
  await page.goto(`${URL}/`, { waitUntil: 'domcontentloaded' })
  await page.waitForURL('**/dashboard', { timeout: 20000 })
  // The "nothing actually sends" badge belongs to the web demo. The desktop
  // app these pictures stand in for does not have it.
  await page.addStyleTag({ content: '.demo-badge{display:none !important}' })
  await page.waitForTimeout(2500)
  // Seeding the account rewrites theme_mode/theme_name from the account
  // record, so a theme set before load is overwritten. Apply it afterwards,
  // through the same event the app's own settings screen fires.
  await page.evaluate(t => {
    localStorage.setItem('theme_mode', 'manual')
    localStorage.setItem('theme_name', t)
    window.dispatchEvent(new Event('guvercin-theme-changed'))
  }, THEME)
  await page.waitForTimeout(1800)
  if (offline) {
    // Cutting the network for real also stops the offline icon's own SVG from
    // loading, which renders as a broken image. The app reads navigator.onLine,
    // so override that and fire the event it listens for.
    await page.evaluate(() => {
      Object.defineProperty(navigator, 'onLine', { get: () => false, configurable: true })
      window.dispatchEvent(new Event('offline'))
    })
    await page.waitForTimeout(2000)
  }
  return { ctx, page }
}

const shot = async (page, name) => {
  await page.screenshot({ path: `${OUT}/${name}.png` })
  console.log(`  ${name}`)
}

// mail — a message open, so the reading pane is not the empty state
{
  const { ctx, page } = await open()
  await page.getByText('Re: Q3 roadmap').first().click()
  await page.waitForTimeout(2500)
  await shot(page, 'mail')
  await ctx.close()
}

// offline — the network panel over a message list that is still readable
{
  const { ctx, page } = await open({ offline: true })
  await page.getByRole('button', { name: 'Sync and network status' }).first().click()
  await page.waitForTimeout(2000)
  await shot(page, 'offline')
  await ctx.close()
}

// the workspace tabs
for (const [label, name] of [['Calendar', 'calendar'], ['Contacts', 'contacts'], ['Todo', 'tasks']]) {
  const { ctx, page } = await open()
  await page.getByRole('button', { name: label, exact: true }).first().click()
  await page.waitForTimeout(1800)
  // Contacts opens on an empty detail pane. Pick someone, so the picture shows
  // the card rather than the "select a contact" placeholder.
  if (name === 'contacts') {
    await page.getByText('Amara Diallo').first().click()
    await page.waitForTimeout(1800)
  }
  await shot(page, name)
  await ctx.close()
}

// composer
{
  const { ctx, page } = await open()
  await page.getByRole('button', { name: 'New Mail', exact: true }).first().click()
  await page.waitForTimeout(2500)
  await shot(page, 'composer')
  await ctx.close()
}

// settings — it opens on Appearance, so that one needs no click. The sidebar
// entries are plain text; the only buttons in there are the "Expand" chevrons.
for (const [label, name] of [[null, 'appearance'], ['Security', 'privacy'], ['General', 'keyboard']]) {
  const { ctx, page } = await open()
  await page.goto(`${URL}/settings`, { waitUntil: 'domcontentloaded' })
  await page.addStyleTag({ content: '.demo-badge{display:none !important}' })
  await page.waitForTimeout(2500)
  if (label) {
    await page.getByText(label, { exact: true }).first().click()
    await page.waitForTimeout(1800)
  }
  await shot(page, name)
  await ctx.close()
}

// signin — a context with no seeded account lands on the add-an-account screen
{
  const ctx = await browser.newContext({
    viewport: { width: 1600, height: 1000 },
    deviceScaleFactor: 2,
  })
  await ctx.addInitScript(t => {
    localStorage.setItem('theme_mode', 'manual')
    localStorage.setItem('theme_name', t)
  }, THEME)
  const page = await ctx.newPage()
  await page.goto(`${URL}/dashboard`, { waitUntil: 'domcontentloaded' })
  await page.waitForTimeout(4000)
  await shot(page, 'signin')
  await ctx.close()
}

await browser.close()
