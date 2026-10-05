# Python runner blocks — style recipe

A runner block is a Python snippet the lecturer can run live on the slide
(Pyodide in the browser: nothing to install, but it needs internet). One
look across the course: a framed cell with a `PYTHON` header and a ▶ button,
the code, and the output under a hairline in the same frame. This page says
how to write one. The look itself is automatic, so don't restyle a block on
a slide.

## When to use one

- **Runner**: any short snippet whose result is the point of the slide (a
  number, a printed table, a small plot).
- **Static ` ```text `**: a terminal session or a printed result shown as is.
- **Static ` ```python `**: code that cannot run in the browser, such as
  reading or writing files on the student's disk, `input()`, `subprocess`,
  threads, network calls, or anything longer than about 12 lines.

## The fence

````md
```py {monaco-run} {autorun:false}
print(0.1 + 0.2)          # 0.30000000000000004
print(0.1 + 0.2 == 0.3)   # False
```
````

- Always `{autorun:false}`. The block waits for ▶, and nothing runs while
  the slides load.
- Use the language `py` (or `python`). Both are registered in
  `setup/shiki.ts`, and a new alias has to be added there first.

## The code

1. **Print what you want to show.** A block runs as a script, not in the
   REPL, so a bare expression on the last line prints nothing.
2. **Put the result in a trailing comment** (`# 0.30000000000000004`). The
   slide then reads correctly unrun (PDF export, handout, a slow projector),
   and the run confirms it. Compute the value, don't guess it.
3. **Every line fits its editor.** Monaco scrolls sideways instead of
   wrapping, so a long line is cut off at the frame on the projector.
   In a half-width card (`grid-2`) that is about **50 characters**, full
   width in a card about **115**, and about 120 with no card around it.
   `pnpm qa` fails a slide whose code is wider than its editor. Shorten the
   comment first.
4. **About 10 lines at most.** A plotting block (matplotlib) also keeps to
   about 10 lines, so that its figure fits in the output box.
5. **One block, one idea, self-contained.** All blocks of a deck share one
   Python session in the order they are run. The lecturer may skip a slide,
   so don't rely on a variable from an earlier block. Import what you use.
6. **A runner is its own panel.** Don't wrap a block alone in a card: the
   card's frame and the cell's frame then sit 20px apart with nothing between
   them. A card holds a runner only together with text.
7. **A block that shows an error names it on the slide**, in the title
   ("Fix It — NameError") or in a comment (`total = "3" + 4   # TypeError`).
   Then `pnpm qa:runners` treats that error as the expected result. Any
   other error fails the check.

## Packages

Pyodide's own packages (numpy, matplotlib, pandas, scipy, scikit-learn, …)
load by themselves from the block's `import`. Any other package and any shared
setup go in the deck's cover frontmatter. The runner reads them from slide 1:

```yaml
python:
  installs: ["termcolor"]      # PyPI packages (micropip)
  prelude: |
    import numpy as np         # runs once, before the first block
```

The runner needs internet in the lecture room: Pyodide 0.26.4 (about
10 MB) and its packages load from cdn.jsdelivr.net, also in the offline
`--keep-videos` build. The first ▶ in a deck waits a few seconds for that
download, and the status row says `Running...` in the meantime. Press one ▶
before the lecture starts so that Pyodide is already loaded.

## Room on the slide

`pnpm qa` measures a slide before anything runs. At that point the runner
shows a status row (`CLICK THE PLAY BUTTON TO RUN THE CODE`, 1.25rem). After
▶, the output replaces that row: 0.9rem of padding plus 17px (1.06rem) for
each printed line, the same line height as the code. The box stops growing
at 11rem and scrolls after that. Leave that room under the block, or the
output pushes the slide's last card past the frame. `pnpm qa:runners` runs
every block and fails a slide that overflows with its output open.

A block that fills the slide (the two 18-line blocks of L16, "The Training
Loop in NumPy" and "Generating Text") gets a fixed output height on the
fence instead: `{autorun:false, outputHeight:'4.8rem'}`. A height of
0.45rem + N × 17px + 1px shows N whole rows, and the rest scroll inside the
box; 4.8rem is four rows. The fixed height also holds before ▶, so
`pnpm qa` measures the slide at its full height.

## What lives where

| Piece | File |
|---|---|
| Frame, header label, ▶ position, output box (11rem cap, scroll), error colour | `lectures/content/theme/styles/monaco.css` |
| Editor behaviour: no hover or suggestion pop-ups, current line only while typing, thin scrollbars | `lectures/content/setup/monaco.ts` |
| Code colours, cursor, selection and scrollbar colours | `lectures/content/setup/shiki.ts` |
| matplotlib figures in the output; tracebacks trimmed to the student's frames | `lectures/content/setup/code-runners.ts` |
| One output row per printed line (upstream added a blank row after each `print`) | `patches/slidev-addon-python-runner@0.1.3.patch` |
| Run every block, check errors and fit | `scripts/check-runners.mjs` (`pnpm qa:runners`) |

## Checks

```bash
pnpm qa --only <slug>            # fits unrun, no code wider than its editor
pnpm qa:runners --only <slug>    # runs every block: no unexpected error, fits with output open
```

`pnpm qa:runners` downloads Pyodide from the jsDelivr CDN, so it is not part
of CI. Run it after adding or editing a runner block.
