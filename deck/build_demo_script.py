# -*- coding: utf-8 -*-
"""EdgeVision demo script (RetailTrack + Fabric Lens) — printable runbook.
Single doc, both demos. Part A RetailTrack = existing store-floor content;
Part B Fabric Lens matches the recorded QSR software (Store #1234): Live Wall,
Stations 1-3, Ops Board, Insights & Alerts. Plain language, three cues
per step (SHOW / SAY / POINT) so a presenter can learn and deliver it naturally."""
import html, os
OUT="/home/user/edgevision-pro/deck/EdgeVision-Demo-Script.html"
def esc(s): return html.escape(s, quote=False)

CHECKLIST=[
 "Laptop connected to the projector; screen mirrored and tested. Sound ON — some steps have an alert chime.",
 "Both apps open and full-screen: RetailTrack (the store floor) and Fabric Lens (the kitchen). Know which you’re showing.",
 "Each part of the walkthrough is queued in order. Know which screen comes next before you start.",
 "Close every other tab and notification. Nothing should pop up while you present.",
 "Keep this sheet where you can see it. You tell the story; the screen shows the proof.",
 "Open with one line: “This is our software running live — the same idea in a store and in a kitchen.”",
]

# (num, title, time, [(label,text)...])   labels: SHOW / SAY / POINT
# Part A — RetailTrack (existing store-floor content)
RETAIL=[
 (1,"People, seen clearly","0:45",[
   ("SHOW","Store floor — coloured boxes follow each person; staff in amber, customers in cyan."),
   ("SAY","“This is a normal store camera. Our software marks every person — amber for your staff, cyan for a customer. It does this on its own, and it never saves anyone’s face.”"),
   ("POINT","Point to one amber box and one cyan box as they move.")]),
 (2,"One screen for the manager","0:45",[
   ("SHOW","The manager’s screen — people in today, staff on the floor, alerts, and a busy-hours chart."),
   ("SAY","“This is the only screen a manager needs. How many people came in, how many staff are on the floor, what needs attention now, and the busy hours — all on one page.”"),
   ("POINT","Trace the busy-hours line with your finger and stop on the tallest point.")]),
 (3,"Where people spend time","0:45",[
   ("SHOW","The heat-map — busy spots glow red; a list shows the top areas."),
   ("SAY","“The red areas are where customers actually stop and spend time. Here, the brand wall pulls the most, the entrance the least. Now you can put your best products where people really go — not where you guessed.”"),
   ("POINT","Point to the hottest area, then the coldest.")]),
 (4,"Spotting your best customer","1:00",[
   ("SHOW","A loyalty customer walks in; a message pops up on the phone with their name, level, and last visit."),
   ("SAY","“Watch the phone. A loyalty customer just walked in, and the manager’s phone shows who they are, their level, and what to offer. Now they get a warm welcome instead of walking past unnoticed.”"),
   ("POINT","When the message appears, point to the name and level. All of this is worked out inside the store.")]),
 (5,"Small problems, caught early","0:45",[
   ("SHOW","Alerts appear — “section left unattended”, “queue building at till 2”, “too many staff in the back”."),
   ("SAY","“The same cameras watch the floor for you. An empty section, a growing queue, too many staff in the back — the manager gets a quiet nudge while there’s still time to fix it.”"),
   ("POINT","Read out one or two alerts as they appear.")]),
 (6,"Quick recap","0:20",[
   ("SAY","“Same cameras, two jobs — help the customer, and help your team. It all runs on one small box inside the store, and nothing leaves the building.”")]),
]

