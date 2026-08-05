# -*- coding: utf-8 -*-
"""EdgeVision — Retail & QSR : one comprehensive deck (16:9, edgevision.pro theme)."""
import html, os

OUT = "/home/user/edgevision-pro/deck/EdgeVision-Retail-QSR.html"
IMG = "../assets/images"

rects = "\n".join(
    '<rect x="22.7" y="2.4" width="2.6" height="13.6" rx="1.3"{}/>'.format(
        "" if a == 0 else ' transform="rotate({} 24 24)"'.format(a)) for a in range(0, 360, 15))
MARK_SYMBOL = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true">'
    '<symbol id="pat-mark" viewBox="0 0 48 48"><g fill="currentColor">'+rects+'</g></symbol></svg>')
def mark(cls=""): return '<svg class="mark {}" aria-hidden="true"><use href="#pat-mark"/></svg>'.format(cls)
def esc(s): return html.escape(s, quote=False)

_n = [0]
PROD = "RETAIL&nbsp;&&nbsp;QSR"
FOOT_MID = "Two products of the store floor · one edge platform"
def slide(ctx, body, cls=""):
    _n[0]+=1
    chrome=('<div class="chrome"><span class="chrome__brand">{m}<b>PATTERN</b><i>AI&nbsp;LABS</i>'
        '<span class="chrome__div">/</span><span class="chrome__prod">{prod}</span></span>'
        '<span class="chrome__ctx">{ctx}</span></div>').format(m=mark("mark--sm"),prod=PROD,ctx=esc(ctx))
    foot=('<div class="foot"><span>EDGEVISION · RETAIL &amp; QSR</span>'
        '<span class="foot__mid">{fm}</span><span class="foot__n">{n:02d}</span></div>').format(fm=FOOT_MID,n=_n[0])
    return ('<section class="slide {cls}">{chrome}<div class="slide__body">{body}</div>{foot}</section>').format(
        cls=cls,chrome=chrome,body=body,foot=foot)

def divider(ctx, num, title, sub, bg):
    _n[0]+=1
    chrome=('<div class="chrome"><span class="chrome__brand">{m}<b>PATTERN</b><i>AI&nbsp;LABS</i>'
        '<span class="chrome__div">/</span><span class="chrome__prod">{prod}</span></span>'
        '<span class="chrome__ctx">{ctx}</span></div>').format(m=mark("mark--sm"),prod=PROD,ctx=esc(ctx))
    foot=('<div class="foot"><span>EDGEVISION · RETAIL &amp; QSR</span>'
        '<span class="foot__mid">{fm}</span><span class="foot__n">{n:02d}</span></div>').format(fm=FOOT_MID,n=_n[0])
    body=('<p class="divider__num">{num}</p><h2 class="divider__title">{title}</h2>'
        '<p class="divider__sub">{sub}</p><div class="divider__rule"></div>').format(num=esc(num),title=title,sub=esc(sub))
    return ('<section class="slide slide--divider"><img class="slide__bg" src="{img}/{bg}" alt=""/>'
        '<div class="divveil"></div>{chrome}<div class="slide__body">{body}</div>{foot}</section>').format(
        img=IMG,bg=bg,chrome=chrome,body=body,foot=foot)

def eyebrow(t): return '<p class="eyebrow">{}</p>'.format(esc(t))
def display(t,cls=""): return '<h2 class="display {}">{}</h2>'.format(cls,t)
def lede(t): return '<p class="lede">{}</p>'.format(t)
def pull(t): return '<p class="pullquote"><span class="pullquote__bar"></span><span>{}</span></p>'.format(t)

def numcards(items,cols=4,brand=False):
    bc=" num-card--brand" if brand else ""
    cells="".join('<article class="num-card{bc}"><span class="num-card__n">{n:02d}</span>'
        '<h3>{h}</h3><p>{p}</p></article>'.format(bc=bc,n=i,h=esc(h),p=p) for i,(h,p) in enumerate(items,1))
    return '<div class="num-grid num-grid--{c}">{cells}</div>'.format(c=cols,cells=cells)

def dotcards(items):  # 4 cards each with a header + bullet list
    cells=""
    for i,(h,bl) in enumerate(items,1):
        lis="".join('<li>{}</li>'.format(esc(x)) for x in bl)
        cells+=('<article class="num-card num-card--brand"><span class="num-card__n">{n:02d}</span>'
            '<h3>{h}</h3><ul class="dotlist">{lis}</ul></article>').format(n=i,h=esc(h),lis=lis)
    return '<div class="num-grid num-grid--4">{}</div>'.format(cells)

