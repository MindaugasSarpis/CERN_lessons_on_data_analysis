# Seminar 3 — Bit, Number & Format Explorer ⚡

**Paired lecture:** 03 How Computers Work · **Format:** hackathon · **~90 min**

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

## Stretch goals
- Write a tiny converter: read the first number as text and print it in binary/hex.
- Estimate: if the experiment recorded 10× more events, how big would the file be?

## Solution notes (instructor)
Tie back to the lecture: a CSV is a *named sequence of bytes*; the `.csv`
extension is a convention, not a guarantee. The hexdump makes "everything is
bytes" concrete.

## Aims practised
📁 know your data at the byte level · 🔧 CLI tools that work anywhere
