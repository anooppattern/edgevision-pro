# -*- coding: utf-8 -*-
"""EdgeVision Intel-event 30-minute dry-run runsheet — stitches the 22-slide
event deck and the pre-recorded demo into one running clock, with the two
'switch to demo' cues and a Q&A buffer. Printable A4, same design system."""
import html, os
OUT="/home/user/edgevision-pro/deck/EdgeVision-Event-Runsheet.html"
def esc(s): return html.escape(s, quote=False)

# kind: seg (deck/talk) | demo (switch to video) | qa
# (clock, dur, kind, block, what, cue)
ROWS=[
 ("0:00","0:30","seg","Open","Slide 1 · Cover",
   "Welcome the room, one line on Pattern AI Labs. Set the frame: “~20 minutes, then your questions.”"),
 ("0:30","2:00","seg","The problem","Slides 2–3 · The problem · Three blind spots",
   "Cameras record everything and tell you nothing. Name the three blind spots that cost money every day."),
 ("2:30","1:00","seg","The idea","Slide 4 · The idea",
   "“What if every camera could think?” That’s EdgeVision — the turn of the whole pitch."),
 ("3:30","1:00","seg","How","Slide 5 · How it works",
   "Uses the cameras you already have, one small box on-site, switched on in days. Keep it light."),
 ("4:30","1:00","seg","What you get","Slide 6 · Four outcomes",
   "The four things a manager will feel. Don’t over-explain — you’re about to show them."),
 ("5:30","0:30","seg","Retail","Slide 7 · Retail — for your stores",
   "“Let’s see it running in a store.” This is your hand-off line into the demo."),
 ("6:00","5:00","demo","▶ DEMO A","Switch to video · RetailTrack (Part A of the demo script)",
   "Play the 6 RetailTrack clips and narrate: people seen · manager screen · heat-map · best-customer · early alerts · recap. Runs ~4:20; leave slack for transitions."),
 ("11:00","1:00","seg","QSR","Slides 13–14 · QSR — for your restaurants · The three numbers",
   "“Now the same thing in a restaurant.” Frame the three numbers every shift lives by, then hand to the demo."),
 ("12:00","4:30","demo","▶ DEMO B","Switch to video · Fabric Lens (Part B of the demo script)",
   "Play the 5 Fabric Lens clips: reads the line · catches & fixes the mistake · two signals · the numbers · recap. Runs ~3:55; leave slack for transitions."),
 ("16:30","1:00","seg","The engine","Slide 17 · Why it can do this: GenAI + VLMs",
   "The one ‘how is this possible’ slide. It understands scenes, it doesn’t just count."),
 ("17:30","1:00","seg","Why different","Slide 18 · Old cameras count, GenAI understands",
   "Sharp contrast slide. Land the difference in one breath."),
 ("18:30","1:30","seg","The money","Slide 19 · Where it shows up in your P&L",
   "Tie it to their numbers — sales, labour, waste, safety. This is what the decision-maker remembers."),
 ("20:00","1:00","seg","Trust","Slide 20 · Private by design + Intel",
   "Nothing leaves the store; runs on Intel edge. Pre-empt the privacy question before it’s asked."),
 ("21:00","0:45","seg","Proof","Slide 21 · Built by a team that’s shipped this",
   "Quick credibility. Don’t linger."),
 ("21:45","1:15","seg","Close","Slide 22 · The ask",
   "“See it live in your own store in three weeks.” Make the ask, then stop talking."),
 ("23:00","6:00","qa","Q&A","Open the floor",
   "Use the ‘simple answers’ sheet. Repeat each question so the room hears it. Park deep-dives for a 1:1."),
 ("29:00","1:00","qa","Wrap","Restate the ask · hand the leave-behind",
   "One-line recap, hand out the 2-page handout, collect cards / book pilots. Buffer to 30:00."),
]

SKIP=[
 "Retail use-case slides (8–12) and QSR use-case slides (15–16) are intentionally NOT clicked through — the live demo covers exactly that ground. Showing both would run you well past 30 minutes and repeat yourself.",
 "The VIP-moment slide (12) is your backup: if the best-customer clip stalls, jump to that slide and tell the story from it.",
]
NODEMO=[
 "Cut both demo blocks (saves ~9:30) and instead click through the retail slides 8–12 (~3:30) and QSR slides 14–16 (~2:30).",
 "That leaves ~3–4 extra minutes — spend it on the P&L slide and a longer Q&A. You still land inside 30 minutes.",
]

def clk(t): return '<span class="clk">{}</span>'.format(esc(t))

def row(c,d,kind,block,what,cue):
    cls={"demo":"r-demo","qa":"r-qa"}.get(kind,"")
    return ('<tr class="{cls}"><td class="c-clk">{c}<span class="dur">{d}</span></td>'
      '<td class="c-blk">{b}</td><td class="c-what"><b>{w}</b><span>{cue}</span></td></tr>').format(
      cls=cls,c=esc(c),d=esc(d),b=esc(block),w=esc(what),cue=esc(cue))

