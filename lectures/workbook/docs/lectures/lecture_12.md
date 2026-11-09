# 12: Code That Lasts

Lectures 8 to 11 asked questions of the weather log: how sure 7.16 °C is,
whether it is getting warmer, whether it will freeze tonight, what a language
model does with a prompt. Lecture 12, the last before the presentations,
asks whether the answers will come out the same next year, on another
laptop. It opens on the four measured hours of 21 July 2019: the same two
lines of Python give 25.275 in Python 3.11 and 25.275000000000002 in Python
3.14, so a test that compares them exactly passes on one laptop and fails on
the other. It then takes the files that 7.16 depends on one at a time: the
module `weather.py` and what goes where; objects, with the perceptron of
Lecture 10 as a class; tests, starting from 25.275 worked out by hand;
environments and packages, as a tree of dependencies with ranges and pins;
`scripts/rebuild.sh`, which the room has had since Lecture 4, now with the
tests as its last line. It proves the result by deleting it and making it
again, in the folder and in a fresh clone, with the same checksums, and
closes on FAIR, a checklist for the project and Lecture 1's question: Smiltė's
7.16 and Ben's 7.11, both rebuilt, the difference written down as one
function. Every slide is plain Python or the shell; no library is called on a
slide.

## What the lecture covers

1. **The question**: the mean of four hours in Python 3.11 and 3.14; what
   7.16 depends on, file by file.
2. **Modules**: the four steps behind 7.16 as four functions, the six hours
   and the whole log pushed through them; what goes where (as received, the
   recipe, what the recipe makes); the module and a script that imports it;
   a new column in the file, one edit; a function that returns can be
   checked; a docstring.
3. **Objects**: the objects used since Lecture 5 (`str`, `list`,
   `Figure`); the perceptron of Lecture 10 on one evening, 8 December 2025,
   z = 1.2; the same as a class, run live; a model's numbers kept in a file;
   why library models are objects; a class or functions.
4. **Tests**: the mean of the six hours by hand, 25.275; `assert`; a test
   of `mean` that fails with 25.275000000000002, and the failure read; why
   the last digit is 2; comparing within a tolerance, |x̄ − 25.275| < 10⁻⁹;
   a test of an object; a test of the result file (87 552 rows, 7.16), which
   stops Tomas's change of Seminar 6 (5.78); the test file beside the
   module; a mistake found once gets a test; two kinds of test; a test must
   be able to fail; what a test runner reports.
5. **Environments**: Python 3.12 changed the last digit of 7.16 (the sum
   of the 87 552 hours); pandas brings NumPy, 32 packages for two asked
   for; the environment of weeks 8 to 12, 4 asked for and 89 installed;
   one NumPy that fits every range; the pandas releases since 2023; ranges
   and pins; one pin moves another package; writing an install down; what
   the file fixes and what it does not; a fresh environment as the proof;
   the pinned `environment.yml`.
6. **One command**: `rebuild.sh` as Lecture 4 left it; the tests as its
   last line; `set -e` and the exit status; a wrong mean stops the rebuild;
   why the tests come last; How to rebuild in the README.
