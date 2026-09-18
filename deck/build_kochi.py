# -*- coding: utf-8 -*-
"""EdgeVision — Kochi 15-minute pitch (Retail + QSR). Big, visual, dead-simple. 16:9."""
import html, os
OUT="/home/user/edgevision-pro/deck/EdgeVision-Kochi-Pitch.html"
IMG="../assets/images"
def esc(s): return html.escape(s, quote=False)

ICON={
 "camera":'<path d="M3 7h4l2-3h6l2 3h4v12H3z"/><circle cx="12" cy="13" r="3.5"/>',
 "eye":'<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "chip":'<rect x="5" y="5" width="14" height="14" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/>',
 "bell":'<path d="M18 16V11a6 6 0 1 0-12 0v5l-2 2h16zM10 20a2 2 0 0 0 4 0"/>',
 "users":'<circle cx="9" cy="8" r="3.5"/><path d="M2 20c0-3.6 3.1-6.5 7-6.5s7 2.9 7 6.5"/><circle cx="17" cy="6" r="2.5"/><path d="M22 18c0-2.5-2-4.5-5-4.5"/>',
 "shield":'<path d="M12 2l8 4v6c0 5-3.5 9.5-8 10-4.5-.5-8-5-8-10V6z"/>',
 "lock":'<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
 "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "check":'<polyline points="4 12 10 18 20 6"/>',
 "trend":'<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
 "leaf":'<path d="M4 20c8 2 16-4 16-16-8 0-14 6-14 12 2-4 5-6 9-7"/>',
 "star":'<path d="M12 3l2.5 6 6.5.5-5 4 1.6 6.3L12 16l-5.6 3.8L8 13.5 3 9.5 9.5 9z"/>',
}
def ic(n): return '<svg viewBox="0 0 24 24">{}</svg>'.format(ICON[n])

N=[0]; TOTAL=13
def bar():
    N[0]+=1
    return ('<div class="brandbar"><span><b>PATTERN AI LABS</b> · EDGEVISION</span>'
        '<span class="pg">{n:02d} / {t}</span></div>').format(n=N[0],t=TOTAL)

def fb(img,kicker,h1,sub="",cls=""):
    s='<p class="sub">{}</p>'.format(sub) if sub else ""
    k='<p class="kicker">{}</p>'.format(esc(kicker)) if kicker else ""
    return ('<section class="slide fb {cls}"><img class="bg" src="{i}/{img}" alt=""/><div class="veil"></div>'
        '{bar}<div class="content">{k}<h1 class="h1">{h1}</h1>{s}</div></section>').format(
        cls=cls,i=IMG,img=img,bar=bar(),k=k,h1=h1,s=s)

def cover(img,kicker,word,sub):
    return ('<section class="slide fb cover"><img class="bg" src="{i}/{img}" alt=""/><div class="veil veil--cover"></div>'
        '{bar}<div class="content"><p class="kicker">{k}</p>'
        '<h1 class="word"><span>Edge</span><span class="em">Vision</span></h1>'
        '<p class="sub sub--cover">{sub}</p>'
        '<p class="coverfoot">Pattern AI Labs · Intel Edge AI Partner · edgevision.pro</p></div></section>').format(
        i=IMG,img=img,bar=bar(),k=esc(kicker),sub=sub)

def tiles(kicker,head,items,cls=""):
    cells="".join('<article class="tile"><div class="ic">{i}</div><h3>{h}</h3><p>{p}</p></article>'.format(
        i=ic(icn),h=esc(h),p=esc(p)) for icn,h,p in items)
    return ('<section class="slide dark {cls}">{bar}<div class="head"><p class="kicker">{k}</p>'
        '<h2 class="h2">{head}</h2></div><div class="tiles">{cells}</div></section>').format(
        cls=cls,bar=bar(),k=esc(kicker),head=head,cells=cells)

def steps4(kicker,head,items,note):
    parts=['<article class="step"><div class="ic">{i}</div><span class="sn">{n}</span><h3>{h}</h3><p>{p}</p></article>'.format(
        i=ic(icn),n=esc(n),h=esc(h),p=esc(p)) for icn,n,h,p in items]
    row='<span class="arw">→</span>'.join(parts)
    return ('<section class="slide dark">{bar}<div class="head"><p class="kicker">{k}</p>'
        '<h2 class="h2">{head}</h2></div><div class="steps">{row}</div>'
        '<p class="note">{note}</p></section>').format(bar=bar(),k=esc(kicker),head=head,row=row,note=esc(note))

