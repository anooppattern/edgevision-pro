# -*- coding: utf-8 -*-
"""Presenter cue sheet for the Intel event deck — one printable page, timed to 30 min."""
import html, os
OUT="/home/user/edgevision-pro/deck/EdgeVision-Event-CueSheet.html"
def esc(s): return html.escape(s, quote=False)

# (title, seconds, key message, delivery cue)
ROWS=[
 ("Cover",30,"Turn the cameras you already have into a decision engine.","Warm open. Frame: ~20 min, then discussion."),
 ("The problem — hook",45,"You record everything, and learn nothing — until it’s too late.","Show of hands: “reviewed footage only after a complaint?”"),
 ("Three blind spots",60,"Can’t watch every camera · find out too late · decide on gut feel.","Tie each to their world; these are what we remove."),
 ("The idea",30,"What if every camera could think? Meet EdgeVision.","One sentence: an AI teammate, not more screens."),
 ("How it works",75,"Connect → Watch → Understand → Act.","Reassure: no new cameras, no cloud, one small Intel box."),
 ("Four outcomes",60,"More sales · better service · less loss · safer & cleaner.","Pick the one that matters most to this room; expand it."),
 ("Retail — divider",15,"First, your stores.","Quick transition."),
 ("What it sees",60,"Same cameras, two answers: customer + team.","Speaks to GMs and ops leaders."),
 ("Retail use cases — customers",50,"Footfall, conversion, VIP, queues.","One line each; pause on the 2–3 that fit the room."),
 ("Retail use cases — operations",50,"Staffing, shrink, safety, compliance.","Ask which of these costs them most today."),
 ("One screen",75,"One screen your managers actually use.","Make it feel like their morning huddle."),
 ("The VIP moment",60,"A VIP walks in; your team knows in seconds.","Tell it as a story. Stress: no faces stored."),
 ("QSR — divider",15,"Now your restaurants.","Quick transition."),
 ("The three numbers",60,"Speed, accuracy, safety — live.","Tie to P&L and health / FSSAI audits."),
 ("QSR use cases — speed & accuracy",50,"Drive-thru, queues, accuracy, remakes.","Tie straight to revenue and the drive-thru."),
 ("QSR use cases — safety & ops",50,"PPE, handwash, hold-times, labour.","The audit & compliance story; great for multi-unit."),
 ("Drive-thru",60,"Every lane, every car, every second.","Biggest revenue line, hardest to measure — on existing cameras."),
 ("The engine — GenAI + VLMs",90,"A Vision-Language Model reads the scene like a person.","THE why. Keep it plain — one or two sentences, no deep tech."),
 ("Why it’s different",60,"Old cameras count. GenAI understands.","Read one before/after example aloud — it lands."),
 ("Where it shows up in your P&L",75,"Sales · shrink · throughput · loyalty.","Do the quick math with them; invite their own numbers."),
 ("Private by design + Intel",60,"Nothing leaves the store; runs on Intel.","Handle privacy + IT head-on. Lean into the Intel partnership."),
 ("Proof",45,"Intel partner · production CV at scale · retail+QSR focus.","Credibility; names they’ll recognise."),
 ("Close — the ask",60,"One location, 3-week pilot, zero risk.","“Which location should we start with?”"),
]
def mmss(s): return "{}:{:02d}".format(s//60, s%60)
rows_html=""; clock=0
for i,(t,dur,msg,cue) in enumerate(ROWS,1):
    rows_html+=('<tr><td class="n">{n:02d}</td><td class="clk">{clk}</td><td class="dur">{dur}</td>'
        '<td class="msg"><b>{t}</b><span>{msg}</span></td><td class="cue">{cue}</td></tr>').format(
        n=i,clk=mmss(clock),dur="+"+mmss(dur),t=esc(t),msg=esc(msg),cue=esc(cue))
    clock+=dur
present=mmss(clock)
CSS="""
@page{size:210mm 297mm;margin:9mm 12mm 8mm}
*{box-sizing:border-box}
body{margin:0;font-family:'Inter',system-ui,sans-serif;color:#15151a;font-weight:300;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
.mono{font-family:'JetBrains Mono',monospace}
header{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid #F52E67;padding-bottom:8px;margin-bottom:6px}
.h-l b{font-weight:700;letter-spacing:.02em;font-size:15pt;color:#111}
.h-l span{display:block;font-family:'JetBrains Mono',monospace;font-size:7.5pt;letter-spacing:.18em;
  text-transform:uppercase;color:#F52E67;margin-top:3px}
.h-r{text-align:right;font-family:'JetBrains Mono',monospace;font-size:7.5pt;letter-spacing:.12em;color:#6a6a72;line-height:1.5}
.h-r b{color:#111;font-size:9pt}
table{width:100%;border-collapse:collapse;margin-top:4px}
th{font-family:'JetBrains Mono',monospace;font-size:6.5pt;letter-spacing:.16em;text-transform:uppercase;
  color:#8a8a92;text-align:left;padding:0 6px 5px;border-bottom:1px solid #e2e2e6}
td{padding:3px 6px;border-bottom:1px solid #eeeef1;vertical-align:top}
td.n{font-family:'JetBrains Mono',monospace;font-size:8pt;color:#F52E67;width:22px}
td.clk{font-family:'JetBrains Mono',monospace;font-size:9pt;color:#111;width:42px;font-weight:500}
td.dur{font-family:'JetBrains Mono',monospace;font-size:7.5pt;color:#9a9aa2;width:40px}
td.msg{width:44%}
td.msg b{font-size:9pt;font-weight:600;color:#111;display:block;letter-spacing:-.01em}
td.msg span{font-size:7.6pt;color:#44444c;display:block;margin-top:1px;line-height:1.28}
td.cue{font-size:7.6pt;color:#55555d;line-height:1.28}
tr:nth-child(even) td{background:#faf9fb}
footer{display:flex;justify-content:space-between;margin-top:8px;font-family:'JetBrains Mono',monospace;
  font-size:7pt;letter-spacing:.1em;color:#9a9aa2}
.tot{color:#F52E67;font-weight:600}
"""
doc=('<!doctype html><html><head><meta charset="utf-8"/><title>EdgeVision · Presenter Cue Sheet</title>'
 '<link rel="stylesheet" href="fonts.css"/><style>{css}</style></head><body>'
 '<header><div class="h-l"><b>EdgeVision — Retail &amp; QSR</b>'
 '<span>Presenter Cue Sheet · Intel Event</span></div>'
 '<div class="h-r"><b>30-minute session</b><br/>~{present} present · rest for Q&amp;A<br/>Pattern AI Labs</div></header>'
 '<table><thead><tr><th>#</th><th>At</th><th>Len</th><th>Slide · key message</th><th>Delivery cue</th></tr></thead>'
 '<tbody>{rows}</tbody></table>'
 '<footer><span>Clock = when to be ON that slide · aim to finish presenting by <span class="tot">{present}</span></span>'
 '<span>EDGEVISION.PRO · PATTERN AI LABS</span></footer>'
 '</body></html>').format(css=CSS,rows=rows_html,present=present)
os.makedirs(os.path.dirname(OUT),exist_ok=True)
open(OUT,"w",encoding="utf-8").write(doc)
print("Wrote",OUT,"| present time",present)
