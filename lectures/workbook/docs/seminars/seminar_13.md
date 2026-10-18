# Seminar 13 · Workflows

**Paired lecture:** 13 Reproducible Workflows · **Format:** type-along tutorial, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's goal:** Can a stranger rebuild every number? Every student pins the project's environment, makes all
of `data/processed` and `results` with one command that also tests the
numbers, and proves it in a fresh clone with a fresh environment: the same
checksums.

Everything is typed in VS Code's terminal (zsh on macOS, Git Bash on
Windows), in today's folder `weather-s13`, with `(s13)` in the prompt.
In the blocks, a line that starts with `$` is typed in the terminal, a line
that starts with `>>>` or `...` is typed at Python's prompt, and every other
line is what comes back.

**If time runs short:** skip the Task of Part 3 and go to Part 4; section 9
is the proof the seminar is about.

??? info "Before the session"
    - **Room:** VS Code, Miniforge (`conda`), Git with a name and e-mail
      set, and internet: section 1 downloads today's folder and makes its
      environment, section 9 a second one. Nothing from an earlier seminar
      is needed.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` and Git: [Setup, steps 2–4](../setup.md#shell); your name for
      Git: [Setup, step 6](../setup.md#github).
    - **You:** nothing to prepare. Today's folder is
      [`weather-s13.zip`](https://github.com/MindaugasSarpis/weather-project/releases)
      on the course repository's Releases page: the weather project with
      the hill station's file and `scripts/clean_hill.py`, as a Git
      repository with one commit. Ids of commits made today differ on every
      laptop; the checksums do not.
    - **Keys** are written for Windows, macOS in brackets. Every line typed
      is the same on macOS and Windows.

---

## Part 1 · An environment anyone can make { #part-1 }

<!-- 0:00 to 0:25 -->

`environment.yml` lists what the scripts need; today every line gets an exact version.

Further reading: [The Turing Way, Reproducible environments](https://book.the-turing-way.org/reproducible-research/renv);
[pytest, Get started](https://docs.pytest.org/en/stable/getting-started.html).

---

### 1. Today's folder, its environment and pytest { #pytest }

<!-- 0:00 · 10 min -->

Today's folder is a Git repository with one commit. **pytest** runs tests: small functions that check a number. Part 3 writes them.

1. On the course repository's
   [Releases page](https://github.com/MindaugasSarpis/weather-project/releases),
   under **Assets**, click `weather-s13.zip`. In VS Code's terminal,
   unpack it into the home folder and go in.

    ```text
    $ unzip ~/Downloads/weather-s13.zip -d ~
    Archive:  /Users/smilte/Downloads/weather-s13.zip
       creating: /Users/smilte/weather-s13/
    ...
    $ cd ~/weather-s13
    $ ls
    README.md  data  environment.yml  results  scripts
    ```

    Safari unpacks a download by itself: then type
    `mv ~/Downloads/weather-s13 ~` instead of `unzip`.

2. **File** > **Open Folder...** > `weather-s13`, then **View** >
   **Terminal**. The folder is a repository: one commit, nothing changed.

    ```text
    $ git log --oneline
    7f5c9f6 The starting folder of the seminar
    $ git status
    On branch main
    nothing to commit, working tree clean
    ```

3. Make the conda environment `s13` from `environment.yml` (Python with
   NumPy, Matplotlib, SciPy and pandas), then switch it on: the prompt
   starts with `(s13)`.

    ```text
    $ conda env create -n s13 -f environment.yml
    ...
    #     $ conda activate s13
    $ conda activate s13
    ```

    `conda: command not found`: install Miniforge as on the
    [Setup page, steps 2–4](../setup.md#shell), then open a new terminal.

4. pytest is not there yet. `python -m pytest` runs pytest as a module of
   this Python; the answer starts with that Python's path.

    ```text
    $ python -m pytest --version
    /opt/homebrew/Caskroom/miniforge/base/envs/s13/bin/python: No module named pytest
    ```

5. Install it. Press `Enter` at `Proceed ([y]/n)?`. Then check.

    ```text
    $ conda install pytest
      added / updated specs:
        - pytest
    ...
    $ python -m pytest --version
    pytest 9.1.1
    ```

**Check:** `(s13)` in the prompt and `pytest 9.1.1`.

---

### 2. Pin every version { #pin }

<!-- 0:10 · 15 min -->

`numpy=2.5` means "the newest 2.5.x on the day of install"; a full pin, `numpy=2.5.4`, means the same on every day.

1. The versions in this environment, for the seven packages the project
   asks for. `conda list` takes a pattern: `^(...)$` means exactly one of
   these names.

    ```text
    $ conda list "^(jupyterlab|python|numpy|pandas|matplotlib-base|scipy|pytest)$"
    # Name                     Version          Build               Channel
    jupyterlab                 4.6.4            pyhd8ed1ab_0        conda-forge
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
    name: s13
    channels:
      - conda-forge
    dependencies:
      - jupyterlab=4.6.4
      - python=3.14.8
      - numpy=2.5.4
      - matplotlib-base=3.11.2
      - scipy=1.18.1
      - pandas=3.0.6
      - pytest=9.1.1
    ```

    A line from an earlier seminar that is not in this list gets its
    version from `conda list` too.

3. The change; `-U0` shows the changed lines only.

    ```text
    $ git diff -U0
    @@ -5,5 +5,5 @@ dependencies:
    -  - jupyterlab=4.6
    -  - python=3.14
    -  - numpy=2.5
    -  - matplotlib-base=3.11
    -  - scipy=1.18
    +  - jupyterlab=4.6.4
    +  - python=3.14.8
    +  - numpy=2.5.4
    +  - matplotlib-base=3.11.2
    +  - scipy=1.18.1
    @@ -10,0 +11 @@ dependencies:
    +  - pytest=9.1.1
    ```

4. Commit it.

    ```text
    $ git commit -am "Pin every version in the environment"
    [main be0e110] Pin every version in the environment
     1 file changed, 6 insertions(+), 5 deletions(-)
    ```

    Your id differs.

**Check:** every line under `dependencies:` has `=` and a full version.

!!! question "Task: what is not pinned?"
    `conda env create` installs about 200 packages for these seven (207 on
    Linux). Which of them does `environment.yml` pin, and what decides
    the versions of the rest?

??? success "Answer"
    Only the seven. The others (OpenBLAS for numpy, the fonts and image
    libraries of matplotlib, the web server of JupyterLab, …) are what
    the seven depend on; conda picks versions that fit the pinned seven,
    on the day of install, for the system. `conda env export` without
    `--from-history` writes all of them with their build strings, but that
    list only installs on the same system:

    ```text
    $ conda env export | head -n 8
    name: s13
    channels:
      - conda-forge
    dependencies:
      - _openmp_mutex=4.5=20_gnu
      - _python_abi3_support=1.0=hd8ed1ab_3
      - anyio=4.15.1=pyh5ded981_1
      - argon2-cffi=25.1.0=pyhd8ed1ab_0
    ```

    These lines are from Linux; `_openmp_mutex=4.5=20_gnu` is a build for
    Linux that macOS and Windows do not have. Seven pins that install
    everywhere are the choice here; section 9 checks that they are enough.

---

## Part 2 · One command { #part-2 }

<!-- 0:25 to 1:00 -->

`scripts/rebuild.sh` runs its lines in the shell. Today a Python script takes its place: it needs only the environment's Python.

---

### 3. The -999 rows in Python { #drop }

<!-- 0:25 · 10 min -->

`grep -v` and `>` belong to the shell; `run_all.py` will run Python scripts only, so the filter becomes one.

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

2. Run it, then count the lines it wrote. The list in one line kept every
   line without `,-999,`; `newline="\n"` writes the same bytes on macOS
   and Windows.

    ```text
    $ python scripts/drop_missing.py
    87552 rows written to data/processed/weather_valid.csv
    $ wc -l data/processed/weather_valid.csv
    87553 data/processed/weather_valid.csv
    ```

**Check:** 87 553 lines: 87 672 hours, minus 120 rows of −999, plus the header.

---

### 4. `run_all.py` { #run-all }

<!-- 0:35 · 15 min -->

One Python script runs the others, in order, and stops at the first that fails. First at the prompt, then in a file.

1. Start Python. `subprocess.run` starts a program and waits for it;
   `sys.executable` is the Python that is running now, the one of the
   active environment.

    ```pycon
    $ python
    >>> import subprocess, sys
    >>> sys.executable
    '/opt/homebrew/Caskroom/miniforge/base/envs/s13/bin/python'
    ```

    Your path differs (Git Bash: `C:\Users\…\miniforge3\envs\s13\python.exe`).

2. Run one stage. `capture_output=True, text=True` keeps what it prints,
   as text. `returncode` is the exit code: 0 means it worked.

    ```pycon
    >>> done = subprocess.run([sys.executable, "scripts/drop_missing.py"], capture_output=True, text=True)
    >>> done.returncode
    0
    >>> done.stdout
    '87552 rows written to data/processed/weather_valid.csv\n'
    ```

3. A stage that fails: a file that is not there. The exit code is 1, and
   the message is in `stdout`. Then leave Python.

    ```pycon
    >>> bad = subprocess.run([sys.executable, "scripts/clean_export.py", "data/raw/nothing.csv", "out.csv"], capture_output=True, text=True)
    >>> bad.returncode
    1
    >>> bad.stdout, bad.stderr
    ('no file data/raw/nothing.csv\n', '')
    >>> exit()
    ```

4. The same in a file: right-click the empty space of the Explorer >
   **New File...**, `run_all.py` (next to the README). First, the stages:

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
    ```

