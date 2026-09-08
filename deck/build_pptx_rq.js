const pptxgen = require('/tmp/claude-0/-home-user-edgevision-pro/436fd082-261e-51d6-8eb6-5a0fa453e8f2/scratchpad/fonts/node_modules/pptxgenjs');
const fs=require('fs'), path=require('path');
const IMGDIR='/tmp/claude-0/-home-user-edgevision-pro/436fd082-261e-51d6-8eb6-5a0fa453e8f2/scratchpad/rqimg';
const OUT='/home/user/edgevision-pro/deck/EdgeVision-Retail-QSR.pptx';
const pres=new pptxgen();
pres.defineLayout({name:'PPT16x9',width:13.333,height:7.5}); pres.layout='PPT16x9';
pres.author='Pattern AI Labs'; pres.company='Pattern AI Labs'; pres.title='EdgeVision — Retail & QSR';
const ctx=['Cover','Ch.01 The Visibility Gap','The Challenge — store floor','Ch.02 The Platform',
 'The Solution — EdgeVision Platform','Live Operations Console','Ch.03 Two Lenses, One Network',
 'Customer & Staff Analytics','Detection at Work','Customer Analytics, elaborated','Heat Mapping',
 'VIP Recognition Flow','Staff Analytics, elaborated','The Hidden Loops (per-staff activity)',
 'Brand-Level Staff Heat Map','Retail — the long tail of use-cases','QSR Edition — From Counter to Drive-Thru',
 'QSR Capabilities — speed, accuracy, safety','QSR Drive-Thru Operations','QSR — every service window',
 'Ch.05 The Paradigm Shift','Why GenAI analytics changes everything','Hybrid Intelligence',
 'Edge-First Architecture','Hardware & Privacy','Engagement — three weeks','About Pattern AI Labs',
 'Contact — every store & line'];
const files=fs.readdirSync(IMGDIR).filter(f=>/^slide-\d+\.png$/.test(f)).sort();
files.forEach((f,i)=>{const s=pres.addSlide(); s.background={color:'000000'};
 s.addImage({path:path.join(IMGDIR,f),x:0,y:0,w:13.333,h:7.5,sizing:{type:'cover',w:13.333,h:7.5}});
 if(ctx[i]) s.addNotes(ctx[i]);});
pres.writeFile({fileName:OUT}).then(()=>console.log('WROTE',OUT,files.length,'slides')).catch(e=>{console.error(e);process.exit(1)});
