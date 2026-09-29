---
name: Verlyn Tech
description: Fog Over Basalt. Pale fog surfaces over dark volcanic rock; calm, weighty, precise.
colors:
  fog: "#f5f6f7"
  fog-surface: "#fbfbfc"
  fog-tint: "#eceef0"
  fog-line: "#e0e3e6"
  basalt: "#121517"
  slate: "#586168"
  slate-quiet: "#666f76"
  field-line: "#7c858c"
  stone: "#a67c52"
  stone-ink: "#8a6440"
  stone-deep: "#7d5a39"
  ember-error: "#a3362a"
  night: "#0f1214"
  night-surface: "#161a1d"
  night-tint: "#1a1f23"
  night-line: "#262c31"
  mist: "#eef0f1"
  mist-muted: "#a3adb4"
  mist-quiet: "#7f8a92"
  mist-rule: "#d8dde0"
  mist-tile-text: "#c9ced2"
  stone-night: "#c49a6f"
  ember-night: "#e08a7e"
typography:
  display:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "clamp(28px, 4vw, 46px)"
    fontWeight: 300
    lineHeight: 1.22
    letterSpacing: "0.08em"
  display-sm:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "clamp(28px, 3.4vw, 38px)"
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: "0.06em"
  headline:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "clamp(26px, 3vw, 34px)"
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  subhead:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "24px"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "20px"
    fontWeight: 500
    lineHeight: 1.4
  title-sm:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "18px"
    fontWeight: 500
    lineHeight: 1.4
  body:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.7
  body-text:
    fontFamily: "Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.7
  body-sm:
    fontFamily: "Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 500
    lineHeight: 1.6
  caption:
    fontFamily: "Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 600
    letterSpacing: "0.16em"
rounded:
  none: "0px"
spacing:
  xs: "8px"
  sm: "16px"
  md: "28px"
  lg: "40px"
  xl: "72px"
  section: "128px"
  section-mobile: "80px"
  gutter: "48px"
  gutter-mobile: "16px"
components:
  button-primary:
    backgroundColor: "{colors.basalt}"
    textColor: "{colors.fog}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "15px 30px"
  button-primary-hover:
    backgroundColor: "{colors.stone-deep}"
    textColor: "{colors.fog}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.basalt}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "10px 18px"
    height: "44px"
  button-ghost-hover:
    backgroundColor: "{colors.basalt}"
    textColor: "{colors.fog}"
  icon-button:
    backgroundColor: "transparent"
    textColor: "{colors.basalt}"
    rounded: "{rounded.none}"
    size: "44px"
  input:
    backgroundColor: "transparent"
    textColor: "{colors.basalt}"
    typography: "{typography.body-text}"
    rounded: "{rounded.none}"
    padding: "12px 0"
  panel:
    backgroundColor: "{colors.fog-surface}"
    rounded: "{rounded.none}"
    padding: "40px"
  panel-tinted:
    backgroundColor: "{colors.fog-tint}"
    rounded: "{rounded.none}"
    padding: "40px"
  panel-basalt:
    backgroundColor: "{colors.basalt}"
    textColor: "{colors.mist}"
    rounded: "{rounded.none}"
    padding: "40px"
---

# Design System: Verlyn Tech

## Overview

**Creative North Star: "Fog Over Basalt"**

The page is a pale, quiet field of fog laid over dark volcanic rock. Most of the screen is soft off-white with generous empty space; the weight comes from basalt charcoal type, thin charcoal rules and one photograph of a mist-wrapped basalt ridge that anchors the first screen. A single warm stone accent appears rarely, like light catching rock. Nothing shouts. Confidence comes from restraint, precision and room to breathe.

Density is low: large section spacing, short measures, few elements per view. Components are precise and restrained: square corners, hairline borders, quiet hover states that invert rather than glow. Photography is used sparingly: the single desaturated, misty basalt ridge in the hero, dissolving into the fog rather than sitting in a hard box. Content sections are type and rules, not pictures. Dark mode is the same world at night: basalt surfaces, mist-coloured type, photos dimmed.

