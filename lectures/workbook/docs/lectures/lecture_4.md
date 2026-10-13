# 4: Command Line & File Handling

The lecture works on files with typed commands, because a step that was
typed can be written down, checked and run again. It starts from nothing:
what a terminal and a shell are, how to get the same shell onto every
laptop, and one command per slide. Every command is shown in two shells side
by side: `zsh` on macOS and PowerShell 7 on Windows.

One small project folder runs through the lecture: `weather-project`, the
log of a weather station. The lecture opens with three questions about the log: how many lines, what is on
line 5000, and which hour was the coldest. Typed lines answer all three. The
third answer is −999 °C, which is not a measurement but the mark the
logger wrote while its thermometer was down.

## What the lecture covers

1. **Set up the shell**: terminal, shell and program as three things; one
   shell per system; on macOS, `echo $SHELL` (and what a variable is), and
   `chsh -s /bin/zsh` if an old account still starts bash; on Windows,
   Windows PowerShell 5.1 next to PowerShell 7.6.6, installed with one
   `winget` line and opened as `pwsh`; the terminal of VS Code and its
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
7. **Checksums & backups**: SHA-256 as one command in each shell; a list of
   checksums for `data/raw`; one digit changed; how files are lost; the
   3-2-1 rule with its arithmetic.
8. **Tools & environments**: where a program comes from, with Python and
   `conda` from Miniforge; `PATH`, and why a stand-in in `WindowsApps`
   answers `Python was not found`; a package manager's five jobs, with
   `winget` and Homebrew; settings that stay: an alias and a prompt, the
   start-up files `~/.zshrc` and `$PROFILE`, Oh My Zsh, Oh My Posh and
   Starship; what `conda init` wrote into those files, and `(base)` in the
   prompt; `conda` as a package manager and an environment manager, with
   the channel conda-forge; one shared Python breaking a project; an
   environment as a folder (`conda create`, `conda env list`); activation
   as a change of `PATH`; `conda install numpy` measured; `environment.yml`
   from `conda env export --from-history`, and why the full export works
   on one system only.
9. **The README**: what it must still answer; columns and units; how to
   rebuild, one line per shell, and its test; the rebuild lines as a shell
   script (`#!/bin/zsh`, `chmod +x`, `./`), and a script that stops at its
   first error (`set -e`; in PowerShell `$ErrorActionPreference` and
   `$PSNativeCommandUseErrorActionPreference`); the licence; which copy of
   the cleaned export the README means.

## Showing the slides offline

`node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/04-command-line-and-files/`.

Slide 4 links the project folder as
[`weather_project.zip`](../data/weather_project.zip) (565 KB): both data
files, the README and the two scripts. Every command of the lecture runs on
it.

## The lecture in 90 minutes

The lecture is slides 1–89. Its speaker notes add up to about 177 minutes,
live moments included. The plan below takes 91 of them: it keeps every idea
the core of Seminar 4 uses, and leaves the ideas of the seminar's optional
sections (regular expressions, a conda environment for the project, the
list of checksums) for a longer slot. Slide 90 opens the self-check
section, and slides 91–101 are its eleven quizzes: they take no lecture
time. To jump, type the slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–2, 4–6 | The goal, the project folder, the columns of `weather.csv`, three questions |
| 0:09 | 7–11 | Set up the shell: zsh on macOS, PowerShell 7 on Windows |
| 0:19 | 13–14, 16–21, 23, 26 | Prompt, `pwd`, `ls`, `cd`, paths, the parts of a command, `Tab` (live), an error |
| 0:38 | 27–28, 30–34 | `head` and `tail`, counting lines (live) and bytes, `mkdir`, `cp`, `mv`, `rm` |
| 0:51 | 37–38, 40, 43–45, 47 | `>`, the pipe (live), `sort`, the ends of a column (live, −999), `grep`, `data/processed` |
| 1:07 | 54, 56, 59 | `clean_export.py` run and measured, the mean with and without the −999 rows |
| 1:13 | 60–61 | The checksum of a file |
| 1:16 | 68, 73 | `PATH`, "Python was not found", and the `(base)` that `conda init` puts in the prompt |
| 1:21 | 80, 83, 85, 88–89 | How to rebuild, the rebuild script (live), which copy the README means, the Recap |
| 1:31 | | Move to the seminar |