def splitwow(img,kicker,h1,points,cap):
    lis="".join('<li>{}</li>'.format(esc(x)) for x in points)
    return ('<section class="slide split">{bar}<div class="media"><img src="{i}/{img}" alt=""/>'
        '<span class="cap">{cap}</span></div><div class="copy"><p class="kicker">{k}</p>'
        '<h1 class="h1 h1--sp">{h1}</h1><ul class="pts">{lis}</ul></div></section>').format(
        bar=bar(),i=IMG,img=img,cap=esc(cap),k=esc(kicker),h1=h1,lis=lis)

def contrast(kicker,head,old,new):
    lo="".join('<li>{}</li>'.format(esc(x)) for x in old)
    ln="".join('<li>{}</li>'.format(esc(x)) for x in new)
    return ('<section class="slide dark">{bar}<div class="head"><p class="kicker">{k}</p>'
        '<h2 class="h2">{head}</h2></div><div class="cmp">'
        '<div class="cmp__c cmp__old"><p class="cmp__h">Old cameras — count</p><ul>{lo}</ul></div>'
        '<div class="cmp__c cmp__new"><p class="cmp__h">EdgeVision — understands</p><ul>{ln}</ul></div>'
        '</div></section>').format(bar=bar(),k=esc(kicker),head=head,lo=lo,ln=ln)

S=[]
S.append(cover("koc-cover.png","Kochi · 2026",
  "EdgeVision",
  "AI that turns the cameras you already have into a real-time decision engine — for your stores and restaurants."))
S.append(fb("koc-problem.png","The Problem",
  "Your cameras record everything.<br/>And tell you <span class='em'>nothing</span>.",
  "Hours of footage, every day. Almost none of it becomes a decision — until it’s already too late."))
S.append(fb("koc-idea.png","The Idea",
  "What if every camera<br/>could <span class='em'>think</span>?"))
S.append(steps4("How It Works","Simple to switch on.",
  [("camera","01","Connect","Use the cameras you already have."),
   ("eye","02","Watch","It watches every feed, all day."),
   ("chip","03","Understand","It reads the whole scene — not just motion."),
   ("bell","04","Act","Your team gets a clear alert in seconds.")],
  "No new cameras · No cloud · Runs on one small Intel box inside your store"))
S.append(fb("koc-retail.png","For your stores",
  "See every moment<br/>that <span class='em'>makes a sale</span>."))
S.append(tiles("In-Store · What you get","Three wins on every shift.",
  [("trend","More sales","Convert more of the footfall you already pay for — see what pulls people in."),
   ("users","Better service","The right staff in the right place, the moment a customer needs help."),
   ("shield","Safer store","Spills, queues, shrink and safety — caught as they happen, not after.")]))
S.append(splitwow("koc-retail2.png","A moment that matters",
  "A regular walks in —<br/>your team <span class='em'>knows in seconds</span>.",
  ["The manager’s phone lights up at the door","Name, tier and what to offer — for a warm welcome",
   "Worked out inside the store · no faces stored"],"STORE FLOOR · ONE SCREEN"))
S.append(fb("koc-qsr.png","For your restaurants",
  "Speed, accuracy, safety —<br/><span class='em'>every shift</span>."))
S.append(tiles("QSR · What you get","The three numbers every shift lives by.",
  [("clock","Faster service","Queues and slow stations spotted live — move staff before guests give up."),
   ("check","Right orders","Wrong or missing items caught before the bag leaves the counter."),
   ("leaf","Safe & clean","Gloves, hygiene and hold-times — checked continuously, audit-ready.")]))
S.append(splitwow("koc-qsr2.png","The wow moment",
  "It catches the missing item —<br/><span class='em'>before</span> the bag leaves.",
  ["Reads the order against what’s on the tray","Flags a miss the instant it happens",
   "A wrong order fixed before the customer ever sees it"],"MAKE-LINE · ORDER CHECK"))
