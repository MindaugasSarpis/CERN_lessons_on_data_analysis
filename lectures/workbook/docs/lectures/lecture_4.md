# 4: Command Line & File Handling

Lecture 2 cleaned a small table by hand and wrote into the README, in words,
what was done. Lecture 3 went down to the bytes of a file, and Seminar 3
typed `pwd`, `ls`, `cd` and `clear` in the terminal without naming its
parts. Lecture 4 names them and does the work on files with typed commands,
because a step that was typed can be written down, checked and run again.
Every command is shown in two shells side by side: `zsh` on macOS and
PowerShell 7 on Windows. The lecture opens on four copies of the cleaned
pendulum table that look the same and have four sizes, and it ends when the
README names the right one by its size and its SHA-256.

## What the lecture covers

1. **The shell** — the terminal in VS Code, `zsh` and the two PowerShells
   of Windows; terminal, shell and program as three things; cmdlets and
   aliases; the prompt read part by part; program, option (parameter) and
   argument; absolute and relative paths; the keys that save typing; how to
   read an error message, `Python was not found` among them.
2. **Files & folders** — `head`, `tail` and `Get-Content`; `wc` and
   `Measure-Object`, characters against bytes; `mkdir`, `cp`, `mv`, `rm`
   and where the two shells differ; wildcards, and who reads the `*`; the
   project folder of Lecture 2 as habits at the prompt.
3. **Pipes & filters** — output into a file with `>` and `>>`, and why the
   same two lines take 26 bytes on a Mac and 28 on Windows; the pipe, which
   carries text in `zsh` and objects in PowerShell; columns with `cut` and
   `Import-Csv`; sorting as text and as numbers; the two ends of the mass
   column; the mark `-100.0` found by counting repeats; keeping lines, and
   `data/processed/D0_valid.csv`.
4. **Regular expressions** — a pattern in place of a fixed text; the signs
   for one character, for repetition and for a place in the line, each with
   the lines it fits in the pendulum table; the Find box of VS Code and
   capture groups; one pattern in both shells; wildcards against regular
   expressions; a pattern on a file with CRLF.
5. **Programs someone else wrote** — a program as a text file; the
   handed-out `clean_pendulum.py` run with one line, 97 bytes in both
   shells; where 107 bytes come from when the shell writes the lines; the
   handed-out `column_stats.py`, and what 49 marked rows do to a mean.
6. **Checksums & backups** — a checksum by hand, then SHA-256 as a command
   in both shells; the script against the hand; a list of checksums for
   `data/raw`; one digit changed; how files are lost; the 3-2-1 rule with
   its arithmetic.
7. **The README** — what it still lacks; its six parts; columns and units;
   how to rebuild, one line per shell, and its test; the licence; which of
   the four copies the README means.

## The lecture in 90 minutes

The lecture is slides 1–67 and estimates about 141 min (the speaker notes
add up to 143). Slide 68 opens the self-check section, and slides 69–75 are
its seven quizzes: they take no lecture time. For a 90-minute slot, skip
the slides in the second table: that leaves about 90 min. To jump, type the
slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–2, 4–6 | The goal, the hand edits of Lecture 2 as one typed line, four copies of one table, three questions clicked and typed |
| 0:09 | 7–8, 10–13, 15 | The two shells, the prompt, the parts of a command, absolute and relative paths, a command that fails |
| 0:26 | 17–19, 22 | Reading and counting files, characters against bytes, wildcards |
| 0:34 | 25–28, 30–35 | `>` and `>>`, 26 or 28 bytes, the pipe, columns, sorting, the ends of a column, repeats, `D0_valid.csv` |
| 0:54 | 36–38 | Regular expressions: a pattern instead of a text, the signs for one character |
| 1:00 | 45, 47–50 | The cleaning script run and measured, where 107 bytes come from, `column_stats.py`, the mean with and without the marked rows |
| 1:13 | 51–55, 58 | A checksum by hand and by command, the script against the hand, a list of checksums, the 3-2-1 rule |
| 1:24 | 59, 63, 66 | The README: how to rebuild, and which copy it means |
| 1:29 | 67 | Recap |
| 1:30 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Learning Objectives | 3 | 1 min |
| Terminal, Shell, Program | 9 | 3 min |
| Keys That Save Typing | 14 | 2 min |
| A Path That Fails | 16 | 2 min |
| Make, Copy, Move; Delete | 20–21 | 6 min |
| Who Reads the `*`?; The Project Folder, from the Shell | 23–24 | 3 min |
| The Pipe Carries Text or Objects | 29 | 3 min |
| Signs for How Many and Where, the Find box, Capture Groups, One Pattern in Two Shells, Wildcards Are Not Regular Expressions, A Pattern on Another Laptop | 39–44 | 17 min |
| A Program Is a Text File | 46 | 3 min |
| One Digit Changed; How Files Are Lost | 56–57 | 3 min |
| What the README Still Lacks; Anatomy of a README; Columns and Units | 60–62 | 5 min |
| Test the Section; The Licence | 64–65 | 5 min |

