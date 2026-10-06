# Seminar 12 — Clean a Table by Script

**Paired lecture:** 12 Pandas & Data Cleaning · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student has a script that cleans `D0_KPi.csv` into
`data/processed/d0_clean.csv`, prints a count for every rule it applied,
and has those counts in the README.

The new tool of the session is Pandas. Everything else is known: the project
folder, the terminal (`zsh` on macOS, PowerShell 7 on Windows), running a
script, NumPy masks, checksums.

## Run sheet

One screen for the front of the room. Each line links to its section.

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · A small table by script** · 42 min | | |
| 0:00 | [1. Install Pandas](#install) | `python3 -m pip install pandas` (Windows `python`) | A version number printed |
| 0:08 | [2. Read the pendulum file](#read) | `pd.read_csv(RAW, sep=";", decimal=",")` | Three columns, two with the right type |
| 0:20 | [3. Clean it and compare](#compare) | `scripts/clean.py`, then `shasum -a 256`, `Get-FileHash` | The same bytes as Lecture 4's `pendulum_script.csv` |
| 0:34 | [4. The partner's second file](#second) | `pendulum_run2.csv` through both scripts | 10 rows from Lecture 4's script, 9 from `clean.py` |
| | **Part 2 · Audit the data file** · 36 min | | |
| 0:42 | [5. Shape and types](#types) | `scripts/audit.py`, `df.dtypes` | 91 583 rows, four columns of `float64` |
| 0:48 | [6. The summary and the code −100](#code) | `df.describe()` | 49 codes turned into NaN |
| 1:02 | [7. Five questions](#questions) | The audit, one count per line | A count for each question |
| | **Part 3 · Clean by script** · 21 min | | |
| 1:18 | [8. The cleaning script](#clean) | `scripts/clean_d0.py` | `data/processed/d0_clean.csv` and a log |
| 1:30 | [9. Check what it did](#check) | The checksums of both files | The raw file unchanged, the output the same on every laptop |
| | **Part 4 · Write it down** · 21 min | | |
| 1:39 | [10. The cleaning in the README](#readme) | `README.md`, then the preview | A **Cleaning** section with the counts, committed |
| 1:54 | [11. Wrap up](#wrap-up) | The list of what was learned | |
| | **Optional, if the room is fast** | | |
| — | [12. A table by group](#group) | `scripts/tau_by_region.py`, `groupby` | `results/tau_by_region.csv` |

**If time runs short:** show section 4 on the projector only, shorten
section 9 to step 3, the two checksums, and keep section 10: the README is
the written result of the session.

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

    Every command stands alone in a block. It is typed as it stands, in the
    terminal of VS Code, in the project folder, and ended with `Enter`. The
    terminal is `zsh` on macOS and PowerShell 7 on Windows, as since
    Seminar 4. Where the two differ, the step has a tab for **macOS** and
    one for **Windows**. Most often the difference is the first word:
    `python3` on macOS, `python` on Windows. The outputs were printed by
    `zsh` with Pandas 3.0.1 and by PowerShell 7.6 on Windows with Pandas
    3.0.6. Keys are written for Windows, with macOS in brackets.

??? info "Before the session"
    For the room: the project folder `analysis-project` with Python from
    Seminar 4, Git, and the files of the next box in their folders. `pip`
    installs NumPy together with Pandas in section 1 if it is missing.

    Section 3 compares with `data/processed/pendulum_script.csv`, the file
    Lecture 4's script writes. It is listed in `.gitignore` since Seminar 5,
    so it is in the folder and not in the repository. A student who does not
    have it makes it with the line of Seminar 4:

    === "macOS"

        ```text
        python3 scripts/clean_pendulum.py data/raw/pendulum.csv data/processed/pendulum_script.csv
        ```

    === "Windows"

        ```text
        python scripts/clean_pendulum.py data/raw/pendulum.csv data/processed/pendulum_script.csv
        ```

    It prints `9 rows written to data/processed/pendulum_script.csv`.

    For you:

    - The page done once on a Mac and once on a Windows laptop with
      PowerShell 7.
    - `pendulum_script.csv` on your own laptop checked: 97 bytes, SHA-256
      `be05af03…fff0870b`. Section 3 compares against it.
    - The network of the room tried: section 1 downloads about 10 MB, and
      about 12 MB more where NumPy is missing. If it is slow, have a phone
      hotspot ready, and let a student whose download stalls work with a
      neighbour until it finishes.

??? info "Files for this seminar"
    A browser saves each file under the name in the second column. Drag it
    from **Downloads** onto the folder in the third.

    | File | Saved as | Goes into | What it is |
    |--|--|--|--|
    | [`pendulum_raw.csv`](../data/pendulum_raw.csv){ download="pendulum.csv" } | `pendulum.csv` | `data/raw` | The pendulum table as the lab partner sent it, 130 bytes |
    | [`pendulum_run2_raw.csv`](../data/pendulum_run2_raw.csv){ download="pendulum_run2.csv" } | `pendulum_run2.csv` | `data/raw` | Section 4: the partner's second series, 125 bytes |
    | [`cli_clean_pendulum.py`](../data/cli_clean_pendulum.py){ download="clean_pendulum.py" } | `clean_pendulum.py` | `scripts` | Lecture 4's script, handed out in Seminar 4 |
    | [`D0_KPi.csv`](../data/D0_KPi.csv){ download="D0_KPi.csv" } | `D0_KPi.csv` | `data/raw` | The LHCb file, 3 926 142 bytes |

---

## Part 1 · A small table by script { #part-1 }

**0:00 to 0:42 · sections 1 to 4**

Lecture 2 cleaned the pendulum table by hand: one line deleted, two
replacements, one column removed. Lecture 4's script `clean_pendulum.py`
makes the same four edits as text and writes `pendulum_script.csv`, 97
bytes. The room now writes the cleaning again with Pandas, as rules about
what a column holds, proves that the result is the same file, and runs both
scripts on a second file.

---

### 1. Install Pandas { #install }

**0:00 · 8 min**

**Tell the room.** Pandas is a library for tables. A table in Pandas has
columns with names, one type per column, and cells that may be empty. It is
installed with `pip`, the program that comes with Python and fetches
libraries.

1. Open the project folder in VS Code and select **Terminal** >
   **New Terminal**.

2. Install Pandas.

    === "macOS"

        ```text
        python3 -m pip install pandas
        ```

    === "Windows"

        ```text
        python -m pip install pandas
        ```

    Near the end of the output stands a line that begins with
    `Successfully installed`.

3. Check that Python finds it.

    === "macOS"

        ```text
        python3 -c "import pandas; print(pandas.__version__)"
        ```

    === "Windows"

        ```text
        python -c "import pandas; print(pandas.__version__)"
        ```

!!! success "You should now see"
    A version number, for example `3.0.6`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: `No module named pip` | `py -m pip install pandas` |
    | `externally-managed-environment` | The Python is the one of the system, not the one from python.org. Run the installer from python.org again |
    | The version starts with `2.` | Nothing. The one difference on this page is named where it occurs |

---

### 2. Read the pendulum file { #read }

**0:08 · 12 min**

**Tell the room.** `read_csv` turns a text file into a table. It has to be
told two things that a spreadsheet takes from the settings of the computer:
the character between the values and the decimal sign. The room finds both
by reading the file three times.

1. Select the `scripts` folder, then **New File**, and name it:

    ```text
    clean.py
    ```

    It is a new file next to Lecture 4's `clean_pendulum.py`, which stays
    as it is. Type into it:

    ```text
    import pandas as pd

    RAW = "data/raw/pendulum.csv"

    df = pd.read_csv(RAW)
    print(df.shape)
    ```

2. Save and run it.

    === "macOS"

        ```text
        python3 scripts/clean.py
        ```

    === "Windows"

        ```text
        python scripts/clean.py
        ```

    It prints `(10, 1)`: ten rows, one column. Pandas expects a comma
    between the values.

3. Change the line with `read_csv` and add a line under the `print`.

    ```text
    df = pd.read_csv(RAW, sep=";")
    print(df.shape)
    print(df.dtypes)
    ```

    Run it with `↑` and Enter.

    ```text
    (10, 3)
    nr           float64
    length_cm        str
    t10_s            str
    dtype: object
    ```

    Three columns. `str` means text (Pandas 2 prints `object`). The times
    are text because `9,02` is not a number to Python.

4. Give the decimal sign, and print the table itself.

    ```text
    df = pd.read_csv(RAW, sep=";", decimal=",")
    print(df)
    print(df.dtypes)
    ```

!!! success "You should now see"
    ```text
        nr length_cm  t10_s
    0  1.0        20   9.02
    1  2.0        30  11.05
    2  3.0        40  12.61
    3  4.0        50  14.23
    4  5.0        60  15.49
    5  6.0        70  16.84
    6  7.0        80  17.90
    7  8.0        90  19.10
    8  9.0       100  20.01
    9  NaN      mean  15.14
    nr           float64
    length_cm        str
    t10_s        float64
    dtype: object
    ```

Ask the room why `nr` is a float and `length_cm` is text. Both answers are
in row 9. The cell under `nr` is empty: Pandas writes NaN, and NaN is a
float. The cell under `length_cm` says `mean`, and a column has one type.
The numbers 0 to 9 on the left are not in the file. They are the index, a
label for each row.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `FileNotFoundError` | The terminal is not in the project folder. Run `pwd`, then `cd` to the folder |
    | `ModuleNotFoundError: No module named 'pandas'` | `python` and `pip` belong to two installations. Install with `-m pip` after the same first word, as in section 1 |

---

### 3. Clean it and compare { #compare }

**0:20 · 14 min**

**Tell the room.** Each hand edit becomes one line. The two replacements are
already done: they are the two options of `read_csv`. What is left is the
line with the mean, the column of row numbers and the type of `length_cm`.
Then the output is compared with the file Lecture 4's script wrote,
`data/processed/pendulum_script.csv`. That file stays as it is.

1. Replace the two `print` lines at the end of the script by:

    ```text
    df = df[df["nr"].notna()]
    df = df.drop(columns="nr")
    df["length_cm"] = df["length_cm"].astype(int)
    print(df.dtypes)

    OUT = "data/processed/pendulum.csv"
    df.to_csv(OUT, index=False)
    print(f"{len(df)} rows written to {OUT}")
    ```

    The script writes over `data/processed/pendulum.csv`, the cleaned copy
    the README names. From today a script makes it.

2. Run the script.

    === "macOS"

        ```text
        python3 scripts/clean.py
        ```

    === "Windows"

        ```text
        python scripts/clean.py
        ```

    It prints:

    ```text
    length_cm      int64
    t10_s        float64
    dtype: object
    9 rows written to data/processed/pendulum.csv
    ```

3. Compare the two files in VS Code. Select `pendulum.csv` in the Side Bar,
   hold `Ctrl` (macOS `Cmd`) and select `pendulum_script.csv`. Right-click
   and select **Compare Selected**. Two lines are marked:

    ```text
    Lecture 4   80,17.90    90,19.10
    Pandas      80,17.9     90,19.1
    ```

    17.90 and 17.9 are the same number, and Pandas writes the shorter text.
    In the file the zero said that the time was read to 0.01 s. The file of
    Pandas has 95 bytes, and on Windows 105: each line ends in CR LF.

4. Say how the numbers are written. Change the line with `to_csv`:

    ```text
    df.to_csv(OUT, index=False, float_format="%.2f",
              lineterminator="\n")
    ```

    `"%.2f"` writes two decimals in every row. `"\n"` ends every line with
    one byte on every system. Without it Windows writes two.

5. Delete the line `print(df.dtypes)`, run the script and compare the
   checksums of the two files. The wildcard takes both.

    === "macOS"

        ```text
        shasum -a 256 data/processed/pendulum*.csv
        ```

        ```text
        be05af034937ef615c93b2fb5d8369c899def80d0472a6187c5dbd3afff0870b  data/processed/pendulum.csv
        be05af034937ef615c93b2fb5d8369c899def80d0472a6187c5dbd3afff0870b  data/processed/pendulum_script.csv
        ```

    === "Windows"

        ```text
        (Get-FileHash data/processed/pendulum*.csv).Hash
        ```

        ```text
        BE05AF034937EF615C93B2FB5D8369C899DEF80D0472A6187C5DBD3AFFF0870B
        BE05AF034937EF615C93B2FB5D8369C899DEF80D0472A6187C5DBD3AFFF0870B
        ```

!!! success "You should now see"
    Two lines that end in the same digits, `fff0870b`. The two files are
    identical: 97 bytes each.

**Say it in these words.** The Pandas script does what Lecture 4's script
did, and this is the proof. Delete `data/processed/pendulum.csv`, run
`clean.py`, and it is back with the same 97 bytes.

??? info "The script, complete"
    ```text
    """Clean the pendulum table: data/raw -> data/processed."""
    import pandas as pd

    RAW = "data/raw/pendulum.csv"
    OUT = "data/processed/pendulum.csv"

    df = pd.read_csv(RAW, sep=";", decimal=",")
    df = df[df["nr"].notna()]
    df = df.drop(columns="nr")
    df["length_cm"] = df["length_cm"].astype(int)
    df.to_csv(OUT, index=False, float_format="%.2f",
              lineterminator="\n")
    print(f"{len(df)} rows written to {OUT}")
    ```

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: the checksums differ, and **Compare Selected** shows no difference | `lineterminator="\n"` is missing: the file ends its lines in CR LF. `(Get-Item data/processed/pendulum.csv).Length` prints 107, not 97 |
    | One line only: `pendulum_script.csv` is missing | Make it with the line in **Before the session**, then compare again |
    | `ValueError: invalid literal for int() with base 10: 'mean'` | The line with `notna()` is missing or stands below `astype` |
    | The file begins with `,length_cm,t10_s` | `index=False` is missing |

---

### 4. The partner's second file { #second }

**0:34 · 8 min**

**Tell the room.** The lab partner sent a second series: the same nine
lengths, in the same form. A person sees two differences at once. The
summary line is spelt `Mean`, and the time at 80 cm was not taken. Both
scripts are run on it, and the room predicts first how many rows a cleaned
file should have.

1. Download `pendulum_run2_raw.csv` from the box **Files for this seminar**.
   The browser saves it as `pendulum_run2.csv`. Drag it onto `data/raw` and
   open it.

    ```text
    nr;length_cm;t10_s
    1;20;8,97
    2;30;11,02
    3;40;12,74
    4;50;14,15
    5;60;15,58
    6;70;16,83
    7;80;
    8;90;19,08
    9;100;20,04
    ;Mean;14,80
    ```

    Ask how many rows the cleaned file should have. Nine lengths, eight of
    them with a time.

2. Run Lecture 4's script on it.

    === "macOS"

        ```text
        python3 scripts/clean_pendulum.py data/raw/pendulum_run2.csv data/processed/run2_script.csv
        ```

    === "Windows"

        ```text
        python scripts/clean_pendulum.py data/raw/pendulum_run2.csv data/processed/run2_script.csv
        ```

    It prints `10 rows written to data/processed/run2_script.csv`. Open
    the file. It ends in:

    ```text
    80,
    90,19.08
    100,20.04
    Mean,14.80
    ```

    The script skips a line that contains `mean`. `M` is not `m`: 77 and
    109 in the ASCII table of Lecture 3.

3. In `clean.py`, change the two names at the top to:

    ```text
    RAW = "data/raw/pendulum_run2.csv"
    OUT = "data/processed/pendulum_run2.csv"
    ```

    Run it.

    === "macOS"

        ```text
        python3 scripts/clean.py
        ```

    === "Windows"

        ```text
        python scripts/clean.py
        ```

    It prints `9 rows written to data/processed/pendulum_run2.csv`. Open
    the file. It ends in:

    ```text
    70,16.83
    80,
    90,19.08
    100,20.04
    ```

4. Change the two names back to `pendulum.csv` and run the script once
   more: `9 rows written to data/processed/pendulum.csv`. Seminar 13 turns
   the two names into words on the command line.

!!! success "You should now see"
    In `data/processed`: `run2_script.csv` with 10 rows and the `Mean`
    line, 103 bytes, and `pendulum_run2.csv` with 9 rows and an empty time
    at 80 cm, 92 bytes.

**Say it in these words.** Lecture 4's script moves characters, and does
what its text says. `clean.py` drops the row that has no `nr`, whatever the
summary line is called. The missing time becomes NaN, and the file still
says that 80 cm was not timed.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `ValueError: invalid literal for int() with base 10: 'Mean'` | `RAW` names the second file and the line with `notna()` is missing |
    | `FileNotFoundError: ... pendulum_run2.csv` | The file is still in **Downloads**, or was saved as `pendulum_run2_raw.csv`. Rename it in the Side Bar |

---

## Part 2 · Audit the data file { #part-2 }

**0:42 to 1:18 · sections 5 to 7**

Nobody can read 91 583 rows. An audit asks the table a fixed list of
questions, and every answer is a count. Nothing is changed in this part: the
script only reads and prints.

---

### 5. Shape and types { #types }

**0:42 · 6 min**

**Tell the room.** The first look at a table is its size and the type of
each column. Line 1 of the file becomes the names of the columns.

1. Select the `scripts` folder, then **New File**, and name it:

    ```text
    audit.py
    ```

    Type into it:

    ```text
    import numpy as np
    import pandas as pd

    df = pd.read_csv("data/raw/D0_KPi.csv")
    print(df.shape)
    print(df.dtypes)
    print(df.head())
    ```

2. Run it.

    === "macOS"

        ```text
        python3 scripts/audit.py
        ```

    === "Windows"

        ```text
        python scripts/audit.py
        ```

!!! success "You should now see"
    ```text
    (91583, 4)
    M         float64
    PT        float64
    TAU       float64
    IPCHI2    float64
    dtype: object
               M         PT       TAU       IPCHI2
    0  1880.6490  3000.9534  0.000413  1299.167500
    1  1860.6599  2803.4126  0.000186     0.341822
    2  1913.8755  2542.1690  0.000185    17.386473
    3  1888.7571  4453.1040  0.000568    56.797930
    4  1862.5100  2764.2280  0.000287     3.644997
    ```

Four columns of `float64` and no column of text: every cell of the file was
read as a number. The size agrees with the README: 91 583 rows and 4
columns. The printout is rounded to six decimals. The table holds every
digit of the file.

---

### 6. The summary and the code −100 { #code }

**0:48 · 14 min**

**Tell the room.** `describe()` gives eight numbers for each column. Reading
them is the fastest way to find a value that cannot be a measurement.

Give the room two minutes with the table before you say anything.

1. Replace the line `print(df.head())` by this line, and run the script:

    ```text
    print(df.describe())
    ```

    It prints:

    ```text
                      M            PT           TAU         IPCHI2
    count  91583.000000  91583.000000  91583.000000   91583.000000
    mean    1864.104582   3448.928182     -0.052522     457.513042
    std       25.565096   1301.067191      2.312500    6378.852807
    min     1766.209600    755.268600   -100.000000       0.000014
    25%     1845.991900   2723.341800      0.000185       2.124486
    50%     1864.078100   3048.925800      0.000272       6.298690
    75%     1881.531250   3676.466550      0.000605      27.436283
    max     2453.658400  64509.950000      0.578799  891711.060000
    ```

2. Ask which numbers cannot be right. Collect the answers on the board:

    | In the table | Why it stands out |
    |--|--|
    | `TAU`: mean −0.052522 | A mean decay time below zero |
    | `TAU`: min −100 | The file's code for a missing value |
    | `M`: min 1766.2, max 2453.7 | The quartiles are 1846 and 1882 |
    | `PT`: min 755.3 | The first quartile is 2723 |

3. Put a `#` in front of `print(df.describe())`. Under it, count the code,
   turn it into NaN and look at the column again.

    ```text
    print((df == -100).sum())
    df["TAU"] = df["TAU"].replace(-100, np.nan)
    print(df.isna().sum())
    print(df["TAU"].describe())
    ```

!!! success "You should now see"
    The same four lines twice:

    ```text
    M          0
    PT         0
    TAU       49
    IPCHI2     0
    dtype: int64
    ```

    and then the summary of `TAU` without the code:

    ```text
    count    91534.000000
    mean         0.000982
    std          0.004382
    min         -0.137153
    25%          0.000185
    50%          0.000272
    75%          0.000605
    max          0.578799
    Name: TAU, dtype: float64
    ```

Work out with the room what the 49 rows did. They are 0.054 % of the file.
Their sum is 49 × (−100) = −4900, and the sum of the other 91 534 values is
89.868. Together: −4810.132 / 91 583 = −0.0525. Without the code the mean is
0.000982 and the standard deviation falls from 2.31 to 0.0044. The median
did not move in its first three digits.

The minimum is still negative: −0.137. That is the next finding.

!!! warning "Watch for"
    `print(df["TAU"] == -100)` instead of the count. It prints a column of
    91 583 times True or False. The sum of a mask is the number of True.

---

### 7. Five questions { #questions }

**1:02 · 16 min**

**Tell the room.** The audit has five questions: completeness, validity,
uniqueness, consistency, units. Each is one line and one count. The room
rewrites `audit.py` so that it prints the whole list, and fills in a table.

1. Replace everything below the line with `read_csv` by:

    ```text
    # Consistency: shape and types as the README says
    print("shape         ", df.shape)
    print("types         ", set(df.dtypes.astype(str)))

    # Completeness: empty cells, and the code -100
    print("empty cells   ", df.isna().sum().to_dict())
    print("cells == -100 ", (df == -100).sum().to_dict())
    df["TAU"] = df["TAU"].replace(-100, np.nan)

    # Validity: values that cannot be true
    print("M <= 0        ", (df["M"] <= 0).sum())
    print("PT <= 0       ", (df["PT"] <= 0).sum())
    print("TAU < 0       ", (df["TAU"] < 0).sum())
    print("IPCHI2 < 0    ", (df["IPCHI2"] < 0).sum())
    print("M outside     ", (~df["M"].between(1800, 1930)).sum())

    # Uniqueness: rows that are there twice
    print("duplicate rows", df.duplicated().sum())

    # Units: a typical value against a known number
    print("median M      ", df["M"].median())
    print("median TAU, ps", df["TAU"].median() * 1000)
    ```

2. Run the script.

    === "macOS"

        ```text
        python3 scripts/audit.py
        ```

    === "Windows"

        ```text
        python scripts/audit.py
        ```

    It prints:

    ```text
    shape          (91583, 4)
    types          {'float64'}
    empty cells    {'M': 0, 'PT': 0, 'TAU': 0, 'IPCHI2': 0}
    cells == -100  {'M': 0, 'PT': 0, 'TAU': 49, 'IPCHI2': 0}
    M <= 0         0
    PT <= 0        0
    TAU < 0        3
    IPCHI2 < 0     0
    M outside      2
    duplicate rows 0
    median M       1864.0781
    median TAU, ps 0.27245521000000006
    ```

3. Look at the rows that broke a rule. Add at the end and run again:

    ```text
    print(df[df["TAU"] < 0])
    print(df[~df["M"].between(1800, 1930)])
    ```

    It prints:

    ```text
                   M          PT       TAU      IPCHI2
    22854  1844.2952  10253.5440 -0.137153   64641.477
    35318  1822.4904   2943.2370 -0.059467  891711.060
    42860  1867.3162   2748.1152 -0.098111  120145.600
                   M          PT       TAU      IPCHI2
    10046  2453.6584    755.2686  0.227682    1.050094
    89859  1766.2096  12493.0220  0.003727  214.383360
    ```

    The number on the left is the label of the row. It is the line of the
    file minus 2: row 10046 is line 10 048.

4. Fill in the table with the room.

    | Question | Finding |
    |--|--|
    | Completeness | No empty cell. 49 cells of `TAU` hold the code −100 |
    | Validity | 3 negative decay times. 2 masses far outside the range of the others |
    | Uniqueness | No row is there twice |
    | Consistency | 91 583 × 4, all `float64`, as the README says |
    | Units | Median `M` 1864.08, the D⁰ mass is 1864.84 MeV/c². Median `TAU` 0.27 ps, the D⁰ lifetime is 0.41 ps |

!!! success "You should now see"
    Twelve lines of counts and two small tables in the terminal, and the
    five findings on the board.

Two points to make. The validity rules come from the meaning of a column: a
decay time is not negative, whatever the file holds. The window 1800 to 1930
is different: it comes from this file, where all other masses lie between
1808.14 and 1920.35. And `TAU < 0` counted 3, not 52: after the replacement
the 49 gaps are NaN, and a comparison with NaN is False.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `TAU < 0` prints 52 | The line with `replace` stands below the validity lines, or is missing |
    | `ValueError: The truth value of a Series is ambiguous` | `not` was typed for `~`, or `and` for `&` |

---

## Part 3 · Clean by script { #part-3 }

**1:18 to 1:39 · sections 8 and 9**

The audit found 49 codes, 3 impossible values and 2 masses outside the
window. The cleaning script turns each finding into a decision, applies it
and reports it.

---

### 8. The cleaning script { #clean }

**1:18 · 12 min**

**Tell the room.** Three decisions, said aloud before any typing. A gap
stays a gap: the 49 rows keep their mass and momentum, and `TAU` becomes
NaN. A row that breaks a rule is removed. Nothing is filled in. Each rule is
one mask with a name, and the script prints the count of each.

1. Select the `scripts` folder, then **New File**, and name it:

    ```text
    clean_d0.py
    ```

    Type into it:

    ```text
    """Clean the LHCb file: data/raw -> data/processed."""
    import numpy as np
    import pandas as pd

    RAW = "data/raw/D0_KPi.csv"
    OUT = "data/processed/d0_clean.csv"

    df = pd.read_csv(RAW)

    # 1. -100 is the file's code for a missing decay time
    n_code = (df["TAU"] == -100).sum()
    df["TAU"] = df["TAU"].replace(-100, np.nan)

    # 2. a decay time is not negative
    bad_tau = df["TAU"] < 0
    # 3. outside the mass window of the sample
    bad_m = ~df["M"].between(1800, 1930)
    # 4. one candidate written twice
    dup = df.duplicated()

    clean = df[~bad_tau & ~bad_m & ~dup]
    clean.to_csv(OUT, index=False, lineterminator="\n")

    print("rows read          ", len(df))
    print("TAU = -100 -> NaN  ", n_code)
    print("TAU < 0, dropped   ", bad_tau.sum())
    print("M outside, dropped ", bad_m.sum())
    print("duplicates, dropped", dup.sum())
    print("rows written       ", len(clean))
    ```

2. Run it.

    === "macOS"

        ```text
        python3 scripts/clean_d0.py
        ```

    === "Windows"

        ```text
        python scripts/clean_d0.py
        ```

!!! success "You should now see"
    ```text
    rows read           91583
    TAU = -100 -> NaN   49
    TAU < 0, dropped    3
    M outside, dropped  2
    duplicates, dropped 0
    rows written        91578
    ```

91 583 − 3 − 2 = 91 578. Every row that left the table is in one line of
the log.

Ask why the masks are written for the bad rows and then turned round with
`~`. Let a student try this line on the projector:

```text
clean = df[df["TAU"] >= 0]
```

It keeps 91 531 rows. The 49 rows with NaN are gone as well, because NaN is
not greater than or equal to anything, and nothing was printed.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `OSError: Cannot save file into a non-existent directory` | The folder `data/processed` is missing. Create it in the Side Bar |
    | `rows written 91529` | A mask was written for the good rows. See the paragraph above |

---

### 9. Check what it did { #check }

**1:30 · 9 min**

**Tell the room.** A cleaning script is trusted after its output has been
looked at and the raw file has been shown to be untouched.

1. Open `data/processed/d0_clean.csv` in VS Code and press `Ctrl+End`
   (macOS `Cmd+↓`). The last line is 91 580 and it is empty: one header
   line and 91 578 rows.

2. Press `Ctrl+F` (macOS `Cmd+F`) and type:

    ```text
    ,,
    ```

    VS Code finds 49 places. The first is in line 343:

    ```text
    1818.1002,2978.644,,9901.186
    ```

    Pandas writes NaN as an empty cell, and `read_csv` reads an empty cell
    as NaN.

3. Compute the checksum of both files.

    === "macOS"

        ```text
        shasum -a 256 data/raw/D0_KPi.csv
        ```

        ```text
        shasum -a 256 data/processed/d0_clean.csv
        ```

    === "Windows"

        ```text
        (Get-FileHash data/raw/D0_KPi.csv).Hash
        ```

        ```text
        (Get-FileHash data/processed/d0_clean.csv).Hash
        ```

    | File | Bytes | SHA-256 |
    |--|--|--|
    | `data/raw/D0_KPi.csv` | 3 926 142 | `25c3c972…c1505136` |
    | `data/processed/d0_clean.csv` | 3 925 641 | `7aa9470b…3bb91b16` |

    `Get-FileHash` writes the same digits in upper case.

4. Delete `d0_clean.csv` in the Side Bar, run the script again and compute
   the checksum again. It is the same.

!!! success "You should now see"
    The same two checksums on every laptop in the room.

The first checksum is the one of the file as downloaded: the script read it
and did not write it. The second is the same on every laptop because the
script, not a person, made the file. Ask two students to read their last
eight characters aloud.

---

## Part 4 · Write it down { #part-4 }

**1:39 to 2:00 · sections 10 and 11**

---

### 10. The cleaning in the README { #readme }

**1:39 · 15 min**

**Tell the room.** The log of the script is the cleaning written as numbers.
It belongs in the README, next to where the file came from. A reader then
knows which rows are not in the cleaned table and why, without running
anything.

1. Open `README.md` and add a section under **Data**:

    ```text
    ## Cleaning

    `scripts/clean_d0.py` reads `data/raw/D0_KPi.csv` and writes
    `data/processed/d0_clean.csv`. The raw file is not changed.

    | Rule | Reason | Rows |
    |--|--|--|
    | `TAU = -100` to empty | code for a missing value | 49 |
    | `TAU < 0` dropped | a decay time is not negative | 3 |
    | `M` outside 1800 to 1930 dropped | outside the mass window | 2 |
    | duplicate rows dropped | one candidate written twice | 0 |

    Rows read: 91 583. Rows written: 91 578. Run on 2026-12-15.

    `scripts/clean.py` makes `data/processed/pendulum.csv` from
    `data/raw/pendulum.csv` by rule: a row without `nr` is dropped.

    Run in the project folder:

    - zsh: `python3 scripts/clean.py` and `python3 scripts/clean_d0.py`
    - PowerShell: `python scripts/clean.py` and `python scripts/clean_d0.py`
    ```

2. In the **Data** section, change the end of the line **Cleaned copy**.
   The words after the checksum list the edits made by hand. Replace them
   by:

    ```text
    Made by `scripts/clean.py`
    ```

    Under it, add the second file:

    ```text
    - **File:** `data/raw/pendulum_run2.csv`, the partner's second series, 2026-12-15
    ```

3. Open the preview with `Ctrl+K`, then `V` (macOS `Cmd+K`, then `V`), and
   read the table.

4. Commit the scripts, the second file and the README.

    ```text
    git add scripts data/raw/pendulum_run2.csv README.md
    ```

    ```text
    git commit -m "Clean both tables by script"
    ```

!!! success "You should now see"
    A **Cleaning** section with four rules in the preview, and the commit in
    the Source Control view.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The table shows as text with `|` signs | An empty line is missing before the table, or the line `|--|--|--|` is missing |
    | Windows: `warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it`, one line per file | A note, not an error: the commit is made. Git on this laptop missed the setting of Seminar 5. Type `git config --global core.autocrlf false` once |

---

### 11. Wrap up { #wrap-up }

**1:54 · 6 min**

Read the list aloud. Ask on the way out which step was hardest.

- `read_csv` is told the separator and the decimal sign. The types of the
  columns then show where a cell is not a number.
- `clean.py` writes the same 97 bytes as Lecture 4's script. On the second
  file Lecture 4's script kept the `Mean` line; `clean.py` dropped it by
  rule and kept the missing time as a gap.
- A script reads `data/raw/` and writes `data/processed/`. The raw file
  keeps its checksum.
- `describe()` first: a minimum or a mean that cannot be measured points at
  a code or an error.
- A code for a missing value is replaced by NaN before anything is
  computed.
- One mask per rule, written for the rows that break it, with a count.
- The same script gives the same bytes on every laptop.
- The counts go into the README.

---

## Optional, if the room is fast { #optional }

Section 12 fits between sections 9 and 10 when the room reaches the end of
section 9 before 1:32. Nothing later in the course reads its table.

---

### 12. A table by group { #group }

**— · 7 min**

**Tell the room.** An analysis starts from the cleaned file, not from the
raw one. `groupby` splits the rows by the values of a column, computes
something for each group and puts the results into one small table. The
column to split by is made first.

1. Select the `scripts` folder, then **New File**, and name it:

    ```text
    tau_by_region.py
    ```

    Type into it:

    ```text
    import numpy as np
    import pandas as pd

    clean = pd.read_csv("data/processed/d0_clean.csv")
    clean["tau_ps"] = clean["TAU"] * 1000
    in_peak = clean["M"].between(1840, 1890)
    clean["region"] = np.where(in_peak, "peak", "side")

    table = clean.groupby("region")["tau_ps"].agg(
        ["size", "count", "median"])
    print(table)
    table.to_csv("results/tau_by_region.csv", lineterminator="\n")
    ```

2. Run it.

    === "macOS"

        ```text
        python3 scripts/tau_by_region.py
        ```

    === "Windows"

        ```text
        python scripts/tau_by_region.py
        ```

3. Commit the script and the table.

    ```text
    git add scripts/tau_by_region.py results/tau_by_region.csv
    ```

    ```text
    git commit -m "Decay time by mass region"
    ```

!!! success "You should now see"
    ```text
             size  count    median
    region                        
    peak    56575  56546  0.308202
    side    35003  34983  0.232948
    ```

`size` counts rows and `count` counts values: 29 of the gaps are in the
peak and 20 beside it. The median decay time is 0.308 ps in the peak region
and 0.233 ps in the sidebands. `results/tau_by_region.csv` has three lines.
Here the index is written on purpose: it holds the names of the regions.

---

## Stretch goals

For students who finish a section early. Answers are given for the
lecturer.

- Read the file with `pd.read_csv(RAW, na_values={"TAU": [-100]})` and
  compare the table with the one made by `replace`, using `a.equals(b)`.
  The answer is `True`.
- Compute the median of `IPCHI2` for the rows with and without a decay
  time: `df.loc[df["TAU"].isna(), "IPCHI2"].median()` and the same with
  `notna()`. The answers are 31465.645 and 6.29089965. The gaps are not a
  random sample of the rows.
- Apply the rule Q1 − 1.5 IQR and Q3 + 1.5 IQR to `M`, with
  `df["M"].quantile(0.25)` for Q1. The fences are 1792.68 and 1934.84, and
  2 rows lie outside. The same rule on `TAU` flags 11 435 rows, 12.5 % of
  the column: it does not suit a column with a long tail.
- Flag instead of dropping. Read `data/processed/d0_clean.csv` into
  `clean`, add `clean["long_tau"] = clean["TAU"] > 0.01` and count it. The answer is
  1452 rows with a decay time above 10 ps.
- Save the cleaned table as Parquet. Install the library with
  `python3 -m pip install pyarrow` (Windows `python`), then
  `clean.to_parquet(...)` with a name that ends in `.parquet`. The file has
  about 3.3 MB against 3.9 MB, and `pd.read_parquet(...)` gives a table
  that `equals` the one written.
- Sort the cleaned table by `PT`, largest first, and print three rows:
  `clean.sort_values("PT", ascending=False).head(3)`. The largest is
  64509.95, in a row whose `TAU` is NaN.
- Count the empty cells of the second pendulum file before cleaning, as on
  slide 16: `RAW` naming `pendulum_run2.csv`, print `df.isna().sum()`
  right after `read_csv`. The answer is 1 in `nr`, 0 in `length_cm` and 1
  in `t10_s`: the summary line and the missing time, found before anything
  is cleaned.
- A student with a dataset of their own points `audit.py` at it: the
  shape, the types, `describe()`, the empty cells per column and the
  duplicate rows. How does the file write a missing value: an empty cell,
  `-999`, `NA`, `n/a`, `?`?

## If students ask for more

| Topic | Week |
|--|--|
| A fixed version of Pandas, so that the script gives the same file next year | 13 (Reproducible Workflows) |
| One command that runs all scripts in the right order | 13 (Reproducible Workflows) |
| A test that fails when the cleaned file changes | 13 (Reproducible Workflows) |

Leave out, even if asked: filling gaps with a mean, Excel files, databases,
Polars.

## Aims practised

♻️ the same bytes on every run · ⚙️ a cleaning that can be run again · 📁 raw data read, never written · 🔧 the same script on every system