def circles(items,cols=3):
    cells="".join('<article class="circ"><span class="circ__n">{n}</span><h3>{h}</h3><p>{p}</p></article>'.format(
        n=i,h=esc(h),p=p) for i,(h,p) in enumerate(items,1))
    return '<div class="circle-grid circle-grid--{c}">{cells}</div>'.format(c=cols,cells=cells)

def pipeline(steps):
    parts=['<div class="pipe-card"><span class="pipe-card__n">{lab}</span><h3>{h}</h3><p>{p}</p></div>'.format(
        lab=(lab if lab else "{:02d}".format(i)),h=esc(h),p=esc(p)) for i,(lab,h,p) in enumerate(steps,1)]
    return '<div class="pipeline pipeline--{}">{}</div>'.format(len(steps),'<span class="pipe-arrow">→</span>'.join(parts))

def stats(items):
    cells="".join('<div><b>{}</b><span>{}</span></div>'.format(big,esc(sub)) for big,sub in items)
    return '<div class="stats stats--{}">{}</div>'.format(len(items),cells)

def lenscard(head,title,bullets,kind="dash"):
    lis="".join('<li>{}</li>'.format(esc(b)) for b in bullets)
    ul='<ul class="{}">{}</ul>'.format("dashlist" if kind=="dash" else "checklist",lis)
    t='<h3>{}</h3>'.format(esc(title)) if title else ""
    return '<article class="lens"><p class="lens__head">{}</p>{}{}</article>'.format(esc(head),t,ul)
def twocol(a,b): return '<div class="two-col">{}{}</div>'.format(a,b)

def split(copy,img,cap=None,cls=""):
    c='<span class="mediacap">{}</span>'.format(esc(cap)) if cap else ""
    return ('<div class="split {cls}"><div class="split__copy">{copy}</div>'
        '<div class="split__media"><img src="{i}/{m}" alt=""/>{c}</div></div>').format(cls=cls,copy=copy,i=IMG,m=img,c=c)

def dashlist(items,cls=""):
    return '<ul class="dashlist {}">{}</ul>'.format(cls,"".join('<li>{}</li>'.format(esc(x)) for x in items))

S=[]

# 1 · COVER
S.append('<section class="slide slide--cover"><img class="slide__bg" src="{img}/ev-cover.png" alt=""/>'
  '<div class="cover__veil"></div><div class="cover__inner">'
  '<div class="cover__top">{mk}<span class="cover__brandtxt"><b>PATTERN</b><i>AI&nbsp;LABS</i></span>'
  '<span class="cover__edition">EDITION · 2026 · RETAIL &amp; QSR</span></div>'
  '<p class="cover__eyebrow">EdgeVision · Store Floors &amp; Quick-Service</p>'
  '<h1 class="cover__wordmark"><span class="w-edge">Edge</span><span class="w-vision">Vision</span>'
  '<span class="w-sub">Retail &amp; QSR</span></h1>'
  '<p class="cover__tag">Every camera, a real-time operations engine.</p>'
  '<p class="cover__sub">Intelligent AI surveillance at the edge — turning every store and restaurant camera '
  'into a real-time operations &amp; customer-intelligence engine. One on-prem edge platform across '
  'retail floors and quick-service restaurants.</p>'
  '<ul class="cover__tags"><li><svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#F52E67"/></svg> EDGE-FIRST</li><li><svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#F52E67"/></svg> PRIVACY BY DESIGN</li>'
  '<li><svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#F52E67"/></svg> INTEL POWERED</li></ul>'
  '<div class="cover__foot"><span>EDGEVISION.PRO · PATTERN AI LABS</span>'
  '<span class="cover__sigil">RETAIL<br/>&amp; QUICK-SERVICE</span></div></div></section>'.format(img=IMG,mk=mark("mark--lg")))

# 2 · Ch01 divider
S.append(divider("CHAPTER 01 · THE VISIBILITY GAP","CHAPTER 01","The Visibility Gap",
  "Modern retail and QSR sites capture thousands of hours of CCTV every week. Almost none of it becomes a decision.",
  "ev-hook.png"))

