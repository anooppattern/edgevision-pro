# -*- coding: utf-8 -*-
"""Generate the EdgeVision Fabric Lens deck (16:9 print slides) in the
edgevision.pro editorial-dark design system."""
import html, os

OUT = "/home/user/edgevision-pro/deck/index.html"
IMG = "../assets/images"  # relative to deck/index.html

# ---- Pattern AI Labs 24-spoke wheel mark (from edgevision.pro) ----
rects = "\n".join(
    '<rect x="22.7" y="2.4" width="2.6" height="13.6" rx="1.3"{}/>'.format(
        "" if a == 0 else ' transform="rotate({} 24 24)"'.format(a))
    for a in range(0, 360, 15))
MARK_SYMBOL = '<svg width="0" height="0" style="position:absolute" aria-hidden="true">'\
    '<symbol id="pat-mark" viewBox="0 0 48 48"><g fill="currentColor">'+rects+'</g></symbol></svg>'

def mark(cls=""):
    return '<svg class="mark {}" aria-hidden="true"><use href="#pat-mark"/></svg>'.format(cls)

def esc(s):
    return html.escape(s, quote=False)

# ---- slide chrome ----
_slide_no = [0]
def slide(ctx, body, cls="", num=True, bg=None, veil=False):
    _slide_no[0] += 1
    n = _slide_no[0]
    bgel = ''
    if bg:
        bgel = '<img class="slide__bg" src="{}/{}" alt=""/>'.format(IMG, bg)
        if veil:
            bgel += '<div class="slide__veil"></div>'
    chrome = (
      '<div class="chrome">'
        '<span class="chrome__brand">{m}<b>PATTERN</b><i>AI&nbsp;LABS</i>'
        '<span class="chrome__div">/</span><span class="chrome__prod">FABRIC&nbsp;LENS</span></span>'
        '<span class="chrome__ctx">{ctx}</span>'
      '</div>'
    ).format(m=mark("mark--sm"), ctx=esc(ctx))
    foot = (
      '<div class="foot">'
        '<span>EDGEVISION · FABRIC LENS</span>'
        '<span class="foot__mid">The vision system that doesn’t blink</span>'
        '<span class="foot__n">{:02d}</span>'
      '</div>'
    ).format(n)
    return ('<section class="slide {cls}">{bg}{chrome}'
            '<div class="slide__body">{body}</div>{foot}</section>').format(
        cls=cls, bg=bgel, chrome=chrome, body=body, foot=foot)

def eyebrow(t):
    return '<p class="eyebrow">{}</p>'.format(esc(t))

def display(t, cls=""):
    return '<h2 class="display {}">{}</h2>'.format(cls, t)  # t may contain markup

def lede(t):
    return '<p class="lede">{}</p>'.format(t)

def numcards(items, cols=4, brand=False):
    bc = " num-card--brand" if brand else ""
    cells = ""
    for i, it in enumerate(items, 1):
        if len(it) == 3:
            n, h, p = it
        else:
            n, h, p = "{:02d}".format(i), it[0], it[1]
        cells += ('<article class="num-card{bc}"><span class="num-card__n">{n}</span>'
                  '<h3>{h}</h3><p>{p}</p></article>').format(bc=bc, n=esc(n), h=esc(h), p=p)
    return '<div class="num-grid num-grid--{c}">{cells}</div>'.format(c=cols, cells=cells)

def costcards(items):
    cells = ""
    for i, (h, p, tags) in enumerate(items, 1):
        chips = "".join('<span class="chip">{}</span>'.format(esc(t)) for t in tags)
        cells += ('<article class="num-card num-card--cost"><span class="num-card__n">{n:02d}</span>'
                  '<h3>{h}</h3><p>{p}</p><div class="chips">{chips}</div></article>').format(
            n=i, h=esc(h), p=esc(p), chips=chips)
    return '<div class="num-grid num-grid--4">{}</div>'.format(cells)

def circles(items, cols=3, icon=False):
    cells = ""
    for i, (h, p) in enumerate(items, 1):
        cells += ('<article class="circ"><span class="circ__n">{n}</span>'
                  '<h3>{h}</h3><p>{p}</p></article>').format(n=i, h=esc(h), p=p)
    return '<div class="circle-grid circle-grid--{c}">{cells}</div>'.format(c=cols, cells=cells)

def pipeline(steps):
    parts = []
    for i, (h, p) in enumerate(steps, 1):
        parts.append('<div class="pipe-card"><span class="pipe-card__n">{:02d}</span>'
                     '<h3>{}</h3><p>{}</p></div>'.format(i, esc(h), esc(p)))
    joined = '<span class="pipe-arrow">→</span>'.join(parts)
    return '<div class="pipeline pipeline--{}">{}</div>'.format(len(steps), joined)