The second table lists what the plan skips. In a 2-hour slot, add the rows
marked **add**: about 29 minutes.

| Skipped in 90 minutes | Slides | Saves | 2-hour slot |
|--|--|--|--|
| Learning Objectives | 3 | 1 min | |
| Open a Terminal in VS Code | 12 | 2 min | |
| Run a Command: `echo`; Spaces in Names | 15, 22 | 2 min | |
| Keys for the Shell; Help on a Command | 24–25 | 4 min | |
| The Whole File: `cat`; Many Files at Once: Wildcards; Where Commands Read and Write | 29, 35–36 | 5 min | |
| Why the Sizes Differ: Line Endings | 39 | 2 min | add |
| zsh Pipes Text, PowerShell Pipes Objects; Pick Columns | 41–42 | 4 min | add |
| Count Rows per Year: `uniq -c` | 46 | 2 min | |
| Regular Expressions; Below Freezing: a Fixed Text or a Pattern | 48–49 | 3 min | add |
| Signs for One Character; Signs for How Many and Where; Regex in VS Code's Find Box; Replace with Capture Groups | 50–53 | 12 min | |
| A Program Is a Text File; The Mean of a Column | 55, 58 | 4 min | add |
| PowerShell's `>` Adds CRLF | 57 | 2 min | |
| A List of Checksums for `data/raw` | 62 | 2 min | add |
| A Changed File Fails the Check; How Files Are Lost; Backups: the 3-2-1 Rule | 63–65 | 5 min | |
| Tools & Environments; Where a Program Comes From; A Package Manager | 66–67, 69 | 5 min | |
| An Alias and a Prompt; A File the Shell Runs at Start; Ready-Made Settings: Oh My Zsh | 70–72 | 6 min | |
| `conda`: Packages and Environments; An Upgrade for One Project Breaks Another; An Environment Is a Folder; Activation Changes PATH | 74–77 | 9 min | add |
| Install numpy into One Environment | 78 | 2 min | |
| Write the Environment Down: `environment.yml` | 79 | 2 min | add |
| What the README Must Answer; Columns and Units; Test the Rebuild Lines; Licence | 81–82, 84, 87 | 9 min | |
| Stop at the First Error | 86 | 3 min | add |

- **Never skip** slide 6 (the three questions), 14 (the prompt), 16–18
  (`pwd`, `ls`, `cd`), 20 (relative paths), 21 (the parts of a command),
  40 (the pipe), 44–45 (−999 found, and where), 59 (the mean), 61 (the
  checksum), 68 (`PATH`), 85 (the rebuild script), 88 (which copy) and 89
  (the Recap).
- **The three questions of slide 6 are answered on slides 30, 40 and 44.**
  Point back to slide 6 at each.
- **A room that had Lecture 02 in its version of 12 October** has met the
  mark −999 already, found there with `Ctrl+F`. Slide 44 then becomes the
  same check by a typed line: ask the room what the coldest hour will be
  before running it. In 2026 the room had the earlier Lecture 02, so the
  mark is new to it.
- **Slides 10–11 are for both systems.** Read both columns. Installing is
  done with the room in the seminar, not here.
- **The slides carry everything.** Every command is on its slide with its
  output in both shells. The few live moments below run the same lines in
  a terminal first; the slide after them is the record.
- **Every speaker note has the same form**: **Live** (a line run in the
  terminal, only on the slides below), **Do** (something done with the
  room: the board, a show of hands), **Say** (the one point of the slide),
  **Ask** (a question for the room), **If asked** (the detail kept off the
  slide), then the minutes. In presenter mode the note is on the right of
  the slide.

## Live in the lecture

Five moments run in a terminal what their slide shows, because a slide
cannot show a key being pressed or a line growing. Each costs about a
minute more than the slide alone, and the minutes above include it. If a
line misbehaves, go to the slide: it has the output.

**Before the lecture.** On the laptop that drives the projector, unzip
[`weather_project.zip`](../data/weather_project.zip), open the folder
`weather-project` in VS Code, open its terminal, make the font large
(`Cmd +` a few times) and shorten the prompt: `PROMPT='%1~ %# '`. Run
`clear` before each moment. Running the five once beforehand also checks
the macOS outputs on the slides.

