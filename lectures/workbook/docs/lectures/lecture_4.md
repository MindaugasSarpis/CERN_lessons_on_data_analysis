# 4: Command Line & File Handling

The lecture checks one number with typed commands, then makes the check
repeatable. In Lecture 1, Smiltė sent the mean air temperature of a weather
station over ten years, **7.16 °C**, with the folder it came from,
`weather-project`. Is 7.16 right? The lecture answers in eight steps, each a
section, and each section ends on a number or a file. Every command runs in zsh on macOS and
in Git Bash on Windows, almost always as the same line; the slides show two
columns only where the systems really differ (checksum program, paths, the
padding of `wc`, error messages).

| Step | Question about 7.16 | Answer, from a typed line |
|--|--|--|
| 1 | Which column of `weather.csv` is the temperature? | `temp_c`, column 2 of 4 |
| 2 | Does the file hold every hour of ten years? | 87 673 lines = 3653 days × 24 hours + the header |
| 3 | Which rows are not measurements? | 120 rows of −999, 22 to 26 July 2019 |
| 4 | Is every other row a measurement? | 87 552 rows fit the pattern of a measured row |
| 5 | The mean without those rows, and with them? | 7.16 and 5.78 °C |
| 6 | Does a second program give the same mean? | `column_stats.py`: 7.15997 |
| 7 | Is my `weather.csv` the file Smiltė used? | SHA-256 `3F1AD06D…FBE00756` |
| 8 | Can anyone run the whole check again? | `./scripts/rebuild.sh` |

## What the lecture covers

1. **The shell** (slides 5–18): terminal, shell and program, and what comes
   with each system (zsh on macOS; on Windows, Windows PowerShell, used only
   for the first install lines); the six things the shell does with a line
   (read, split at spaces, replace `$HOME`, `~` and `*`, find the program,
   start it, keep its exit status); the installs: Homebrew, Git and
   Miniforge on macOS, `winget` for Git and Miniforge on Windows, Git Bash
   as VS Code's default profile, `conda init`; the two prompts; the
   commands of Lecture 03 in one table; relative and absolute paths
   (`/Users/smilte/…` and `/c/Users/smilte/…`); program, option and
   argument; variables; `Tab` and the history; `type`, `man` and `--help`;
   three error messages in both shells; the four columns of `weather.csv`.
2. **Read and count** (slides 19–22): `head` and `tail`; `wc -l`, 87 673
   lines, derived from the calendar (2016, 2020 and 2024 are leap years);
   `wc -c`, 2 515 215 bytes, 29 bytes for a line of 28 characters and its
   LF.
3. **Pipes & filters** (slides 23–33): standard output and standard error,
   `>`, `>>` and `2>`; line 5000 worked out by hand (4998 hours = 208 days
   and 6 hours: 27 July 2016, 06:00) and checked with `head | tail`; `cut`;
   sorting as text (the lowest humidity "is" 100 %) and with `sort -n`
   (34 %); the coldest hours by `sort -t, -k2,2n`, −999 °C; `awk` finds the
   same 120 rows by physics, below −273.15 °C; `grep -c` and `grep -n` find
   them by text, lines 31 154 to 31 273; rows per year with `uniq -c`;
   every one of 3653 days has 24 rows and no hour is there twice
   (`uniq -d`).
4. **Regular expressions** (slides 34–42): hours below freezing, 22 472 by a
   fixed text and 22 352 by a pattern (`grep -cE`); quotes keep a pattern
   from the shell (unquoted, zsh stops with `no matches found` and bash
   drops the backslash and counts 22 472); the signs for one character, for
   how many and for where, each with the part of line 2 it fits and the
   number of lines; `'7.16'` fits 600 lines and none of them is 7.16 °C;
   the 13 forms of the lines (`sed 's/[0-9]/9/g' | sort | uniq -c`); the
   pattern of a measured row built piece by piece, each piece checked by a
   count; the 121 lines it does not fit (`grep -v`) are the header and the
   120 marked rows.
5. **The mean** (slides 43–46): `weather_valid.csv` with 87 553 lines; an
   `awk` line gives 7.15997 without the marks and 5.7828 with them, derived
   from the sum 626 869.3; a formula for what k marks do to a mean, and one
   mark already moves the second decimal.
