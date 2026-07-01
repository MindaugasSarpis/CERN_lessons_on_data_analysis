# FF-2026 Visual Style Upgrade — Design Spec

**Status:** Approved direction, spec awaiting author review · **Date:** 2026-07-01 · **Branch:** `ff2026` (work in worktree `visual-style-upgrade`)
**Owner:** Mindaugas Šarpis
**Relationship to roadmap:** Additive **visual workstream** — not one of the existing A/B/C workstreams in `2026-07-01-ff2026-master-roadmap-design.md`. Should be logged as a new workstream once the pilot is approved.

> A "bold & kinetic" modernisation of the Slidev deck's visual system. The goal is
> to make the slides look modern and genuinely exciting — pushing **past** the
> current most-polished reference (`crash_course_for_video_lecture.md`), not just
> matching it. This cycle delivers a **reusable theme-level system** plus a **single
> pilot lecture** applied end-to-end so the look can be approved before any rollout.

---

## 0. How to resume this work

**What this is.** A theme-level visual upgrade for the lecture decks. The polished
motion patterns that currently live *duplicated inline* in the video deck and L06
get promoted into the shared theme, extended with a bolder palette, modern
typography, and kinetic motion — then applied fully to one pilot lecture (**L01
Course Orientation**) for sign-off.

**Where we are.** Direction approved by owner (2026-07-01): bold & kinetic;
Space-Grotesk-display + PT-Serif-body typography; electric cyan/violet/amber
accent trio; L01 as pilot. Spec written, awaiting author review of the written spec.

**To continue in a new session:**
1. Read this file top to bottom.
2. Confirm the theme survey in §2 still holds (`git log` on the theme dir).
3. Next action is in §8.
4. Locked decisions are in §2.4.

**Process note.** Produced via `superpowers:brainstorming`. Terminal step after
spec approval is `superpowers:writing-plans` to produce the implementation plan.

---

## 1. Goal & scope

### Goal
Make the decks look **modern and exciting** — a bold, kinetic visual language that
goes **beyond** the current best reference deck, delivered as a **reusable theme
system** (so every deck inherits it) plus a **fully-applied pilot lecture**.

### In scope (this cycle)
- Theme-level design system: palette tokens, typography, a generalized **motion &
  effects library**, upgraded hero/section layouts, one new layout.
- **Backward compatibility**: all existing class names (`card-*`, `card-glass`,
  `grid-*`, `pad-*`, `anim-*`, `flow-*`, etc.) keep working unchanged.
- **One pilot lecture (L01)** re-authored end-to-end to the new standard.

### Non-goals (explicitly deferred)
- **No content edits.** Visual only. In particular, L01's stale grading slide
  (20/20/60) is a Workstream-A content fix, **not** touched here.
- **No rollout** to the other 17 decks this cycle. L09 is named as the immediate
  next dense-content target *after* pilot approval, but is not built here.
- **No changes** to FF `.docx` sources, roadmap workstreams A/B/C, the video
  pipeline, or the workbook.

### Constraints
- **`bs2026` deploy branch untouched.** GitHub Pages deploys from `bs2026`; this
  work is on `ff2026`. No risk to the live site this cycle.
- **Motion discipline.** Every animation must honour `prefers-reduced-motion` and
  degrade on mobile / coarse pointers — matching the existing `cover.vue` pattern.
- **Additive only.** New effects are opt-in classes/layouts; nothing existing is
  removed or renamed.
- **No new build tooling** unless strictly required (fonts load via the theme's
  existing Slidev `fonts` mechanism, not a new bundler step).

---

## 2. Context snapshot (theme survey, so a fresh session needn't re-survey)

### 2.1 Current theme state
- **Theme dir:** `lectures/content/theme/` — local `@slidev/theme-scienced`.
  - `styles/custom-slides.css` (639 lines) — mature card system: `card` +
    `card-primary/secondary/accent/info/success/warning`, `card-glass` (left-border
    fade card), `pad-*`, `grid-2/3`, dice boxes, dropdown-card (`dd-*`), `miss-*`,
    `fig`, extensive typography utilities. Deep-blue monochrome palette in `:root`.
  - `styles/layouts.css` (136 lines) — heading scale, per-layout sizing
    (cover/intro/fact/statement/quote/section), Mermaid readability, default bg.
  - `styles/mermaid-styles.css` (43 lines).
  - `layouts/` — `cover.vue` (**already sophisticated**: Ken Burns bg drift,
    volumetric light glows, accent-line sweep, staged content reveal, full
    reduced-motion + mobile guards), plus `section.vue`, `fact.vue`, `statement.vue`,
    `intro.vue`, `quote.vue`, `center-bkg.vue`.
  - `section.vue`, `fact.vue`, `statement.vue`, `intro.vue` are **bare** (just a
    centered `<slot/>`); all their styling is in `layouts.css`. Big opportunity.
