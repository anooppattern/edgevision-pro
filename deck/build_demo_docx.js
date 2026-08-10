// EdgeVision demo script -> Word (.docx). Plain, simple black-and-white layout —
// no brand colours. Same content as the PDF runbook. No pre-recorded-video wording.
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, LevelFormat, HeadingLevel,
} = require('docx');

const INK = "000000";
const GREY = "444444";

const OUT = "/home/user/edgevision-pro/deck/EdgeVision-Demo-Script.docx";

// ---- content -----------------------------------------------------------
const CHECKLIST = [
 "Laptop connected to the projector; screen mirrored and tested. Sound on — a couple of steps have an alert chime.",
 "Each part of the demo is open and lined up in order, full-screen. Know which step comes next before you start.",
 "Close every other tab and notification. Nothing should pop up while you present.",
 "Keep this sheet where you can see it. You tell the story; the screen shows the proof.",
 "Open with one line: “What you’re about to see is our software running on everyday store and restaurant cameras.”",
];

// step: [num, title, time, rows[[label,text]...]]
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

const FABRIC = [
 [1,"Reading the kitchen line","0:50",[
   ["Show","The counter where food is made — a box on each item, with a simple label: there, correct, or not right."],
   ["Say","“Same idea, now in a restaurant. Our software watches the counter where food is made. It doesn’t just see a burger — it checks the build: is every item there, and is it right?”"],
   ["Point","Point to one item and its label."]]],
 [2,"It catches the mistake — and fixes it","1:10",[
   ["Show","An order is missing an item; an alert pops up on the kitchen screen with a chime; the item is added and the order clears."],
   ["Say","“This is the important part. This order is missing a sauce. The screen flags it straight away, before the bag goes out. The team add it, the software checks again, and the order is cleared. A wrong order caught in seconds — not after the customer complains.”"],
   ["Point","Follow it on screen: the alert, then the green ‘all correct’ once it’s fixed."]]],
 [3,"Two signals are better than one","0:50",[
   ["Show","The camera view next to the fryer reading and the order screen."],
   ["Say","“Here’s something a camera alone can’t do. The fryer says the food is cooked. The camera says it still looks pale. Put the two together and you learn the fryer is running cool — a problem you’d never catch by eye until customers did.”"],
   ["Point","Point to the two readings that disagree."]]],
 [4,"The numbers a manager cares about","0:45",[
   ["Show","The dashboard — service speed, order accuracy, and food-safety checks, by shift and station."],
   ["Say","“It all adds up to the numbers an owner runs on — how fast service is, how accurate orders are, and food-safety checks — for every shift and every station, ready for the next audit.”"],
   ["Point","Point to the speed, accuracy, and safety tiles."]]],
 [5,"Recap + hand back","0:20",[
   ["Say","“Counting things is easy. The real difference is that it understands what’s happening — and speaks up in time to fix it. That’s Fabric Lens.”"]]],
];

const CLOSE = [
 "Bring it home: “Two products, one platform. It runs on your existing cameras, on a small box on-site. Nothing goes to the cloud.”",
 "The ask: “Give us three weeks in one of your stores and we’ll show you these same results on your own floor.”",
 "Then pause and take questions — the quick answers are below.",
];

const QA = [
 ["Is this recording faces?","No faces are saved and no video leaves the site. Everything is worked out on the box inside your store."],
 ["Won’t it cry wolf?","Every alert comes with a short clip so a person can glance and confirm. You set how sensitive it is, per site."],
 ["Does it need new cameras?","No — it uses the cameras you already have. Just one small box added on-site."],
 ["Does it need the internet?","No. It keeps working even if the internet goes down, because everything runs locally."],
 ["How does it fit our systems?","It plugs into your billing / kitchen screens and can send alerts to a phone or WhatsApp."],
 ["How soon do we see results?","A three-week trial in one location — real results on your own floor by week three."],
];

function total(steps){
  let t=0; steps.forEach(s=>{const [m,sec]=s[2].split(":").map(Number); t+=m*60+sec;});
  return `${Math.floor(t/60)}:${String(t%60).padStart(2,"0")}`;
}

// ---- helpers -----------------------------------------------------------
function noBorders(){
  const none={ style:BorderStyle.NONE, size:0, color:"FFFFFF" };
  return { top:none,bottom:none,left:none,right:none,insideHorizontal:none,insideVertical:none };
}

// two-column cue row: label (bold) | text
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
    spacing:{ before:200, after:40 },
    tabStops:[{ type:"right", position:9360 }],
    children:[
      new TextRun({ text:`${num}. ${title}`, bold:true, size:22, color:INK }),
      new TextRun({ text:`\t(${time})`, size:18, color:GREY }),
    ],
  });
  const tbl = new Table({
    width:{ size:9360, type:WidthType.DXA },
    columnWidths:[1000,8360],
    borders: noBorders(),
    rows: rows.map(([l,t])=>stepRow(l,t)),
  });
  return [header, tbl];
}

function sectionHeading(text, right){
  return new Paragraph({
    spacing:{ before:300, after:120 },
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

// title
children.push(new Paragraph({ spacing:{ after:40 },
  children:[ new TextRun({ text:"EdgeVision — Demo Script", bold:true, size:34, color:INK }) ] }));
children.push(new Paragraph({ spacing:{ after:40 },
  children:[ new TextRun({ text:"RetailTrack + Fabric Lens · Intel Event", size:20, color:GREY }) ] }));
children.push(new Paragraph({ spacing:{ after:200 },
  border:{ bottom:{ color:"999999", space:6, style:BorderStyle.SINGLE, size:6 } },
  children:[ new TextRun({ text:"About 8–9 minutes · Pattern AI Labs", size:18, color:GREY }) ] }));

// intro
children.push(new Paragraph({ spacing:{ after:120, line:280 }, children:[
  new TextRun({ text:"Three cues per step — ", size:20, color:INK }),
  new TextRun({ text:"Show", bold:true, size:20, color:INK }),
  new TextRun({ text:" what’s on the screen, ", size:20, color:INK }),
  new TextRun({ text:"Say", bold:true, size:20, color:INK }),
  new TextRun({ text:" it in your own words, ", size:20, color:INK }),
  new TextRun({ text:"Point", bold:true, size:20, color:INK }),
  new TextRun({ text:" to what matters. Learn the ideas, not the exact wording. Speak slowly, and give each screen a moment to land before you move on.", size:20, color:INK }),
]}));

// checklist
children.push(sectionHeading("Before you start"));
bulletList(CHECKLIST).forEach(p=>children.push(p));

// Part A
children.push(sectionHeading("Part A — RetailTrack (the store floor)", total(RETAIL)));
RETAIL.forEach(s=> stepBlock(...s).forEach(p=>children.push(p)));

// Part B
children.push(sectionHeading("Part B — Fabric Lens (the restaurant line)", total(FABRIC)));
FABRIC.forEach(s=> stepBlock(...s).forEach(p=>children.push(p)));

// How to close
children.push(sectionHeading("How to close"));
bulletList(CLOSE).forEach(p=>children.push(p));

// Q&A
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

Packer.toBuffer(doc).then(buf=>{
  fs.writeFileSync(OUT, buf);
  console.log("WROTE", OUT, "| RetailTrack", total(RETAIL), "| Fabric Lens", total(FABRIC));
});