S.append(contrast("Why It’s Different","Old cameras count. EdgeVision understands.",
  ["“A person entered the store.”","“Motion in aisle 4.”","“Someone is at the counter.”"],
  ["“A regular came in — greet them, they love the front table.”",
   "“Spill in aisle 4 — clean-up sent.”",
   "“This order is missing a sauce — fix it before it’s bagged.”"]))
S.append(fb("koc-edge.png","Private by design",
  "Everything stays in your store.<br/>On one small <span class='em'>Intel</span> box.",
  "No faces stored · nothing sent to the cloud · works even if the internet drops."))
S.append(fb("koc-close.png","Let’s start",
  "See it live in your store<br/>in <span class='em'>three weeks</span>.",
  "Pick one location. We install on your cameras. By week three you’re watching real results — with zero risk. "
  "info@pattern-ai.com · edgevision.pro · +91 99618 71254"))

CSS="""
:root{--bg:#0A0A0E;--brand:#F52E67;--brand2:#FF5C8A;--dim:#C2C2CE;--mute:#8A8A96;
  --tx:'Inter',system-ui,sans-serif;--mono:'JetBrains Mono',monospace}
@page{size:13.333in 7.5in;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#000}
body{font-family:var(--tx);color:#fff;font-weight:300;-webkit-font-smoothing:antialiased;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
.slide{position:relative;width:1280px;height:720px;overflow:hidden;background:var(--bg);
  page-break-after:always;break-after:page}
.slide:last-child{page-break-after:auto;break-after:auto}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0}
.em{color:var(--brand);font-weight:300}
.brandbar{position:absolute;top:38px;left:64px;right:64px;z-index:6;display:flex;justify-content:space-between;
  align-items:center;font-family:var(--mono);font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;
  color:rgba(255,255,255,.68)}
.brandbar b{color:#fff;font-weight:600}.brandbar .pg{color:var(--brand);letter-spacing:.12em}

/* full-bleed */
.fb .veil{position:absolute;inset:0;z-index:1;background:
  linear-gradient(180deg,rgba(6,6,10,.55),rgba(6,6,10,.05) 34%,rgba(6,6,10,.55) 72%,rgba(6,6,10,.94) 100%),
  linear-gradient(75deg,rgba(6,6,10,.78),rgba(6,6,10,.12) 62%)}
.fb .veil--cover{background:
  linear-gradient(180deg,rgba(6,6,10,.5),rgba(6,6,10,.15) 40%,rgba(6,6,10,.62) 74%,rgba(6,6,10,.97) 100%),
  linear-gradient(75deg,rgba(6,6,10,.72),rgba(6,6,10,.1) 66%)}
.content{position:absolute;left:70px;right:70px;bottom:80px;z-index:3;max-width:940px}
.kicker{font-family:var(--mono);font-size:13px;letter-spacing:.3em;text-transform:uppercase;color:var(--brand);
  margin:0 0 22px;display:inline-flex;align-items:center;gap:14px}
.kicker::before{content:"";width:40px;height:2px;background:var(--brand)}
.h1{font-weight:200;font-size:66px;line-height:1.04;letter-spacing:-.03em;color:#fff}
.sub{margin-top:26px;font-size:21px;line-height:1.5;color:var(--dim);font-weight:300;max-width:56ch}
.coverfoot{margin-top:30px;font-family:var(--mono);font-size:12px;letter-spacing:.16em;color:var(--mute);text-transform:uppercase}
.cover .word{font-weight:200;font-size:104px;letter-spacing:-.04em;line-height:.98}
.cover .word .em{font-weight:300}
.sub--cover{font-size:24px;max-width:52ch;color:#E7E7EE}

/* dark tiles / steps / contrast */
.dark{background:radial-gradient(130% 110% at 0% 0%,#15151f 0%,#0a0a0e 55%,#08080c 100%)}
.head{position:absolute;top:112px;left:70px;right:70px;z-index:3}
.h2{font-weight:200;font-size:52px;letter-spacing:-.025em;line-height:1.05;color:#fff;max-width:24ch}
.tiles{position:absolute;left:70px;right:70px;bottom:78px;z-index:3;display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.tile{background:rgba(255,255,255,.045);border:1px solid rgba(255,255,255,.11);border-radius:16px;
  padding:34px 30px 32px;min-height:238px;display:flex;flex-direction:column;gap:16px}
.tile .ic{width:50px;height:50px;color:var(--brand)}
.tile .ic svg{width:100%;height:100%;stroke:currentColor;fill:none;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.tile h3{font-size:29px;font-weight:400;letter-spacing:-.01em}
.tile p{font-size:16.5px;line-height:1.5;color:var(--dim);font-weight:300}

.steps{position:absolute;left:70px;right:70px;bottom:118px;z-index:3;display:grid;
  grid-template-columns:1fr auto 1fr auto 1fr auto 1fr;align-items:stretch;gap:14px}
.step{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.10);border-radius:16px;
  padding:28px 24px;display:flex;flex-direction:column;gap:12px}
.step .ic{width:42px;height:42px;color:var(--brand)}
.step .ic svg{width:100%;height:100%;stroke:currentColor;fill:none;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.step .sn{font-family:var(--mono);font-size:12px;letter-spacing:.2em;color:var(--mute)}
.step h3{font-size:24px;font-weight:500}
.step p{font-size:15px;line-height:1.45;color:var(--dim);font-weight:300}
.arw{align-self:center;color:var(--brand);font-size:26px}
.note{position:absolute;left:70px;bottom:66px;z-index:3;font-family:var(--mono);font-size:13px;
  letter-spacing:.12em;color:var(--dim);display:flex;align-items:center;gap:14px}
.note::before{content:"";width:34px;height:2px;background:var(--brand)}

/* contrast */
.cmp{position:absolute;left:70px;right:70px;bottom:84px;z-index:3;display:grid;grid-template-columns:1fr 1fr;gap:22px}
.cmp__c{border-radius:16px;padding:32px 34px;border:1px solid rgba(255,255,255,.11)}
.cmp__old{background:rgba(255,255,255,.035)}
.cmp__new{background:linear-gradient(180deg,rgba(245,46,103,.12),rgba(245,46,103,.03));border-color:rgba(245,46,103,.4)}
.cmp__h{font-family:var(--mono);font-size:13px;letter-spacing:.16em;text-transform:uppercase;margin:0 0 18px;color:var(--mute)}
.cmp__new .cmp__h{color:var(--brand)}
.cmp__c li{list-style:none;font-size:20px;line-height:1.4;padding:11px 0 11px 26px;position:relative;color:var(--dim)}
.cmp__new li{color:#fff}
.cmp__old li::before{content:"—";position:absolute;left:0;color:var(--mute)}
.cmp__new li::before{content:"→";position:absolute;left:0;color:var(--brand)}

/* split wow */
.split{display:grid;grid-template-columns:1.05fr 1fr;background:var(--bg)}
.split .media{position:relative;overflow:hidden}
.split .media img{width:100%;height:100%;object-fit:cover}
.split .media::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(6,6,10,.15),rgba(10,10,14,.85))}
.split .cap{position:absolute;left:24px;bottom:24px;z-index:2;font-family:var(--mono);font-size:11px;
  letter-spacing:.2em;color:#fff;background:rgba(0,0,0,.5);padding:7px 11px;border-radius:4px}
.split .copy{padding:0 74px;display:flex;flex-direction:column;justify-content:center;z-index:2}
.h1--sp{font-size:52px}
.pts{margin-top:28px;list-style:none}
.pts li{position:relative;padding:11px 0 11px 26px;font-size:19px;line-height:1.4;color:var(--dim)}
.pts li::before{content:"";position:absolute;left:0;top:20px;width:12px;height:2px;background:var(--brand)}
"""
doc=('<!doctype html><html lang="en"><head><meta charset="utf-8"/>'
     '<title>EdgeVision — Kochi Pitch</title>'
     '<link rel="stylesheet" href="fonts.css"/><style>{css}</style></head><body>{slides}</body></html>').format(
     css=CSS,slides="".join(S))
os.makedirs(os.path.dirname(OUT),exist_ok=True)
open(OUT,"w",encoding="utf-8").write(doc)
print("Wrote",OUT,"with",len(S),"slides")
