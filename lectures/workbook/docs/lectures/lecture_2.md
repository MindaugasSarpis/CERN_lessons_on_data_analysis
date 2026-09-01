# 2: Introduction to Data

Lecture 1 was the *why* — the course, the four aims, and the motivation reel
from the cosmos down to CERN. Lecture 2 is the *what*: what a dataset is, where
one comes from, and how you write down where it came from.

## What the lecture covers

1. **Data in your life** — a day's worth of datasets; what data even is; its
   lifecycle; structured vs unstructured; the four flavours (tables, text,
   images, time series); measurement vs metadata; data at work in science,
   society and money.
2. **Four eyes on the ring** — ATLAS, CMS, ALICE, LHCb, and the particle you will
   analyse: the D⁰ meson and its K⁻π⁺ invariant-mass peak near 1865 MeV.
3. **Why data?** — from collision to dataset, from events to petabytes, why the
   trigger has to work in real time.
4. **Open data & provenance** — portals, the anatomy of a record, licences
   (CC0 / CC BY / share-alike), the minimal provenance note, data you bring
   yourself, from record to your repo.
5. **A dataset up close** — the LHCb sample as a file: rows are events, columns
   are measured / derived / bookkeeping quantities, units are metadata, five
   questions to ask any file before writing code.
6. **Beyond the ring** — the Web, the computing grid, open data up close.

## Paired seminar

[Seminar 2 — Find & Document a Dataset](../seminars/seminar_02.md): locate the
LHCb masterclass sample on the CERN Open Data Portal
([record 401](https://opendata.cern.ch/record/401),
DOI `10.7483/OPENDATA.LHCb.E7EJ.JUWR`) — or a dataset from your own field — put
it in `data/raw/`, checksum it, and record its provenance in the README.

## Take-aways

- Cite the **record**, not the file: DOI or stable URL, version or fetch date,
  checksum.
- Read the record before the data: what is one row, how was it selected, what
  may you publish.
- Units are metadata — if the file does not say, your README must.
- Large or restricted data stays out of git; the README says how to fetch it.