5. Under it, the loop over the stages: it stops at the first exit code
   that is not 0.

    ```python
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
    ```

6. Last, the checksum of every file made. Save.

    ```python
    # The checksum of every file made: the same digits on every laptop.
    for folder in ["data/processed", "results"]:
        for name in sorted(os.listdir(folder)):
            path = f"{folder}/{name}"
            with open(path, "rb") as handle:
                digest = hashlib.sha256(handle.read()).hexdigest()
            print(digest[:12], path)
    ```

7. Run it. Each stage prints `==` and its words, then what it printed.

    ```text
    $ python run_all.py
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
    ```

8. Then the hill's stage:

    ```text
    == scripts/clean_hill.py
    rows read       8740
    temp missing    27
    rows in F       72
    duplicate rows  24
    days < 20 hours 4
    days compared   361
    hill - valley   -1.19
    ```

9. Last, the checksums of the files it made: the first 12 hex digits of
   each file's SHA-256.

    ```text
    33fe5e77a979 data/processed/daily.csv
    67106615f8c1 data/processed/hill_daily.csv
    85b1f38d0df9 data/processed/weather_valid.csv
    58c921c33f22 results/hill.txt
    ade2805b90fe results/temp_c.txt
    ```

**Check:** `mean 7.15997`, `hill - valley -1.19`, and the five checksums
above, digit for digit.