- **Never skip** slides 5 (the four copies, the question of the lecture),
  10 (Read the Prompt), 47–48 (the script's 97 bytes in both shells, and
  where 107 come from), 52–54 (the checksum by hand, of a file, and the
  script against the hand), 66 (which copy the README means) and 67 (the
  Recap).
- **The question of slide 5 is answered in steps.** On the 90-minute plan
  slide 19 explains copy B, 96 bytes, by about 0:32, and slide 27 explains
  copies C and D, CRLF, by about 0:40. The full answer, which needs the
  checksum, comes on slide 66 at about 1:27: it cannot come earlier,
  because size alone cannot tell copy A from a copy with one digit
  changed. Point back to slide 5 at slides 19, 27 and 66.
- **The seminar repeats** slides 6, 9–13, 19, 27, 32–35, 47, 49–50,
  53–55, 63 and 66 with the room, in both shells. Slides 39–44 (regular expressions in
  depth) and 60–62 and 64–65 (the rest of the README) are its optional
  sections, so nothing is lost by skipping them here.
- **The lecture is shown live.** Keep VS Code beside the slides, with the
  project folder open and a terminal in it, and type each command when its
  slide comes up. Every command slide has a column for macOS `zsh` and one
  for Windows PowerShell 7: type the column of your own laptop and read the
  other one aloud. The Windows outputs on the slides are from PowerShell
  7.6.
- **Most Windows laptops in the room answer `5` on slide 8 and have no
  Python yet.** They watch the Python lines on the projector and read the
  PowerShell column. Seminar 4 installs PowerShell 7, Python and Git in its
  first 25 minutes.
- **Before the lecture**, the project folder holds `README.md` with the
  line **Cleaned copy**, `data/raw/D0_KPi.csv`, `data/raw/pendulum.csv`,
  `data/processed/pendulum.csv`, `results` with the `report.md` and
  `pendulum_plot.png` of Seminar 1, and in `scripts` the two handed-out
  programs
  [`clean_pendulum.py`](../data/cli_clean_pendulum.py){ download="clean_pendulum.py" }
  and [`column_stats.py`](../data/cli_column_stats.py){ download="column_stats.py" }.
  [`project_after_s1.zip`](../data/project_after_s1.zip) has all of it but
  the two scripts.
- **The live demos leave files behind**: `results/note.txt`,
  `results/copy.csv`, `results/pendulum_ps.csv`,
  `data/processed/pendulum_script.csv`, `data/processed/D0_valid.csv` and
  `data/checksums.txt`, and the folder `backup` until slide 21 deletes it.
  The seminar makes the files in `data` again with the room. Delete them in
  the break, or run the lecture in a copy of the folder.
- **Slide 4** (A Step, Written Down): read the README line aloud, then run
  the typed line once without explaining it. The script is opened on
  slide 46, which the 90-minute plan skips.
- **Slide 56** (One Digit Changed): change the digit in a copy of the
  project, never in the folder of the lecture.
- **Slide 66** (Which Copy? The README Says) is where the lecture arrives.
  Add the line to the README live and run the checksum of your shell.

