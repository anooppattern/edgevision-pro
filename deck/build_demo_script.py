# -*- coding: utf-8 -*-
"""EdgeVision live software demo script (RetailTrack + Fabric Lens) — printable runbook."""
import html, os
OUT="/home/user/edgevision-pro/deck/EdgeVision-Demo-Script.html"
def esc(s): return html.escape(s, quote=False)

CHECKLIST=[
 "Edge appliance powered on and on the venue LAN; all demo cameras streaming (status green).",
 "RetailTrack + Fabric Lens consoles open in full-screen browser tabs; already logged in.",
 "One “VIP” profile pre-enrolled (a teammate/volunteer) for the recognition moment.",
 "Alert phone in hand or mirrored to the screen; ringer ON, WhatsApp/app logged in, battery full.",
 "Recorded backup clip saved locally for every step (in case a live feed drops).",
 "Screen mirroring / HDMI tested; laser pointer ready; you know which camera = which zone.",
 "Runs fully on-prem — no cloud needed. If the venue Wi-Fi is flaky, the demo still works.",
]

# (num, title, time, [(label,text)...])
RETAIL=[
 (1,"Live detection","0:45",[
   ("SHOW","Live store camera with overlays — STAFF (amber) and CUSTOMER (cyan) boxes on people."),
   ("SAY","“This is an ordinary store camera — nothing special. EdgeVision is watching it live, on a small box inside the store. Every person is detected and classified — staff or customer — in real time. And notice: no faces are ever stored.”"),
   ("DO","Point to a couple of boxes. Walk into frame yourself so a fresh detection pops up."),
   ("WATCH","A new box appears as you enter; the staff/customer count ticks up.")]),
 (2,"One screen for the manager","0:45",[
   ("SHOW","The live operations console — footfall, active staff, alert stream, hourly-footfall chart."),
   ("SAY","“Here’s what the manager actually sees — one screen. Footfall today, how many staff are on the floor, live alerts, and the busy-hours curve. This is the morning huddle, on a screen.”"),
   ("DO","Run a finger along the hourly chart; land on the peak.")]),
 (3,"Dwell heat-map","0:45",[
   ("SHOW","The dwell heat-map and top dwell zones (brand wall, centre table, entry…)."),
   ("SAY","“Where do customers actually spend time? The brand wall pulls the most dwell; the entry the least. Now you merchandise to real behaviour, not guesswork — and it’s all computed on the in-store box.”"),
   ("DO","Point to the hottest zone, then the coldest.")]),
 (4,"VIP recognition — the wow moment","1:15",[
   ("SHOW","Live feed. Your enrolled “VIP” volunteer is about to walk in."),
   ("SAY","“Watch this. We’ve enrolled a loyalty customer. The moment they walk in…”"),
   ("DO","Cue the volunteer to enter. Within ~3 seconds the alert fires — hold up the phone."),
   ("SHOW","Phone alert: name, tier, last visit, suggested next action."),
   ("SAY","“…the manager’s phone lights up — name, tier, last basket, and a recommended action. Matched entirely on the in-store box; no raw face ever leaves the building.”"),
   ("WATCH","The alert on the phone. If it lags, switch to the recorded clip and keep talking.")]),
 (5,"Staff & live alerts","0:45",[
   ("SHOW","Alert stream: “wall unattended 2m”, “queue > 4 at till 2”, “back store > 4 staff”."),
   ("SAY","“The same cameras watch the team. A zone left unattended, a queue building, too many staff clustered in the back — the manager gets nudged, with a clip, while it still matters.”"),
   ("DO","Trigger one live if you can (have 5 people form a queue), or walk the alert stream.")]),
 (6,"Recap","0:20",[
   ("SAY","“Same cameras. Two answers — the customer, and the team. On-prem, private, on one small Intel box.”")]),
]

