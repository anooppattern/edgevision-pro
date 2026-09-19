# -*- coding: utf-8 -*-
"""EdgeVision × Zach & Kiki — Retail use-cases + Statement of Work deck (16:9, edgevision.pro theme)."""
import html, os
OUT = "/home/user/edgevision-pro/deck/EdgeVision-ZachKiki-Retail-SOW.html"
IMG = "../assets/images"
DATE = "SEPTEMBER 2026"
CLIENT = "Zach &amp; Kiki"

rects = "\n".join('<rect x="22.7" y="2.4" width="2.6" height="13.6" rx="1.3"{}/>'.format(
    "" if a==0 else ' transform="rotate({} 24 24)"'.format(a)) for a in range(0,360,15))
MARK_SYMBOL = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true">'
    '<symbol id="pat-mark" viewBox="0 0 48 48"><g fill="currentColor">'+rects+'</g></symbol></svg>')
def mark(cls=""): return '<svg class="mark {}" aria-hidden="true"><use href="#pat-mark"/></svg>'.format(cls)
def esc(s): return html.escape(s, quote=False)

ICON = {
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
 "star":'<path d="M12 3l2.5 6 6.5.5-5 4 1.6 6.3L12 16l-5.6 3.8L8 13.5 3 9.5 9.5 9z"/>',
 "door":'<path d="M6 3h9v18H6z"/><path d="M6 3 18 5v16l-3-1"/><circle cx="13" cy="12" r="1"/>',
}
def ic(name): return '<svg viewBox="0 0 24 24">{}</svg>'.format(ICON[name])

_n=[0]
PROD="ZACH&nbsp;&&nbsp;KIKI"
FOOT_MID="Retail intelligence for children’s stores"
def _chrome(ctx):
    return ('<div class="chrome"><span class="chrome__brand">{m}<b>PATTERN</b><i>AI&nbsp;LABS</i>'
        '<span class="chrome__div">/</span><span class="chrome__prod">{p}</span></span>'
        '<span class="chrome__ctx">{c}</span></div>').format(m=mark("mark--sm"),p=PROD,c=esc(ctx))
def _foot(n):
    return ('<div class="foot"><span>EDGEVISION · FOR {cl}</span>'
        '<span class="foot__mid">{fm}</span><span class="foot__n">{n:02d}</span></div>').format(
        cl=CLIENT.upper(),fm=FOOT_MID,n=n)
def slide(ctx, body, cls=""):
    _n[0]+=1
    return '<section class="slide {cls}">{c}<div class="slide__body">{b}</div>{f}</section>'.format(
        cls=cls,c=_chrome(ctx),b=body,f=_foot(_n[0]))
def statement(ctx, eye, lead, sub, bg):
    _n[0]+=1
    body=('<p class="statement__eye">{eye}</p><h2 class="statement__lead">{lead}</h2>'
          '<p class="statement__sub">{sub}</p>').format(eye=esc(eye),lead=lead,sub=sub)
    return ('<section class="slide slide--statement"><img class="slide__bg" src="{img}/{bg}" alt=""/>'
        '<div class="divveil"></div>{c}<div class="slide__body">{b}</div>{f}</section>').format(
        img=IMG,bg=bg,c=_chrome(ctx),b=body,f=_foot(_n[0]))

def eyebrow(t): return '<p class="eyebrow">{}</p>'.format(esc(t))
def display(t,cls=""): return '<h2 class="display {}">{}</h2>'.format(cls,t)
def lede(t): return '<p class="lede">{}</p>'.format(t)
def pull(t): return '<p class="pullquote"><span class="pullquote__bar"></span><span>{}</span></p>'.format(t)
def wins(items,cls="wins"):
    cells="".join('<article class="win"><div class="win__ic">{i}</div><h3>{h}</h3><p>{p}</p></article>'.format(
        i=ic(icn),h=esc(h),p=esc(p)) for icn,h,p in items)
    return '<div class="{cls}">{cells}</div>'.format(cls=cls,cells=cells)
def steps(items):
    parts=['<div class="step"><div class="step__ic">{i}</div><span class="step__n">{n}</span>'
           '<h3>{h}</h3><p>{p}</p></div>'.format(i=ic(icn),n=esc(n),h=esc(h),p=esc(p)) for icn,n,h,p in items]
    return '<div class="steps">'+'<span class="step-arrow">→</span>'.join(parts)+'</div>'
