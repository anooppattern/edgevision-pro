# -*- coding: utf-8 -*-
"""EdgeVision — Retail & QSR · Intel Event Edition.
A simplified, non-technical, outcome-led 30-min pitch deck (16:9)."""
import html, os

OUT = "/home/user/edgevision-pro/deck/EdgeVision-Retail-QSR-IntelEvent.html"
IMG = "../assets/images"

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
 "car":'<path d="M3 12l2-5h14l2 5v6h-3v-2H6v2H3z"/><circle cx="7.5" cy="15.5" r="1"/><circle cx="16.5" cy="15.5" r="1"/>',
 "check":'<polyline points="4 12 10 18 20 6"/>',
 "trend":'<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
 "leaf":'<path d="M4 20c8 2 16-4 16-16-8 0-14 6-14 12 2-4 5-6 9-7"/>',
 "star":'<path d="M12 3l2.5 6 6.5.5-5 4 1.6 6.3L12 16l-5.6 3.8L8 13.5 3 9.5 9.5 9z"/>',
}
def ic(name): return '<svg viewBox="0 0 24 24">{}</svg>'.format(ICON[name])

_n=[0]
PROD="RETAIL&nbsp;&&nbsp;QSR"
FOOT_MID="One AI teammate for every camera"
def _chrome(ctx):
    return ('<div class="chrome"><span class="chrome__brand">{m}<b>PATTERN</b><i>AI&nbsp;LABS</i>'
        '<span class="chrome__div">/</span><span class="chrome__prod">{p}</span></span>'
        '<span class="chrome__ctx">{c}</span></div>').format(m=mark("mark--sm"),p=PROD,c=esc(ctx))
def _foot(n):
    return ('<div class="foot"><span>EDGEVISION · RETAIL &amp; QSR</span>'
        '<span class="foot__mid">{fm}</span><span class="foot__n">{n:02d}</span></div>').format(fm=FOOT_MID,n=n)

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

def wins(items,cls="wins"):  # (icon,h,p)
    cells="".join('<article class="win"><div class="win__ic">{i}</div><h3>{h}</h3><p>{p}</p></article>'.format(
        i=ic(icn),h=esc(h),p=esc(p)) for icn,h,p in items)
    return '<div class="{cls}">{cells}</div>'.format(cls=cls,cells=cells)

def vtiles(items):
    cells="".join('<article class="vtile"><div class="vtile__ic">{i}</div><h3>{h}</h3><p>{p}</p></article>'.format(
        i=ic(icn),h=esc(h),p=esc(p)) for icn,h,p in items)
    return '<div class="vtiles">{}</div>'.format(cells)

def steps(items):  # (icon,n,h,p)
    parts=['<div class="step"><div class="step__ic">{i}</div><span class="step__n">{n}</span>'
           '<h3>{h}</h3><p>{p}</p></div>'.format(i=ic(icn),n=esc(n),h=esc(h),p=esc(p)) for icn,n,h,p in items]
    return '<div class="steps">'+'<span class="step-arrow">→</span>'.join(parts)+'</div>'

def lenscard(head,title,bullets,kind="dash"):
    lis="".join('<li>{}</li>'.format(esc(b)) for b in bullets)
    ul='<ul class="{}">{}</ul>'.format("dashlist" if kind=="dash" else "checklist",lis)
    t='<h3>{}</h3>'.format(esc(title)) if title else ""
    return '<article class="lens"><p class="lens__head">{}</p>{}{}</article>'.format(esc(head),t,ul)
def twocol(a,b): return '<div class="two-col">{}{}</div>'.format(a,b)

def split(copy,img,cap=None):
    c='<span class="mediacap">{}</span>'.format(esc(cap)) if cap else ""
    return ('<div class="split"><div class="split__copy">{copy}</div>'
        '<div class="split__media"><img src="{i}/{m}" alt=""/>{c}</div></div>').format(copy=copy,i=IMG,m=img,c=c)