# 3 · The Challenge (retail)
copy=(eyebrow("The Challenge · Store Floor")
  +display("The In-Store<br/>Visibility Gap.","display--mid")
  +lede("Stores capture hours of CCTV every shift. But almost none of it becomes a decision.")
  +dashlist(["Staff effort & productivity is opaque — who is attending, grouping, on the phone",
             "Customer journey is invisible after entry — footfall ≠ engagement",
             "High-value customers walk in unannounced — loyalty runs blind to the first 60 seconds",
             "Floor-hygiene failures surface late — scattered footwear, disturbed displays, > 4 in back store"],"dashlist--split"))
S.append(slide("THE CHALLENGE",split(copy,"ev-hook.png","IN-STORE CCTV · UNWATCHED")))

# 4 · Ch02 divider
S.append(divider("CHAPTER 02 · THE PLATFORM","CHAPTER 02","The Platform",
  "A single edge appliance per site. Hybrid Vision + GenAI on-prem. Insights in seconds.","ev-platform.png"))

# 5 · The Solution — EdgeVision Platform
body=(eyebrow("The Solution")
  +display("EdgeVision Platform.")
  +lede("High-performance Intel edge compute on the site LAN ingests existing CCTV, runs hybrid Vision + GenAI "
        "on-prem, and produces real-time alerts, dashboards and APIs.")
  +pipeline([("01","Connect Cameras","Existing IP / CCTV via RTSP. No new wiring."),
             ("02","Process on Edge","Intel edge compute inside the site. Air-gapped & isolated."),
             ("03","Analyse & Detect","Vision + GenAI models reason over the scene."),
             ("04","Generate Insights","Alerts, KPIs, clips, dashboards, APIs, WhatsApp.")])
  +stats([("Real-time","Detection"),("Multi-cam","Per edge node"),("0<i>KB</i>","Cloud bandwidth"),("&lt;1<i>wk</i>","Deployment")]))
S.append(slide("THE SOLUTION",body))

# 6 · Operations Console
console=('<div class="console">'
  '<div><label>Snapshot</label><div class="console__stats">'
  '<div class="kv"><label>FOOTFALL</label><b>1,284</b></div>'
  '<div class="kv"><label>ACTIVE STAFF</label><b>12 / 14</b></div>'
  '<div class="kv"><label>ALERTS</label><b>3</b></div>'
  '<div class="kv"><label>AVG DWELL</label><b>4:21</b></div></div></div>'
  '<div><label>Hourly footfall</label>'
  '<div class="bars"><i style="--h:18%"></i><i style="--h:32%"></i><i style="--h:48%"></i>'
  '<i style="--h:62%"></i><i style="--h:74%"></i><i style="--h:86%"></i><i style="--h:70%"></i>'
  '<i style="--h:96%" class="hi"></i><i style="--h:78%"></i><i style="--h:58%"></i><i style="--h:42%"></i><i style="--h:28%"></i></div>'
  '<div class="bars__axis"><span>10AM</span><span>2PM</span><span>6PM</span><span>10PM</span></div></div>'
  '<div><label>Alert stream</label><ul class="alerts">'
  '<li><svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#F52E67"/></svg> VIP entered · gold tier</li>'
  '<li><svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#56565F"/></svg> Wall #3 unattended 2m</li>'
  '<li><svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#56565F"/></svg> Queue &gt; 4 at till 2</li>'
  '<li><svg class="cdot" viewBox="0 0 10 10" width="7" height="7"><circle cx="5" cy="5" r="4.5" fill="#F52E67"/></svg> Back store &gt; 4 staff</li></ul></div></div>'
  '<div class="cam-strip"><span>CAM 01</span><span>CAM 02</span><span>CAM 03</span>'
  '<span>CAM 04</span><span>CAM 05</span><span>CAM 06</span></div>')
body=(eyebrow("Live Operations Console")+display("One Pane of Glass<br/>for the Store Floor.","display--mid")+console)
S.append(slide("OPERATIONS CONSOLE",body))

# 7 · Ch03 divider
S.append(divider("CHAPTER 03 · TWO LENSES","CHAPTER 03","Two Lenses, One Network",
  "The same feeds answer two questions at once: what is the customer experiencing, and how is the team performing?",
  "ev-idea.png"))