Before the session, start the local copy of the slides:
`node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/04-command-line-and-files/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 68–75: seven quiz slides for students to try afterwards. The same
questions, with their answers:

1. The terminal is in `analysis-project/results`. Which path names the raw
   pendulum file, in `zsh` and in PowerShell alike?
   *`../data/raw/pendulum.csv`. Two points go up one level, from `results`
   to `analysis-project`, and from there the path goes down into `data` and
   `raw`. A path that starts with `/` starts at the top of the disk, and `~`
   is the home folder.*
2. `notes.txt` has five lines. Then `echo done > notes.txt` and
   `echo checked >> notes.txt` run. How many bytes does it have in `zsh` on
   a Mac and in PowerShell 7 on Windows?
   *13 and 15. A single `>` empties the file first, and `>>` adds a second
   line. The letters are 4 + 7 = 11. `zsh` ends each line with LF, one
   byte; PowerShell on Windows with CRLF, two.*
3. In PowerShell, `Get-ChildItem data/raw | Sort-Object Length` lists
   `pendulum.csv` (130 bytes) before `D0_KPi.csv`. What does the pipe
   carry?
   *File objects, each with properties such as `Name` and `Length`.
   `Sort-Object` reads the property `Length` of each. A `zsh` pipe carries
   lines of text: `ls -l data/raw | sort -n -k5` has to find the size as
   the fifth word.*
4. A file has the four lines `20,9.02`, `100,20.01`, `length_cm,t10_s` and
   `7;80;17,90`. Which lines does the pattern `^[0-9]+,[0-9]+\.[0-9]+$`
   find?
   *`20,9.02` and `100,20.01`: a whole line that is a number, a comma, a
   number, a point and a number. The header has letters, and the line with
   semicolons has no point. `grep -E`, `Select-String` and the Find box find
   the same two lines.*
5. A column has 1000 rows. Ten hold the mark −999 for a missing value, and
   the other 990 have the mean 2.0. What is the mean of all 1000 values?
   *(1980 − 9990) / 1000 = −8.01. One row in a hundred gives the mean the
   wrong sign. The marked rows are taken out first.*
6. On a Mac, `shasum -a 256 pendulum.csv` prints `be05af03…fff0870b`. On
   Windows, `Get-FileHash pendulum.csv` prints `BE05AF03…FFF0870B`. What
   follows?
   *The two files hold the same 97 bytes. `Get-FileHash` computes SHA-256
   too and writes the digits in capitals. The line endings count: the same
   table with CRLF has 107 bytes and the checksum `c06d1344…`.*
7. A project is kept on a laptop, in a second folder on the same laptop, and
   on a USB stick in the laptop bag. Which part of the 3-2-1 rule is not met?
   *The 1: no copy is in another place. One theft or one fire takes all
   three.*

## Paired seminar

[Seminar 4 — Work on Files from the Shell](../seminars/seminar_04.md) does
everything in class, in `zsh` on macOS and PowerShell 7 on Windows. Its
first 25 minutes bring every project folder to the state this lecture
assumed and install PowerShell 7, Python and Git, with the steps of
[Install Python, Git and PowerShell 7](../seminars/install_python_git.md).
The room then names the parts of the prompt and of a command, measures a
text and `D0_KPi.csv` in bytes by command, asks `D0_KPi.csv` the three
questions of slide 6, finds the four far masses and the mark `-100.0`,
writes `D0_valid.csv`, runs `clean_pendulum.py` and finds one checksum,
`be05af03…fff0870b`, on every laptop in the room, runs `column_stats.py`,
writes `data/checksums.txt`, and puts the size, the checksum and **How to
rebuild** into the README. Regular expressions and the rest of the README
are its optional sections.

## What left the deck

The deck was rebuilt on 4 October 2026 and again on 6 October. The second
rebuild dropped Git Bash: every command now stands in `zsh` and in
PowerShell 7, and only the ideas both shells share stay. The cleaning of the
pendulum table by `grep`, `tr` and `cut`, the shell script
`clean_pendulum.sh`, variables, the `for` loop, `ranges.sh`, `find`, the
histogram of the mass column, help pages, the decimal sign and the language
setting, `.*` taking all it can, and the backup routine are parked in
`lectures/content/parked/04_Command_Line_and_Files.md`. The cleaning is now
the handed-out `scripts/clean_pendulum.py`.

## Take-aways

- A typed command is a step that can be kept: in the README, in a script,
  for the next file.
- On macOS the shell is `zsh`, on Windows PowerShell 7. The ideas are the
  same, the words often differ, and a word that is the same can be another
  program.
- A command is a program, its options (parameters) and its arguments. A
  space ends an argument.
- A path that starts at the project folder works on every laptop. A path
  that starts with `/Users/ada` or `C:\Users\ada` works on one.
- `zsh` replaces a wildcard by the names that fit before the program
  starts. PowerShell hands it on, and its own commands replace it.
- `>` empties the file it writes to. A command never writes into the file it
  reads, and never into `data/raw`.
- A pipe joins programs: text in `zsh`, objects in PowerShell.
- The two ends of a sorted column and the count of repeated values are the
  first checks of a data file. In `D0_KPi.csv` they find four far masses
  and the mark `-100.0` in 49 rows.
- A mark for a missing value that is written as a number is counted as one:
  49 rows of 91 583 move the mean decay time from +0.00098 to −0.0525 ns.
- A regular expression describes a kind of text. `[0-9]` works everywhere,
  `\d` does not. A pattern goes in single quotes.
- The same lines written by the shell take 1 byte per line more on Windows:
  CRLF. A program that states its line break writes the same bytes on every
  system.
- Two files with the same SHA-256 are the same, byte for byte. A list of
  checksums guards `data/raw`.
- Three copies, on two kinds of storage, one of them in another place.
- A README names a file by its size and checksum, and keeps the lines that
  rebuild it, one per shell.
