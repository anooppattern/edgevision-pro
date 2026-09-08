# -*- coding: utf-8 -*-
"""Leave-behind handout for the Intel event — premium 2-page A4 (on-brand dark)."""
import html, os
OUT="/home/user/edgevision-pro/deck/EdgeVision-Retail-QSR-Handout.html"
IMG="../assets/images"
def esc(s): return html.escape(s, quote=False)

rects="\n".join('<rect x="22.7" y="2.4" width="2.6" height="13.6" rx="1.3"{}/>'.format(
    "" if a==0 else ' transform="rotate({} 24 24)"'.format(a)) for a in range(0,360,15))
MARK=('<svg class="mk" viewBox="0 0 48 48" aria-hidden="true"><g fill="currentColor">'+rects+'</g></svg>')
ICON={
 "trend":'<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
 "users":'<circle cx="9" cy="8" r="3.5"/><path d="M2 20c0-3.6 3.1-6.5 7-6.5s7 2.9 7 6.5"/><circle cx="17" cy="6" r="2.5"/><path d="M22 18c0-2.5-2-4.5-5-4.5"/>',
 "shield":'<path d="M12 2l8 4v6c0 5-3.5 9.5-8 10-4.5-.5-8-5-8-10V6z"/>',
 "leaf":'<path d="M4 20c8 2 16-4 16-16-8 0-14 6-14 12 2-4 5-6 9-7"/>',
 "eye":'<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "check":'<polyline points="4 12 10 18 20 6"/>',
 "chip":'<rect x="5" y="5" width="14" height="14" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/>',
 "lock":'<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
}
def ic(n): return '<svg class="ic" viewBox="0 0 24 24">{}</svg>'.format(ICON[n])

def tiles(items):
    return '<div class="tiles">'+"".join(
      '<div class="tile">{i}<h4>{h}</h4><p>{p}</p></div>'.format(i=ic(k),h=esc(h),p=esc(p)) for k,h,p in items)+'</div>'
def buckets(items):
    return '<div class="buckets">'+"".join(
      '<div class="bk"><p class="bk-h">{h}</p><ul>{l}</ul></div>'.format(
        h=esc(h),l="".join('<li>{}</li>'.format(esc(x)) for x in bl)) for h,bl in items)+'</div>'

OUTCOMES=[("trend","More sales","Convert more of the footfall you already pay for."),
 ("users","Better service","The right staff, in the right place, at the right moment."),
 ("shield","Less loss","Catch shrink and mistakes as they happen — not weeks later."),
 ("leaf","Safer & cleaner","Hygiene and safety, checked continuously — audit-ready.")]
RETAIL=[("Customers & Conversion",["Footfall, dwell & hot-spots","Which displays pull people in","Browse-to-buy & queue drop-off","VIP & loyalty at the door"]),
 ("Staff & Service",["Zone coverage at peak","Greeting & attentiveness","Who actually converts","Fitting-room & counter service"]),
 ("Loss & Safety",["Tag-removal & concealment cues","After-hours / restricted motion","Slips, spills & blocked exits","Cash-desk ↔ door correlation"]),
 ("Store & Compliance",["Display & shelf hygiene","Planogram / VM adherence","Opening & closing checks","Camera health & blind spots"])]
QSR=[("Speed & Throughput",["Drive-thru wait per lane","Counter & kiosk queues","Time-to-first-bag","Kitchen bottlenecks, live"]),
 ("Order Accuracy",["Item & modifier checks","Missing-item catch before bagging","Packaging accuracy","Remake & refire rate"]),
 ("Food Safety & Hygiene",["Gloves, hairnets & aprons","Handwash cadence vs SOP","Hot / cold hold-time & temp","Spills & cleaning cadence"]),
 ("Guest & Ops",["Dining-area & restroom checks","Greeter & upsell prompts","Labour vs demand by daypart","Closing-audit photo trail"])]
STEPS=[("Week 1","Audit & install","Site survey and camera audit. The edge appliance goes in on your LAN; baseline data starts."),
 ("Week 2","Calibrate & tune","Zones and thresholds tuned to your store; alerts routed to the tools your team already uses."),
 ("Week 3","Handover & results","Manager training and your first live results — on your own floor, on the cameras you already own.")]