# 8 · Customer & Staff Analytics
a=lenscard("CUSTOMER ANALYTICS","What customers do, where they linger, who they are.",
  ["Heat-mapping by entry, fixture and category","Walk-in flow between departments and categories",
   "Self-service vs assisted journey detection","VIP / loyalty member recognition at entry",
   "POS ↔ camera time-stitch for billing intelligence"])
b=lenscard("STAFF ANALYTICS","Who is attending, who is missing, who is grouping.",
  ["Peak vs non-peak presence by zone","Grouping > 1 min, mobile use, back-store time",
   "Style/size run timing — wall to back-store","Per-staff customer attention & conversion proxy",
   "Brand-level heat-map for back-store activity"],kind="check")
body=(eyebrow("Two Lenses")+display("Customer &amp; Staff Analytics.","display--mid")+twocol(a,b)
  +pull("<b>Same hardware. Same cameras. Two outcomes.</b> Intel edge compute on the store LAN — no extra installation."))
S.append(slide("TWO LENSES",body))

# 9 · Detection at Work
def _box(kind,l,t,w,h,lab):
    return ('<span class="det-box det-box--{k}" style="left:{l}%;top:{t}%;width:{w}%;height:{h}%">'
        '<span>{lab}</span></span>').format(k=kind,l=l,t=t,w=w,h=h,lab=lab)
_boxes=(_box("cust",57,32,9,63,"CUSTOMER")+_box("cust",6.8,12,6.2,46,"CUSTOMER")
  +_box("cust",15.5,4,8,34,"CUSTOMER")+_box("staff",74,7,6,40,"STAFF")+_box("staff",28.5,11,5.5,28,"STAFF"))
detfig=('<figure class="detfig"><img src="{i}/fw-uc-customers.png" alt=""/>{boxes}'
  '<span class="det-chip det-chip--cam">CAM 03 · MAIN FLOOR · LIVE</span>'
  '<span class="det-chip det-chip--rec">● REC</span>'
  '<span class="det-chip det-chip--key"><i class="sq sq--s"></i> STAFF · 2 &nbsp; <i class="sq sq--c"></i> CUSTOMERS · 3</span>'
  '<span class="det-chip det-chip--note">NO BIOMETRIC DATA RETAINED</span></figure>').format(i=IMG,boxes=_boxes)
body=(eyebrow("In-Store Detection")+display("Tracking Customers &amp; Staff Simultaneously.","display--mid")
  +lede("Every person on the floor is detected, classified and tracked — without ever storing a face.")+detfig)
S.append(slide("DETECTION AT WORK",body))

# 10 · Customer Analytics Elaborated
body=(eyebrow("Capability 01")+display("Customer Analytics, Elaborated.","display--mid")
  +circles([("Heat Mapping","By entry, fixture, category. Walk-in flow between categories becomes a measurable cross-category insight."),
            ("Customer Tracking","VIP & loyalty recognition at entrance. Auto-enroll dwell > 15 min. No biometric data leaves the store."),
            ("Self-Service vs Assisted","Identifies customers who buy without staff help — critical for VM, range planning and staffing."),
            ("POS ↔ Camera Stitch","Correlate bills with in-store trail. Every transaction becomes a journey: dwell, attended-by, time-to-bill.")],cols=4))
S.append(slide("CAPABILITY 01",body))

# 11 · Heat Mapping
heat=('<div class="heat"><figure class="heat__img"><img src="{i}/fw-heat.png" alt=""/>'
  '<span class="heat__cap">CONCEPT FLOOR · DWELL HEAT</span></figure>'
  '<div class="heat__bars"><label style="font-family:var(--mono);font-size:.62rem;letter-spacing:.22em;color:var(--text-mute);margin-bottom:14px;display:block">TOP DWELL ZONES</label>'
  +"".join('<div class="hbar"><span class="hbar__l">{l}</span><span class="hbar__v">{v}%</span>'
      '<span class="hbar__t"><i style="width:{v}%"></i></span></div>'.format(l=l,v=v) for l,v in
      [("Brand Wall",92),("Centre Table",78),("Gondola",54),("Entry",41),("Cash Desk",32)])
  +'<p class="heat__fine">Generated entirely on the in-store edge box. No cloud round-trip.</p></div></div>').format(i=IMG)
body=(eyebrow("Heat Mapping")+display("Customer Dwell, Visualised.","display--mid")+heat)
S.append(slide("HEAT MAPPING",body))

