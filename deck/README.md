# EdgeVision Fabric Lens — Deck

Sales/overview deck for **EdgeVision Fabric Lens** by **Pattern AI Labs** — a
custom-installed computer-vision system for quick-service restaurants (QSR),
built on the EdgeVision edge platform.

**Deliverable:** [`EdgeVision-Fabric-Lens.pdf`](./EdgeVision-Fabric-Lens.pdf) — 22 slides, 16:9.

## What it combines

- **Fabrick Lens** (`fabrick.co/lens`) — the QSR vision product: the visibility gap,
  the compounding cost, the intervention loop, the five-technique CV stack
  (detection · classification · action recognition · tracking + re-ID · signal
  fusion), the six P&L-tied measurement categories, the fusion-only KPIs, the
  three-zone architecture, production lineage, and the pilot→rollout engagement model.
- **EdgeVision · RetailTrack** (`edgevision.pro`) — the Retail + QSR use cases:
  speed-of-service, drive-thru, kitchen choke-points, food safety, and the
  customer/staff "two lenses" store-floor material, plus the Intel edge hardware
  and privacy-by-design story.

## Design system

Mirrors **edgevision.pro**: editorial dark theme (`#000`), magenta accent
`#F52E67`, Inter (200/300/400/500/600) display type, JetBrains Mono labels,
numbered cards, pipelines, giant stat numbers, and pull-quotes. The 24-spoke
Pattern AI Labs wheel mark is rendered inline as SVG.

## Files

| File | Purpose |
|------|---------|
| `EdgeVision-Fabric-Lens.pdf` | The rendered deck (final deliverable) |
| `index.html` | Slide source (self-contained: embedded fonts + relative `../assets/images`) |
| `deck.css` | The design-system stylesheet |
| `fonts.css` | Inter + JetBrains Mono, base64-embedded (`@font-face`) |
| `build_deck.py` | Generator that emits `index.html` |
| `render.js` | Playwright/Chromium script that prints `index.html` → PDF (1280×720 pages) |

## Rebuild

```bash
python3 deck/build_deck.py        # regenerate deck/index.html
node deck/render.js               # print to deck/EdgeVision-Fabric-Lens.pdf
```

Images are pulled from `../assets/images/` (the edgevision.pro site assets).

---

## EdgeVision — Retail & QSR (comprehensive deck)

A second, standalone deck that **combines the Apparel-Retail and QSR use cases**
of EdgeVision RetailTrack into one comprehensive story, in the same
editorial-dark design system.

**Deliverables:**
- [`EdgeVision-Retail-QSR.pdf`](./EdgeVision-Retail-QSR.pdf) — 28 pages, 16:9 (13.333″ × 7.5″)
- [`EdgeVision-Retail-QSR.pptx`](./EdgeVision-Retail-QSR.pptx) — native PowerPoint, same size

**Flow (28 slides):** Cover → *Ch.01 Visibility Gap* → The Challenge → *Ch.02 The
Platform* → Solution → Live Operations Console → *Ch.03 Two Lenses* → Customer &
Staff Analytics → Detection at Work → Customer Analytics elaborated → Heat Mapping
→ VIP Recognition → Staff Analytics elaborated → Hidden Loops → Brand-Level Heat
Map → Retail Long Tail → **QSR Edition** → QSR Capabilities → Drive-Thru → QSR Long
Tail → *Ch.05 Paradigm Shift* → Why GenAI → Hybrid Intelligence → Architecture →
Hardware & Privacy → Engagement → About → Contact.

**Rebuild:**

```bash
python3 deck/build_retail_qsr.py    # -> deck/EdgeVision-Retail-QSR.html
node    deck/render_rq.js           # -> deck/EdgeVision-Retail-QSR.pdf  (+ overflow check)
node    deck/build_pptx_rq.js       # -> deck/EdgeVision-Retail-QSR.pptx (needs 2x slide PNGs)
```

---

## EdgeVision — Retail & QSR · Intel Event Edition

A **simplified, non-technical, outcome-led** cut of the Retail & QSR story, built for a
30-minute closed-room pitch to retail + QSR prospects (Intel event). Same dark
editorial theme, far less text, plain-language headlines, big ideas.

**Deliverables:**
- [`EdgeVision-Retail-QSR-IntelEvent.pdf`](./EdgeVision-Retail-QSR-IntelEvent.pdf) — 16 pages, 16:9
- [`EdgeVision-Retail-QSR-IntelEvent.pptx`](./EdgeVision-Retail-QSR-IntelEvent.pptx) — native PowerPoint, **with a presenter talk-track in the speaker notes**

**Flow (16 slides):** Cover → *Hook: cameras record everything, tell you nothing* →
Three blind spots → *Idea: what if every camera could think?* → How it works (4 steps)
→ Four outcomes → **Retail** (what it sees · the VIP moment) → **QSR** (three numbers ·
drive-thru) → Why it's different (old counts / EdgeVision understands) → Private by
design + Intel → Proof → Close: see it live in 3 weeks.

**Rebuild:**

```bash
python3 deck/build_event.py     # -> deck/EdgeVision-Retail-QSR-IntelEvent.html
node    deck/render_ev.js       # -> ...IntelEvent.pdf  (+ overflow check)
node    deck/build_pptx_ev.js   # -> ...IntelEvent.pptx (needs 2x slide PNGs; notes embedded)
```