def dashlist(items): return '<ul class="dashlist dashlist--split">{}</ul>'.format(
    "".join('<li>{}</li>'.format(esc(x)) for x in items))

def ba(old,new):
    lo="".join('<li>{}</li>'.format(esc(x)) for x in old)
    ln="".join('<li>{}</li>'.format(esc(x)) for x in new)
    return ('<div class="ba"><div class="ba__col"><p class="ba__h">Old camera analytics</p><ul>{lo}</ul></div>'
        '<div class="ba__col ba__col--new"><p class="ba__h">EdgeVision</p><ul>{ln}</ul></div></div>').format(lo=lo,ln=ln)

def dotcards(items):  # (heading,[bullets]) -> 4 branded capability cards
    cells=""
    for i,(h,bl) in enumerate(items,1):
        lis="".join('<li>{}</li>'.format(esc(x)) for x in bl)
        cells+=('<article class="num-card num-card--brand"><span class="num-card__n">{n:02d}</span>'
            '<h3>{h}</h3><ul class="dotlist">{lis}</ul></article>').format(n=i,h=esc(h),lis=lis)
    return '<div class="num-grid num-grid--4">{}</div>'.format(cells)

def ucards(items):  # (title, one-sentence) -> 2-col detailed use-case grid
    cells="".join('<article class="uc"><span class="uc__n">{n:02d}</span>'
        '<div><h3>{h}</h3><p>{p}</p></div></article>'.format(n=i,h=esc(h),p=esc(p)) for i,(h,p) in enumerate(items,1))
    return '<div class="ucards">{}</div>'.format(cells)

def ucsplit(items,img,cap):  # detailed use-cases beside a relevant photo
    cells="".join('<article class="uc"><span class="uc__n">{n:02d}</span>'
        '<div><h3>{h}</h3><p>{p}</p></div></article>'.format(n=i,h=esc(h),p=esc(p)) for i,(h,p) in enumerate(items,1))
    return ('<div class="split split--uc"><div class="split__copy"><div class="ucards ucards--col">{cells}</div></div>'
        '<div class="split__media"><img src="{i}/{m}" alt=""/><span class="mediacap">{cap}</span></div></div>').format(
        cells=cells,i=IMG,m=img,cap=esc(cap))

def console(stats, hi, alerts, cams):
    DOTB='<svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#F52E67"/></svg>'
    DOTG='<svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#56565F"/></svg>'
    kv="".join('<div class="kv"><label>{l}</label><b>{v}</b></div>'.format(l=esc(l),v=esc(v)) for l,v in stats)
    heights=[18,32,48,62,74,86,70,96,78,58,42,28]
    bars="".join('<i style="--h:{h}%"{c}></i>'.format(h=h,c=' class="hi"' if idx==hi else '') for idx,h in enumerate(heights))
    al="".join('<li>{d} {t}</li>'.format(d=(DOTB if b else DOTG),t=esc(t)) for b,t in alerts)
    cs="".join('<span>{}</span>'.format(esc(c)) for c in cams)
    return ('<div class="console">'
      '<div><label>Snapshot</label><div class="console__stats">{kv}</div></div>'
      '<div><label>Hourly footfall</label><div class="bars">{bars}</div>'
      '<div class="bars__axis"><span>10AM</span><span>2PM</span><span>6PM</span><span>10PM</span></div></div>'
      '<div><label>Alert stream</label><ul class="alerts">{al}</ul></div></div>'
      '<div class="cam-strip">{cs}</div>').format(kv=kv,bars=bars,al=al,cs=cs)