# 12 · VIP Recognition Flow
tl=""
for i,(t,h,p) in enumerate([("0.4s","Recognition","Privacy-preserving embedding match against the store-local gallery. No raw faces leave the box."),
    ("2.1s","Notification","Manager pinged via WhatsApp / app — name, tier, last visit, last basket, preferences."),
    ("3.0s","Activation","Next-best-action: assign senior associate, push targeted POS offer, trigger follow-up sequence.")],1):
    tl+=('<article class="tl-card"><header><span class="tl-card__n">{n:02d}</span>'
         '<span class="tl-card__t">{t}</span></header><h3>{h}</h3><p>{p}</p></article>').format(n=i,t=t,h=esc(h),p=esc(p))
copy=(eyebrow("VIP Recognition Flow")+display("From CCTV Frame<br/>to Manager’s Phone.","display--mid")
  +lede("A loyalty member walks in. Within 3 seconds the manager has identity, history and a recommended action — without a single cloud round-trip."))
body=split(copy,"fw-vip.png","LOYALTY · TIER-GOLD ARRIVAL")+'<div class="timeline timeline--3" style="grid-template-columns:1fr auto 1fr auto 1fr;margin-top:16px">'+ \
  tl.replace('</article><article','</article><span class="tl-arr" style="align-self:center;color:var(--brand);font-size:1.2rem">→</span><article')+'</div>'
S.append(slide("VIP RECOGNITION",body))

# 13 · Staff Analytics Elaborated
body=(eyebrow("Capability 02")+display("Staff Analytics, Elaborated.","display--mid")
  +circles([("Grouping & Inattention","Flags clusters of staff grouped > 1 minute without an active customer. Manager receives a real-time alert with clip."),
            ("Wall-Location Coverage","Detects when a staffed wall is unattended beyond threshold during peak hours. Trended hourly, store by store."),
            ("Mobile-Use Tracking","Phone use detected with thresholds (1 min floor, 2 min back store). A coaching tool, not a surveillance tool.")],cols=3))
S.append(slide("CAPABILITY 02",body))

# 14 · Hidden Loops + shift chart
shift=('<div class="shift"><label>PER-STAFF ACTIVITY · S04 · SHIFT 10–8</label>'
  '<div class="track"><span>Attended</span><div class="trackbar"><i class="seg seg--b" style="left:14%;width:14%"></i>'
  '<i class="seg seg--b" style="left:32%;width:13%"></i><i class="seg seg--b" style="left:55%;width:15%"></i>'
  '<i class="seg seg--b" style="left:74%;width:11%"></i></div></div>'
  '<div class="track"><span>Wall Station</span><div class="trackbar"><i class="seg seg--w" style="left:48%;width:10%"></i>'
  '<i class="seg seg--w" style="left:88%;width:8%"></i></div></div>'
  '<div class="track"><span>Back Store</span><div class="trackbar"><i class="seg seg--g" style="left:20%;width:7%"></i>'
  '<i class="seg seg--g" style="left:60%;width:6%"></i></div></div>'
  '<div class="track"><span>Mobile Use</span><div class="trackbar"><i class="seg seg--a" style="left:42%;width:5%"></i></div></div>'
  '<div class="track"><span>Grouping</span><div class="trackbar"><i class="seg seg--m" style="left:46%;width:5%"></i></div></div></div>')
body=(eyebrow("Capability 02 · Continued")+display("The Hidden Loops That Decide a Sale.","display--mid")
  +twocol(lenscard("STYLE / SIZE RUN-TIME","",["Time between staff leaving the brand location to look for a size and returning with stock","Measured per-brand, per-staff, per-shift"]),
          lenscard("PER-STAFF SALE CONVERSION","",["Stitching the journey to attending staff and POS bill","Yields an objective attended-conversion score"],kind="check"))
  +shift)
S.append(slide("HIDDEN LOOPS",body))

# 15 · Brand-Level Staff Heat Map
a=lenscard("FLOOR MOVEMENT MAP","",["Per-staff movement trail across the floor","Brand-zone occupancy heat by 30-min slot",
   "Hand-off detection between brand zones","Comparison: peak vs non-peak coverage"],kind="check")
b=lenscard("BACK-STORE ACTIVITY","",["Round-trips per brand per day (size hunts)","Time spent by each staff in back store",
   "Alert if > 4 staff in back store at once","End-of-day back-store occupancy report"],kind="check")