---

### 5. Delete and rebuild { #rebuild }

<!-- 0:50 · 10 min -->

Everything in `data/processed` and `results` must come back from `data/raw` alone.

1. Delete both folders.

    ```text
    $ rm -r data/processed results
    $ ls data
    raw
    ```

2. Rebuild. The same lines as in section 4, ending with:

    ```text
    $ python run_all.py
    ...
    33fe5e77a979 data/processed/daily.csv
    67106615f8c1 data/processed/hill_daily.csv
    85b1f38d0df9 data/processed/weather_valid.csv
    58c921c33f22 results/hill.txt
    ade2805b90fe results/temp_c.txt
    ```

3. The exit code: 0 means every stage ran.

    ```text
    $ echo $?
    0
    ```

4. Git sees only the two new files; the made files are in `.gitignore`.

    ```text
    $ git status --short
    ?? run_all.py
    ?? scripts/drop_missing.py
    ```

5. Commit.

    ```text
    $ git add run_all.py scripts/drop_missing.py
    $ git commit -m "Make everything from data/raw with one command"
    [main 315a8af] Make everything from data/raw with one command
     2 files changed, 50 insertions(+)
     create mode 100644 run_all.py
     create mode 100644 scripts/drop_missing.py
    ```

**Check:** the same five checksums as before the delete.

!!! question "Task: a stage that fails"
    Rename `data/raw/daily_export.csv` to `daily_export.bak` with `mv`,
    run `run_all.py`, and read the exit code. Which stages
    ran? Then give the file its name back.

