# EdgeVision — Pattern AI Labs

Marketing site for **EdgeVision** by Pattern AI Labs — the on-prem Vision + GenAI edge AI platform that powers **RetailTrack** (store floors) and **RiderTrack** (delivery hubs).

Live at **[www.edgevision.pro](https://www.edgevision.pro)**.

## Stack

100% static — plain HTML, CSS, JS. No build step.

```
index.html       Single-page site
styles.css       Editorial dark theme, Inter Light display type
script.js        Sticky context label, progress bar, scroll reveal
assets/
  logo.svg       Original Pattern AI Labs wordmark (kept for reference)
  images/*.png   Hero + section imagery (generated via Gemini)
gen_image.py     Helper for re-generating images via Gemini 2.5 Flash Image
CNAME            Custom domain config for GitHub Pages
```

## Local preview

```bash
python3 -m http.server 8000
# open http://127.0.0.1:8000
```

## Deploy

This repo deploys to GitHub Pages on push to `main`.

- Custom domain: `www.edgevision.pro` (set via `CNAME` file)
- Pages source: `main` branch, root directory