6. **Programs and packages** (slides 47–57): `column_stats.py` read as a
   text file; `type` shows where `head`, `git` and `python` live; `PATH`,
   searched top to bottom, on both systems; what a package is (files, a
   name and a version, dependencies, a repository), shown by `conda install
   numpy`, which brings six more packages; a package manager's jobs in
   Homebrew and `winget` (search, install, list, upgrade, remove; Git and
   Miniforge); `conda` as package and environment manager, channel
   conda-forge; one environment per project (`np.float_` removed in NumPy
   2.0), `conda create`, `conda activate`; `environment.yml` from `conda env
   export --from-history`; the script gives 7.15997, the same as `awk`; the
   second script cleans the spreadsheet export, 180 bytes to 148.
7. **Checksums & backups** (slides 58–63): `shasum -a 256` on macOS and
   `sha256sum` in Git Bash, the same output; a check against the source with
   `-c`, and what a checksum does and does not tell; a list of checksums
   for `data/raw`, and the `FAILED` after one digit changed; which made
   files have the same bytes on both systems (the `grep` file and the
   script's 148 bytes do; `results/temp_c.txt`, written by Python's `print`,
   has CRLF on Windows: 113 + 6 = 119 bytes), so the README names raw files
   by checksum and results by what they say; the 3-2-1 rule with its
   arithmetic.
8. **Make it repeatable** (slides 64–73): the README's column table, the
   mark and the result; `scripts/rebuild.sh` (`#!/usr/bin/env bash`,
   `chmod +x`, `./`), run after deleting everything it makes; the README's
   three rebuild lines; exit status and `$?` (`grep` says 1 when it found
   nothing); a script that runs on after a failed line, and `set -e`, which
   stops it; the same 113 bytes from two runs; a script as a record of what
   was done; the table of the eight steps, answered.

## Showing the slides offline

`node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/04-command-line-and-files/`.

Slide 3 links the project folder as
[`weather_project.zip`](../data/weather_project.zip) (565 KB): both data
files, the README and the two scripts. Every command of the lecture runs on
it.

## The lecture in two hours

The lecture is slides 1–73. Its speaker notes add up to about 147 minutes,
the live moments included; a two-hour slot has about 110 minutes of
teaching. Slide 74 opens the self-check section, and slides 75–86 are its
twelve quizzes: they take no lecture time. To jump, type the slide number
and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–4 | The number to check, and the eight steps |
| 0:06 | 5–18 | Step 1: the shell, zsh and Git Bash, the installs, the columns |
| 0:36 | 19–22 | Step 2: 87 673 lines (live) |
| 0:44 | 23–33 | Step 3: streams, the pipe (live), objects, the coldest hours (live), 120 rows |
| 1:08 | 34–42 | Step 4: a regular expression, built and counted |
| 1:26 | 43–46 | Step 5: 7.16 against 5.78 |
| 1:34 | 47–57 | Step 6: programs, packages, a conda environment, the second program |
| 1:55 | 58–63 | Step 7: checksums and backups |
| 2:07 | 64–73 | Step 8: the README, `rebuild.sh` (live), exit status, 7.16 checked |
| 2:27 | | End |

In a two-hour slot, skip the slides below: about 30 minutes, and keep the pace of the live moments. Each one
deepens a step; none is needed by a later slide.

| Skip if time is short | Slides | Saves |
|--|--|--|
| Read the Prompt; Where a Command Is, and Its Help; Read an Error Message | 10, 16, 17 | 6 min |
| Sort as Text or as Numbers; Keep Rows by a Condition; Rows per Year | 28, 30, 32 | 6 min |
| A Point Fits Any Character; The Forms of the Lines | 38, 40 | 4 min |
| What One Mark Does to a Mean | 46 | 2 min |
| A Program Is a Text File; The Second Script | 48, 57 | 4 min |
| Check Against the Source; Backups: the 3-2-1 Rule | 60, 63 | 4 min |
| The Same Result, Byte for Byte | 70 | 2 min |

- **Never skip** slide 4 (the eight steps), 7 (what the shell does), 15
  (`Tab`, live), 21 (the count, live), 26 (the pipe, live), 29 (−999,
  live), 31 (the 120 rows), 36 (quotes), 41–42 (the pattern and what it leaves), 45 (the
  two means), 52 (a package manager), 54–55 (an environment and
  `environment.yml`), 59 and 62 (checksums), 66 (the script, live), 69 (stop
  at the first error) and 72 (the eight steps answered).
- **Each section slide names its step**, and each section ends on a card
  with a ✅ and the step's answer. Point back to slide 4 there.
- **Installing is not done here.** Slides 8 and 9 show the install lines
  for both systems; the room installs in Seminar 4.
- **Two columns only where the systems differ.** A card headed
  *zsh · Git Bash* is one line for both. On a Mac `wc` and `uniq -c` pad
  their numbers differently from the slides' Git Bash output; slide 21
  says so once.
