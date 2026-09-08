/**
 * Course-wide Mermaid look — "kinetic glass", the same language as the card
 * system in theme/styles/custom-slides.css: deep-navy translucent nodes with a
 * luminous cyan edge and a soft glow, teal connectors, Space Grotesk labels,
 * amber for decisions, emerald for outputs, red for failures.
 *
 * WHY HERE and not in CSS: Slidev renders every mermaid fence into a shadow
 * root, so page CSS never reaches the SVG. The only levers are the mermaid
 * config — `themeVariables` for colours and `themeCSS`, which mermaid injects
 * into the SVG's own <style>. Slidev passes `theme: 'dark'` per fence (the
 * deck is colorSchema dark) and merges it over this object, so the base theme
 * is always `dark`; everything below overrides its variables.
 *
 * Per-diagram `%%{init: …}%%` blocks are therefore unnecessary — leave them
 * out. Semantic node colours come from a small set of classDefs documented in
 * theme/mermaid-config.md (input / process / output / check / bad …).
 */
// No @slidev/types import (not hoisted under pnpm — see shiki.ts);
// defineMermaidSetup is an identity helper, a plain default export works.
type MermaidConfig = Record<string, any>

// Palette (mirrors --color-* / --accent-* in custom-slides.css)
const ink = '#020617'          // page black
const navy = '#0a1f3f'         // node fill (glass, see fill-opacity below)
const navyDeep = '#08172f'
const navyMid = '#0b2d4d'
const text = '#e8f1ff'
const textSoft = '#cbd5e1'
const cyan = '#22d3ee'         // connectors, glow
const sky = '#38bdf8'          // node borders
const teal = '#5eead4'
const violet = '#a78bfa'
const amber = '#fbbf24'
const emerald = '#34d399'
const rose = '#f472b6'
const red = '#f87171'
const blue = '#60a5fa'

const font = "'Space Grotesk', Inter, system-ui, -apple-system, 'Segoe UI', sans-serif"

const themeCSS = `
  /* ---- flowchart nodes: glass slabs with a luminous edge ---- */
  .node rect, .node polygon, .node circle, .node ellipse, .node path {
    stroke-width: 1.5px;
    fill-opacity: 0.82;
    filter: drop-shadow(0 0 6px rgba(56, 189, 248, 0.35)) drop-shadow(0 8px 18px rgba(2, 6, 23, 0.6));
  }
  .node rect { rx: 14px; ry: 14px; }
  .node .label, .nodeLabel {
    font-family: ${font};
    font-weight: 600;
    letter-spacing: 0.01em;
  }
  .node .label p, .nodeLabel p { margin: 0; }

  /* ---- connectors: thin, teal, rounded, glowing ---- */
  .edgePath .path, .flowchart-link, path.path {
    stroke-width: 2px;
    stroke-linecap: round;
    stroke-linejoin: round;
    filter: drop-shadow(0 0 3px rgba(34, 211, 238, 0.55));
  }
  .marker, .marker path { fill: ${cyan}; stroke: ${cyan}; }
  /* Edge labels as small chips. Label-less edges still emit an empty
     <span class="edgeLabel"> inside a .labelBkg div — keep those invisible. */
  .edgeLabel, .labelBkg, .edgeLabel p { background: transparent !important; }
  .edgeLabel span.edgeLabel:not(:empty) {
    display: inline-block;
    padding: 0.1em 0.7em;
    border-radius: 999px;
    border: 1px solid rgba(34, 211, 238, 0.4);
    background: ${ink} !important;
    color: #a5f3fc;
    font-family: ${font};
    font-weight: 600;
    font-size: 0.85em;
    letter-spacing: 0.02em;
  }
  .edgeLabel span.edgeLabel:not(:empty) p { margin: 0; background: transparent !important; }

  /* ---- subgraph clusters: faint dashed glass panels ---- */
  .cluster rect {
    fill: rgba(56, 189, 248, 0.06) !important;
    stroke: rgba(56, 189, 248, 0.35) !important;
    stroke-width: 1px !important;
    stroke-dasharray: 6 5;
    rx: 18px; ry: 18px;
  }
  .cluster-label .nodeLabel, .cluster text {
    font-family: ${font};
    font-weight: 700;
    font-size: 0.8em;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    fill: #7dd3fc; color: #7dd3fc;
  }

  /* ---- sequence diagrams ---- */
  .actor {
    stroke-width: 1.5px;
    fill-opacity: 0.85;
    filter: drop-shadow(0 0 6px rgba(56, 189, 248, 0.35));
  }
  text.actor > tspan { font-family: ${font}; font-weight: 600; }
  .messageLine0, .messageLine1 { stroke-width: 2px; stroke-linecap: round; }
  .messageText { font-family: ${font}; font-weight: 500; }
  .note { stroke-width: 1px; fill-opacity: 0.9; }
  .noteText, .noteText > tspan { font-family: ${font}; }
  .labelBox { stroke-width: 1.5px; }
  .labelText, .labelText > tspan, .loopText, .loopText > tspan { font-family: ${font}; font-weight: 600; }
  .loopLine { stroke-dasharray: 4 4; }

  /* ---- gitGraph ---- */
  .commit { stroke-width: 2px; filter: drop-shadow(0 0 5px rgba(34, 211, 238, 0.45)); }
  .commit-label, .branchLabel text, .label text { font-family: ${font}; font-weight: 600; }
  .arrow { stroke-width: 2px; stroke-linecap: round; }
`

