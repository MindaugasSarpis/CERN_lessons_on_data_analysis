/**
 * Course-wide Mermaid look: the landing page's design language (tokens in
 * theme/styles/tokens.css, spec docs/superpowers/specs/2026-10-05-decks-match-
 * landing-design.md). Near-transparent nodes with a 1px hairline edge on the
 * near-black backdrop, Space Grotesk labels in --fg, --dim connectors, edge
 * labels on a --bg chip, subgraph frames dashed hairlines. The one
 * accent (#7dd3fc) marks inputs / highlighted nodes; --warn and --ok carry
 * meaning only (checks, results). No gradients, glows or drop shadows.
 *
 * WHY HERE and not in CSS: Slidev renders every mermaid fence into a shadow
 * root, so page CSS never reaches the SVG. The only levers are the mermaid
 * config — `themeVariables` for colours and `themeCSS`, which mermaid injects
 * into the SVG's own <style> (scoped under the diagram's #id). Slidev passes
 * `theme: 'dark'` per fence (the deck is colorSchema dark) and merges it over
 * this object, so the base theme is always `dark`; everything below overrides
 * its variables.
 *
 * Label METRICS (font, weight, letter-spacing) must match the measuring rules
 * in theme/styles/mermaid-styles.css: mermaid sizes the boxes in the light DOM
 * before the SVG moves into the shadow root (clipped text otherwise).
 *
 * Semantic classDefs written in the slides (input / process / output / check /
 * bad and their aliases, see theme/mermaid-config.md) still spell out the old
 * navy fills. Mermaid writes a classDef as an INLINE `style="… !important"`
 * on the shape, which no stylesheet can outrank, so setup/transformers.ts strips
 * fill / stroke / color from those classDefs in the markdown at build time,
 * and the `.node.<class>` rules in themeCSS colour them instead. Slide sources
 * need no edits; classDefs with other names (L03's outline-only black box) are
 * left alone.
 *
 * Per-diagram `%%{init: …}%%` colour blocks are unnecessary — leave them out.
 */
// No @slidev/types import (not hoisted under pnpm — see shiki.ts);
// defineMermaidSetup is an identity helper, a plain default export works.
type MermaidConfig = Record<string, any>

// Tokens (mirror theme/styles/tokens.css — the shadow root cannot read var()s
// reliably across mermaid's colour maths, so they are spelled out here).
const bg = '#050507'
const fg = '#f2f5f9'
const fg2 = '#c3ccd8'
const dim = '#8b97a6'
const accent = '#7dd3fc'
const warn = '#fbbf24'
const ok = '#2dd4bf'
const bad = '#f87171'          // failures only (no token: a dead end must read)
// A hairline that stays visible on #050507 (--hair at .18 vanishes on a projector).
const hair = 'rgba(139, 151, 166, 0.45)'
const hairSolid = '#3a4350'    // solid twin for mermaid's colour maths
const panel = 'rgba(255, 255, 255, 0.02)'
const panelSolid = '#0a0a0c'   // #050507 + 2 % white, for colour maths

// Git branches: the accent first, then muted hues that still tell lanes apart.
// Course colours first (no violet/pink: one accent + the two semantic hues + neutrals).
const branch = ['#7dd3fc', '#e5e7eb', '#2dd4bf', '#fbbf24', '#94a3b8', '#bae6fd', '#99f6e4', '#fde68a']

const font = "'Space Grotesk', system-ui, -apple-system, 'Segoe UI', sans-serif"
const mono = "'Space Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

const semantic = (classes: string[], stroke: string, text = fg) => {
  const sel = (tail: string) => classes.map(c => `.node.${c} ${tail}`).join(', ')
  return `
  ${sel('> rect')}, ${sel('> polygon')}, ${sel('> circle')}, ${sel('> ellipse')}, ${sel('> path')},
  ${sel('> g > rect')}, ${sel('> g > path')} {
    fill: ${panel} !important;
    stroke: ${stroke} !important;
  }
  ${sel('span')}, ${sel('.nodeLabel')}, ${sel('p')} { color: ${text} !important; }`
}

