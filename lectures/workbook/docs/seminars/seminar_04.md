# Seminar 4 — Tame a Messy Project from the Command Line ⚡

**Paired lecture:** 04 Command Line & File Handling · **Format:** hackathon · **~90 min**

> **Running project — this session adds:** a clean `raw/`–`processed/` structure,
> tidy filenames, and CLI-only inspection of the data.

## Goal
Do real work on the dataset **without a mouse**: inspect, filter, and count with
shell pipelines, and lock in a sane directory structure.

## Prerequisites
Seminar 3.

## Tasks
1. From the project root, explore with the shell only:
   - First/last rows: `head`, `tail`. The header: `head -1`.
   - How many events have positive total charge? Build a pipeline:
     `grep`, `cut`/`awk`, `sort`, `uniq -c`, `wc -l`.
2. Extract a small sample for fast iteration:
   `head -1000 data/raw/*.csv > data/processed/sample_1000.csv`.
3. Confirm your structure is clean: `raw/` read-only inputs, `processed/`
   derived files, no spaces or `final_final` in any name. Rename anything messy.
4. Save the exact commands you used into `scripts/explore.sh` with comments.

## Stretch goals
- One-liner: the maximum invariant mass in the file (hint: `cut`/`awk` the `M`
  column, `sort -g`, `tail -1`).
- Use `find` to list every file larger than 1 MB in the project.

## Solution notes (instructor)
The deliverable is `scripts/explore.sh` — a **re-runnable record** of the
exploration. That's the difference between a scriptable and a click-based
workflow (revisit the reproducibility MCQ from the lecture).

## Aims practised
⚙️ do it once, then script it · 📁 clean structure · 🔧 portable shell tools
