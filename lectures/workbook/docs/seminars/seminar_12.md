# Seminar 12 · pytest

**Paired lecture:** 12 Code That Lasts · **Format:** type-along tutorial, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** Will the result come out the same next year, on another laptop?

**Today's goal:** every student adds pytest to the environment `analysis`
and writes it down, writes three tests for `weather.py` and for the mean
7.16, makes `scripts/rebuild.sh` run them as its last line, pins the exact
versions, deletes the results and makes them again, and rebuilds a fresh
clone of the folder: the same checksums.

Everything is typed in VS Code: the test file in the editor, the commands in
its terminal (zsh on macOS, Git Bash on Windows; the lines are the same in
both, except the checksum command). In the blocks, a line that starts with
`$` is typed in the terminal, a line that starts with `>>>` is typed at
Python's prompt, and every other line is what comes back; `...` stands for
lines left out.

**If time runs short:** skip the Tasks, but keep sections 9 and 10, the
delete and the fresh clone; sections 13 to 15 are optional.

??? info "Before the session"
    - **Room:** Miniforge, VS Code with its Python extension, and Git with a
      name and an e-mail on every laptop (the [Setup](../setup.md) page);
      internet for the download (1.1 MB) and for pytest (8 packages,
      1.4 MB). Nothing from earlier seminars is needed: a laptop without the
      environment `analysis` makes it from today's folder.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` (Miniforge): [Setup, steps 2–4](../setup.md#shell); your name
      for Git: [Setup, step 6](../setup.md#github).
    - **You:** nothing to prepare. Today's folder is a Git repository with
      one commit, the same on every laptop; the ids of commits made today
      differ on every laptop, the checksums do not.
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.

---

## Part 1 · pytest in the environment { #part-1 }

<!-- 0:00 to 0:20 -->

**pytest** runs tests: small functions that check a number. It goes into the environment, and into the file that lists it.

Further reading: [pytest, Get started](https://docs.pytest.org/en/stable/getting-started.html).

---

### 1. Get today's folder { #start }

<!-- 0:00 · 10 min -->

Today's folder holds the data, the module `weather.py`, the rebuild script and `environment.yml`.

1. On the [Releases page](https://github.com/MindaugasSarpis/weather-project/releases),
   under **Assets**, click `weather-s12.zip`. Open VS Code, then the
   terminal (**View** > **Terminal**), and unzip it into the home folder.

    ```text
    $ unzip ~/Downloads/weather-s12.zip -d ~
    Archive:  /Users/smilte/Downloads/weather-s12.zip
       creating: /Users/smilte/weather-s12/
    ...
      inflating: /Users/smilte/weather-s12/scripts/weather.py
    $ cd ~/weather-s12
    $ ls
    README.md  data  environment.yml  results  scripts
    ```

    Safari unpacks a zip by itself: then `mv ~/Downloads/weather-s12 ~`
    instead.

2. **File** > **Open Folder...** > `weather-s12` > **Open**. The window
   reloads: open the terminal again (**View** > **Terminal**); it starts in
   the folder.
3. The folder is a Git repository with one commit, and nothing changed.

    ```text
    $ git log --oneline
    618d3f0 The starting folder of the seminar
    $ git status
    On branch main
    nothing to commit, working tree clean
    ```

4. The environment of weeks 8 to 12 is `analysis`. Switch it on: the
   prompt starts with `(analysis)`.

    ```text
    $ conda activate analysis
    ```

    `EnvironmentNameNotFound: Could not find conda environment: analysis`:
    this laptop does not have it yet. Make it from the folder's list (a
    few minutes), then switch it on.

    ```text
    $ conda env create -f environment.yml
    ...
    #     $ conda activate analysis
    $ conda activate analysis
    ```

5. VS Code too: `Ctrl+Shift+P` (macOS `Cmd+Shift+P`), `Python: Select
   Interpreter`, pick the entry with `envs/analysis` in its path. The
   Status Bar shows `analysis`.

**Check:** `(analysis)` at the start of the prompt, `618d3f0` in the log.

---

### 2. Install pytest, write it down { #install }

<!-- 0:10 · 10 min -->

A new package goes into the active environment and into `environment.yml`, or the next laptop cannot run the tests.

1. pytest is not there yet. `python -m pytest` runs pytest as a module of
   this Python, so the answer names that Python.

    ```text
    $ python -m pytest --version
    /Users/smilte/miniforge3/envs/analysis/bin/python: No module named pytest
    ```

2. Install it, with its version.

    ```text
    $ conda install pytest=9.2
    ...
      added / updated specs:
        - pytest=9.2
    ...
    The following NEW packages will be INSTALLED:

      colorama           conda-forge/noarch::colorama-0.4.6-pyhd8ed1ab_1
      exceptiongroup     conda-forge/noarch::exceptiongroup-1.3.1-pyhd8ed1ab_0
      iniconfig          conda-forge/noarch::iniconfig-2.3.1-pyhd8ed1ab_0
      pluggy             conda-forge/noarch::pluggy-1.7.0-pyh5ded981_0
      pygments           conda-forge/noarch::pygments-2.21.0-pyhcf101f3_0
      pytest             conda-forge/noarch::pytest-9.2.0-pyhc364b38_1
      tomli              conda-forge/noarch::tomli-2.5.0-pyh5ded981_0
      typing_extensions  conda-forge/noarch::typing_extensions-4.16.0-pyhcf101f3_0

    Proceed ([y]/n)?
    ```

    Eight packages: pytest and the seven it needs, 1.4 MB.

3. At `Proceed ([y]/n)?` press `Enter`. Then ask for the version.

    ```text
    $ python -m pytest --version
    pytest 9.2.0
    ```

4. Export the list again.

    ```text
    $ conda env export --from-history -f environment.yml
    ```

5. Open `environment.yml`, delete its last line, `prefix: ...` (a folder on
   this laptop), save: pytest is the new last line.

    ```text
    name: analysis
    channels:
      - conda-forge
    dependencies:
      - pandas=3.1
      - matplotlib-base=3.11
      - python=3.14
      - pytest=9.2
    ```

    The order of the first three lines differs from laptop to laptop, and
    a package you added in an earlier week is listed too.

**Check:** `pytest 9.2.0`, and `- pytest=9.2` at the end of
`environment.yml`.

!!! warning "`No module named pytest` after the install"
    The prompt says `(base)`: `conda activate analysis`, then again.

---

## Part 2 · Tests of `weather.py` { #part-2 }

<!-- 0:20 to 0:50 -->

A test states a fact known without the code: worked out by hand, or counted in the data's description.

---

### 3. A fact, stated with `assert` { #assert }

<!-- 0:20 · 10 min -->

`assert` and a statement: nothing happens when the statement is true; Python stops with `AssertionError` when it is false.

1. Python finds `weather.py` in the terminal's folder, so start it in
   `scripts`. One line of the log, the evening of 21 July 2019, into
   `temp_of`:

    ```pycon
    $ cd scripts
    $ python
    >>> import weather
    >>> weather.temp_of("2019-07-21T20:00,27.3,63,4.5")
    27.3
    ```

2. The same as two statements. The true one prints nothing; the false one
   stops.

    ```pycon
    >>> assert weather.temp_of("2019-07-21T20:00,27.3,63,4.5") == 27.3
    >>> assert weather.temp_of("2019-07-21T20:00,27.3,63,4.5") == 25.6
    Traceback (most recent call last):
      ...
    AssertionError
    ```

3. The four measured hours of that evening: by hand, (27.3 + 25.6 + 24.6
   + 23.6) / 4 = 101.1 / 4 = 25.275. And `mean`:

    ```pycon
    >>> weather.mean([27.3, 25.6, 24.6, 23.6])
    25.275000000000002
    >>> exit()
    $ cd ..
    ```

    The tail of digits is a float's binary rounding, as in `0.1 + 0.2`.

**Check:** `AssertionError` for 25.6, `25.275000000000002` for the mean,
and the terminal back in `weather-s12` (`cd ..`).

---

### 4. A test file, run by pytest { #test-file }

<!-- 0:30 · 10 min -->

pytest runs every function whose name starts with `test_`, in files whose names start with `test_`.

1. In the Explorer, right-click `scripts` > **New File...**, type
   `test_weather.py`, press `Enter`. It stands beside `weather.py`, so
   `import weather` finds the module. Type, save:

    ```python
    import weather


    def test_temp_of():
        assert weather.temp_of("2019-07-21T20:00,27.3,63,4.5") == 27.3


    def test_mean_of_four_hours():
        assert weather.mean([27.3, 25.6, 24.6, 23.6]) == 25.275
    ```

2. Run pytest from the project folder. It finds the file, runs both
   functions, and prints one character per test: `.` passed, `F` failed.

    ```text
    $ python -m pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.14.10, pytest-9.2.0, pluggy-1.7.0
    rootdir: /Users/smilte/weather-s12
    collected 2 items

    scripts/test_weather.py .F                                               [100%]
    ...
    ========================= 1 failed, 1 passed in 0.02s ==========================
    ```

    On Windows the second line says `platform win32`.

**Check:** `.F` and `1 failed, 1 passed`.

---

### 5. Read the failure, compare within a tolerance { #tolerance }

<!-- 0:40 · 10 min (Task: 5 min, skip if late) -->

A failure names the test, the line and the values; a computed float is compared within a tolerance, never exactly.

1. The lines in the middle of the output, which `...` cut above:

    ```text
    ___________________________ test_mean_of_four_hours ____________________________

        def test_mean_of_four_hours():
    >       assert weather.mean([27.3, 25.6, 24.6, 23.6]) == 25.275
    E       assert 25.275000000000002 == 25.275
    ...
    scripts/test_weather.py:9: AssertionError
    ```

    Which test: its name, between the underscores. Which line: the one
    marked `>`, line 9. Which values: the line marked `E`, the mean on the
    left, the number of the test on the right.

2. `mean` is right; the test asks for more digits than a float keeps.
   Allow a tiny difference: `abs` is the distance without its sign, and
   `1e-9` is 0.000000001. Change the second test, save:

    ```python
    def test_mean_of_four_hours():
        m = weather.mean([27.3, 25.6, 24.6, 23.6])
        assert abs(m - 25.275) < 1e-9
    ```

3. Run again.

    ```text
    $ python -m pytest
    ...
    scripts/test_weather.py ..                                               [100%]

    ============================== 2 passed in 0.01s ===============================
    ```

**Check:** `2 passed`.

!!! question "Task: see the test catch a mistake"
    In `weather.py`, change the last line of `mean` to
    `return sum(values) / (len(values) - 1)`, save, run pytest. Which value
    does the failure show? Then put the line back.

??? success "Answer"
    ```text
    $ python -m pytest
    ...
    >       assert abs(m - 25.275) < 1e-9
    E       assert 8.425000000000004 < 1e-09
    E        +  where 8.425000000000004 = abs((33.7 - 25.275))
    ...
    ========================= 1 failed, 1 passed in 0.02s ==========================
    ```

    The broken `mean` gives 101.1 / 3 = 33.7, 8.425 away from 25.275. A
    test that has been seen to fail checks something. With the line put
    back: `2 passed`.

---

## Part 3 · One command that rebuilds and tests { #part-3 }

<!-- 0:50 to 1:16 -->

`scripts/rebuild.sh` makes `data/processed` and `results` from `data/raw`. Today its last line runs the tests.

---

### 6. A test of the result { #result }

<!-- 0:50 · 10 min -->

The second kind of test reads what the rebuild wrote: 87 552 rows, from the README's 87 672 hours less 120 marked `-999`, and the mean 7.16.

1. Run the rebuild as it is, then read the file it wrote.

    ```text
    $ ./scripts/rebuild.sh
    9 rows written to data/processed/daily.csv
    $ cat results/temp_c.txt
    file    data/processed/weather_valid.csv
    column  temp_c
    rows    87552
    min     -16.3
    max     32.4
    mean    7.15997
    ```

2. At the end of `scripts/test_weather.py`, a third test, save. The loop
   puts each line's two words into a dict: `stats["rows"]` is `"87552"`;
   the README says 7.16, so half of its last digit, 0.005, is the
   tolerance.

    ```python


    def test_mean_temperature():
        stats = {}
        for line in open("results/temp_c.txt").read().splitlines():
            parts = line.split()
            stats[parts[0]] = parts[1]
        assert stats["rows"] == "87552"
        assert abs(float(stats["mean"]) - 7.16) < 0.005
    ```

3. Run the tests.

    ```text
    $ python -m pytest
    ...
    scripts/test_weather.py ...                                              [100%]

    ============================== 3 passed in 0.01s ===============================
    ```

**Check:** `3 passed`.

---

### 7. The tests as the last line of `rebuild.sh` { #last-line }

<!-- 1:00 · 8 min -->

The tests read what the lines above them wrote, so they come last.

1. Open `scripts/rebuild.sh`, add one line at its end, save:

    ```text
    python -m pytest -q
    ```

    `-q` is the short output: one line of dots and the summary.

2. The one command now makes every file, then checks it. `echo $?` prints
   its exit status: 0 when every line worked.

    ```text
    $ ./scripts/rebuild.sh
    9 rows written to data/processed/daily.csv
    ...                                                                      [100%]
    3 passed in 0.00s
    $ echo $?
    0
    ```

3. Commit the three changed files. `??` is a file Git does not know yet.

    ```text
    $ git status --short
     M environment.yml
     M scripts/rebuild.sh
    ?? scripts/test_weather.py
    $ git add environment.yml scripts/rebuild.sh scripts/test_weather.py
    $ git commit -m "Test the module and the mean at the end of rebuild.sh"
    [main 08cade2] Test the module and the mean at the end of rebuild.sh
     3 files changed, 23 insertions(+), 2 deletions(-)
     create mode 100644 scripts/test_weather.py
    ```

    Your id differs, and so may the count of insertions and deletions.

**Check:** `3 passed`, `0`, and the commit.

---

### 8. A wrong mean stops the rebuild { #wrong }

<!-- 1:08 · 8 min -->

Tomas's change of Seminar 6 again: the mean taken from the raw file, `-999` rows and all.

1. In `scripts/rebuild.sh`, on the `column_stats.py` line, change
   `data/processed/weather_valid.csv` to `data/raw/weather.csv`. Save, run.

    ```text
    $ ./scripts/rebuild.sh
    9 rows written to data/processed/daily.csv
    ..F                                                                      [100%]
    ...
    >       assert stats["rows"] == "87552"
    E       AssertionError: assert '87672' == '87552'
    ...
    1 failed, 2 passed in 0.01s
    $ echo $?
    1
    ```

2. The file holds the wrong mean, and the rebuild says it failed.

    ```text
    $ tail -n 1 results/temp_c.txt
    mean    5.7828
    ```

3. Take the change back with Git, and rebuild.

    ```text
    $ git restore scripts/rebuild.sh
    $ ./scripts/rebuild.sh
    9 rows written to data/processed/daily.csv
    ...                                                                      [100%]
    3 passed in 0.00s
    ```

**Check:** `1 failed` and `1` with the change, `3 passed` after the
restore.

---

## Part 4 · The same result in a fresh folder { #part-4 }

<!-- 1:16 to 1:43 -->

Exact versions in the file, then the proof: the results deleted and made again, and a fresh clone that has only what was committed.

---

### 9. Pin the versions, delete, rebuild { #pin }

<!-- 1:16 · 12 min -->

`pandas=3.1` means any 3.1.x on the day of the install; `pandas=3.1.1` means the same on every day.

1. The exact versions of the four packages the file names. `"^(...)$"`
   means exactly one of these names.

    ```text
    $ conda list "^(python|matplotlib-base|pandas|pytest)$"
    # packages in environment at /Users/smilte/miniforge3/envs/analysis:
    #
    # Name                     Version          Build               Channel
    matplotlib-base            3.11.2           py314heb334b3_1     conda-forge
    pandas                     3.1.1            np2py314h78ec565_0  conda-forge
    pytest                     9.2.0            pyhc364b38_1        conda-forge
    python                     3.14.10          h0ae1c2c_100_cp314  conda-forge
    ```

    The **Build** column differs between macOS and Windows, and your last
    digits may be higher: write yours.

2. In `environment.yml`, give each line its full version, save. Commit.

    ```text
    name: analysis
    channels:
      - conda-forge
    dependencies:
      - python=3.14.10
      - matplotlib-base=3.11.2
      - pandas=3.1.1
      - pytest=9.2.0
    ```

    ```text
    $ git commit -am "Pin the exact versions"
    [main e1c56e7] Pin the exact versions
     1 file changed, 4 insertions(+), 4 deletions(-)
    ```

3. The checksums of the three files the rebuild makes.

    === "macOS"

        ```text
        $ shasum -a 256 data/processed/*.csv results/temp_c.txt
        33fe5e77a97900b6e8f94776f266da4d6e3c96590088d21bc9842987f705483d  data/processed/daily.csv
        85b1f38d0df905a9232078d97c6bb21455e87239ea8754faceda0d868b564881  data/processed/weather_valid.csv
        ade2805b90fe64a0053fa65e28329eee616ad0389f9ca55db86400b1c7a9a18b  results/temp_c.txt
        ```

    === "Windows"

        ```text
        $ sha256sum data/processed/*.csv results/temp_c.txt
        33fe5e77a97900b6e8f94776f266da4d6e3c96590088d21bc9842987f705483d  data/processed/daily.csv
        85b1f38d0df905a9232078d97c6bb21455e87239ea8754faceda0d868b564881  data/processed/weather_valid.csv
        1dadaacc2e6f6666fb53d1c6e0c89084fd495e8d064e6d3cafbf194ee72a5382  results/temp_c.txt
        ```

    `temp_c.txt` differs: Python on Windows ends each of its 6 lines with
    CRLF, 119 bytes instead of 113. The test reads the numbers, which are
    the same.

4. Delete both folders of results, rebuild, and take the checksums again
   (`shasum -a 256` on macOS).

    ```text
    $ rm -r data/processed results
    $ ls data
    raw
    $ ./scripts/rebuild.sh
    9 rows written to data/processed/daily.csv
    ...                                                                      [100%]
    3 passed in 0.00s
    $ sha256sum data/processed/*.csv results/temp_c.txt
    33fe5e77a97900b6e8f94776f266da4d6e3c96590088d21bc9842987f705483d  data/processed/daily.csv
    85b1f38d0df905a9232078d97c6bb21455e87239ea8754faceda0d868b564881  data/processed/weather_valid.csv
    ...
    ```

**Check:** the same three checksums before and after the delete.

---

### 10. A fresh clone, rebuilt { #clone }

<!-- 1:28 · 15 min -->

A stranger gets the repository and its README, nothing else. A clone into a second folder is that stranger, on this laptop.

1. In `README.md`, replace everything from `## How to rebuild` to the end
   of the file with this, save:

    ```text
    ## How to rebuild

    In the project folder, in zsh on macOS or Git Bash on Windows, with
    Miniforge:

        conda env create -f environment.yml
        conda activate analysis
        ./scripts/rebuild.sh

    It makes `data/processed` and `results` from `data/raw`, then runs the
    tests: `3 passed`.
    ```

2. Commit it. Git now holds everything the stranger needs.

    ```text
    $ git commit -am "How to rebuild: the environment, then one command"
    [main 6439d91] How to rebuild: the environment, then one command
     1 file changed, 6 insertions(+), 5 deletions(-)
    ```

3. Clone the folder into `weather-check`, next to it in the home folder.
   A clone has only what was committed: no `data/processed`, no `results`.

    ```text
    $ cd ~
    $ git clone weather-s12 weather-check
    Cloning into 'weather-check'...
    done.
    $ cd weather-check
    $ ls
    README.md  data  environment.yml  scripts
    $ ls data
    raw
    ```

4. The one command, then the checksums (`shasum -a 256` on macOS).

    ```text
    $ ./scripts/rebuild.sh
    9 rows written to data/processed/daily.csv
    ...                                                                      [100%]
    3 passed in 0.01s
    $ sha256sum data/processed/*.csv results/temp_c.txt
    33fe5e77a97900b6e8f94776f266da4d6e3c96590088d21bc9842987f705483d  data/processed/daily.csv
    85b1f38d0df905a9232078d97c6bb21455e87239ea8754faceda0d868b564881  data/processed/weather_valid.csv
    ...
    ```

5. Back to the project.

    ```text
    $ cd ~/weather-s12
    ```

**Check:** `3 passed` in `weather-check`, and the same three checksums as
in section 9.

!!! question "Task: a file left out"
    In `weather-check`, what would `./scripts/rebuild.sh` print if
    `scripts/test_weather.py` had never been committed? Think first, then
    look.

??? success "Answer"
    The clone would have no test file, and pytest finds no test:

    ```text
    $ ./scripts/rebuild.sh
    9 rows written to data/processed/daily.csv

    no tests ran in 0.00s
    $ echo $?
    5
    ```

    pytest's exit status 5 means "no tests collected", and `set -e` stops
    the rebuild. On the author's laptop it said `3 passed`: only a fresh
    clone shows what was never committed.

---

## Part 5 · Your project { #part-5 }

<!-- 1:43 to 2:00 -->

The same steps on your own project. Skip this part if your project has no data yet.

---

### 11. Tests and one command for your project { #project }

<!-- 1:43 · 15 min -->

One fact about your data, known without your code, checked on every rebuild.

1. **File** > **Open Folder...** > your project's folder. In its terminal,
   switch on its environment (`conda activate analysis`, or your project's
   own) and install pytest there if `python -m pytest --version` does not
   find it (section 2).
2. One fact known without the code: the number of data rows of your raw
   file, from its source, or counted with `wc -l` (minus the header line).
   Make `scripts/test_project.py` with your file name and your number:

    ```python
    def test_rows():
        lines = open("data/raw/YOUR_FILE.csv").read().splitlines()
        assert len(lines) - 1 == 1234
    ```

3. `python -m pytest` in the project folder: `1 passed`. Change the
   number once, see it fail, put it back.
4. `python -m pytest -q` as the last line of your `scripts/rebuild.sh`. If
   the project has no rebuild script yet, make one with the lines that make
   your results, and the tests last:

    ```bash
    #!/usr/bin/env bash
    set -e
    python scripts/YOUR_SCRIPT.py
    python -m pytest -q
    ```

    On macOS, once: `chmod +x scripts/rebuild.sh`.

5. Exact versions in your `environment.yml` (section 9), then commit. If
   the project is on GitHub, `git push`, and clone it from there into a
   second folder: `git clone https://github.com/YOUR_NAME/YOUR_PROJECT
   project-check`. Rebuild in the clone.

**Check:** `passed` in your project, and a fresh clone that rebuilds it.

---

### 12. Wrap up { #wrap-up }

<!-- 1:58 · 2 min -->

The lines of today, by what they do.

| To | Type |
|--|--|
| add a package, and write it down | `conda install pytest=9.2`, `conda env export --from-history -f environment.yml`, delete `prefix:` |
| state a fact | `assert value == 27.3`; a float: `assert abs(m - 25.275) < 1e-9` |
| run every test | `python -m pytest` (`-q` for the short form) |
| rebuild and test | `./scripts/rebuild.sh`, its last line `python -m pytest -q` |
| did every line work? | `echo $?`: 0 |
| the exact versions | `conda list "^(python|pandas)$"` |
| the bytes of a file | `shasum -a 256 FILE` (macOS), `sha256sum FILE` (Windows) |
| what a stranger gets | `git clone weather-s12 weather-check` |

---

## Optional, if the room goes fast { #optional }

---

### 13. A fresh environment from the pinned file { #fresh-env }

<!-- — · 10 min -->

The clone was a fresh folder; an environment made from `environment.yml` alone is a fresh laptop.

1. In `weather-check`, make an environment `check` from the pinned file,
   switch it on, and rebuild.

    ```text
    $ cd ~/weather-check
    $ conda env create -n check -f environment.yml
    ...
    $ conda activate check
    $ ./scripts/rebuild.sh
    9 rows written to data/processed/daily.csv
    ...                                                                      [100%]
    3 passed in 0.00s
    ```

    `-n check` gives it another name; `analysis` is taken on this laptop.
    Most packages come from conda's cache, so it takes seconds.

2. Remove it again, and go back. Press `Enter` at the first question,
   `y` and `Enter` at the second.

    ```text
    $ conda activate analysis
    $ conda env remove -n check
    ...
    Proceed ([y]/n)?
    ...
    Everything found within the environment (/Users/smilte/miniforge3/envs/check), including any conda environment configurations and any non-conda files, will be deleted. Do you wish to continue?
     (y/[n])? y
    $ cd ~/weather-s12
    ```

**Check:** `3 passed` in an environment that only the file made.

!!! question "Task: a package never written down"
    What would the rebuild print in `check` if `environment.yml` had no
    line `- pytest=9.2.0`?

??? success "Answer"
    The environment would lack pytest, and the last line of the rebuild
    stops:

    ```text
    $ ./scripts/rebuild.sh
    9 rows written to data/processed/daily.csv
    /Users/smilte/miniforge3/envs/check/bin/python: No module named pytest
    $ echo $?
    1
    ```

    On the laptop where pytest was installed by hand, everything runs; only
    an environment made from the file alone shows what the file forgot.

---

### 14. Ben's way, with its test { #midrange }

<!-- — · 10 min -->

Lecture 1's Ben took each day's midrange, halfway between its lowest and highest hour. One more function, tested on the four hours like `mean`.

1. At the end of `scripts/weather.py`, add, save:

    ```python
    def midrange(values):
        return (min(values) + max(values)) / 2
    ```

2. By hand: (23.6 + 27.3) / 2 = 25.45. At the end of
   `scripts/test_weather.py`, add, save, run the one command:

    ```python


    def test_midrange_of_four_hours():
        m = weather.midrange([27.3, 25.6, 24.6, 23.6])
        assert abs(m - 25.45) < 1e-9
    ```

    ```text
    $ ./scripts/rebuild.sh
    9 rows written to data/processed/daily.csv
    ....                                                                     [100%]
    4 passed in 0.01s
    ```

**Check:** `4 passed`.

---

### 15. Advanced tasks { #advanced }

<!-- — · 20 min -->

Harder checks on the same project, for a room that is done early. Each answer is one way; others are fine.

!!! question "Advanced task: a test for the export"
    Add a test: `data/processed/daily.csv` has 10 lines, and its first row
    is 1 October 2025.

??? success "Answer"
    ```python
    def test_daily_export():
        lines = open("data/processed/daily.csv").read().splitlines()
        assert len(lines) == 10
        assert lines[1].startswith("2025-10-01,")
    ```

    `./scripts/rebuild.sh` then ends with `4 passed` (5 with section 14).

!!! question "Advanced task: the raw file is the file received"
    The SHA-256 of `data/raw/weather.csv`, as it was received, starts with
    `3f1ad06d` (Lecture 4). Write a test that computes it with Python's
    `hashlib` and compares.

??? success "Answer"
    ```python
    import hashlib


    def test_raw_file_unchanged():
        data = open("data/raw/weather.csv", "rb").read()
        digest = hashlib.sha256(data).hexdigest()
        assert digest.startswith("3f1ad06d")
    ```

    `"rb"` reads the bytes as they are, without turning them into text. An
    edit of one value in the raw file now stops the rebuild.

!!! question "Advanced task: pytest's own tolerance"
    pytest has a short form for "equal within a tolerance":
    `assert m == pytest.approx(25.275)`, with `import pytest` at the top
    of the file. Use it in `test_mean_of_four_hours`. How close must `m`
    be?

??? success "Answer"
    ```python
    import pytest

    import weather


    def test_mean_of_four_hours():
        m = weather.mean([27.3, 25.6, 24.6, 23.6])
        assert m == pytest.approx(25.275)
    ```

    `pytest.approx` accepts a difference of one part in a million of the
    expected value: 25.275 × 10⁻⁶, about 0.000025. `pytest.approx(7.16,
    abs=0.005)` sets the tolerance by hand.

---

## Aims practised

- ♻️ **Reproducibility:** pinned versions, and a fresh clone that gives the
  same checksums; the tests say which number broke and where.
- ⚙️ **Automation:** one command makes every file from `data/raw` and then
  checks it; its exit status says whether the result can be trusted.
- 🔧 **Tool-agnostic:** the same `./scripts/rebuild.sh` on macOS and
  Windows; `environment.yml` names versions, not a laptop.
