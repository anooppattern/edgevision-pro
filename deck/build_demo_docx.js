// EdgeVision demo script -> Word (.docx). Plain black-and-white, no brand colours.
// Single doc, BOTH demos: Part A RetailTrack (existing store-floor content) and
// Part B Fabric Lens (matches the recorded QSR software: Live Wall, Stations 1-3,
// Ops Board, Inventory, Insights & Alerts — Store #1234).
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, LevelFormat,
} = require('docx');

const INK = "000000";
const GREY = "444444";
const OUT = "/home/user/edgevision-pro/deck/EdgeVision-Demo-Script.docx";

// ---- content -----------------------------------------------------------
const CHECKLIST = [
 "Laptop connected to the projector; screen mirrored and tested. Sound on — some steps have an alert chime.",
 "Both apps open and full-screen: RetailTrack (the store floor) and Fabric Lens (the kitchen). Know which you’re showing.",
 "Each part of the walkthrough is queued in order. Know which screen comes next before you start.",
 "Close every other tab and notification. Nothing should pop up while you present.",
 "Keep this sheet where you can see it. You tell the story; the screen shows the proof.",
 "Open with one line: “This is our software running live — the same idea in a store and in a kitchen.”",
];

// Part A — RetailTrack (existing store-floor content)
const RETAIL = [
 [1,"People, seen clearly","0:45",[
   ["Show","Store floor — coloured boxes follow each person; staff in amber, customers in cyan."],
   ["Say","“This is a normal store camera. Our software marks every person — amber for your staff, cyan for a customer. It does this on its own, and it never saves anyone’s face.”"],
   ["Point","Point to one amber box and one cyan box as they move."]]],
 [2,"One screen for the manager","0:45",[
   ["Show","The manager’s screen — people in today, staff on the floor, alerts, and a busy-hours chart."],
   ["Say","“This is the only screen a manager needs. How many people came in, how many staff are on the floor, what needs attention now, and the busy hours — all on one page.”"],
   ["Point","Trace the busy-hours line with your finger and stop on the tallest point."]]],
 [3,"Where people spend time","0:45",[
   ["Show","The heat-map — busy spots glow red; a list shows the top areas."],
   ["Say","“The red areas are where customers actually stop and spend time. Here, the brand wall pulls the most, the entrance the least. Now you can put your best products where people really go — not where you guessed.”"],
   ["Point","Point to the hottest area, then the coldest."]]],
 [4,"Spotting your best customer","1:00",[
   ["Show","A loyalty customer walks in; a message pops up on the phone with their name, level, and last visit."],
   ["Say","“Watch the phone. A loyalty customer just walked in, and the manager’s phone shows who they are, their level, and what to offer. Now they get a warm welcome instead of walking past unnoticed.”"],
   ["Point","When the message appears, point to the name and level. All of this is worked out inside the store."]]],
 [5,"Small problems, caught early","0:45",[
   ["Show","Alerts appear — “section left unattended”, “queue building at till 2”, “too many staff in the back”."],
   ["Say","“The same cameras watch the floor for you. An empty section, a growing queue, too many staff in the back — the manager gets a quiet nudge while there’s still time to fix it.”"],
   ["Point","Read out one or two alerts as they appear."]]],
 [6,"Quick recap","0:20",[
   ["Say","“Same cameras, two jobs — help the customer, and help your team. It all runs on one small box inside the store, and nothing leaves the building.”"]]],
];