S=[]
# 1 COVER
S.append('<section class="slide slide--cover"><img class="slide__bg" src="{img}/ev-cover.png" alt=""/>'
  '<div class="cover__veil"></div><div class="cover__inner">'
  '<div class="cover__top">{mk}<span class="cover__brandtxt"><b>PATTERN</b><i>AI&nbsp;LABS</i></span>'
  '<span class="cover__edition">RETAIL &amp; QSR · 2026</span></div>'
  '<p class="cover__eyebrow">EdgeVision · for Stores &amp; Restaurants</p>'
  '<h1 class="cover__wordmark"><span class="w-edge">Edge</span><span class="w-vision">Vision</span>'
  '<span class="w-sub">Retail &amp; QSR</span></h1>'
  '<p class="cover__tag">Turn the cameras you already have into a decision engine.</p>'
  '<p class="cover__sub">Real-time AI that watches every store and restaurant camera — and tells your team '
  'exactly what to do, the moment it matters. On-site. Private. Intel-powered.</p>'
  '<ul class="cover__tags"><li><svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#F52E67"/></svg> EDGE-FIRST</li><li><svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#F52E67"/></svg> PRIVACY BY DESIGN</li>'
  '<li><svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#F52E67"/></svg> INTEL POWERED</li></ul>'
  '<div class="cover__foot"><span>PATTERN AI LABS · INTEL EDGE AI PARTNER</span>'
  '<span class="cover__sigil">EDGEVISION.PRO</span></div></div></section>'.format(img=IMG,mk=mark("mark--lg")))

# 2 HOOK
S.append(statement("THE PROBLEM","The Problem",
  "Your cameras record everything.<br/>And tell you nothing.",
  "Hundreds of feeds. Thousands of hours. Almost none of it turns into a decision — "
  "until it’s already too late.","ev-hook.png"))

# 3 PROBLEM cards
S.append(slide("THE PROBLEM",
  eyebrow("The Problem")+display("Three blind spots that<br/>cost you every day.","display--mid")
  +wins([("eye","You can’t watch every camera","One person can watch a handful of screens. The rest of the store runs unseen."),
         ("clock","You find out too late","The problem shows up at the till, in a complaint, or in next month’s audit — not now."),
         ("trend","You decide on gut feel","Staffing, layout, service, speed — big calls made without the numbers to back them.")])))

# 4 IDEA
S.append(statement("THE IDEA","The Idea",
  "What if every camera<br/>could think?",
  "EdgeVision is an AI teammate that watches every camera in real time — and tells your team "
  "what’s happening and what to do, <b>right now</b>.","ev-idea.png"))

# 5 HOW IT WORKS
S.append(slide("HOW IT WORKS",
  eyebrow("How It Works")+display("Simple to switch on.","display--mid")
  +steps([("camera","STEP 01","Connect","Use the cameras you already have — nothing new to install."),
          ("eye","STEP 02","Watch","The AI watches every feed, all day, every day."),
          ("chip","STEP 03","Understand","It reads the whole scene — not just motion."),
          ("bell","STEP 04","Act","Your team gets a clear, simple alert in seconds.")])
  +'<p class="steps-note">No new cameras · No cloud · Runs on a small Intel appliance inside your store</p>'))

# 6 VALUE TILES
S.append(slide("WHAT YOU GET",
  eyebrow("What You Get")+display("Four outcomes you can feel.","display--mid")
  +vtiles([("trend","More sales","Convert more of the footfall you already pay for."),
           ("users","Better service","The right staff, in the right place, at the right moment."),
           ("shield","Less loss","Catch shrink and mistakes as they happen, not weeks later."),
           ("leaf","Safer & cleaner","Hygiene and safety, checked continuously — audit-ready.")])))

# 7 RETAIL divider (reuse statement style)
S.append(statement("RETAIL","For your stores",
  "In your stores.",
  "See every moment that decides a sale — as it happens.","fw-retail.png"))

# 8 RETAIL what it sees
a=lenscard("CUSTOMERS","Who walks in, where they linger, who’s a VIP.",
  ["Spot loyalty & high-value guests at the door","See which displays actually pull people in",
   "Know the busy moments before queues build"])
b=lenscard("STAFF","Who’s on the floor — and who’s actually helping.",
  ["Is every zone covered at peak?","Which staff turn browsers into buyers",
   "Fewer huddles, more helping"],kind="check")
