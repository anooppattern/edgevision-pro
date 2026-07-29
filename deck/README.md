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