- **Fonts (theme `package.json` defaults):** `sans`/`serif` = **PT Serif**,
  `mono` = **PT Mono**. Academic serif look throughout.
- **Slidev:** `@slidev/cli ^52.14.2`. Addons: `slidev-addon-python-runner`.
  Mermaid `^11.12.0`. No UnoCSS/Vite config override in repo root.

### 2.2 The polished-reference patterns (to generalize)
`crash_course_for_video_lecture.md` and `L06` contain the deck's most modern
patterns, but **inline in `<style>` blocks** (duplicated, not shared):
- **`anim-card` collapse/expand** — heading large when collapsed, shrinks as
  `anim-ex` example rows fade/expand in on `v-click`; card slides in from left when
  revealed. Uses `:has()` + `slidev-vclick-hidden`.
- **`anim-sub`** — italic subtitle under a card heading.
- **`flow-container` / `flow-row` / `flow-arrow`** — vertical staged pyramid
  (Data → Information → Knowledge → Wisdom) with per-row `v-click` reveal.
- Heavy use of `card-glass` + staged `v-click` + video backgrounds.

These are exactly the patterns to lift into the theme, then extend.

### 2.3 The palette today
`:root` in `custom-slides.css` is a **deep-blue monochrome**: primary `#031633`,
accents topping out at cyan `#0ea5e9`/`#38bdf8`, teal `#14b8a6`, amber `#f59e0b`
(warning only). `cover.vue` independently uses cyan `#5ec4c4`. There is **no
unified accent-emphasis system** and no violet. Effectively single-hue.

### 2.4 Decisions locked (2026-07-01, owner-approved)
1. **Bold & kinetic** intensity — push past the video reference.
2. **Typography:** **Space Grotesk** display font for headings; **PT Serif** kept
   for body prose. (All-sans was the considered alternative; serif body retained.)
3. **Palette:** keep deep-blue base; add **electric accent trio — cyan (lead) +
   violet + amber** — for kinetic emphasis (gradient text, glow, big numbers).
4. **Scope:** theme system + **L01 pilot** only; rollout deferred.
5. **Backward compatible & motion-safe** are hard requirements.

---

## 3. The design language

### 3.1 Palette
Keep the calm deep-blue base for surfaces; introduce a small **accent-emphasis
layer** used sparingly for energy. New `:root` tokens (added, not replacing):

| Token | Value (proposed) | Use |
|---|---|---|
| `--accent-cyan` | `#5ec4c4` → `#22d3ee` range | lead accent; matches cover |
| `--accent-violet` | `#a78bfa` / `#8b5cf6` | secondary emphasis, gradient stops |
| `--accent-amber` | `#fbbf24` / `#f59e0b` | energy pops, big-number highlights |
| `--grad-kinetic` | `linear-gradient(100deg, cyan, violet)` | gradient headings/text |
| `--grad-energy` | `linear-gradient(100deg, amber, cyan)` | stats/dividers |
| `--glow-cyan` | soft `box-shadow`/`filter` glow | key cards, hero elements |

Existing `--color-*` tokens are **unchanged** so every current card keeps its look.

### 3.2 Typography
- **Headings:** Space Grotesk (600/700), tighter tracking, optional gradient fill
  via `.gradient-text` / `.kinetic`.
- **Body:** PT Serif retained (readability, academic tone).
- **Mono:** PT Mono retained.
- Wire Space Grotesk through the theme `package.json` `slidev.defaults.fonts`
  mechanism (Slidev auto-imports Google Fonts) — no new bundler step. Add a
  `--font-display` token; apply to `h1/h2` in layouts and a `.font-display` util.

### 3.3 Motion & effects (all `prefers-reduced-motion`-guarded)
- **Reveal helpers:** `reveal-left`, `reveal-up`, `reveal-scale`, `reveal-blur`
  (fly/fade/blur-in on `v-click`, generalizing the inline `translateX(-40px)` trick).
- **`gradient-text` / `kinetic`:** gradient-filled, optionally animated (slow hue
  shift) heading text.
- **`glow`:** soft accent glow for a hero/key card.
- **`aurora`:** subtle animated gradient backdrop layer (behind content) for
  section/hero slides — a stronger, colour-shifting cousin of the cover's
  volumetric glows.
- **Big-stat / `metric`:** oversized gradient number with a count-up-style entrance
  and a label (e.g. `27 km`, `1 PB/s`, `99.9999991%`).