body=(eyebrow("Brand-Level Staff Heat Map")+display("Where Your Staff Actually Spend Time.","display--mid")+twocol(a,b))
S.append(slide("BRAND-LEVEL HEAT",body))

# 16 · Retail Long Tail
body=(eyebrow("More Out-of-the-Box · Retail")+display("The Long Tail of Use-Cases.","display--mid")
  +dotcards([("Floor & Display Hygiene",["Footwear out of place > 2 min triggers alert","Restore-display task auto-assigned","Daily hygiene compliance score per zone","End-of-day VM delta photos"]),
             ("Queue & Cash-Desk",["Live queue length & wait time per till","Auto-alert when queue > 4 customers","Bagging / hand-off duration tracking","Trial-room turnover & queue at fitting bay"]),
             ("Loss Prevention",["Tag-removal & concealment cues","After-hours motion in restricted zones","Unauthorised back-store entries","Door-open / cash-drawer correlation"]),
             ("Operations & Compliance",["Opening & closing procedure audit","Mannequin / dummy-presence at promo zones","Camera health & obstruction monitoring","Daily / weekly executive summary email"])]))
S.append(slide("RETAIL · LONG TAIL",body))

# 17 · QSR Edition divider
S.append(divider("QSR EDITION · FROM COUNTER TO KITCHEN","QSR EDITION","From Counter to Kitchen",
  "Quick-service restaurants run on three numbers: speed, accuracy and food safety. Every camera in the dining room, "
  "at the counter and across the kitchen already sees them. RetailTrack turns them into a live signal.","ev-qsr.png"))

# 18 · QSR Capabilities
body=(eyebrow("QSR Capabilities")+display("Speed, Accuracy,<br/>Safety — Live.","display--mid")
  +lede("Three operational levers every QSR brand tracks weekly via spreadsheets and mystery-shopper audits. "
        "EdgeVision tracks them per-shift, per-station, per-car — automatically.")
  +circles([("Speed of Service","Counter queue length, mobile-pickup dwell, kitchen-to-pass timing and time-to-first-bag — every daypart benchmarked against itself, not a corporate average."),
            ("Kitchen Choke-Points","Idle stations, expo bottleneck, fry-station coverage, grill hand-off delays — flagged the moment they exceed threshold, not after the rush has cost a guest."),
            ("Food Safety & Hygiene","Gloves, hairnets, handwash frequency, holding-time at the heat lamp, spillage detection — scene-aware checks, low false-positive, ready for the next FSSAI / health audit.")],cols=3))
S.append(slide("QSR · CAPABILITIES",body))

# QSR Long Tail
body=(eyebrow("More Out-of-the-Box · QSR")+display("Every Camera, Every Service Window.","display--mid")
  +dotcards([("Counter & Kiosk",["Queue length vs labour deployed by daypart","Self-order kiosk abandonment & completion","Greeter / smile-at-window compliance","Mobile-order pickup-bay dwell & handoff"]),
             ("Kitchen & Holding",["Station coverage per shift (grill · fry · expo)","Hot-hold & cold-hold zone compliance","Order assembly time & bagging accuracy","Wipe-down cadence between rushes"]),
             ("Cleanliness & Safety",["Dining-area spillage & tray-bus cadence","Restroom check cadence vs schedule","Slip-and-fall hazard auto-flagging","End-of-day closing-audit photo trail"]),
             ("Compliance & Audit",["PPE: gloves · hairnet · apron per station","Handwash frequency vs corporate SOP","Camera health & obstruction monitoring","Daily / weekly executive summary email"])]))
S.append(slide("QSR · LONG TAIL",body))

# 21 · Ch05 divider
S.append(divider("CHAPTER 05 · THE PARADIGM SHIFT","CHAPTER 05","The Paradigm Shift",
  "Why GenAI-powered analytics finally makes the in-store camera a primary business sensor.","ev-paradigm.png"))

# 22 · Why GenAI changes everything (table)
rows=[("Detection","Bounding boxes & pixel thresholds","Contextual scene understanding"),
      ("Accuracy","High false-positive in varying light","Adaptive to lighting & occlusions"),
      ("Self-Service","Cannot determine purchase intent","Full customer journey with billing"),
      ("Hygiene","Static detection, frequent false alerts","Scene-aware: items vs. decor"),
      ("Adaptability","Manual re-calibration per store","Self-adapting, zero retraining"),
      ("Insights","Counts and timestamps only","Rich descriptions: why, not what")]