def stats(items):
    cells = ""
    for big, sub in items:
        cells += '<div><b>{}</b><span>{}</span></div>'.format(big, esc(sub))
    return '<div class="stats stats--{}">{}</div>'.format(len(items), cells)

def lenscard(head, title, bullets, kind="dash"):
    lis = "".join('<li>{}</li>'.format(esc(b)) for b in bullets)
    ul = '<ul class="{}">{}</ul>'.format("dashlist" if kind == "dash" else "checklist", lis)
    t = '<h3>{}</h3>'.format(esc(title)) if title else ""
    return '<article class="lens"><p class="lens__head">{}</p>{}{}</article>'.format(esc(head), t, ul)

def twocol(a, b):
    return '<div class="two-col">{}{}</div>'.format(a, b)

def pull(t):
    return '<p class="pullquote"><span class="pullquote__bar"></span><span>{}</span></p>'.format(t)

def split(copy, media_img, media_cap=None):
    cap = '<span class="mediacap">{}</span>'.format(esc(media_cap)) if media_cap else ""
    return ('<div class="split"><div class="split__copy">{copy}</div>'
            '<div class="split__media"><img src="{img}/{m}" alt=""/>{cap}</div></div>').format(
        copy=copy, img=IMG, m=media_img, cap=cap)

S = []

# ───────────────────────── 1 · COVER ─────────────────────────
S.append(
  '<section class="slide slide--cover">'
  '<img class="slide__bg" src="{img}/qsr-counter.png" alt=""/>'
  '<div class="cover__veil"></div>'
  '<div class="cover__inner">'
    '<div class="cover__top">{mk}<span class="cover__brandtxt"><b>PATTERN</b><i>AI&nbsp;LABS</i></span>'
      '<span class="cover__edition">EDITION · 2026 · FOR QSR</span></div>'
    '<p class="cover__eyebrow">Introducing · EdgeVision × Fabric&nbsp;Lens</p>'
    '<h1 class="cover__wordmark"><span class="w-edge">Edge</span><span class="w-vision">Vision</span>'
      '<span class="w-sub">Fabric Lens</span></h1>'
    '<p class="cover__tag">The vision system that doesn’t blink.</p>'
    '<p class="cover__sub">Custom-installed computer vision for quick-service restaurants — '
      'purpose-built cameras, on-site edge compute, and real-time intervention at the stations you '
      'choose. Machine oversight that is more accurate, more consistent, and never looks away.</p>'
    '<ul class="cover__tags"><li><i></i> EDGE-FIRST</li><li><i></i> PRIVACY BY DESIGN</li>'
      '<li><i></i> REAL-TIME INTERVENTION</li></ul>'
    '<div class="cover__foot"><span>EDGEVISION.PRO · PATTERN AI LABS</span>'
      '<span class="cover__sigil">RETAIL · QSR<br/>&amp; DELIVERY HUBS</span></div>'
  '</div></section>'
.format(img=IMG, mk=mark("mark--lg")))

# ───────────────────────── 2 · POSITIONING ─────────────────────────
body = (eyebrow("The Platform · The Lens")
    + display("One edge platform.<br/>One QSR vision lens.")
    + lede("EdgeVision is Pattern AI Labs’ on-prem Vision&nbsp;+&nbsp;GenAI edge runtime. "
           "<b>Fabric&nbsp;Lens</b> is the quick-service-restaurant product built on it — "
           "purpose-built industrial cameras, an on-site edge appliance, and signal fusion with the "
           "equipment already on your line. Start with one station, scale at your pace.")
    + stats([("&lt;300<i>ms</i>", "Inference latency · on-site"),
             ("Modular", "One station or all"),
             ("24/7", "Continuous watch"),
             ("Real-time", "Drift caught before handoff")]))
S.append(slide("POSITIONING", body))

# ───────────────────────── 3 · PROBLEM ─────────────────────────
plist = '<ul class="dashlist dashlist--split">' + "".join(
    '<li><b>{h}</b> — {p}</li>'.format(h=esc(h), p=esc(p)) for h, p in [
      ("Attention fatigues", "human attention degrades within minutes; drift worsens as the shift wears on"),
      ("Coverage is partial", "even the best line lead watches one station at a time — the rest run unobserved"),
      ("Events are fast", "an assembly sequence takes seconds; a missing item a fraction of that — eye-blink fast"),
      ("Audits are backward", "camera review happens after a complaint, by which point the cost has compounded"),
    ]) + '</ul>'