S.append(slide("RETAIL · WHAT IT SEES",
  eyebrow("In-Store")+display("It watches two things at once.","display--mid")+twocol(a,b)
  +pull("<b>Same cameras. Two answers.</b> What is the customer experiencing — and how is the team performing?")))

# 9 RETAIL — use cases (customers & conversion)
S.append(slide("RETAIL · USE CASES · CUSTOMERS",
  eyebrow("Retail · Use Cases")+display("What it sees for your customers.","display--mid")
  +ucsplit([
    ("Footfall & dwell heat-maps","See where shoppers go and linger, so layout follows real behaviour."),
    ("Window & display pull-rate","Measure how many passers-by each display draws inside — and prove what works."),
    ("Browse-to-buy conversion","Track how many browsers become buyers, by zone and hour, and act the same day."),
    ("VIP & loyalty recognition","Spot a high-value guest at the door and cue the right associate — no faces stored."),
    ("Queue & checkout wait","Get an alert the instant a queue builds, so you open a till before a walk-out."),
    ("Category cross-shopping","See how customers flow between sections, and place ranges where journeys lead."),
  ],"fw-uc-customers.png","STORE FLOOR · SHOPPER JOURNEY")))

# 10 RETAIL — use cases (operation)
S.append(slide("RETAIL · USE CASES · OPERATIONS",
  eyebrow("Retail · Use Cases")+display("What it sees for your operation.","display--mid")
  +ucsplit([
    ("Zone coverage at peak","Know whether every section is staffed when it’s busy, and get alerted when it isn’t."),
    ("Service attentiveness","Measure how quickly customers are acknowledged and helped — a real service metric."),
    ("Conversion by associate","Link who was helping to what sold, so coaching is based on outcomes, not opinion."),
    ("Shrink & concealment cues","Flag tag-tampering and concealment as they happen — not at stock-take."),
    ("Slips, spills & blocked exits","Catch safety hazards the moment they appear and send the fix at once."),
    ("Display & compliance checks","Verify planogram, housekeeping and open/close standards automatically."),
  ],"fw-uc-ops.png","COUNTER & FLOOR · STAFF IN ACTION")))

# 10 RETAIL — one screen (ops console)
S.append(slide("RETAIL · ONE SCREEN",
  eyebrow("One Pane of Glass")+display("One screen your managers actually use.","display--mid")
  +console([("FOOTFALL","1,284"),("ACTIVE STAFF","12 / 14"),("ALERTS","3"),("AVG DWELL","4:21")],7,
    [(True,"VIP entered · gold tier"),(False,"Wall #3 unattended 2m"),
     (False,"Queue > 4 at till 2"),(True,"Back store > 4 staff")],
    ["CAM 01","CAM 02","CAM 03","CAM 04","CAM 05","CAM 06"])))

# 11 RETAIL VIP moment
copy=(eyebrow("A Moment That Matters")+display("A VIP walks in. Your<br/>team knows in seconds.","display--mid")
  +dashlist(["The moment they enter, the manager’s phone lights up",
             "Name, tier, last visit and favourites — ready for a warm welcome",
             "The right associate and the right offer, before they reach the rail"])
  +'<p class="steps-note">No faces are stored · it all happens inside your store</p>')
S.append(slide("RETAIL · THE VIP MOMENT",split(copy,"fw-vip.png","LOYALTY · HIGH-VALUE GUEST")))

# 10 QSR divider
S.append(statement("QSR","For your restaurants",
  "In your restaurants.",
  "Speed, accuracy and safety — on every shift, on every lane.","ev-qsr.png"))

# 11 QSR three numbers
S.append(slide("QSR · THE THREE NUMBERS",
  eyebrow("Quick-Service")+display("The three numbers<br/>every shift lives by.","display--mid")
  +wins([("clock","Speed","Counter and kiosk queues, mobile-pickup dwell and time-to-first-bag — measured live, every daypart."),
         ("check","Accuracy","Right items, right modifiers — caught before the bag ever leaves the counter."),
         ("shield","Safety","Gloves, handwash and hold-times — checked continuously, ready for the next audit.")])))

