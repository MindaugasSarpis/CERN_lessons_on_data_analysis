# 4: Command Line & File Handling

The lecture checks one number with typed commands, then makes the check
repeatable. In Lecture 1, Smiltė sent the mean air temperature of a weather
station over ten years, **7.16 °C**, with the folder it came from,
`weather-project`. Is 7.16 right? The lecture answers in eight steps, each a
section, and each section ends on a number or a file. Every command is
PowerShell 7, the same line on macOS and on Windows.

| Step | Question about 7.16 | Answer, from a typed line |
|--|--|--|
| 1 | Which column of `weather.csv` is the temperature? | `temp_c`, column 2 of 4 |
| 2 | Does the file hold every hour of ten years? | 87 673 lines = 3653 days × 24 hours + the header |
| 3 | Which rows are not measurements? | 120 rows of −999, 22 to 26 July 2019 |
| 4 | Is every other row a measurement? | 87 552 rows fit the pattern of a measured row |
| 5 | The mean without those rows, and with them? | 7.16 and 5.78 °C |
| 6 | Does a second program give the same mean? | `column_stats.py`: 7.15997 |
| 7 | Is my `weather.csv` the file Smiltė used? | SHA-256 `3F1AD06D…FBE00756` |
| 8 | Can anyone run the whole check again? | `./scripts/rebuild.ps1` |

## What the lecture covers

1. **The shell** (slides 5–18): terminal, shell and program; the six things
   the shell does with a line (read, split at spaces, replace variables,
   find the command, run it, note whether it worked); PowerShell 7 on both
   systems, installed with Homebrew on macOS (`brew install --cask
   powershell`) and with `winget` on Windows, and set as the default profile
   of VS Code's terminal; the prompt and `Get-ChildItem` on both systems;
   the commands of Lecture 03 in one table, with the warning that on macOS
   `ls`, `cat`, `cp`, `mv`, `rm` and `mkdir` start the Mac's own programs;
   relative and absolute paths; command, parameter and argument; variables;
   `Tab` and the history; `Get-Command` and `Get-Help`; three error
   messages; the four columns of `weather.csv`.
2. **Read and count** (slides 19–22): the first and last lines; 87 673
   lines, derived from the calendar (2016, 2020 and 2024 are leap years);
   2 515 215 bytes, 29 bytes for a line of 28 characters and its LF.
3. **Pipes & filters** (slides 23–33): the output and the error stream,
   `>`, `>>` and `2>`; line 5000 worked out by hand (4998 hours = 208 days
   and 6 hours: 27 July 2016, 06:00) and checked with a pipe; lines from
   `Get-Content` against objects from `Import-Csv`; sorting as text (the
   lowest humidity "is" 100 %) and as numbers (34 %); the coldest hours,
   −999 °C; `Where-Object` finds the same 120 rows by physics, below
   −273.15 °C; `Select-String` finds them by text, lines 31 154 to 31 273;
   rows per year with `Group-Object`; every one of 3653 days has 24 rows
   and no hour is there twice.
4. **Regular expressions** (slides 34–42): hours below freezing, 22 472 by a
   fixed text and 22 352 by a pattern; quotes that keep a pattern from the
   shell (`,` makes a list in PowerShell); the signs for one character, for
   how many and for where, each with the part of line 2 it fits and the
   number of lines; `'7.16'` fits 600 lines and none of them is 7.16 °C;
   the 13 forms of the lines (every digit written as 9); the pattern of a
   measured row built piece by piece, each piece checked by a count; the
   121 lines it does not fit are the header and the 120 marked rows.
5. **The mean** (slides 43–46): `weather_valid.csv` with 87 553 lines;
   `Measure-Object -Average` gives 7.15996550621346 without the marks and
   5.78279610365909 with them, derived from the sum 626 869.3; a formula
   for what k marks do to a mean, and one mark already moves the second
   decimal.
6. **Programs and packages** (slides 47–57): `column_stats.py` read as a
   text file; `Get-Command` tells a cmdlet from an application; `PATH`,
   searched top to bottom; what a package is (files, a name and a version,
   dependencies, a repository), shown by `conda install numpy`, which brings
   six more packages; a package manager's jobs in Homebrew and `winget`
   (search, install, list, upgrade, remove; PowerShell, Git, Miniforge);
   `conda` as package and environment manager, channel conda-forge; one
   environment per project (`np.float_` removed in NumPy 2.0), `conda
   create`, `conda activate`; `environment.yml` from `conda env export
   --from-history`; the script gives 7.15997, the same as `Measure-Object`;
   the second script cleans the spreadsheet export, 180 bytes to 148.
7. **Checksums & backups** (slides 58–63): `Get-FileHash` of `weather.csv`;
   what a checksum tells and what it does not; a list of checksums for
   `data/raw` checked with `Compare-Object`, and what it prints after one
   digit changed; the same rows in other bytes (`>` writes LF on macOS and
   CRLF on Windows: 2 511 735 + 87 553 = 2 599 288 bytes), so the README
   names raw files by checksum and made files by lines and result; the
   3-2-1 rule with its arithmetic.
