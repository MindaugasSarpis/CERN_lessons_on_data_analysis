# Seminar 14 — Make It Reproducible: Environment + Makefile ⚡

**Paired lecture:** 14 Reproducible Workflows & Automation · **Format:** hackathon · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

> **Running project — this session adds:** a one-command rebuild of the entire
> analysis from raw data.

## Goal
Turn your pile of scripts into a **pipeline** anyone can reproduce with a single
command, in a pinned environment.

## Prerequisites
Seminars 8–13 (ingest → clean → plot → fit scripts exist).

## Tasks
1. Capture the environment: `pip freeze > requirements.txt` (or an
   `environment.yml`). Pin versions.
2. Write a `Makefile` with targets that encode the dependencies:
   `clean.py → events_clean.parquet`, `plot_spectrum.py → mass_spectrum.png`,
   `fit_peak.py → fit results`. Add an `all` target and a `clean` target.
3. Wipe `processed/` and `results/`, then run `make all` — everything rebuilds
   from `data/raw/` alone.
4. Update the README's **How to rebuild** section to: "create the env, then `make all`".
5. Audit your project against the lecture's **FAIR** principles: is it Findable (a
   README on top, provenance from Seminar 2), Accessible (open CSV/parquet), Interoperable
   (standard units, plain-text formats), Reusable (licence noted, environment pinned)?
   Note one gap in the README and fix it if time allows.
6. Tag this reproducible milestone in Git: `git tag -a v1.0-pipeline -m "One-command
   rebuild from raw data"` — a durable reference point any collaborator can check out.

## Stretch goals
- Add a `make test` that runs a quick sanity check (e.g. row count > 0).
- Seed every random step so results are bit-for-bit reproducible.
- Time the full `make all` rebuild and record it in the README — a future regression
  here is an early warning sign.

## Wrap-up (last 10 min)
- Run `make clean && make all` once more, live, in front of your neighbour — the
  ultimate proof this reproduces ♻️.
- Commit everything (`git add -A && git commit -m "One-command reproducible
  pipeline"`) and make sure your tag is in `git tag`.
- Note one lesson in the README, e.g. the one dependency you forgot to pin until
  `make all` failed on a clean checkout.

## Solution notes (instructor)
The acceptance test: delete everything except `raw/` and `scripts/`, run one
command, get all results back. This is the whole course's thesis in one seminar —
♻️ + ⚙️ made concrete. In the 120-minute slot, protect task 3's clean rebuild as the
anchor demo — if a group is behind, cut task 6's tagging before you'd ever cut the
rebuild itself.

## Aims practised
♻️ reproducible from raw · ⚙️ automated pipeline · 📁 raw is the single source of truth