// Part B — Fabric Lens (matches the recorded QSR software)
const FABRIC = [
 [1,"The whole restaurant on one screen","0:30",[
   ["Show","The Live Wall — every camera at once: the make-line stations, the fryer, the storeroom shelves, and the back door."],
   ["Say","“This is the whole restaurant on one screen — the front line, the fryer, the storeroom, even the delivery door. One system watches all of it, live. Everything I show next is happening on these same cameras.”"],
   ["Point","Point out a make-line station, the fryer, and the storeroom shelves."]]],
 [2,"Station 1 — is the order right?","1:00",[
   ["Show","Station 1, looking down at the box. It reads the ticket (a Box Combo) and checks every item. A red line appears: “Drop a slice of Texas toast in the box.”"],
   ["Say","“Station one checks the order before it’s bagged. The camera reads the ticket and counts what’s actually in the box — and it’s caught a missing Texas toast. The screen tells the team exactly what to add.”"],
   ["Point","Point to the alert line, then to the ticket checklist on the right."],
   ["Show","The toast goes in; the team taps Re-check; the panel turns green — “Order complete · Ready, bag it.”"],
   ["Say","“They add it, re-check, and it clears to green. A wrong order fixed before it ever left the counter.”"]]],
 [3,"Station 2 — is it cooked right?","0:45",[
   ["Show","Station 2, two cooked tenders side by side, graded against the ideal. Batch score 95%. One is flagged: “Pull the over-fried tender, drop a fresh one.”"],
   ["Say","“Station two grades how the food is cooked. It compares each piece to the ideal — colour, size, how well it’s fried. Here it’s spotted one that’s over-fried and says: pull it, drop a fresh one. That’s quality no busy line can watch by eye.”"],
   ["Point","Point to the two tenders and the batch score."]]],
 [4,"Station 3 — was it built in the right order?","0:45",[
   ["Show","Station 3, the build shown as a strip of steps. A step is missing: “Add sauce to the order before bag.” The item is tagged “without sauce.”"],
   ["Say","“Station three watches how the food is built, step by step. This order was about to be bagged without its sauce — the system catches it and asks for it before the bag closes. When it’s right, it shows ‘SOP compliant.’”"],
   ["Point","Point to the step strip, then the ‘add sauce’ flag."]]],
 [5,"Ops Board — every order, scored live","0:50",[
   ["Show","Operations, Store #1234. A live list — every ticket, its channel (drive-thru, dine-in, mobile) and a score for order accuracy, quality, and prep. Along the top: throughput 41/hr, average order time 2m 47s, fryer oil 342°F, 14 open alerts."],
   ["Say","“Everything rolls up here — every order, from every channel, scored as it happens. Green is clean, red needs a look. The manager sees the whole shift on one screen — even the fryer temperature and how long orders are taking.”"],
   ["Point","Run your finger down the ticket list; stop on a red ‘re-check’ row."]]],
 [6,"The back of house, too","0:40",[
   ["Show","Inventory — the storeroom shelves tracking stock (crinkle fries, tenders), the fryer, and the receiving door as deliveries arrive."],
   ["Say","“It’s not just the front line. The same system watches the storeroom and the back door — what’s on the shelf, what’s running low, and what’s just been delivered. One platform, front to back.”"],
   ["Point","Point to a tracked box on the shelf, then the receiving-door camera."]]],
 [7,"The numbers that add up","0:35",[
   ["Show","Insights and Alerts — the shift’s key numbers (accuracy, speed, food safety, waste) and a live list of what needs attention."],
   ["Say","“And it adds up to the numbers a manager and an owner actually use — accuracy, speed, food safety, waste — with a live list of what needs a look. Ready for the next audit, with nobody filling in a clipboard.”"],
   ["Point","Point to one number, then the alert list."]]],
 [8,"Recap","0:20",[
   ["Say","“Same cameras, the whole restaurant. It doesn’t just watch — it catches the missing toast, the over-fried tender, the forgotten sauce, and fixes them before the customer ever sees. That’s Fabric Lens.”"]]],
];

const CLOSE = [
 "Bring it home: “Two products, one platform. It runs on your existing cameras, on a small box on-site. Nothing goes to the cloud.”",
 "The ask: “Give us three weeks in one store or one restaurant and we’ll show you these same results on your own floor.”",
 "Then pause and take questions — the quick answers are below.",
];

const QA = [
 ["Is this recording faces?","No faces are stored and no video leaves the site. In the store it only matches loyalty opt-ins; in the kitchen it scores the food, not the person. Everything runs on the box on-site."],
 ["Won’t it cry wolf?","Every alert comes with the picture, so a person can glance and confirm. You set how strict it is, per site and per station."],
 ["Does it need new cameras?","No — it uses the cameras you already have. Just one small box added on-site."],
 ["Does it need the internet?","No. It keeps working even if the internet goes down, because everything runs locally."],
 ["How does it fit our systems?","It connects to your POS / kitchen screens and can send alerts to a screen or a phone."],
 ["How soon do we see results?","A three-week trial in one location — real results on your own floor by week three."],
];

function total(steps){
  let t=0; steps.forEach(s=>{const [m,sec]=s[2].split(":").map(Number); t+=m*60+sec;});
  return `${Math.floor(t/60)}:${String(t%60).padStart(2,"0")}`;
}
function grandTotal(){
  let t=0; [RETAIL,FABRIC].forEach(g=>g.forEach(s=>{const [m,sec]=s[2].split(":").map(Number); t+=m*60+sec;}));
  return `${Math.floor(t/60)}:${String(t%60).padStart(2,"0")}`;
}