CSS="""
@page{size:210mm 297mm;margin:0}
*{box-sizing:border-box}
body{margin:0;background:#000;font-family:'Inter',system-ui,sans-serif;color:#fff;font-weight:300;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;padding:16mm 15mm 13mm;
  page-break-after:always;background:#000;background-image:linear-gradient(0deg,rgba(90,23,41,.28),transparent 40mm)}
.page:last-child{page-break-after:auto}
.mk{width:30px;height:30px;color:#F52E67}
.ic{width:26px;height:26px;stroke:#F52E67;fill:none;stroke-width:1.5}
.top{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(255,255,255,.12);padding-bottom:12px}
.brand{display:flex;align-items:center;gap:11px}
.brand b{font-weight:700;letter-spacing:.14em;font-size:10pt}
.brand i{font-style:normal;font-weight:300;color:#8B8B96;letter-spacing:.14em;font-size:9pt}
.brand .div{color:#3A3A42;padding:0 3px}.brand .pr{color:#F52E67;font-weight:600;letter-spacing:.18em;font-size:9pt}
.tagline{font-family:'JetBrains Mono',monospace;font-size:7pt;letter-spacing:.16em;color:#8B8B96;text-transform:uppercase}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:7.5pt;letter-spacing:.22em;color:#F52E67;text-transform:uppercase;margin:20px 0 8px}
h1{font-weight:200;font-size:27pt;line-height:1.06;letter-spacing:-.02em;margin:0 0 12px;max-width:16em}
h1 .g{color:#F52E67}
.lead{font-size:10.5pt;line-height:1.55;color:#c9c9d0;max-width:44em;margin:0 0 6px;font-weight:300}
.hero{margin:14px 0 6px;border:1px solid rgba(255,255,255,.1);height:52mm;overflow:hidden}
.hero img{width:100%;height:100%;object-fit:cover;filter:brightness(.66) saturate(.92)}
.sec{font-family:'JetBrains Mono',monospace;font-size:7.5pt;letter-spacing:.22em;color:#F52E67;text-transform:uppercase;
  margin:18px 0 10px;display:flex;align-items:center;gap:10px}
.sec::before{content:"";width:26px;height:1px;background:#F52E67}
.tiles{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.1)}
.tile{background:#000;padding:15px 14px 17px}
.tile h4{font-weight:400;font-size:11pt;margin:11px 0 5px;color:#fff}
.tile p{font-size:8.2pt;line-height:1.4;color:#8B8B96;margin:0}
.why{display:grid;grid-template-columns:1.1fr 1fr;gap:22px;margin-top:6px;align-items:center}
.why p{font-size:10pt;line-height:1.55;color:#c9c9d0;margin:0}
.why b{color:#fff;font-weight:500}
.why .pts{list-style:none;padding:0;margin:0;display:grid;gap:9px}
.why .pts li{position:relative;padding-left:22px;font-size:9pt;color:#c9c9d0}
.why .pts li::before{content:"\\2192";position:absolute;left:0;color:#F52E67}
.buckets{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.1)}
.bk{background:#000;padding:14px 13px 15px}
.bk-h{font-family:'Inter';font-weight:600;font-size:9.5pt;color:#F52E67;margin:0 0 9px}
.bk ul{list-style:none;padding:0;margin:0}
.bk li{position:relative;padding:4px 0 4px 13px;font-size:8pt;line-height:1.3;color:#b7b7be}
.bk li::before{content:"\\2022";position:absolute;left:2px;top:4px;color:#F52E67}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.1)}
.step{background:#000;padding:15px 15px 17px;border-top:2px solid transparent}
.step:first-child{border-top-color:#F52E67}
.step .wk{font-family:'JetBrains Mono',monospace;font-size:7pt;letter-spacing:.2em;color:#F52E67;text-transform:uppercase}
.step h4{font-weight:400;font-size:11.5pt;color:#fff;margin:7px 0 6px}
.step p{font-size:8.4pt;line-height:1.45;color:#8B8B96;margin:0}
.cta{margin-top:20px;border:1px solid rgba(245,46,103,.4);background:rgba(245,46,103,.05);padding:18px 20px;
  display:flex;justify-content:space-between;align-items:center}
.cta .l b{font-weight:400;font-size:15pt;color:#fff}
.cta .l span{display:block;font-size:9pt;color:#c9c9d0;margin-top:4px}
.cta .r{text-align:right;font-family:'JetBrains Mono',monospace;font-size:8.5pt;color:#c9c9d0;line-height:1.7}
.cta .r b{color:#fff}
.foot{position:absolute;left:15mm;right:15mm;bottom:9mm;display:flex;justify-content:space-between;
  font-family:'JetBrains Mono',monospace;font-size:6.5pt;letter-spacing:.16em;color:#56565F;text-transform:uppercase}
.tags{display:flex;gap:22px;margin-top:14px;font-family:'JetBrains Mono',monospace;font-size:7.5pt;
  letter-spacing:.18em;color:#8B8B96;text-transform:uppercase}
.tags i{font-style:normal;display:inline-flex;align-items:center;gap:8px}
.tags .d{width:6px;height:6px;border-radius:50%;background:#F52E67;display:inline-block}
"""

