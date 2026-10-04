# 4: Command Line & File Handling

Lecture 2 cleaned a small table by hand and wrote into the README, in words,
what was done. Lecture 3 went down to the bytes of a file and opened the
terminal for three commands, `pwd`, `ls` and `cd`. Lecture 4 stays in the
terminal. The same work on files is done by typed commands, because a step
that was typed can be written down, checked and run again. At the end the
hand cleaning of Lecture 2 is a script, and a checksum shows that the script
writes the same 97 bytes as the hands did.

## What the lecture covers

1. **The shell** — the terminal in VS Code, with Git Bash on Windows; the
   terminal, the shell and a program as three things; the parts of a
   command; absolute and relative paths; the keys that save typing; help;
   how to read an error message.
2. **Files & folders** — `cat`, `head`, `tail`, `less`, `wc`; `mkdir`, `cp`,
   `mv`, `rm`; wildcards and what the shell does with them; `find`; the
   project folder of Lecture 2 as habits at the prompt.
3. **Pipes & filters** — output into a file with `>` and `>>`; the pipe;
   `cut`, `sort`, `uniq -c`, `grep`, `tr`; the two ends of a sorted column;
   `sort -n` and the decimal sign; the mark for a missing value found by
   counting repeats; a histogram of the mass column from five programs; the
   cleaning of Lecture 2 as one line.
4. **Regular expressions** — a pattern in place of a fixed text; the signs
   for one character, for repetition and for a place in the line, each with
   the lines it fits in the pendulum table; patterns and capture groups in
   the Find box of VS Code; `grep -E`; how wildcards and regular expressions
   differ.
5. **A first script** — a script as a file of commands, run with `bash`;
   running a Python script that is handed out; what 49 marked rows do to a
   mean; variables; the `for` loop; a script that prints the range of every
   column.
6. **Checksums & backups** — SHA-256 as a command; the script's output
   against the hand-cleaned file; a list of checksums for `data/raw`; how
   files are lost; the 3-2-1 rule with its arithmetic; a backup as a
   routine.
7. **The README** — what it still lacks after Lectures 2 and 3; its six
   parts; columns and units; how to rebuild; the licence.

## The lecture in 90 minutes

The lecture is slides 1–67 and estimates about 140 min. Slides 68–75 are the
self-check quizzes and take no lecture time. For a 90-minute slot, skip the
slides in the second table: that leaves about 91 min. To jump, type the
slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–4 | The goal, and the hand edits of Lecture 2 as one typed line |
| 0:06 | 6–7, 9–11, 14 | The terminal, the parts of a command, paths, error messages |
| 0:18 | 15–20, 22 | Reading, counting, copying and deleting files; wildcards |
| 0:32 | 23–28, 30–32, 35–36 | Redirection, the pipe, `cut`, `sort`, `uniq -c`, `grep`, `tr`, the cleaning line |
| 0:56 | 37–40, 44 | Regular expressions: the signs, and `grep -E` |
| 1:06 | 46–49 | A script, a Python script that is handed out, the mean with and without the marked rows |
| 1:13 | 54–56, 59 | Checksums, the script against the hand, the 3-2-1 rule |
| 1:21 | 61–62, 64–65 | The README: columns and units, how to rebuild |
| 1:29 | 67 | Recap |
| 1:31 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Three Questions, Clicked and Typed | 5 | 2 min |
| Terminal, Shell, Program | 8 | 2 min |
| Keys That Save Typing, Help | 12–13 | 5 min |
| Search the Folders: `find` | 21 | 2 min |
| `sort -n` and the Decimal Sign | 29 | 3 min |
| A Pipeline, Stage by Stage, and The Mass Column as a Histogram | 33–34 | 4 min |
| Regex in the Find Box, Capture Groups, `.*` Takes All It Can | 41–43 | 7 min |
| Wildcards Are Not Regular Expressions | 45 | 2 min |
| Variables, `for`, the script `ranges.sh` and its reading | 50–53 | 9 min |
| A List of Checksums for `data/raw` | 57 | 2 min |
| How Files Are Lost | 58 | 2 min |
| A Backup Is a Routine | 60 | 3 min |
| Anatomy of a README | 63 | 2 min |
| The Licence | 66 | 2 min |

- **Do not cut** slides 24–28, 30–32 and 35–36 (the pipe and the filters),
  47–49 (the script, the Python script, the mean) or 55–56 (checksums). The
  seminar builds on every one of them.
- **Slides 33–34 and 41–42 are done in the seminar** in any case: its
  sections 6 and 7 build the histogram and the patterns step by step. In a
  90-minute lecture nothing is lost by skipping them.
- **Slide 12** (Keys That Save Typing) stays on the projector at the start
  of the seminar, also when the lecture skipped it.
- **The lecture is shown live.** Keep VS Code beside the slides, with the
  project folder open and a terminal in it, and type each command when its
  slide comes up. Every output on the slides was produced by the command
  above it, on macOS. Git Bash prints the same, without the spaces in front
  of the numbers of `wc`, and words its error messages differently.
- **Before the lecture**, the project folder is in the state after
  Seminar 3: `data/raw/D0_KPi.csv`, `data/raw/pendulum.csv`,
  `data/processed/pendulum.csv`, `README.md`. Put
  [`column_stats.py`](../data/cli_column_stats.py){ download="column_stats.py" }
  into `scripts`. Slide 60 copies the folder to a USB drive: plug one in, or
  copy to any other folder.
