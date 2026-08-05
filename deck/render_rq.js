const { chromium } = require('./fonts/node_modules/playwright-core');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox','--font-render-hinting=none'] });
  const page = await browser.newPage();
  await page.goto('file:///home/user/edgevision-pro/deck/EdgeVision-Retail-QSR.html', { waitUntil: 'networkidle', timeout:60000 });
  await page.evaluate(() => document.fonts.ready);
  const over = await page.evaluate(() => Array.from(document.querySelectorAll('.slide')).map((s,i)=>{
    const b=s.querySelector('.slide__body'); const o=b?b.scrollHeight-b.clientHeight:0;
    return {n:i+1,o}; }).filter(x=>x.o>2));
  const imgs = await page.evaluate(()=>Array.from(document.images).filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.getAttribute('src')));
  console.log('OVERFLOW', JSON.stringify(over));
  console.log('BROKEN', JSON.stringify(imgs));
  await page.pdf({ path:'/home/user/edgevision-pro/deck/EdgeVision-Retail-QSR.pdf', printBackground:true, preferCSSPageSize:true, width:'13.333in', height:'7.5in', margin:{top:0,right:0,bottom:0,left:0} });
  await browser.close();
  console.log('WROTE pdf');
})();