CSS="""
@page{size:210mm 297mm;margin:11mm 12mm 10mm}
*{box-sizing:border-box}
body{margin:0;font-family:'Inter',system-ui,sans-serif;color:#17171c;font-weight:300;line-height:1.4;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
header{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid #F52E67;
  padding-bottom:9px;margin-bottom:11px}
.h-l b{font-weight:700;font-size:16pt;color:#111}
.h-l span{display:block;font-family:'JetBrains Mono',monospace;font-size:7.5pt;letter-spacing:.18em;
  text-transform:uppercase;color:#F52E67;margin-top:3px}
.h-r{text-align:right;font-family:'JetBrains Mono',monospace;font-size:7.5pt;letter-spacing:.1em;color:#6a6a72;line-height:1.6}
.h-r b{color:#111;font-size:9.5pt}
.intro{font-size:8.6pt;color:#44444c;margin:0 0 10px;line-height:1.5}
.intro b{color:#111;font-weight:600}
table{width:100%;border-collapse:collapse;margin-bottom:6px}
td{vertical-align:top;padding:6.5px 8px;border-bottom:1px solid #eeeef1}
.c-clk{width:62px;font-family:'JetBrains Mono',monospace;font-size:10pt;color:#111;font-weight:500;white-space:nowrap}
.c-clk .dur{display:block;font-size:6.6pt;color:#a2a2aa;font-weight:400;margin-top:2px;letter-spacing:.05em}
.c-blk{width:150px;font-family:'JetBrains Mono',monospace;font-size:7.4pt;letter-spacing:.1em;
  text-transform:uppercase;color:#F52E67;padding-top:8px}
.c-what b{display:block;font-size:9.4pt;color:#111;font-weight:600;margin-bottom:2px}
.c-what span{font-size:8.5pt;color:#4a4a52;line-height:1.4}
tr.r-demo td{background:#fff4f7;border-top:2px solid #F52E67;border-bottom:2px solid #F52E67}
tr.r-demo .c-blk{color:#F52E67;font-weight:700}
tr.r-demo .c-what b{color:#c21c4b}
tr.r-qa td{background:#faf9fb}
.sec{font-family:'JetBrains Mono',monospace;font-size:8pt;letter-spacing:.2em;text-transform:uppercase;
  color:#F52E67;margin:13px 0 8px;display:flex;align-items:center;gap:11px}
.sec::before{content:"";width:24px;height:2px;background:#F52E67}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.box{border:1px solid #e6e6ea;border-left:3px solid #F52E67;background:#faf9fb;padding:10px 13px}
.box h5{margin:0 0 6px;font-size:8pt;font-family:'JetBrains Mono',monospace;letter-spacing:.14em;
  text-transform:uppercase;color:#111}
.box ul{margin:0;padding:0;list-style:none}
.box li{position:relative;padding:2.5px 0 2.5px 15px;font-size:8.4pt;color:#33333a;line-height:1.4}
.box li::before{content:"";position:absolute;left:2px;top:8px;width:5px;height:5px;border-radius:50%;background:#F52E67}
.box.alt{border-left-color:#8a8a92}.box.alt li::before{background:#8a8a92}.box.alt h5{color:#5a5a62}
footer{margin-top:11px;padding-top:8px;border-top:1px solid #e6e6ea;display:flex;justify-content:space-between;
  font-family:'JetBrains Mono',monospace;font-size:7pt;letter-spacing:.1em;color:#9a9aa2}
"""

body=('<p class="intro">One running clock for the full 30-minute slot — deck and demo stitched together. '
  'The <b>pink rows are the two demo hand-offs</b>: stop presenting slides and play the recorded clips from the '
  'demo script. Times are cumulative from the start; if you slip, trim Q&amp;A, not the demo. '
  'Total lands at <b>30:00</b>.</p>'
 '<table>'+"".join(row(*r) for r in ROWS)+'</table>'
 +'<div class="two">'
   '<div class="box"><h5>What you deliberately skip</h5><ul>'
    +"".join('<li>{}</li>'.format(esc(x)) for x in SKIP)+'</ul></div>'
   '<div class="box alt"><h5>If you can’t run the demo</h5><ul>'
    +"".join('<li>{}</li>'.format(esc(x)) for x in NODEMO)+'</ul></div>'
  '</div>')

doc=('<!doctype html><html><head><meta charset="utf-8"/><title>EdgeVision · Event Runsheet</title>'
 '<link rel="stylesheet" href="fonts.css"/><style>{css}</style></head><body>'
 '<header><div class="h-l"><b>EdgeVision — 30-Minute Runsheet</b>'
 '<span>Intel Event · Deck + Live Demo · Dry-Run</span></div>'
 '<div class="h-r"><b>30:00 total</b><br/>~20 min present · ~9 min demo · Q&amp;A<br/>Pattern AI Labs</div></header>'
 +body+
 '<footer><span>EDGEVISION.PRO · PATTERN AI LABS · INTEL EDGE AI PARTNER</span>'
 '<span>DECK ↔ DEMO · ONE CLOCK</span></footer></body></html>').format(css=CSS)
os.makedirs(os.path.dirname(OUT),exist_ok=True)
open(OUT,"w",encoding="utf-8").write(doc)
# sanity check: cumulative time
def toS(t): m,s=t.split(":"); return int(m)*60+int(s)
end=toS(ROWS[-1][0])+toS(ROWS[-1][1])
print("Wrote",OUT,"| ends at {}:{:02d}".format(end//60,end%60))