---

## 4. Deliverables — theme system (units & interfaces)

Each is an isolated, independently-reviewable unit.

1. **`styles/animations.css` (new)** — the shared motion & effects library:
   `anim-card`/`anim-sub`/`anim-ex`/`flow-*` (lifted verbatim-in-behaviour from the
   inline blocks so the video deck & L06 can later drop their inline copies), plus
   the new `reveal-*`, `gradient-text`, `kinetic`, `glow`, `aurora`, big-stat
   utilities. Imported via the theme `styles/index.ts`.
   - *What it does:* provides opt-in animation classes. *How to use:* add the class
     to a card/element with `v-click`. *Depends on:* Slidev's `slidev-vclick-hidden`.
2. **Palette + type tokens** — new `--accent-*`, `--grad-*`, `--glow-*`,
   `--font-display` in `:root`; existing tokens untouched.
3. **`layouts/section.vue` (upgraded)** — bold kinetic section divider: giant
   gradient keyword, animated accent sweep, `aurora` backdrop, subtle drift.
   Backward-compatible with existing `layout: section` slides (they gain the look
   for free; `# Section **Keyword**` markup unchanged).
4. **`layouts/fact.vue` + `layouts/statement.vue` (enhanced)** — gradient + glow
   big statement/number treatment.
5. **`layouts/metric.vue` (new, optional)** — hero-stat layout for animated big
   numbers.
6. **Font wiring** — theme `package.json` `fonts.sans`/display; `--font-display`
   applied in `layouts.css`.

**Compatibility contract:** no existing class or layout is renamed or removed. A
deck that used none of the new classes renders identically except for the global
heading font and any layout that opts into new backdrops. `section.vue`'s visual
change is intentional and applies deck-wide — reviewed as part of the pilot.

## 5. Deliverable — pilot lecture (L01 Course Orientation)

Re-author **L01** end-to-end to the new standard: kinetic cover, bold section
dividers, gradient/emphasis headings, `metric` hero stats where apt, `reveal-*`
staged builds, glass cards with selective `glow`. **Content unchanged** (same
slides, same words; the stale grading slide is left as-is for Workstream A). Goal:
a fully-realised example that demonstrates the system and anchors the later rollout.

## 6. Testing / verification

No automated tests exist (repo convention). Verification is **visual**, via:
- `pnpm dev:lecture lectures/content/slides/L01_Course_Orientation.md` — pilot look,
  click-through of all staged builds.
- `pnpm dev:staging` — smoke-check that the theme changes (esp. `section.vue`,
  global font) don't regress other decks.
- Manual `prefers-reduced-motion` check (DevTools emulation) — animations settle to
  static end-states.
- Mobile/coarse-pointer check — heavy effects disabled, content intact.

Record before/after screenshots of the L01 cover + one section divider for the
approval message.

## 7. Risks & mitigations
- **`section.vue` change is deck-wide.** Mitigate: keep the markup contract
  identical; smoke-test via staging; the new look is content-agnostic.
- **New display font shifts every heading's metrics** (line wraps, overflow).
  Mitigate: staging smoke-test; conservative size/tracking; PT Serif body keeps
  most text metrics stable.
- **Over-animation / distraction.** Mitigate: effects are opt-in per element;
  reduced-motion guards; restrained defaults on shared layouts.
- **Perf (blur/gradient layers).** Mitigate: reuse cover.vue's discipline
  (`will-change`, compositor-friendly props, mobile disable).

## 8. Decomposition & next steps
Terminal step of brainstorming: on spec approval, invoke `superpowers:writing-plans`
to produce the implementation plan. Recommended build order:
1. Tokens (palette + type) + font wiring — foundation, low risk.
2. `animations.css` (lift existing patterns first, then add new effects).
3. `section.vue` upgrade → smoke-test on staging.
4. `fact`/`statement` enhance + `metric` new layout.
5. L01 pilot re-author → visual verification → before/after screenshots.
6. Owner review of pilot → (later cycle) rollout, starting with L09.

## 9. Open questions (non-blocking)
- Exact Space Grotesk weights to import (600/700 assumed) vs. bundle size.
- Whether to also refactor the video deck / L06 inline `<style>` blocks to consume
  the new shared classes now, or defer to rollout (default: defer — out of scope).
- Whether `metric.vue` is worth a dedicated layout or is better as a utility class
  (decide during implementation from L01's actual needs).

## 10. Change log
- **2026-07-01** — Spec drafted from theme survey + approved direction (bold/kinetic,
  Space-Grotesk+PT-Serif, cyan/violet/amber, L01 pilot). Awaiting author review.
