# 13: Reproducible Workflows & Automation

Lecture 12 turned the hand cleaning of the first weeks into a script. The
project folder now holds scripts that clean, plot and fit the pendulum
table, and each of them was run by hand. Lecture 13 opens by deleting
`results/` and asking the room to write down what brings it back. It then
writes down what surrounds the scripts: which files they work on, which
packages they need, in which order they run, and how anyone knows that the
result is right. It is the last scheduled lecture, and it closes on the four
aims of Lecture 1, each answered by a file of one project folder.

The objectives of the lecture: give a script a command line with
`argparse` and keep its parameters in a config file; build an environment
and write its versions into `requirements.txt`; rebuild every result with
one command that reruns only what is out of date; write a test with
`pytest` and read a failed one; draw the pipeline as a diagram written as
text; say what continuous integration, containers and FAIR add when a
project leaves the laptop.

## What the lecture covers

One pipeline runs through the whole lecture: the raw pendulum file, the
cleaned table, a plot, a fit of *g*, and a report with the number in it.
Every command and every output on the slides was produced by running it.
A shell line is shown for zsh (`%`) and for PowerShell 7 (`PS>`) where the
two differ, and once where it is the same (`python`, `pip`, `git`; on macOS
`python3` until the environment is active).

1. **From steps by hand to a pipeline** — `results/` deleted, and the room
   writes on paper what brings it back; the project as it is; five things
   that go wrong when steps are done by hand, each with its remedy; what
   *reproducible* means and how it differs from *replicable*; the pipeline
   as a diagram, written as text in Mermaid; the project folder of
   Lecture 4 with five new entries.
2. **A script with a command line** — file names leave the code; `sys.argv`;
   `argparse` with positional arguments, options, types, defaults and
   `--help`; the cleaning as a function; a file that is a command and a
   module (`if __name__ == "__main__":`); docstrings; exit codes, read with
   `$?` in zsh and `$LASTEXITCODE` in PowerShell; the parameters of the fit
   in `config.json`, and one parameter that changes *g* from 9.84 ± 0.06 to
   9.81 ± 0.02 m/s²; *g* by method, the five values of Lectures 9, 10 and
   13 in one table; results written as data (`fit.json`) and a report
   written by a script.
3. **Environments** — one program that prints two answers under two
   versions of pandas; what the scripts import; `venv`; an empty
   environment as a test; `pip freeze > requirements.txt`; what pinned
   versions fix and what they do not; conda and uv; `.vscode/extensions.json`.
4. **One command** — when a file is out of date, as a rule on file times,
   worked on a table of ten files; `run_all.py` in three parts (the stages
   as a table, the rule as a function, the loop); four cases run for real;
   delete and rebuild, checked with `git status` and a checksum, which
   answers the question of the opening; Make as the same table in another
   notation, and why Windows does not have it; Snakemake.
5. **Tests** — the decimal comma left out: two stages end without an error
   and the plot is a straight line; `assert`; a first test file; running
   pytest and reading a failure; floats and `pytest.approx`; a fit tested
   on data with a known answer; what is worth a test; the tests inside the
   one command.
6. **Beyond one laptop** — what goes into Git; the second version of the
   README's *How to rebuild* of Lecture 4; continuous integration; Docker;
   large data as a pointer (Git LFS, DVC); FAIR, checked on the LHCb record
   and on the pendulum project; the four aims of Lecture 1, answered.

## The pipeline of the lecture

| Stage | Reads | Writes |
|--|--|--|
| `scripts/clean.py` | `data/raw/pendulum.csv` | `data/processed/pendulum.csv` |
| `scripts/plot.py` | the cleaned table | `results/pendulum_plot.png` |
| `scripts/fit.py` | the cleaned table, `config.json` | `results/fit.json` |
| `scripts/report.py` | the cleaned table, `fit.json`, the plot | `results/report.md` |

`run_all.py` at the top of the project runs the tests and then every stage
whose output is out of date. The files are those of
[Seminar 13](../seminars/seminar_13.md), where they can be downloaded.

The numbers that the slides quote, all from one run on macOS with Python
3.13.9, pandas 3.0.6, NumPy 2.5.3, Matplotlib 3.11.2, SciPy 1.18.1 and
pytest 9.1.1:

- The cleaned table has 97 bytes and the SHA-256 `be05af03…fff0870b`, the
  checksum that Lecture 4 wrote into the README for the table of the
  handed-out `clean_pendulum.py`. `report.md` has the SHA-256
  `1bf0d728…fb3f`. Both were checked again in PowerShell 7.6 on Windows,
  after `Remove-Item -Recurse data/processed, results` and
  `python run_all.py`.
- The fit gives a slope of 4.014 ± 0.025 s²/m and *g* = 9.84 ± 0.06 m/s².
  Forced through the origin it gives 4.024 ± 0.009 s²/m and
  *g* = 9.81 ± 0.02 m/s².
