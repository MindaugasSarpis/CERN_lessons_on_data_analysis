# SVG Diagram Recipe

Reusable template + palette for hand-built SVG figures that match the deck's dark, glass-card aesthetic. Used by `git_flow.svg`, `git_staging.svg`, `data_types.svg`.

## Canvas

- `viewBox="0 0 1600 900"` for full-slide diagrams (16:9). Use `1600 x 1100` when you need a taller layout.
- Slides embed via `layout: image` + `backgroundSize: contain`.

## Palette (semantic)

Match the `card-*` classes in `custom-slides.css`:

| Role        | Accent (stroke/title) | Fill-top    | Fill-bot    |
|-------------|-----------------------|-------------|-------------|
| primary     | `#38bdf8` (sky)       | `#1e293b`   | `#0f172a`   |
| secondary   | `#f59e0b` (amber)     | `#78350f`   | `#1c1917`   |
| success     | `#10b981` (emerald)   | `#064e3b`   | `#0b1220`   |
| info        | `#60a5fa` (blue)      | `#1e3a8a`   | `#0f172a`   |
| accent      | `#c084fc` (violet)    | `#581c87`   | `#1e1b4b`   |
| warning     | `#eab308` (yellow)    | `#78350f`   | `#1c1917`   |
| neutral/muted | `#94a3b8` (slate)   | `#0b1220`   | `#0b1220`   |

Text colors: titles `#f1f5f9`, body `#e2e8f0`, subtle `#94a3b8`, faint `#64748b`.

## Drop-in `<defs>`

```xml
<defs>
  <!-- one gradient per semantic color you use -->
  <linearGradient id="gPrimary" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#1e293b" stop-opacity="0.9"/>
    <stop offset="100%" stop-color="#0f172a" stop-opacity="0.9"/>
  </linearGradient>
  <!-- repeat for gSecondary, gAccent, gSuccess, gInfo, gWarning -->

  <!-- soft drop shadow used on every card -->
  <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="4"/>
    <feOffset dx="0" dy="3"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.35"/></feComponentTransfer>
    <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>

  <!-- explicit per-color arrowheads (DO NOT use context-stroke — poor renderer support) -->
  <marker id="arrAmber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="#f59e0b"/>
  </marker>
  <!-- repeat: arrGreen #10b981, arrPurple #c084fc, arrBlue #60a5fa, arrGray #94a3b8 -->
  <!-- for two-headed arrows, add an `-S` variant with refX="1" -->

  <style>
    .card-title { font-size: 22px; font-weight: 700; text-anchor: middle; }
    .card-sub   { font-size: 14px; fill: #94a3b8; text-anchor: middle; }
    .cmd        { font-family: 'JetBrains Mono','Fira Code',monospace; font-weight: 600; }
  </style>
</defs>
```

Set the root `<svg>` font: `font-family="'Inter','Helvetica Neue',Arial,sans-serif"`.

## Building blocks

### Glass card (node / container)

```xml
<g filter="url(#soft)">
  <rect x="X" y="Y" width="W" height="H" rx="16"
        fill="url(#gPrimary)" stroke="#38bdf8" stroke-width="2"/>
</g>
<text x="X+W/2" y="Y+36" class="card-title" fill="#38bdf8">📊 Title</text>
<text x="X+W/2" y="Y+60" class="card-sub">one-line caption</text>
```

- `rx="16"` for large cards, `rx="10–12"` for small leaves.
- Put the `<rect>` inside a `<g filter="url(#soft)">` so only the shape casts the shadow (not text).

### Leaf / code chip

Small rect, no shadow, mono font:

```xml
<rect x="X" y="Y" width="W" height="70" rx="10" fill="#0b1220" stroke="#334155" stroke-width="1.5"/>
<text x="X+20" y="Y+30" font-size="18" fill="#e2e8f0" class="cmd">📄 file1.txt</text>
<text x="X+20" y="Y+52" font-size="13" fill="#64748b">status</text>
```

### Arrows

- Solid forward promotion: `stroke-width="3"`, semantic accent color, `marker-end="url(#arrGreen)"`.
- Dashed for inspect/undo: `stroke-dasharray="5 4"`, `stroke="#94a3b8"`, `stroke-width="2"`.
- Two-headed (compare): `marker-start="url(#arrGrayS)" marker-end="url(#arrGray)"`.

### Connectors in hierarchies

Bezier curves between parent and child:

```xml
<path d="M Px Py Q Mx My Cx Cy" stroke="#f59e0b" stroke-width="2" fill="none" opacity="0.7"/>
```

Use `stroke-dasharray="3 4"` + `opacity="0.5"` for leaf-level (weaker) connectors.

## Layout conventions

- **Title**: `<text x="800" y="60" text-anchor="middle" font-size="36" font-weight="700" fill="#f1f5f9">`
- **Subtitle**: `font-size="18" fill="#94a3b8"` at `y="92"`.
- **Legend** (if needed): bottom-left, `x="70" y="1020"`, `font-size="13"`.
- Leave ~60 px top margin and ~40 px bottom margin so nothing gets clipped under slide chrome.

## Gotchas

- **`fill="context-stroke"` on markers is not portable.** Define one marker per color.
- **XML comments cannot contain `--`.** Write "cached" not `--cached`.
- **Emoji fonts differ per renderer.** Keep emojis, but don't rely on exact pixel-level alignment.
- Validate with `xmllint --noout path.svg` before committing.

## Using in a Slidev slide

```md
---
hideInToc: true
layout: image
image: /figures/your_diagram.svg
backgroundSize: contain
---
```

Or inline for small inserts:

```md
<img src="/figures/your_diagram.svg" class="w-full" />
```

## Existing diagrams as references

- `git_flow.svg` — 4-lane swim diagram, solid+dashed arrows, legend.
- `git_staging.svg` — 3-zone hub-and-spoke with commit chain.
- `data_types.svg` — hierarchy tree with colored branches and leaf chips.
