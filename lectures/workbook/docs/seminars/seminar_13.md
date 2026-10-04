# Seminar 13 — One Command Rebuilds the Analysis

**Paired lecture:** 13 Reproducible Workflows & Automation · **Format:** follow-along · **~120 min**
in class, 45 min at home

The seminar has four parts, in this order.

1. **An environment.** The project gets its own Python environment, and the
   versions of its packages are written into `requirements.txt`.
2. **Four stages.** The cleaning script gets a command line. Three more
   scripts are added: plot, fit, report. Each is run by hand once.
3. **One command.** `run_all.py` rebuilds what is out of date. The room
   changes a script and a parameter, watches what runs again, then deletes
   every result and gets it back.
4. **One test.** A test of the cleaning is written, run with pytest, and
   made to fail once.

Everything is done on the pendulum table of the project folder. The same
steps on a dataset of the student's own are the work at home.

## How to use this page

This page is written for the person at the front. Students can follow the
same page.

- The **paragraph at the top of a section** is what to tell the room.
- The **numbered steps** are what to do on the projector. The room repeats
  each step on their own laptops.
- **You should now see** closes a section. Ask for hands: "who sees this?"
  Go on when about four in five have it. The rest get help from a neighbour.
- **Watch for** is the usual slip in that section.

Commands are typed in the terminal of VS Code, in the project folder. On
Windows the terminal is Git Bash. Where a command differs between systems,
both forms are given. Keys are written for Windows, with macOS in brackets.