- *g* by method, all from the same nine rows: the weighted mean of
  Lecture 9, 9.805 ± 0.042; the weighted fit of Lecture 10 (0.1 s on each
  timing) through the origin, 9.806 ± 0.042, and with a free intercept,
  9.845 ± 0.090; the unweighted fits of `fit.py`, 9.810 ± 0.023 and
  9.836 ± 0.062.
- `requirements.txt` has 17 lines. The environment folder has 300 MB.
- With pandas 2.3.3, NumPy 2.3.5, Matplotlib 3.10.7 and SciPy 1.16.2 the
  three text results have the same bytes, and the picture differs: 20 868
  bytes against 21 965.

## The lecture in 90 minutes

The lecture is slides 1–65 and estimates about 141 min. Slides 66–73 are the
self-check quizzes and take no lecture time. For a 90-minute slot, skip
the slides in the second table. In a 2-hour slot, skipping slides 32–34
and 60–61 alone brings the estimate to about 128 min. To jump, type the
slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–3, 5–9 | `results/` deleted and the lists on paper, the project as it is, what breaks by hand, what reproducible means, the pipeline as a diagram |
| 0:14 | 12–13, 15, 18–19, 21–22, 25 | The command line: file names in the code, argparse, the cleaning as a function, a command and a module, exit codes in both shells, the config file, results as data |
| 0:31 | 26–27, 29, 31 | Environments: two answers from one program, venv in zsh and PowerShell, `requirements.txt` |
| 0:41 | 35–43 | One command: the rule, the worked example, `run_all.py`, four cases, delete and rebuild. Slide 43 answers the opening at about 1:00 |
| 1:02 | 46–51, 55 | Tests: the plot that looked fine, assert, the first test, pytest, a failure, tests in the one command |
| 1:17 | 56, 58–59, 63–65 | How to rebuild, second version; continuous integration; FAIR on two cases; recap; the four aims, answered |
| 1:30 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Learning Objectives | 4 | 2 min |
| Diagrams as Text, The Project Folder Extended | 10–11 | 5 min |
| The Words of a Command, The Script Explains Itself, Options | 14, 16–17 | 7 min |
| Docstrings | 20 | 2 min |
| One Parameter Two Results, *g* by Method | 23–24 | 5 min |
| What Do the Scripts Need?, An Empty Environment Is a Test | 28, 30 | 5 min |
| What the File Fixes and What It Does Not, conda and uv, The Editor Has Requirements Too | 32–34 | 7 min |
| Make, Make on Windows and Larger Pipelines | 44–45 | 5 min |
| Floats in a Test, A Test with a Known Answer, What to Test | 52–54 | 8 min |
| What Goes into Git | 57 | 2 min |
| Docker, Large Data, FAIR | 60–62 | 8 min |

Together the rows save about 56 min and bring the estimate to about 85 min,
which leaves a few minutes for the live runs.

- **Do not cut** slide 3 or slide 43. Slide 3 asks the room what brings
  `results/` back; slide 43 is the answer, one line in both shells.
- **Do not cut** slides 36–43. They are one argument: the four commands,
  the rule, the rule worked on file times, the rule as code, the four
  cases, the proof. The seminar writes this file.
- **Do not cut** slides 47–51. Slide 47 is the reason for tests, and slide
  51 finds the same mistake in a quarter of a second.
- **Do not cut** slide 65 (The Four Aims, Answered), the closing slide of
  the lecture and of the course. Its four cards are those of the aims slide
  of Lecture 1, each with the file that now makes it true, and its last line
  answers slide 3.
- **Slide 3**: delete `results/` in the shell of your laptop, give the room
  one minute, and write two or three of the lists on the board. Leave them
  there until slide 43.
- **Slide 38** (The Rule, Worked): cover the right-hand card and do the four
  comparisons with the room.
- **Slides 15–19 are shown live.** Keep the project open in VS Code beside
  the slides. Run `clean.py` with no arguments, with `--help`, and on the
  raw file.
- **Slide 21** shows the exit code in both shells: `echo $?` in zsh,
  `$LASTEXITCODE` in PowerShell, where `$?` prints only `False`.