copy = (eyebrow("The Visibility Gap")
    + display("Humans can’t be<br/>every station,<br/>every second.", "display--mid")
    + lede("A QSR runs 8–12 stations across cook, prep, assembly and pass. A shift produces hundreds "
           "of orders, each carrying 15–30 quality and accuracy checkpoints. The math does not work "
           "for human oversight.")
    + plist)
body = split(copy, "challenge-cctv.png", "IN-STORE CCTV · UNWATCHED")
S.append(slide("PROBLEM · CHAPTER 01", body))

# ───────────────────────── 4 · COMPOUNDING COST ─────────────────────────
body = (eyebrow("The Compounding Cost")
    + display("Every miss has a<br/>compounding cost.")
    + lede("The moments that drive refunds, NPS damage, complaints and brand erosion. None are visible "
           "in real time today. All can be detected and resolved in real time by Fabric&nbsp;Lens.")
    + costcards([
        ("Burger count missed", "A double leaves the line as a single. The operator never sees it.",
         ["Refund", "Brand trust", "Social complaint"]),
        ("Wrong sauce portioned", "The order spec says one sauce, a different one gets boxed.",
         ["Customer return", "Order remake", "Ticket time"]),
        ("Modifier ignored", "Cheese on a no-cheese order. Allergen risk on the wrong customer.",
         ["Allergen risk", "Refund", "Health complaint"]),
        ("Fry cook drift", "Fryer recovers slow on a rush. Pale fries reach the bag.",
         ["NPS drop", "Repeat-rate decline", "Review damage"]),
      ]))
S.append(slide("PROBLEM · THE COST", body))

# ───────────────────────── 5 · SOLUTION ─────────────────────────
copy = (eyebrow("The Product")
    + display("A vision system<br/>that intervenes.")
    + lede("Fabric&nbsp;Lens is a modular, custom-installed computer-vision platform for QSRs. "
           "Industrial cameras at the stations you choose to instrument, an on-site edge appliance, "
           "and signal fusion with the equipment already on your line. Start with one station, scale "
           "at your pace."))
body = (split(copy, "nuc-device.png", "EDGE APPLIANCE · ONE PER STORE")
    + '<div class="split--after">' + pipeline([
        ("Capture", "Cameras at your priority stations"),
        ("Detect", "Task-specific models analyse every frame"),
        ("Decide", "Rules and fusion logic evaluate the scene"),
        ("Act", "Operator alerted at the station, in real time"),
      ]) + '</div>')
S.append(slide("SOLUTION · THE PRODUCT", body))

# ───────────────────────── 6 · INTERVENTION LOOP ─────────────────────────
tl = ""
for i, (t, h, p) in enumerate([
    ("14:32:08", "Detect", "Drift identified"),
    ("14:32:08", "Decide", "Rules evaluated"),
    ("14:32:09", "Alert", "Operator notified"),
    ("14:32:14", "Verify", "Corrected in frame"),
    ("14:32:14", "Audit", "Logged for BI"),
  ], 1):
    tl += ('<article class="tl-card"><header><span class="tl-card__n">{n:02d}</span>'
           '<span class="tl-card__t">{t}</span></header><h3>{h}</h3><p>{p}</p></article>').format(
        n=i, t=t, h=esc(h), p=esc(p))
tlwrap = '<div class="timeline timeline--5">{}</div>'.format(tl)
body = (eyebrow("The Intervention Loop")
    + display("Detection is the start.<br/>Intervention is the point.")
    + lede("Real-time computer vision is only as valuable as the action it triggers. Fabric&nbsp;Lens "
           "closes the loop: every detected drift becomes an alert, an intervention, and an audit entry.")
    + tlwrap
    + pull("<b>Example · missing-sauce intervention.</b> 14:32:08 — order #4271 boxed; vision "
           "detects entrée and fries but no sauce cup, KDS calls for one. 14:32:09 — alert fires "
           "to the assembly screen, audio chime at pass. 14:32:14 — sauce added, re-verified, order "
           "released, event logged."))
S.append(slide("SOLUTION · THE LOOP", body))

