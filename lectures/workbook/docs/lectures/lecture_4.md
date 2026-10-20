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

The lecture is built for the room to predict before it sees: the output of
a command sits behind a click, and where a command or a script grows step
by step, one block changes on each click (a Shiki magic move) instead of a
run of near-identical slides.

1. **The shell** (slides 5–17): terminal, shell and program, and what comes
   with each system (zsh on macOS; on Windows, Windows PowerShell, used only
   for the first install lines); the six things the shell does with a line;
   the installs: Homebrew, Git and Miniforge on macOS, `winget` for Git and
   Miniforge on Windows, Git Bash as VS Code's default profile, `conda
   init`; the two prompts; the commands of Lecture 03 in one table; `pwd`,
   `ls` and `cd` in one growing session, with relative and absolute paths;
   program, option and argument; what the shell replaces (`$name`, `~`,
   `*`) and variables; `Tab` and the history; three error messages in both
   shells; the four columns of `weather.csv`.
2. **Read and count** (slides 18–21): `head` and `tail`; one line in bytes
   with `xxd`, 28 characters and `0a`; the line count predicted from the
   calendar (2016, 2020 and 2024 are leap years), then `wc -l`, 87 673, and
   `wc -c`, 2 515 215 bytes.
3. **Pipes & filters** (slides 22–30): standard output and standard error,
   `>`, `>>` and `2>`; standard input, `<` and the pipe; line 5000 worked
   out by hand (27 July 2016, 06:00) and checked with `head | tail`; sorting
   as text (the lowest humidity "is" 100 %) and with `sort -n` (34 %); the
   coldest hour built filter by filter (`cut`, `tail -n +2`, `sort -n`,
   `sort -t, -k2,2n`): −999 °C; `awk` finds the same 120 rows by physics,
   below −273.15 °C; `grep -c` and `grep -n` find them by text, lines 31 154
   to 31 273; rows per year, days with 24 rows, no hour twice.
4. **Regular expressions** (slides 31–38): `,-` finds 22 472 lines, the
   −999 rows among them; four signs for one character (itself, `.`,
   `[0-9]`, `\.`); `'7.16'` fits 600 lines and none of them is 7.16 °C;
   three signs for how many and where (`+`, `?`, `^`); the pattern for a
   frost hour built one sign at a time (22 472, 120, 22 352); a pattern in
   single quotes; `,-?[0-9]+\.[0-9],` fits 87 552 rows, and the 121 it does not
   fit (`grep -v`) are the header and the 120 marked rows.
5. **The mean** (slides 39–42): `weather_valid.csv` with 87 553 lines; an
   `awk` program built in three steps gives 7.15997 without the marks and
   5.7828 with them, derived from the sum 626 869.3; a formula for what k
   marks do to a mean, and one mark already moves the second decimal.
6. **Programs and packages** (slides 43–53): `type` shows where `head`,
   `git` and `python` live; `PATH`, searched top to bottom, on both
   systems; what a package is (files, a name and a version, dependencies, a
   repository), shown by `conda install numpy`, which brings six more
   packages; a package manager's jobs in Homebrew and `winget`; `conda` as
   package and environment manager, channel conda-forge; one environment
   per project (`np.float_` removed in NumPy 2.0); activation puts the
   environment first on `PATH`; `environment.yml` from `conda env export
   --from-history`; `column_stats.py`, a program someone else wrote, gives
   7.15997, the same as `awk`; the second script cleans the spreadsheet
   export, 180 bytes to 148. Python itself is Lecture 05: here it is only a
   program that is run.
7. **Checksums & backups** (slides 54–59): `shasum -a 256` on macOS and
   `sha256sum` in Git Bash, the same output; a check against the source with
   `-c`, and what a checksum does and does not tell; a list of checksums
   for `data/raw`, and the `FAILED` after one digit changed; which made
   files have the same bytes on both systems; the 3-2-1 rule with its
   arithmetic.
8. **Make it repeatable** (slides 60–66), kept short: the README's result
   and its three rebuild lines; `scripts/rebuild.sh` growing line by line,
   then run after deleting everything it makes; exit status, and `set -e`,
   which stops the script at the first failing line; a second run gives the
   same checksum; the eight steps, answered.

## Showing the slides offline

`node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/04-command-line-and-files/`.

Slide 3 links the project folder as
[`weather_project.zip`](../data/weather_project.zip) (565 KB): both data
files, the README and the two scripts. Every command of the lecture runs on
it.

## The lecture, part by part

The lecture is slides 1–66; when time is short, skip the slides of the
second table. Slide 67 opens the self-check section, and slides 68–79 are
its twelve quizzes: they take no lecture time. To jump, type the slide
number and press Enter. Many slides take several clicks: the output, or the
next step of a growing command, comes on the click.

| Slides | Part |
|--|--|
| 1–4 | The number to check, and the eight steps |
| 5–17 | Step 1: the shell, zsh and Git Bash, the installs, the columns |
| 18–21 | Step 2: 87 673 lines, predicted, then counted (live) |
| 22–30 | Step 3: streams, line 5000 (live), the coldest hour (live), 120 rows |
| 31–38 | Step 4: a regular expression, one sign at a time |
| 39–42 | Step 5: 7.16 against 5.78 |
| 43–53 | Step 6: programs, packages, a conda environment, the second program |
| 54–59 | Step 7: checksums and backups |
| 60–66 | Step 8: the README, `rebuild.sh` (live), `set -e`, 7.16 checked |

Each one deepens a step; none is needed by a later slide.

| Skip if time is short | Slides |
|--|--|
| Read the Prompt; The Commands of Lecture 03; Read an Error Message | 10, 11, 16 |
| One Line, Byte by Byte; Standard Input | 20, 24 |
| The Lowest Humidity; Keep Rows by a Condition; Every Year, Every Day, Every Hour | 26, 28, 30 |
| A Point Fits Any Character | 34 |
| What One Mark Does to a Mean | 42 |
| Activation Changes PATH; The Second Script | 50, 53 |
| Check Against the Source; Backups: the 3-2-1 Rule | 56, 59 |

- **Never skip** slide 4 (the eight steps), 7 (what the shell does), 15
  (`Tab`, live), 21 (the count, live), 25 (line 5000, live), 27 (the
  coldest hour, live), 29 (the 120 rows), 36 (below freezing, one sign at a
  time), 38 (every other row a measurement), 41 (the two means), 47 (a
  package manager), 49 and 51 (an environment and `environment.yml`), 55
  and 58 (checksums), 62 (the script, live), 63 (`set -e`) and 65 (the
  eight steps answered).
- **Predict first.** On a slide with a click, ask the note's **Ask** before
  clicking: the room says what the line will print, then sees it.
- **Each section slide names its step**, and each section ends on a card
  with a ✅ and the step's answer. Point back to slide 4 there.
- **Installing is not done here.** Slides 8 and 9 show the install lines
  for both systems; the room installs in Seminar 4.
- **Two columns only where the systems differ.** A card headed
  *zsh · Git Bash* is one line for both. On a Mac `wc` and `uniq -c` pad
  their numbers differently from the slides' Git Bash output; slide 21
  says so in its note.
- **The slides carry everything.** Every command is on its slide with its
  output. The live moments run the same lines in a terminal first; the
  slide is the record.
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
| 21 | after the prediction: `wc -l data/raw/weather.csv` |
| 25 | `head -n 5000 data/raw/weather.csv`, then `↑` and add `| tail -n 1` |
| 27 | `cut -d, -f2 data/raw/weather.csv | head -n 3`; with `↑` put `tail -n +2 data/raw/weather.csv |` in front and `| sort -n` before `head`; then `sort -t, -k2,2n data/raw/weather.csv | head -n 3` |
| 62 | In VS Code, a new file `scripts/rebuild.sh` with the five lines below; then `chmod +x scripts/rebuild.sh`, `rm -r data/processed results`, `./scripts/rebuild.sh`, `tail -n 1 results/temp_c.txt` |
| 57, optional | `shasum -a 256 data/raw/* > data/checksums.txt`; change `6,3` to `6,4` in `daily_export.csv` and save; `shasum -a 256 -c data/checksums.txt`. Change it back and save |

The file of slide 62 (slide 63 then adds `set -e` as line 2):

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
slides 67–79: twelve quiz slides for students to try afterwards. The same
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
the room installs the tools with a package manager, sets up its shell,
types six hours of the station's log into a file from the terminal, and
checks and rebuilds their mean temperature, 25.3 °C without the `-999`
rows, with typed lines and a script.

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
mean, quotes and the shell, a pattern built one sign at a time, a formula for what a mark does to a mean, exit status, and a
script as a record. Later the same day the regular-expression
section was made easier to follow: the forms of the lines (`sed`) and the
full-row pattern were parked, and the section ends on a short pattern for
the temperature. The removed slides are in
`lectures/content/parked/04_Command_Line_and_Files.md`, each with a note
saying where it stood.

Later on 13 October the deck was made to read as a lecture: outputs behind
a click, so the room predicts first, and Shiki magic moves where a line
grows (the session of `cd`, line 5000, the coldest hour filter by filter,
the counts per year and day, the frost pattern sign by sign, the `awk`
mean, `rebuild.sh` line by line, exit status and `set -e`). Runs of
one-command slides became one slide each. Step 8 was cut to the README,
the script, `set -e` and a second run. Python is left to Lecture 05: the
slide that read `column_stats.py` as a text file is parked, with the slide
on `type` and help and the table of where the answers about 7.16 are
written. New: one line in bytes with `xxd`, standard input, and
activation as a change of `PATH`.

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
