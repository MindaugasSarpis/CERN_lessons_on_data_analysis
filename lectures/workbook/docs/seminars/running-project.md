# The Running Project

Every seminar adds one layer to **the same** analysis project. By the end you own
one clean, versioned, automated, documented repository that embodies the course's
four aims — 🔧 tool-agnostic, ♻️ reproducible, ⚙️ automated, 📁 well-organised data.

## The dataset — CMS dimuon events

We use a real **CERN Open Data** teaching set: dimuon events recorded by the CMS
experiment. Each row is one event in which two muons were detected; the columns
give each muon's energy and momentum and (optionally) the reconstructed
**invariant mass `M`** of the pair.

- Source: CERN Open Data Portal (CMS education sample, e.g. `Dimuon_DoubleMu.csv`,
  ~100k rows). Download link and exact citation are recorded in Seminar 2.
- Key columns: `Run, Event, E1, px1, py1, pz1, pt1, eta1, phi1, Q1, E2, px2, py2, pz2, pt2, eta2, phi2, Q2, M`.
- Why it's great: it's a plain CSV (works with every tool), it's real physics, and
  its invariant-mass spectrum contains famous **resonance peaks** — the
  J/ψ (~3.1 GeV), Υ (~9.5 GeV) and Z boson (~91 GeV) — so there is a genuine
  signal to find, fit, and classify.

> If offline or the portal is unavailable, any tabular CSV with a numeric column
> of interest works; the instructor may provide a local copy.

## The repository you will build

```text
dimuon-analysis/
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
| 10 | First committed figure: the dimuon mass spectrum |
| 11 | A measurement with an uncertainty (mass near a peak, ± SE) |
| 12 | A fit: Gaussian + background on a resonance, mass ± error, χ² |
| 13 | Clean, tidy `processed/` table produced with Pandas |
| 14 | One-command reproducible rebuild (environment + Makefile) |
| 15 | The pipeline run as a batch/remote-style job, at scale *(optional)* |
| 16 | A trained + honestly-evaluated signal-vs-background classifier *(optional)* |