# Part B — Fabric Lens (matches the recorded QSR software)
FABRIC=[
 (1,"The whole restaurant on one screen","0:30",[
   ("SHOW","The Live Wall — every camera at once: the make-line stations, the fryer, the storeroom shelves, and the back door."),
   ("SAY","“This is the whole restaurant on one screen — the front line, the fryer, the storeroom, even the delivery door. One system watches all of it, live. Everything I show next is happening on these same cameras.”"),
   ("POINT","Point out a make-line station, the fryer, and the storeroom shelves.")]),
 (2,"Station 1 — is the order right?","1:00",[
   ("SHOW","Station 1, looking down at the box. It reads the ticket (a Box Combo) and checks every item. A red line appears: “Drop a slice of Texas toast in the box.”"),
   ("SAY","“Station one checks the order before it’s bagged. The camera reads the ticket and counts what’s actually in the box — and it’s caught a missing Texas toast. The screen tells the team exactly what to add.”"),
   ("POINT","Point to the alert line, then to the ticket checklist on the right."),
   ("SHOW","The toast goes in; the team taps Re-check; the panel turns green — “Order complete · Ready, bag it.”"),
   ("SAY","“They add it, re-check, and it clears to green. A wrong order fixed before it ever left the counter.”")]),
 (3,"Station 2 — is it cooked right?","0:45",[
   ("SHOW","Station 2, two cooked tenders side by side, graded against the ideal. Batch score 95%. One is flagged: “Pull the over-fried tender, drop a fresh one.”"),
   ("SAY","“Station two grades how the food is cooked. It compares each piece to the ideal — colour, size, how well it’s fried. Here it’s spotted one that’s over-fried and says: pull it, drop a fresh one. That’s quality no busy line can watch by eye.”"),
   ("POINT","Point to the two tenders and the batch score.")]),
 (4,"Station 3 — was it built in the right order?","0:45",[
   ("SHOW","Station 3, the build shown as a strip of steps. A step is missing: “Add sauce to the order before bag.” The item is tagged “without sauce.”"),
   ("SAY","“Station three watches how the food is built, step by step. This order was about to be bagged without its sauce — the system catches it and asks for it before the bag closes. When it’s right, it shows ‘SOP compliant.’”"),
   ("POINT","Point to the step strip, then the ‘add sauce’ flag.")]),
 (5,"Ops Board — every order, scored live","0:50",[
   ("SHOW","Operations, Store #1234. A live list — every ticket, its channel (drive-thru, dine-in, mobile) and a score for order accuracy, quality and prep. Along the top: throughput 41/hr, average order time 2m 47s, fryer oil 342°F, 14 open alerts."),
   ("SAY","“Everything rolls up here — every order, from every channel, scored as it happens. Green is clean, red needs a look. The manager sees the whole shift on one screen — even the fryer temperature and how long orders are taking.”"),
   ("POINT","Run your finger down the ticket list; stop on a red ‘re-check’ row.")]),
 (6,"The numbers that add up","0:35",[
   ("SHOW","Insights and Alerts — the shift’s key numbers (accuracy, speed, food safety, waste) and a live list of what needs attention."),
   ("SAY","“And it adds up to the numbers a manager and an owner actually use — accuracy, speed, food safety, waste — with a live list of what needs a look. Ready for the next audit, with nobody filling in a clipboard.”"),
   ("POINT","Point to one number, then the alert list.")]),
 (7,"Recap","0:20",[
   ("SAY","“Same cameras, the whole restaurant. It doesn’t just watch — it catches the missing toast, the over-fried tender, the forgotten sauce, and fixes them before the customer ever sees. That’s Fabric Lens.”")]),
]

CLOSE=[
 "Bring it home: “Two products, one platform. It runs on your existing cameras, on a small box on-site. Nothing goes to the cloud.”",
 "The ask: “Give us three weeks in one store or one restaurant and we’ll show you these same results on your own floor.”",
 "Then pause and take questions — the quick answers are below.",
]
QA=[
 ("Is this recording faces?","No faces are stored and no video leaves the site. In the store it only matches loyalty opt-ins; in the kitchen it scores the food, not the person. Everything runs on the box on-site."),
 ("Won’t it cry wolf?","Every alert comes with the picture, so a person can glance and confirm. You set how strict it is, per site and per station."),
 ("Does it need new cameras?","No — it uses the cameras you already have. Just one small box added on-site."),
 ("Does it need the internet?","No. It keeps working even if the internet goes down, because everything runs locally."),
 ("How does it fit our systems?","It connects to your POS / kitchen screens and can send alerts to a screen or a phone."),
 ("How soon do we see results?","A three-week trial in one location — real results on your own floor by week three."),
]