def numcards(items,cols=4,brand=True):
    bc=" num-card--brand" if brand else ""
    cells="".join('<article class="num-card{bc}"><span class="num-card__n">{n:02d}</span>'
        '<h3>{h}</h3><p>{p}</p></article>'.format(bc=bc,n=i,h=esc(h),p=esc(p)) for i,(h,p) in enumerate(items,1))
    return '<div class="num-grid num-grid--{c}">{cells}</div>'.format(c=cols,cells=cells)
def ucsplit(items,img,cap):
    cells="".join('<article class="uc"><span class="uc__n">{n:02d}</span>'
        '<div><h3>{h}</h3><p>{p}</p></div></article>'.format(n=i,h=esc(h),p=esc(p)) for i,(h,p) in enumerate(items,1))
    return ('<div class="split split--uc"><div class="split__copy"><div class="ucards ucards--col">{cells}</div></div>'
        '<div class="split__media"><img src="{i}/{m}" alt=""/><span class="mediacap">{cap}</span></div></div>').format(
        cells=cells,i=IMG,m=img,cap=esc(cap))
def ucards(items):
    cells="".join('<article class="uc"><span class="uc__n">{n:02d}</span>'
        '<div><h3>{h}</h3><p>{p}</p></div></article>'.format(n=i,h=esc(h),p=esc(p)) for i,(h,p) in enumerate(items,1))
    return '<div class="ucards">{}</div>'.format(cells)
def lenscard(head,title,bullets,kind="check"):
    lis="".join('<li>{}</li>'.format(esc(b)) for b in bullets)
    ul='<ul class="{}">{}</ul>'.format("dashlist" if kind=="dash" else "checklist",lis)
    t='<h3>{}</h3>'.format(esc(title)) if title else ""
    return '<article class="lens"><p class="lens__head">{}</p>{}{}</article>'.format(esc(head),t,ul)
def twocol(a,b): return '<div class="two-col">{}{}</div>'.format(a,b)
def weeks(items):
    cells="".join('<article class="week{f}"><span class="week__n">{wn}</span>'
        '<h3>{h}</h3><p>{p}</p></article>'.format(f=" week--first" if i==0 else "",wn=esc(wn),h=esc(h),p=esc(p))
        for i,(wn,h,p) in enumerate(items))
    return '<div class="weeks weeks--4" style="grid-template-columns:repeat(3,1fr)">{}</div>'.format(cells)

def console(stats, hi, alerts, cams):
    DOTB='<svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#F52E67"/></svg>'
    DOTG='<svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#56565F"/></svg>'
    kv="".join('<div class="kv"><label>{l}</label><b>{v}</b></div>'.format(l=esc(l),v=esc(v)) for l,v in stats)
    heights=[16,28,44,60,76,88,72,94,80,60,40,26]
    bars="".join('<i style="--h:{h}%"{c}></i>'.format(h=h,c=' class="hi"' if idx==hi else '') for idx,h in enumerate(heights))
    al="".join('<li>{d} {t}</li>'.format(d=(DOTB if b else DOTG),t=esc(t)) for b,t in alerts)
    cs="".join('<span>{}</span>'.format(esc(c)) for c in cams)
    return ('<div class="console">'
      '<div><label>Snapshot</label><div class="console__stats">{kv}</div></div>'
      '<div><label>Family footfall · today</label><div class="bars">{bars}</div>'
      '<div class="bars__axis"><span>10AM</span><span>1PM</span><span>4PM</span><span>8PM</span></div></div>'
      '<div><label>Alert stream</label><ul class="alerts">{al}</ul></div></div>'
      '<div class="cam-strip">{cs}</div>').format(kv=kv,bars=bars,al=al,cs=cs)

