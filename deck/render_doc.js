const { chromium } = require('/tmp/claude-0/-home-user-edgevision-pro/436fd082-261e-51d6-8eb6-5a0fa453e8f2/scratchpad/fonts/node_modules/playwright-core');
(async () => {
  const [src,out]=process.argv.slice(2);
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox','--font-render-hinting=none']});
  const p=await b.newPage();
  await p.goto('file://'+src,{waitUntil:'networkidle',timeout:60000});
  await p.evaluate(()=>document.fonts.ready);
  await p.pdf({path:out,printBackground:true,preferCSSPageSize:true});
  const pages=await p.evaluate(()=>document.querySelectorAll('table').length); // noop
  await b.close(); console.log('WROTE',out);
})();