# 15 QSR — use cases (speed & accuracy)
S.append(slide("QSR · USE CASES · SPEED & ACCURACY",
  eyebrow("QSR · Use Cases")+display("Speed and accuracy, in detail.","display--mid")
  +ucsplit([
    ("Counter & kiosk queues","See queues build at the counter or kiosk and move staff before guests give up."),
    ("Time-to-first-bag","Track how long from order to hand-off, so you catch a slow shift as it happens."),
    ("Kitchen bottlenecks","Spot the station backing up the line and rebalance before tickets pile up."),
    ("Order accuracy","Check items and modifiers against the order and flag a mistake before it’s bagged."),
    ("Packaging & remakes","Catch packaging errors and rising remake rates that quietly eat margin."),
    ("Mobile & pickup dwell","See how long online and pickup orders wait at the shelf, and clear the backlog."),
  ],"ev-qsrline.png","ASSEMBLY & PASS · ORDER READY")))

# 16 QSR — use cases (safety, cleanliness & ops)
S.append(slide("QSR · USE CASES · SAFETY & OPS",
  eyebrow("QSR · Use Cases")+display("Safety, cleanliness and ops.","display--mid")
  +ucsplit([
    ("PPE compliance","Confirm gloves, hairnets and aprons are worn where they should be — audit-ready."),
    ("Handwash cadence","Track handwash frequency against your SOP, so hygiene is a habit you can prove."),
    ("Hold-time & temperature","Watch hot- and cold-hold zones for time and temperature breaches, live."),
    ("Spills & cleaning cadence","Detect spills and missed cleaning rounds in the dining area and restrooms."),
    ("Labour vs demand","Compare staffing to real demand by daypart, so you schedule to the rush."),
    ("Greeter & upsell prompts","See whether greeting and upsell moments actually happen at the counter."),
  ],"ev-qsrsafe.png","KITCHEN · HYGIENE & PREP")))

# THE ENGINE — GenAI + VLMs (why it can do all this)
S.append(slide("THE ENGINE · GENAI + VLMS",
  eyebrow("The Engine")+display("Why it can do all this: GenAI.","display--mid")
  +lede("The breakthrough is the <b>Vision-Language Model</b> — an AI that looks at a camera frame the way a "
        "person would. It reads the whole scene and its context, not just pixels or motion. That’s what lets it "
        "judge quality, spot what’s missing and explain why — across hundreds of situations, with no reprogramming for each one.")
  +wins([("eye","It understands context","Tells a real spill from a shadow, a browser from a buyer, a queue from a cluster."),
         ("check","It judges quality","A missing sauce, a pale fry, an untidy display — not just ‘a person was here.’"),
         ("chip","It adapts on its own","New store, new menu, new season — it keeps up without re-training.")])
  +'<p class="steps-note">Everyday vision runs continuously · the heavier GenAI kicks in only when it matters — efficient enough for one small Intel box</p>'))

# 17 WHY DIFFERENT
S.append(slide("WHY IT'S DIFFERENT",
  eyebrow("Why It’s Different")+display("Old cameras count.<br/>GenAI understands.","display--mid")
  +ba(["“Someone entered the store.”","“A person is at the counter.”","“Motion in aisle 4.”"],
      ["“They browsed 4 minutes, loved the front table, and left without buying — and who was nearby.”",
       "“This order is missing a sauce — fix it before it’s bagged.”",
       "“Spill in aisle 4 — clean-up sent.”"])))

# 18 THE BUSINESS CASE — where it shows up in the P&L
S.append(slide("THE BUSINESS CASE",
  eyebrow("The Business Case")+display("Where it shows up in your P&amp;L.","display--mid")
  +vtiles([("trend","More sales","Convert more of today’s footfall — a small lift on traffic you already have moves the number."),
           ("shield","Less shrink","Catch loss and process gaps as they happen — not at stock-take."),
           ("clock","More throughput","Shorter queues and faster service mean more covers and baskets per hour."),
           ("star","More loyalty","Fewer wrong orders and cleaner stores lift repeat visits and reviews.")])
  +pull("<b>The math is simple.</b> A one-point lift in conversion on 50,000 monthly visitors is thousands of extra "
        "baskets a month — from cameras you already own.")))

