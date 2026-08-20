# -*- coding: utf-8 -*-
"""EdgeVision — single Pricing slide (original editorial-dark design)."""
import html, os
OUT = "/home/user/edgevision-pro/deck/EdgeVision-Pricing.html"
IMG = "../assets/images"

rects = "\n".join('<rect x="22.7" y="2.4" width="2.6" height="13.6" rx="1.3"{}/>'.format(
    "" if a==0 else ' transform="rotate({} 24 24)"'.format(a)) for a in range(0,360,15))
MARK_SYMBOL = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true">'
    '<symbol id="pat-mark" viewBox="0 0 48 48"><g fill="currentColor">'+rects+'</g></symbol></svg>')
def mark(cls=""): return '<svg class="mark {}" aria-hidden="true"><use href="#pat-mark"/></svg>'.format(cls)
def esc(s): return html.escape(s, quote=False)

chrome = ('<div class="chrome"><span class="chrome__brand">{m}<b>PATTERN</b><i>AI&nbsp;LABS</i>'
    '<span class="chrome__div">/</span><span class="chrome__prod">RETAIL&nbsp;&&nbsp;QSR</span></span>'
    '<span class="chrome__ctx">COMMERCIALS</span></div>').format(m=mark("mark--sm"))
foot = ('<div class="foot"><span>EDGEVISION · RETAIL &amp; QSR</span>'
    '<span class="foot__mid">Simple, flexible, edge-first</span><span class="foot__n">01</span></div>')

# Two pricing cards: POC and Post-POC
poc = ('<article class="price-card price-card--poc">'
  '<div class="price-card__tag">STAGE 01</div>'
  '<h3>Proof of Concept</h3>'
  '<p class="price-card__lead">We invest in the hardware and waive the fees — you try it risk-free.</p>'
  '<ul class="pricelist">'
  '<li><span class="pl__k">Per-camera usage fee</span><span class="pl__v pl__v--free">Waived</span></li>'
  '<li><span class="pl__k">Hardware cost</span><span class="pl__v pl__v--free">We invest</span></li>'
  '<li><span class="pl__k">Refundable security deposit</span><span class="pl__v">₹20,000</span></li>'
  '</ul>'
  '<p class="price-card__note">The deposit is fully refunded once the POC is approved and you decide to proceed.</p>'
  '</article>')

post = ('<article class="price-card price-card--post">'
  '<div class="price-card__tag">STAGE 02</div>'
  '<h3>Post-POC · Rollout</h3>'
  '<p class="price-card__lead">Go live across stores on a simple, predictable model.</p>'
  '<ul class="pricelist">'
  '<li><span class="pl__k">One-time hardware<br/><i>by compute for the use cases deployed</i></span>'
  '<span class="pl__v">₹1&ndash;1.5&nbsp;<em>lakh</em></span></li>'
  '<li><span class="pl__k">Ongoing software</span><span class="pl__v">₹500 <em>/ camera / month</em></span></li>'
  '</ul>'
  '<p class="price-card__note">Flexible — further negotiable on the number of stores and overall volume.</p>'
  '</article>')

privacy = ('<div class="price-privacy">'
  '<div class="price-privacy__ic">{lock}</div>'
  '<div><p class="price-privacy__h">Edge-compute architecture · private by design</p>'
  '<p class="price-privacy__p">All CCTV data stays on-premise on the edge server inside your store — '
  '<b>nothing is sent to the cloud</b> unless a specific use case requires it. Full compliance with the '
  'latest privacy regulations and data-handling standards.</p></div></div>').format(
  lock='<svg viewBox="0 0 24 24"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>')

body = ('<p class="eyebrow">Commercials</p>'
  '<h2 class="display display--mid">Simple pricing. Risk-free to start.</h2>'
  '<div class="price-grid">'+poc+post+'</div>'
  + privacy)

slide = ('<section class="slide">'+chrome+'<div class="slide__body">'+body+'</div>'+foot+'</section>')

CSS = open("/home/user/edgevision-pro/deck/deck.css").read() + """
/* ── Pricing slide ── */
.price-grid{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--border);
  border:1px solid var(--border);margin-top:12px}
.price-card{background:var(--bg);padding:22px 26px 22px;display:flex;flex-direction:column;position:relative}
.price-card--post{background:linear-gradient(180deg,rgba(245,46,103,.06),var(--bg))}
.price-card__tag{font-family:var(--mono);font-size:.58rem;letter-spacing:.24em;color:var(--text-mute);margin-bottom:12px}
.price-card--post .price-card__tag{color:var(--brand)}
.price-card h3{font-family:var(--tx);font-weight:400;font-size:1.4rem;color:#fff;margin:0 0 6px}
.price-card__lead{font-size:.82rem;line-height:1.4;color:var(--text-dim);margin:0 0 14px}
.pricelist{margin:0;padding:0;list-style:none;border-top:1px solid var(--border)}
.pricelist li{display:flex;align-items:baseline;justify-content:space-between;gap:16px;
  padding:11px 0;border-bottom:1px solid var(--border)}
.pl__k{font-size:.84rem;color:var(--text-dim);line-height:1.3}
.pl__k i{display:block;font-style:normal;font-size:.68rem;color:var(--text-mute);margin-top:2px}
.pl__v{font-family:var(--tx);font-weight:300;font-size:1.35rem;color:#fff;white-space:nowrap;text-align:right}
.pl__v em{font-style:normal;font-size:.6em;color:var(--text-dim);font-weight:300}
.pl__v--free{color:var(--brand);font-size:1.05rem;font-weight:500;letter-spacing:.02em}
.price-card__note{margin:14px 0 0;font-size:.74rem;line-height:1.4;color:var(--text-mute)}
.price-card--post .price-card__note{color:var(--text-dim)}
.price-privacy{display:flex;gap:18px;align-items:flex-start;margin-top:16px;padding:18px 22px;
  border:1px solid var(--border-2);background:var(--bg-2)}
.price-privacy__ic{width:34px;height:34px;color:var(--brand);flex:0 0 auto}
.price-privacy__ic svg{width:100%;height:100%;stroke:currentColor;fill:none;stroke-width:1.4}
.price-privacy__h{font-family:var(--tx);font-weight:600;font-size:.9rem;color:#fff;margin:0 0 4px}
.price-privacy__p{font-size:.8rem;line-height:1.45;color:var(--text-dim);margin:0;max-width:none}
.price-privacy__p b{color:#fff}
"""

doc = ('<!doctype html><html lang="en"><head><meta charset="utf-8"/><title>EdgeVision — Pricing</title>'
  '<link rel="stylesheet" href="fonts.css"/><style>{css}</style></head><body>{sym}{slide}</body></html>').format(
  css=CSS, sym=MARK_SYMBOL, slide=slide)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(doc)
print("Wrote", OUT)
