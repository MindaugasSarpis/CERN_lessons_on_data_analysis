# Seminar 7 — Python Warm-Up: Parse One Event

**Paired lecture:** 07 Python Foundations · **Format:** hands-on · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

> **This session builds:** your first parsing code — one CSV line
> turned into numbers.

## Goal
Write clean Python that turns a raw text line into usable numeric values, using
only the language basics (strings, lists, functions, control flow).

## Prerequisites
Seminar 6. Python basics from lecture 07.

## Tasks
1. In `scripts/parse.py`, hard-code one data row from the CSV as a string.
2. Use `str.strip()` and `str.split(",")` to break it into fields.
3. Convert the numeric fields with `float()`; keep IDs as `int`/`str`.
4. Write a function `parse_line(line) -> dict` mapping column names to values.
   Guard against a bad line with `try/except` and return `None`.
5. Print the parsed dict nicely with an f-string.

## Stretch goals
- Read the header row and build the column-name list automatically instead of
  hard-coding it.
- Add a `list comprehension` that extracts just the kaon and pion momenta.
- Write a second function `validate_line(fields) -> bool` that rejects a row
  whose momentum components fail to convert or come out `NaN` — a preview of
  Seminar 9's audit.

## Wrap-up (last 10 min)
- Run `python scripts/parse.py` once more from a clean terminal and confirm
  the exact same dict prints, byte for byte.
- Commit it: `git add -A && git commit -m "First parser for one event"`.
- Note one lesson in the README: which field was trickiest to convert, and why
  (the classic `str` vs `float` trap?).

## Solution notes (instructor)
This is the `strip → split → convert` recipe from the lecture. Keep it in a
**function** — Seminar 8 will call it over the whole file. Watch for off-by-one
column errors and locale decimal issues. In the 120-minute slot, the
`try/except` guard in task 4 is where groups stall — put the recipe on the
board early so task 5 and the stretch goals still get their time.

## Aims practised
🔧 language-agnostic parsing ideas · 📁 turning bytes into structured values