**Key Characteristics:**
- Fog-white ground, basalt ink, one rare stone accent.
- Square geometry everywhere (0px radius); hairline rules instead of shadows.
- Wide uppercase display type, light weight, generous tracking.
- Desaturated, misty photography that melts into the page.
- One authored motion moment (the hero settling in); everything else is still.

## Colors

A near-monochrome fog-and-basalt palette with a single warm stone accent.

### Primary
- **Basalt Charcoal** (fog theme ink): primary text, headings, primary buttons, strong rules. The dominant dark of the system.
- **Warm Stone** (accent): focus rings, text selection, the caret, rare decorative accents. Never a large fill.
- **Stone Ink**: stone at a darker value for any small stone-coloured text, so it passes 4.5:1 on fog.
- **Deep Stone**: primary button hover fill under fog-white text (5.7:1).

### Neutral
- **Fog** : page background.
- **Fog Surface**: raised sections (examples, contact) and panels.
- **Fog Tint**: the tinted panel variant, used to vary a grid without cards.
- **Fog Line**: hairline dividers and panel borders.
- **Misty Slate**: secondary text (5.8:1 on fog).
- **Quiet Slate**: small labels, captions, placeholders, table headings (4.7:1 on fog; do not place on Fog Tint).
- **Field Line**: input underlines (3.6:1, the non-text minimum for form boundaries).
- **Ember**: error text and error borders only.

### Night (dark theme)
- **Night / Night Surface / Night Tint / Night Line**: the dark equivalents of Fog, Fog Surface, Fog Tint and Fog Line.
- **Mist / Mist Muted / Mist Quiet**: primary, secondary and small text on night surfaces.
- **Mist Rule**: strong rules in dark mode (the night equivalent of basalt rules).
- **Tile Mist**: secondary text on the basalt tile, in both themes.
- **Night Stone**: the accent in dark mode, also the primary button hover fill under night text (7.3:1).
- **Night Ember**: error text and borders in dark mode.

### Named Rules
**The Rare Stone Rule.** Warm stone never covers more than a sliver of any screen: a focus ring, a selection, a hover. If stone is filling a box, it is wrong.

