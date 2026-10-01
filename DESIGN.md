---
version: alpha
name: MercuReal
name_display: MercuReal Tech Solutions
description: Dark luxury digital brand. Deep navy canvas, warm gold-amber accent, glass surface treatment, bold geometric typography, 3D immersive backgrounds. Premium technology services for ambitious businesses.
colors:
  primary: "#070d1a"
  secondary: "#0a0e1a"
  surface: "rgba(255,255,255,0.035)"
  surface-border: "rgba(255,255,255,0.07)"
  ink: "#f3f0eb"
  ink-muted: "rgba(243,240,235,0.55)"
  ink-dim: "rgba(243,240,235,0.22)"
  accent: "#e0b060"
  accent-deep: "#c49a40"
  accent-glow: "rgba(224,176,96,0.25)"
typography:
  display:
    fontFamily: "Outfit"
    fontSize: "clamp(2.8rem, 10vw, 5.2rem)"
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.04em"
  body:
    fontFamily: "DM Sans"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "DM Sans"
    fontSize: "0.85rem"
    fontWeight: 400
    letterSpacing: "0.01em"
rounded:
  pill: 9999px
  card: 16px
spacing:
  section: 2.25rem
  card-padding: 1.5rem
  gap-small: 0.75rem
  gap-medium: 1.25rem
components:
  header-pill:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.surface-border}"
    borderRadius: "{rounded.pill}"
    backdropFilter: blur(18px)
    padding: 0.35rem 0.35rem 0.35rem 0.35rem
  avatar:
    size: 36px
    borderRadius: 50%
    border: 1.5px solid rgba(255,255,255,0.12)
  tag-pill:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.surface-border}"
    borderRadius: "{rounded.pill}"
    padding: 0.55rem 1.1rem
    color: "{colors.ink-muted}"
    typography: label
  button-primary:
    backgroundColor: linear-gradient(135deg, "{colors.accent}" 0%, "{colors.accent-deep}" 100%)
    textColor: "#0b0d14"
    borderRadius: "{rounded.pill}"
    fontFamily: "Outfit"
    fontWeight: 600
    padding: 0.85rem 1.8rem
    shadow: "0 8px 28px {colors.accent-glow}, inset 0 1px 0 rgba(255,255,255,0.2)"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.surface-border}"
    borderRadius: "{rounded.pill}"
    fontFamily: "Outfit"
    fontWeight: 600
    padding: 0.85rem 1.8rem
  feature-check:
    iconColor: "{colors.accent}"
    textColor: "{colors.ink}"
    fontSize: "0.9rem"
---

## Overview (Brand & Style)

MercuReal is a technology company built on the idea of "a digital place for all" — premium digital systems for ambitious businesses. The design language communicates confidence through deep darkness, precision through glass surfaces, and premium quality through warm gold-amber accents.

The visual posture is **dark luxury with immersive depth**. Every page should feel like it floats in a deep environment — not flat, not decorative for its own sake, but layered and dimensional.

## Colors

- **Primary (`#070d1a`)**: Deep navy-black background. Not pure black — retains warmth and prevents harsh contrast fatigue.
- **Surface (`rgba(255,255,255,0.035)`)**: Glass card background. Low opacity so background depth shows through.
- **Accent (`#e0b060`)**: Warm gold-amber. The only bright color. Used sparingly: one word in the headline, the primary CTA, icon highlights, and glow effects.
- **Ink (`#f3f0eb`)**: Warm off-white text. Never pure `#fff` — it softens against the dark base and feels editorial.

All interactive elements use the accent color exclusively. No rainbow palettes, no secondary bright colors.

## Typography

- **Display (Outfit, 800, -0.04em tracking)**: Headlines only. Large, tight, geometric. The negative tracking creates authority.
- **Body (DM Sans, 300/400)**: All supporting text. Clean, readable, slightly lighter weight to create hierarchy against the bold display.
- **Labels (DM Sans, 400, 0.01em tracking)**: Buttons, tags, meta text. Slight positive tracking improves legibility at small sizes.

Never use serif for headings. The geometric sans family reinforces the technology / engineering identity.

## Layout & Spacing

- **Max-width container**: 640px centered. Keeps focus tight — this is a personal/business landing page, not a sprawling site.
- **Vertical rhythm**: Sections separated by `2.25rem`. Large whitespace is intentional — it lets the dark background breathe.
- **Glass cards**: Every interactive/card element uses the same glass treatment: `rgba` background + `rgba` border + `backdrop-filter: blur(18px)`. Consistency is critical — mixing glass and solid cards breaks the aesthetic.

## Elevation & Depth

Depth comes from layers, not shadows alone:
1. **3D WebGL background** — particle constellation or geometric scene, slow rotation, cool-blue ambient glow. Always present.
2. **Glass cards** — floating above the 3D scene with blur.
3. **Text and buttons** — crisply rendered on top of glass.

No drop shadows on cards except the subtle `box-shadow` that mimics ambient light (`0 8px 32px rgba(0,0,0,0.35)`). No heavy shadows.

## Components

### Header Pill
A rounded glass bar at the top containing brand identity on the left and minimal actions on the right. Never a full-width solid header — the pill shape keeps the design open.

### Primary CTA Button (`button-primary`)
Filled with the gold-amber gradient. High-contrast dark text (`#0b0d14`) on bright background ensures readability. Used for the single most important action (contact / start project).

### Secondary CTA Button (`button-secondary`)
Transparent glass with border. Used for secondary actions (explore, learn more). Less emphasis than primary but still clearly interactive.

### Feature Checklist (`feature-check`)
Three short capability statements with gold checkmarks. No cards, no icons beyond the check — the list is clean and scannable.

## Do's and Don'ts

**Do:**
- Keep the gold accent to one element per viewport section (headline word, one CTA, icon accents).
- Use `backdrop-filter` consistently on all floating surfaces.
- Keep the 3D background subtle — it should feel ambient, not distracting.
- Ensure text has at least 4.5:1 contrast against glass surfaces (tested: `#f3f0eb` on `rgba(255,255,255,0.035)` passes at display sizes).

**Don't:**
- Add a second bright color (no green, blue, purple accents).
- Use solid black (`#000`) for cards — the glass treatment requires partial transparency.
- Place more than two buttons side-by-side. If more actions are needed, use a dropdown or secondary page.
- Add decorative gradients behind text that reduce readability.
- Use stock photography as hero imagery — the 3D background serves that role.