const branchCSS = branch.map((c, i) => `
  .branchLabelBkg.label${i} { fill: ${bg}; stroke: ${c}; stroke-width: 1px; }
  .branch-label${i}, .branch-label${i} text { fill: ${c}; }`).join('')

const themeCSS = `
  /* ---- flowchart nodes: hairline panels, no glow ---- */
  .node rect, .node polygon, .node circle, .node ellipse, .node path {
    fill: ${panel};
    stroke: ${hair};
    stroke-width: 1px;
    filter: none;
  }
  .node rect { rx: 5px; ry: 5px; }
  .node .label, .nodeLabel {
    font-family: ${font};
    font-weight: 500;
    letter-spacing: 0.01em;
    color: ${fg};
  }
  .node .label p, .nodeLabel p { margin: 0; }
  ${semantic(['input', 'action', 'highlight', 'accent'], accent)}
  ${semantic(['output', 'good', 'success'], ok)}
  ${semantic(['check', 'decision', 'warning', 'warn'], warn)}
  ${semantic(['bad', 'fail', 'error'], bad)}
  ${semantic(['process', 'step', 'stage'], hair)}

  /* ---- connectors: thin, dim ---- */
  .edgePath .path, .flowchart-link, path.path {
    stroke: ${dim};
    stroke-width: 1.25px;
    stroke-linecap: round;
    stroke-linejoin: round;
    filter: none;
  }
  .marker, .marker path { fill: ${dim}; stroke: ${dim}; }
  /* Edge labels as small --bg chips. Label-less edges still emit an empty
     <span class="edgeLabel"> inside a .labelBkg div — keep those invisible. */
  .edgeLabel, .labelBkg, .edgeLabel p { background: transparent !important; }
  .edgeLabel span.edgeLabel:not(:empty) {
    display: inline-block;
    padding: 0.1em 0.6em;
    border-radius: 4px;
    border: 1px solid ${hair};
    background: ${bg} !important;
    color: ${fg2};
    font-family: ${font};
    font-weight: 500;
    font-size: 0.85em;
    letter-spacing: 0.01em;
  }
  .edgeLabel span.edgeLabel:not(:empty) p { margin: 0; background: transparent !important; }

  /* ---- subgraph clusters: open hairline frames, label as a kicker ---- */
  .cluster rect {
    fill: transparent !important;
    stroke: ${hair} !important;
    stroke-width: 1px !important;
    stroke-dasharray: 4 4;
    rx: 6px; ry: 6px;
  }
  .cluster-label .nodeLabel, .cluster text {
    font-family: ${font};
    font-weight: 500;
    letter-spacing: 0.01em;
    fill: ${dim}; color: ${dim};
  }

  /* ---- sequence diagrams ---- */
  .actor { stroke-width: 1px; filter: none; }
  text.actor > tspan { font-family: ${font}; font-weight: 500; fill: ${fg}; }
  .messageLine0, .messageLine1 { stroke-width: 1.25px; stroke-linecap: round; }
  .messageText { font-family: ${font}; font-weight: 500; }
  .note { stroke-width: 1px; }
  .noteText, .noteText > tspan { font-family: ${font}; }
  .labelBox { stroke-width: 1px; }
  .labelText, .labelText > tspan, .loopText, .loopText > tspan { font-family: ${font}; font-weight: 500; }
  .loopLine { stroke-dasharray: 4 4; }

  /* ---- gitGraph: thin lanes, outlined branch chips, mono hashes ---- */
  .commit { filter: none; }
  .arrow { stroke-width: 3px; stroke-linecap: round; }
  .branch { stroke: ${hairSolid}; stroke-width: 1px; stroke-dasharray: 3 4; }
  .branch-label, .branchLabel text { font-family: ${font}; font-weight: 500; }
  .commit-label { font-family: ${mono}; fill: ${fg2}; }
  .commit-label-bkg { fill: ${bg}; opacity: 1; }
  .tag-label { font-family: ${mono}; }
  ${branchCSS}

`