- **The slides carry everything.** Every command is on its slide with its
  output. The live moments run the same lines in a terminal first; the
  slide after them is the record.
- **Every speaker note has the same form**: **Live** (a line run in the
  terminal, only on the slides below), **Do** (something done with the
  room), **Say** (the one point of the slide), **Ask** (a question for the
  room), **If asked** (the detail kept off the slide), then the minutes.

## Live in the lecture

Five moments run in a terminal what their slide shows, because a slide
cannot show a key being pressed or a line growing. If a line misbehaves, go
to the slide: it has the output.

**Before the lecture.** On the Mac that drives the projector, unzip
[`weather_project.zip`](../data/weather_project.zip), open the folder
`weather-project` in VS Code, open its terminal (zsh) and make the font
large (`Cmd +` a few times). Shorten the prompt: `PROMPT='%1~ %# '`. Make
the folders the lines write into: `mkdir -p data/processed results`. Run
`clear` before each moment. Running the five once beforehand also checks
the macOS outputs on the slides (the Mac pads `wc`'s numbers).

| Slide | What to type |
|--|--|
| 15 | `head -n 2 da`, then `Tab` three times, `Enter`; then `↑` brings the line back |
| 21 | `wc -l data/raw/weather.csv` |
| 26 | `head -n 5000 data/raw/weather.csv | tail -n 1` |
| 29 | `sort -t, -k2,2n data/raw/weather.csv | head -n 3`, then with `↑` change `head -n 3` to `tail -n 1` |
| 66 | In VS Code, a new file `scripts/rebuild.sh` with the five lines below; then `chmod +x scripts/rebuild.sh`, `rm -r data/processed results`, `./scripts/rebuild.sh`, `tail -n 1 results/temp_c.txt` |
| 61, optional | `shasum -a 256 data/raw/* > data/checksums.txt`; change `6,3` to `6,4` in `daily_export.csv` and save; `shasum -a 256 -c data/checksums.txt`. Change it back and save |

The file of slide 66 (slide 69 then adds `set -e` as line 2):

```text
#!/usr/bin/env bash
mkdir -p data/processed results
grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv
python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
python scripts/column_stats.py data/processed/weather_valid.csv temp_c > results/temp_c.txt
```

It needs `python` in the terminal: Miniforge's `base` after `conda init zsh`,
or the environment `weather` after `conda activate weather`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 74–86: twelve quiz slides for students to try afterwards. The same
questions, with their answers:

1. The terminal is in `weather-project/results`. Which path names the raw
   weather file on every laptop?
   *`../data/raw/weather.csv`. Two points go up one level, from `results` to
   `weather-project`, and from there the path goes down into `data` and
   `raw`. A path that starts with `/` starts at the top of the disk, and `~`
   is the home folder.*
2. `head -n 3 data/raw/wether.csv > results/out.txt` runs. The file name
   has a typo. What happens?
   *The error is printed on the screen, and `out.txt` is an empty file. The
   error goes to standard error, which still reaches the screen; `>`
   writes only standard output, and it makes or empties its file before the
   program runs.*
3. `notes.txt` has five lines. Then `echo done > notes.txt` and
   `echo checked >> notes.txt` run. How many bytes does it have?
   *13, in zsh and in Git Bash alike. A single `>` empties the file first,
   and `>>` adds a second line. The letters are 4 + 7 = 11, and `echo` ends
   each line with LF, one byte.*
4. `cut -d, -f3 weather.csv | sort | head -n 1` prints 100 as the lowest
   humidity. Why?
   *Without `-n`, `sort` compares text character by character, and `1`
   comes before `3`. `sort -n` compares numbers and puts 34 first.*
5. In zsh, `grep -cE ,-[0-9]+\.[0-9], weather.csv` stops with
   `no matches found`. Why?
   *The shell reads `[0-9]` as a pattern for file names before `grep` runs,
   and no file fits. bash passes it on but drops the backslash, and the
   count comes out wrong (22 472). In single quotes every character reaches
   `grep` unchanged.*
6. A file has the four lines `2025-10-01,6.3`, `2025-10-06,10.4`,
   `date,temp_c` and `7;2025-10-07;9,2`. Which lines does the pattern
   `^[0-9-]+,[0-9]+\.[0-9]$` find?
   *The first two: a whole line of digits and minus signs, a comma, a
   number, a point and one digit. The header has letters, and the line with
   semicolons has a semicolon where only digits and minus signs may stand.*
7. A column has 1000 rows. Ten hold the mark −999 for a missing value, and
   the other 990 have the mean 2.0. What is the mean of all 1000 values?
   *(1980 − 9990) / 1000 = −8.01. One row in a hundred gives the mean the
   wrong sign. The marked rows are taken out first.*
8. `PATH` lists `/opt/a/bin` before `/opt/b/bin`. Both hold a program named
   `python`, 3.12 in a and 3.14 in b. What does `python --version` print?
   *Python 3.12. The shell goes through `PATH` in order and runs the first
   program of that name it finds; a newer version further down is never
   reached.*
9. A colleague receives the project folder with `environment.yml`, which
   lists `python=3.14` and `numpy=2.5.4`. Which lines give them the same
   environment?
   *`conda env create -f environment.yml`, then `conda activate weather`.
   The file names the channel and the packages, and `numpy=2.5.4` pins the
   version. A copied environment folder holds the paths of the other
   laptop, and `base` is shared by every project.*
10. `results/temp_c.txt`, written by `python scripts/column_stats.py … >
    results/temp_c.txt`, has 113 bytes on a Mac and 119 on Windows. What
    follows?
    *The same six lines, with LF on the Mac and CRLF on Windows: 119 − 113
    = 6, one byte per line. The checksums differ, the mean does not. The
    README names such a file by what it says.*
11. A project is kept on a laptop, in a second folder on the same laptop, and
    on a USB stick in the laptop bag. Which part of the 3-2-1 rule is not met?
    *The 1: no copy is in another place. One theft or one fire takes all
    three.*
12. `rebuild.sh` has no `set -e`. Its `python` line for the export fails;
    the last line works. What does `echo $?` print after the script?
    *0. Without `set -e` a script runs every line, and its exit status is
    that of its last line. With `set -e` it stops at the failing line and
    reports 1.*

## Paired seminar

[Seminar 4](../seminars/seminar_04.md) works on the same weather project:
the room installs the tools with a package manager, sets up its shell, and
checks and rebuilds the mean temperature, 7.16 °C, with typed lines and a
script.

## What left the deck

On 13 October 2026, after the lecture was given, the deck was rebuilt
around one question, "is 7.16 right?", in eight steps. The course's shells
became zsh on macOS and Git Bash on Windows, so each command is one line
for both, and two columns appear only where the systems differ. The
one-command slides that Lecture 03 already taught became one table. Out
went the step-by-step clicking (opening a terminal in VS Code, the Find box
of VS Code), PowerShell 7 and its install, `chsh`, capture groups, and from
the old section *Tools & Environments* the shell settings (an alias and a
prompt, the start-up files, Oh My Zsh) and what `conda init` writes.
Package managers stayed, as a section of their own; the conda environment
is three slides. New: what the shell does with a line, variables, the two
output streams, line 5000 by arithmetic, `awk` as a filter and for the
mean, quotes and the shell, the forms of the lines, a pattern built piece
by piece, a formula for what a mark does to a mean, exit status, and a
script as a record. The removed slides are in
`lectures/content/parked/04_Command_Line_and_Files.md`, each with a note
saying where it stood.

## Take-aways

- A typed command is a step that can be kept: in the README, in a script,
  for the next file.
- The terminal is the window, the shell reads the line, a program does the
  work. The course's shells are zsh on macOS and Git Bash on Windows, and
  almost every line runs in both unchanged.
- The shell splits a line at spaces and replaces `$names`, `~` and `*`
  before the program runs; a pattern goes in single quotes.
- A path that starts at the project folder works on every laptop.
- `>` writes standard output and empties its file first; errors go to
  standard error. A pipe passes one program's output to the next.
- A count derived from the calendar checks a file; the two ends of a sorted
  column show its wrong values. In `weather.csv` they show −999, the mark of
  120 hours without a temperature.
- A regular expression describes a kind of text. Build it a piece at a
  time and check each piece by its count.
- A mark for a missing value written as a number is counted as one: 120
  rows of 87 672 move a ten-year mean from 7.16 to 5.78 °C, and one row
  moves the second decimal.
- A package is files, a name, a version and its dependencies, from a
  repository. A package manager installs it with a line that can be kept:
  Homebrew or `winget` for programs, `conda` for Python packages in one
  environment. The shell finds a program in the folders of `PATH`, in
  order.
- Two files with the same SHA-256 are the same, byte for byte. A file
  written by Python's `print` has other bytes on Windows; name it by what
  it says.
- A script is the check written down in order. It runs again with one
  line, and with `set -e` it ends at the first error and reports it in its
  exit status.
