# The Running Project

Every seminar adds one layer to **the same** analysis project. By the end you own
one clean, versioned, automated, documented repository that embodies the course's
four aims — 🔧 tool-agnostic, ♻️ reproducible, ⚙️ automated, 📁 well-organised data.

## Pick your dataset — two tracks

The skills are identical whichever you choose. **Pick the one that fits your
background:**

### 🅰 The physics track — LHCb D⁰ → K⁻π⁺ events *(the default)*

The real **LHCb open-data masterclass** set on the CERN Open Data Portal:
~60,000 events pre-selected to contain **D⁰ → K⁻π⁺** decay candidates. Each event
gives the kaon and pion momenta, from which you reconstruct the **K–π invariant
mass** — and see the D⁰ appear as a peak.

- Source: CERN Open Data Portal — *LHCb event file for real measurement*,
  [record 401](https://opendata.cern.ch/record/401),
  DOI `10.7483/OPENDATA.LHCb.E7EJ.JUWR` (event-display files:
  [record 400](https://opendata.cern.ch/record/400)). You find and record this
  in **Seminar 2**.
- What you compute: the **K–π invariant mass** per event → a spectrum with a clear
  **D⁰ peak at ~1865 MeV** over combinatorial background.
- Why it's great: real LHCb data, a genuine signal to find, **fit** (extract the
  D⁰ mass), and classify — the same masterclass analysis school students do, and
  the same lifetime/CP measurements LHCb physicists run.

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

Wherever the physics track says "invariant mass / D⁰ peak", read it as
"your numeric variable / the pattern you're looking for". Clear this choice with
the instructor in Seminar 2.

> Offline or the portal is down? Any tabular CSV works; the instructor can
> provide a local copy of the LHCb sample.

## The repository you will build

```text
analysis-project/       # name it after your data (e.g. d0-analysis)
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
| 10 | First committed figure (physics: the K–π mass spectrum) |
| 11 | A measurement with an uncertainty (a value ± SE) |
| 12 | A fit: the D⁰ peak (Gaussian + background) → mass ± error, χ² |
| 13 | Clean, tidy `processed/` table produced with Pandas |
| 14 | One-command reproducible rebuild (environment + Makefile) |
| 15 | The pipeline run as a batch/remote-style job, at scale *(optional)* |
| 16 | A trained + honestly-evaluated classifier *(optional)* |
