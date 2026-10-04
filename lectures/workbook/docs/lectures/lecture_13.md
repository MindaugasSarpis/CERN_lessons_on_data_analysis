# 13: Reproducible Workflows & Automation

Lecture 12 turned the hand cleaning of the first weeks into a script. The
project folder now holds scripts that clean, plot and fit the pendulum
table, and each of them was run by hand. Lecture 13 writes down what
surrounds the scripts: which files they work on, which packages they need,
in which order they run, and how anyone knows that the result is right. It
is the last scheduled lecture, and it closes the four aims of the course on
one project folder.

## What the lecture covers

One pipeline runs through the whole lecture: the raw pendulum file, the
cleaned table, a plot, a fit of *g*, and a report with the number in it.
Every command and every output on the slides was produced by running it.

1. **From steps by hand to a pipeline** — the project as it is; five things
   that go wrong when steps are done by hand, each with its remedy; what
   *reproducible* means and how it differs from *replicable*; the pipeline
   as a diagram, written as text in Mermaid; the project folder of week 2
   with five new entries.
2. **A script with a command line** — file names leave the code; `sys.argv`;
   `argparse` with positional arguments, options, types, defaults and
   `--help`; the cleaning as a function; a file that is a command and a
   module (`if __name__ == "__main__":`); docstrings; exit codes; the
   parameters of the fit in `config.json`, and one parameter that changes
   *g* from 9.84 ± 0.06 to 9.81 ± 0.02 m/s²; results written as data
   (`fit.json`) and a report written by a script.
3. **Environments** — one program that prints two answers under two
   versions of pandas; what the scripts import; `venv`; an empty
   environment as a test; `pip freeze > requirements.txt`; what pinned
   versions fix and what they do not; conda and uv; `.vscode/extensions.json`.
4. **One command** — when a file is out of date, as a rule on file times,
   worked on a table of ten files; `run_all.py` in three parts (the stages
   as a table, the rule as a function, the loop); four cases run for real;
   delete and rebuild, checked with `git status` and a checksum; Make as
   the same table in another notation; Make on Windows; Snakemake.
5. **Tests** — the decimal comma left out: two stages end without an error
   and the plot is a straight line; `assert`; a first test file; running
   pytest and reading a failure; floats and `pytest.approx`; a fit tested
   on data with a known answer; what is worth a test; the tests inside the
   one command.
6. **Beyond one laptop** — what goes into Git; the README gains *How to
   rebuild*; continuous integration; pre-commit; Docker; large data as a
   pointer (Git LFS, DVC); FAIR, checked on the LHCb record and on the
   pendulum project; the four aims of the course in one folder.

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

- The cleaned table has 97 bytes, the same bytes as the copy cleaned by
  hand in Lecture 2.
- The fit gives a slope of 4.014 ± 0.025 s²/m and *g* = 9.84 ± 0.06 m/s².
  Forced through the origin it gives 4.024 ± 0.009 s²/m and
  *g* = 9.81 ± 0.02 m/s².
- `requirements.txt` has 17 lines. The environment folder has 300 MB.
- With pandas 2.3.3, NumPy 2.3.5, Matplotlib 3.10.7 and SciPy 1.16.2 the
  three text results have the same bytes, and the picture differs: 20 868
  bytes against 21 965.

## The lecture in 90 minutes