??? success "Answer"
    ```text
    $ mv data/raw/daily_export.csv data/raw/daily_export.bak
    $ python run_all.py
    == scripts/drop_missing.py
    87552 rows written to data/processed/weather_valid.csv
    == scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
    no file data/raw/daily_export.csv
    stopped: exit code 1
    $ echo $?
    1
    $ mv data/raw/daily_export.bak data/raw/daily_export.csv
    ```

    The first stage ran, the second failed, the last two did not run: they
    would have read files that were not made.

---

## Part 3 · Tests { #part-3 }

<!-- 1:00 to 1:25 -->

A test states a number known without the scripts; a wrong number then stops the run.

---

### 6. A test file { #test }

<!-- 1:00 · 15 min -->

A test is an `assert`: a line that does nothing when its statement is true and stops when it is false.

1. At the prompt first. `assert` with a true statement prints nothing;
   with a false one it raises `AssertionError`.

    ```pycon
    $ python
    >>> assert 87672 - 120 == 87552
    >>> assert 87672 - 120 == 87553
    Traceback (most recent call last):
      ...
    AssertionError
    ```

2. Floats are compared within a tolerance: `0.1 + 0.2` is not exactly
   `0.3` in binary. `pytest.approx` says "equal within".

    ```pycon
    >>> 0.1 + 0.2 == 0.3
    False
    >>> import pytest
    >>> 0.1 + 0.2 == pytest.approx(0.3)
    True
    >>> 7.15997 == pytest.approx(7.16, abs=0.005)
    True
    >>> 7.15997 == pytest.approx(7.17, abs=0.005)
    False
    >>> exit()
    ```

3. pytest runs every function whose name starts with `test_`, in files
   named `test_*.py`. In the Explorer, right-click the empty space > **New
   File...**, type `tests/test_results.py`, press `Enter`. VS Code makes
   the folder too. Write its first part, two helpers that read a file:

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
    ```

4. Under them, the three tests, each a number known without the scripts.
   Save.

    ```python
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

5. Run the tests: one dot per test that passed.

    ```text
    $ python -m pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.14.8, pytest-9.1.1, pluggy-1.7.0
    rootdir: /Users/smilte/weather-s13
    plugins: platformdirs-4.13.3, anyio-4.15.1
    collected 3 items

    tests/test_results.py ...                                                [100%]

    ============================== 3 passed in 0.01s ===============================
    ```

    Python left a `__pycache__` folder in `tests`; `.gitignore` already
    leaves it out.

6. In `run_all.py`, add the tests as the last stage, before the `]`.

    ```text
        (["-m", "pytest", "-q"], None),
    ```

7. Run the one command. It ends with:

    ```text
    $ python run_all.py
    ...
    == -m pytest -q
    ...                                                                      [100%]
    3 passed in 0.01s
    33fe5e77a979 data/processed/daily.csv
    67106615f8c1 data/processed/hill_daily.csv
    85b1f38d0df9 data/processed/weather_valid.csv
    58c921c33f22 results/hill.txt
    ade2805b90fe results/temp_c.txt
    ```

8. Commit the two files.

    ```text
    $ git add run_all.py tests/test_results.py
    $ git commit -m "Test the results at the end of run_all.py"
    [main 3182c7e] Test the results at the end of run_all.py
     2 files changed, 26 insertions(+)
     create mode 100644 tests/test_results.py
    ```

**Check:** `3 passed`, and `git status` clean.

---

### 7. Make a test fail { #fail }

<!-- 1:15 · 10 min -->

Tomas's change of Seminar 6 again: the mean of the raw file, `-999` rows and all.

1. In `run_all.py`, in the `column_stats.py` stage, change
   `data/processed/weather_valid.csv` to `data/raw/weather.csv`. Save.
2. Run. The stage runs without an error:

    ```text
    $ python run_all.py
    ...
    == scripts/column_stats.py data/raw/weather.csv temp_c
    file    data/raw/weather.csv
    column  temp_c
    rows    87672
    min     -999.0
    max     32.4
    mean    5.7828
    ```

