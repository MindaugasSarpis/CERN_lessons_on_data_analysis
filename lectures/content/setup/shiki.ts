// Slidev shiki setup (no @slidev/types import — not hoisted under pnpm;
// defineShikiSetup is an identity helper, a plain function works the same).
//
// Slidev's RUNTIME (Monaco) highlighter only bundles its default languages
// (markdown, vue, js, ts, html, css) — static fences are highlighted at build
// time with the full grammar set, but `{monaco-run}` editors tokenize at
// runtime and rendered monochrome for python. Register the grammars our
// interactive blocks actually use.
export default () => ({
  langs: [
    'markdown', 'vue', 'javascript', 'typescript', 'html', 'css',
    // 'py' too: monaco registers language ids verbatim from this list, and
    // our fences say ```py — without the alias the tokenizer never attaches.
    'python', 'py', 'bash', 'yaml', 'json',
  ],
})
