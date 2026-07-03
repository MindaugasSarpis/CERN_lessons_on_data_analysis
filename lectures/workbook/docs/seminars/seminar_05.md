# Seminar 5 — Write the Project's README in Markdown

**Paired lecture:** 05 Markdown & VS Code · **Format:** hands-on · **~90 min**

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

## Stretch goals
- Add a Markdown table of the resonance peaks you expect to find later
  (J/ψ ≈ 3.1, Υ ≈ 9.5, Z ≈ 91 GeV).
- Add a task list (`- [ ]`) of the remaining pipeline steps.

## Solution notes (instructor)
A good README answers *what*, *where from*, and *how to reproduce*. Stress the
column-units table — undocumented units are the classic silent killer in data
analysis.

## Aims practised
♻️ documentation enables reproduction · 🔧 Markdown works everywhere
