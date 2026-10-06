# Seminar 13 — One Command Rebuilds the Analysis

**Paired lecture:** 13 Reproducible Workflows & Automation · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student deletes every result of the project and
gets it back with one command, `python run_all.py`, in an environment with
pinned versions and with a test that runs first.

Commands are typed in the terminal of VS Code, in the project folder: `zsh`
on macOS, PowerShell 7 on Windows, with Python and Git from Seminar 4. New
today are an environment, a script with a command line, `run_all.py` and
pytest.

## Run sheet

One screen for the front of the room. Each line links to its section.

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · An environment** · 30 min | | |
| 0:00 | [1. Start from a committed state](#start) | `git status`, then a commit | A clean `git status` |
| 0:05 | [2. Create and activate an environment](#venv) | `python -m venv .venv`, then `activate` | A prompt that starts with `(.venv)` |
| 0:15 | [3. Install, and write down the versions](#freeze) | `pip install`, then `pip freeze > requirements.txt` | `requirements.txt`, and `.venv` ignored by Git |
| | **Part 2 · Four stages** · 30 min | | |
| 0:30 | [4. Give the cleaning a command line](#cli) | `scripts/clean.py`, then `--help` | `clean.py` with two arguments and a help text |
| 0:45 | [5. Plot, fit, report](#stages) | The three stages run by hand | A report with *g* in it, written by a script |
| | **Part 3 · One command** · 30 min | | |
| 1:00 | [6. Write run_all.py](#run-all) | `python run_all.py` | Four lines that end in `up to date` |
| 1:15 | [7. Change something](#change) | `"o"` to `"s"`, `false` to `true` | Only the affected stages run again |
| 1:22 | [8. Delete and rebuild](#rebuild) | `rm`, `Remove-Item`, four files | A clean `git status` after a rebuild |
| | **Part 4 · One test** · 30 min | | |
| 1:30 | [9. A first test](#test) | `tests/test_clean.py`, then `python -m pytest` | `3 passed` |
| 1:40 | [10. Make it fail](#fail) | `, decimal=","` taken out | A failure read and repaired |
| 1:48 | [11. Tests in the one command, and the README](#readme) | Three lines in `run_all.py`, then `README.md` | **How to rebuild**, second version |
| 1:55 | [12. Wrap up](#wrap-up) | The list of what was learned | |

**If time runs short:** leave out section 7, and in section 4 hand out
`clean.py` as a file and do only its steps 2 to 5. Keep section 11:
Seminar 14 rebuilds the project from its **How to rebuild** section.

??? info "How to use this page"
    This page is written for the person at the front. Students follow the
    same page.

    - **Tell the room** is the paragraph to say before the steps.
    - The **numbered steps** are what to do on the projector. The room
      repeats each step on their own laptops.
    - **You should now see** closes a section. Ask for hands: "who sees
      this?" Go on when about four in five have it. The rest get help from a
      neighbour.
    - **Watch for** is the usual slip in that section.

    Every command stands alone in a block. Where the two shells differ, the
    step has a tab for **macOS** (`zsh`) and one for **Windows**
    (PowerShell 7). Every command of the page was run in both shells. Keys
    are written for Windows, with macOS in brackets.

??? info "Before the session"
    For the room:

    - The project folder `analysis-project` under Git, with
      `data/raw/pendulum.csv` in it: the file as received, with `;` between
      the values and decimal commas. A student who does not have it
      downloads
      [`pendulum_raw.csv`](../data/pendulum_raw.csv){ download="pendulum.csv" }
      and drags it onto the `raw` folder.
    - Python and Git, installed in Seminar 4. On Windows, PowerShell 7 as
      the terminal of VS Code, also from Seminar 4: the name at the top
      right of the Panel reads `pwsh`.
    - The section **How to rebuild** that Seminar 4 wrote into the README.
      Section 11 replaces it.

    The scripts of this page are complete in themselves. A student has a
    `clean.py` from Seminar 12 and may have a `plot.py` or `fit.py` from the
    lectures. The files of this page take their place. Section 1 commits the old ones first, so Git
    keeps them. `clean_pendulum.py` of Seminar 4 stays as it is.

    For you:

    - The whole page done once on a copy of your own project folder.
    - The network of the room tried out: section 3 downloads about 50 MB per
      laptop.
    - A USB stick with the files of the next box, in case the network
      fails.

??? info "Files for this seminar"
    A browser saves each file under the name in the second column. The
    handed-out `run_all.py` is the final one, with the three lines of
    section 11 in it.

    | File | Saved as | What it is |
    |--|--|--|
    | [`pendulum_raw.csv`](../data/pendulum_raw.csv){ download="pendulum.csv" } | `pendulum.csv` | The raw table as received, for `data/raw` |
    | [`workflows_clean.py`](../data/workflows_clean.py){ download="clean.py" } | `clean.py` | Section 4: the cleaning with a command line |
    | [`workflows_plot.py`](../data/workflows_plot.py){ download="plot.py" } | `plot.py` | Section 5: the plot stage |
    | [`workflows_fit.py`](../data/workflows_fit.py){ download="fit.py" } | `fit.py` | Section 5: the fit stage |
    | [`workflows_report.py`](../data/workflows_report.py){ download="report.py" } | `report.py` | Section 5: the report stage |
    | [`workflows_config.json`](../data/workflows_config.json){ download="config.json" } | `config.json` | Section 5: the parameters of the fit |
    | [`workflows_run_all.py`](../data/workflows_run_all.py){ download="run_all.py" } | `run_all.py` | Sections 6 and 11: the one command |
    | [`workflows_test_clean.py`](../data/workflows_test_clean.py){ download="test_clean.py" } | `test_clean.py` | Section 9: the three tests of the cleaning |
    | [`workflows_test_fit.py`](../data/workflows_test_fit.py){ download="test_fit.py" } | `test_fit.py` | Stretch goal: two tests of the fit |

---

## Part 1 · An environment { #part-1 }

**0:00 to 0:30 · sections 1 to 3**

The room ends this part with a folder `.venv` that holds the packages of
this project, and a file `requirements.txt` that says which versions they
are.

---

### 1. Start from a committed state { #start }

**0:00 · 5 min**

**Tell the room.** Today adds files to the project and replaces three that
were made by hand: the cleaned table, the plot and the report. Before
anything is replaced, the present state is committed. Git then keeps the
versions made by hand.

1. Open the project folder in VS Code and select **Terminal** >
   **New Terminal**. Check the name at the top right of the Panel: `zsh`
   on macOS, `pwsh` on Windows.

2. Ask Git for the state of the folder:

    ```text
    git status
    ```

3. If it lists changes or untracked files, commit them.

    ```text
    git add -A
    ```

    ```text
    git commit -m "State before the pipeline"
    ```

4. List the folder:

    ```text
    ls
    ```

    The list has `README.md`, `data`, `results` and `scripts`.

!!! success "You should now see"
    `nothing to commit, working tree clean` as the last line of
    `git status`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `fatal: not a git repository` | The folder is not under Git yet. Run `git init`, then the two commands of step 3 |
    | Windows: the Panel reads `powershell`, not `pwsh` | That is Windows PowerShell 5.1. Make PowerShell 7 the default as in [Seminar 4, section 4](seminar_04.md#shell), step 1, and open a new terminal |

---

### 2. Create and activate an environment { #venv }

**0:05 · 10 min**

**Tell the room.** An environment is a folder with its own `python` and its
own packages. This project gets one, named `.venv`, inside the project
folder. Whatever is installed while it is active goes into that folder and
nowhere else. The packages installed on the laptop over the semester stay
as they are.

1. Create the environment. The command prints nothing and takes a few
   seconds.

    === "macOS"

        ```text
        python3 -m venv .venv
        ```

    === "Windows"

        ```text
        python -m venv .venv
        ```

2. Activate it.

    === "macOS"

        ```text
        source .venv/bin/activate
        ```

    === "Windows"

        ```text
        .venv\Scripts\Activate.ps1
        ```

        `Activate.ps1` is a PowerShell script. PowerShell 7 runs a script
        made on the laptop itself, and `venv` has just made this one.

    The prompt now starts with `(.venv)`.

3. Ask which `python` answers now:

    === "macOS"

        ```text
        which python
        ```

        ```text
        /Users/ada/Documents/analysis-project/.venv/bin/python
        ```

    === "Windows"

        ```text
        (Get-Command python).Source
        ```

        ```text
        C:\Users\ada\Documents\analysis-project\.venv\Scripts\python.exe
        ```

    The answer is a path inside the project folder. From here on the
    command is `python` on every system, `python3` on macOS included.

4. List the packages of the environment:

    ```text
    pip list
    ```

    A new environment holds `pip` and nothing else. On a Python older than
    3.12 it also holds `setuptools`.

5. Press `Ctrl+Shift+P` (macOS `Cmd+Shift+P`) and type:

    ```text
    interpreter
    ```

    Select **Python: Select Interpreter** and choose the entry with `.venv`
    in it.

6. Close the terminal with the bin icon at the top right of the Panel and
   open a new one. If its prompt does not start with `(.venv)`, repeat
   step 2. An environment is activated in every new terminal.

!!! success "You should now see"
    `(.venv)` at the start of the prompt, and a folder `.venv` in the Side
    Bar.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `zsh: command not found: python` in step 1 | The command is `python3` there. After the activation it is `python` |
    | Windows: `Activate.ps1 cannot be loaded because running scripts is disabled on this system` | The terminal is Windows PowerShell 5.1, or the laptop has a stricter rule. Check that the Panel reads `pwsh`. If it does, type `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then step 2 again |
    | Windows: `source` is not recognized | That is the macOS line. Use the **Windows** tab |
    | **Python: Select Interpreter** is not in the list | The Python extension is missing. Install it from the Extensions view |

---

### 3. Install, and write down the versions { #freeze }

**0:15 · 15 min**

**Tell the room.** The new environment is empty. That makes it a test: it
shows which packages this project needs. Four are installed. Then the
versions of everything that arrived are written into a file. The file goes
into Git. The folder `.venv` does not: it is large, and it can be made
again from the file.

1. Install the four packages. This downloads about 50 MB. It took 13 s on a
   fast network. Allow a few minutes when the whole room downloads at once.

    ```text
    pip install pandas matplotlib scipy pytest
    ```

    A line near the end begins with `Successfully installed` and names more
    than four packages: each package brings the packages it needs. A
    `[notice]` about a new release of pip may follow. It can be ignored.

2. List the packages again and find `numpy`. Nobody asked for it. pandas
   did.

    ```text
    pip list
    ```

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

5. Open the file `.gitignore` of Seminar 5 at the top of the project. If
   there is none, select the empty area below the folders, then
   **New File**, and name it:

    ```text
    .gitignore
    ```

    Add four lines at its end and save.

    ```text
    .venv/
    __pycache__/
    .pytest_cache/
    data/processed/
    ```

6. Commit the two files.

    ```text
    git add requirements.txt .gitignore
    ```

    ```text
    git commit -m "Environment with pinned versions"
    ```

!!! success "You should now see"
    `requirements.txt` in the Side Bar, and a `git status` that does not
    mention `.venv`. The file had 17 lines on macOS on the day this page was
    checked. On Windows pandas and pytest ask for two packages more,
    `tzdata` and `colorama`, so the file is longer there.

**Say what the file is for.** On another laptop,
`pip install -r requirements.txt` in a new environment installs exactly
these versions.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `error: externally-managed-environment` | The environment is not active. Section 2, step 2 |
    | Source Control shows thousands of changes | `.gitignore` is not saved, is named `.gitignore.txt`, or is not at the top of the project |
    | The installation stops with a network error | Run the command again. It continues where it stopped |
    | Windows: `warning: in the working copy of '.gitignore', LF will be replaced by CRLF` | A note, not an error: the commit is made. Git on this laptop missed the setting of Seminar 5. Type `git config --global core.autocrlf false` once |

---

## Part 2 · Four stages { #part-2 }

**0:30 to 1:00 · sections 4 and 5**

The analysis is four steps: clean, plot, fit, report. Each becomes a script
that is told on the command line which files to read and which file to
write.

---

### 4. Give the cleaning a command line { #cli }

**0:30 · 15 min**

**Tell the room.** Lecture 2 cleaned the raw table by hand, with four
edits. In Seminar 4 the handed-out `clean_pendulum.py` made the same edits,
and Lecture 12 wrote them as four lines of pandas, with the two file names
typed into the code. Today the four lines become a function, and the script
around it takes two arguments: the file to read and the file to write. No
file name is typed into the code.

1. Select the `scripts` folder, then **New File**, and name it:

    ```text
    clean.py
    ```

    If the file exists, open it and delete its content. Copy the block below
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

3. Ask it what it wants.

    ```text
    python scripts/clean.py --help
    ```

    Nobody wrote this text. It is put together from the first line of the
    file and the two `help=` strings.

4. Run it on the raw file.

    ```text
    python scripts/clean.py data/raw/pendulum.csv data/processed/pendulum.csv
    ```

    It prints:

    ```text
    data/processed/pendulum.csv: 9 rows
    ```

5. Measure the result.

    === "macOS"

        ```text
        wc -c data/processed/pendulum.csv
        ```

        ```text
              97 data/processed/pendulum.csv
        ```

    === "Windows"

        ```text
        (Get-Item data/processed/pendulum.csv).Length
        ```

        ```text
        97
        ```

    The file has 97 bytes on every laptop, the size that the README names
    since Seminar 4. Open it: ten lines, a comma between the values, a
    decimal point, and `17.90` with its zero.

6. Run step 4 again, then ask for its exit code:

    === "macOS"

        ```text
        echo $?
        ```

    === "Windows"

        ```text
        $LASTEXITCODE
        ```

        Not `$?`: in PowerShell it says only `True` or `False`.

    The answer is `0`: the command ended without an error. Run step 2 again
    and ask again. Now it is `2`.

!!! success "You should now see"
    `data/processed/pendulum.csv` with these first lines:

    ```text
    length_cm,t10_s
    20,9.02
    30,11.05
    ```

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `ModuleNotFoundError: No module named 'pandas'` | The environment is not active: the prompt does not start with `(.venv)` |
    | `No such file or directory: 'data/raw/pendulum.csv'` | The terminal is not in the project folder, or the raw file has another name. `pwd`, then `ls data/raw`: the same two words in both shells |
    | `KeyError: 'nr'` | The file in `data/raw` is not the file as received. It is a cleaned copy. Download the raw file again |
    | `IndentationError` | The paste went into a file that was not empty. Delete everything and paste again |

---

### 5. Plot, fit, report { #stages }

**0:45 · 15 min**

**Tell the room.** Three more stages of the same form: the files to read
come first, the file to write comes last. They are handed out, because
nothing in them is new: Matplotlib, `curve_fit`, f-strings. Two things are
worth showing. The fit takes its parameters from a file, `config.json`. And
the report is written by a script, so no number is copied by hand.

1. Download
   [`plot.py`](../data/workflows_plot.py){ download="plot.py" },
   [`fit.py`](../data/workflows_fit.py){ download="fit.py" } and
   [`report.py`](../data/workflows_report.py){ download="report.py" }, and
   drag them from **Downloads** onto the `scripts` folder. If a file of
   that name is there, replace it.

2. Select the empty area below the folders in the Side Bar, then
   **New File**, and name it:

    ```text
    config.json
    ```

    Type four lines and save.

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

4. Run the three stages, one at a time. Each command is one line, the same
   in both shells. Copy it with the button in the corner of its block.

    ```text
    python scripts/plot.py data/processed/pendulum.csv results/pendulum_plot.png
    ```

    ```text
    python scripts/fit.py data/processed/pendulum.csv config.json results/fit.json
    ```

    ```text
    python scripts/report.py data/processed/pendulum.csv results/fit.json results/pendulum_plot.png results/report.md
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
    ```

    ```text
    git commit -m "Four stages with a command line"
    ```

!!! success "You should now see"
    In the preview: a title, a table of nine rows, the plot, and a last
    sentence that ends in `g = 9.84 ± 0.06 m/s²`.

**Say what is new.** This is the report handed out in Seminar 4. Its table
was typed, and now a loop of two lines builds it. The last sentence is new,
and nobody typed the number in it.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | A script is named `plot (1).py` | It was downloaded twice. Delete it and rename nothing: use the first one |
    | The browser shows the script as a page of text | Go back, right-click the link and select **Save Link As...** |
    | `json.decoder.JSONDecodeError` | `config.json` has a slip: a missing comma, or `False` with a capital letter |
    | `No such file or directory: 'results/…'` | The folder `results` is missing. Create it in the Side Bar |

---

## Part 3 · One command { #part-3 }

**1:00 to 1:30 · sections 6 to 8**

Four commands in a fixed order are a list that somebody has to remember.
The list goes into a file, and a rule decides which of the four has to run.

---

### 6. Write run_all.py { #run-all }

**1:00 · 15 min**

**Tell the room.** The rule: a file is out of date when it does not exist,
or when one of the files it is made from was changed after it was written.
The files it is made from are its inputs and the script that writes it.
`run_all.py` holds the four stages as a table and applies this rule to each
of them in order.

1. Select the empty area below the folders, then **New File**, and name it:

    ```text
    run_all.py
    ```

    The file sits at the top of the project, next to `README.md`. Paste the
    block and save.

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

5. Commit the new file.

    ```text
    git add run_all.py
    ```

    ```text
    git commit -m "One command rebuilds every result"
    ```

!!! success "You should now see"
    Four lines:

    ```text
    data/processed/pendulum.csv: up to date
    results/pendulum_plot.png: up to date
    results/fit.json: up to date
    results/report.md: up to date
    ```

    Every result was built by hand a few minutes ago and nothing was
    changed since, so the rule finds nothing to do.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `can't open file '…run_all.py'` | The file was saved inside `scripts`. Drag it onto the empty area of the Side Bar |
    | `FileNotFoundError: … 'config.json'` | `config.json` is not at the top of the project, or it is named `config.json.txt` |
    | A stage runs in place of `up to date` | One of its sources was saved after its output. That is the rule at work. Run the command again |
    | `no tests ran`, then `tests failed, nothing rebuilt` | The file is the handed-out `run_all.py`, which runs the tests first, and there are no tests yet. Delete the three lines that start with `tests =` until section 11 |

---

### 7. Change something { #change }

**1:15 · 7 min**

**Tell the room.** The rule is tried on two changes. Before each run, ask
the room which stages will run. The answer is in the table `STAGES`.

1. Open `scripts/plot.py`. In the line with `ax.plot`, change `"o"` to
   `"s"` and save. Ask, then run:

    ```text
    python run_all.py
    ```

    It prints:

    ```text
    data/processed/pendulum.csv: up to date
    results/pendulum_plot.png: 9 points
    results/fit.json: up to date
    results/report.md: 19 lines
    ```

    Open the picture: the points are squares. The fit did not run, because
    nothing it reads has changed.

2. Open `config.json`, change `false` to `true` and save. Ask, then run
   again:

    ```text
    python run_all.py
    ```

    It prints:

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

4. Ask Git what changed.

    ```text
    git status
    ```

!!! success "You should now see"
    `nothing to commit, working tree clean` from `git status`: the two files
    were changed and put back, and the results were rebuilt to what they
    were.

---

### 8. Delete and rebuild { #rebuild }

**1:22 · 8 min**

**Tell the room.** This is the test of the whole session. Everything that
`run_all.py` writes is deleted. One command brings it back, and Git checks
that it is the same.

1. Delete the four files that `run_all.py` writes. Each command is one
   line.

    === "macOS"

        ```text
        rm data/processed/pendulum.csv results/pendulum_plot.png results/fit.json results/report.md
        ```

    === "Windows"

        ```text
        Remove-Item data/processed/pendulum.csv, results/pendulum_plot.png, results/fit.json, results/report.md
        ```

    The other files in `results`, such as `summary.txt` of Seminar 7, stay.
    Scripts that `run_all.py` does not run made them, so it would not bring
    them back.

2. Ask Git what is gone.

    ```text
    git status --short
    ```

    Git lists the four files as deleted.

    ```text
     D data/processed/pendulum.csv
     D results/fit.json
     D results/pendulum_plot.png
     D results/report.md
    ```

    The first line is missing where `data/processed/pendulum.csv` was never
    committed.

3. Rebuild. All four stages run.

    ```text
    python run_all.py
    ```

    It prints:

    ```text
    data/processed/pendulum.csv: 9 rows
    results/pendulum_plot.png: 9 points
    results/fit.json: g = 9.84 +- 0.06 m/s^2
    results/report.md: 19 lines
    ```

4. Ask Git again.

    ```text
    git status
    ```

    It ends with `nothing to commit, working tree clean`. Every rebuilt file
    has the bytes of the file that was committed, the picture included.

5. Compute the checksum of the report, as in Seminar 4.

    === "macOS"

        ```text
        shasum -a 256 results/report.md
        ```

    === "Windows"

        ```text
        (Get-FileHash results/report.md).Hash
        ```

    It begins with `1bf0d728` and ends with `fb3f`, in capitals on
    Windows. Ask who has the same.

!!! success "You should now see"
    A clean `git status` after a rebuild from nothing but `data/raw`,
    `scripts` and `config.json`.

**Say it in these words.** Any file that `run_all.py` writes can be deleted
at any time. Nothing in `data/raw`, `scripts` or `config.json` can.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The checksum differs from the neighbour's | Compare `data/processed/pendulum.csv` first: 97 bytes on both? Then the two reports line by line. The raw tables differ, or one `config.json` says `true` |
    | `git status` shows the picture as modified | The picture was committed from another environment. Commit the new one |

---

## Part 4 · One test { #part-4 }

**1:30 to 2:00 · sections 9 to 12**

The pipeline gives the same result every time. Whether the result is right
is another question, and it is answered by tests.

---

### 9. A first test { #test }

**1:30 · 10 min**

**Tell the room.** A test states one fact that is known without the script,
and lets the computer check it. Three facts about the cleaned table are
known from the lab notebook and from the raw file: there are nine
measurements, the table has two columns, and the first time is 9.02 s.

1. Select the empty area below the folders, then **New Folder**, and name
   it:

    ```text
    tests
    ```

    Select the folder `tests`, then **New File**, and name it:

    ```text
    test_clean.py
    ```

    The room types this one.

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

3. Run them again, one line per test:

    ```text
    python -m pytest -v
    ```

    Each test is listed by name with `PASSED` beside it.

!!! success "You should now see"
    A line that ends in `3 passed`, with a time of well under a second.

**Say how the tests were found.** pytest runs every function named `test_…`
in every file named `test_….py`. Line 1 imports `clean` from
`scripts/clean.py`. That works because the cleaning is a function and the
script ends with the two lines about `__main__`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `ModuleNotFoundError: No module named 'scripts'` | The command was `pytest`, or the terminal is not at the top of the project. Use `python -m pytest` there |
    | `No module named pytest` | The environment is not active |
    | `collected 0 items` | The file is not named `test_….py`, or the functions are not named `test_…` |

---

### 10. Make it fail { #fail }

**1:40 · 8 min**

**Tell the room.** A test is worth something only if it fails when the code
is wrong. One argument is taken out of the cleaning, the one that is
easiest to forget. First the pipeline runs without the test, to show what
happens when nobody checks.

1. Open `scripts/clean.py`. In the line with `read_csv`, delete this text
   and save:

    ```text
    , decimal=","
    ```

2. Run the pipeline.

    ```text
    python run_all.py
    ```

    It prints:

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

4. Now run the tests.

    ```text
    python -m pytest
    ```

    It ends with `1 failed, 2 passed`. Read the failure with the room:

    ```text
    >       assert table["t10_s"].iloc[0] == 9.02
    E       AssertionError: assert '9,02' == 9.02
    ```

    The line marked `>` is the assertion that failed. The line marked `E`
    shows the two values: the text `'9,02'` and the number 9.02.

5. Put `, decimal=","` back with `Ctrl+Z` (macOS `Cmd+Z`) and save. Run the
   tests, then the pipeline.

    ```text
    python -m pytest
    ```

    ```text
    python run_all.py
    ```

!!! success "You should now see"
    `3 passed`, then four stages that run, and a plot whose points lie on a
    curve again.

---

### 11. Tests in the one command, and the README { #readme }

**1:48 · 7 min**

**Tell the room.** Two things are left. The tests should run without anyone
remembering them, and the README should say how to rebuild the project.
Its section **How to rebuild** from Seminar 4 names one script,
`clean_pendulum.py`. Four stages would need four lines in the right order,
and no line says which packages they import. The section gets its second
version: an environment, then one command.

1. Open `run_all.py` and add three lines above the line that starts with
   `for script`, with an empty line after them.

    ```text
    tests = subprocess.run([sys.executable, "-m", "pytest", "-q"])
    if tests.returncode != 0:
        sys.exit("tests failed, nothing rebuilt")
    ```

2. Run the one command.

    ```text
    python run_all.py
    ```

    The tests come first: a line of three dots and a line with `3 passed`.
    The four lines that end in `up to date` follow.

3. Ask for the version of Python:

    ```text
    python --version
    ```

4. Open `README.md` and its preview. Select the whole section
   **How to rebuild** of Seminar 4, from its heading to the end of its
   step 2, and paste the block below in its place. Step 3 of the block is
   the old step 2, unchanged. In the line **Needs Python** write the
   version that step 3 printed.

    ```text
    ## How to rebuild

    Run in the project folder: zsh on macOS, PowerShell 7 on Windows.
    Needs Python 3.14.

    1. Once, an environment with the versions of `requirements.txt`:
       - zsh: `python3 -m venv .venv`, then `source .venv/bin/activate`
       - PowerShell: `python -m venv .venv`, then `.venv\Scripts\Activate.ps1`
       - both: `pip install -r requirements.txt`
    2. The pendulum table, the plot, the fit and the report:
       `python run_all.py`, in both shells, with the environment active. In a
       new terminal, activate it first with the second command of step 1.
       It runs the tests, then rebuilds what is out of date in
       `data/processed/` and `results/`. The cleaned table has 97 bytes,
       SHA-256 `be05af03…fff0870b`.
    3. `D0_KPi.csv` without the 49 rows marked `-100`, 91 535 lines:
       - zsh: `grep -v ',-100' data/raw/D0_KPi.csv > data/processed/D0_valid.csv`
       - PowerShell: `Select-String ',-100' data/raw/D0_KPi.csv -NotMatch -Raw > data/processed/D0_valid.csv`
    ```

5. Commit.

    ```text
    git add -A
    ```

    ```text
    git commit -m "Tests, and how to rebuild"
    ```

!!! success "You should now see"
    One section **How to rebuild** in the preview of the README, with three
    numbered steps and no `clean_pendulum.py` in it, and a clean
    `git status`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Two sections **How to rebuild** in the preview | The block was pasted below the old section. Delete the old one, from its heading to the end of its step 2 |
    | The preview shows a step as one paragraph | An empty line is missing before `1.`, or the `-` lines are not indented by three spaces |

---

### 12. Wrap up { #wrap-up }

**1:55 · 5 min**

Read the list aloud. Ask on the way out which step was hardest.

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

---

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
  `cd ../analysis-copy` and the lines of your shell in steps 1 and 2 of
  **How to rebuild**. The answer is the tests passing, the four stages
  and a clean `git status`. On Windows, a `git status` that lists the
  three text results as modified means that Git missed the setting
  `core.autocrlf false` of Seminar 5. Then `cd ../analysis-project`,
  activate the environment of the project again, and delete the copy.
- A student who already has data for the semester project: make an
  environment there, install what its scripts import, and write
  `requirements.txt`. Give one of its scripts a command line with a help
  text. Write a `run_all.py` with at least two stages, delete the results,
  run it, and check with `git status` that they came back. Write one test
  of a fact known about that data: the number of rows, the names of the
  columns, or a range that the values cannot leave.
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
| `make` | It applies the same rule to a file named `Makefile`. macOS has it with the developer tools of Seminar 4. Windows has no `make`, in PowerShell or elsewhere, until it is installed separately, which is why this page uses `run_all.py` |
| conda or uv in place of venv | Both can install from the same `requirements.txt`. One tool per project |
| A server that runs `run_all.py` after every push | Continuous integration. The file shown in the lecture works once the project is on GitHub |
| A pipeline with a hundred input files | Snakemake: the same table of stages, with patterns in place of file names |

Leave out, even if asked: Docker, pre-commit hooks, Git LFS. Each was named
in the lecture, and none is needed for a project of this size.

## Aims practised

♻️ pinned versions and a rebuild from raw data · ⚙️ one command for every result · 🔧 one pipeline, run the same way in zsh and in PowerShell · 📁 raw data read, results rebuilt