The lecture is slides 1–65 and estimates about 140 min. Slides 66–73 are the
self-check quizzes and take no lecture time. For a 90-minute slot, skip
the slides in the second table. In a 2-hour slot, skipping slides 31–33
and 59–61 alone brings the estimate to about 125 min. To jump, type the
slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–8, 10 | The project as it is, what breaks by hand, what reproducible means, the pipeline as a diagram, the extended folder |
| 0:15 | 11–12, 14–15, 17–18, 20–21, 24 | The command line: argparse, the cleaning as a function, a command and a module, exit codes, the config file, results as data |
| 0:34 | 25–26, 28–30 | Environments: two answers from one program, venv, the empty environment, `requirements.txt` |
| 0:44 | 34–42 | One command: the rule, the worked example, `run_all.py`, four cases, delete and rebuild |
| 1:04 | 45–50, 54 | Tests: the plot that looked fine, assert, the first test, pytest, a failure, tests in the one command |
| 1:18 | 55, 57–58, 62, 64–65 | How to rebuild, continuous integration, FAIR, the four aims, recap |
| 1:31 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Diagrams as Text, A Diagram Git Can Compare | 9, 23 | 5 min |
| The Words of a Command, Options, Docstrings | 13, 16, 19 | 7 min |
| One Parameter, Two Results | 22 | 3 min |
| What Do the Scripts Need? | 27 | 2 min |
| What the File Fixes and What It Does Not, conda and uv, The Editor Has Requirements Too | 31–33 | 7 min |
| Make, Make on Windows and Larger Pipelines | 43–44 | 5 min |
| Floats in a Test, A Test with a Known Answer, What to Test | 51–53 | 8 min |
| What Goes into Git | 56 | 2 min |
| pre-commit, Docker, Large Data | 59–61 | 8 min |
| FAIR, Checked on Two Cases | 63 | 3 min |

Together the rows save about 49 min and bring the estimate to about 91 min.

- **Do not cut** slides 35–42. They are one argument: the four commands,
  the rule, the rule worked on file times, the rule as code, the four
  cases, the proof. The seminar writes this file.
- **Do not cut** slides 46–50. Slide 46 is the reason for tests, and slide
  50 finds the same mistake in a quarter of a second.
- **Slide 37** (The Rule, Worked): cover the right-hand card and do the four
  comparisons with the room.
- **Slides 14–18 are shown live.** Keep the project open in VS Code beside
  the slides. Run `clean.py` with no arguments, with `--help`, and on the
  raw file.
- **Slides 28–30 are shown live** if the network of the room is good:
  create the environment, show the empty `pip list` and the
  `ModuleNotFoundError`, install, freeze. The installation downloads
  about 50 MB and took 13 s on a fast network. With a weak network, show
  the slides and have the environment ready.
- **Slides 41–42 are shown live.** Edit `plot.py`, run; edit
  `config.json`, run; delete `data/processed` and `results`, run, and
  show `git status`.
- **Slide 50** is shown live: take `, decimal=","` out of `clean.py`, run
  `python -m pytest`, read the failure, put it back.
- **Slides 54 and 57** show `5 passed`. With slides 51–53 skipped, say
  that two of the five are tests of the fit, in a second file.
- **Slide 64** (The Four Aims, in One Folder) closes the course. Go through
  it with the project open and point at the file behind each sentence.

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
5. After deleting the results and rebuilding, `git status` reports only the
   picture as modified. What is the most likely cause?
   *A package, for example Matplotlib, has another version than at the last
   commit. The text results have the same bytes, so the data and the
   numbers are unchanged.*
6. Which is most worth a test: the shade of blue of the points, the number
   of rows of the cleaned table, the resolution of the picture, or the
   wording of a label?
   *The number of rows. It has a right answer that comes from outside the
   code, the lab notebook.*
7. What makes an analysis scriptable?
   *Every step is code or a command, and all of it can be run again from
   the raw data.*

## Paired seminar

[Seminar 13 — One Command Rebuilds the Analysis](../seminars/seminar_13.md)
builds the pipeline of the lecture in the room's own project folder. It has
four parts: an environment and `requirements.txt`; the cleaning script with
a command line, and three handed-out stages; `run_all.py`, tried on two
changes and on a rebuild from nothing; one test file, made to fail once.
It uses `run_all.py` and not Make, because Git Bash on Windows does not
include `make`. At home students do the same four steps on their own
dataset.

## Take-aways

- A result is reproducible when another person, on another computer, at a
  later time, gets the same result from the same data with the same
  analysis. Four things have to be written down: the data, the code with
  its parameters, the versions, and the order of the steps.
- File names are arguments of a script, not part of its code. `argparse`
  gives them names, checks them, and writes the help text.
- A script whose work is in functions, and that ends with
  `if __name__ == "__main__":`, can be run and can be imported. Tests need
  the second.
- A choice that changes the result goes into a config file under Git, not
  into the memory of the analyst.
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