S=[]
# 1 · COVER
S.append('<section class="slide slide--cover"><img class="slide__bg" src="{img}/zk-cover.png" alt=""/>'
  '<div class="cover__veil"></div><div class="cover__inner">'
  '<div class="cover__top">{mk}<span class="cover__brandtxt"><b>PATTERN</b><i>AI&nbsp;LABS</i></span>'
  '<span class="cover__edition">STATEMENT OF WORK · {date}</span></div>'
  '<p class="cover__eyebrow">Retail Intelligence · Prepared for {cl}</p>'
  '<h1 class="cover__wordmark"><span class="w-edge">Edge</span><span class="w-vision">Vision</span>'
  '<span class="w-sub">for {cl}</span></h1>'
  '<p class="cover__tag">Every camera in your store &amp; fulfilment — a real-time teammate for a safe, delightful family experience.</p>'
  '<p class="cover__sub">A proposal to turn the cameras {cl} already has into live retail intelligence — across your '
  'store floor and packing space — family experience, child safety and order accuracy, running on-site, private by design.</p>'
  '<ul class="cover__tags"><li><svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#F52E67"/></svg> CHILD-SAFE</li><li><svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#F52E67"/></svg> PRIVACY BY DESIGN</li>'
  '<li><svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#F52E67"/></svg> INTEL EDGE</li></ul>'
  '<div class="cover__foot"><span>PATTERN AI LABS · PREPARED FOR {clu}</span>'
  '<span class="cover__sigil">EDGEVISION.PRO</span></div></div></section>'.format(
    img=IMG,mk=mark("mark--lg"),date=DATE,cl=CLIENT,clu=CLIENT.upper()))

# 2 · Context — children's retail
S.append(slide("CONTEXT",
  eyebrow("Prepared for "+CLIENT.replace("&amp;","&"))
  +display("A kids’ fashion brand,<br/>online and in-store.","display--mid")
  +lede("Zach &amp; Kiki is loved online and in the store — with festive and occasion peaks (Onam, heirloom, best-sellers). "
        "Whether a parent is on your shop floor or an order is on the packing table, the moments that build loyalty happen in real time.")
  +wins([("users","Online-first, store-loved","Families discover you online and come in to touch the fabric — both journeys deserve to be understood, not guessed."),
         ("star","Festive & occasion peaks","Onam, occasion and heirloom drops bring surges — of footfall in-store and orders to pack — that are hard to staff by gut feel."),
         ("shield","Little customers, big duty of care","Small children on the shop floor mean safety and attentiveness matter as much as the sale.")])))

# 3 · The Opportunity (blind spots)
S.append(slide("THE OPPORTUNITY",
  eyebrow("The Opportunity")+display("What your cameras see<br/>but can’t tell you.","display--mid")
  +wins([("eye","You can’t watch every corner","Fitting areas, aisles, the storeroom, the packing bench and the entrance — all at once is impossible for one team."),
         ("clock","You learn too late","A wandering child, a spill, a best-seller stocked out, a wrong-size dispatch — noticed after it matters, not now."),
         ("trend","You decide on gut feel","Which displays convert, when the festive rush hits, how to staff store and packing — guessed, not measured.")])))

# 4 · EdgeVision key features
S.append(slide("THE PLATFORM",
  eyebrow("EdgeVision · Key Features")+display("One platform. On your cameras.","display--mid")
  +numcards([
    ("Edge-first","Runs on a small Intel appliance inside the store. No cloud dependency — it keeps working if the internet drops."),
    ("GenAI + VLMs","Reads the whole scene like a person would — safety, behaviour, quality — not just motion or a tripwire."),
    ("Private by design","No faces stored, no video leaves the store. Built to be safe for a children’s environment."),
    ("Acts in seconds","A clear, simple alert to the right person’s phone — the instant something needs attention."),
  ])
  +'<p class="steps-note">Uses your existing cameras · a small on-site edge box (a few added only where coverage needs it)</p>'))

# 5 · How it works
S.append(slide("HOW IT WORKS",
  eyebrow("How It Works")+display("Simple to switch on.","display--mid")
  +steps([("camera","STEP 01","Connect","Use the cameras you already have — a small edge box on the store LAN."),
          ("eye","STEP 02","Watch","The AI watches every feed, all day, every day."),
          ("chip","STEP 03","Understand","It reads the whole scene — safety, families, service."),
          ("bell","STEP 04","Act","Your team gets a clear alert in seconds.")])
  +'<p class="steps-note">No new cameras to rip out · No cloud · Runs on a small Intel appliance inside your store</p>'))

