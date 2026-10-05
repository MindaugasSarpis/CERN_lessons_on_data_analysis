// Slidev shiki setup (no @slidev/types import — not hoisted under pnpm;
// defineShikiSetup is an identity helper, a plain function works the same).
//
// Slidev's RUNTIME (Monaco) highlighter only bundles its default languages
// (markdown, vue, js, ts, html, css) — static fences are highlighted at build
// time with the full grammar set, but `{monaco-run}` editors tokenize at
// runtime and rendered monochrome for python. Register the grammars our
// interactive blocks actually use.
//
// Token colours: a small course theme on the landing's tokens instead of
// vitesse — calm, cyan-led, and with COMMENTS READABLE on a projector: many
// decks print a line's result as a `# …` comment, so a comment is content.

const fg = '#e6ebf1'
const comment = '#a9b6c5'
const dim = '#8b97a6'
const accent = '#7dd3fc'
const fn = '#bae6fd'
const str = '#a7f3d0'
const num = '#fde68a'

const courseDark = {
  name: 'course-dark',
  type: 'dark',
  colors: {
    'editor.background': '#00000000',
    'editor.foreground': fg,
  },
  tokenColors: [
    { settings: { foreground: fg } },
    { scope: ['comment', 'punctuation.definition.comment'], settings: { foreground: comment, fontStyle: '' } },
    { scope: ['keyword', 'storage', 'storage.type', 'keyword.operator.logical', 'keyword.operator.word',
      'keyword.control', 'support.type.property-name', 'entity.name.tag', 'markup.heading', 'entity.name.section'],
      settings: { foreground: accent } },
    { scope: ['string', 'string.quoted', 'markup.inline.raw', 'markup.raw', 'string.unquoted'], settings: { foreground: str } },
    { scope: ['constant.numeric', 'constant.language', 'constant.character', 'constant.other', 'support.constant'],
      settings: { foreground: num } },
    { scope: ['entity.name.function', 'support.function', 'meta.function-call.generic', 'entity.name.type',
      'entity.name.class', 'support.class', 'support.type', 'entity.other.attribute-name'],
      settings: { foreground: fn } },
    { scope: ['punctuation', 'meta.brace', 'keyword.operator', 'punctuation.definition.list.begin.markdown',
      'punctuation.definition.heading', 'markup.list'], settings: { foreground: dim } },
    { scope: ['variable', 'variable.parameter', 'variable.other', 'meta.definition.variable'], settings: { foreground: fg } },
    { scope: ['markup.bold'], settings: { foreground: fg, fontStyle: 'bold' } },
    { scope: ['markup.italic'], settings: { foreground: fg, fontStyle: 'italic' } },
    { scope: ['markup.underline.link', 'string.other.link'], settings: { foreground: accent } },
  ],
}

export default () => ({
  themes: {
    dark: courseDark,
    light: courseDark,
  },
  langs: [
    'markdown', 'vue', 'javascript', 'typescript', 'html', 'css',
    // 'py' too: monaco registers language ids verbatim from this list, and
    // our fences say ```py — without the alias the tokenizer never attaches.
    'python', 'py', 'bash', 'yaml', 'json',
  ],
})
