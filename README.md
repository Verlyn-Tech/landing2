# Verlyn Tech — 5 Landing Page Directions

> **A small team's unfair advantage.**  
> Serious, crafted digital intelligence for physical operations: independent cafes, specialty roasteries, and automotive repair workshops.

---

## Overview

**Verlyn Tech** installs lean, permanent operational systems for independent businesses that lack an in-house digital presence. We build featherweight, sub-second web portals, configure official WhatsApp Business automation desks, and set up automated review-harvesting engines — giving local owners an unfair advantage without bloated SaaS retainers or complex software to learn.

This repository contains **5 complete, fully realized design directions**, each built from scratch in its own directory (`v1/` to `v5/`), committing entirely to its aesthetic without blending.

---

## The 5 Design Directions

### 1. `v1/` — Print-Tech Paper
* **Aesthetic**: Print-tech $\times$ data.
* **Palette**: Pale sage ground (`#e1e7dc`), dark-green forest ink linework (`#1f382b`), muted sage surfaces, with burnt terracotta rust accents (`#c84c24`).
* **Hero Feature**: Topographic contour-line illustration in dark-green ink floating seamlessly on sage paper, surrounded by pinned floating monospace telemetry chips (`[NODE 01: WHATSAPP ROUTE]`, `[SPEC: WORKSHOP AUTO]`, `[SPEC: CAFE DISPATCH]`).
* **Typography**: Space Grotesk display paired with JetBrains Mono data callouts and film-strip calibration ticks.
* **Location**: [`v1/index.html`](v1/index.html)

### 2. `v2/` — Data-as-Texture
* **Aesthetic**: Cinematic data-texture clouds rendered from amber binary characters.
* **Palette**: Dark teal sky (`#030e11` to `#082329`), cyan telemetry grid, with glowing amber/gold accents (`#f2b33d` at 589nm spectra).
* **Hero Feature**: Golden-hour clouds constructed from dense amber binary digits (`01001011...`) clustering in the lower right over a full-bleed dark teal atmosphere, with the headline anchored in the deepest left zone.
* **Typography**: Syne display with razor-sharp micro-mono telemetry tickers.
* **Location**: [`v2/index.html`](v2/index.html)

### 3. `v3/` — Vast Quiet Cinematic
* **Aesthetic**: Editorial minimalism $\times$ cinematic mountain atmosphere.
* **Palette**: Pure fog white (`#f5f6f7`), misty slate midtones (`#717c83`), and basalt charcoal (`#121517`) with a subtle warm stone accent (`#a67c52`).
* **Hero Feature**: Desaturated aerial mountain ridge in mist anchoring the lower half of the viewport, with the pure fog-white upper half dedicated to extreme whitespace and tiny centered sans typography.
* **Typography**: Understated, wide-tracked Space Grotesk (`letter-spacing: 0.25em`) with quiet hairline pill controls.
* **Location**: [`v3/index.html`](v3/index.html)

### 4. `v4/` — Dither Mono
* **Aesthetic**: Brutalist-editorial black & white with heavy bitmap dither.
* **Palette**: Stark studio dark (`#050505`), optical white, and high-contrast grayscale with an industrial phosphor hazard orange accent (`#ff5500`).
* **Hero Feature**: 1-bit Bayer bitmap dither matrix emerging on the right and dissolving into pitch black on the left; anchored at the base by a monumental cropped `VERLYN TECH` wordmark bleeding off the bottom viewport.
* **Typography**: Archivo Black display, brutalist grid dividers, and raw terminal prompts.
* **Location**: [`v4/index.html`](v4/index.html)

### 5. `v5/` — Classical Remix
* **Aesthetic**: Classical treatise $\times$ white editorial.
* **Palette**: Crisp museum white (`#ffffff` / `#fbfbfa`), charcoal ink, concentric orbit curves, with a royal lapis/blue pill CTA (`#1d4ed8`).
* **Hero Feature**: Vintage etched illustration plate of a classical scholar measuring chart geometry, framed with coordinate ticks and stipple hatching, flanked by celestial orbit curves and an independent client trust row.
* **Typography**: Cormorant Garamond serif with italicized emphasis (*"The small team's unfair advantage in an era of indifference"*), Space Grotesk, and JetBrains Mono.
* **Location**: [`v5/index.html`](v5/index.html)

---

## Master Preview Switcher

The root [`index.html`](index.html) provides an interactive preview switcher to seamlessly cycle through and inspect all 5 versions side-by-side or in full-screen tabs.

---

## Universal Guardrails Maintained

Across all 5 versions:
- ✅ **One Monumental Anchor**: Flat CSS/SVG hero stand-ins are placed with exact aspect ratios and positions, ready for final processed image drop-in with **zero layout shifts**.
- ✅ **Processed Imagery Only**: Linework, binary clouds, aerial mist silhouettes, 1-bit Bayer dither, and etched celestial orbits.
- ✅ **Technical Marginalia**: Real coordinates (`25°12'19.4"N 55°16'28.8"E`), catalog IDs, film-strip ticks, and millisecond latency timers.
- ✅ **Extreme Typography**: Monumental display headlines paired with tiny 10px–11px monospace notation; no middle-of-the-road blandness.
- ✅ **Monochrome + Single Contrast Accent**: Restrained palettes focused on clarity and confidence.
- 🚫 **Never Used**: No purple gradients, no glossy 3D SaaS blobs, no untextured stock photography, no rounded-everything friendliness, no generic icon-grid rows, and no Inter-only typography.

---

## Local Development & Preview

### Option 1: Python Server (Recommended)
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the preview server
python server.py
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

*(Note: `server.py` includes automatic fallback to the standard Python `http.server` if FastAPI/Uvicorn are not yet installed).*

### Option 2: Node / npx
```bash
npx serve -l 8000 .
```

### Option 3: Direct Browser
Simply double-click [`index.html`](index.html) to open the master switcher directly in any modern browser.

---

## Project Structure

```text
├── index.html          # Master interactive preview switcher
├── requirements.txt    # Python preview server dependencies
├── server.py           # FastAPI + standard library HTTP preview server
├── README.md           # Documentation & design specifications
├── v1/                 # Direction 1: Print-Tech Paper
│   └── index.html
├── v2/                 # Direction 2: Data-as-Texture
│   └── index.html
├── v3/                 # Direction 3: Vast Quiet Cinematic
│   └── index.html
├── v4/                 # Direction 4: Dither Mono
│   └── index.html
└── v5/                 # Direction 5: Classical Remix
    └── index.html
```

---

## License

Proprietary © 2026 Verlyn Tech. All rights reserved.
