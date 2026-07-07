# Seminar 3 — Bit, Number & Format Explorer ⚡

**Paired lecture:** 03 How Computers Work · **Format:** hackathon · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

> **Running project — this session adds:** a real understanding of your raw file
> as bytes — its encoding, size, and format.

## Goal
Demystify "it's just a CSV" by looking at the actual bytes, and connect file size
to the number/precision concepts from the lecture.

## Prerequisites
Seminar 2 (dataset in `raw/`).

## Tasks
1. How big is the file, in bytes and in human units? (`ls -l`, `du -h`.) How many
   rows? (`wc -l`.) Roughly how many bytes per row — does that match the columns?
2. Peek at the raw bytes of the first line: `head -c 200 data/raw/*.csv | hexdump -C`.
   Find the comma (`0x2C`) and newline (`0x0A`) bytes.
3. Is it text or binary? Open it in a text editor — readable? Why?
4. Pick one mass value and reason about **float precision**: how many significant
   digits does the file store, and is that exact in binary? (Recall IEEE-754.)
5. What fraction of the file is *structure* rather than data? Count the separator
   bytes and compare against the total size:
   ```bash
   tr -cd ',' < data/raw/*.csv | wc -c    # commas
   wc -l data/raw/*.csv                   # newlines
   ```
6. Text is an *encoding choice*: a mass like `1.86484` costs 7 bytes as text but
   only 4 as a float32. Using your row and column counts, estimate the file's
   size if every number were stored as float32 binary — smaller or larger than
   the CSV? Why do experiments prefer binary formats?

## Stretch goals
- Write a tiny converter: read the first number as text and print it in binary/hex.
- Estimate: if the experiment recorded 10× more events, how big would the file be?
- Compress a copy (`gzip -c data/raw/*.csv > data/processed/raw_copy.csv.gz`) and
  compute the compression ratio — why does repetitive text shrink so well, and
  what does that say about its information density?

## Wrap-up (last 10 min)
- Add a short **File anatomy** note to the README: size, rows, bytes/row,
  encoding, and the structure-vs-data split you measured.
- Commit it (`git add -A && git commit -m "Document raw file anatomy"`), then
  re-run task 1 to confirm the raw file is byte-identical — today you only
  *looked*, never wrote.
- One lesson learned, e.g. "`.csv` is a convention, not a guarantee".

## Solution notes (instructor)
Tie back to the lecture: a CSV is a *named sequence of bytes*; the `.csv`
extension is a convention, not a guarantee. The hexdump makes "everything is
bytes" concrete. For the 2-hour slot, cap the IEEE-754 reasoning in task 4 at
~10 minutes on the board — that's where groups stall — so tasks 5–6 keep their
time.

## Aims practised
📁 know your data at the byte level · 🔧 CLI tools that work anywhere
