# -*- coding: utf-8 -*-
"""EdgeVision demo script (RetailTrack + Fabric Lens) — printable runbook.
Plain language for a mixed technical / non-technical room; three cues per step
(SHOW / SAY / POINT) written so a presenter can learn and deliver it naturally."""
import html, os
OUT="/home/user/edgevision-pro/deck/EdgeVision-Demo-Script.html"
def esc(s): return html.escape(s, quote=False)

CHECKLIST=[
 "Laptop connected to the projector; screen mirrored and tested. Sound ON — a couple of steps have an alert chime.",
 "Each part of the demo is open and lined up in order, full-screen. Know which step comes next before you start.",
 "Close every other tab and notification. Nothing should pop up while you present.",
 "Keep this sheet where you can see it. You tell the story; the screen shows the proof.",
 "Open with one line: “What you’re about to see is our software running on everyday store and restaurant cameras.”",
]

# (num, title, time, [(label,text)...])   labels: SHOW / SAY / POINT
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

FABRIC=[
 (1,"Reading the kitchen line","0:50",[
   ("SHOW","The counter where food is made — a box on each item, with a simple label: there, correct, or not right."),
   ("SAY","“Same idea, now in a restaurant. Our software watches the counter where food is made. It doesn’t just see a burger — it checks the build: is every item there, and is it right?”"),
   ("POINT","Point to one item and its label.")]),
 (2,"It catches the mistake — and fixes it","1:10",[
   ("SHOW","An order is missing an item; an alert pops up on the kitchen screen with a chime; the item is added and the order clears."),
   ("SAY","“This is the important part. This order is missing a sauce. The screen flags it straight away, before the bag goes out. The team add it, the software checks again, and the order is cleared. A wrong order caught in seconds — not after the customer complains.”"),
   ("POINT","Follow it on screen: the alert, then the green ‘all correct’ once it’s fixed.")]),
 (3,"Two signals are better than one","0:50",[
   ("SHOW","The camera view next to the fryer reading and the order screen."),
   ("SAY","“Here’s something a camera alone can’t do. The fryer says the food is cooked. The camera says it still looks pale. Put the two together and you learn the fryer is running cool — a problem you’d never catch by eye until customers did.”"),
   ("POINT","Point to the two readings that disagree.")]),
 (4,"The numbers a manager cares about","0:45",[
   ("SHOW","The dashboard — service speed, order accuracy, and food-safety checks, by shift and station."),
   ("SAY","“It all adds up to the numbers an owner runs on — how fast service is, how accurate orders are, and food-safety checks — for every shift and every station, ready for the next audit.”"),
   ("POINT","Point to the speed, accuracy, and safety tiles.")]),
 (5,"Recap + hand back","0:20",[
   ("SAY","“Counting things is easy. The real difference is that it understands what’s happening — and speaks up in time to fix it. That’s Fabric Lens.”")]),
]

CLOSE=[
 "Bring it home: “Two products, one platform. It runs on your existing cameras, on a small box on-site. Nothing goes to the cloud.”",
 "The ask: “Give us three weeks in one of your stores and we’ll show you these same results on your own floor.”",
 "Then pause and take questions — the quick answers are below.",
]
QA=[
 ("Is this recording faces?","No faces are saved and no video leaves the site. Everything is worked out on the box inside your store."),
 ("Won’t it cry wolf?","Every alert comes with a short clip so a person can glance and confirm. You set how sensitive it is, per site."),
 ("Does it need new cameras?","No — it uses the cameras you already have. Just one small box added on-site."),
 ("Does it need the internet?","No. It keeps working even if the internet goes down, because everything runs locally."),
 ("How does it fit our systems?","It plugs into your billing / kitchen screens and can send alerts to a phone or WhatsApp."),
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

body=('<p class="intro">Three cues per step — <b>SHOW</b> what’s on the screen, <b>SAY</b> it in your own words, '
  '<b>POINT</b> to what matters. Learn the ideas, not the exact wording. Speak slowly, and give each screen a '
  'moment to land before you move on. The whole walkthrough is about 8–9 minutes.</p>'
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
  +"".join('<div><b>{q}</b><span>{a}</span></div>'.format(q=esc(q),a=esc(a)) for q,a in QA)+'</div>')

doc=('<!doctype html><html><head><meta charset="utf-8"/><title>EdgeVision · Demo Script</title>'
 '<link rel="stylesheet" href="fonts.css"/><style>{css}</style></head><body>'
 '<header><div class="h-l"><b>EdgeVision — Demo Script</b>'
 '<span>RetailTrack + Fabric Lens · Intel Event</span></div>'
 '<div class="h-r"><b>~8–9 min walkthrough</b><br/>Show it · tell the story<br/>Pattern AI Labs</div></header>'
 +body+
 '<footer><span>EDGEVISION.PRO · PATTERN AI LABS · INTEL EDGE AI PARTNER</span>'
 '<span>SHOW · SAY · POINT</span></footer></body></html>').format(css=CSS)
os.makedirs(os.path.dirname(OUT),exist_ok=True)
open(OUT,"w",encoding="utf-8").write(doc)
print("Wrote",OUT,"| RetailTrack",steps_total(RETAIL),"| Fabric Lens",steps_total(FABRIC))