export default (): MermaidConfig => ({
  theme: 'dark',
  themeVariables: {
    fontFamily: font,
    fontSize: '16px',
    darkMode: true,

    // flowchart
    primaryColor: navy,
    primaryTextColor: text,
    primaryBorderColor: sky,
    secondaryColor: navyMid,
    secondaryTextColor: text,
    secondaryBorderColor: teal,
    tertiaryColor: navyDeep,
    tertiaryTextColor: text,
    tertiaryBorderColor: violet,
    lineColor: cyan,
    defaultLinkColor: cyan,
    textColor: text,
    mainBkg: navy,
    nodeBkg: navy,
    nodeBorder: sky,
    nodeTextColor: text,
    clusterBkg: navyDeep,
    clusterBorder: '#1e3a5f',
    titleColor: text,
    edgeLabelBackground: ink,
    background: ink,

    // sequence
    actorBkg: navy,
    actorBorder: sky,
    actorTextColor: text,
    actorLineColor: '#334155',
    signalColor: cyan,
    signalTextColor: text,
    labelBoxBkgColor: navyMid,
    labelBoxBorderColor: teal,
    labelTextColor: text,
    loopTextColor: textSoft,
    noteBkgColor: '#2a2208',
    noteBorderColor: amber,
    noteTextColor: '#fef3c7',
    activationBkgColor: navyMid,
    activationBorderColor: teal,
    sequenceNumberColor: ink,

    // gitGraph — branch colours cycle through the accent set
    git0: cyan, git1: violet, git2: emerald, git3: amber,
    git4: rose, git5: blue, git6: red, git7: teal,
    gitBranchLabel0: ink, gitBranchLabel1: ink, gitBranchLabel2: ink, gitBranchLabel3: ink,
    gitBranchLabel4: ink, gitBranchLabel5: ink, gitBranchLabel6: ink, gitBranchLabel7: ink,
    commitLabelColor: text,
    commitLabelBackground: navy,
    commitLabelFontSize: '13px',
    tagLabelColor: ink,
    tagLabelBackground: amber,
    tagLabelBorder: amber,
    tagLabelFontSize: '13px',

    // pie
    pie1: cyan, pie2: violet, pie3: emerald, pie4: amber, pie5: rose, pie6: blue, pie7: red, pie8: teal,
    pieTitleTextColor: text,
    pieSectionTextColor: ink,
    pieLegendTextColor: text,
    pieStrokeColor: ink,
    pieOuterStrokeColor: ink,
  },
  themeCSS,
  flowchart: {
    curve: 'basis',
    htmlLabels: true,
    useMaxWidth: true,
    nodeSpacing: 40,
    rankSpacing: 48,
    padding: 14,
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
