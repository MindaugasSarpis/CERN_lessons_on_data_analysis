# 4: Command Line & File Handling

The lecture works on files with typed commands, because a step that was
typed can be written down, checked and run again. It starts from nothing:
what a terminal and a shell are, how to get the same shell onto every
laptop, and one command per slide. Every command is shown in two shells side
by side: `zsh` on macOS and PowerShell 7 on Windows.

One small project folder runs through the lecture: `weather-project`, the
log of a weather station. The station is made up. A script generated its
files for the course, and they behave like a real station's log. The
lecture opens with three questions about the log: how many lines, what is on
line 5000, and which hour was the coldest. Typed lines answer all three. The
third answer is −999 °C, which is not a measurement but the mark the
logger wrote while its thermometer was down.

## What the lecture covers

1. **Set up the shell**: terminal, shell and program as three things; one
   shell per system; on macOS, check that the shell is `zsh` and make it the
   default with `chsh -s /bin/zsh` if an old account still starts bash; on
   Windows, the two PowerShells, PowerShell 7.6.6 installed with one
   `winget` line, and opened as `pwsh`; the terminal of VS Code and its
   default profile.
2. **First commands**: the prompt read part by part; `echo`; `pwd`, `ls`
   and `cd`; absolute and relative paths, `.`, `..` and `~`; program,
   option and argument; spaces in names; `Tab`; history, `Ctrl+C` and
   `clear`; `man` and `Get-Help`; reading an error message.
3. **Files & folders**: `head`, `tail` and `Get-Content`; `cat`; counting
   lines (87 673 = 3653 days × 24 hours + the header) and bytes; `mkdir`,
   `cp`, `mv`, `rm`; the wildcards `*` and `?`; the project folder as habits
   at the prompt.
4. **Pipes & filters**: `>` and `>>`, and why the same two lines take 26
   bytes on a Mac and 28 on Windows; the pipe, which carries text in `zsh`
   and objects in PowerShell; columns with `cut` and `Import-Csv`; sorting
   as text and as numbers (the lowest humidity is not 100 %); the ends of
   the temperature column, where −999 shows up; `grep` and `Select-String`
   find the 120 marked hours, 22 to 26 July 2019; rows per year with
   `uniq -c` and `Group-Object`; `data/processed/weather_valid.csv`.
5. **Regular expressions**: a pattern in place of a fixed text (hours below
   freezing: 22 352, not 22 472); the signs for one character, for
   repetition and for a place in the line, each with the lines it fits in
   the spreadsheet export; the Find box of VS Code; capture groups.
6. **Programs someone else wrote**: a program as a text file; the handed-out
   `clean_export.py` run with one line, 148 bytes in both shells; where 158
   bytes come from when PowerShell writes the lines; the handed-out
   `column_stats.py`; what 120 marked rows do to a mean, 7.16 against
   5.78 °C.
7. **Tools & environments**: where a program comes from; `PATH`, and why a
   stand-in in `WindowsApps` answers `Python was not found`; a package
   manager's five jobs, with `winget` and Homebrew; pip and PyPI;
   `pip install numpy` measured; one shared Python breaking a project; a
   virtual environment; `requirements.txt`.
8. **Checksums & backups**: SHA-256 as one command in each shell; a list of
   checksums for `data/raw`; one digit changed; how files are lost; the
   3-2-1 rule with its arithmetic.
9. **The README**: what a stranger still asks; columns and units; how to
   rebuild, one line per shell, and its test; the licence; which copy of
   the cleaned export the README means.

## Before the lecture

- Download [`weather_project.zip`](../data/weather_project.zip) and unzip
  it into `Documents` on each laptop you show. It holds the folder
  `weather-project`: the README, `data/raw/weather.csv`,
  `data/raw/daily_export.csv`, and in `scripts` the two handed-out programs
  [`clean_export.py`](../data/cli_clean_export.py){ download="clean_export.py" }
  and [`column_stats.py`](../data/cli_column_stats.py){ download="column_stats.py" }.
  The files are made by
  [`weather_files.py`](../data/weather_files.py){ download="weather_files.py" }.