tbody="".join('<tr><td>{d}</td><td>{a}</td><td class="cmp__hi">{b}</td></tr>'.format(d=esc(d),a=esc(a),b=esc(b)) for d,a,b in rows)
table=('<table class="cmp"><thead><tr><th>Dimension</th><th>Traditional CV</th>'
  '<th class="cmp__hi">EdgeVision GenAI</th></tr></thead><tbody>'+tbody+'</tbody></table>')
body=(eyebrow("The Paradigm Shift")+display("Why GenAI Analytics Changes Everything.","display--mid")+table
  +pull("<i>“Traditional analytics tells you someone entered the store. EdgeVision tells you they browsed for 4 minutes, "
        "showed interest in the brand wall, and left without purchasing — and which staff member was nearest.”</i>"))
S.append(slide("PARADIGM SHIFT",body))

# 23 · Hybrid Intelligence
body=(eyebrow("Hybrid Intelligence")+display("Real-Time Vision<br/>+ On-Device GenAI.","display--mid")
  +circles([("Hybrid Intelligence","Vision AI runs continuously at 15+ FPS. GenAI (VLM) is triggered only when the rule engine demands context — about 90% compute reduction."),
            ("Zero Cloud Dependency","Everything happens on Intel edge compute inside the site. No frames, no biometrics, no PII transmitted off-premise. Full data sovereignty."),
            ("Configurable Rules","Node-RED-style rule engine. Tune thresholds (e.g. ‘> 4 staff in back store’) without code changes or retraining.")],cols=3)
  +stats([("15<i>+</i>","FPS continuous Vision AI per camera"),("~90<i>%</i>","Compute reduction via VLM triggering"),("0","Frames, biometrics or PII off-premise")]))
S.append(slide("HYBRID INTELLIGENCE",body))

# 24 · Architecture
body=(eyebrow("Edge-First Architecture")+display("Built for the Store LAN.","display--mid")
  +lede("High-performance Intel edge compute on the site LAN. Reads existing CCTV via RTSP. Runs the full pipeline locally.")
  +pipeline([("STAGE 01","Store Cameras","Existing IP CCTV via RTSP"),
             ("STAGE 02","Edge Compute","Intel Core Ultra · ~100 TOPS"),
             ("STAGE 03","AI Pipeline","Vision + GenAI inference"),
             ("STAGE 04","Rule Engine","Configurable thresholds"),
             ("STAGE 05","Outputs","Dashboards · APIs · WhatsApp")])
  +'<div class="lan-bar lan-bar--wide"><span class="lan-bar__l">INSIDE SITE LAN</span>'
   '<span class="lan-bar__line"></span><span class="lan-bar__r">AIR-GAPPED · NO CLOUD</span></div>')
S.append(slide("ARCHITECTURE",body))

# 25 · Hardware & Privacy
spec=('<article class="lens"><p class="lens__head">HARDWARE · REFERENCE EDGE NODE</p>'
  '<dl class="speclist">'+"".join('<div><dt>{k}</dt><dd>{v}</dd></div>'.format(k=esc(k),v=esc(v)) for k,v in
    [("PLATFORM","Lenovo · ThinkEdge"),("PROCESSOR","Intel Core Ultra 9 285H · ~100 TOPS"),
     ("MEMORY","32 GB"),("STORAGE","1 TB NVMe"),("OS","Ubuntu 24.04 LTS"),("NETWORK","Closed LAN, isolated")])+'</dl></article>')
priv=lenscard("PRIVACY & SECURITY","",["On-prem deployment — all processing inside the site",
  "Air-gapped — no external API calls required","Role-based access (RBAC) for managers & HQ",
  "FIFO video retention with configurable policy","Tamper-resistant edge appliance","Zero biometric data leaves the device"],kind="check")
body=(eyebrow("Hardware & Privacy")+display("Intel-Powered.<br/>Privacy by Design.","display--mid")+twocol(spec,priv))
S.append(slide("HARDWARE & PRIVACY",body))