# 6 · Divider — use cases
S.append(statement("USE CASES","For "+CLIENT.replace("&amp;","&"),
  "Use cases for store &amp; fulfilment.",
  "Grouped for a kids’ fashion brand — family experience, child safety, and D2C fulfilment &amp; operations.","zk-store.png"))

# 7 · Family experience use cases
S.append(slide("USE CASES · FAMILY EXPERIENCE",
  eyebrow("Use Cases · Family Experience")+display("Delight the family, win the basket.","display--mid")
  +ucsplit([
    ("Footfall & dwell by section","See how many families come in and where they linger — infants, boys, girls, occasion wear."),
    ("Festive & occasion display pull","Measure which displays — Onam, occasion, best-sellers — actually draw families in and convert."),
    ("Fit, size & trial demand","See trial-area demand and which sizes families ask for, so you stock and staff to real behaviour."),
    ("Browse-to-buy by category","Track how browsers become buyers across sections and price points, and act the same day."),
    ("Queue & billing wait","An alert the moment the till queue builds — so families aren’t kept waiting, especially at COD and festive rush."),
    ("Repeat-family welcome","Recognise loyal parents at the door for a warm welcome — no faces stored."),
  ],"zk-family.png","STORE FLOOR · THE FAMILY JOURNEY")))

# 8 · Child safety use cases (the hero)
S.append(slide("USE CASES · CHILD SAFETY",
  eyebrow("Use Cases · Child Safety & Care")+display("Peace of mind, watched continuously.","display--mid")
  +ucsplit([
    ("Unattended-child alert","Flag a child who’s been on their own too long, so a team member can gently step in."),
    ("Exit & door watch","A little one drifting toward the open entrance triggers an instant nudge to staff."),
    ("Floor-hazard detection","Spills, dropped pins or small parts (a choking risk) and scattered stock — caught the moment they appear."),
    ("Restricted-area entry","A child slipping into the stockroom or back-of-house is flagged immediately."),
    ("Slips & blocked aisles","Obstructions and hazards surfaced before anyone trips."),
    ("After-hours security","Motion in the closed store or restricted zones flagged out of hours."),
  ],"zk-safety.png","SAFETY · DUTY OF CARE")))

# 9 · Fulfilment & Operations (D2C) use cases
S.append(slide("USE CASES · FULFILMENT & OPS",
  eyebrow("Use Cases · Fulfilment & Operations")+display("Right size, right box, out the door.","display--mid")
  +ucsplit([
    ("Pack accuracy — style & size","Check the packed order against the ticket before the box is sealed — right print, right size — so wrong-size returns drop."),
    ("Dispatch & hand-off visibility","See packing, staging and courier hand-off as they happen, and clear a backlog before it slows the day."),
    ("Festive stock & fast-movers","Watch shelves for best-sellers and festive drops (Onam, occasion) running low — restock before you sell out."),
    ("Staff vs order volume","Compare packing staff to real order flow by hour, so festive surges are covered."),
    ("Shrink & process gaps","Flag mishandling and process gaps as they happen — not at month-end stock-take."),
    ("Camera & area health","Know at once if a camera is down, moved or blocked."),
  ],"zk-fulfil.png","PACKING & DISPATCH · D2C")))

# 10 · One screen
S.append(slide("ONE SCREEN",
  eyebrow("One Pane of Glass")+display("One screen your store team<br/>actually uses.","display--mid")
  +console([("FOOTFALL","842"),("FAMILIES","310"),("ACTIVE STAFF","6 / 7"),("OPEN ALERTS","2")],7,
    [(True,"Child unattended · kids aisle"),(True,"Exit approach · front door"),
     (False,"Queue > 3 at billing"),(False,"Spill · aisle 4")],
    ["CAM 01","CAM 02","CAM 03","CAM 04","CAM 05","CAM 06"])))

# 11 · Private by design
S.append(slide("PRIVATE BY DESIGN",
  eyebrow("Private by Design")+display("Especially important with children.","display--mid")
  +wins([("lock","No faces stored","No biometrics and no video are sent anywhere. Recognition (loyalty opt-ins only) is matched on-box and discarded."),
         ("shield","Everything stays on-site","Runs fully on-prem — aligned with India’s DPDP data-protection expectations for minors."),
         ("chip","Intel-powered edge","A small, efficient Intel appliance per store — nothing else to buy or send away.")],cls="reassure")))