FABRIC=[
 (1,"Live station: detection + classification","0:50",[
   ("SHOW","A counter / assembly camera. Boxes on items, with quality labels (present · right · low)."),
   ("SAY","“Same idea, in a restaurant. Fabric Lens watches the make-line. It doesn’t just see a burger — it reads the build: which items are there, and whether they’re right.”"),
   ("DO","Point to one classified item and its confidence.")]),
 (2,"The intervention loop — the point","1:15",[
   ("SHOW","An order being assembled that is missing an item (e.g., a sauce the ticket calls for)."),
   ("SAY","“Here’s what makes it different — it doesn’t just detect, it intervenes. This order should have a sauce. It doesn’t.”"),
   ("DO","Show the alert fire to the assembly screen (audio chime at the pass)."),
   ("SHOW","Operator adds the sauce → it re-verifies → order released → event logged."),
   ("SAY","“The operator is flagged before the bag ever leaves the counter. Fixed, re-verified, and logged for the audit trail — the whole loop in seconds.”"),
   ("WATCH","Alert → correction → the ‘verified / released’ state.")]),
 (3,"Signal fusion — the moat","0:50",[
   ("SHOW","The fusion view: vision + equipment telemetry (fryer temp) + the order (KDS)."),
   ("SAY","“This is what no camera-only system has. The fryer reports ‘done at temperature.’ Vision reports the product is under-colored. Neither signal alone catches it — together, EdgeVision knows the equipment is drifting, not the cook.”"),
   ("DO","Point to the two conflicting signals meeting in the fusion core.")]),
 (4,"The numbers that run the business","0:50",[
   ("SHOW","The dashboard — speed, order accuracy, food safety (rolling up to the P&L categories)."),
   ("SAY","“And it rolls up to what an operator actually runs on — speed, order accuracy, food safety — per shift, per station, ready for the next audit.”"),
   ("DO","Point to the speed, accuracy and safety tiles.")]),
 (5,"Recap + hand back","0:20",[
   ("SAY","“Detection that counts is table stakes. EdgeVision understands — and acts. That’s Fabric Lens.”")]),
]

FALLBACK=[
 "A live feed drops → switch to that step’s recorded clip and narrate the same lines. Don’t debug live.",
 "Console is slow → use the saved screenshot walkthrough; the story is the same.",
 "One sentence covers any hiccup: “We run fully on-prem, so this is just our venue network.” Then move on.",
 "Keep the phone awake and the alert sound on for the VIP and intervention moments.",
]
QA=[
 ("Privacy / faces","Nothing leaves the store — no biometrics, no video sent anywhere. Matching is on the box; retention is FIFO and you configure it."),
 ("False alerts","Scene-aware GenAI with thresholds you tune per site. Every alert comes with a clip, so a human confirms."),
 ("Our cameras / IT","Uses your existing IP cameras over RTSP. One small Intel appliance on the LAN. No cloud dependency — it works offline."),
 ("Integration","REST APIs, webhooks and WhatsApp. Connects to POS / KDS and your BI stack."),
 ("Time to value","A focused 3-week pilot in one location — live results on your own floor by week 3."),
]