| Slide | What to type |
|--|--|
| 23 | `head -n 2 da`, then `Tab` three times, `Enter`; then `↑` brings the line back |
| 30 | `wc -l data/raw/weather.csv` |
| 40 | `head -n 5000 data/raw/weather.csv | tail -n 1` |
| 44 | `cut -d, -f2 data/raw/weather.csv | head`, then with `↑` add `| sort -n` before `| head`, then change the last `head` to `head -n 1` |
| 85 | In VS Code, a new file `scripts/rebuild.sh` with the three lines below; then `chmod +x scripts/rebuild.sh`, `rm data/processed/*`, `./scripts/rebuild.sh`, `wc -c data/processed/*` |
| 63, optional | `shasum -a 256 data/raw/* > data/checksums.txt`; change `6,3` to `6,4` in `daily_export.csv` and save; `shasum -a 256 -c data/checksums.txt`. Change it back and save |

The file of slide 85:

```text
#!/bin/zsh
python3 scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv
```

`data/processed` must hold the two files when slide 85 starts, from slide
47 and slide 56 or from the README lines of slide 83: if neither ran live,
`rm` has nothing to remove, which does no harm.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 91–101: eleven quiz slides for students to try afterwards. The same
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
10. A colleague receives the project folder with `environment.yml`, which
    lists `python=3.14` and `numpy=2.5.4`. Which lines give them the same
    environment?
    *`conda env create -f environment.yml`, then `conda activate weather`.
    The file names the channel and the packages, and `numpy=2.5.4` pins the
    version, so 2.5.4 arrives and not the newest one. A copied environment
    folder holds the paths of the other laptop, and `base` is shared by
    every project.*
11. A `zsh` script without `set -e` has three lines. Line 2 fails, line 3
    works. What does `echo $?` print after the script?
    *0. Without `set -e` a script runs every line, and its status is the
    status of its last line. Line 3 worked, so the script reports success,
    and the failure in line 2 is easy to miss. With `set -e` it stops at
    line 2 and reports that line's status.*

## Paired seminar

[Seminar 4 — Work on Files from the Shell](../seminars/seminar_04.md) asks
one question of its own file, two years of hourly counts from two bicycle
counters: how many bicycles pass in an hour? It installs PowerShell 7, Git
and Miniforge first, with VS Code closed, then builds the project folder
from nothing with `mkdir` and starts the README. The room checks the
downloaded file by its checksum, counts its lines and bytes (with a hex
view of the first lines), finds the mark `9999` at an end of a sorted
column, counts the 168 marked rows of one broken week and keeps the others
in `data/processed`. `column_stats.py` gives the answer, 86.3 bicycles an
hour with the mark and 38.6 without. A script then makes every processed
file and result again with one command, a copy saved with CRLF stops it on
a Mac, and the README says what each file is and how to rebuild it. Every
part ends with a task the room solves alone.

## What left the deck

The deck was rebuilt on 4, 6 and 11 October 2026, and again on 12 October.
The rebuild of 12 October replaced the pendulum table and the LHCb file by
the weather station, so the lecture assumes no example from an earlier
week, and it introduces the command line from the start, one step per
slide: the shells are installed and checked before the first command. The
notes on Windows PowerShell 5.1 went, because the room uses PowerShell 7
from slide 11 on. Later on 12 October the section Tools & Environments
changed from python.org, pip, a virtual environment and `requirements.txt`
to Miniforge, `conda` environments and `environment.yml`. In the evening
of 12 October the five install slides became two, *Checksums & Backups*
moved before *Tools & Environments*, two slides on a first shell script
joined the README section, slide 4 got the download link, and five slides
got a live moment. The earlier
versions are in the history of the
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
  that starts with `/Users/smilte` or `C:\Users\smilte` works on one.
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
  kept: `winget` for the system, `conda` for one environment. A conda
  environment is a folder with a Python and packages of its own;
  activation puts it first on `PATH`, and `environment.yml` makes it again
  on any laptop.
- Two files with the same SHA-256 are the same, byte for byte. A list of
  checksums guards `data/raw`. Three copies, on two kinds of storage, one of
  them in another place.
- A README names a file by its size and checksum and keeps the lines that
  rebuild every file, one per shell.
- A script is those lines in a file, run with one command. Without a stop
  line it runs on after a failure and reports success; `set -e` in `zsh`,
  and two lines in PowerShell, end it at the first error.