# ───────────────────────── 7 · TECH OVERVIEW ─────────────────────────
body = (eyebrow("How It Works")
    + display("Five techniques.<br/>One vision system.")
    + lede("A real CV product is not one model. It is a stack: detection finds what is there, "
           "classification judges if it is right, action recognition reads the sequence, tracking "
           "holds identity through occlusion, and fusion correlates all of it with equipment and order data.")
    + '<div class="circle-grid circle-grid--5">' + "".join(
        '<article class="circ"><span class="circ__n">{n}</span><h3>{h}</h3><p>{p}</p></article>'.format(
            n=i, h=esc(h), p=p) for i, (h, p) in enumerate([
          ("Object Detection", "Finds and locates. Class, confidence, box, centroid."),
          ("Classification", "Judges every item. Is it actually right?"),
          ("Action Recognition", "Reads the sequence. Was the step done?"),
          ("Tracking + Re-ID", "Holds identity across stations and occlusion."),
          ("Signal Fusion", "Correlates vision with equipment and KDS."),
        ], 1)) + '</div>')
S.append(slide("TECH · CHAPTER 02", body))

# ───────────────────────── 8 · DETECTION + CLASSIFICATION ─────────────────────────
a = lenscard("01 · OBJECT DETECTION", "Detection finds it.", [
    "Class label — one of the trained menu classes",
    "Confidence score — below threshold, the detection is suppressed",
    "Bounding box — the tightest rectangle that contains the object",
    "Centroid + scale — feeds tracking, counting and placement checks",
  ])
b = lenscard("02 · CLASSIFICATION", "Classification judges it.", [
    "Fine-grained, pixel-level quality assessment",
    "Answers the harder question: is the item right?",
    "Where a bounding box alone is not enough",
    "Catches the one item that fails (e.g. chickpeas fill 0.62 · LOW)",
  ], kind="check")
body = (eyebrow("Tech 01–02 · Perception")
    + display("Detection finds it.<br/>Classification judges it.")
    + twocol(a, b)
    + pull("<b>A box says something is there.</b> Classification says exactly what — and exactly "
           "whether it is right."))
S.append(slide("TECH · PERCEPTION", body))

# ───────────────────────── 9 · ACTION + TRACKING ─────────────────────────
a = lenscard("03 · ACTION RECOGNITION", "Questions that only exist over time.", [
    "A single frame cannot confirm a build sequence or a hygiene step",
    "Reads a sequence of frames, building confidence as motion completes",
    "Confidence ramps 0.12 → 0.97 as ‘cheeseburger assembled’ resolves",
    "Confirms the step actually happened, not just that items are present",
  ])
b = lenscard("04 · TRACKING + RE-ID", "One order, followed end to end.", [
    "Persistent identity on an order across stations and through occlusion",
    "Re-acquires the same order after it is briefly hidden",
    "ByteTrack and DeepSORT re-identification",
    "Enables true ticket-time decomposition — where the time was spent",
  ], kind="check")
body = (eyebrow("Tech 03–04 · Time & Identity")
    + display("Some quality questions<br/>only exist over time.")
    + twocol(a, b)
    + pull("<b>Not just how long an order took — where it lost the time.</b> Tracking plus KDS "
           "timestamps turn ‘six minutes’ into ‘ninety seconds lost at assembly.’"))
S.append(slide("TECH · TIME & IDENTITY", body))

# ───────────────────────── 10 · SIGNAL FUSION ─────────────────────────
fusion = '<div class="fusion">' + "".join(
    '<article class="fusion__card"><p class="fusion__h">{h}</p><p class="fusion__p">{p}</p></article>'.format(
        h=esc(h), p=esc(p)) for h, p in [
      ("VISION", "Detection, classification, action recognition, tracking"),
      ("EQUIPMENT TELEMETRY", "Fryer temp, cook timers, holding-cabinet state, weight sensors"),
      ("KDS + POS", "Order content, modifiers, timestamps, bump events"),
    ]) + '<div class="fusion__core"><span>SIGNAL FUSION CORE</span><i>Frame-synced correlation across all three layers</i></div></div>'
body = (eyebrow("Tech 05 · The Moat")
    + display("Vision + sensors + KDS.<br/>The layer no one else has.")
    + lede("Three input streams correlated frame by frame inside a single fusion core. It catches what "
           "one signal alone misses, separates equipment fault from human error, and confirms rather "
           "than merely detects.")
    + fusion
    + pull("<b>Fusion in one line.</b> The fryer reports done-at-temp. Vision reports the product is "
           "under-colored. Neither signal alone catches it — together they say the equipment is "
           "drifting, not the cook."))
S.append(slide("TECH · SIGNAL FUSION", body))

