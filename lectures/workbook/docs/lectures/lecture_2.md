# 2: Introduction to Data

Lecture 1 was the *why* — the course, the four aims, and the motivation reel
from the cosmos down to CERN. Lecture 2 is the *what*: what a dataset is, where
one comes from, and how you write down where it came from.

## What the lecture covers

1. **Data in your life** — a day's worth of datasets; what data even is; its
   lifecycle; structured vs unstructured; the four flavours (numbers, text,
   images, events); measurement vs metadata; data at work in life, planet,
   money, sky and the subatomic.
2. **Four eyes on the ring** — ATLAS, CMS, ALICE, LHCb, each with a short clip,
   and the particle you will analyse: the D⁰ meson and its K⁻π⁺ invariant-mass
   peak near 1865 MeV.
3. **Why data?** — the 5-sigma standard, from collision to dataset, from events
   to petabytes, why the trigger has to work in real time; the people who run
   it (careers at CERN, a day in the data).
4. **Beyond the ring** — the Web, the computing grid, and why CERN can publish
   its data years later.
5. **Open data & provenance** — portals, the anatomy of a record, licences
   (CC0 / CC BY / share-alike), the minimal provenance note, data you bring
   yourself, from record to your repo.
6. **A dataset up close** — the LHCb sample as a file: rows are candidates,
   columns are measured / derived / bookkeeping quantities, units are metadata,
   five questions to ask any file before writing code.

## Paired seminar

[Seminar 2 — First Hands-On](../seminars/seminar_02.md) is the first session in
class and starts from zero: install VS Code, build a project folder, put the
lecture's example file into `data/raw/`, and write into the README where it
came from. At home you choose a dataset from your own field and install Python
and Git ([Seminar 1](../seminars/seminar_01.md)).

## Take-aways

- Cite the **record**, not the file: DOI or stable URL, version or fetch date,
  checksum.
- Read the record before the data: what is one row, how was it selected, what
  may you publish.
- Units are metadata — if the file does not say, your README must.
- Large or restricted data stays out of git; the README says how to fetch it.