- Open the folder in VS Code (**File > Open Folder**) with a terminal in the
  Panel. Python 3.14 from python.org is needed from slide 59 on.
- **Run once before the lecture, and correct the slide if it differs.**
  These lines were not run on a Mac or on Windows: the `chsh` dialogue
  (slide 11), the `winget` output (slide 13), the `ls` table of PowerShell
  (slide 20; its date column follows the laptop's settings), `which python3`
  and `(Get-Command python).Source` (slide 64), the two `PATH` listings
  (slide 65). Every other output was run in `zsh` 5.9 and PowerShell 7.6.6
  on Linux on the same files; macOS formats (`wc`, `uniq -c`, error
  messages) and the Windows CRLF sizes were then written by hand from the
  rules on the slides. The pip and venv numbers (slides 67–72) are from
  Python 3.14.8 on Linux.
- **The demos leave files behind**: `results/note.txt`, `results/copy.csv`,
  `data/processed/daily.csv`, `data/processed/weather_valid.csv`,
  `data/checksums.txt`, `.venv`, `requirements.txt`. Unzip a fresh copy for
  the next group.

To show the slides offline: `node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/04-command-line-and-files/`.

## The lecture in 90 minutes

The lecture is slides 1–86. Its speaker notes add up to about 160 minutes.
The plan below takes 91 of them: it keeps every idea the core of Seminar 4
uses, and leaves the ideas of the seminar's optional sections (regular
expressions, the virtual environment, the list of checksums) for a longer
slot. Slide 87 opens the self-check section, and slides 88–97 are its ten
quizzes: they take no lecture time. To jump, type the slide number and
press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–2, 4–6 | The goal, the folder, one row, three questions |
| 0:09 | 7–15 | Set up the shell: zsh on macOS, PowerShell 7 on Windows, the terminal of VS Code |
| 0:25 | 16–26, 29 | Prompt, `echo`, `pwd`, `ls`, `cd`, paths, the parts of a command, spaces, `Tab`, an error |
| 0:45 | 30–31, 33–38 | `head` and `tail`, counting lines and bytes, `mkdir`, `cp`, `mv`, `rm`, wildcards |
| 0:59 | 40–41, 43, 46–48, 50 | `>`, the pipe, `sort`, the ends of a column (−999), `grep`, `data/processed` |
| 1:12 | 57, 59, 62 | `clean_export.py` run and measured, what 120 rows do to a mean |
| 1:18 | 63, 65 | `PATH`, and "Python was not found" |
| 1:22 | 73–74 | The checksum of a file |
| 1:25 | 79, 82, 85–86 | How to rebuild, which copy the README means, the Recap |
| 1:31 | | Move to the seminar |

The second table lists what the plan skips. In a 2-hour slot, add the rows
marked **add**: about 20 minutes.

| Skipped in 90 minutes | Slides | Saves | 2-hour slot |
|--|--|--|--|
| Learning Objectives | 3 | 1 min | |
| History, Stop, Clear; Help on a Command | 27–28 | 4 min | |
| The Whole File: `cat`; The Project Folder, from the Shell | 32, 39 | 3 min | |
| 24 Characters, 26 or 28 Bytes | 42 | 2 min | add |
| The Pipe Carries Text or Objects; Columns | 44–45 | 4 min | add |
| Count Groups: `uniq -c` | 49 | 2 min | |
| Regular Expressions; A Pattern Instead of a Text | 51–52 | 3 min | add |
| Signs for One Character; Signs for How Many and Where; the Find box; Capture Groups | 53–56 | 12 min | |
| A Program Is a Text File; A Program for 87 672 Rows | 58, 61 | 4 min | add |
| Where 158 Bytes Come From | 60 | 2 min | |
| Where a Program Comes From; A Package Manager; pip; `pip install numpy`; One Python, Every Project | 64, 66–69 | 10 min | |
| A Virtual Environment; requirements.txt | 70, 72 | 5 min | add |
| An Empty Environment, Filled | 71 | 2 min | |
| A List of Checksums for `data/raw` | 75 | 2 min | add |
| One Digit Changed; How Files Are Lost; the 3-2-1 Rule | 76–78 | 5 min | |
| What a Stranger Asks; Columns and Units; Test the Section; The Licence | 80–81, 83–84 | 9 min | |