- **The live demos leave files behind**: `results/tau.txt`,
  `data/processed/D0_valid.csv`, `data/processed/pendulum_script.csv`,
  `scripts/clean_pendulum.sh`, `scripts/ranges.sh` and `data/checksums.txt`.
  The seminar makes most of them again with the room. Delete them in the
  break, or run the lecture in a copy of the folder.
- **Slide 7** (Open the Terminal): show the four steps for Windows even on a
  Mac. Open the Command Palette, type `default profile`, and show the
  entry.
- **Slide 29** (`sort -n` and the Decimal Sign): the left-hand command
  carries `LC_ALL=lt_LT.UTF-8`, so it shows the wrong order also on a laptop
  set to English. It needs the Lithuanian locale, which macOS has.
- **Slide 36** (The Cleaning of Lecture 2, in One Line): build the line
  stage by stage and watch the last row change from `9;100;20,01` to
  `100,20.01`.
- **Slide 56** (The Script Against the Hand) is where the lecture arrives.
  Give it time: two checksums, the same 64 digits.

Before the session, start the local copy of the slides:
`node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/04-command-line-and-files/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 68–75: seven quiz slides for students to try afterwards. The same
questions, with their answers:

1. A folder holds `run_1.log`, `run_12.log`, `run_A.log` and `notes.txt`.
   What does `ls run_?.log` list?
   *`run_1.log` and `run_A.log`. `?` fits exactly one character.*
2. The terminal is in `analysis-project/results`. Which path names the raw
   pendulum file?
   *`../data/raw/pendulum.csv`. Two points go up one folder.*
3. `runs.txt` has the lines alpha, beta, alpha, gamma, alpha, beta. What
   does `sort runs.txt | uniq -c | sort -n -r | head -n 1` print?
   *`3 alpha`. `uniq -c` writes the count in front of the value.*
4. `notes.txt` has five lines. After `echo done > notes.txt` and
   `echo checked >> notes.txt`, what does `wc -l notes.txt` count?
   *2 lines. A single `>` empties the file first.*
5. Which of the lines `20,9.02`, `100,20.01`, `length_cm,t10_s` and
   `7;80;17,90` does `grep -E '^[0-9]+,[0-9]+\.[0-9]+$'` print?
   *The first two: a whole line that is a number, a comma, a number, a point
   and a number.*
6. A column has 1000 rows. Ten hold the mark −999, and the other 990 have
   the mean 2.0. What is the mean of all rows?
   *(1980 − 9990) / 1000 = −8.01. The marked rows are taken out first.*
7. A project is kept on a laptop, in a second folder on the same laptop, and
   on a USB stick in the laptop bag. Which part of 3-2-1 is not met?
   *The 1: no copy is in another place.*

## Paired seminar

[Seminar 4 — Work on Files from the Shell](../seminars/seminar_04.md) starts
by switching the terminal of VS Code to Git Bash on Windows. The room then
makes and deletes a folder by command, asks `D0_KPi.csv` four questions with
pipes, cleans the raw pendulum table with regular expressions in the Find
box, writes the cleaning script, compares its output across the room by
checksum, runs `column_stats.py`, and completes the README with columns and
units, a list of checksums, how to rebuild, and the licence.

## What left the deck

The deck was rebuilt on 4 October 2026. Gone are the PowerShell columns, the
log-file examples, the five slides on file names and the second folder
layout, which Lecture 2 now teaches, and everything that needed Git. The
earlier deck is in the history of
`lectures/content/slides/04_Command_Line_and_Files.md`.

## Take-aways

- A typed command is a step that can be kept: in the README, in a script,
  for the next file.
- On Windows the terminal is Git Bash. It reads the same commands as the
  terminal of macOS and Linux.
- A path that starts at the project folder works on every laptop. A path
  that starts with `/Users/ada` works on one.
- The shell replaces a wildcard by the names that fit, before the program
  starts. `echo` shows the list.
- `>` empties the file it writes to. A command never writes into the file it
  reads, and never into `data/raw`.
- A filter does one thing to lines of text: `cut` takes columns, `sort`
  orders, `uniq -c` counts repeats, `grep` keeps lines, `tr` changes
  characters. A pipe joins them.
- `sort` orders text unless `-n` is given, and `sort -n` takes the decimal
  sign from the language of the computer. `LC_ALL=C` makes it the point.
- The two ends of a sorted column and the count of repeated values are the
  first checks of a data file. In `D0_KPi.csv` they find four far masses and
  the mark `-100.0` in 49 rows.
- A mark for a missing value that is written as a number is counted as one:
  49 rows of 91 583 move the mean decay time from +0.00098 to −0.0525 ns.
- A regular expression describes a kind of text. `[0-9]` works everywhere,
  `\d` does not. A pattern goes in single quotes.
- A script is a text file of commands, saved with LF line endings and run
  with `bash`.
- Two files with the same SHA-256 are the same, byte for byte. A list of
  checksums guards `data/raw` and checks a backup.
- Three copies, on two kinds of storage, one of them in another place. A
  folder that syncs is not an older copy.
- A README is complete when a stranger with an empty laptop gets the same
  results from it: columns and units, the commands in order, the licence.