- **Slides 29–31 are shown live** if the network of the room is good:
  create the environment, show the empty `pip list` and the
  `ModuleNotFoundError`, install, freeze. The installation downloads
  about 50 MB and took 13 s on a fast network. With a weak network, show
  the slides and have the environment ready. PowerShell 7 on Windows runs
  `Activate.ps1` as it is: its default policy, `RemoteSigned`, allows a
  script made on the laptop. If it refuses ("running scripts is disabled
  on this system"), the terminal is Windows PowerShell 5.1 or the laptop
  has a stricter rule: run
  `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once.
- **Slides 42–43 are shown live.** Edit `plot.py`, run; edit
  `config.json`, run; delete `data/processed` and `results`, run, and
  show `git status`.
- **Slide 51** is shown live: take `, decimal=","` out of `clean.py`, run
  `python -m pytest`, read the failure, put it back.
- **Slides 55 and 58** show `5 passed`. With slides 52–54 skipped, say
  that two of the five are tests of the fit, in a second file.

Slides taken out of this deck (A Diagram Git Can Compare; pre-commit) are
kept in `lectures/content/parked/13_Reproducible_Workflows.md`.

Before the session, follow the page of [Seminar 13](../seminars/seminar_13.md)
once on a copy of your project folder. The result is the project that the
slides show. Start the local copy of the slides with
`node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/13-reproducible-workflows/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 66–73: seven quiz slides for students to try afterwards. The same
questions, with their answers:

1. The four stages of the lecture. The files were last changed at: raw data
   08:10, `clean.py` 08:20, `plot.py` 08:25, the table 08:30, the plot
   08:31, `fit.json` 08:32, the report 08:33, `fit.py` 08:50; `config.json`
   and `report.py` at 08:00. Which stages does `run_all.py` run?
   *The fit and the report. `fit.json` is older than `fit.py`, so the fit
   runs. Its new output is then newer than the report.*
2. A script is started as `python scale.py data.csv --factor 2.5`. What is
   `sys.argv[3]`?
   *The string `2.5`. The list is `scale.py`, `data.csv`, `--factor`, `2.5`,
   counted from 0, and every entry is a string.*
3. A test contains `assert 0.1 * 3 == 0.3` and fails. Which line repairs it?
   *`assert 0.1 * 3 == pytest.approx(0.3)`. The product is
   0.30000000000000004.*
4. `pip install requests` in an empty environment installs 5 packages. How
   many lines does `pip freeze > requirements.txt` write?
   *5, each with `==` and its version: every installed package, asked for
   or not. pip itself is left out.*
5. `data/processed` and `results` are deleted, then `python run_all.py`
   runs. `git status` reports only the picture as modified. What is the
   most likely cause?
   *A package, for example Matplotlib, has another version than at the last
   commit. The text results have the same bytes, so the data and the
   numbers are unchanged.*
6. Which is most worth a test: the shade of blue of the points, the number
   of rows of the cleaned table, the resolution of the picture, or the
   wording of a label?
   *The number of rows. It has a right answer that comes from outside the
   code, the lab notebook.*
7. In PowerShell, `python scripts/clean.py` is run without its two file
   names. Which line then prints the exit code, 2: `echo $?`, `$?`,
   `$LASTEXITCODE` or `sys.exit()`?
   *`$LASTEXITCODE`. PowerShell's own `$?` holds only True or False, here
   False; `echo $?` is the zsh form; `sys.exit()` is Python, not a shell
   command.*

## Paired seminar

[Seminar 13 — One Command Rebuilds the Analysis](../seminars/seminar_13.md)
builds the pipeline of the lecture in the room's own project folder. It has
four parts: an environment and `requirements.txt`; the cleaning script with
a command line, and three handed-out stages; `run_all.py`, tried on two
changes and on a rebuild from nothing; one test file, made to fail once.
It uses `run_all.py` and not Make, because Windows has no `make`, in
PowerShell or elsewhere, until it is installed separately. Its last section
replaces the README's *How to rebuild* of Seminar 4 with the second version
of the lecture. All of it is done in class, on the pendulum table of the
project folder, in zsh on macOS and PowerShell 7 on Windows.

## Take-aways

- A result is reproducible when another person, on another computer, at a
  later time, gets the same result from the same data with the same
  analysis. Four things have to be written down: the data, the code with
  its parameters, the versions, and the order of the steps.
- The question of the opening, "delete `results/`, now what?", has a
  one-line answer, the same in zsh and in PowerShell: `python run_all.py`.
- File names are arguments of a script, not part of its code. `argparse`
  gives them names, checks them, and writes the help text.
- A script whose work is in functions, and that ends with
  `if __name__ == "__main__":`, can be run and can be imported. Tests need
  the second.
- A choice that changes the result goes into a config file under Git, not
  into the memory of the analyst. The same nine rows give *g* from 9.805
  to 9.845 m/s² by method; a number in a report comes with its method.
- An environment is a folder that can be thrown away. `requirements.txt`
  is the environment written as text, and it goes into Git.
- A file is out of date when it is missing or older than something it is
  made from, the script included. A program can apply this rule. A person
  forgets.
- Everything a script wrote can be deleted and rebuilt. `git status` or a
  checksum shows that it came back the same.
- A test asserts a fact that is known without the code. It is run by the
  computer, every time.
- A mistake that raises no error is found by a test at the stage where it
  was made, or by luck two stages later.
- A diagram written as text has a history that Git can show.
- Continuous integration, containers and FAIR are the same ideas carried
  past one laptop: a server follows the README, the operating system is
  written down too, and strangers can find and reuse the data.
