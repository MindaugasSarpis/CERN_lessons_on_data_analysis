// Slidev monaco setup: editor options for every `{monaco-run}` block.
// (No @slidev/types import — not hoisted under pnpm; a plain function works
// the same as defineMonacoSetup.) Colours are in setup/shiki.ts, the frame
// and the output box in theme/styles/monaco.css. The style rules for runner
// slides: docs/python-runner-recipe.md.
export default () => ({
  editorOptions: {
    // a faint current-line band only while someone is typing
    renderLineHighlight: 'line',
    renderLineHighlightOnlyWhenFocus: true,
    // a long line or a grown snippet scrolls inside the editor; thin bars,
    // and the wheel goes back to the page once the editor reaches its end
    scrollbar: {
      verticalScrollbarSize: 6,
      horizontalScrollbarSize: 6,
      useShadows: false,
      alwaysConsumeMouseWheel: false,
    },
    // no hover popups or suggestion widgets over the code on a projector
    hover: { enabled: 'off' },
    quickSuggestions: false,
    suggestOnTriggerCharacters: false,
    parameterHints: { enabled: false },
    contextmenu: false,
    occurrencesHighlight: 'off',
    selectionHighlight: false,
    matchBrackets: 'near',
    guides: { indentation: false },
    fontLigatures: false,
    cursorBlinking: 'smooth',
  },
})