**The Contrast Floor Rule.** Every text colour is checked against the surface it sits on: 4.5:1 for body and small text, 3:1 for large text and form boundaries. The lighter grey (#8e98a0) failed this and is retired.

**The Basalt Tile Rule.** A panel that is basalt stays basalt in both themes (its own tile tokens); it is the one intentional dark block on a fog page.

## Typography

**Display Font:** Space Grotesk (with system-ui fallback), self-hosted variable, weights 300 to 600
**Body Font:** Space Grotesk for reading copy; Plus Jakarta Sans (self-hosted variable, 400 to 600) for supporting text, labels, forms and tables

**Character:** Space Grotesk's slightly technical geometry carries the voice: light, wide and calm at display sizes. Plus Jakarta Sans is the quieter, rounder workhorse for everything small and functional.

### Hierarchy
- **Display** (300, uppercase, wide tracking): the hero headline only. A single strong word run may step to 600.
- **Display Small** (300, uppercase): the contact headline, the one other uppercase heading.
- **Headline** (300, balanced wrapping): section headings, max about 22 to 30ch.
- **Subhead** (400): group headings inside a panel and the basalt tile heading.
- **Title / Title Small** (500): example headings (Title) and item and table-row headings (Title Small).
- **Body** (400): reading copy, max about 52 to 60ch.
- **Body Text** (Plus Jakarta Sans): capability descriptions, table cells, the "What we install" lines.
- **Body Small** (Plus Jakarta Sans, 500): the guarantee line, form alerts, the skip link.
- **Caption** (Plus Jakarta Sans): form labels (600), helper text, error messages, the footer.
- **Label** (600, uppercase): buttons and table column headings. Never as a kicker above a heading.

### Named Rules
**The No-Kicker Rule.** No small uppercase label sits above a heading. The heading carries its own weight.

**The One Uppercase Voice Rule.** Uppercase is reserved for the hero display line, the contact headline and functional labels (buttons, column headings). Body copy is never uppercase.

## Layout

A single centred column with a 1180px maximum width and 48px gutters (16px on phones). Sections are separated by large vertical space (128px, 80px on phones) and by switching between the fog and fog-surface grounds with hairline borders, never by boxes.

The hero is a full-height column: nav, then centred display copy, then the basalt ridge photograph filling the remaining height and fading upward into the fog. Content sections use CSS grid: a 12-column bento for capabilities (8 + 4 split, the basalt tile spanning two rows), two equal columns for the examples and the contact block (5 + 6). Every multi-column layout collapses to one column at 767px and below; the capabilities grid collapses at 1024px.

Breakpoints: 1024px (tablet), 767px (phone), 479px (small phone: the nav drops its CTA because the hero CTA sits directly below).

## Elevation & Depth

Flat. The system uses no shadows. Depth comes from tonal layering (fog, fog surface, fog tint, and the one basalt tile), hairline rules and the photograph's own atmosphere. Hover states invert fills rather than lifting elements.

### Named Rules
**The No-Shadow Rule.** Surfaces are flat at rest and on hover. If an element needs separation, use a tone step or a 1px rule, not a shadow.

## Shapes

Square everything: 0px radius on buttons, inputs, panels, the theme switch and images. Borders are 1px hairlines; the only 2px line is an input's focused underline. The hero photograph fills its space and is desaturated to sit in the palette. Text blocks such as the business examples open on a thin basalt rule instead of a picture.

## Components

### Buttons
Precise and restrained: square, uppercase label type, no radius, no shadow.
- **Shape:** square corners (0px).
- **Primary:** basalt fill, fog text, 15px by 30px padding, one line, never wraps.
- **Hover / Focus:** fill shifts to deep stone (night stone in dark mode); 2px warm stone focus ring offset 3px; presses down 1px on active. Disabled while sending: 70% opacity, progress cursor.
- **Ghost:** transparent with a 35% basalt hairline border, 44px minimum height; inverts to a basalt fill on hover. Used for the nav CTA.
- **Icon button (theme switch):** 44px square ghost with a 20px Phosphor icon inline as SVG, same inversion on hover.

### Cards / Containers
- **Corner Style:** square (0px).
- **Background:** fog surface with a fog-line border, or fog tint with no border, or basalt for the single dark tile.
- **Shadow Strategy:** none (see Elevation & Depth).
- **Internal Padding:** 40px (28px by 20px on phones). Items inside a panel are separated by hairline rules, never nested cards.

### Inputs / Fields
- **Style:** transparent, underline only (1px field line), square, 16px text so phones never zoom.
- **Labels:** always above the field in 13px 600 Plus Jakarta Sans; placeholders are examples, never labels; optional fields say "(optional)".
- **Focus:** the underline thickens to 2px basalt.
- **Error:** ember underline and an ember message directly below; a form-level alert box with an ember hairline border for sending failures.

### Navigation
Logo left, actions right, 80px tall (64px on phones), no background. The logo link, theme switch and ghost CTA are all at least 44px tall. The logo and emblem swap to their light variants in dark mode, and only the active variant downloads.

### Data Table (signature)
The deliverables table: uppercase Label column headings over a basalt rule, row headings in Title type, hairline rules between rows, tabular numerals. On phones each row stacks and every value shows its column name above it.

## Do's and Don'ts

### Do:
- **Do** keep the fog ground dominant; basalt is for type, rules and the single dark tile.
- **Do** use warm stone only for focus, selection and small moments (The Rare Stone Rule).
- **Do** keep every corner square (0px) and every border 1px.
- **Do** desaturate and mist every photograph so it melts into the page.
- **Do** make every control at least 44px tall and every text colour pass its contrast floor.
- **Do** let the hero's settle-in be the only entrance animation, and switch it off under reduced motion.

### Don't:
- **Don't** add shadows, glows, gradients on text, or glass blur.
- **Don't** round corners or mix pill buttons into the square system.
- **Don't** put a small uppercase kicker above a heading.
- **Don't** use big-number stat blocks unless the number is a real, measured client result.
- **Don't** add coordinate strips, fake metadata badges or labels overlaid on photographs.
- **Don't** use the retired light grey (#8e98a0) for text.
