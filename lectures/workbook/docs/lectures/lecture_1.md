# 1: Orientation & Motivation

Lecture 1 is the *why*: who is in the room, then a motivation reel that runs
from the cosmos down to a particle track and into the LHC tunnels, and after
the break how the course works and what you are graded on.
Lecture 2 is the *what*: data itself.

## What the lecture covers

1. **Introductions** — a Google Earth pull-back from the Physics Faculty to the
   cosmos as the cold open, then a show of hands:
   your field, your operating system, whether you have written code before.
2. **Logistics** — lectures and seminars, the 16-lecture map in five blocks, and
   the weekly schedule (lecture only in week 1; lecture + seminar every Tuesday
   from week 2).
3. **The reel** — from the cosmos to the quantum: a drone ascent, Cassini at
   Saturn, Mars, telescopes and the expanding universe, then down to plasma,
   atoms and a cloud chamber.
4. **What is CERN** — four slides (the organisation, the LHC, the accelerator
   chain, how a detector sees a collision), then the CERN clips: the site,
   the ATLAS shaft and cavern, LHCb, the FCC — with time to talk about them.
5. **Why you need these skills** — CERN's toolkit is this course's toolkit.
   *Break.*
6. **The four aims** — 🔧 tool-agnosticism, ♻️ reproducibility, ⚙️ automation,
   📁 efficient work with data & files — each as a before/after pair drawn from
   real projects, and how they reinforce each other.
7. **Grading and your project** — one course-long project of your own choice,
   graded on the four aims; deliverables: repository, one-page report, short
   video, final presentation.
8. **How this course works** — the lecture/seminar week, what "done" looks like
   each week, how to succeed, what the course is not.
9. **Seminars & your project** — why real, open data; what the sixteen seminars
   cover; the project tree and the golden rule.
10. **Homework** before next Tuesday.

## Before next Tuesday (there is no seminar in week 1)

Install three tools and prove they work:

- **Python 3.10+** — [python.org](https://python.org) (conda or any equivalent works)
- **VS Code** — [code.visualstudio.com](https://code.visualstudio.com)
- **Git** — [git-scm.com](https://git-scm.com)

```bash
python --version   # or python3
git --version
code --version
```

Three version numbers means you are done; then create an empty `analysis-project`
folder. Seminar 1's brief is **self-paced**: work through it at home. We check it
together during the first 40 minutes of Seminar 2 on 15 September, then go
straight on to the first dataset. Stuck on an install? Bring the error message.

## Paired seminar

[Seminar 1 — Set Up Your Toolkit & First Repo](../seminars/seminar_01.md):
self-paced before 15 September, checked at the start of
[Seminar 2](../seminars/seminar_02.md).

## Take-aways

- The whole grade is one project of your own; the seminars teach the moves, the
  project is where you make them yours.
- Reproducible means data, code and environment recorded together — a plot on
  its own is not a result.
- Once by hand, twice by script.
- The golden rule: delete everything but `data/raw/` and `scripts/`, and rebuild
  it all with one command.