// Slidev calls this once (a singleton promise) before the first render.
export default (): MermaidConfig => ({
  theme: 'dark',
  // Mermaid 12 defaults to the ELK layout and the `neo` look (gradient strokes,
  // shadows), which re-lays out every diagram and fights the hairline style
  // below. Keep the dagre layout and the classic look the slides were sized for.
  layout: 'dagre',
  look: 'classic',
  themeVariables: {
    fontFamily: font,
    fontSize: '16px',
    darkMode: true,

    // flowchart
    primaryColor: panelSolid,
    primaryTextColor: fg,
    primaryBorderColor: hairSolid,
    secondaryColor: panelSolid,
    secondaryTextColor: fg,
    secondaryBorderColor: hairSolid,
    tertiaryColor: panelSolid,
    tertiaryTextColor: fg,
    tertiaryBorderColor: hairSolid,
    lineColor: dim,
    defaultLinkColor: dim,
    textColor: fg,
    mainBkg: panelSolid,
    nodeBkg: panelSolid,
    nodeBorder: hairSolid,
    nodeTextColor: fg,
    clusterBkg: bg,
    clusterBorder: hairSolid,
    titleColor: fg,
    edgeLabelBackground: bg,
    background: bg,

    // sequence
    actorBkg: panelSolid,
    actorBorder: hairSolid,
    actorTextColor: fg,
    actorLineColor: hairSolid,
    signalColor: dim,
    signalTextColor: fg,
    labelBoxBkgColor: bg,
    labelBoxBorderColor: hairSolid,
    labelTextColor: fg,
    loopTextColor: dim,
    noteBkgColor: bg,
    noteBorderColor: warn,
    noteTextColor: fg,
    activationBkgColor: panelSolid,
    activationBorderColor: accent,
    sequenceNumberColor: bg,

    // gitGraph — lanes cycle through `branch`; chips are restyled in themeCSS
    git0: branch[0], git1: branch[1], git2: branch[2], git3: branch[3],
    git4: branch[4], git5: branch[5], git6: branch[6], git7: branch[7],
    gitInv0: bg, gitInv1: bg, gitInv2: bg, gitInv3: bg,
    gitInv4: bg, gitInv5: bg, gitInv6: bg, gitInv7: bg,
    gitBranchLabel0: bg, gitBranchLabel1: bg, gitBranchLabel2: bg, gitBranchLabel3: bg,
    gitBranchLabel4: bg, gitBranchLabel5: bg, gitBranchLabel6: bg, gitBranchLabel7: bg,
    commitLabelColor: fg2,
    commitLabelBackground: bg,
    commitLabelFontSize: '13px',
    tagLabelColor: bg,
    tagLabelBackground: warn,
    tagLabelBorder: warn,
    tagLabelFontSize: '13px',

    // pie — accent first, then the muted branch hues
    pie1: branch[0], pie2: branch[1], pie3: branch[2], pie4: branch[3],
    pie5: branch[4], pie6: branch[5], pie7: branch[6], pie8: branch[7],
    pieTitleTextColor: fg,
    pieSectionTextColor: bg,
    pieLegendTextColor: fg,
    pieStrokeColor: bg,
    pieOuterStrokeColor: bg,
  },
  themeCSS,
  flowchart: {
    curve: 'basis',
    htmlLabels: true,
    useMaxWidth: true,
    nodeSpacing: 40,
    rankSpacing: 48,
    padding: 14,
    // Mermaid 12 wraps labels at 120px and widens every node to 120px; the
    // slides were laid out with mermaid 11's 200px wrap and content-sized nodes.
    wrappingWidth: 200,
    minNodeWidth: 0,
  },
  sequence: {
    useMaxWidth: true,
    mirrorActors: false,
    actorMargin: 60,
    messageMargin: 40,
    boxMargin: 12,
  },
  gitGraph: {
    useMaxWidth: true,
  },
})
