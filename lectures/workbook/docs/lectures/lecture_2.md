# 2: Introduction to Data

Lecture 1 was the *why* — the course, the four aims, and the motivation reel
from the cosmos down to CERN. Lecture 2 is the *what*: what a dataset is, where
one comes from, and how you write down where it came from.

## What the lecture covers

1. **Data in your life** — a day's worth of datasets; what data even is; its
   lifecycle from collecting to sharing.
2. **Kinds of data** — structured vs unstructured; the four flavours (numbers,
   text, images, events) and their parametrisation — how each one is written
   as numbers; kinds of variables (continuous, discrete, nominal, ordinal);
   measurement vs metadata; the anatomy of a table; the same table as CSV,
   spreadsheet and binary file; data at work in other fields.
3. **Open data & provenance** — portals, the anatomy of a record, licences
   (CC0 / CC BY / share-alike), the minimal provenance note, data you bring
   yourself, from record to your project folder.
4. **Case study: CERN** — the four LHC experiments; the 5-sigma standard; from
   collision to dataset and why the trigger works in real time; the Web, the
   computing grid and open data.
5. **A dataset up close** — the LHCb example as a file: rows are candidates,
   four computed columns, units are metadata, five questions to ask any file
   before writing code.

## Paired seminar

[Seminar 2 — First Hands-On](../seminars/seminar_02.md) is the first session in
class and starts from zero: install VS Code, build a project folder, put the
lecture's example file into `data/raw/`, and write into the README where it
came from. At home you choose a dataset from your own field and install Python
and Git ([Seminar 1](../seminars/seminar_01.md)).

## Take-aways

- Parametrisation: every flavour of data is written as a set of numbers before
  it is analysed — a character as a code, a pixel as three values 0–255, an
  event as a time plus what was measured. Written as a number is not the same
  as behaving like one: a postcode has no average.
- Cite the **record**, not the file: DOI or stable URL, version or fetch date,
  checksum.
- Read the record before the data: what is one row, how was it selected, what
  may you publish.
- Units are metadata — if the file does not say, your README must.
- A row is one observation, a column is one variable of one kind, a cell is
  one value.
- A CSV file is plain text; a spreadsheet shows its own interpretation of it.
- Large or restricted data stays out of git; the README says how to fetch it.