# 12 · Scope of Work
inscope=lenscard("IN SCOPE · WE DELIVER","",
  ["Edge appliance install & camera on-boarding (RTSP)","Configure selected use cases — family experience, child safety & fulfilment",
   "Live operations dashboard + mobile / WhatsApp alerts","Manager & packing-team training + alert rehearsal",
   "Weekly insights report (store &/or fulfilment)","Support through the pilot"],kind="check")
youprovide=lenscard("YOU PROVIDE","",
  ["Access to existing IP cameras (store &/or packing area)","Store / site LAN access for the edge box",
   "A single point of contact","Site access for a half-day install",
   "Sign-off on which use cases go live first"],kind="dash")
S.append(slide("SCOPE OF WORK",
  eyebrow("Statement of Work")+display("What a pilot includes.","display--mid")+twocol(inscope,youprovide)
  +pull("<b>Start with one store.</b> We prove the safety and experience use cases on your own floor before any wider rollout — with zero risk to the rest of your estate.")))

# 13 · Engagement / timeline
S.append(slide("ENGAGEMENT",
  eyebrow("Engagement Model")+display("From cameras to insights<br/>in three weeks.","display--mid")
  +weeks([
    ("WEEK 01","Audit & Install","Site survey, camera audit, edge box on the store LAN. Baseline data collection starts."),
    ("WEEK 02","Calibrate & Tune","Zone & play-area definitions, safety thresholds, alert routing wired to your team’s phones."),
    ("WEEK 03","Handover & Train","Manager training, dashboard onboarding, alert rehearsal, first weekly insights report.")])
  +pull("<b>By end of week 3:</b> a running EdgeVision install, live safety &amp; experience alerts, and a store team that has run a full daily cycle on the console.")))

# 14 · Commercials / Pricing
poc=('<article class="price-card price-card--poc"><div class="price-card__tag">STAGE 01</div>'
  '<h3>Proof of Concept</h3><p class="price-card__lead">We invest in the hardware and waive the fees — you try it risk-free.</p>'
  '<ul class="pricelist">'
  '<li><span class="pl__k">Per-camera usage fee</span><span class="pl__v pl__v--free">Waived</span></li>'
  '<li><span class="pl__k">Hardware cost</span><span class="pl__v pl__v--free">We invest</span></li>'
  '<li><span class="pl__k">Refundable security deposit</span><span class="pl__v">₹20,000</span></li></ul>'
  '<p class="price-card__note">Fully refunded once the POC is approved and you decide to proceed.</p></article>')
post=('<article class="price-card price-card--post"><div class="price-card__tag">STAGE 02</div>'
  '<h3>Post-POC · Rollout</h3><p class="price-card__lead">Go live across stores on a simple, predictable model.</p>'
  '<ul class="pricelist">'
  '<li><span class="pl__k">One-time hardware<br/><i>by compute for the use cases deployed</i></span>'
  '<span class="pl__v">₹1&ndash;1.5&nbsp;<em>lakh</em></span></li>'
  '<li><span class="pl__k">Ongoing software</span><span class="pl__v">₹500 <em>/ camera / month</em></span></li></ul>'
  '<p class="price-card__note">Flexible — further negotiable on the number of stores and overall volume.</p></article>')
price_privacy=('<div class="price-privacy"><div class="price-privacy__ic"><svg viewBox="0 0 24 24">'
  '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg></div>'
  '<div><p class="price-privacy__h">Edge-compute architecture · private by design</p>'
  '<p class="price-privacy__p">All CCTV data stays on-premise on the edge server inside your store — '
  '<b>nothing is sent to the cloud</b> unless a specific use case requires it. Full compliance with the latest '
  'privacy regulations and data-handling standards.</p></div></div>')
S.append(slide("COMMERCIALS",
  eyebrow("Commercials")+display("Simple pricing. Risk-free to start.","display--mid")
  +'<div class="price-grid">'+poc+post+'</div>'+price_privacy))

