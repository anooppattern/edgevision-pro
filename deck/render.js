const { chromium } = require('/tmp/claude-0/-home-user-edgevision-pro/436fd082-261e-51d6-8eb6-5a0fa453e8f2/scratchpad/fonts/node_modules/playwright-core');
const path = require('path');

(async () => {
  const htmlPath = 'file:///home/user/edgevision-pro/deck/index.html';
  const out = '/home/user/edgevision-pro/deck/EdgeVision-Fabric-Lens.pdf';
  const browser = await chromium.launch({
    executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
    args: ['--no-sandbox', '--font-render-hinting=none'],
  });
  const page = await browser.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('PAGEERR: ' + e.message));
  page.on('requestfailed', r => errors.push('REQFAIL: ' + r.url() + ' :: ' + (r.failure()||{}).errorText));
  await page.goto(htmlPath, { waitUntil: 'networkidle', timeout: 60000 });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(400);
  // report any images that failed to load
  const imgInfo = await page.evaluate(() => {
    const imgs = Array.from(document.images);
    return {
      total: imgs.length,
      broken: imgs.filter(i => !i.complete || i.naturalWidth === 0).map(i => i.getAttribute('src')),
    };
  });
  await page.pdf({
    path: out,
    printBackground: true,
    preferCSSPageSize: true,
    pageRanges: '',
  });
  await browser.close();
  console.log('IMAGES total=%d broken=%d %s', imgInfo.total, imgInfo.broken.length, JSON.stringify(imgInfo.broken));
  if (errors.length) console.log('ERRORS:\n' + errors.slice(0,20).join('\n'));
  console.log('WROTE ' + out);
})().catch(e => { console.error(e); process.exit(1); });
