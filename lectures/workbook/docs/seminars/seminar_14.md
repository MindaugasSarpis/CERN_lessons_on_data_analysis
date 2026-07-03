# Seminar 14 — Make It Reproducible: Environment + Makefile ⚡

**Paired lecture:** 14 Reproducible Workflows & Automation · **Format:** hackathon · **~90 min**

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

## Stretch goals
- Add a `make test` that runs a quick sanity check (e.g. row count > 0).
- Seed every random step so results are bit-for-bit reproducible.

## Solution notes (instructor)
The acceptance test: delete everything except `raw/` and `scripts/`, run one
command, get all results back. This is the whole course's thesis in one seminar —
♻️ + ⚙️ made concrete.

## Aims practised
♻️ reproducible from raw · ⚙️ automated pipeline · 📁 raw is the single source of truth
