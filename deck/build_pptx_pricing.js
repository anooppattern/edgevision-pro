const pptxgen = require('/tmp/claude-0/-home-user-edgevision-pro/436fd082-261e-51d6-8eb6-5a0fa453e8f2/scratchpad/fonts/node_modules/pptxgenjs');
const path='/tmp/claude-0/-home-user-edgevision-pro/436fd082-261e-51d6-8eb6-5a0fa453e8f2/scratchpad/priceimg/slide-01.png';
const OUT='/home/user/edgevision-pro/deck/EdgeVision-Pricing.pptx';
const pres=new pptxgen();
pres.defineLayout({name:'PPT16x9',width:13.333,height:7.5}); pres.layout='PPT16x9';
pres.author='Pattern AI Labs'; pres.company='Pattern AI Labs'; pres.title='EdgeVision — Pricing';
const s=pres.addSlide(); s.background={color:'000000'};
s.addImage({path,x:0,y:0,w:13.333,h:7.5,sizing:{type:'cover',w:13.333,h:7.5}});
pres.writeFile({fileName:OUT}).then(()=>console.log('WROTE',OUT)).catch(e=>{console.error(e);process.exit(1)});