# 15 · Close / contact
S.append('<section class="slide slide--closing"><img class="slide__bg" src="{img}/zk-closing.png" alt=""/>'
  '<div class="closing__veil"></div><div class="closing__inner">'
  '<div class="closing__brand">{mk}<span class="cover__brandtxt"><b>PATTERN</b><i>AI&nbsp;LABS</i></span></div>'
  '<h2 class="closing__head">Let’s make every {cl}<br/>store <span class="grad">safe &amp; delightful</span>.</h2>'
  '<p class="closing__sub">Pick one store. We install on the cameras you already have. By week three you’re watching '
  'real safety and experience results on your own floor — with no risk to the rest of your estate.</p>'
  '<div class="contact"><a class="contact__card"><span class="contact__h">EMAIL</span><span class="contact__v">info@pattern-ai.com</span></a>'
  '<a class="contact__card"><span class="contact__h">WEB</span><span class="contact__v">www.edgevision.pro</span></a>'
  '<a class="contact__card"><span class="contact__h">PHONE</span><span class="contact__v">+91 99618 71254</span></a></div>'
  '<div class="closing__foot"><span>PREPARED FOR {clu} · {date}</span>'
  '<span>© 2026 PATTERN AI LABS</span></div></div></section>'.format(
    img=IMG,mk=mark("mark--lg"),cl=CLIENT,clu=CLIENT.upper(),date=DATE))

PRICE_CSS="""
.price-grid{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--border);border:1px solid var(--border);margin-top:12px}
.price-card{background:var(--bg);padding:22px 26px 22px;display:flex;flex-direction:column;position:relative}
.price-card--post{background:linear-gradient(180deg,rgba(245,46,103,.06),var(--bg))}
.price-card__tag{font-family:var(--mono);font-size:.58rem;letter-spacing:.24em;color:var(--text-mute);margin-bottom:12px}
.price-card--post .price-card__tag{color:var(--brand)}
.price-card h3{font-family:var(--tx);font-weight:400;font-size:1.4rem;color:#fff;margin:0 0 6px}
.price-card__lead{font-size:.82rem;line-height:1.4;color:var(--text-dim);margin:0 0 14px}
.pricelist{margin:0;padding:0;list-style:none;border-top:1px solid var(--border)}
.pricelist li{display:flex;align-items:baseline;justify-content:space-between;gap:16px;padding:11px 0;border-bottom:1px solid var(--border)}
.pl__k{font-size:.84rem;color:var(--text-dim);line-height:1.3}
.pl__k i{display:block;font-style:normal;font-size:.68rem;color:var(--text-mute);margin-top:2px}
.pl__v{font-family:var(--tx);font-weight:300;font-size:1.35rem;color:#fff;white-space:nowrap;text-align:right}
.pl__v em{font-style:normal;font-size:.6em;color:var(--text-dim);font-weight:300}
.pl__v--free{color:var(--brand);font-size:1.05rem;font-weight:500;letter-spacing:.02em}
.price-card__note{margin:14px 0 0;font-size:.74rem;line-height:1.4;color:var(--text-mute)}
.price-card--post .price-card__note{color:var(--text-dim)}
.price-privacy{display:flex;gap:18px;align-items:flex-start;margin-top:16px;padding:18px 22px;border:1px solid var(--border-2);background:var(--bg-2)}
.price-privacy__ic{width:34px;height:34px;color:var(--brand);flex:0 0 auto}
.price-privacy__ic svg{width:100%;height:100%;stroke:currentColor;fill:none;stroke-width:1.4}
.price-privacy__h{font-family:var(--tx);font-weight:600;font-size:.9rem;color:#fff;margin:0 0 4px}
.price-privacy__p{font-size:.8rem;line-height:1.45;color:var(--text-dim);margin:0;max-width:none}
.price-privacy__p b{color:#fff}
"""
CSS=open("/home/user/edgevision-pro/deck/deck.css").read()+PRICE_CSS
doc=('<!doctype html><html lang="en"><head><meta charset="utf-8"/>'
     '<title>EdgeVision × Zach &amp; Kiki — Retail SOW</title>'
     '<link rel="stylesheet" href="fonts.css"/><style>{css}</style></head><body>{sym}{slides}</body></html>').format(
     css=CSS,sym=MARK_SYMBOL,slides="".join(S))
os.makedirs(os.path.dirname(OUT),exist_ok=True)
open(OUT,"w",encoding="utf-8").write(doc)
print("Wrote",OUT,"with",_n[0]+2,"slides")
