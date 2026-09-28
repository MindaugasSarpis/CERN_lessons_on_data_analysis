# Seminar 2 — Find & Document a Dataset

**Paired lecture:** 02 Introduction to Data · **Format:** hands-on · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

> **29 September runs Seminars 1 and 2 back to back.** The first ~40 minutes
> check the self-paced [Seminar 1](seminar_01.md) — tools installed, project
> skeleton, first commit — then this brief's core tasks follow. Stretch goals
> are skipped that day; the timing above is for the brief on its own.

> **This session builds:** your chosen dataset (LHCb D⁰ → K⁻π⁺, or your own) in `data/raw/`, with
> its provenance recorded.

> **Works the same on Windows, macOS and Linux.** Folders and files are handled
> in VS Code's Explorer; the terminal is used for one command only (task 5),
> given per system. The command line proper starts in Lecture 4.

## Goal
Acquire the seminar dataset and record **where it came from** — the first
act of reproducibility.

## Prerequisites
Seminar 1 (project skeleton).

## Tasks
1. Choose your dataset (see the [seminar overview](overview.md)):
   - **Physics** — find the **LHCb masterclass** dataset on the **CERN Open Data
     Portal** ([record 401](https://opendata.cern.ch/record/401), D⁰ → K⁻π⁺;
     event-display files at [record 400](https://opendata.cern.ch/record/400)).
     Note the record's title, DOI (`10.7483/OPENDATA.LHCb.E7EJ.JUWR`), and licence.
   - **Your own field** — pick a tabular dataset from your own field (weather,
     survey, prices, lab measurements…). Note where it came from and its licence.
2. Download the record's file into `data/raw/` **without renaming it** — with
   the browser, then drag it into the folder in VS Code's Explorer. For record
   401 that is `MasterclassData.root`: a ROOT file, the binary format of
   particle physics, which a text editor cannot read. Put the course's converted
   copy next to it: [`D0_KPi.csv`](../data/D0_KPi.csv), made from that exact
   file by [`root_to_csv.py`](../data/root_to_csv.py). Open the CSV in VS Code
   and look at the first lines.
3. In `README.md`, start a **Data** section: source URL, DOI, licence, download
   date, file names, and a one-line description of what a row represents. Say
   which file is the **original** and which is **derived** — and by what.
4. Record each file's size and the CSV's row count next to the provenance: the
   size from your file manager, the row count from the last line number VS Code
   shows (you'll verify both with command-line tools in Seminar 3).
5. Fingerprint the original download so anyone can verify they hold the *exact*
   same bytes, and record the hash in the **Data** section. In VS Code's
   terminal (**Terminal → New Terminal**), one of:
   ```text
   Windows (PowerShell)   Get-FileHash data\raw\MasterclassData.root -Algorithm SHA256
   macOS                  shasum -a 256 data/raw/MasterclassData.root
   Linux, Git Bash        sha256sum data/raw/MasterclassData.root
   ```
   Compare with a neighbour on a different system: same file, same 64
   characters (upper or lower case does not matter).
6. Cross-check your provenance against the portal's own metadata: open the
   record's JSON export (linked on the record page) and compare title, DOI,
   licence and file size with what you wrote. Add any field you had missed.

## Stretch goals
- What are the units of the mass column `M` — MeV or GeV? Neither the file nor
  the record says; the D⁰ mass (1865 MeV/c²) does. Write the answer, and how
  you know, into your README.
- The record says "about 60k events"; how many rows does the CSV have? Note both
  numbers and a possible reason for the difference.
- Identify one other open dataset in your own field of interest and note its licence.

## Wrap-up (last 10 min)
- Snapshot today's work: `git add -A && git commit -m "Add dataset + provenance"`
  (a large raw file can stay out of Git — provided your **Data** section says
  exactly how to fetch it).
- The acid test: could a stranger re-download the byte-identical file from your
  README alone, and confirm it with your checksum? Fix whatever they couldn't.
- Note one lesson in the README — e.g. what "provenance" turned out to include
  that you hadn't expected.

## Solution notes (instructor)
Emphasise that "I downloaded it from somewhere" is not provenance. A good entry
lets a stranger obtain the *exact* same file years later. Raw data goes in
`raw/` and is never edited from here on. Reference values for record 401:
`MasterclassData.root` is 1 289 541 bytes, SHA-256 `8694a2ed…6b23b039b`;
`D0_KPi.csv` has 91 583 rows + header, four columns (`M`, `PT`, `TAU`,
`IPCHI2`), SHA-256 `25c3c972…c1505136`. The ROOT file declares 147 columns but
fills only those four. In the 120-minute slot the portal hunt
(task 1) is the time sink — if it passes ~25 minutes, hand out the local copy
and let students backfill provenance from the record page.

## Aims practised
♻️ provenance = reproducibility · 📁 raw data captured, untouched