7. **Delete and rebuild**: the same three checksums after a delete; a
   fresh clone holds only what was committed; `.gitignore`; a test file
   never committed (pytest's exit status 5); four tests of a reproducible
   result: another folder, laptop, time and system.
8. **The four aims**: FAIR; each aim with its file; the review checklist
   of twelve questions; decide before you look; the weather project checked
   against the twelve questions; a review comment someone can act on;
   Smiltė's 7.16 and Ben's 7.11 on two single days; Ben's way as one more
   function; Lecture 1's question answered.
9. **For the curious**, after the recap and outside the lecture time: file
   names as arguments with argparse; the method in a config file (7.11 and
   7.16 from one script); rebuilding only what changed with Make and
   Snakemake; continuous integration on GitHub; containers; how a test
   runner finds the tests; why `sum` changed in Python 3.12.

## The lecture, part by part

The lecture is slides 1–68 and estimates about 118 min, so in the two-hour
slot **plan to skip the slides of the second table** (about 13 min). Slides
69–76 are the optional section For the Curious, and slides 77–85 the
self-check quizzes; neither takes lecture time. To jump, type the slide
number and press Enter.

| Slides | Part |
|--|--|
| 1–4 | The mean of four hours in Python 3.11 and 3.14 (the question of the lecture); what 7.16 depends on |
| 5–10 | Modules: the steps behind 7.16, what goes where, the module and a script, a new column, a function that returns |
| 12–15, 17 | Objects: since Lecture 5, the perceptron on 8 December 2025, the class run live, why library models are objects |
| 19–32 | Tests: 25.275 by hand, `assert`, the failing test and its reading, the last digit, the tolerance, a test of an object and of the result file, the test file, a mistake found once, two kinds, a test that can fail, the runner |
| 33–39, 41–44 | Environments: the last digit of 7.16, the dependency tree, 89 packages, one NumPy for every range, pandas releases, ranges and pins, writing an install down, what the file fixes, the fresh environment, the pinned file |
| 45–49, 51 | One command: `rebuild.sh`, the tests as its last line, `set -e`, the wrong mean stopped, How to rebuild |
| 52–54, 56–57 | Delete and rebuild, a fresh clone, a test file never committed, four tests of a reproducible result |
| 58–63, 65–68 | FAIR, the four aims, the checklist, decide before you look, the weather project checked, 7.16 and 7.11, Ben's function, Lecture 1's question, the recap |

| Skip | Slides |
|--|--|
| A docstring | 11 |
| A model's numbers kept in a file; a class or functions | 16, 18 |
| One pin moves another package | 40 |
| Why the tests come last | 50 |
| What goes into Git | 55 |
| A review comment someone can act on | 64 |

- **Do not cut** slide 3, the question, or slides 65–67, its answer:
  Smiltė's 7.16 and Ben's 7.11 rebuilt, the difference written down as one
  function.
- **Do not cut** slides 20–25: the test of `mean` that fails on the float,
  read and repaired; slide 34 comes back to it as a change of Python.
- **Do not cut** slides 43, 49 and 53–54: the fresh environment, the wrong
  mean stopped by the tests, the delete and the fresh clone. They are the
  proof the lecture is about, and the steps the seminar repeats.
- **Slides 15, 21, 22, 25 and 66** run plain Python in the browser: the
  perceptron as a class; `assert`; the failing test of `mean`; the
  tolerance; Ben's midrange. Slides 21 and 22 end with `AssertionError` on
  purpose. The first run downloads the Python runtime, so run one before the
  lecture.
- **Slides 6, 14 and 20** reveal a formula and its numbers on a click;
  **slides 47, 53 and 54** build a terminal session one step per click.
- **Every number** on the slides is printed by
  `python figures/src/lasting.py` from `weather.csv`, from the two scripts
  of Lecture 4 run as `rebuild.sh` runs them, and from conda-forge's
  package data of 9 November 2026 (kept in `figures/src/lasting_env.json`).
  The Python 3.11 values were checked in Python 3.11.18, 3.12.12, 3.13.9 and
  3.14.10; every terminal output was run in a copy of `weather-s12.zip`
  with conda 26.9.4.
- **Slides 69–76** (For the Curious) are for time left at the end or for
  students afterwards. The workflow file and the Dockerfile are shown as
  examples and were not run for the slides.

Before the session, start the local copy of the slides: `node
scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/12-code-that-lasts/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 77–85: eight quiz slides for students to try afterwards. The same
questions, with their answers:

1. `assert mean([27.3, 25.6, 24.6, 23.6]) == 25.275` fails: the mean is
   25.275000000000002. What is the repair?
   *Compare within a tolerance: `abs(mean(four) - 25.275) < 1e-9`. The
   code is right; the stored floats are rounded, by 3.6 × 10⁻¹⁵, and the
   tolerance still stops a real mistake such as the −999 left in, 341.4
   away.*
2. Which is the best test for the cleaned file `weather_valid.csv`?
   *It has 87 553 lines: 87 672 hours less the 120 marked −999, plus the
   header, as the README states. A fact from outside the code; comparing the
   script with itself, or with its own last checksum, can never catch a
   mistake.*
3. `environment.yml` holds the line `- pandas=3.1`. Which pandas can a
   fresh environment made next year get?
   *The newest 3.1.x on that day: 3.1.1 or a later fix. `pandas=3.1.1`
   would allow only 3.1.1; a bare `pandas` would allow 4.0 as well.*
4. pandas 3.1.1 needs NumPy ≥ 2.0.2; Matplotlib 3.11.2 needs NumPy ≥ 1.25
   and < 3. Which NumPy can the environment hold?
   *NumPy ≥ 2.0.2 and < 3: one version that lies in every range. On 9
   November 2026 the newest of them was 2.5.4.*
5. In an environment made fresh from `environment.yml`, `rebuild.sh` stops
   at its last line: `No module named pytest`. On the author's laptop it
   passes. What happened?
   *pytest was installed into the author's environment by hand and never
   written into `environment.yml`.*
6. `rebuild.sh` starts with `set -e` and ends with `python -m pytest -q`.
   One test fails. What is `$?` afterwards?
   *1, the exit status of pytest, which the script hands on. The result
   files were written before the tests ran.*
7. After a delete and rebuild, `results/temp_c.txt` has 113 bytes on a Mac
   and 119 on Windows, and the tests pass on both. Why?
   *Windows ends each of the 6 lines with CRLF; the checksums differ, and
   the test reads the numbers, which are the same.*
8. A fresh clone runs `rebuild.sh`, and pytest prints `no tests ran` with
   exit status 5. On the author's laptop: `3 passed`. What is the most
   likely cause?
   *`scripts/test_weather.py` was never committed: a clone holds only
   committed files.*

## Paired seminar

[Seminar 12 · pytest](../seminars/seminar_12.md) does the same with the
real tool. Every student starts from today's folder, a Git repository with
one commit, adds pytest to the `analysis` environment and writes it down,
writes the three tests of the lecture in `scripts/test_weather.py` (one
line, the four hours with a tolerance, the result file), adds `python -m
pytest -q` as the last line of `scripts/rebuild.sh`, sees Tomas's change
stopped, pins the exact versions, deletes the results and makes them again
with the same checksums, and rebuilds a fresh clone of the folder. The last
part adds a test and the one command to the student's own project.

## Slides that left the deck

On 9 November 2026 the old Lecture 13, Reproducible Workflows & Automation,
became Lecture 12 and was rebuilt on the weather project as a lecture of
ideas. The old deck worked on the pendulum table with venv, pip,
`requirements.txt`, PowerShell and a Python script `run_all.py`; the course
uses conda, Git Bash and the `scripts/rebuild.sh` of Lecture 4 (decided on 9
November: no `run_all.py`). The old deck is parked whole in
`lectures/content/parked/decks/13_Reproducible_Workflows.md`; slides parked
from it earlier are in `lectures/content/parked/13_Reproducible_Workflows.md`.

| Earlier slides | What happened | Reason |
|--|--|--|
| Delete `results/`: Which Commands Rebuild It?; Learning Objectives | Replaced by slides 3–4 | The opening is a question with real numbers; no objectives slide |
| A Script with a Command Line (argparse, options, exit codes, a config file, results as data) | Two slides in For the Curious, on the weather project | A tool, not an idea of the main path |
| Environments (venv, `requirements.txt`, conda and uv) | Replaced by slides 33–44 | conda and `environment.yml`, as the room uses them; the dependency tree, ranges and pins as ideas |
| One Command (`run_all.py`, the rule of out-of-date files, Make) | Replaced by slides 45–51; Make in For the Curious | The one command stays `rebuild.sh`; its last line runs the tests |
| Tests (the decimal comma of the pendulum file, `pytest.approx`) | Replaced by slides 19–32 | Tests of the six hours and of the result file; plain `assert` with a tolerance |
| Beyond One Laptop (Git, the README, CI, Docker, Git LFS, FAIR on two cases) | `.gitignore`, the README, FAIR and the four aims on the main path; CI and containers in For the Curious; Git LFS and the pipeline as a Mermaid diagram not carried over | The proof by delete, clone and fresh environment comes first |

## Further reading

- **G. Wilson, J. Bryan, K. Cranston, J. Kitzes, L. Nederbragt and T. K.
  Teal**, *Good Enough Practices in Scientific Computing*, PLoS
  Computational Biology 13, e1005510 (2017): the practices of this lecture,
  for a project of one person.
- **The Turing Way**, the chapters on reproducible environments and code
  testing: book.the-turing-way.org.
- **M. D. Wilkinson et al.**, *The FAIR Guiding Principles for scientific
  data management and stewardship*, Scientific Data 3, 160018 (2016).
- **pytest**, Get started: docs.pytest.org; **conda**, Managing
  environments: docs.conda.io.

## Take-aways

- A result depends on its data, its code, and the versions it ran on:
  Python 3.12 changed the last digit of 7.16.
- Each step is a function that takes its data and returns its result; a
  module holds the functions, a script one question.
- An object keeps numbers together with the methods that use them; a
  library's models are objects with the same two methods, `fit` and
  `predict`.
- A test states a fact known without the code, one fact per test, and has
  been seen to fail once. A computed float is compared within a tolerance.
- A package brings its dependencies, each with a range of versions; the
  package manager picks one version that fits every range. A range follows
  new releases, a pin names one version.
- `environment.yml` is complete only if an environment made from it alone
  runs everything: install, then write it down.
- One command makes every result again and runs the tests last; its exit
  status is 0 only when everything worked.
- A result is reproducible when it survives a delete and a rebuild, a fresh
  clone and a fresh environment, with the same checksums.
- Send the folder, not the number.