- **Never skip** slide 6 (the three questions), 17 (the prompt), 19–21
  (`pwd`, `ls`, `cd`), 23 (relative paths), 24 (the parts of a command),
  43 (the pipe), 47–48 (−999 found, and where), 62 (the mean), 65 (`PATH`),
  74 (the checksum), 85 (which copy) and 86 (the Recap).
- **The three questions of slide 6 are answered on slides 33, 43 and 47.**
  Point back to slide 6 at each.
- **A room that had Lecture 02 in its version of 12 October** has met the
  mark −999 already, found there with `Ctrl+F`. Slide 47 then becomes the
  same check by a typed line: ask the room what the coldest hour will be
  before running it. In 2026 the room had the earlier Lecture 02, so the
  mark is new to it.
- **Slides 10–15 are for both systems.** Show your own system live and read
  the other aloud. Installing is done with the room in the seminar, not
  here.
- **Every speaker note has the same form**: **Do** (what to type or show),
  **Say** (the one point of the slide), **Ask** (a question for the room),
  **If asked** (the detail kept off the slide), then the minutes. In
  presenter mode the note is on the right of the slide.
- **Slide 76** (One Digit Changed): change the digit in a copy of the
  project, never in the folder of the lecture.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 87–97: ten quiz slides for students to try afterwards. The same
questions, with their answers:

1. The terminal is in `weather-project/results`. Which path names the raw
   weather file, in `zsh` and in PowerShell alike?
   *`../data/raw/weather.csv`. Two points go up one level, from `results` to
   `weather-project`, and from there the path goes down into `data` and
   `raw`. A path that starts with `/` starts at the top of the disk, and `~`
   is the home folder.*
2. `notes.txt` has five lines. Then `echo done > notes.txt` and
   `echo checked >> notes.txt` run. How many bytes does it have in `zsh` on
   a Mac and in PowerShell 7 on Windows?
   *13 and 15. A single `>` empties the file first, and `>>` adds a second
   line. The letters are 4 + 7 = 11. `zsh` ends each line with LF, one
   byte; PowerShell on Windows with CRLF, two.*
3. `cut -d, -f3 weather.csv | sort | head -n 1` prints 100 as the lowest
   humidity. Why?
   *Without `-n`, `sort` compares text character by character, and `1`
   comes before `3`. `sort -n` compares numbers and puts 34 first; in
   PowerShell `[int]` in `Sort-Object` does the same.*
4. In PowerShell, `ls data/raw | Sort-Object Length` lists
   `daily_export.csv` (180 bytes) before `weather.csv`. What does the pipe
   carry?
   *File objects, each with properties such as `Name` and `Length`.
   `Sort-Object` reads the property `Length` of each. A `zsh` pipe carries
   lines of text: `wc -c data/raw/* | sort -n` finds the size as the first
   word of each line.*
5. A file has the four lines `2025-10-01,6.3`, `2025-10-06,10.4`,
   `date,temp_c` and `7;2025-10-07;9,2`. Which lines does the pattern
   `^[0-9-]+,[0-9]+\.[0-9]$` find?
   *The first two: a whole line of digits and minus signs, a comma, a
   number, a point and one digit. The header has letters, and the line with
   semicolons has a semicolon where only digits and minus signs may stand.*
6. A column has 1000 rows. Ten hold the mark −999 for a missing value, and
   the other 990 have the mean 2.0. What is the mean of all 1000 values?
   *(1980 − 9990) / 1000 = −8.01. One row in a hundred gives the mean the
   wrong sign. The marked rows are taken out first.*
