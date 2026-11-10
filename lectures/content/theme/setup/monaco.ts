// The type size of every `{monaco-run}` editor, with the theme's other sizes
// (10 Nov 2026: 11.5 → 13px, for the projector and phones). Slidev merges the
// editorOptions of the theme's setup with the deck folder's own
// (lectures/content/setup/monaco.ts, which holds the behaviour and sets no
// size). The line height is fixed, not Monaco's per-platform default (1.5 ×
// on macOS, 1.35 × elsewhere), so a runner is as tall in the Linux QA as on
// the lecturer's Mac. The output box under the editor uses the same size
// and lines (styles/monaco.css).
export default () => ({
  editorOptions: {
    fontSize: 13,
    lineHeight: 20,
  },
})
