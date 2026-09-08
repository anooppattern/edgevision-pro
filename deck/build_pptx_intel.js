const pptxgen = require('/tmp/claude-0/-home-user-edgevision-pro/436fd082-261e-51d6-8eb6-5a0fa453e8f2/scratchpad/fonts/node_modules/pptxgenjs');
const fs=require('fs'), path=require('path');
const IMGDIR='/tmp/claude-0/-home-user-edgevision-pro/436fd082-261e-51d6-8eb6-5a0fa453e8f2/scratchpad/intelimg';
const OUT='/home/user/edgevision-pro/deck/EdgeVision-Retail-QSR-IntelTemplate.pptx';
const pres=new pptxgen();
pres.defineLayout({name:'PPT16x9',width:13.333,height:7.5}); pres.layout='PPT16x9';
pres.author='Pattern AI Labs'; pres.company='Pattern AI Labs'; pres.title='EdgeVision — Retail & QSR · Intel Template';
// Presenter talk-track (speaker notes) — ~30 min, non-technical room
const notes=[
"Open warm — thank them for the closed-room time. One line: 'We turn the cameras you already have into something that helps you run the store, in real time.' Set the frame: ~25 min, then open discussion.",
"Name the pain everyone feels: you've invested in cameras, but they only help AFTER something goes wrong. Quick show of hands: 'Who's reviewed footage only after a complaint?'",
"Three blind spots that cost money every day. Keep it conversational and tie each to their world — staffing, layout, service. These are exactly what we remove.",
"The shift in one sentence: cameras that think. Not more screens to watch — an AI teammate that tells your team what to do, right now.",
"Reassure the non-technical folks: nothing to rip out, no cloud, one small Intel box per site. Four simple steps — connect, watch, understand, act.",
"Move from features to outcomes. Pick the one that matters most to THIS room (sales, service, loss, or safety) and expand with a quick example.",
"Transition: 'Let's make it concrete — first, your stores.'",
"Same cameras, two answers: what the customer is experiencing, and how the team is performing. Speaks to GMs and ops leaders.",
"Retail use cases, customer side — one line each. Don't read them all; pause on the two or three that match this room and let them react.",
"Retail use cases, operations side — staffing, shrink, safety, compliance. Ask which of these currently costs them the most.",
"Managers don't want AI — they want ONE screen. Walk the live snapshot, the footfall trend, and the alert stream they'd actually act on. Make it feel like their morning huddle.",
"Tell it as a story: a gold-tier guest walks in, the manager's phone lights up, the right welcome happens in seconds. Stress privacy — no faces are stored.",
"Transition: 'Now your restaurants.'",
"Speed, accuracy, safety — the three things every QSR operator lives by. Tie to P&L and health/FSSAI audits.",
"QSR use cases, speed & accuracy — one line each, tied straight to revenue and throughput. Let operators point at their pain.",
"QSR use cases, safety & ops — PPE, handwash, hold-times, cleaning, labour. This is the audit-and-compliance story; great for multi-unit operators.",
"This is the WHY. Keep it plain: a Vision-Language Model reads a frame like a person would. THAT is why it can judge quality and context, not just detect motion. Don't go deep on the tech — one or two sentences.",
"The contrast lands the point — old cameras count, GenAI understands. Read one example out loud; it always gets a nod.",
"Make it their money. Pick the lever that matters most to this room and do the quick mental math with them — small lifts on traffic they already have. Invite them to plug in their own numbers.",
"Handle the two objections head-on: privacy and IT. Nothing leaves the store; it runs on Intel. Lean into the Intel partnership — we're at their event.",
"Credibility: Intel Edge AI Partner, production computer vision at scale, purpose-built for retail + QSR. Names they'll recognise.",
"Clear ask: pick ONE location, 3-week pilot, see live results with zero risk to the rest of the estate. Close with: 'Which location should we start with?'",
];
const files=fs.readdirSync(IMGDIR).filter(f=>/^slide-\d+\.png$/.test(f)).sort();
files.forEach((f,i)=>{const s=pres.addSlide(); s.background={color:'000000'};
 s.addImage({path:path.join(IMGDIR,f),x:0,y:0,w:13.333,h:7.5,sizing:{type:'cover',w:13.333,h:7.5}});
 if(notes[i]) s.addNotes(notes[i]);});
pres.writeFile({fileName:OUT}).then(()=>console.log('WROTE',OUT,files.length,'slides')).catch(e=>{console.error(e);process.exit(1)});
