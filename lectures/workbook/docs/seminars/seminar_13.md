# Seminar 13 — Can a Stranger Rebuild Every Number? One Command for the Weather Project

**Paired lecture:** 13 Reproducible Workflows · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student pins the project's environment, makes all
of `data/processed` and `results` with one command that also tests the
numbers, and proves it in a fresh clone with a fresh environment: the same
checksums.

Everything is typed in the terminal of VS Code (zsh on macOS, Git Bash on
Windows), in the `weather-project` folder, with `(weather)` in the prompt.

## Run sheet

| Clock | Section | Typed | The room ends with |
|--|--|--|--|
| | **Part 1 · An environment anyone can make** · 25 min | | |
| 0:00 | [1. Install pytest](#pytest) | `conda install pytest` | `pytest 9.1.1` |
| 0:10 | [2. Pin every version](#pin) | `conda list` | six pinned lines, committed |
| | **Part 2 · One command** · 35 min | | |
| 0:25 | [3. The -999 rows in Python](#drop) | `python scripts/drop_missing.py` | 87 553 lines |
| 0:35 | [4. `run_all.py`](#run-all) | `python run_all.py` | four stages and five checksums |
| 0:50 | [5. Delete and rebuild](#rebuild) | `rm -r data/processed results` | the same five checksums, committed |
| | **Part 3 · Tests** · 25 min | | |
| 1:00 | [6. A test file](#test) | `python -m pytest` | `3 passed`, also inside `run_all.py` |
| 1:15 | [7. Make a test fail](#fail) | `python run_all.py` | `1 failed`, `stopped: exit code 1` |
| | **Part 4 · A stranger's laptop** · 35 min | | |
| 1:25 | [8. The README says one command](#readme) | `git rm scripts/rebuild.sh` | the README on GitHub |
| 1:35 | [9. A fresh clone, a fresh environment](#clone) | `conda env create -f environment.yml -n weather-check` | the same five checksums |
| 1:50 | [10. Record the check, push](#record) | `git push` | the check in the README |
| 1:55 | [11. Wrap up](#wrap-up) | `conda env remove -n weather-check` | |
| | **Optional, if the room is fast** | | |
| — | [12. A stage of your own: a figure](#figure) | `python scripts/plot_hill.py` | six checksums |
| — | [13. An option on the command line](#option) | `--min-hours 24` | 351 days compared |

**If time runs short:** skip the Task of Part 3 and go to Part 4 by
1:30; section 9 is the proof the seminar is about.

??? info "Before the session"
    - **Room:** internet (conda downloads pytest, and section 9 makes a
      second environment). Each student has `weather-project` as Seminar 12
      left it, pushed to their GitHub, and the conda environment `weather`.
    - **You:** nothing to prepare. Ids of commits differ on every laptop;
      the checksums do not.
    - **Keys** are written for Windows, macOS in brackets. Every line typed
      is the same on macOS and Windows.

---

## Part 1 · An environment anyone can make { #part-1 }

**0:00 to 0:25** · `environment.yml` lists what the scripts need; today every line gets an exact version.

---

### 1. Install pytest { #pytest }

**0:00 · 10 min** · pytest runs the tests of Part 3.

1. Open `weather-project` in VS Code, then the terminal. Switch on the
   environment.

    ```text
    conda activate weather
    ```

2. Start from a clean state.

    ```text
    git status
    ```

    ```text
    On branch main
    Your branch is up to date with 'origin/main'.

    nothing to commit, working tree clean
    ```

3. pytest is not there yet.

    ```text
    python -m pytest --version
    ```

    ```text
    No module named pytest
    ```

    The line starts with the path of the environment's Python.

4. Install it. Press `Enter` at `Proceed ([y]/n)?`.

    ```text
    conda install pytest
    ```

    ```text
      added / updated specs:
        - pytest
    ```

5. Check.

    ```text
    python -m pytest --version
    ```

    ```text
    pytest 9.1.1
    ```

**Check:** `pytest 9.1.1`.

---

### 2. Pin every version { #pin }

**0:10 · 15 min** · `numpy` without a version means "the newest on the day of install"; a pin means the same on every day.

1. The versions in this environment, for the six packages the project
   asks for.

    ```text
    conda list "^(python|numpy|pandas|matplotlib-base|scipy|pytest)$"
    ```

    ```text
    # Name                     Version          Build               Channel
    matplotlib-base            3.11.2           py314h9124352_1     conda-forge
    numpy                      2.5.4            py314hd3a7d6b_0     conda-forge
    pandas                     3.0.6            np2py314h9e1d7c2_0  conda-forge
    pytest                     9.1.1            pyhc364b38_2        conda-forge
    python                     3.14.8           hcd007b5_102_cp314  conda-forge
    scipy                      1.18.1           py314h36f0660_1     conda-forge
    ```

    The first lines name the folder of the environment. The **Build**
    column differs between macOS and Windows; the versions do not.

2. In `environment.yml`, give every line the full version from that
   list, add `- pytest=9.1.1` as the last line, save.

    ```text
    name: weather
    channels:
      - conda-forge
    dependencies:
      - python=3.14.8
      - numpy=2.5.4
      - matplotlib-base=3.11.2
      - scipy=1.18.1
      - pandas=3.0.6
      - pytest=9.1.1
    ```

    A line from an earlier seminar that is not in this list gets its
    version from `conda list` too.

3. The change.

    ```text
    git diff
    ```

    ```text
    @@ -2,8 +2,9 @@ name: weather
     channels:
       - conda-forge
     dependencies:
    -  - python=3.14
    -  - numpy=2.5
    -  - matplotlib-base=3.11
    -  - scipy
    +  - python=3.14.8
    +  - numpy=2.5.4
    +  - matplotlib-base=3.11.2
    +  - scipy=1.18.1
       - pandas=3.0.6
    +  - pytest=9.1.1
    ```

4. Commit it.

    ```text
    git commit -am "Pin every version in the environment"
    ```

    ```text
    [main ff01c97] Pin every version in the environment
     1 file changed, 5 insertions(+), 4 deletions(-)
    ```

    Your id differs.

**Check:** every line under `dependencies:` has `=` and a full version.

!!! question "Task: what is not pinned?"
    `conda env create` installs about 100 packages for these six (98 on
    Linux). Which of them does `environment.yml` pin, and what decides
    the versions of the rest?

??? note "Answer"
    Only the six. The others (OpenBLAS for numpy, the fonts and image
    libraries of matplotlib, …) are what the six depend on; conda picks
    versions that fit the pinned six, on the day of install, for the
    system. `conda env export` without `--from-history` writes all of
    them with their build strings, but that list only installs on the
    same system:

    ```text
    conda env export | head -n 8
    ```

    ```text
    name: weather
    channels:
      - conda-forge
    dependencies:
      - _openmp_mutex=4.5=20_gnu
      - brotli=1.2.0=h505cf86_4
      - brotli-bin=1.2.0=h9908984_4
      - bzip2=1.0.8=hda65f42_10
    ```

    These lines are from Linux; `_openmp_mutex=4.5=20_gnu` is a build for
    Linux that macOS and Windows do not have. Six pins that install
    everywhere are the choice here; section 9 checks that they are enough.

---

## Part 2 · One command { #part-2 }

**0:25 to 1:00** · `scripts/rebuild.sh` runs its lines in the shell. Today a Python script takes its place: it needs only the environment's Python.

---

### 3. The -999 rows in Python { #drop }

**0:25 · 10 min** · `grep -v` and `>` belong to the shell; `run_all.py` runs Python scripts, so the filter becomes one.

1. In the Explorer, right-click `scripts` > **New File...**, type
   `drop_missing.py`, press `Enter`. Write and save:

    ```python
    """Write weather.csv without the rows whose temp_c is -999.

    Run from the project folder:  python scripts/drop_missing.py
    """
    import os

    RAW = "data/raw/weather.csv"
    OUT = "data/processed/weather_valid.csv"

    with open(RAW, encoding="utf-8") as source:
        lines = [line for line in source if ",-999," not in line]
    os.makedirs("data/processed", exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as target:
        target.writelines(lines)
    print(len(lines) - 1, "rows written to", OUT)
    ```

2. Run it.

    ```text
    python scripts/drop_missing.py
    ```

    ```text
    87552 rows written to data/processed/weather_valid.csv
    ```

3. Count the lines.

    ```text
    wc -l data/processed/weather_valid.csv
    ```

    ```text
    87553 data/processed/weather_valid.csv
    ```

**Check:** 87 553 lines: 87 672 hours, minus 120 rows of −999, plus the header.

---

### 4. `run_all.py` { #run-all }

**0:35 · 15 min** · The stages as a table, run in order; the run stops at the first stage that fails.

1. In the Explorer, right-click the empty space under the files > **New
   File...**, type `run_all.py`, press `Enter`. It sits next to the
   README. Write and save:

    ```python
    """Make data/processed and results from data/raw: python run_all.py"""
    import hashlib
    import os
    import subprocess
    import sys

    # One line per stage: the words after `python`, and the file for its output.
    STAGES = [
        (["scripts/drop_missing.py"], None),
        (["scripts/clean_export.py", "data/raw/daily_export.csv",
          "data/processed/daily.csv"], None),
        (["scripts/column_stats.py", "data/processed/weather_valid.csv",
          "temp_c"], "results/temp_c.txt"),
        (["scripts/clean_hill.py"], "results/hill.txt"),
    ]

    os.makedirs("results", exist_ok=True)
    for words, output in STAGES:
        print("==", " ".join(words), flush=True)
        done = subprocess.run([sys.executable] + words,
                              capture_output=True, text=True)
        print(done.stdout + done.stderr, end="")
        if done.returncode != 0:
            sys.exit(f"stopped: exit code {done.returncode}")
        if output:
            with open(output, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(done.stdout)

    # The checksum of every file made: the same digits on every laptop.
    for folder in ["data/processed", "results"]:
        for name in sorted(os.listdir(folder)):
            path = f"{folder}/{name}"
            with open(path, "rb") as handle:
                digest = hashlib.sha256(handle.read()).hexdigest()
            print(digest[:12], path)
    ```

    `sys.executable` is the Python running `run_all.py`: the one of the
    active environment.

2. Run it.

    ```text
    python run_all.py
    ```

    ```text
    == scripts/drop_missing.py
    87552 rows written to data/processed/weather_valid.csv
    == scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
    9 rows written to data/processed/daily.csv
    == scripts/column_stats.py data/processed/weather_valid.csv temp_c
    file    data/processed/weather_valid.csv
    column  temp_c
    rows    87552
    min     -16.3
    max     32.4
    mean    7.15997
    == scripts/clean_hill.py
    rows read       8740
    temp missing    27
    rows in F       72
    duplicate rows  24
    days < 20 hours 4
    days compared   361
    hill - valley   -1.19
    33fe5e77a979 data/processed/daily.csv
    67106615f8c1 data/processed/hill_daily.csv
    85b1f38d0df9 data/processed/weather_valid.csv
    58c921c33f22 results/hill.txt
    ade2805b90fe results/temp_c.txt
    ```

    Files made by your own scripts of earlier seminars are listed too;
    section 5 deletes them.

**Check:** `mean 7.15997`, `hill - valley -1.19`, and the five checksums
above, digit for digit.

---

### 5. Delete and rebuild { #rebuild }

**0:50 · 10 min** · Everything in `data/processed` and `results` must come back from `data/raw` alone.

1. Delete both folders.

    ```text
    rm -r data/processed results
    ```

    ```text
    ls data
    ```

    ```text
    raw
    ```

2. Rebuild.

    ```text
    python run_all.py
    ```

    The same lines as in section 4, ending with:

    ```text
    33fe5e77a979 data/processed/daily.csv
    67106615f8c1 data/processed/hill_daily.csv
    85b1f38d0df9 data/processed/weather_valid.csv
    58c921c33f22 results/hill.txt
    ade2805b90fe results/temp_c.txt
    ```

3. The exit code: 0 means every stage ran.

    ```text
    echo $?
    ```

    ```text
    0
    ```

4. Git sees only the two new files; the made files are in `.gitignore`.

    ```text
    git status --short
    ```

    ```text
    ?? run_all.py
    ?? scripts/drop_missing.py
    ```

5. Commit.

    ```text
    git add run_all.py scripts/drop_missing.py
    ```

    ```text
    git commit -m "Make everything from data/raw with one command"
    ```

    ```text
    [main 799e5a6] Make everything from data/raw with one command
     2 files changed, 50 insertions(+)
     create mode 100644 run_all.py
     create mode 100644 scripts/drop_missing.py
    ```

**Check:** the same five checksums as before the delete.

!!! question "Task: a stage that fails"
    Rename `data/raw/daily_export.csv` to `daily_export.bak` with `mv`,
    run `run_all.py`, and read the exit code. Which stages
    ran? Then give the file its name back.

??? note "Answer"
    ```text
    mv data/raw/daily_export.csv data/raw/daily_export.bak
    ```

    ```text
    python run_all.py
    ```

    ```text
    == scripts/drop_missing.py
    87552 rows written to data/processed/weather_valid.csv
    == scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
    no file data/raw/daily_export.csv
    stopped: exit code 1
    ```

    ```text
    echo $?
    ```

    ```text
    1
    ```

    The first stage ran, the second failed, the last two did not run: they
    would have read files that were not made.

    ```text
    mv data/raw/daily_export.bak data/raw/daily_export.csv
    ```

---

## Part 3 · Tests { #part-3 }

**1:00 to 1:25** · A test states a number known without the scripts; a wrong number then stops the run.

---

### 6. A test file { #test }

**1:00 · 15 min** · pytest runs every function whose name starts with `test_`, in files named `test_*.py`.

1. In the Explorer, right-click the empty space > **New File...**, type
   `tests/test_results.py`, press `Enter`. VS Code makes the folder too.
   Write and save:

    ```python
    """Facts about the results, known without the scripts: python -m pytest"""
    import pytest


    def read(path):
        """The lines of a file the rebuild made."""
        with open(path, encoding="utf-8") as handle:
            return handle.read().splitlines()


    def numbers(path):
        """A file of `name value` lines, as a dict."""
        return dict(line.rsplit(maxsplit=1) for line in read(path))


    def test_valid_rows():
        # 87 672 hours, 120 of them -999, and the header line
        assert len(read("data/processed/weather_valid.csv")) == 87553


    def test_mean_temperature():
        stats = numbers("results/temp_c.txt")
        assert stats["rows"] == "87552"
        assert float(stats["mean"]) == pytest.approx(7.16, abs=0.005)


    def test_hill_station():
        hill = numbers("results/hill.txt")
        assert hill["days compared"] == "361"
        assert float(hill["hill - valley"]) == pytest.approx(-1.19, abs=0.005)
    ```

    `pytest.approx` compares floats within a tolerance: 7.15997 is 7.16
    within 0.005.

2. Run the tests.

    ```text
    python -m pytest
    ```

    ```text
    ============================= test session starts ==============================
    platform darwin -- Python 3.14.8, pytest-9.1.1, pluggy-1.6.0
    rootdir: /Users/smilte/weather-project
    collected 3 items

    tests/test_results.py ...                                                [100%]

    ============================== 3 passed in 0.01s ===============================
    ```

    One dot per test that passed.

3. Python left a `__pycache__` folder in `tests`. In `.gitignore`, add a
   last line and save.

    ```text
    __pycache__/
    ```

4. In `run_all.py`, add the tests as the last stage, before the `]`.

    ```text
        (["-m", "pytest", "-q"], None),
    ```

5. Run the one command.

    ```text
    python run_all.py
    ```

    It ends with:

    ```text
    == -m pytest -q
    ...                                                                      [100%]
    3 passed in 0.01s
    33fe5e77a979 data/processed/daily.csv
    67106615f8c1 data/processed/hill_daily.csv
    85b1f38d0df9 data/processed/weather_valid.csv
    58c921c33f22 results/hill.txt
    ade2805b90fe results/temp_c.txt
    ```

6. Commit the three files.

    ```text
    git add .gitignore run_all.py tests/test_results.py
    ```

    ```text
    git commit -m "Test the results at the end of run_all.py"
    ```

    ```text
    [main 573d364] Test the results at the end of run_all.py
     3 files changed, 32 insertions(+)
     create mode 100644 tests/test_results.py
    ```

**Check:** `3 passed`, and `git status` clean.

---

### 7. Make a test fail { #fail }

**1:15 · 10 min** · Tomas's change of Seminar 5 again: the mean of the raw file, `-999` rows and all.

1. In `run_all.py`, in the `column_stats.py` stage, change
   `data/processed/weather_valid.csv` to `data/raw/weather.csv`. Save.
2. Run.

    ```text
    python run_all.py
    ```

    ```text
    == scripts/column_stats.py data/raw/weather.csv temp_c
    file    data/raw/weather.csv
    column  temp_c
    rows    87672
    min     -999.0
    max     32.4
    mean    5.7828
    ```

    The stage ran without an error. The tests stop it:

    ```text
    == -m pytest -q
    .F.                                                                      [100%]
    =================================== FAILURES ===================================
    ____________________________ test_mean_temperature _____________________________

        def test_mean_temperature():
            stats = numbers("results/temp_c.txt")
    >       assert stats["rows"] == "87552"
    E       AssertionError: assert '87672' == '87552'
    E
    E         - 87552
    E         + 87672

    tests/test_results.py:23: AssertionError
    =========================== short test summary info ============================
    FAILED tests/test_results.py::test_mean_temperature - AssertionError: assert ...
    1 failed, 2 passed in 0.02s
    stopped: exit code 1
    ```

    The failure names the test, the line, and the two values.

3. Take the edit back.

    ```text
    git restore run_all.py
    ```

4. The tests read the files, which are still the wrong ones.

    ```text
    python -m pytest -q
    ```

    ```text
    1 failed, 2 passed in 0.02s
    ```

    That line comes last, after the failure.

5. Rebuild.

    ```text
    python run_all.py
    ```

    ```text
    3 passed in 0.01s
    ```

    That line comes just above the five checksums.

**Check:** `3 passed` again, and `git status` clean.

!!! question "Task: a test for the export"
    Add a test: `data/processed/daily.csv` has 10 lines, and its first
    row is 1 October 2025. Run the one command.

??? note "Answer"
    At the end of `tests/test_results.py`:

    ```python
    def test_daily_export():
        lines = read("data/processed/daily.csv")
        assert len(lines) == 10
        assert lines[1].startswith("2025-10-01,")
    ```

    ```text
    python run_all.py
    ```

    ```text
    4 passed in 0.01s
    ```

    Commit it: `git commit -am "Test the cleaned export"`.

---

## Part 4 · A stranger's laptop { #part-4 }

**1:25 to 2:00** · A stranger has the repository and the README, nothing else. A second folder and a second environment play the stranger.

---

### 8. The README says one command { #readme }

**1:25 · 10 min** · `run_all.py` does what `rebuild.sh` did, so the old script goes.

1. In `README.md`, replace the section `## How to rebuild` (up to the
   next `##`) with this, and save:

    ```text
    ## How to rebuild

    In zsh on macOS or Git Bash on Windows, with Miniforge, in the project folder:

        conda env create -f environment.yml
        conda activate weather
        python run_all.py

    `run_all.py` makes `data/processed` and `results` from `data/raw`, runs the
    tests and prints the checksum of every file it made.
    ```

2. Remove the old script; Git deletes the file and stages the deletion.

    ```text
    git rm scripts/rebuild.sh
    ```

    ```text
    rm 'scripts/rebuild.sh'
    ```

3. Stage the README, look, commit.

    ```text
    git add README.md
    ```

    ```text
    git status --short
    ```

    ```text
    M  README.md
    D  scripts/rebuild.sh
    ```

    ```text
    git commit -m "Rebuild with conda and run_all.py"
    ```

    ```text
    [main 64f4a99] Rebuild with conda and run_all.py
     2 files changed, 6 insertions(+), 13 deletions(-)
     delete mode 100755 scripts/rebuild.sh
    ```

4. Push.

    ```text
    git push
    ```

    ```text
    To https://github.com/your-username/weather-project.git
       40ac9f0..64f4a99  main -> main
    ```

**Check:** on GitHub, the README's **How to rebuild** shows the three lines.

---

### 9. A fresh clone, a fresh environment { #clone }

**1:35 · 15 min** · The stranger follows the README word for word, in a second folder.

1. Go to the home folder and clone your repository into `weather-check`.

    ```text
    cd ~
    ```

    ```text
    git clone https://github.com/your-username/weather-project.git weather-check
    ```

    ```text
    Cloning into 'weather-check'...
    ```

2. Go in and look.

    ```text
    cd weather-check
    ```

    ```text
    ls data
    ```

    ```text
    raw
    ```

    No `data/processed`, and no `results` either.

3. A new environment from the file. The name `weather` is taken on this
   laptop, so `-n` gives another one.

    ```text
    conda env create -f environment.yml -n weather-check
    ```

    ```text
      added / updated specs:
        - matplotlib-base=3.11.2
        - numpy=2.5.4
        - pandas=3.0.6
        - pytest=9.1.1
        - python=3.14.8
        - scipy=1.18.1
    ```

    About 100 packages; most are in conda's cache from `weather`, so it
    takes a minute. It ends with:

    ```text
    #     $ conda activate weather-check
    ```

4. Switch it on.

    ```text
    conda activate weather-check
    ```

    The prompt starts with `(weather-check)`.

5. The one command.

    ```text
    python run_all.py
    ```

    It ends with:

    ```text
    3 passed in 0.01s
    33fe5e77a979 data/processed/daily.csv
    67106615f8c1 data/processed/hill_daily.csv
    85b1f38d0df9 data/processed/weather_valid.csv
    58c921c33f22 results/hill.txt
    ade2805b90fe results/temp_c.txt
    ```

6. Compare the five checksums with section 5, and with your neighbour's
   screen, a Mac beside a Windows laptop.

**Check:** the same five checksums in both folders and on every laptop in
the room. A test you added in the Task makes it `4 passed`.

!!! warning "`git clone` asks for a password"
    The repository is private. Run the clone in VS Code's terminal, which
    signs in with the GitHub account of Seminar 5.

---

### 10. Record the check, push { #record }

**1:50 · 5 min** · The README says when the check was made and what it found.

1. Back to the project and its environment.

    ```text
    cd ~/weather-project
    ```

    ```text
    conda activate weather
    ```

2. In `README.md`, under the line that ends with `every file it made.`,
   add a line and save.

    ```text
    Checked on 2026-12-22 in a fresh clone: the same five checksums.
    ```

3. Commit and push.

    ```text
    git commit -am "Record the check in a fresh clone"
    ```

    ```text
    [main 13d8c7a] Record the check in a fresh clone
     1 file changed, 2 insertions(+)
    ```

    ```text
    git push
    ```

    ```text
    To https://github.com/your-username/weather-project.git
       64f4a99..13d8c7a  main -> main
    ```

4. Today's history.

    ```text
    git log --oneline -n 6
    ```

    ```text
    13d8c7a Record the check in a fresh clone
    64f4a99 Rebuild with conda and run_all.py
    573d364 Test the results at the end of run_all.py
    799e5a6 Make everything from data/raw with one command
    ff01c97 Pin every version in the environment
    40ac9f0 Clean the hill station's file and compare it with the valley
    ```

**Check:** the check line on GitHub.

---

### 11. Wrap up { #wrap-up }

**1:55 · 5 min**

1. Remove the stranger's environment; answer `y` to both questions.

    ```text
    conda env remove -n weather-check
    ```

2. Remove the stranger's folder.

    ```text
    rm -rf ~/weather-check
    ```

| To | Type |
|--|--|
| see the exact version of a package | `conda list pandas` |
| make the environment on any laptop | `conda env create -f environment.yml` |
| make every file from `data/raw` | `python run_all.py` |
| check the numbers | `python -m pytest` |
| did every stage run? | `echo $?` |
| delete what the scripts make | `rm -r data/processed results` |
| remove a file from Git and the folder | `git rm FILE` |

---

## Optional, if the room is fast { #optional }

---

### 12. A stage of your own: a figure { #figure }

**— · 10 min** · A file in `results` that no stage makes cannot be rebuilt by a stranger. Each script of your own from earlier seminars gets a stage the same way.

1. In `scripts`, a new file `plot_hill.py`. Write and save:

    ```python
    """The hill minus the valley, month by month: python scripts/plot_hill.py"""
    import matplotlib.pyplot as plt
    import pandas as pd

    hill = pd.read_csv("data/processed/hill_daily.csv", index_col="time",
                       parse_dates=True)["hill"]
    v = pd.read_csv("data/raw/weather.csv", na_values=["-999"],
                    parse_dates=["time"])
    valley = v.set_index("time")["temp_c"].resample("D").mean()
    diff = (hill - valley).dropna()
    month = diff.groupby(diff.index.month).mean()
    month.plot.bar(xlabel="month", ylabel="hill - valley (°C)")
    plt.savefig("results/hill_by_month.png")
    print("results/hill_by_month.png:", len(month), "bars from",
          round(month.max(), 2), "to", round(month.min(), 2))
    ```

2. In `run_all.py`, a stage after `clean_hill.py`, before the tests.

    ```text
        (["scripts/plot_hill.py"], None),
    ```

3. Run.

    ```text
    python run_all.py
    ```

    It ends with:

    ```text
    == scripts/plot_hill.py
    results/hill_by_month.png: 12 bars from -0.82 to -1.63
    == -m pytest -q
    ...                                                                      [100%]
    3 passed in 0.01s
    33fe5e77a979 data/processed/daily.csv
    67106615f8c1 data/processed/hill_daily.csv
    85b1f38d0df9 data/processed/weather_valid.csv
    58c921c33f22 results/hill.txt
    214f49e6e708 results/hill_by_month.png
    ade2805b90fe results/temp_c.txt
    ```

4. Run it again: the figure's checksum stays. Commit both files.

    ```text
    git add run_all.py scripts/plot_hill.py
    ```

    ```text
    git commit -m "Plot the difference by month as a stage"
    ```

**Check:** six checksums, the figure's the same on every run on this
laptop. A figure can differ from your neighbour's, by the fonts of the
system; the tests check numbers, not pixels.

---

### 13. An option on the command line { #option }

**— · 10 min** · The 20 hours of `clean_hill.py` become an option with a default, read by `argparse`.

1. In `scripts/clean_hill.py`, add `import argparse` above `import os`.
   Under the line `OUT = …`, add:

    ```python
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-hours", type=int, default=20,
                        help="hours a day needs to be kept (default 20)")
    args = parser.parse_args()
    ```

2. Replace the two lines with `20` in them:

    ```python
    print("days too short ", (day["hours"] < args.min_hours).sum())
    day = day[day["hours"] >= args.min_hours]
    ```

3. The help, written by `argparse`.

    ```text
    python scripts/clean_hill.py --help
    ```

    ```text
    usage: clean_hill.py [-h] [--min-hours MIN_HOURS]

    Clean the hill station's export; compare it with the valley, day by day. Run
    from the project folder: python scripts/clean_hill.py

    options:
      -h, --help            show this help message and exit
      --min-hours MIN_HOURS
                            hours a day needs to be kept (default 20)
    ```

4. Only full days.

    ```text
    python scripts/clean_hill.py --min-hours 24
    ```

    ```text
    rows read       8740
    temp missing    27
    rows in F       72
    duplicate rows  24
    days too short  14
    days compared   351
    hill - valley   -1.2
    ```

5. A word where a number belongs.

    ```text
    python scripts/clean_hill.py --min-hours twenty
    ```

    ```text
    usage: clean_hill.py [-h] [--min-hours MIN_HOURS]
    clean_hill.py: error: argument --min-hours: invalid int value: 'twenty'
    ```

    `echo $?` prints `2`.

6. Run the one command: `run_all.py` passes no option, so the default 20
   holds and the tests pass. The checksum of `results/hill.txt` changes to
   `b8bc8972e9c6`: one label of its text changed, the numbers did not.

**Check:** 351 days with `--min-hours 24`, 361 without.

---

## Aims practised

- ♻️ **Reproducibility:** a fresh clone and a fresh environment give the
  same five checksums; the tests say which number broke and where.
- ⚙️ **Automation:** one command makes every file from `data/raw`, stops
  at the first stage that fails, and checks the numbers.
- 🔧 **Tool-agnostic:** the same `python run_all.py` and the same bytes on
  macOS and Windows; `environment.yml` names versions, not a laptop.
