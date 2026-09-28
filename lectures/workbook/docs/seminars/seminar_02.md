# Seminar 2 — Find & Document a Dataset

**Paired lecture:** 02 Introduction to Data · **Format:** hands-on · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

> **29 September is a 90-minute session.** It opens with a guided tour of VS
> Code and a check of the self-paced [Seminar 1](seminar_01.md) — tools
> installed, project skeleton, first commit — then runs tasks 1–5 of this
> brief. Task 6 and the stretch goals are homework; the timing above is for the
> brief on its own. Run-of-show: [lecturer's brief](lecturer_02.md).

> **This session builds:** a dataset of your own choice in `data/raw/`, with its
> provenance recorded.

> **Works the same on Windows, macOS and Linux.** Folders and files are handled
> in VS Code's Explorer; the terminal is used for one command only (task 5),
> given per system. The command line proper starts in Lecture 4.

## Goal
Acquire a dataset and record **where it came from** — the first act of
reproducibility.

## Prerequisites
Seminar 1 (project skeleton).

## Tasks
1. Choose a dataset **from your own field** on an open-data portal — weather,
   survey, prices, lab measurements, sky catalogues… (Lecture 2 lists portals:
   Eurostat, Copernicus, NASA, Zenodo, Kaggle). It should be tabular, with a few
   thousand rows or more and at least one numeric column. Note the record's
   title, DOI or stable URL, and licence.
   *No idea yet?* Practise on the lecture's example and swap later: the LHCb
   sample, [record 401](https://opendata.cern.ch/record/401) on the CERN Open
   Data Portal, DOI `10.7483/OPENDATA.LHCb.E7EJ.JUWR`.
2. Download the file into `data/raw/` **without renaming it** — with the
   browser, then drag it into the folder in VS Code's Explorer. Open it in VS
   Code and look at the first lines. If it is not text (the LHCb record holds a
   binary ROOT file, `MasterclassData.root`), keep the original and add a
   readable copy next to it — for LHCb the workbook's
   [`D0_KPi.csv`](../data/D0_KPi.csv), made by
   [`root_to_csv.py`](../data/root_to_csv.py).
3. In `README.md`, start a **Data** section: source URL, DOI, licence, download
   date, file names, and a one-line description of what a row represents. If
   you hold a converted copy, say which file is the **original** and which is
   **derived** — and by what.
4. Record the file's size and row count next to the provenance: the size from
   your file manager, the row count from the last line number VS Code shows
   (you'll verify both with command-line tools in Seminar 3).
5. Fingerprint the original download so anyone can verify they hold the *exact*
   same bytes, and record the hash in the **Data** section. In VS Code's
   terminal (**Terminal → New Terminal**), with your file's name, one of:
   ```text
   Windows (PowerShell)   Get-FileHash data\raw\myfile.csv -Algorithm SHA256
   macOS                  shasum -a 256 data/raw/myfile.csv
   Linux, Git Bash        sha256sum data/raw/myfile.csv
   ```
   Send the file to a neighbour on a different system: same file, same 64
   characters (upper or lower case does not matter).
6. Answer Lecture 2's five questions for your file, in the README: how many
   rows and columns, what one row is, which columns are measured / derived /
   bookkeeping, their units, and how missing values are marked.

## Stretch goals
- Cross-check your provenance against the portal's own metadata (many portals
  offer a JSON or "cite" export of the record): compare title, DOI, licence and
  file size with what you wrote. Add any field you had missed.
- A column whose unit is written nowhere: work the unit out from the values and
  note how you know.
- Identify a second open dataset in your field and note how its licence differs.

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
`raw/` and is never edited from here on. Datasets are the students' own; the
LHCb record is only the fallback. Reference values for record 401:
`MasterclassData.root` is 1 289 541 bytes, SHA-256 `8694a2ed…6b23b039b`;
`D0_KPi.csv` has 91 583 rows + header, four columns (`M`, `PT`, `TAU`,
`IPCHI2`), SHA-256 `25c3c972…c1505136`. The ROOT file declares 147 columns but
fills only those four. In the 120-minute slot the portal hunt
(task 1) is the time sink — if it passes ~25 minutes, point the student to the
LHCb fallback and let them swap in their own dataset later.

## Aims practised
♻️ provenance = reproducibility · 📁 raw data captured, untouched
