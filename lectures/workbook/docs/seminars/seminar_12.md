# Seminar 12 · pytest

**Paired lecture:** 12 Code That Lasts · **Format:** a showcase, then a problem, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** Can you trust a function an LLM wrote, and will its result come out the same next year, on another laptop?

The lecturer runs Part 2 from this page; in Part 3 the room works in pairs.
Everything is typed in VS Code: the files in the editor, the commands in its
terminal (zsh on macOS, Git Bash on Windows; the same lines in both). A line
that starts with `$` is typed without the `$`; `...` stands for lines left out.

**If time runs short:** leave out section 5 (the station file's flags); Part 3 downloads the file itself.

??? info "Before the session"
    - **Room:** Miniforge and VS Code with its Python extension on every
      laptop (the [Setup](../setup.md) page), Git for the optional section;
      internet for pytest (8 packages, 1.4 MB), for the data and for a chat
      LLM. A laptop without `analysis` makes it in section 1 (Python,
      pandas, Matplotlib and pytest, about 100 MB on a Mac and 220 MB on
      Windows).
    - **No file is handed out.** Section 5 and Part 3 download one public
      file once, with `curl`: the daily record of the Vilnius weather
      station, `LH000026730.csv` (6.1 MB, 1 January 1881 to 24 August
      2025), from NOAA NCEI's GHCN-Daily.
    - **Terms:** GHCN-Daily, NOAA NCEI, "for free and unrestricted use in
      research, education, and other non-commercial activities" (WMO
      Resolution 40); cite Menne et al. 2012, *Global Historical
      Climatology Network - Daily (GHCN-Daily)*, Version 3.35, NOAA NCDC,
      [doi:10.7289/V5D21VHZ](https://doi.org/10.7289/V5D21VHZ), accessed
      10 November 2026.
    - **The numbers** on this page come from runs on 10 November 2026. If
      NCEI adds days after 24 August 2025 to the file, the lines about 2025
      and later change; no earlier year does.
    - **A chat LLM:** Part 3 asks one for a function: any chat LLM in the
      browser on a free account. The page shows no reply of a chat: replies
      differ from chat to chat. A pair without one asks a neighbour's, or
      writes the function from the hints.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` (Miniforge): [Setup, steps 2–4](../setup.md#shell); your
      name for Git: [Setup, step 6](../setup.md#github).
    - **The conda lines** are shown as on a Mac (`/Users/smilte/...`); Git
      Bash shows `/c/Users/smilte/...`, and the Build column of `conda list`
      differs between systems.

---

## Part 1 · Set up { #part-1 }

### 1. A new folder, the environment `analysis` with pytest { #start }

<!-- 0:00 · 8 min -->

pytest runs tests: small functions that check a result against a fact known without the code. It goes into `analysis`, the environment of weeks 8 to 12.

1. In VS Code, **View** > **Terminal**. Make the folder and go into it.

    ```text
    $ mkdir ~/weather-s12
    $ cd ~/weather-s12
    ```

2. **File** > **Open Folder...** > `weather-s12` (in your home folder) >
   **Open**, then **View** > **Terminal**. The Explorer on the left is empty.

3. Switch on `analysis` and add pytest. At `Proceed ([y]/n)?` press `Enter`.

    ```text
    $ conda activate analysis
    $ conda install pytest=9.2
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

    pytest and the seven packages it needs. `EnvironmentNameNotFound`
    after the first line: this laptop has no `analysis` yet. Make it with
    pytest in one line, then switch it on.

    ```text
    $ conda create -n analysis python=3.14 pandas=3.1 matplotlib-base=3.11 pytest=9.2
    ...
    $ conda activate analysis
    ```

4. Ask for pytest's version. `python -m pytest` runs pytest with this
   Python.

    ```text
    $ python -m pytest --version
    pytest 9.2.0
    ```

5. Tell VS Code which Python to use: `Ctrl+Shift+P` (macOS `Cmd+Shift+P`),
   `Python: Select Interpreter`, pick the entry with `envs/analysis` in its
   path.

**Check:** `(analysis)` at the start of the prompt, and `pytest 9.2.0`.

---

### 2. Pin the exact versions in `environment.yml` { #pin }

<!-- 0:08 · 7 min -->

`pytest=9.2` lets in any 9.2.x on the day of the install; `pytest=9.2.0` means the same version on every day.

1. Write the environment into a file. Click `environment.yml` in the
   Explorer, delete its last line, `prefix: ...`, save (`Ctrl+S`, macOS
   `Cmd+S`). The new package is the last line; the others may stand in
   another order, and a package of an earlier week stands there too.

    ```text
    $ conda env export --from-history -f environment.yml
    ```

    ```text
    name: analysis
    channels:
      - conda-forge
    dependencies:
      - python=3.14
      - pandas=3.1
      - matplotlib-base=3.11
      - pytest=9.2
    ```

2. Ask conda for the exact versions of the four. `"^(...)$"` means exactly
   one of these names.

    ```text
    $ conda list "^(python|pandas|matplotlib-base|pytest)$"
    # packages in environment at /Users/smilte/miniforge3/envs/analysis:
    #
    # Name                     Version          Build               Channel
    matplotlib-base            3.11.2           py314heb334b3_1     conda-forge
    pandas                     3.1.1            np2py314h78ec565_0  conda-forge
    pytest                     9.2.0            pyhc364b38_1        conda-forge
    python                     3.14.10          h0ae1c2c_100_cp314  conda-forge
    ```

3. Give each line of `environment.yml` its full version (yours may be
   higher in the last digit), save.

    ```text
    name: analysis
    channels:
      - conda-forge
    dependencies:
      - python=3.14.10
      - pandas=3.1.1
      - matplotlib-base=3.11.2
      - pytest=9.2.0
    ```

**Check:** every package in `environment.yml` with three numbers; a package of an earlier week gets its version from `conda list` the same way.

---

## Part 2 · Showcase { #part-2 }

The lecturer runs three test files and makes the environment again from
`environment.yml`; the room watches or types along. For each file: in the
Explorer, right-click > **New File...**, the name above the code, paste,
save, run the line under it in the terminal. pytest prints one character per
test: `.` passed, `F` failed; then each failure with its line and values.
Your times differ.

### 3. A test with an answer known by hand, and one that fails for the wrong reason { #known }

<!-- 0:15 · 9 min -->

A test states a fact known without the code and checks the code against it; pytest runs every function named `test_...` in the files named `test_....py`.

```python title="test_mean.py"
import pytest


def mean_valid(values):
    """The mean of the values that are not None."""
    present = [v for v in values if v is not None]
    return sum(present) / len(present)


# 21 July 2019, 20:00 to 01:00: four hours measured, then the sensor failed
EVENING = [27.3, 25.6, 24.6, 23.6, None, None]


def test_mean_exact():
    assert mean_valid(EVENING) == 25.275          # 101.1 / 4, by hand


def test_mean_within_tolerance():
    assert mean_valid(EVENING) == pytest.approx(25.275)
```

```text
$ python -m pytest -q test_mean.py
F.                                                                       [100%]
=================================== FAILURES ===================================
_______________________________ test_mean_exact ________________________________

    def test_mean_exact():
>       assert mean_valid(EVENING) == 25.275          # 101.1 / 4, by hand
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       assert 25.275000000000002 == 25.275
E        +  where 25.275000000000002 = mean_valid([27.3, 25.6, 24.6, 23.6, None, None])

test_mean.py:15: AssertionError
=========================== short test summary info ============================
FAILED test_mean.py::test_mean_exact - assert 25.275000000000002 == 25.275
1 failed, 1 passed in 0.01s
```

**Notice:** the function is right and the first test is wrong: it asks for more digits than a float keeps. `pytest.approx` accepts a difference of a millionth of the value.

**Ask the room:** Python 3.11 prints this mean as 25.275. Would `test_mean_exact` pass there?

??? note "Answer"
    Yes. Python 3.11 adds the four values one after the other, and the
    rounding lands on 25.275; since 3.12 `sum` adds them more exactly and
    gets 25.275000000000002. A test that compares floats exactly passes or
    fails with the version of Python: compare within a tolerance, and pin
    the Python.

---

### 4. One case on each side of every border { #borders }

<!-- 0:24 · 9 min -->

Code goes wrong most often at a border, so a test takes the value on it and the value just below; `@pytest.mark.parametrize` runs one test for each row of a table.

```python title="test_word.py"
import pytest


def word_for(temp):
    """The word for a mean temperature in °C: cold below 0, cool below 10,
    mild below 15, warm from 15."""
    if temp <= 0:
        return "cold"
    if temp < 10:
        return "cool"
    if temp < 15:
        return "mild"
    return "warm"


@pytest.mark.parametrize("temp, word", [
    (-3.9, "cold"), (-0.1, "cold"), (0, "cool"), (9.9, "cool"),
    (10, "mild"), (14.9, "mild"), (15, "warm"), (18.5, "warm"),
])
def test_word_for(temp, word):
    assert word_for(temp) == word
```

```text
$ python -m pytest -q test_word.py
..F.....                                                                 [100%]
=================================== FAILURES ===================================
____________________________ test_word_for[0-cool] _____________________________

temp = 0, word = 'cool'
...
>       assert word_for(temp) == word
E       AssertionError: assert 'cold' == 'cool'
...
test_word.py:21: AssertionError
=========================== short test summary info ============================
FAILED test_word.py::test_word_for[0-cool] - AssertionError: assert 'cold' ==...
1 failed, 7 passed in 0.02s
```

**Notice:** one case of eight fails, the value on the border at 0, and its name in brackets, `[0-cool]`, says which: the docstring says "below 0", the code says `<= 0`.

**Ask the room:** if the border at 10 were written `temp <= 10` instead, which of the eight cases would fail?

??? note "Answer"
    Only `(10, "mild")`: 10 would come out `cool`. The cases inside the
    ranges, −3.9 and 18.5, catch no border mistake; the pair on either
    side of a border, 9.9 and 10, catches it whichever way it slips.

---

### 5. Tests of the data as received: the station file and its flags { #data }

<!-- 0:33 · 10 min -->

A test can check a file too: what must hold on every row. GHCN-Daily marks each value that failed one of NCEI's checks with a quality flag, in the column `..._ATTRIBUTES` beside it.

1. Download the station file once into the folder; the numbers of curl's
   last line differ per laptop.

    ```text
    $ curl -O https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/LH000026730.csv
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100 5976k  100 5976k    0     0  2662k      0  0:00:02  0:00:02 --:--:-- 2662k
    ```

2. The tests read the file on the disk, not from the address: a test run
   needs no network.

    ```python title="test_vilnius.py"
    import csv

    import pytest

    with open("LH000026730.csv") as file:        # downloaded once with curl
        ROWS = list(csv.DictReader(file))


    def value(row, column, use_flags):
        """The value in °C; None if empty, or if flagged and use_flags is True."""
        flag = (row[column + "_ATTRIBUTES"] + ",,").split(",")[1]
        if row[column].strip() == "" or (use_flags and flag != ""):
            return None
        return int(row[column]) / 10               # the file stores tenths of °C


    def test_dates_in_order_none_twice():
        dates = [row["DATE"] for row in ROWS]
        assert dates == sorted(set(dates))


    @pytest.mark.parametrize("use_flags", [False, True])
    def test_tmin_not_above_tmax(use_flags):
        wrong = []
        for row in ROWS:
            tmin = value(row, "TMIN", use_flags)
            tmax = value(row, "TMAX", use_flags)
            if tmin is not None and tmax is not None and tmin > tmax:
                wrong.append((row["DATE"], tmin, tmax))
        assert wrong == [], f"{len(wrong)} days, the first: {wrong[:2]}"
    ```

```text
$ python -m pytest -q test_vilnius.py
.F.                                                                      [100%]
=================================== FAILURES ===================================
_______________________ test_tmin_not_above_tmax[False] ________________________
...
E       AssertionError: 56 days, the first: [('1901-12-01', 9.5, -3.2), ('1904-06-24', 6.8, 1.6)]
...
test_vilnius.py:30: AssertionError
=========================== short test summary info ============================
FAILED test_vilnius.py::test_tmin_not_above_tmax[False] - AssertionError: 56 ...
1 failed, 2 passed in 0.18s
```

**Notice:** read as it is, the file has 56 days whose lowest temperature lies above their highest; with the flagged values left out, none.

**Ask the room:** the test fails on a file that NCEI has checked. Is the file wrong, the test, or the reading?

??? note "Answer"
    The reading. NCEI's checks found all 56 days and flagged them, most
    with `I`, "failed internal consistency check" in its readme; 31 of
    them are December 2002, when the two columns look swapped. A reader
    who ignores the flags uses values the provider marked as wrong. The
    test states a fact true of every real day and finds the rows that
    break it in a fraction of a second.

---

### 6. The environment again from the pinned file, the same results { #fresh-env }

<!-- 0:43 · 9 min -->

The environment on this laptop holds everything ever installed into it; one made from `environment.yml` alone is the next laptop, and the tests must give the same results in it.

1. All the tests of the folder, in `analysis`.

    ```text
    $ python -m pytest -q
    F..F...F.....                                                            [100%]
    ...
    3 failed, 10 passed in 0.16s
    ```

2. A new environment `check` from the file alone (`-n check` gives it
   another name), the same tests in it. conda takes most packages from its
   cache, so it is quick.

    ```text
    $ conda env create -n check -f environment.yml
    ...
    #     $ conda activate check
    $ conda activate check
    $ python -m pytest -q
    F..F...F.....                                                            [100%]
    ...
    3 failed, 10 passed in 0.14s
    ```

3. Back to `analysis`, and remove `check`: `Enter` at the first question,
   `y` and `Enter` at the second.

    ```text
    $ conda activate analysis
    $ conda env remove -n check
    ...
    Proceed ([y]/n)?
    ...
    Everything found within the environment (/Users/smilte/miniforge3/envs/check), including any conda environment configurations and any non-conda files, will be deleted. Do you wish to continue?
     (y/[n])? y
    ```

**Notice:** the same three failures and ten passes in an environment made from the file alone: the result does not depend on what else this laptop holds.

**Ask the room:** what would `python -m pytest -q` print in `check` if `environment.yml` had no line for pytest?

??? note "Answer"
    ```text
    $ python -m pytest -q
    /Users/smilte/miniforge3/envs/check/bin/python: No module named pytest
    ```

    On the laptop where pytest was installed by hand everything runs; only
    an environment made from the file shows what the file forgot.

---

### 7. Library card { #card }

<!-- 0:52 · 3 min -->

The calls and commands of this page, one line each.

| Call | What it does |
|--|--|
| `def test_name():` in a file `test_....py` | a test that pytest finds and runs |
| `assert condition, message` | nothing when true; a failure with the message when false |
| `x == pytest.approx(25.275)` | equal within a millionth of 25.275 |
| `@pytest.mark.parametrize("temp, word", [(0, "cool"), ...])` | the test below runs once per row of the table |
| `python -m pytest -q` | every test of the folder; `-q`: one line of dots and the summary |
| `python -m pytest -q test_mean.py` | the tests of one file |
| `csv.DictReader(file)` | the rows of a CSV file, each a dict from the header's names |
| `(text + ",,").split(",")[1]` | the second field of a text with commas, empty if missing |
| `str(date(2023, 1, 1) + timedelta(days=i))` | the date i days after 1 January 2023, as `"2023-01-..."` |
| `conda list "^(python|pytest)$"` | the exact versions installed |
| `conda env create -n check -f environment.yml` | a new environment from the file alone |
| `conda env remove -n check` | delete that environment |
| `curl -O URL` | download a file into the folder, under its own name |

---

## Part 3 · The problem { #part-3 }

### 8. Which year since 1881 was the coldest in Vilnius? { #problem }

<!-- 0:55 · 50 min: predict 5, solve 25, check 10, hand in 10 -->

An LLM writes the function that turns the station's days into yearly means;
you write the tests that decide whether to trust it. The data: the station
file of section 5 (GHCN-Daily, NOAA NCEI; terms and citation under "Before
the session"), the column `TAVG`, the daily mean temperature in tenths of
°C, empty where missing; in some years whole days are absent from the file.
Download it once if section 5 did not:

```text
$ curl -O https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/LH000026730.csv
```

The prompt, the same for every pair:

```text
Write a Python function yearly_means(dates, temps). dates is a list of
dates as strings "YYYY-MM-DD"; temps is a list of the same length with the
daily mean temperature in °C, or None for a day without a value. Return a
dict that maps each year (an int) to the mean temperature of that year.
Plain Python, no libraries, with a docstring.
```

Work in pairs, with any tools, an LLM too: the work is the tests and the checks, not the typing.

1. **Predict**, before you send the prompt, on paper: three or more inputs
   that could make such a function give a wrong yearly mean, each with
   the answer it should give. And a guess: the coldest year (a decade is
   enough) and its mean.
2. **Solve.** Save the reply as `yearly.py` and your inputs as tests in
   `test_yearly.py`; run `python -m pytest -q test_yearly.py`. Where a
   test fails, decide who is wrong, the test or the function, and fix that
   one, by hand or with the LLM. Then read the station file into `dates`
   and `temps` and find the coldest year.
3. **Check the machine's work.**
    - By hand: the first five days of 1942 in the file, in tenths of °C;
      their mean on paper, in °C; your reading code's five values must
      give the same.
    - Each test able to fail: change one line of `yearly_means` on purpose
      (take out a check you added) and see which test fails; put it back.
    - Read off: how many days the coldest year has in the file, 365 or
      366; how many years have no mean, and why.
    - Against your prediction: where they differ, say which was wrong.
4. **Hand in.** The coldest year with its mean, the answer of the first
   version if it differed, the name of the test that caught it, two
   sentences in your own words, and one line: which LLM wrote what.

??? tip "Hint 1: inputs that break such functions"
    A day with `None`; a year with every day `None`; a year with days
    absent from the lists altogether (in the file, 1883 has only January
    and February); a leap year, 366 days; two years in one list. For each,
    decide first what the function should return: a mean, or `None`.

??? tip "Hint 2: a whole year of dates in a test"
    ```python
    from datetime import date, timedelta


    def days_of(year):
        """Every date of a year, "YYYY-MM-DD": 365 strings, 366 in a leap year."""
        first = date(year, 1, 1)
        days = (date(year + 1, 1, 1) - first).days
        return [str(first + timedelta(days=i)) for i in range(days)]
    ```

??? tip "Hint 3: reading the file"
    ```python
    import csv

    dates, temps = [], []
    with open("LH000026730.csv") as file:
        for row in csv.DictReader(file):
            dates.append(row["DATE"])
            text = row["TAVG"].strip()
            temps.append(int(text) / 10 if text else None)   # tenths of °C
    ```

??? note "One solution"
    The tests, written before the function was read:

    ```python title="test_yearly.py"
    from datetime import date, timedelta

    import pytest

    from yearly import yearly_means


    def days_of(year):
        """Every date of a year, "YYYY-MM-DD": 365 strings, 366 in a leap year."""
        first = date(year, 1, 1)
        days = (date(year + 1, 1, 1) - first).days
        return [str(first + timedelta(days=i)) for i in range(days)]


    def test_one_warm_day_by_hand():
        temps = [365.0] + [0.0] * 364               # (365 + 0 + ... + 0) / 365
        assert yearly_means(days_of(2023), temps)[2023] == pytest.approx(1.0)


    def test_a_leap_year_has_366_days():
        temps = [366.0] + [0.0] * 365
        assert yearly_means(days_of(2024), temps)[2024] == pytest.approx(1.0)


    def test_two_years_apart():
        temps = [0.0] * 365 + [10.0] * 365
        means = yearly_means(days_of(2022) + days_of(2023), temps)
        assert means[2022] == pytest.approx(0.0)
        assert means[2023] == pytest.approx(10.0)


    def test_a_day_without_a_value():
        temps = [5.0] * 365
        temps[100] = None
        assert yearly_means(days_of(2023), temps)[2023] is None


    def test_a_year_of_two_days():
        means = yearly_means(["1883-01-01", "1883-01-02"], [-5.0, -6.0])
        assert means == {1883: None}
    ```

    A first version that does what the prompt says, the mean of the days
    that have a value:

    ```python title="yearly.py"
    def yearly_means(dates, temps):
        """The mean temperature of each year, from the days that have a value."""
        sums = {}
        counts = {}
        for day, temp in zip(dates, temps):
            if temp is not None:
                year = int(day[:4])
                sums[year] = sums.get(year, 0) + temp
                counts[year] = counts.get(year, 0) + 1
        return {year: sums[year] / counts[year] for year in sums}
    ```

    ```text
    $ python -m pytest -q test_yearly.py
    ...FF                                                                    [100%]
    =================================== FAILURES ===================================
    __________________________ test_a_day_without_a_value __________________________
    ...
    E       assert 5.0 is None
    ...
    ___________________________ test_a_year_of_two_days ____________________________
    ...
    E       assert {1883: -5.5} == {1883: None}
    ...
    =========================== short test summary info ============================
    FAILED test_yearly.py::test_a_day_without_a_value - assert 5.0 is None
    FAILED test_yearly.py::test_a_year_of_two_days - assert {1883: -5.5} == {1883...
    2 failed, 3 passed in 0.01s
    ```

    The answer, from the station file:

    ```python title="coldest.py"
    import csv
    import matplotlib.pyplot as plt
    from yearly import yearly_means

    dates, temps = [], []
    with open("LH000026730.csv") as file:
        for row in csv.DictReader(file):
            dates.append(row["DATE"])
            text = row["TAVG"].strip()
            temps.append(int(text) / 10 if text else None)   # tenths of °C
    first = dates.index("1942-01-01")
    print(dates[first:first + 5], temps[first:first + 5])
    means = yearly_means(dates, temps)
    complete = {year: m for year, m in means.items() if m is not None}
    print(len(means), "years in the file,", len(complete), "with a mean")
    ranked = sorted(complete, key=complete.get)
    for year in ranked[:3] + ranked[-1:]:          # the 3 coldest, the warmest
        print(f"{year}: {complete[year]:.2f} °C")

    days = {}                        # the years without a mean: the days present
    for day, temp in zip(dates, temps):
        if means.get(int(day[:4])) is None and temp is not None:
            days.setdefault(int(day[:4]), []).append(temp)
    partial = {year: sum(v) / len(v) for year, v in days.items()}
    print("no mean:", {year: round(m, 2) for year, m in partial.items()})

    fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
    ax.plot(list(complete), list(complete.values()), "o", markersize=4,
            label="Years with a value on every day")
    ax.plot(list(partial), list(partial.values()), "x", color="C3",
            label="Years without: the mean of the days present")
    ax.set_xlabel("Year")
    ax.set_ylabel("Mean of the daily mean temperatures (°C)")
    ax.set_title("Vilnius: 1942 is the coldest year with every day, 4.35 °C")
    ax.legend(frameon=False)
    fig.savefig("coldest.svg")
    ```

    ```text
    $ python coldest.py
    ['1942-01-01', '1942-01-02', '1942-01-03', '1942-01-04', '1942-01-05'] [-17.1, -20.8, -13.9, -4.3, 0.2]
    142 years in the file, 142 with a mean
    1883: -5.63 °C
    1941: 3.88 °C
    1942: 4.35 °C
    2024: 9.32 °C
    no mean: {}
    ```

    With the first version, the coldest year is 1883, from 59 winter days.
    The version that passes every test: a year has a mean only if each of
    its days has a value.

    ```python title="yearly.py"
    import calendar


    def yearly_means(dates, temps):
        """The mean temperature of each year; None for a year in which a day is
        missing from the lists or has the value None."""
        by_year = {}
        for day, temp in zip(dates, temps):
            by_year.setdefault(int(day[:4]), []).append(temp)
        means = {}
        for year, values in by_year.items():
            days = 366 if calendar.isleap(year) else 365
            if len(values) == days and None not in values:
                means[year] = sum(values) / days
            else:
                means[year] = None
        return means
    ```

    ```text
    $ python -m pytest -q test_yearly.py
    .....                                                                    [100%]
    5 passed in 0.01s
    $ python coldest.py
    ['1942-01-01', '1942-01-02', '1942-01-03', '1942-01-04', '1942-01-05'] [-17.1, -20.8, -13.9, -4.3, 0.2]
    143 years in the file, 128 with a mean
    1942: 4.35 °C
    1940: 4.37 °C
    1980: 4.44 °C
    2020: 8.70 °C
    no mean: {1883: -5.63, 1884: 8.95, 1890: 6.91, 1892: 7.06, 1915: 6.42, 1919: 5.68, 1920: 4.54, 1941: 3.88, 1986: 5.93, 1994: 6.66, 1999: 7.61, 2021: 7.05, 2024: 9.32, 2025: 8.99}
    ```

    ![The yearly mean temperature of Vilnius, 1881 to 2025: blue points for the 128 years with a value on every day, between 4.35 °C in 1942 and 8.70 °C in 2020; red crosses for the years without, at the mean of the days present: 1883 far below at −5.63 °C from two winter months, 1884, 2024 and 2025 above every blue point](img/s12/coldest.svg)

    By hand: the file holds −171, −208, −139, −43 and 2 tenths of °C for
    1 to 5 January 1942; (−17.1 − 20.8 − 13.9 − 4.3 + 0.2) / 5 = −55.9 / 5
    = −11.18 °C, the mean of the five values printed.

    Handed in: *The coldest year of the Vilnius station since 1881, of the
    128 years with a value on every day, is 1942, 4.35 °C, just below 1940
    (4.37 °C). The first version gave 1883 at −5.63 °C, the mean of 59
    days of January and February; `test_a_year_of_two_days` caught it.*

**With your own project data:** a function of your own project that turns
rows into one number per group (a mean per year, a count per sample, a sum
per person): send an LLM your own prompt for it, write the inputs that
could break it and their answers first, then the tests, then run them.

---

## Part 4 · Show and discuss { #part-4 }

### 9. Three questions about the pairs' tests { #discuss }

<!-- 1:45 · 15 min -->

Two or three pairs show their tests and their answer, and read their two sentences.

**Ask the room:** two pairs hand in 1883, −5.63 °C, and 1942, 4.35 °C. Which test tells them apart?

??? note "Answer"
    A year with days absent from the lists. In the file, 1883 has 59 rows,
    January and February, and no `None` among them: a function that only
    skips `None` averages two winter months and calls them a year. A test
    with two days of one year, and `None` as its answer, catches it.

**Ask the room:** one pair's tests all passed on the first run. Is their function right?

??? note "Answer"
    Only as far as tests that can fail say so. Change the function on
    purpose: a test that has never failed may check nothing. Then the
    function is right for the cases the tests hold, and the pair can name
    them.

**Ask the room:** 2024 has 355 days in the file and their mean is 9.32 °C, above every year with every day (the warmest, 2020, 8.70 °C). Was 2024 the warmest year?

??? note "Answer"
    The rule of the tests gives 2024 no mean, and the rule stays: it was
    decided before looking at which year it favours. A second question
    can still be answered by hand: to bring 2024 down to 8.70 °C, its 11
    absent days would have to average (366 × 8.70 − 355 × 9.32) / 11 =
    −11.3 °C. They are 28–31 March, 1 May, 12 August, 18–21 November and
    1 December: 2024 was almost certainly the warmest year, a statement
    that needs this argument next to it.

A test states what the function must do, decided before its code is read; code from anyone, an LLM included, is trusted as far as tests that have been seen to fail, and a pinned environment makes the same tests give the same answer on the next laptop.

---

## Optional, if the room is fast { #optional }

### 10. A fresh clone, rebuilt with one command { #clone }

<!-- — · 15 min -->

A clone holds only what was committed; rebuilt there, it is the stranger's copy of the work.

1. Two files. `.gitignore` names what Git leaves out: the downloaded data
   and what the scripts make. `rebuild.sh` makes everything again and runs
   the tests.

    ```text title=".gitignore"
    LH000026730.csv
    coldest.svg
    __pycache__/
    .pytest_cache/
    ```

    ```bash title="rebuild.sh"
    # Download the station file, compute the yearly means, run their tests.
    set -e                 # stop at the first command that fails
    curl -sSO https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/LH000026730.csv
    python coldest.py
    python -m pytest -q test_yearly.py
    ```

2. Make the folder a Git repository and commit everything. Your id and
   the counts differ.

    ```text
    $ git init
    Initialized empty Git repository in /Users/smilte/weather-s12/.git/
    $ git add .
    $ git commit -m "Yearly means of Vilnius, their tests, one command"
    [main (root-commit) 3a706af] Yearly means of Vilnius, their tests, one command
     9 files changed, 180 insertions(+)
    ...
    ```

3. Clone it into a second folder and rebuild there.

    ```text
    $ cd ~
    $ git clone weather-s12 weather-check
    Cloning into 'weather-check'...
    done.
    $ cd weather-check
    $ ls
    coldest.py  environment.yml  rebuild.sh  test_mean.py  test_vilnius.py  test_word.py  test_yearly.py  yearly.py
    $ bash rebuild.sh
    ['1942-01-01', '1942-01-02', '1942-01-03', '1942-01-04', '1942-01-05'] [-17.1, -20.8, -13.9, -4.3, 0.2]
    143 years in the file, 128 with a mean
    1942: 4.35 °C
    1940: 4.37 °C
    1980: 4.44 °C
    2020: 8.70 °C
    no mean: {1883: -5.63, 1884: 8.95, 1890: 6.91, 1892: 7.06, 1915: 6.42, 1919: 5.68, 1920: 4.54, 1941: 3.88, 1986: 5.93, 1994: 6.66, 1999: 7.61, 2021: 7.05, 2024: 9.32, 2025: 8.99}
    .....                                                                    [100%]
    5 passed in 0.01s
    $ cd ~/weather-s12
    ```

**Check:** in `weather-check`, the same years and `5 passed`, from what Git holds and the file at its address.

---

## Aims practised

- ♻️ **Reproducibility:** exact versions in `environment.yml`, and an
  environment made from that file alone gives the same test results; a
  fresh clone rebuilds the answer.
- ⚙️ **Automation:** pytest runs every test of the folder in one command,
  and its exit status says whether the result can be trusted.
- 🔧 **Tool-agnosticism:** tests decided before the code is read check a
  function whoever wrote it, a person or any LLM.