# ───────────────────────── 11 · CUSTOM MODELS LIFECYCLE ─────────────────────────
body = (eyebrow("Custom Models")
    + display("Data to deployment,<br/>then it never stops.")
    + lede("Every custom model moves through the same six-stage lifecycle. The first pass produces a "
           "working model; the loop keeps it accurate as your menu, lighting and seasons change.")
    + pipeline([
        ("Capture", "Footage from your stations under real conditions"),
        ("Annotate", "Label items, regions and actions to your spec"),
        ("Train", "Fine-tune the task-specific model"),
        ("Evaluate", "Test on held-out footage; tune precision & recall"),
        ("Deploy", "Push to the edge appliance, run live"),
        ("Monitor", "Track drift, surface edge cases, feed back"),
      ])
    + '<div class="lan-bar"><span class="lan-bar__l">CONTINUOUS FEEDBACK LOOP</span>'
      '<span class="lan-bar__line"></span>'
      '<span class="lan-bar__r">EDGE CASES FROM MONITOR → BACK INTO CAPTURE</span></div>')
S.append(slide("TECH · MODEL LIFECYCLE", body))

# ───────────────────────── 12 · WHAT YOU CAN MEASURE ─────────────────────────
body = (eyebrow("What You Can Measure")
    + display("Six categories.<br/>Every one tied to the P&amp;L.")
    + lede("Built from the way a multi-unit operator actually thinks. Each category ties to a revenue "
           "line or a brand-risk line, measured continuously through the fusion of video and equipment data.")
    + '<div class="num-grid num-grid--3 num-grid--rows2">' + "".join(
        '<article class="num-card num-card--brand"><span class="num-card__n">{n:02d}</span>'
        '<h3>{h}</h3><p>{p}</p></article>'.format(n=i, h=esc(h), p=esc(p)) for i, (h, p) in enumerate([
          ("Order Accuracy", "Perfect-order rate, item-level error, count accuracy, modifier compliance, condiment attach, packaging accuracy."),
          ("Food Quality & Consistency", "Cook doneness, cook-time conformance, temp at handoff, hold-time compliance, portion & build consistency."),
          ("Speed & Throughput", "Ticket time by station, station dwell, cook recovery, drive-thru time, throughput per labor hour, SLA breach."),
          ("Food Safety & Compliance", "Danger-zone events, hold-time violations, handwash compliance, cross-contamination risk, HACCP checkpoints."),
          ("Equipment Health & Calibration", "Calibration drift, oil quality & fryer health, recovery-time degradation, holding-cabinet conformance, sensor faults."),
          ("Labor & Waste Efficiency", "Staffing vs demand, throughput per labor hour, SOP adherence, overproduction waste, remake and refire rate."),
        ], 1)) + '</div>')
S.append(slide("VALUE · MEASUREMENT", body))

# ───────────────────────── 13 · FUSION ADVANTAGE KPIs ─────────────────────────
kpi = '<div class="num-grid num-grid--5">' + "".join(
    '<article class="num-card"><span class="num-card__n">{n:02d}</span><h3>{h}</h3><p>{p}</p></article>'.format(
        n=i, h=esc(h), p=esc(p)) for i, (h, p) in enumerate([
      ("Calibration drift", "Fryer reports done-at-temp; vision reports under-colored. The equipment is the problem, not the cook."),
      ("True ticket-time decomposition", "Not ‘the order took six minutes’ but ‘it lost ninety seconds at assembly.’"),
      ("Sensor-fault detection", "Holding cabinet reports a full pan; vision sees it empty. The sensor needs service — flagged."),
      ("Root-cause quality", "Oil TPM rising, product color darkening in step. The fries are worse because the oil is spent."),
      ("Predictive SLA breach", "Queue depth and per-station throughput forecast a ticket-time miss 60–90s before it happens."),
    ], 1)) + '</div>'
body = (eyebrow("The Fusion Advantage")
    + display("The KPIs that<br/>only exist with fusion.")
    + lede("These five do not exist in a camera-only system or an equipment-only system. They require "
           "video and equipment data cross-referenced, frame by frame — the reason signal fusion is the moat.")
    + kpi
    + pull("<b>The moat.</b> Competitors with cameras can copy detection. They cannot copy what they "
           "have not instrumented: the equipment signal layer underneath."))
S.append(slide("VALUE · THE MOAT", body))

# ───────────────────────── 14 · QSR USE CASES ─────────────────────────
qlist = ('<p class="minihead">Speed of Service</p>'
    '<ul class="dashlist dashlist--split"><li>Drive-thru wait per lane, counter queue length, mobile-pickup dwell, time-to-first-bag — benchmarked per daypart against itself</li></ul>'
    '<p class="minihead">Kitchen Choke-Points</p>'
    '<ul class="dashlist dashlist--split"><li>Idle stations, expo bottleneck, fry-station coverage, grill hand-off delays — flagged the moment they exceed threshold</li></ul>'
    '<p class="minihead">Food Safety &amp; Hygiene</p>'
    '<ul class="dashlist dashlist--split"><li>Gloves, hairnets, handwash frequency, holding-time at the heat lamp, spillage — scene-aware, low false-positive, audit-ready</li></ul>')