7. On a Mac, `shasum -a 256 daily.csv` prints `33fe5e77…f705483d`. On
   Windows, `Get-FileHash daily.csv` prints `33FE5E77…F705483D`. What
   follows?
   *The two files hold the same 148 bytes. `Get-FileHash` computes SHA-256
   too and writes the digits in capitals. The line endings count: the same
   table with CRLF has 158 bytes and the checksum `b68430c5…`.*
8. A project is kept on a laptop, in a second folder on the same laptop, and
   on a USB stick in the laptop bag. Which part of the 3-2-1 rule is not met?
   *The 1: no copy is in another place. One theft or one fire takes all
   three.*
9. Two folders on `PATH` hold a program named `python`: `C:\Python312` is
   listed before `C:\Python314`. The terminal types `python --version`.
   Which Python answers?
   *Python 3.12. The shell goes through `PATH` in order and runs the first
   program of that name it finds; a newer version further down is never
   reached.*
10. A colleague receives the project folder without `.venv`.
    `requirements.txt` holds the line `numpy==2.5.4`. Which lines give them
    the same environment?
    *`python -m venv .venv`, activate it, then
    `python -m pip install -r requirements.txt`. The `==` pins the version,
    so numpy 2.5.4 arrives and not the newest one. A copied `.venv` holds
    the paths of the other laptop.*

## Paired seminar

[Seminar 4 — Work on Files from the Shell](../seminars/seminar_04.md) does
the ideas of this lecture with the room, in the same order and in both
shells, on files of its own: two years of hourly counts from two made-up
bicycle counters. The room installs PowerShell 7, Git and Python, builds a
project folder with `mkdir`, reads and counts the files, finds the mark
`9999` at an end of the count column and the broken week behind it, writes
a clean copy, runs `clean_export.py` and `column_stats.py`, gets one
checksum on every laptop, and writes the README. Bytes, regular
expressions, a virtual environment, a list of checksums and a test of the
README are its optional sections.

## What left the deck

The deck was rebuilt on 4, 6 and 11 October 2026, and again on 12 October.
The rebuild of 12 October replaced the pendulum table and the LHCb file by
the weather station, so the lecture assumes no example from an earlier
week, and it introduces the command line from the start, one step per
slide: the shells are installed and checked before the first command. The
notes on Windows PowerShell 5.1 went, because the room uses PowerShell 7
from slide 14 on. The earlier versions are in the history of the
repository; the slides parked before are in
`lectures/content/parked/04_Command_Line_and_Files.md`.

## Take-aways

- A typed command is a step that can be kept: in the README, in a script,
  for the next file.
- The terminal is the window, the shell reads the line, a program does the
  work. On macOS the shell is `zsh`, on Windows PowerShell 7.
- A command is a program, its options and its arguments. A space ends an
  argument.
- A path that starts at the project folder works on every laptop. A path
  that starts with `/Users/ada` or `C:\Users\ada` works on one.
- `>` empties the file it writes to. A command never writes into the file it
  reads, and never into `data/raw`.
- A pipe joins programs: text in `zsh`, objects in PowerShell.
- The two ends of a sorted column are the first check of a data file. In
  `weather.csv` they show −999, the mark of 120 hours without a temperature.
- A mark for a missing value that is written as a number is counted as one:
  120 rows of 87 672 move a ten-year mean from 7.16 to 5.78 °C.
- A regular expression describes a kind of text. The counter of the Find box
  is its check.
- The same lines written by the shell take one byte per line more on
  Windows: CRLF. A program that states its line break writes the same bytes
  on every system.
- The shell finds a program in the folders of `PATH`, in order, and stops at
  the first.
- A package manager installs programs by name with a typed line that can be
  kept: `winget` for the system, pip for one Python. A virtual environment
  gives a project a Python of its own; `requirements.txt` makes it again.
- Two files with the same SHA-256 are the same, byte for byte. A list of
  checksums guards `data/raw`. Three copies, on two kinds of storage, one of
  them in another place.
- A README names a file by its size and checksum and keeps the lines that
  rebuild every file, one per shell.
