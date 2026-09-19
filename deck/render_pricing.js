const { chromium } = require('/tmp/claude-0/-home-user-edgevision-pro/436fd082-261e-51d6-8eb6-5a0fa453e8f2/scratchpad/fonts/node_modules/playwright-core');
(async () => {
  const b = await chromium.launch({ executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args:['--no-sandbox','--font-render-hinting=none'] });
  const p = await b.newPage();
  await p.goto('file:///home/user/edgevision-pro/deck/EdgeVision-Pricing.html',{waitUntil:'networkidle',timeout:60000});
  await p.evaluate(()=>document.fonts.ready);
  const over = await p.evaluate(()=>Array.from(document.querySelectorAll('.slide')).map((s,i)=>{const bd=s.querySelector('.slide__body');return {n:i+1,o:bd?bd.scrollHeight-bd.clientHeight:0};}).filter(x=>x.o>2));
  console.log('OVERFLOW',JSON.stringify(over));
  await p.pdf({path:'/home/user/edgevision-pro/deck/EdgeVision-Pricing.pdf',printBackground:true,preferCSSPageSize:true,width:'13.333in',height:'7.5in',margin:{top:0,right:0,bottom:0,left:0}});
  await b.close(); console.log('WROTE pdf');
})();