# 26 · Engagement
weeks=('<div class="weeks weeks--4" style="grid-template-columns:repeat(3,1fr)">'
  +"".join('<article class="week{f}"><span class="week__n">{wn}</span><h3>{h}</h3><p>{p}</p></article>'.format(
      f=" week--first" if i==0 else "",wn=esc(wn),h=esc(h),p=esc(p)) for i,(wn,h,p) in enumerate([
      ("WEEK 01","Audit & Install","Site survey, camera audit, RTSP setup. Intel edge compute installed on the site LAN. Baseline data collection starts."),
      ("WEEK 02","Calibrate & Tune","Zone definitions, threshold tuning per fixture, alert routing setup, custom rules wired to messaging stack."),
      ("WEEK 03","Handover & Train","Manager training, dashboard onboarding, alert rehearsal, first weekly executive insights report delivered.")]))+'</div>')
body=(eyebrow("Engagement Model")+display("From CCTV to Insights<br/>in Three Weeks.","display--mid")+weeks
  +pull("<b>What you get at end of week 3:</b> a fully running EdgeVision installation, two weeks of baseline analytics, "
        "a configured alert pipeline, and an operations team that has run a full daily cycle on the new console."))
S.append(slide("ENGAGEMENT",body))

# 27 · About
body=(eyebrow("About")+display("The Team Behind EdgeVision.","display--mid")
  +lede("Pattern AI Labs builds intelligent edge AI for enterprise operations — democratising real-time video "
        "intelligence with privacy and actionable insights in seconds.")
  +numcards([("Generative AI & CV","Multi-modal models for scene understanding, contextual reasoning and visual intelligence — tuned for enterprise edge."),
             ("Edge AI Optimisation","Inference optimised for Intel NPU + iGPU on Core Ultra series. OpenVINO toolchain. Performance & thermal-aware."),
             ("Real-Time Anomaly","Instant alerts for unusual activity, safety violations and compliance — backed by configurable rule logic."),
             ("Enterprise Integration","REST APIs, webhooks, WhatsApp, dashboard plugins. Integrates with POS, BI stack & loyalty platform.")],cols=4)
  +pull("<b style=\"color:var(--brand)\">INTEL EDGE AI PARTNER SPOTLIGHT</b> &nbsp; Featured as a leading edge-AI "
        "innovator in Intel’s exclusive partner ecosystem. Optimised on Intel hardware for real-time inference at the edge."))
S.append(slide("ABOUT",body))

# 28 · Contact / closing
S.append('<section class="slide slide--closing"><img class="slide__bg" src="{img}/ev-closing.png" alt=""/>'
  '<div class="closing__veil"></div><div class="closing__inner">'
  '<div class="closing__brand">{mk}<span class="cover__brandtxt"><b>PATTERN</b><i>AI&nbsp;LABS</i></span></div>'
  '<h2 class="closing__head">Let’s bring <span class="grad">intelligence</span><br/>to every store &amp; line.</h2>'
  '<p class="closing__sub">A focused 3-week pilot. Same cameras. New decisions. Measurable lift in customer '
  'experience, staff productivity and QSR speed-of-service.</p>'
  '<div class="contact"><a class="contact__card"><span class="contact__h">EMAIL</span><span class="contact__v">info@pattern-ai.com</span></a>'
  '<a class="contact__card"><span class="contact__h">WEB</span><span class="contact__v">www.edgevision.pro</span></a>'
  '<a class="contact__card"><span class="contact__h">PHONE</span><span class="contact__v">+91 99618 71254</span></a></div>'
  '<div class="closing__foot"><span>SAN FRANCISCO, USA &nbsp;·&nbsp; KOCHI, INDIA &nbsp;·&nbsp; REMOTE, GLOBAL</span>'
  '<span>© 2026 PATTERN AI LABS</span></div></div></section>'.format(img=IMG,mk=mark("mark--lg")))

CSS=open("/home/user/edgevision-pro/deck/deck.css").read()
doc=('<!doctype html><html lang="en"><head><meta charset="utf-8"/>'
     '<title>EdgeVision — Retail & QSR · Pattern AI Labs</title>'
     '<link rel="stylesheet" href="fonts.css"/><style>{css}</style></head><body>{sym}{slides}</body></html>').format(
     css=CSS,sym=MARK_SYMBOL,slides="".join(S))
os.makedirs(os.path.dirname(OUT),exist_ok=True)
open(OUT,"w",encoding="utf-8").write(doc)
print("Wrote",OUT,"with",_n[0],"slides")
