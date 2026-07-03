# The Running Project

Every seminar adds one layer to **the same** analysis project. By the end you own
one clean, versioned, automated, documented repository that embodies the course's
four aims — 🔧 tool-agnostic, ♻️ reproducible, ⚙️ automated, 📁 well-organised data.

## Pick your dataset — two tracks

The skills are identical whichever you choose. **Pick the one that fits your
background:**

### 🅰 The physics track — LHCb dimuon events *(the default)*

A real **CERN Open Data** teaching set: dimuon (μ⁺μ⁻) events recorded by the
**LHCb** experiment. Each row is one event in which two muons were detected; the
columns give each muon's momentum components and the reconstructed
**invariant mass `M`** of the pair.

- Source: CERN Open Data Portal — the LHCb dimuon education sample (a plain CSV,
  tens of thousands of rows). The exact record, DOI and download link are found
  and recorded in **Seminar 2**.
- Typical columns: `E1, px1, py1, pz1, Q1, E2, px2, py2, pz2, Q2, M` (energies /
  momenta in GeV).
- Why it's great: a plain CSV (works with every tool), real physics, and its
  invariant-mass spectrum contains famous **resonance peaks** —
  J/ψ (~3.10 GeV), ψ(2S) (~3.69 GeV), Υ (~9.46 GeV) — so there is a genuine
  signal to find, fit, and classify.

### 🅱 The bring-your-own track — a dataset from *your* field

Students come from many faculties, so you may instead use a **tabular dataset
from your own discipline** — the four aims and every step below apply unchanged.
Good candidates have a few thousand+ rows and at least one numeric column with
interesting structure:

- 🌦️ **environment** — daily weather (temperature, rainfall) over years
- 💶 **economics / business** — prices, sales, energy consumption
- 🧬 **life sciences** — measurements per sample/patient (anonymised)
- 🗳️ **social science** — public survey / census microdata
- 🏃 **your own** — anything you have measured or can download openly

Wherever the physics track says "invariant mass / resonance peak", read it as
"your numeric variable / the pattern you're looking for". Clear this choice with
the instructor in Seminar 2.

> Offline or the portal is down? Any tabular CSV works; the instructor can
> provide a local copy of the LHCb sample.

## The repository you will build

```text
analysis-project/       # name it after your data (e.g. dimuon-analysis)
|- README.md            # what this is, data provenance, how to rebuild (S5)
|- data/
|  |- raw/              # the CSV exactly as downloaded — READ ONLY (S2, S4)
|  |- processed/        # cleaned tables, produced by scripts only (S13)
|- scripts/            # one script per pipeline step (S7-S16)
|- results/            # figures and numbers, all regenerable (S10-S12)
|- environment.yml / requirements.txt   # pinned dependencies (S14)
|- Makefile            # `make all` rebuilds everything (S14)
```

**The golden rule:** you could delete everything except `data/raw/` and `scripts/`
and rebuild the whole project with one command. If that's true, you've succeeded.

## What each seminar adds

| Seminar | Layer added to the project |
|--|--|
| 1 | Toolkit installed; empty repo + skeleton + first commit |
| 2 | Dataset downloaded into `data/raw/`; provenance recorded |
| 3 | You understand the raw file as bytes (encoding, size, format) |
| 4 | `raw/`–`processed/` structure; clean filenames; CLI inspection |
| 5 | A real `README.md` (provenance, columns, units, rebuild steps) |
| 6 | Project under Git; a feature branch made and merged |
| 7 | First parsing: one event line → numbers |
| 8 | Ingest script: whole CSV read into Python (no Pandas) |
| 9 | Data-quality audit applied (missing, duplicate, impossible values) |
| 10 | First committed figure (physics: the dimuon mass spectrum) |
| 11 | A measurement with an uncertainty (a value ± SE) |
| 12 | A fit: a peak/curve model → parameter ± error, χ² |
| 13 | Clean, tidy `processed/` table produced with Pandas |
| 14 | One-command reproducible rebuild (environment + Makefile) |
| 15 | The pipeline run as a batch/remote-style job, at scale *(optional)* |
| 16 | A trained + honestly-evaluated classifier *(optional)* |