copy = (eyebrow("Use Cases · QSR")
    + display("Speed, Accuracy,<br/>Safety — Live.", "display--mid")
    + lede("Three operational levers every QSR brand tracks weekly via spreadsheets and "
           "mystery-shopper audits. Fabric&nbsp;Lens tracks them per-shift, per-station, per-car "
           "— automatically.")
    + qlist)
body = split(copy, "qsr-counter.png", "QSR LINE · COOK → PASS · LIVE")
S.append(slide("USE CASES · QSR", body))

# ───────────────────────── 15 · DRIVE-THRU + LONG TAIL ─────────────────────────
copy = (eyebrow("Use Cases · Every Service Window")
    + display("Every lane. Every car.<br/>Every second.", "display--mid")
    + '<ul class="dashlist dashlist--tight">' + "".join('<li>{}</li>'.format(esc(x)) for x in [
        "Live per-lane queue length & wait time",
        "Order-board → handoff-window timing per car",
        "Pull-forward, blocked-lane & ‘driver not served’ alerts",
        "Lane-utilisation balance during peak hours",
        "Daypart vs forecast adherence",
      ]) + '</ul>')
body = (split(copy, "qsr-drivethru.png", "DRIVE-THRU · LANE TIMING · LIVE")
    + numcards([
        ("Counter & Kiosk", "Queue vs labour by daypart · kiosk abandonment · greeter compliance · mobile-order handoff"),
        ("Kitchen & Holding", "Station coverage per shift · hot/cold-hold compliance · assembly time · wipe-down cadence"),
        ("Cleanliness & Safety", "Dining spillage & tray-bus cadence · restroom checks · slip-and-fall flagging · closing audit trail"),
        ("Compliance & Audit", "PPE per station · handwash vs SOP · camera-health monitoring · executive summary email"),
      ], cols=4, brand=True))
S.append(slide("USE CASES · DRIVE-THRU", body))

# ───────────────────────── 16 · RETAIL STORE-FLOOR LENS ─────────────────────────
rlist = ('<p class="minihead">Customer Analytics</p>'
    '<ul class="dashlist dashlist--split">'
    '<li>Heat-mapping by entry, fixture &amp; category; walk-in flow between zones</li>'
    '<li>Self-service vs assisted journey; VIP recognition at entry — no biometrics off-device</li>'
    '<li>POS ↔ camera time-stitch for billing intelligence</li></ul>'
    '<p class="minihead">Staff Analytics</p>'
    '<ul class="dashlist dashlist--split">'
    '<li>Presence by zone, grouping &amp; inattention, mobile-use, back-store time</li>'
    '<li>Style/size run timing — wall to back-store; per-staff attention &amp; conversion proxy</li>'
    '<li>Brand-level heat-map for back-store activity</li></ul>')
copy = (eyebrow("Use Cases · Store Floor · Retail")
    + display("Two lenses,<br/>one network.", "display--mid")
    + lede("Fabric&nbsp;Lens runs on the same EdgeVision platform as RetailTrack. The same feeds "
           "answer two questions at once: what is the customer experiencing, and how is the team "
           "performing?")
    + rlist)
body = (split(copy, "two-lenses.png", "STORE FLOOR · CUSTOMER + STAFF")
    + pull("<b>Same hardware. Same cameras. Two outcomes.</b> Intel edge compute on the store LAN "
           "— no extra installation."))
S.append(slide("USE CASES · RETAIL", body))

# ───────────────────────── 17 · ARCHITECTURE ─────────────────────────
zones = '<div class="zones">' + "".join(
    '<article class="zone"><span class="zone__n">{n}</span><p class="zone__h">{h}</p>'
    '<p class="zone__s">{s}</p><ul>{items}</ul></article>'.format(
        n=n, h=esc(h), s=esc(s), items="".join('<li>{}</li>'.format(esc(x)) for x in items))
    for n, h, s, items in [
      ("01", "On-premise", "Custom install per store", [
        "Fryer cam + temp probe", "Cook line profile + top vision",
        "Assembly top-down + weight sensor", "Pass / handoff + KDS feed"]),
      ("02", "Edge appliance · Lens", "One per restaurant", [
        "Stream ingest + detection models", "Tracking + Re-ID",
        "Sensor fusion + rules engine", "Event generator · Intel Core Ultra ~100 TOPS"]),
      ("03", "AWS cloud", "Managed services", [
        "Model training · SageMaker", "Foundation models · Bedrock",
        "Event bus · EventBridge + IoT Core", "Storage · S3 + Timestream"]),
    ]) + '</div>'
