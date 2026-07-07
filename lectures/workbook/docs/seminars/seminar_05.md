# Seminar 5 — Write the Project's README in Markdown

**Paired lecture:** 05 Markdown & VS Code · **Format:** hands-on · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

> **Running project — this session adds:** a real `README.md` — the front page of
> your project.

## Goal
Turn scattered notes into a `README.md` that lets a stranger (or future you)
understand and rebuild the project.

## Prerequisites
Seminars 2–4 (data + structure + provenance notes).

## Tasks
1. Using Markdown, write a `README.md` with these sections:
   - **What this is** — one paragraph.
   - **Data** — source, DOI/URL, licence, download date, and a **table of columns
     with units** (E, px… in GeV).
   - **Structure** — what lives in `raw/`, `processed/`, `scripts/`, `results/`.
   - **How to rebuild** — the steps so far (even if just "download, run explore.sh").
2. Preview it live in VS Code (`Ctrl+Shift+V`) as you write.
3. Add a short **Notes** section for known data quirks you've spotted.
4. Use the Command Palette (`Ctrl/Cmd+Shift+P` → *Markdown: Open Preview to the
   Side*) to keep source and rendered view visible together; add a
   **blockquote** flagging one open question about the data (e.g. "is the
   momentum really in GeV, or GeV/c?").
5. Add a short **math aside** using Markdown's LaTeX syntax: write out the
   invariant-mass formula behind the `M` column you'll meet in Seminar 8, e.g.
   `$M^2 = (E_1 + E_2)^2 - |\vec{p}_1 + \vec{p}_2|^2$` — a first preview of the
   physics behind the pipeline.

## Stretch goals
- Add a Markdown note of the signal you expect to find later
  (the D⁰ peak at ≈ 1865 MeV, over combinatorial background).
- Add a task list (`- [ ]`) of the remaining pipeline steps.
- Install a Markdown-linting extension (e.g. `markdownlint`) and clear every
  warning in your README — consistent heading levels, no bare URLs, blank
  lines around lists.

## Wrap-up (last 10 min)
- Preview the whole README once more (`Ctrl+Shift+V`) and fix any rendering
  glitches — a stray asterisk, a table that didn't align.
- Commit it: `git add -A && git commit -m "Write project README"`, then close
  and reopen the file in VS Code to confirm it renders identically — that's
  the reproducibility test for documentation itself.
- Note one lesson in the Notes section: which Markdown feature surprised you,
  or which sentence took longest to phrase.

## Solution notes (instructor)
A good README answers *what*, *where from*, and *how to reproduce*. Stress the
column-units table — undocumented units are the classic silent killer in data
analysis. In the 120-minute slot, task 1's full draft is the long pole — timebox
it to ~45 minutes and let the Command Palette/LaTeX tasks run in parallel for
early finishers; stragglers should nail the Data section before polishing prose.

## Aims practised
♻️ documentation enables reproduction · 🔧 Markdown works everywhere