8. **Make it repeatable** (slides 64–73): the README's column table, the
   mark and the result; `scripts/rebuild.ps1`, run after deleting
   everything it makes; the README's three rebuild lines; exit status,
   `$LASTEXITCODE` and `$?`; a script that runs on after a failed line, and
   the two lines that stop it; the same 113 bytes from two runs; a script
   as a record of what was done; the table of the eight steps, answered.

## Showing the slides offline

`node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/04-command-line-and-files/`.

Slide 3 links the project folder as
[`weather_project.zip`](../data/weather_project.zip) (565 KB): both data
files, the README and the two scripts. Every command of the lecture runs on
it.

## The lecture in two hours

The lecture is slides 1–73. Its speaker notes add up to about 142 minutes,
the live moments included; a two-hour slot has about 110 minutes of
teaching. Slide 74 opens the self-check section, and slides 75–86 are its
twelve quizzes: they take no lecture time. To jump, type the slide number
and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–4 | The number to check, and the eight steps |
| 0:06 | 5–18 | Step 1: the shell, PowerShell 7 on both systems, the columns |
| 0:34 | 19–22 | Step 2: 87 673 lines (live) |
| 0:42 | 23–33 | Step 3: streams, the pipe (live), objects, the coldest hours (live), 120 rows |
| 1:06 | 34–42 | Step 4: a regular expression, built and counted |
| 1:23 | 43–46 | Step 5: 7.16 against 5.78 |
| 1:30 | 47–57 | Step 6: programs, packages, a conda environment, the second program |
| 1:51 | 58–63 | Step 7: checksums and backups |
| 2:02 | 64–73 | Step 8: the README, `rebuild.ps1` (live), exit status, 7.16 checked |
| 2:22 | | End |

In a two-hour slot, skip the slides below: about 30 minutes. Each one
deepens a step; none is needed by a later slide.

| Skip if time is short | Slides | Saves |
|--|--|--|
| Read the Prompt, List the Folder; Find a Command and Its Parameters; Read an Error Message | 10, 16, 17 | 6 min |
| Sort as Text or as Numbers; Keep Rows by a Condition; Rows per Year | 28, 30, 32 | 6 min |
| A Point Fits Any Character; The Forms of the Lines | 38, 40 | 4 min |
| What One Mark Does to a Mean | 46 | 2 min |
| A Program Is a Text File; The Second Script | 48, 57 | 4 min |
| What a Checksum Tells; Backups: the 3-2-1 Rule | 60, 63 | 4 min |
| The Same Result, Byte for Byte | 70 | 2 min |

- **Never skip** slide 4 (the eight steps), 7 (what the shell does), 15
  (`Tab`, live), 21 (the count, live), 26 (the pipe, live), 29 (−999,
  live), 31 (the 120 rows), 41–42 (the pattern and what it leaves), 45 (the
  two means), 52 (a package manager), 54–55 (an environment and
  `environment.yml`), 59 and 62 (checksums), 66 (the script, live), 69 (stop
  at the first error) and 72 (the eight steps answered).
- **Each section slide names its step**, and each section ends on a card
  with a ✅ and the step's answer. Point back to slide 4 there.
- **Installing is not done here.** Slides 8 and 9 show the install lines
  for both systems; the room installs in Seminar 4.
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
`weather-project` in VS Code, open its terminal (PowerShell 7, `pwsh`, as the
default profile) and make the font large (`Cmd +` a few times). Make the
folders the lines write into: `New-Item -ItemType Directory -Force
data/processed, results`. Run `clear` before each moment. Running the five
once beforehand also checks the macOS outputs on the slides.

| Slide | What to type |
|--|--|
| 15 | `Get-Con`, `Tab`, a space, `-Tot`, `Tab`, ` 2 da`, `Tab`, `/r`, `Tab`, `/w`, `Tab`, `Enter`; then `↑` brings the line back |
| 21 | `(Get-Content data/raw/weather.csv).Count` |
| 26 | `Get-Content data/raw/weather.csv -TotalCount 5000 | Select-Object -Last 1` |
| 29 | `Import-Csv data/raw/weather.csv | Select-Object -First 3`, then with `↑` add `Sort-Object {[double]$_.temp_c} -Stable |` before `Select-Object` |
| 66 | In VS Code, a new file `scripts/rebuild.ps1` with the four lines below; then `Remove-Item data/processed, results -Recurse`, `./scripts/rebuild.ps1`, `Get-Content results/temp_c.txt` |
| 61, optional | `(Get-FileHash data/raw/*).Hash > data/checksums.txt`; change `6,3` to `6,4` in `daily_export.csv` and save; `Compare-Object (Get-Content data/checksums.txt) (Get-FileHash data/raw/*).Hash`. Change it back and save |