body = (eyebrow("Product Architecture")
    + display("Cameras, compute, sensors — edge-first, cloud-managed.", "display--mid")
    + lede("Three zones: a custom install in the restaurant, one edge appliance running vision and "
           "fusion locally, and AWS-native managed services for training, fleet management and reporting.")
    + zones
    + stats([("259<i>ms</i>", "Inference p50"), ("4–16", "4K · 30 FPS streams"),
             ("ZERO", "Cloud round-trip in detect path"), ("us-east-1", "Multi-AZ")]))
S.append(slide("PLATFORM · ARCHITECTURE", body))

# ───────────────────────── 18 · HARDWARE + PRIVACY ─────────────────────────
spec = ('<article class="lens"><p class="lens__head">HARDWARE · REFERENCE EDGE NODE</p>'
        '<dl class="speclist">' + "".join(
    '<div><dt>{k}</dt><dd>{v}</dd></div>'.format(k=esc(k), v=esc(v)) for k, v in [
      ("PLATFORM", "ASUS NUC15CRSU9"), ("PROCESSOR", "Intel Core Ultra 9 285H · ~100 TOPS"),
      ("MEMORY", "32 GB"), ("STORAGE", "1 TB NVMe"),
      ("OS", "Ubuntu 24.04 LTS"), ("NETWORK", "Closed LAN, isolated"),
    ]) + '</dl></article>')
priv = lenscard("PRIVACY & SECURITY", "", [
    "On-prem inference — detection & fusion run inside the site",
    "No frames or biometrics leave in the detection path",
    "Role-based access (RBAC) for managers & HQ",
    "FIFO video retention with configurable policy",
    "Tamper-resistant edge appliance",
    "Zero cloud round-trip for real-time alerts",
  ], kind="check")
body = (eyebrow("Hardware & Privacy")
    + display("Intel-powered.<br/>Privacy by design.")
    + lede("High-performance Intel edge compute on the site LAN reads existing and purpose-built "
           "cameras, and runs the full detection-and-fusion pipeline locally. The cloud is for "
           "training and fleet management — never the real-time detection path.")
    + twocol(spec, priv))
S.append(slide("PLATFORM · HARDWARE", body))

# ───────────────────────── 19 · PARADIGM SHIFT ─────────────────────────
rows = [
    ("Detection", "Bounding boxes & pixel thresholds", "Contextual scene understanding"),
    ("Accuracy", "High false-positive in varying light", "Adaptive to lighting & occlusion"),
    ("Quality", "Cannot judge if the item is right", "Fine-grained, pixel-level classification"),
    ("Root cause", "Counts and timestamps only", "Fusion separates equipment from human error"),
    ("Adaptability", "Manual re-calibration per store", "Continuous-learning custom models"),
    ("Insights", "Tells you what happened", "Tells you why — and intervenes in real time"),
]
tbody = "".join('<tr><td>{d}</td><td>{a}</td><td class="cmp__hi">{b}</td></tr>'.format(
    d=esc(d), a=esc(a), b=esc(b)) for d, a, b in rows)
table = ('<table class="cmp"><thead><tr><th>Dimension</th><th>Traditional CV</th>'
         '<th class="cmp__hi">EdgeVision Fabric Lens</th></tr></thead><tbody>'+tbody+'</tbody></table>')
body = (eyebrow("The Paradigm Shift")
    + display("Why fusion + GenAI<br/>changes everything.", "display--mid")
    + table
    + pull("<i>“Traditional analytics tells you an order left the line. Fabric&nbsp;Lens tells you "
           "the double left as a single, the sauce cup was missing, and the fryer — not the cook "
           "— was drifting.”</i>"))
S.append(slide("WHY · PARADIGM SHIFT", body))

# ───────────────────────── 20 · PRODUCTION LINEAGE ─────────────────────────
lin = '<div class="num-grid num-grid--3">' + "".join(
    '<article class="num-card"><span class="num-card__n">{n:02d}</span><h3>{h}</h3><p>{p}</p>'
    '<div class="chips chips--stat">{chips}</div></article>'.format(
        n=i, h=esc(h), p=esc(p), chips="".join('<span class="chip chip--stat">{}</span>'.format(esc(c)) for c in cc))
    for i, (h, p, cc) in enumerate([
      ("BigBasket Fresho", "Custom vision models for produce quality and self-checkout. Retrained per category, in production at scale.", ["800+ SKUs live", "<300ms inference"]),
      ("Wonder · QSR", "Quality and consistency analytics purpose-built for a multi-unit QSR operator. Vision plus operational signal.", ["Multi-unit", "QSR domain"]),
      ("Pattern AI · EdgeVision", "Edge-first computer vision with on-site inference and real-time event generation — the architectural lineage for Lens.", ["Edge-first", "Real-time events"]),
    ], 1)) + '</div>'
