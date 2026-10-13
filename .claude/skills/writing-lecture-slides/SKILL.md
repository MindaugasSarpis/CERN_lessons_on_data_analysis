---
name: writing-lecture-slides
description: Use when writing, reworking or reviewing a lecture deck in lectures/content/slides/ or a seminar page in lectures/workbook/docs/seminars/ of this course, including slide titles, card headings, captions, section slides and speaker notes, or when the lecturer calls a slide cluttered, a slogan or repetitive.
---

# Writing Lecture Slides

## The principle

The lecturer talks; the slide shows what talk cannot: commands with their
output, tables, worked numbers, definitions. A line on a slide earns its
place by carrying one of those. A line the lecturer could simply say (a
transition, a framing, a reminder) belongs in the speaker note or nowhere.

## What a content slide is

Top to bottom, and nothing else:

1. **A title, or none.** When present, it states what the slide does or
   answers, in plain words:
   - an action: `Read the Prompt`, `Change Folder: cd`, `Pick Columns: cut and Import-Csv`
   - a question: `Where Am I: pwd`
   - the thing shown: `The Columns of weather.csv`
   - a claim the slide proves: `An Upgrade for One Project Breaks Another`

   No title when the boxes already say it (cards headed Terminal / Shell /
   Program need no title "Terminal, Shell, Program").
2. **The boxes**: commands with real output, tables, derivations. Each card
   heading names what its card holds: `🍎 macOS · zsh`,
   `📄 The first two lines of weather.csv`, `🧬 A copy with one digit changed`.
3. **At most one caption** (`note-text` or a small card), and only for a
   fact the boxes do not show: a definition, the arithmetic behind a
   number, a warning.
4. **The speaker note**, in the form of CLAUDE.md convention 13. Transitions
   and framing go here if anywhere, never forward references to later
   slides ("the next slide…").

A **section slide** is the section's name and at most one line with its
idea. It is a pause for questions; it does not list what the next slides
show.

## Test every title, heading and caption

The test reaches titles, card headings, captions, section subtitles and
forward references in the notes. Card bodies are the content: commands,
outputs, tables, step lists, worked numbers and side-by-side comparisons
stay, and change only where they repeat another box word for word.

| Question | If yes |
|--|--|
| Does it repeat a card heading, a table header or the line next to it? | Delete it. |
| Is it a catchy pair, number play or two-beat phrase that the slide has to decode? `One Row, Four Values`, `One Shell per System`, `One Python, Every Project`, `24 Characters, 26 or 28 Bytes`, `One digit changes all` | Write what the slide does or shows instead, or delete it. |
| Does it narrate the deck or the course? `The next slide installs it`, `This course uses PowerShell 7`, `One command per slide:`, `Remember this file`, `From here on…`, `Nothing new on this slide` | Delete it. |
| Could the lecturer say it in one breath with nothing on the slide lost? | Delete it. |
| After a deletion, does a heading no longer make sense (`Open it`, `Still open`, `Five or seven`)? | Name the thing in the heading. |

These stay: a title that states the step (`Delete: rm`), a caption with a
definition or a derivation (`3653 days × 24 = 87 672 hours`), a reading key
needed on every later slide (`%` and `PS>` are printed by the shell), and
section slides.

## Seminar pages

The same test applies to a seminar page. Its `### N.` headings stay,
because the run sheet links them, but each one says what is done:
`Count the 9999 rows, keep the others in a new file`, not
`Count the mark, keep the rest`. Keep `{ #anchor }` ids unchanged, and make
the run-sheet row match the heading.

## Before and after, Lecture 04 (12 October 2026)

| Before | After |
|--|--|
| `# One Row, Four Values` | `# The Columns of weather.csv` |
| `# Three Questions` over a table headed "Question about weather.csv" | no title |
| `# One Shell per System` over a table "Laptop / Shell of this course" | no title |
| caption: "This course uses PowerShell 7. The next slide installs it from the Windows PowerShell window." | deleted |
| section subtitle: "One command per slide: where the shell is, what is there, …" | "Where the shell is, what is there, …" |
| `# Move: cd` | `# Change Folder: cd` |
| `# 24 Characters, 26 or 28 Bytes` | `# Why the Sizes Differ: Line Endings` |
| card `🔢 5 or 7` | `🔢 Windows PowerShell or PowerShell 7` |

## Before and after, Lectures 01–05 (13 October 2026)

Slipped through a rework and caught by the lecturer ("sloppy title again"):
a pair or a parallel that the slide has to decode is a slogan, even when it
is true.

| Before | After |
|--|--|
| `# Two Programs, One Mean` | `# The Mean from column_stats.py` |
| `# The Same Rows, Other Bytes` | `# Which Files Have the Same Bytes on Both Systems` |
| `# Every Program Ends with a Number` | `# Exit Status: $?` |
| `# The Same Result, Byte for Byte` | `# Rebuild Twice, Compare the Checksums` |
| `# A Script Is a Record` | `# Where the Answers About 7.16 Are Written` |
| `# 7.16, Checked` | `# The Eight Steps, Answered` |
| `# Think Like a CPU` | `# The Largest Number, Step by Step` |
| `# Copies Instead of Versions` | `# Versions Kept as Copies` |

Before handing a deck back, list every `# ` title of it (`grep '^# '`) and
run the test above on each line of that list.

The other slide rules (self-contained decks, no "made up" labels, two
shells side by side, the note form, derive rather than assert, quizzes at
the end) are in CLAUDE.md under Slide Authoring Conventions.