| Clock | Section | The room ends with |
|--|--|--|
| | **Part 1 · An environment** · 30 min | |
| 0:00 | [1. Start from a committed state](#start) | A clean `git status` |
| 0:05 | [2. Create and activate an environment](#venv) | A prompt that starts with `(.venv)` |
| 0:15 | [3. Install, and write down the versions](#freeze) | `requirements.txt`, and `.venv` ignored by Git |
| | **Part 2 · Four stages** · 30 min | |
| 0:30 | [4. Give the cleaning a command line](#cli) | `clean.py` with two arguments and a help text |
| 0:45 | [5. Plot, fit, report](#stages) | A report with *g* in it, written by a script |
| | **Part 3 · One command** · 30 min | |
| 1:00 | [6. Write run_all.py](#run-all) | Four lines that end in `up to date` |
| 1:15 | [7. Change something](#change) | Only the affected stages run again |
| 1:22 | [8. Delete and rebuild](#rebuild) | A clean `git status` after a rebuild |
| | **Part 4 · One test** · 30 min | |
| 1:30 | [9. A first test](#test) | `3 passed` |
| 1:40 | [10. Make it fail](#fail) | A failure read and repaired |
| 1:48 | [11. Tests in the one command, and the README](#readme) | A section **How to rebuild** |
| 1:55 | [12. Wrap up](#wrap-up) | The homework known |

In a 90-minute slot, hand out `clean.py` as a file in section 4 and run
only its steps 2 to 5, skip section 7, and stop after section 10. Sections
7 and 11 are then done at home.

## Prerequisites

For the room:

- The project folder `analysis-project` under Git, with
  `data/raw/pendulum.csv` in it: the file as received, with `;` between the
  values and decimal commas. A student who does not have it downloads
  [`pendulum_raw.csv`](../data/pendulum_raw.csv){ download="pendulum.csv" }
  and drags it onto the `raw` folder.
- Python. On Windows, Git Bash as the terminal of VS Code.

The scripts of this page are complete in themselves. A student may have a
`clean.py`, `plot.py` or `fit.py` from earlier sessions. The files of this
page take their place. Section 1 commits the old ones first, so Git keeps
them.

For you, before the session:

- The whole page done once on a copy of your own project folder.
- The network of the room tried out: section 3 downloads about 50 MB per
  laptop.
- A USB stick with the eight files of this page, in case the network fails:
  [`clean.py`](../data/workflows_clean.py){ download="clean.py" },
  [`plot.py`](../data/workflows_plot.py){ download="plot.py" },
  [`fit.py`](../data/workflows_fit.py){ download="fit.py" },
  [`report.py`](../data/workflows_report.py){ download="report.py" },
  [`config.json`](../data/workflows_config.json){ download="config.json" },
  [`run_all.py`](../data/workflows_run_all.py){ download="run_all.py" },
  [`test_clean.py`](../data/workflows_test_clean.py){ download="test_clean.py" }
  and
  [`test_fit.py`](../data/workflows_test_fit.py){ download="test_fit.py" }.
  The handed-out `run_all.py` is the final one, with the three lines of
  section 11 in it.

## Part 1 · An environment { #part-1 }

**0:00 to 0:30 · sections 1 to 3**

The room ends this part with a folder `.venv` that holds the packages of
this project, and a file `requirements.txt` that says which versions they
are.

## 1. Start from a committed state { #start }

**0:00 · 5 min**

Today adds files to the project and replaces three that were made by hand:
the cleaned table, the plot and the report. Before anything is replaced,
the present state is committed. Git then keeps the versions made by hand.

1. Open the project folder in VS Code and select **Terminal** >
   **New Terminal**. On Windows, check the name at the top right of the
   Panel: it reads `bash`.

2. Type `git status` and press Enter.

3. If it lists changes or untracked files, commit them.

    ```text
    git add -A
    git commit -m "State before the pipeline"
    ```

4. Type `ls`. The list has `README.md`, `data`, `results` and `scripts`.

You should now see `nothing to commit, working tree clean` as the last line
of `git status`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `fatal: not a git repository` | The folder is not under Git yet. Run `git init`, then the two commands of step 3 |
    | Windows: the Panel reads `powershell` | Open the list beside the `+` at the top right of the Panel and select **Git Bash** |

## 2. Create and activate an environment { #venv }

**0:05 · 10 min**

An environment is a folder with its own `python` and its own packages. This
project gets one, named `.venv`, inside the project folder. Whatever is
installed while it is active goes into that folder and nowhere else. The
packages installed on the laptop over the semester stay as they are.

1. Create the environment. The command prints nothing and takes a few
   seconds.

    ```text
    Windows          python -m venv .venv
    macOS, Linux     python3 -m venv .venv
    ```

2. Activate it.

    ```text
    Windows          source .venv/Scripts/activate
    macOS, Linux     source .venv/bin/activate
    ```

    The prompt now starts with `(.venv)`.

3. Type `which python`. The answer is a path inside the project folder that
   ends in `.venv/bin/python`, on Windows in `.venv/Scripts/python`. From
   here on the command is `python` on every system.

4. Type `pip list`. A new environment holds `pip` and nothing else. On a
   Python older than 3.12 it also holds `setuptools`.

5. Press `Ctrl+Shift+P` (macOS `Cmd+Shift+P`), type `interpreter` and select
   **Python: Select Interpreter**. Choose the entry with `.venv` in it.

6. Close the terminal with the bin icon at the top right of the Panel and
   open a new one. If its prompt does not start with `(.venv)`, repeat
   step 2. An environment is activated in every new terminal.

You should now see `(.venv)` at the start of the prompt, and a folder
`.venv` in the Side Bar.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `python: command not found` in step 1 | The command is `python3` there. After the activation it is `python` |
    | Windows: `source` is not recognized | The terminal is PowerShell. Select **Git Bash** in the list beside the `+` |
    | Linux: `ensurepip is not available` | Install the package the message names, `python3-venv`, and repeat step 1 |
    | **Python: Select Interpreter** is not in the list | The Python extension is missing. Install it from the Extensions view |

## 3. Install, and write down the versions { #freeze }

**0:15 · 15 min**

The new environment is empty. That makes it a test: it shows which packages
this project needs. Four are installed. Then the versions of everything
that arrived are written into a file. The file goes into Git. The folder
`.venv` does not: it is large, and it can be made again from the file.

1. Install the four packages. This downloads about 50 MB. It took 13 s
   on a fast network. Allow a few minutes when the whole room downloads
   at once.

    ```text
    pip install pandas matplotlib scipy pytest
    ```

    The last line begins with `Successfully installed` and names more than
    four packages: each package brings the packages it needs.

2. Type `pip list` and find `numpy` in the list. Nobody asked for it. pandas
   did.

3. Write the versions into a file.

    ```text
    pip freeze > requirements.txt
    ```

4. Open `requirements.txt`. One line per package, each with `==` and an
   exact version. On the day this page was checked the file began:

    ```text
    contourpy==1.4.0
    cycler==0.12.1
    fonttools==4.66.1
    ```

    The room's versions are those of today and may be newer.

5. Create a file `.gitignore` at the top of the project, or open the one
   that is there, and add four lines.

    ```text
    .venv/
    __pycache__/
    .pytest_cache/
    data/processed/
    ```

6. Commit the two files.

    ```text
    git add requirements.txt .gitignore
    git commit -m "Environment with pinned versions"
    ```

You should now see `requirements.txt` in the Side Bar, and a `git status`
that does not mention `.venv`. The file had 17 lines on macOS on the day
this page was checked. On Windows pandas and pytest ask for two packages
more, `tzdata` and `colorama`, so the file is longer there.

Say what the file is for: on another laptop,
`pip install -r requirements.txt` in a new environment installs exactly
these versions.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `error: externally-managed-environment` | The environment is not active. Section 2, step 2 |
    | Source Control shows thousands of changes | `.gitignore` is not saved, is named `.gitignore.txt`, or is not at the top of the project |
    | The installation stops with a network error | Run the command again. It continues where it stopped |

## Part 2 · Four stages { #part-2 }

**0:30 to 1:00 · sections 4 and 5**

The analysis is four steps: clean, plot, fit, report. Each becomes a script
that is told on the command line which files to read and which file to
write.

## 4. Give the cleaning a command line { #cli }

**0:30 · 15 min**

The raw table was cleaned by hand in the first seminar, with Find and
Replace and a cursor on every line. The same four edits are four lines of
pandas. Today they become a function, and the script around it takes two
arguments: the file to read and the file to write. No file name is typed
into the code.

1. Select the `scripts` folder, then **New File**, and type `clean.py`. If
   the file exists, open it and delete its content. Copy the block below
   with the button in its corner, paste it and save.

    ```text
    """Clean the raw pendulum file: write a plain CSV table."""
    import argparse

    import pandas as pd


    def clean(path):
        """Return the measurements in the raw file as a table."""
        raw = pd.read_csv(path, sep=";", decimal=",")
        rows = raw[raw["nr"].notna()]      # the mean line has no number
        table = rows[["length_cm", "t10_s"]]
        return table.astype({"length_cm": int})   # was text: "mean"


    def main():
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("raw", help="file as received")
        parser.add_argument("out", help="cleaned CSV file to write")
        args = parser.parse_args()

        table = clean(args.raw)
        table.to_csv(args.out, index=False, float_format="%.2f",
                     lineterminator="\n")
        print(f"{args.out}: {len(table)} rows")


    if __name__ == "__main__":
        main()
    ```

    Go through it from the top. The four lines of `clean()` are the four
    edits made by hand: the separator and the decimal comma, the line with
    the mean, the column `nr`, and `length_cm` turned from text into
    numbers. `main()` reads the two arguments and writes the file.

2. Run the script with nothing after its name.

    ```text
    python scripts/clean.py
    ```

    It answers with two lines and does nothing else.

    ```text
    usage: clean.py [-h] raw out
    clean.py: error: the following arguments are required: raw, out
    ```

3. Ask it what it wants: `python scripts/clean.py --help`. Nobody wrote
   this text. It is put together from the first line of the file and the
   two `help=` strings.

4. Run it on the raw file.

    ```text
    python scripts/clean.py data/raw/pendulum.csv data/processed/pendulum.csv
    ```

    It prints `data/processed/pendulum.csv: 9 rows`.

5. Measure the result with `ls -l data/processed`. The file has 97 bytes on
   every laptop. Open it: ten lines, a comma between the values, a decimal
   point, and `17.90` with its zero.

6. Run step 4 again and then type `echo $?`. The answer is `0`: the
   command ended without an error. Run step 2 again and then `echo $?`.
   Now it is `2`.

You should now see `data/processed/pendulum.csv` with these first lines:

```text
length_cm,t10_s
20,9.02
30,11.05
```

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `ModuleNotFoundError: No module named 'pandas'` | The environment is not active: the prompt does not start with `(.venv)` |
    | `No such file or directory: 'data/raw/pendulum.csv'` | The terminal is not in the project folder, or the raw file has another name. `pwd`, then `ls data/raw` |
    | `KeyError: 'nr'` | The file in `data/raw` is not the file as received. It is a cleaned copy. Download the raw file again |
    | `IndentationError` | The paste went into a file that was not empty. Delete everything and paste again |

## 5. Plot, fit, report { #stages }

**0:45 · 15 min**

Three more stages of the same form: the files to read come first, the file
to write comes last. They are handed out, because nothing in them is new:
Matplotlib, `curve_fit`, f-strings. Two things are worth showing. The fit
takes its parameters from a file, `config.json`. And the report is written
by a script, so no number is copied by hand.

1. Download
   [`plot.py`](../data/workflows_plot.py){ download="plot.py" },
   [`fit.py`](../data/workflows_fit.py){ download="fit.py" } and
   [`report.py`](../data/workflows_report.py){ download="report.py" }, and
   drag them from **Downloads** onto the `scripts` folder. If a file of
   that name is there, replace it.

2. Select the empty area below the folders in the Side Bar, then
   **New File**, and type `config.json`. Type four lines and save.

    ```text
    {
      "swings": 10,
      "through_origin": false
    }
    ```

3. Open `scripts/fit.py` and read three places with the room:
   `g_from_slope`, which is one line of physics with its units in the
   docstring; `fit_g`, which is the fit; and the lines of `main()` that
   read `config.json`.

4. Run the three stages. A `\` at the end of a line means that the
   command goes on in the next line.

    ```text
    python scripts/plot.py data/processed/pendulum.csv \
        results/pendulum_plot.png
    python scripts/fit.py data/processed/pendulum.csv config.json \
        results/fit.json
    python scripts/report.py data/processed/pendulum.csv results/fit.json \
        results/pendulum_plot.png results/report.md
    ```

    They print:

    ```text
    results/pendulum_plot.png: 9 points
    results/fit.json: g = 9.84 +- 0.06 m/s^2
    results/report.md: 19 lines
    ```

5. Open `results/fit.json`. Then open `results/report.md` and its preview
   with `Ctrl+K`, then `V` (macOS `Cmd+K`, then `V`).

6. Commit.

    ```text
    git add -A
    git commit -m "Four stages with a command line"
    ```

You should now see, in the preview, a title, a table of nine rows, the
plot, and a last sentence that ends in `g = 9.84 ± 0.06 m/s²`.

Say that this is the report of the first seminar. Its table was built with
a cursor on every line, and now a loop of two lines builds it. The last
sentence is new, and nobody typed the number in it.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | A script is named `plot (1).py` | It was downloaded twice. Delete it and rename nothing: use the first one |
    | The browser shows the script as a page of text | Go back, right-click the link and select **Save Link As...** |
    | `json.decoder.JSONDecodeError` | `config.json` has a slip: a missing comma, or `False` with a capital letter |
    | `No such file or directory: 'results/…'` | The folder `results` is missing. Create it in the Side Bar |

## Part 3 · One command { #part-3 }

**1:00 to 1:30 · sections 6 to 8**

Four commands in a fixed order are a list that somebody has to remember.
The list goes into a file, and a rule decides which of the four has to run.

## 6. Write run_all.py { #run-all }

**1:00 · 15 min**

The rule: a file is out of date when it does not exist, or when one of the
files it is made from was changed after it was written. The files it is
made from are its inputs and the script that writes it. `run_all.py` holds
the four stages as a table and applies this rule to each of them in order.

1. Select the empty area below the folders, then **New File**, and type
   `run_all.py`. The file sits at the top of the project, next to
   `README.md`. Paste the block and save.

    ```text
    """Rebuild every result that is out of date: python run_all.py"""
    import os
    import subprocess
    import sys

    RAW = "data/raw/pendulum.csv"
    TABLE = "data/processed/pendulum.csv"
    PLOT = "results/pendulum_plot.png"
    FIT = "results/fit.json"
    REPORT = "results/report.md"

    # One line per stage: the script, what it reads, what it writes.
    STAGES = [
        ("scripts/clean.py", [RAW], TABLE),
        ("scripts/plot.py", [TABLE], PLOT),
        ("scripts/fit.py", [TABLE, "config.json"], FIT),
        ("scripts/report.py", [TABLE, FIT, PLOT], REPORT),
    ]


    def out_of_date(output, sources):
        """True if output is missing or older than a source."""
        if not os.path.exists(output):
            return True
        built = os.path.getmtime(output)
        for source in sources:
            if os.path.getmtime(source) > built:
                return True
        return False


    for script, inputs, output in STAGES:
        if out_of_date(output, [script] + inputs):
            os.makedirs(os.path.dirname(output), exist_ok=True)
            command = [sys.executable, script] + inputs + [output]
            done = subprocess.run(command)
            if done.returncode != 0:
                sys.exit(f"{script} failed, stopped")
        else:
            print(f"{output}: up to date", flush=True)
    ```

2. Read it with the room in three parts. `STAGES` is the four commands of
   section 5 as a table. `out_of_date` is the rule. The loop builds each
   command from one line of the table, runs it, and stops if a stage ends
   with an exit code other than 0.

3. Run it.

    ```text
    python run_all.py
    ```

4. Run it a second time. Nothing changes.

You should now see four lines:

```text
data/processed/pendulum.csv: up to date
results/pendulum_plot.png: up to date
results/fit.json: up to date
results/report.md: up to date
```

Every result was built by hand a few minutes ago and nothing was changed
since, so the rule finds nothing to do.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `can't open file '…run_all.py'` | The file was saved inside `scripts`. Drag it onto the empty area of the Side Bar |
    | `FileNotFoundError: … 'config.json'` | `config.json` is not at the top of the project, or it is named `config.json.txt` |
    | A stage runs in place of `up to date` | One of its sources was saved after its output. That is the rule at work. Run the command again |

## 7. Change something { #change }

**1:15 · 7 min**

The rule is tried on two changes. Before each run, ask the room which
stages will run. The answer is in the table `STAGES`.

1. Open `scripts/plot.py`. In the line with `ax.plot`, change `"o"` to
   `"s"` and save. Ask, then run `python run_all.py`.

    ```text
    data/processed/pendulum.csv: up to date
    results/pendulum_plot.png: 9 points
    results/fit.json: up to date
    results/report.md: 19 lines
    ```

    Open the picture: the points are squares. The fit did not run, because
    nothing it reads has changed.

2. Open `config.json`, change `false` to `true` and save. Ask, then run.

    ```text
    data/processed/pendulum.csv: up to date
    results/pendulum_plot.png: up to date
    results/fit.json: g = 9.81 +- 0.02 m/s^2
    results/report.md: 19 lines
    ```

    Open the report. Its last sentence now reads `g = 9.81 ± 0.02 m/s²`.
    The straight line is forced through the origin, and the number is
    another one.

3. Put both back: `"o"` in `plot.py`, `false` in `config.json`. Save both
   and run once more. Three stages run, and the report has 9.84 ± 0.06
   again.

4. Commit the new file.

    ```text
    git add run_all.py
    git commit -m "One command rebuilds every result"
    ```

You should now see `nothing to commit, working tree clean` from
`git status`: the two files were changed and put back, and the results
were rebuilt to what they were.

## 8. Delete and rebuild { #rebuild }

**1:22 · 8 min**

This is the test of the whole session. Everything that a script wrote is
deleted. One command brings it back, and Git checks that it is the same.

1. Delete the two folders that hold what was made.

    ```text
    rm -r data/processed results
    ```

2. Type `git status --short`. Git lists the results as deleted.

    ```text
     D results/fit.json
     D results/pendulum_plot.png
     D results/report.md
    ```

    A fourth line, ` D data/processed/pendulum.csv`, stands above them if
    that file was committed before `.gitignore` named its folder.

3. Rebuild with `python run_all.py`. All four stages run.

    ```text
    data/processed/pendulum.csv: 9 rows
    results/pendulum_plot.png: 9 points
    results/fit.json: g = 9.84 +- 0.06 m/s^2
    results/report.md: 19 lines
    ```

4. Type `git status`. It ends with
   `nothing to commit, working tree clean`. Every rebuilt file has the
   bytes of the file that was committed, the picture included.

5. Compute the checksum of the report.

    ```text
    Windows, Linux   sha256sum results/report.md
    macOS            shasum -a 256 results/report.md
    ```

    It begins with `1bf0d728` and ends with `fb3f`. Ask who has the same.

You should now see a clean `git status` after a rebuild from nothing but
`data/raw`, `scripts` and `config.json`.

Say it in these words: anything in `data/processed` and `results` can be
deleted at any time. Nothing in `data/raw`, `scripts` or `config.json`
can.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The checksum differs from the neighbour's | Compare `data/processed/pendulum.csv` first: 97 bytes on both? Then the two reports line by line. The raw tables differ, or one `config.json` says `true` |
    | `git status` shows the picture as modified | The picture was committed from another environment. Commit the new one |

## Part 4 · One test { #part-4 }

**1:30 to 2:00 · sections 9 to 12**

The pipeline gives the same result every time. Whether the result is right
is another question, and it is answered by tests.

## 9. A first test { #test }

**1:30 · 10 min**

A test states one fact that is known without the script, and lets the
computer check it. Three facts about the cleaned table are known from the
lab notebook and from the raw file: there are nine measurements, the table
has two columns, and the first time is 9.02 s.

1. Select the empty area below the folders, then **New Folder**, and type
   `tests`. In it create the file `test_clean.py`. The room types this one.

    ```text
    from scripts.clean import clean

    RAW = "data/raw/pendulum.csv"


    def test_nine_measurements():
        assert len(clean(RAW)) == 9


    def test_two_columns():
        table = clean(RAW)
        assert list(table.columns) == ["length_cm", "t10_s"]


    def test_decimal_comma_is_read():
        table = clean(RAW)
        assert table["t10_s"].iloc[0] == 9.02
    ```

2. Run the tests from the project folder.

    ```text
    python -m pytest
    ```

3. Run them again with `python -m pytest -v`. Each test is listed by name
   with `PASSED` beside it.

You should now see a line that ends in `3 passed`, with a time of well
under a second.

Say how the tests were found: pytest runs every function named `test_…`
in every file named `test_….py`. Line 1 imports `clean` from
`scripts/clean.py`. That works because the cleaning is a function and the
script ends with the two lines about `__main__`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `ModuleNotFoundError: No module named 'scripts'` | The command was `pytest`, or the terminal is not at the top of the project. Use `python -m pytest` there |
    | `No module named pytest` | The environment is not active |
    | `collected 0 items` | The file is not named `test_….py`, or the functions are not named `test_…` |

## 10. Make it fail { #fail }

**1:40 · 8 min**

A test is worth something only if it fails when the code is wrong. One
argument is taken out of the cleaning, the one that is easiest to forget.
First the pipeline runs without the test, to show what happens when nobody
checks.

1. Open `scripts/clean.py`. In the line with `read_csv`, delete
   `, decimal=","` and save.

2. Run `python run_all.py`.

    ```text
    data/processed/pendulum.csv: 9 rows
    results/pendulum_plot.png: 9 points
    ```

    Two stages run without a complaint. Then a traceback follows, and the
    last two lines are:

    ```text
    TypeError: unsupported operand type(s) for /: 'str' and 'int'
    scripts/fit.py failed, stopped
    ```

3. Open `results/pendulum_plot.png`. The points lie on a straight line and
   the labels of the vertical axis read `9,02`, `11,05`: the times were
   read as text. The message of step 2 names neither the comma nor
   `clean.py`.

4. Now run `python -m pytest`. It ends with `1 failed, 2 passed`. Read the
   failure with the room:

    ```text
    >       assert table["t10_s"].iloc[0] == 9.02
    E       AssertionError: assert '9,02' == 9.02
    ```

    The line marked `>` is the assertion that failed. The line marked `E`
    shows the two values: the text `'9,02'` and the number 9.02.

5. Put `, decimal=","` back with `Ctrl+Z` (macOS `Cmd+Z`) and save. Run
   `python -m pytest`, then `python run_all.py`.

You should now see `3 passed`, then four stages that run, and a plot whose
points lie on a curve again.

## 11. Tests in the one command, and the README { #readme }

**1:48 · 7 min**

Two things are left. The tests should run without anyone remembering them,
and the README should say how to rebuild the project.

1. Open `run_all.py` and add three lines above the line that starts with
   `for script`, with an empty line after them.

    ```text
    tests = subprocess.run([sys.executable, "-m", "pytest", "-q"])
    if tests.returncode != 0:
        sys.exit("tests failed, nothing rebuilt")
    ```

2. Run `python run_all.py`. The tests come first: a line of three dots
   and a line with `3 passed`. The four lines that end in `up to date`
   follow.

3. Open `README.md` and add a section. Use the Python version that
   `python --version` prints.

    ```text
    ## How to rebuild

    Needs Python 3.13. On Windows, use Git Bash.

        python -m venv .venv
        source .venv/Scripts/activate
        pip install -r requirements.txt
        python run_all.py

    On macOS and Linux the first two lines are
    `python3 -m venv .venv` and `source .venv/bin/activate`.

    `run_all.py` runs the tests, then rebuilds every file in
    `data/processed/` and `results/` that is out of date.
    ```

4. Commit.

    ```text
    git add -A
    git commit -m "Tests, and how to rebuild"
    ```

You should now see the section **How to rebuild** in the preview of the
README, and a clean `git status`.

## 12. Wrap up { #wrap-up }

**1:55 · 5 min**

Put the tasks of the next section on the projector and read them aloud.
Ask on the way out which step was hardest.

What the room has learned:

- An environment is a folder with its own Python and packages. It is
  activated in every new terminal.
- `pip freeze > requirements.txt` writes the versions down.
  `pip install -r requirements.txt` installs them elsewhere.
- A script takes its file names as arguments. `--help` says which.
- A result is out of date when it is missing or older than something it is
  made from, the script included.
- `python run_all.py` rebuilds what is out of date, in order, and stops at
  the first failure.
- Whatever a script wrote can be deleted and rebuilt. Git or a checksum
  shows that it came back the same.
- A test asserts a fact that is known without the code. `python -m pytest`
  runs all of them.

## Next steps, at home

**45 min, on your own dataset**

1. Make an environment in the project of your own dataset, install what
   your scripts import, and write `requirements.txt`.

2. Give one of your scripts a command line: the file it reads and the file
   it writes as arguments, with a help text.

3. Write a `run_all.py` for your project with at least two stages. Delete
   the results, run it, and check with `git status` that they came back.

4. Write one test of a fact you know about your own cleaned data: the
   number of rows, the names of the columns, or a range that the values
   cannot leave.

5. Add **How to rebuild** to your README. Then try it: make a copy of the
   project with `git clone`, follow your own four lines in the copy, and
   note what was missing.

## Stretch goals

For students who finish a section early. Answers are given for the
lecturer.

- Download
  [`test_fit.py`](../data/workflows_test_fit.py){ download="test_fit.py" }
  into `tests` and run `python -m pytest`. The answer is `5 passed`. Its
  second test fits five periods computed from the formula with g = 9.81
  and gets 9.81 back.
- Add a test that no time is outside 5 s to 25 s:
  `assert table["t10_s"].between(5, 25).all()`. It passes. With the
  decimal comma taken out it fails with a `TypeError`, because a text
  cannot be compared with a number.
- Make the picture for a poster:
  `python scripts/plot.py data/processed/pendulum.csv poster.png --dpi 300`.
  The answer is a picture of 1440 by 960 pixels in place of 720 by 480.
  Delete `poster.png` afterwards.
- In a test, compute the first period, `table["t10_s"].iloc[0] / 10`, and
  assert that it equals `0.902`. The test fails: the value is
  `0.9019999999999999`. With `import pytest` at the top and
  `pytest.approx(0.902)` on the right-hand side it passes.
- Try the README on a fresh copy: `git clone . ../analysis-copy`, then
  `cd ../analysis-copy` and the four lines of **How to rebuild**. The
  answer is the tests passing, four stages running and a clean
  `git status`. Delete the copy afterwards.
- Draw the pipeline in the README. Put these lines into a code block
  marked `mermaid`, and install the extension
  **Markdown Preview Mermaid Support** to see the diagram in the preview.

    ```text
    flowchart LR
        raw[raw/pendulum.csv] --> clean([clean.py])
        clean --> table[processed/pendulum.csv]
        table --> plot([plot.py]) --> png[pendulum_plot.png]
        table --> fit([fit.py]) --> json[fit.json]
        config[config.json] --> fit
        table --> report([report.py])
        png --> report
        json --> report
        report --> md[report.md]
    ```

## If students ask for more

| Topic | What to say |
|--|--|
| `make` | It applies the same rule to a file named `Makefile`. macOS and Linux have it. Git Bash on Windows does not, which is why this page uses `run_all.py` |
| conda or uv in place of venv | Both can install from the same `requirements.txt`. One tool per project |
| A server that runs `run_all.py` after every push | Continuous integration. The file shown in the lecture works once the project is on GitHub |
| A pipeline with a hundred input files | Snakemake: the same table of stages, with patterns in place of file names |

Leave out, even if asked: Docker, pre-commit hooks, Git LFS. Each was named
in the lecture, and none is needed for a project of this size.

## Aims practised

♻️ pinned versions and a rebuild from raw data · ⚙️ one command for every result · 🔧 the same commands on Windows, macOS and Linux · 📁 raw data read, results rebuilt