body = (eyebrow("Production Lineage")
    + display("This team has shipped<br/>production CV before.")
    + lede("Fabric&nbsp;Lens is not a first attempt. The custom-model approach, the edge architecture "
           "and the QSR domain work all trace to production deployments the team has built and run.")
    + lin)
S.append(slide("PROOF · LINEAGE", body))

# ───────────────────────── 21 · ENGAGEMENT ─────────────────────────
weeks = '<div class="weeks weeks--4">' + "".join(
    '<article class="week{first}"><span class="week__n">{ph}</span><span class="week__wk">{wk}</span>'
    '<h3>{h}</h3><p>{p}</p></article>'.format(
        first=" week--first" if i == 0 else "", ph=esc(ph), wk=esc(wk), h=esc(h), p=esc(p))
    for i, (ph, wk, h, p) in enumerate([
      ("PHASE 00", "Week 0–1", "Discovery", "Camera audit, station prioritisation, AWS architecture review, pilot-store selection."),
      ("PHASE 01", "Week 2–6", "Install + pilot", "Custom camera install, edge appliance, first signature model, UAT on the pilot station."),
      ("PHASE 02", "Week 7–14", "Hardening", "Additional models, sensor fusion, dashboard tuning, multi-store readiness."),
      ("PHASE 03", "Week 15+", "Chain rollout", "Zero-touch provisioning, per-store onboarding, continuous model expansion."),
    ]))+ '</div>'
body = (eyebrow("Engagement")
    + display("Pilot to production.<br/>Then chain rollout.")
    + lede("Custom install means a structured roadmap. Each phase has clear outputs and acceptance "
           "criteria; pricing is tiered by chain size to support both pilot economics and scale economics.")
    + weeks
    + pull("<b>What you get at the end of the pilot:</b> a running Fabric&nbsp;Lens install on your "
           "priority stations, a first signature model on your own footage, a live intervention loop, "
           "and a dashboard your operators have run a full daily cycle on."))
S.append(slide("ENGAGEMENT · ROADMAP", body))

# ───────────────────────── 22 · CLOSING ─────────────────────────
S.append(
  '<section class="slide slide--closing">'
  '<img class="slide__bg" src="{img}/paradigm.png" alt=""/>'
  '<div class="closing__veil"></div>'
  '<div class="closing__inner">'
    '<div class="closing__brand">{mk}<span class="cover__brandtxt"><b>PATTERN</b><i>AI&nbsp;LABS</i></span></div>'
    '<h2 class="closing__head">See every station.<br/>Catch every drift.<br/>'
      '<span class="grad">Intervene in real time.</span></h2>'
    '<p class="closing__sub">Production-grade computer vision for QSR operations. Custom models, '
      'custom-installed, edge-first. Methodology you can audit, KPIs you can run the business on.</p>'
    '<div class="contact">'
      '<a class="contact__card"><span class="contact__h">EMAIL</span><span class="contact__v">info@pattern-ai.com</span></a>'
      '<a class="contact__card"><span class="contact__h">WEB</span><span class="contact__v">www.edgevision.pro</span></a>'
      '<a class="contact__card"><span class="contact__h">PHONE</span><span class="contact__v">+91 99618 71254</span></a>'
    '</div>'
    '<div class="closing__foot"><span>SAN FRANCISCO, USA &nbsp;·&nbsp; KOCHI, INDIA &nbsp;·&nbsp; REMOTE, GLOBAL</span>'
      '<span>© 2026 PATTERN AI LABS</span></div>'
  '</div></section>'
.format(img=IMG, mk=mark("mark--lg")))

# ───────────────────────── assemble ─────────────────────────
CSS = open("/home/user/edgevision-pro/deck/deck.css").read()  # written separately
doc = ('<!doctype html><html lang="en"><head><meta charset="utf-8"/>'
       '<title>EdgeVision Fabric Lens — Pattern AI Labs</title>'
       '<link rel="stylesheet" href="fonts.css"/>'
       '<style>{css}</style></head><body>{sym}{slides}</body></html>').format(
    css=CSS, sym=MARK_SYMBOL, slides="".join(S))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(doc)
print("Wrote", OUT, "with", _slide_no[0] + 2, "slides (", len(S), "sections )")
