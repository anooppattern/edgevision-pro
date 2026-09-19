const pptxgen = require('/tmp/claude-0/-home-user-edgevision-pro/436fd082-261e-51d6-8eb6-5a0fa453e8f2/scratchpad/node_modules/pptxgenjs');
const fs=require('fs'),path=require('path');
const IMGDIR='/tmp/claude-0/-home-user-edgevision-pro/436fd082-261e-51d6-8eb6-5a0fa453e8f2/scratchpad/img_koc'; const OUT='/home/user/edgevision-pro/deck/EdgeVision-Kochi-Pitch.pptx';
const notes=[
"Welcome, everyone. We're Pattern AI Labs. EdgeVision is simple: it takes the cameras you already have and turns them into a smart teammate — for shops and for restaurants. Give me 15 minutes and I'll show you how.",
"Every shop and restaurant records hours of video. But no one can watch it all. So it only helps AFTER something goes wrong — a complaint, a loss, a bad review. The footage is there, but it doesn't help you in the moment.",
"So here's our simple idea. What if every camera could actually think? Not just record — but understand what's happening and tell your team what to do, right now.",
"It's easy to start. Four steps: connect to your existing cameras; it watches every feed all day; it understands the whole scene, not just movement; and it sends your team a clear alert in seconds. No new cameras, no cloud — one small box in the store.",
"Let's start with shops. On a store floor, small moments decide every sale. EdgeVision helps you catch them as they happen.",
"A few real examples. One: see where shoppers go and linger, so you place products where people actually walk. Two: get an alert the moment a billing queue builds, so you open a counter before anyone leaves. Three: know every section has staff, so customers get help fast.",
"Here's a favourite. A loyal customer walks in, and the manager's phone lights up with their name and what to offer — so they get a warm welcome in seconds. It's all worked out inside the store, and no faces are ever saved.",
"Now restaurants. Every shift lives on three things — speed, correct orders, and safety. EdgeVision watches all three, live.",
"Again, real examples. One: check the order and catch a wrong or missing item before the bag goes out. Two: spot queues and slow stations and move staff before guests get annoyed. Three: check gloves, handwashing and hygiene all the time, so you're always audit-ready.",
"The big one: it catches a missing item before the bag leaves the counter. It reads the order, sees what's on the tray, and flags the gap instantly — so the mistake is fixed before the customer ever notices.",
"Old cameras just count — 'a person entered', 'motion in aisle 4'. EdgeVision understands — 'a regular came in, greet them', 'spill in aisle 4, send someone', 'this order is missing a sauce'. That's the difference: it doesn't just watch, it helps.",
"One thing people always ask about is privacy. Everything stays inside your store, on one small Intel box. No faces are saved, nothing goes to the cloud, and it keeps working even if the internet drops.",
"That's EdgeVision. The best way to see it is on your own floor. Pick one shop or one restaurant, give us three weeks, and we'll show you real results — with zero risk. Here are our details. Thank you — I'd love to take your questions.",
];
const pres=new pptxgen(); pres.defineLayout({name:'PPT16x9',width:13.333,height:7.5}); pres.layout='PPT16x9';
pres.author='Pattern AI Labs'; pres.company='Pattern AI Labs'; pres.title='EdgeVision — Kochi Pitch';
const files=fs.readdirSync(IMGDIR).filter(f=>/^slide-\d+\.png$/.test(f)).sort();
files.forEach((f,i)=>{const s=pres.addSlide(); s.background={color:'0A0A0E'};
 s.addImage({path:path.join(IMGDIR,f),x:0,y:0,w:13.333,h:7.5,sizing:{type:'cover',w:13.333,h:7.5}});
 if(notes[i]) s.addNotes(notes[i]);});
pres.writeFile({fileName:OUT}).then(()=>console.log('WROTE',OUT,files.length,'slides, notes:',notes.length)).catch(e=>{console.error(e);process.exit(1)});