def top(right):
    return ('<div class="top"><div class="brand">'+MARK+
      '<span><b>PATTERN</b> <i>AI&nbsp;LABS</i> <span class="div">/</span> <span class="pr">EDGEVISION</span></span></div>'
      '<div class="tagline">{}</div></div>').format(right)

page1=('<div class="page">'+top("Intel Edge AI Partner")+
 '<p class="eyebrow">EdgeVision · Retail &amp; QSR</p>'
 '<h1>Turn the cameras you already have into a <span class="g">decision engine</span>.</h1>'
 '<p class="lead">EdgeVision is real-time AI that watches every store and restaurant camera — and tells your team '
 'exactly what to do, the moment it matters. It runs on-site on a small Intel appliance: no new cameras, no cloud, '
 'nothing leaves the building.</p>'
 '<div class="hero"><img src="{img}/ev-cover.png" alt=""/></div>'
 '<div class="sec">What you get</div>'+tiles(OUTCOMES)+
 '<div class="sec">Why it&rsquo;s different — GenAI</div>'
 '<div class="why"><p>The breakthrough is the <b>Vision-Language Model</b> — an AI that looks at a camera frame the '
 'way a person would. It reads the whole scene and its context, not just pixels or motion. Old analytics counts; '
 '<b>EdgeVision understands</b> — and tells you what to do.</p>'
 '<ul class="pts"><li>Understands context — a real spill from a shadow, a browser from a buyer</li>'
 '<li>Judges quality — a missing item, a pale fry, an untidy display</li>'
 '<li>Adapts on its own — new store, new menu, new season, no re-training</li></ul></div>'
 '<div class="tags"><i><span class="d"></span> EDGE-FIRST</i><i><span class="d"></span> PRIVACY BY DESIGN</i>'
 '<i><span class="d"></span> INTEL POWERED</i></div>'
 '<div class="foot"><span>EDGEVISION.PRO</span><span>© 2026 PATTERN AI LABS · INTEL EDGE AI PARTNER</span></div></div>').format(img=IMG)

page2=('<div class="page">'+top("What it can watch")+
 '<div class="sec">In your stores</div>'+buckets(RETAIL)+
 '<div class="sec">In your restaurants</div>'+buckets(QSR)+
 '<div class="sec" style="display:flex;gap:26px;align-items:center"><span style="display:flex;align-items:center;gap:10px">'
 '<svg class="ic" viewBox="0 0 24 24" style="width:18px;height:18px">'+ICON["lock"]+'</svg> PRIVATE BY DESIGN</span></div>'
 '<p class="lead" style="margin-top:-2px">Everything stays in your store. No faces or video leave the building, and it '
 'keeps working even if the internet drops. Runs on one small, efficient Intel appliance per site — with role-based '
 'access and a retention policy you control.</p>'
 '<div class="sec">See it live in three weeks</div>'+
 '<div class="steps">'+"".join('<div class="step"><span class="wk">{w}</span><h4>{h}</h4><p>{p}</p></div>'.format(
    w=esc(w),h=esc(h),p=esc(p)) for w,h,p in STEPS)+'</div>'
 '<div class="cta"><div class="l"><b>Let&rsquo;s run a pilot in one of your locations.</b>'
 '<span>Same cameras. New decisions. Zero risk to the rest of your estate.</span></div>'
 '<div class="r"><b>info@pattern-ai.com</b><br/>www.edgevision.pro<br/>+91 99618 71254</div></div>'
 '<div class="foot"><span>SAN FRANCISCO · KOCHI · REMOTE, GLOBAL</span><span>PATTERN AI LABS</span></div></div>')

doc=('<!doctype html><html><head><meta charset="utf-8"/><title>EdgeVision — Retail & QSR · Handout</title>'
 '<link rel="stylesheet" href="fonts.css"/><style>{css}</style></head><body>{p1}{p2}</body></html>').format(
   css=CSS,p1=page1,p2=page2)
os.makedirs(os.path.dirname(OUT),exist_ok=True)
open(OUT,"w",encoding="utf-8").write(doc)
print("Wrote",OUT)