def step(n,title,time,rows):
    r=""
    for lab,txt in rows:
        cls="say" if lab=="SAY" else ("watch" if lab=="WATCH" else "rd")
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
.intro{font-size:8.6pt;color:#44444c;margin:0 0 12px;line-height:1.5}
.intro b{color:#111;font-weight:600}
.sec{font-family:'JetBrains Mono',monospace;font-size:8.5pt;letter-spacing:.2em;text-transform:uppercase;
  color:#F52E67;margin:16px 0 9px;display:flex;align-items:center;gap:11px}
.sec::before{content:"";width:26px;height:2px;background:#F52E67}
.sec .t{color:#9a9aa2;letter-spacing:.12em;margin-left:auto;font-size:7.5pt}
.box{border:1px solid #e6e6ea;border-left:3px solid #F52E67;background:#faf9fb;padding:11px 14px;margin:0 0 12px}
.box h5{margin:0 0 6px;font-size:8.5pt;font-family:'JetBrains Mono',monospace;letter-spacing:.16em;
  text-transform:uppercase;color:#111}
.box ul{margin:0;padding:0;list-style:none}
.box li{position:relative;padding:2.5px 0 2.5px 16px;font-size:8.5pt;color:#33333a}
.box li::before{content:"";position:absolute;left:2px;top:8px;width:5px;height:5px;border-radius:50%;background:#F52E67}
.step{display:grid;grid-template-columns:26px 1fr;gap:11px;padding:8px 0;border-bottom:1px solid #eeeef1}
.sn{font-family:'JetBrains Mono',monospace;font-size:11pt;color:#F52E67;font-weight:500;padding-top:1px}
.sh{display:flex;align-items:baseline;gap:10px;margin-bottom:4px}
.sh h4{margin:0;font-size:11pt;font-weight:600;color:#111;letter-spacing:-.01em}
.tm{font-family:'JetBrains Mono',monospace;font-size:7.5pt;color:#9a9aa2;margin-left:auto}
.row{display:grid;grid-template-columns:46px 1fr;gap:9px;padding:2px 0}
.lab{font-family:'JetBrains Mono',monospace;font-size:6.8pt;letter-spacing:.12em;color:#9a9aa2;padding-top:2.5px}
.txt{font-size:8.7pt;color:#3a3a42}
.row.say .lab{color:#F52E67}
.row.say .txt{color:#111;font-size:9.4pt;line-height:1.42}
.row.watch .lab{color:#c99}.row.watch .txt{color:#7a5560;font-style:italic;font-size:8.3pt}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:4px}
.qa div{padding:4px 0;border-bottom:1px solid #f0f0f3}
.qa b{display:block;font-size:8.3pt;color:#111;font-weight:600}
.qa span{font-size:8pt;color:#4a4a52}
footer{margin-top:12px;padding-top:8px;border-top:1px solid #e6e6ea;display:flex;justify-content:space-between;
  font-family:'JetBrains Mono',monospace;font-size:7pt;letter-spacing:.1em;color:#9a9aa2}
h5.legend{font-family:'JetBrains Mono',monospace;font-size:7pt;letter-spacing:.14em;color:#9a9aa2;margin:0 0 10px;font-weight:400}
"""

def sec(label,total): return '<div class="sec">{l}<span class="t">≈ {t} live</span></div>'.format(l=esc(label),t=total)

body=('<p class="intro">Read this as a runbook, not a script. <b>SHOW</b> = what’s on screen · '
  '<b>SAY</b> = your line (paraphrase, don’t recite) · <b>DO</b> = the action to take · '
  '<b>WATCH</b> = the thing the room should see happen. Go live-first; a recorded clip is the fallback for '
  'every step. Total demo ≈ 9–10 minutes.</p>'
 '<div class="box"><h5>Before you start — pre-flight checklist</h5><ul>'
  +"".join('<li>{}</li>'.format(esc(x)) for x in CHECKLIST)+'</ul></div>'
 +sec("Part A · RetailTrack — the store floor",steps_total(RETAIL))
  +"".join(step(*s) for s in RETAIL)
 +sec("Part B · Fabric Lens — the QSR line",steps_total(FABRIC))
  +"".join(step(*s) for s in FABRIC)
 +'<div class="sec">If it breaks · recovery</div>'
  '<div class="box" style="border-left-color:#c0392b"><ul>'
  +"".join('<li>{}</li>'.format(esc(x)) for x in FALLBACK)+'</ul></div>'
 +'<div class="sec">Likely questions — quick answers</div>'
  '<div class="two qa">'
  +"".join('<div><b>{q}</b><span>{a}</span></div>'.format(q=esc(q),a=esc(a)) for q,a in QA)+'</div>')

doc=('<!doctype html><html><head><meta charset="utf-8"/><title>EdgeVision · Live Demo Script</title>'
 '<link rel="stylesheet" href="fonts.css"/><style>{css}</style></head><body>'
 '<header><div class="h-l"><b>EdgeVision — Live Demo Script</b>'
 '<span>RetailTrack + Fabric Lens · Intel Event</span></div>'
 '<div class="h-r"><b>~9–10 min demo</b><br/>Live-first · clips as fallback<br/>Pattern AI Labs</div></header>'
 +body+
 '<footer><span>EDGEVISION.PRO · PATTERN AI LABS · INTEL EDGE AI PARTNER</span>'
 '<span>SHOW · SAY · DO · WATCH</span></footer></body></html>').format(css=CSS)
os.makedirs(os.path.dirname(OUT),exist_ok=True)
open(OUT,"w",encoding="utf-8").write(doc)
print("Wrote",OUT,"| RetailTrack",steps_total(RETAIL),"| Fabric Lens",steps_total(FABRIC))
