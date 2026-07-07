# Seminar 4 — Tame a Messy Project from the Command Line ⚡

**Paired lecture:** 04 Command Line & File Handling · **Format:** hackathon · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

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
5. Compute a column statistic in pure shell — the mean of the mass column
   (find its field number in the header first):
   ```bash
   head -1 data/raw/*.csv | tr ',' '\n' | nl                     # which field is M?
   awk -F, 'NR>1 {s+=$5; n++} END {print s/n}' data/raw/*.csv    # adjust $5
   ```
6. Turn `scripts/explore.sh` into a real tool: `#!/usr/bin/env bash` on line 1,
   `chmod +x scripts/explore.sh`, then run it top-to-bottom with
   `./scripts/explore.sh` from the project root — every command must still work.

## Stretch goals
- One-liner: the maximum invariant mass in the file (hint: `cut`/`awk` the `M`
  column, `sort -g`, `tail -1`).
- Use `find` to list every file larger than 1 MB in the project.
- Draw a terminal histogram of the mass column: bucket values with `awk`, count
  with `sort | uniq -c`, and print `#` bars — a sneak preview of Seminar 10.

## Wrap-up (last 10 min)
- Run `./scripts/explore.sh` once more in a fresh shell — identical output means
  the exploration is truly re-runnable, not a one-off click trail.
- Commit the script and sample: `git add -A && git commit -m "Scripted CLI exploration"`.
- Note in the README which pipeline trick you expect to reuse most.

## Solution notes (instructor)
The deliverable is `scripts/explore.sh` — a **re-runnable record** of the
exploration. That's the difference between a scriptable and a click-based
workflow (revisit the reproducibility MCQ from the lecture). Across 120 minutes,
task 5's `awk` mean is the common stall — put the `-F,` flag and the
header-numbering one-liner on the board early rather than letting groups burn
15 minutes on it.

## Aims practised
⚙️ do it once, then script it · 📁 clean structure · 🔧 portable shell tools