# 14 PRIVACY + INTEL
S.append(slide("PRIVATE BY DESIGN",
  eyebrow("Private by Design")+display("Everything stays in your store.","display--mid")
  +wins([("lock","No faces leave","No biometrics and no video are sent anywhere. Ever."),
         ("shield","No cloud needed","Runs fully on-site — it keeps working even if the internet drops."),
         ("chip","Intel-powered","A small, efficient Intel appliance per site — nothing else to buy.")],cls="reassure")
  +'<div style="display:flex;align-items:center;gap:20px;margin-top:22px">'
   '<div class="intel-badge"><span class="intel-badge__inner">intel<i>partner</i></span></div>'
   '<p style="font-size:.95rem;color:var(--text-dim);max-width:46ch;margin:0">Pattern AI Labs is an '
   '<b style="color:#fff">Intel Edge AI Partner</b> — EdgeVision is optimised on Intel hardware for real-time '
   'inference at the edge.</p></div>'))

# 15 PROOF
S.append(slide("PROOF",
  eyebrow("Proof")+display("Built by a team that’s<br/>shipped this before.","display--mid")
  +wins([("chip","Intel Edge AI Partner","Optimised on Intel and featured in Intel’s partner ecosystem."),
         ("trend","Production CV at scale","800+ product types already live in real grocery-vision deployments."),
         ("star","Retail + QSR focus","Purpose-built for stores and multi-unit quick-service brands.")])
  +'<div class="trusted"><span class="trusted__l">TRUSTED BY</span><span>Intel</span>'
   '<span>TATA</span><span>Schneider Electric</span><span>BigBasket</span></div>'))

# 16 CLOSING / CTA
S.append('<section class="slide slide--closing"><img class="slide__bg" src="{img}/ev-closing.png" alt=""/>'
  '<div class="closing__veil"></div><div class="closing__inner">'
  '<div class="closing__brand">{mk}<span class="cover__brandtxt"><b>PATTERN</b><i>AI&nbsp;LABS</i></span></div>'
  '<h2 class="closing__head">See it live in your store<br/>in <span class="grad">three weeks</span>.</h2>'
  '<p class="closing__sub">Pick one location. We install on the cameras you already have. '
  'By week three you’re watching real results on your own floor — with no risk to the rest of your estate.</p>'
  '<div class="contact"><a class="contact__card"><span class="contact__h">EMAIL</span><span class="contact__v">info@pattern-ai.com</span></a>'
  '<a class="contact__card"><span class="contact__h">WEB</span><span class="contact__v">www.edgevision.pro</span></a>'
  '<a class="contact__card"><span class="contact__h">PHONE</span><span class="contact__v">+91 99618 71254</span></a></div>'
  '<div class="closing__foot"><span>LET’S PICK ONE OF YOUR LOCATIONS</span>'
  '<span>© 2026 PATTERN AI LABS · INTEL EDGE AI PARTNER</span></div></div></section>'.format(img=IMG,mk=mark("mark--lg")))

CSS=open("/home/user/edgevision-pro/deck/deck.css").read()
doc=('<!doctype html><html lang="en"><head><meta charset="utf-8"/>'
     '<title>EdgeVision — Retail & QSR · Intel Event Edition</title>'
     '<link rel="stylesheet" href="fonts.css"/><style>{css}</style></head><body>{sym}{slides}</body></html>').format(
     css=CSS,sym=MARK_SYMBOL,slides="".join(S))
os.makedirs(os.path.dirname(OUT),exist_ok=True)
open(OUT,"w",encoding="utf-8").write(doc)
print("Wrote",OUT,"with",_n[0],"slides")