// ---- helpers -----------------------------------------------------------
function noBorders(){
  const none={ style:BorderStyle.NONE, size:0, color:"FFFFFF" };
  return { top:none,bottom:none,left:none,right:none,insideHorizontal:none,insideVertical:none };
}
function stepRow(label, text){
  const isSay = label==="Say", isPoint = label==="Point";
  return new TableRow({ children:[
    new TableCell({ width:{ size:1000, type:WidthType.DXA }, margins:{ top:30,bottom:30,left:0,right:160 },
      borders: noBorders(), children:[
      new Paragraph({ children:[ new TextRun({ text:label, bold:true, size:20, color:INK }) ] }) ] }),
    new TableCell({ width:{ size:8360, type:WidthType.DXA }, margins:{ top:30,bottom:30,left:0,right:0 },
      borders: noBorders(), children:[
      new Paragraph({ spacing:{ line:264 }, children:[
        new TextRun({ text, size: isSay?21:20, color: INK, italics: isPoint }) ] }) ] }),
  ]});
}
function stepBlock(num, title, time, rows){
  const header = new Paragraph({
    spacing:{ before:220, after:40 },
    tabStops:[{ type:"right", position:9360 }],
    children:[
      new TextRun({ text:`${num}. ${title}`, bold:true, size:22, color:INK }),
      new TextRun({ text:`\t(${time})`, size:18, color:GREY }),
    ],
  });
  const tbl = new Table({ width:{ size:9360, type:WidthType.DXA }, columnWidths:[1000,8360],
    borders: noBorders(), rows: rows.map(([l,t])=>stepRow(l,t)) });
  return [header, tbl];
}
function sectionHeading(text, right){
  return new Paragraph({
    spacing:{ before:320, after:120 },
    border:{ bottom:{ color:INK, space:4, style:BorderStyle.SINGLE, size:8 } },
    tabStops: right ? [{ type:"right", position:9360 }] : undefined,
    children:[
      new TextRun({ text, bold:true, size:24, color:INK }),
      ...(right ? [ new TextRun({ text:`\tabout ${right}`, size:18, color:GREY }) ] : []),
    ],
  });
}
function bulletList(items){
  return items.map((it,i)=> new Paragraph({
    spacing:{ after: i===items.length-1?0:80, line:264 },
    bullet:{ level:0 },
    children:[ new TextRun({ text:it, size:20, color:INK }) ],
  }));
}

// ---- build -------------------------------------------------------------
const children = [];
children.push(new Paragraph({ spacing:{ after:40 },
  children:[ new TextRun({ text:"EdgeVision — Demo Script", bold:true, size:34, color:INK }) ] }));
children.push(new Paragraph({ spacing:{ after:40 },
  children:[ new TextRun({ text:"RetailTrack + Fabric Lens · live software walkthrough · Intel Event", size:20, color:GREY }) ] }));
children.push(new Paragraph({ spacing:{ after:200 },
  border:{ bottom:{ color:"999999", space:6, style:BorderStyle.SINGLE, size:6 } },
  children:[ new TextRun({ text:`About ${grandTotal()} for both · Pattern AI Labs`, size:18, color:GREY }) ] }));

children.push(new Paragraph({ spacing:{ after:120, line:280 }, children:[
  new TextRun({ text:"Three cues per step — ", size:20, color:INK }),
  new TextRun({ text:"Show", bold:true, size:20, color:INK }),
  new TextRun({ text:" what’s on the screen, ", size:20, color:INK }),
  new TextRun({ text:"Say", bold:true, size:20, color:INK }),
  new TextRun({ text:" it in your own words, ", size:20, color:INK }),
  new TextRun({ text:"Point", bold:true, size:20, color:INK }),
  new TextRun({ text:" to what matters. Learn the ideas, not the exact wording. Speak slowly, and give each screen a moment to land before you move on.", size:20, color:INK }),
]}));

children.push(sectionHeading("Before you start"));
bulletList(CHECKLIST).forEach(p=>children.push(p));

children.push(sectionHeading("Part A · RetailTrack — the store floor", total(RETAIL)));
RETAIL.forEach(s=> stepBlock(...s).forEach(p=>children.push(p)));

children.push(sectionHeading("Part B · Fabric Lens — the restaurant line", total(FABRIC)));
FABRIC.forEach(s=> stepBlock(...s).forEach(p=>children.push(p)));

children.push(sectionHeading("How to close"));
bulletList(CLOSE).forEach(p=>children.push(p));

children.push(sectionHeading("If someone asks — simple answers"));
QA.forEach(([q,a])=>{
  children.push(new Paragraph({ spacing:{ before:120, after:20 },
    children:[ new TextRun({ text:q, bold:true, size:20, color:INK }) ] }));
  children.push(new Paragraph({ spacing:{ after:20, line:264 },
    children:[ new TextRun({ text:a, size:20, color:INK }) ] }));
});

const doc = new Document({
  creator:"Pattern AI Labs",
  title:"EdgeVision — Demo Script",
  styles:{ default:{ document:{ run:{ font:"Calibri", color:INK, size:20 } } } },
  numbering:{ config:[{ reference:"b", levels:[{ level:0, format:LevelFormat.BULLET, text:"•",
    alignment:AlignmentType.LEFT, style:{ paragraph:{ indent:{ left:340, hanging:200 } } } }] }] },
  sections:[{
    properties:{ page:{ size:{ width:12240, height:15840 }, margin:{ top:1080, bottom:1080, left:1440, right:1440 } } },
    children,
  }],
});
Packer.toBuffer(doc).then(buf=>{ fs.writeFileSync(OUT, buf);
  console.log("WROTE", OUT, "| RetailTrack", total(RETAIL), "| Fabric Lens", total(FABRIC), "| both", grandTotal()); });
