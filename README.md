# Verlyn Tech — Operational Systems Infrastructure

> **A small team's unfair advantage.**  
> Serious, crafted digital intelligence for physical operations: independent cafes, specialty roasteries, and automotive repair workshops.

---

## Overview

**Verlyn Tech** installs the operational systems growing UAE businesses are missing: fast websites, official WhatsApp Business automation, CRM and automated follow-up, proven with the client's own numbers in a small pilot. Product truth (audience, offer, evidence, voice) lives in [`PRODUCT.md`](PRODUCT.md).

The landing page follows the **Fog Over Basalt** design system, documented in [`DESIGN.md`](DESIGN.md) (tokens, components, rules) with a machine-readable sidecar in `.impeccable/design.json`:
* **Palette**: fog white ground, basalt charcoal ink, one rare warm stone accent; a full dark theme (system default plus a manual switch).
* **Hero**: centred uppercase display headline over the desaturated basalt ridge photograph fading up into the fog.
* **Sections**: grouped capabilities (bento with one basalt tile), two illustrative business examples, a deliverables table, and the 14-day pilot form.
* **Typography**: Archivo (semi-expanded) for headings, Space Grotesk for body copy and Plus Jakarta Sans for supporting text, all self-hosted.
* **Main Entry**: [`index.html`](index.html)

---

## Core Capabilities Suite

1. **CRM Setup & Lead Management**: Leads stop living in WhatsApp chats — one pipeline, one owner, automated follow-up. Built around your actual sales process in days, not an off-the-shelf template.
2. **Landing Pages & SEO**: High-converting assets that capture demand and funnel it directly into your sales machine. Optimized for booked meetings and revenue, not vanity traffic.
3. **Marketing & Paid Ads**: Targeted campaigns optimized for ROAS, filling your pipeline predictably with constant split-testing and strict tracking.
4. **Lead Generation**: Predictable, scalable outreach systems to keep your pipeline full of qualified prospects via multi-channel personalized targeting.
5. **ERP Setup**: Centralize business operations—from inventory to finance—into one unified system tailored precisely to unique workflows.
6. **Premium Web Development**: Ultra-fast, meticulously designed digital storefronts built with striking bespoke aesthetics.

---

## Guardrails

The full list is in [`DESIGN.md`](DESIGN.md) (Do's and Don'ts). The essentials:

- **Truth first**: no invented numbers, clients or testimonials; the business examples are labelled as examples (see `PRODUCT.md`, Evidence on Hand).
- **Square and flat**: 0px corners, 1px hairlines, no shadows, glows or glass.
- **Rare stone**: the warm accent is for focus, selection and small moments only.
- **Misty imagery**: every photo desaturated and fading into the fog; no labels or fake metadata overlaid on photos.
- **No kickers**: no small uppercase label above a heading.
- **Accessible by default**: WCAG AA contrast in both themes, 44px touch targets, reduced-motion respected.

## Before launch

- **Form endpoint**: set the `action` attribute of `#pilot-form` in `index.html` to your form service (e.g. Formspree or a Make/n8n webhook). Until then the form honestly reports that it could not send. Optionally add your WhatsApp number to `data-whatsapp` for a fallback link.

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
Double-click [`index.html`](index.html) to open the landing page directly in any modern browser.

---

## Project Structure

```text
├── index.html              # Main Verlyn Tech landing page
├── PRODUCT.md              # Product truth: audience, offer, evidence, voice
├── DESIGN.md               # Fog Over Basalt design system (tokens + rules)
├── .impeccable/design.json # Machine-readable design sidecar
├── requirements.txt        # Python preview server dependencies
├── server.py               # FastAPI + standard library HTTP preview server
├── README.md               # This file
├── v3/                     # Historical snapshot of the pre-redesign page (not maintained)
│   └── index.html
└── assets/
    ├── fonts/              # Self-hosted Archivo, Space Grotesk, Plus Jakarta Sans (SIL OFL)
    ├── hero/
    │   └── v3/             # Basalt crest photography (sized -800 / -1408 versions used)
    ├── img/                # Cafe and garage photography (not used on the page)
    └── logos/              # Bespoke vector and transparent PNG brand marks
```

---

## License

Proprietary © 2026 Verlyn Tech. All rights reserved.