3. The tests stop it. The failure names the test, the line, and the two
   values.

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

    tests/test_results.py:19: AssertionError
    ```

4. The last lines: the summary, and `run_all.py` stops.

    ```text
    =========================== short test summary info ============================
    FAILED tests/test_results.py::test_mean_temperature - AssertionError: assert ...
    1 failed, 2 passed in 0.02s
    stopped: exit code 1
    ```

5. Take the edit back. The tests read the files, which are still the
   wrong ones; the summary line comes last, after the failure.

    ```text
    $ git restore run_all.py
    $ python -m pytest -q
    ...
    1 failed, 2 passed in 0.02s
    ```

6. Rebuild. This line comes just above the five checksums:

    ```text
    $ python run_all.py
    ...
    3 passed in 0.01s
    ```

**Check:** `3 passed` again, and `git status` clean.

!!! question "Task: a test for the export"
    Add a test: `data/processed/daily.csv` has 10 lines, and its first
    row is 1 October 2025. Run the one command.

??? success "Answer"
    At the end of `tests/test_results.py`:

    ```python
    def test_daily_export():
        lines = read("data/processed/daily.csv")
        assert len(lines) == 10
        assert lines[1].startswith("2025-10-01,")
    ```

    ```text
    $ python run_all.py
    ...
    4 passed in 0.01s
    ```

    Commit it: `git commit -am "Test the cleaned export"`.

---

## Part 4 · A stranger's laptop { #part-4 }

<!-- 1:25 to 2:00 -->

A stranger has the repository and the README, nothing else. A clone in a second folder and a second environment play the stranger.

---

### 8. The README says one command { #readme }

<!-- 1:25 · 10 min -->

`run_all.py` does what `rebuild.sh` did, so the old script goes.

1. In `README.md`, replace the section `## How to rebuild` (up to the
   next `##`) with this, and save:

    ```text
    ## How to rebuild

    In zsh on macOS or Git Bash on Windows, with Miniforge, in the project folder:

        conda env create -f environment.yml
        conda activate s13
        python run_all.py

    `run_all.py` makes `data/processed` and `results` from `data/raw`, runs the
    tests and prints the checksum of every file it made.
    ```

2. Remove the old script; `git rm` deletes the file and stages the
   deletion.

    ```text
    $ git rm scripts/rebuild.sh
    rm 'scripts/rebuild.sh'
    ```

3. Stage the README, look, commit. `M` is a changed file, `D` a deleted
   one; both are staged (first column).

    ```text
    $ git add README.md
    $ git status --short
    M  README.md
    D  scripts/rebuild.sh
    $ git commit -m "Rebuild with conda and run_all.py"
    [main 3a13222] Rebuild with conda and run_all.py
     2 files changed, 6 insertions(+), 13 deletions(-)
     delete mode 100755 scripts/rebuild.sh
    ```

**Check:** right-click `README.md` > **Open Preview**: **How to rebuild**
shows the three lines.

---

### 9. A fresh clone, a fresh environment { #clone }

<!-- 1:35 · 15 min -->

The stranger follows the README word for word, in a second folder.

1. Go to the home folder and clone today's repository into
   `weather-check`. A clone has only what was committed, as a clone from
   GitHub would.

    ```text
    $ cd ~
    $ git clone weather-s13 weather-check
    Cloning into 'weather-check'...
    done.
    ```

2. Go in and look: no `data/processed`, and no `results` either.

    ```text
    $ cd weather-check
    $ ls data
    raw
    ```

3. A new environment from the file. The name `s13` is taken on this
   laptop, so `-n` gives another one. About 200 packages; most are in
   conda's cache from `s13`, so it takes a minute.

    ```text
    $ conda env create -f environment.yml -n weather-check
    ...
    #     $ conda activate weather-check
    ```

4. Switch it on: the prompt starts with `(weather-check)`.

    ```text
    $ conda activate weather-check
    ```