The file of slide 66:

```text
New-Item -ItemType Directory -Force data/processed, results | Out-Null
Select-String ',-999,' data/raw/weather.csv -NotMatch -Raw > data/processed/weather_valid.csv
python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
python scripts/column_stats.py data/processed/weather_valid.csv temp_c > results/temp_c.txt
```

It needs `python` in the terminal: Miniforge's `base`, or the environment
`weather` after `conda activate weather`.

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
2. `Get-Content data/raw/wether.csv > results/out.txt` runs. The file name
   has a typo. What happens?
   *The error is printed on the screen, and `out.txt` is an empty file. The
   error goes to the error stream, which still reaches the screen; `>`
   writes only the output stream, and it makes or empties its file before
   the command runs.*
3. `notes.txt` has five lines. Then `'done' > notes.txt` and
   `'checked' >> notes.txt` run in PowerShell 7. How many bytes does the
   file have on a Mac and on Windows?
   *13 and 15. A single `>` empties the file first, and `>>` adds a second
   line. The letters are 4 + 7 = 11. On macOS each line ends with LF, one
   byte; on Windows with CRLF, two.*
4. `Import-Csv weather.csv | Sort-Object humidity_pct | Select-Object -First 1`
   shows a humidity of 100 as the lowest. Why?
   *`Import-Csv` reads every value as text, and text is compared character
   by character: `1` comes before `3`. `Sort-Object {[int]$_.humidity_pct}`
   compares numbers and puts 34 first.*
5. `Select-String ,-999, data/raw/weather.csv` stops with a ParserError.
   Why?
   *The shell reads the comma itself, as the start of a list, before
   `Select-String` runs. In single quotes, `',-999,'`, every character
   reaches the command unchanged.*
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
8. Two folders on `PATH` hold a program named `python`: `C:\Python312` is
   listed before `C:\Python314`. What does `python --version` print?
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
10. `weather_valid.csv`, made with `>` from the same raw file, has
    2 511 735 bytes on a Mac and 2 599 288 on Windows. What follows?
    *The same 87 553 lines, with LF on the Mac and CRLF on Windows:
    2 599 288 − 2 511 735 = 87 553, one byte per line. The checksums
    differ, the mean does not. The README names such a file by its lines
    and its mean.*
11. A project is kept on a laptop, in a second folder on the same laptop, and
    on a USB stick in the laptop bag. Which part of the 3-2-1 rule is not met?
    *The 1: no copy is in another place. One theft or one fire takes all
    three.*
12. `rebuild.ps1` has no stop lines. Its line 3 runs `python` and fails;
    line 4 works. What does `$?` print after the script?
    *`True`. The script runs every line, and its last line worked. With
    `$ErrorActionPreference = 'Stop'` and
    `$PSNativeCommandUseErrorActionPreference = $true` it stops at line 3,
    and `$?` is `False`.*

## Paired seminar

[Seminar 4](../seminars/seminar_04.md) works on the same weather project in
PowerShell 7: the room installs PowerShell 7, Git and Python with a package
manager, searches `weather.csv` and the project folder by command, gets the
mean temperature, 7.16 °C, and writes a script that makes every result
again.

## What left the deck

On 13 October 2026, after the lecture was given, the deck was rebuilt
around one question, "is 7.16 right?", in eight steps, and moved to
PowerShell 7 on both systems (the course's one shell from that day). The
one-command slides that Lecture 03 already taught became one table. Out
went the step-by-step clicking (opening a terminal in VS Code, the Find box
of VS Code), zsh and `chsh`, capture groups, and from the old section
*Tools & Environments* the shell settings (an alias and a prompt,
`~/.zshrc` and `$PROFILE`, Oh My Zsh) and what `conda init` writes. Package
managers stayed, as a section of their own; the conda environment is three
slides. New: what the shell does with a line, variables, the two streams,
line 5000 by arithmetic, `Where-Object`, quotes and the shell, the forms of
the lines, a pattern built piece by piece, a formula for what a mark does
to a mean, exit status, and a script as a record. The removed slides are in
`lectures/content/parked/04_Command_Line_and_Files.md`, each with a note
saying where it stood.

## Take-aways

- A typed command is a step that can be kept: in the README, in a script,
  for the next file.
- The terminal is the window, the shell reads the line, a program does the
  work. The course's shell is PowerShell 7, the same on macOS and Windows.
- The shell splits a line at spaces and replaces `$names` before the
  command runs; a pattern goes in single quotes.
- A path that starts at the project folder works on every laptop.
- `>` writes the output stream and empties its file first; errors go on
  their own stream. A pipe passes one command's output to the next: lines
  from `Get-Content`, objects from `Import-Csv`.
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
- Two files with the same SHA-256 are the same, byte for byte. A file made
  by `>` has other bytes on Windows; name it by its lines and its result.
- A script is the check written down in order. It runs again with one
  line, and with two stop lines it ends at the first error and reports it.