def step(n,title,time,rows):
    r=""
    for lab,txt in rows:
        cls="say" if lab=="SAY" else ("point" if lab=="POINT" else "rd")
        r+='<div class="row {c}"><span class="lab">{l}</span><span class="txt">{t}</span></div>'.format(
            c=cls,l=esc(lab),t=esc(txt))
    return ('<div class="step"><div class="sn">{n:02d}</div><div class="sc">'
        '<div class="sh"><h4>{title}</h4><span class="tm">{time}</span></div>{rows}</div></div>').format(
        n=n,title=esc(title),time=esc(time),rows=r)

def steps_total(steps):
    tot=0
    for _,_,t,_ in steps:
        m,s=t.split(":"); tot+=int(m)*60+int(s)
    return "{}:{:02d}".format(tot//60,tot%60)

CSS="""
@page{size:210mm 297mm;margin:12mm 13mm 11mm}
*{box-sizing:border-box}
body{margin:0;font-family:'Inter',system-ui,sans-serif;color:#17171c;font-weight:300;line-height:1.4;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
header{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid #F52E67;
  padding-bottom:9px;margin-bottom:12px}
.h-l b{font-weight:700;font-size:16pt;color:#111;letter-spacing:.01em}
.h-l span{display:block;font-family:'JetBrains Mono',monospace;font-size:7.5pt;letter-spacing:.18em;
  text-transform:uppercase;color:#F52E67;margin-top:3px}
.h-r{text-align:right;font-family:'JetBrains Mono',monospace;font-size:7.5pt;letter-spacing:.1em;color:#6a6a72;line-height:1.6}
.h-r b{color:#111;font-size:9pt}
.intro{font-size:8.8pt;color:#44444c;margin:0 0 12px;line-height:1.5}
.intro b{color:#111;font-weight:600}
.sec{font-family:'JetBrains Mono',monospace;font-size:8.5pt;letter-spacing:.2em;text-transform:uppercase;
  color:#F52E67;margin:16px 0 9px;display:flex;align-items:center;gap:11px}
.sec::before{content:"";width:26px;height:2px;background:#F52E67}
.sec .t{color:#9a9aa2;letter-spacing:.12em;margin-left:auto;font-size:7.5pt}
.box{border:1px solid #e6e6ea;border-left:3px solid #F52E67;background:#faf9fb;padding:11px 14px;margin:0 0 12px}
.box h5{margin:0 0 6px;font-size:8.5pt;font-family:'JetBrains Mono',monospace;letter-spacing:.16em;
  text-transform:uppercase;color:#111}
.box ul{margin:0;padding:0;list-style:none}
.box li{position:relative;padding:2.5px 0 2.5px 16px;font-size:8.7pt;color:#33333a}
.box li::before{content:"";position:absolute;left:2px;top:8px;width:5px;height:5px;border-radius:50%;background:#F52E67}
.step{display:grid;grid-template-columns:26px 1fr;gap:11px;padding:8px 0;border-bottom:1px solid #eeeef1}
.sn{font-family:'JetBrains Mono',monospace;font-size:11pt;color:#F52E67;font-weight:500;padding-top:1px}
.sh{display:flex;align-items:baseline;gap:10px;margin-bottom:4px}
.sh h4{margin:0;font-size:11pt;font-weight:600;color:#111;letter-spacing:-.01em}
.tm{font-family:'JetBrains Mono',monospace;font-size:7.5pt;color:#9a9aa2;margin-left:auto}
.row{display:grid;grid-template-columns:46px 1fr;gap:9px;padding:2px 0}
.lab{font-family:'JetBrains Mono',monospace;font-size:6.8pt;letter-spacing:.12em;color:#9a9aa2;padding-top:2.5px}
.txt{font-size:8.9pt;color:#3a3a42}
.row.say .lab{color:#F52E67}
.row.say .txt{color:#111;font-size:9.6pt;line-height:1.45}
.row.point .lab{color:#b98}.row.point .txt{color:#6a5560;font-style:italic;font-size:8.4pt}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px 22px;margin-top:4px}
.qa div{padding:4px 0;border-bottom:1px solid #f0f0f3}
.qa b{display:block;font-size:8.6pt;color:#111;font-weight:600}
.qa span{font-size:8.2pt;color:#4a4a52}
footer{margin-top:12px;padding-top:8px;border-top:1px solid #e6e6ea;display:flex;justify-content:space-between;
  font-family:'JetBrains Mono',monospace;font-size:7pt;letter-spacing:.1em;color:#9a9aa2}
"""

def sec(label,total): return '<div class="sec">{l}<span class="t">≈ {t}</span></div>'.format(l=esc(label),t=total)

def grand_total():
    tot=0
    for grp in (RETAIL,FABRIC):
        for _,_,t,_ in grp:
            m,s=t.split(":"); tot+=int(m)*60+int(s)
    return "{}:{:02d}".format(tot//60,tot%60)

body=('<p class="intro">Three cues per step — <b>SHOW</b> what’s on the screen, <b>SAY</b> it in your own words, '
  '<b>POINT</b> to what matters. Learn the ideas, not the exact wording. Speak slowly, and give each screen a '
  'moment to land before you move on. Both walkthroughs together are about {t} minutes.</p>'
 '<div class="box"><h5>Before you start</h5><ul>'
  +"".join('<li>{}</li>'.format(esc(x)) for x in CHECKLIST)+'</ul></div>'
 +sec("Part A · RetailTrack — the store floor",steps_total(RETAIL))
  +"".join(step(*s) for s in RETAIL)
 +sec("Part B · Fabric Lens — the restaurant line",steps_total(FABRIC))
  +"".join(step(*s) for s in FABRIC)
 +'<div class="sec">How to close</div>'
  '<div class="box"><ul>'
  +"".join('<li>{}</li>'.format(esc(x)) for x in CLOSE)+'</ul></div>'
 +'<div class="sec">If someone asks — simple answers</div>'
  '<div class="two qa">'
  +"".join('<div><b>{q}</b><span>{a}</span></div>'.format(q=esc(q),a=esc(a)) for q,a in QA)+'</div>'
 ).format(t=grand_total().split(":")[0])

doc=('<!doctype html><html><head><meta charset="utf-8"/><title>EdgeVision · Demo Script</title>'
 '<link rel="stylesheet" href="fonts.css"/><style>{css}</style></head><body>'
 '<header><div class="h-l"><b>EdgeVision — Demo Script</b>'
 '<span>RetailTrack + Fabric Lens · Live Software Walkthrough · Intel Event</span></div>'
 '<div class="h-r"><b>~{t} min · both demos</b><br/>Show it · tell the story<br/>Pattern AI Labs</div></header>'
 +body+
 '<footer><span>EDGEVISION.PRO · PATTERN AI LABS · INTEL EDGE AI PARTNER</span>'
 '<span>SHOW · SAY · POINT</span></footer></body></html>').format(css=CSS,t=grand_total().split(":")[0])
os.makedirs(os.path.dirname(OUT),exist_ok=True)
open(OUT,"w",encoding="utf-8").write(doc)
print("Wrote",OUT,"| RetailTrack",steps_total(RETAIL),"| Fabric Lens",steps_total(FABRIC),"| both",grand_total())