5. The one command. It ends with:

    ```text
    $ python run_all.py
    ...
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

---

### 10. Record the check { #record }

<!-- 1:50 · 5 min -->

The README says when the check was made and what it found.

1. Back to the project and its environment.

    ```text
    $ cd ~/weather-s13
    $ conda activate s13
    ```

2. In `README.md`, under the line that ends with `every file it made.`,
   add a line and save.

    ```text
    Checked on 2026-12-22 in a fresh clone: the same five checksums.
    ```

3. Commit.

    ```text
    $ git commit -am "Record the check in a fresh clone"
    [main 41cc816] Record the check in a fresh clone
     1 file changed, 2 insertions(+)
    ```

4. Today's history, on top of the folder's first commit.

    ```text
    $ git log --oneline
    41cc816 Record the check in a fresh clone
    3a13222 Rebuild with conda and run_all.py
    3182c7e Test the results at the end of run_all.py
    315a8af Make everything from data/raw with one command
    be0e110 Pin every version in the environment
    7f5c9f6 The starting folder of the seminar
    ```

    Your ids differ, except `7f5c9f6`: that commit came in the zip.

**Check:** six commits, and the check line in the README.

---

### 11. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->

The stranger's environment and folder go; the table holds the lines of today.

1. Remove the stranger's environment; answer `y` to both questions. Then
   remove the stranger's folder.

    ```text
    $ conda env remove -n weather-check
    $ rm -rf ~/weather-check
    ```

| To | Type |
|--|--|
| see the exact version of a package | `conda list pandas` |
| make the environment on any laptop | `conda env create -f environment.yml` |
| run a program from Python | `subprocess.run([sys.executable, "script.py"])` |
| make every file from `data/raw` | `python run_all.py` |
| state a fact in a test | `assert value == pytest.approx(7.16, abs=0.005)` |
| check the numbers | `python -m pytest` |
| did every stage run? | `echo $?` |
| delete what the scripts make | `rm -r data/processed results` |
| remove a file from Git and the folder | `git rm FILE` |

---

## Optional, if the room goes fast { #optional }

---

### 12. A stage of your own: a figure { #figure }

<!-- — · 10 min -->

A file in `results` that no stage makes cannot be rebuilt by a stranger. Every script that writes a result gets a stage the same way.

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

3. Run. It ends with:

    ```text
    $ python run_all.py
    ...
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
    $ git add run_all.py scripts/plot_hill.py
    $ git commit -m "Plot the difference by month as a stage"
    ```

**Check:** six checksums, the figure's the same on every run on this
laptop. A figure can differ from your neighbour's, by the fonts of the
system; the tests check numbers, not pixels.

---

### 13. An option on the command line { #option }

<!-- — · 10 min -->

The 20 hours of `clean_hill.py` become an option with a default, read by `argparse`.

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
    $ python scripts/clean_hill.py --help
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
    $ python scripts/clean_hill.py --min-hours 24
    rows read       8740
    temp missing    27
    rows in F       72
    duplicate rows  24
    days too short  14
    days compared   351
    hill - valley   -1.2
    ```

5. A word where a number belongs: `argparse` refuses it, and `echo $?`
   then prints `2`.

    ```text
    $ python scripts/clean_hill.py --min-hours twenty
    usage: clean_hill.py [-h] [--min-hours MIN_HOURS]
    clean_hill.py: error: argument --min-hours: invalid int value: 'twenty'
    ```

6. Run the one command: `run_all.py` passes no option, so the default 20
   holds and the tests pass. The checksum of `results/hill.txt` changes to
   `b8bc8972e9c6`: one label of its text changed, the numbers did not.

**Check:** 351 days with `--min-hours 24`, 361 without.

---

### 14. Advanced tasks { #advanced }

<!-- — · 20 min -->

Harder questions on the same project, for a room that is done early. Each answer is one way; others are fine.

!!! question "Advanced task: a test for the checksums"
    The tests check four numbers; the checksums cover every byte, but only
    a person compares them. Write the five checksums into `checksums.txt`
    and add a test that recomputes each one. Then change one number in
    `results/hill.txt` that no other test looks at, and run the tests.

??? success "Answer"
    `grep -E` keeps the lines that start with 12 hex digits and a space:

    ```text
    $ python run_all.py | grep -E '^[0-9a-f]{12} ' > checksums.txt
    $ cat checksums.txt
    33fe5e77a979 data/processed/daily.csv
    67106615f8c1 data/processed/hill_daily.csv
    85b1f38d0df9 data/processed/weather_valid.csv
    58c921c33f22 results/hill.txt
    ade2805b90fe results/temp_c.txt
    ```

    `tests/test_checksums.py`:

    ```python
    """The files of the rebuild have the checksums written in checksums.txt."""
    import hashlib


    def test_checksums():
        with open("checksums.txt", encoding="utf-8") as listing:
            for line in listing:
                digest, path = line.split()
                with open(path, "rb") as handle:
                    made = hashlib.sha256(handle.read()).hexdigest()[:12]
                assert made == digest, path
    ```

    With `rows read 8740` changed to `8741` in `results/hill.txt`:

    ```text
    $ python -m pytest -q
    ...
    >               assert made == digest, path
    E               AssertionError: results/hill.txt
    E               assert '0321502665df' == '58c921c33f22'
    ...
    1 failed, 3 passed in 0.02s
    ```

    `python run_all.py` makes the file again and the four tests pass.
    Commit `checksums.txt` with the test: a stranger's run then checks the
    bytes too. A change made on purpose (a new stage, a new label) needs a
    new `checksums.txt` in the same commit.

!!! question "Advanced task: how long does each stage take?"
    Make `run_all.py` print the seconds of each stage under its output.
    Which stage is the slowest, and why?

??? success "Answer"
    `time.perf_counter()` reads a clock; the difference of two readings is
    seconds. In `run_all.py`, `import time` at the top, and in the loop:

    ```python
        start = time.perf_counter()
        done = subprocess.run([sys.executable] + words,
                              capture_output=True, text=True)
        seconds = time.perf_counter() - start
        print(done.stdout + done.stderr, end="")
        print(f"   {seconds:.2f} s")
    ```

    ```text
    $ python run_all.py | grep -E "^==| s$"
    == scripts/drop_missing.py
       0.04 s
    == scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
       0.02 s
    == scripts/column_stats.py data/processed/weather_valid.csv temp_c
       0.10 s
    == scripts/clean_hill.py
       0.33 s
    == -m pytest -q
       0.17 s
    ```

    Your times differ. `clean_hill.py` is the slowest: it starts pandas,
    which takes most of the third of a second, and reads two files. The
    whole rebuild takes under a second; a project with many slow stages
    would skip a stage whose inputs did not change, which is what tools
    such as `make` and Snakemake do.

!!! question "Advanced task: one test, four numbers"
    `test_mean_temperature` checks two lines of `results/temp_c.txt`.
    Write one test that checks `rows`, `min`, `max` and `mean`, and that
    pytest reports as four tests. Look up `pytest.mark.parametrize`.

??? success "Answer"
    `tests/test_stats.py`:

    ```python
    """The statistics of temp_c, one test per number: python -m pytest -v"""
    import pytest


    @pytest.mark.parametrize("name, value", [
        ("rows", "87552"),
        ("min", "-16.3"),
        ("max", "32.4"),
        ("mean", "7.15997"),
    ])
    def test_temp_c(name, value):
        with open("results/temp_c.txt", encoding="utf-8") as handle:
            stats = dict(line.rsplit(maxsplit=1) for line in handle.read().splitlines())
        assert stats[name] == value
    ```

    ```text
    $ python -m pytest -v tests/test_stats.py
    ...
    tests/test_stats.py::test_temp_c[rows-87552] PASSED                      [ 25%]
    tests/test_stats.py::test_temp_c[min--16.3] PASSED                       [ 50%]
    tests/test_stats.py::test_temp_c[max-32.4] PASSED                        [ 75%]
    tests/test_stats.py::test_temp_c[mean-7.15997] PASSED                    [100%]

    ============================== 4 passed in 0.01s ===============================
    ```

    The function runs once per pair; a failure names the pair, for
    example `test_temp_c[min--16.3]`.

---

## Aims practised

- ♻️ **Reproducibility:** a fresh clone and a fresh environment give the
  same five checksums; the tests say which number broke and where.
- ⚙️ **Automation:** one command makes every file from `data/raw`, stops
  at the first stage that fails, and checks the numbers.
- 🔧 **Tool-agnostic:** the same `python run_all.py` and the same bytes on
  macOS and Windows; `environment.yml` names versions, not a laptop.
