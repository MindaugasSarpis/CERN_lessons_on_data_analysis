# Seminar 12 — Clean a Table by Script

**Paired lecture:** 12 Pandas & Data Cleaning · **Format:** follow-along · **~120 min**
in class

The seminar has four parts, in this order.

1. **A small table by script.** The room installs Pandas and writes a script
   that cleans the pendulum table. Its output is compared, byte by byte, with
   the copy that was cleaned by hand in the editor.
2. **Audit the data file.** A second script asks five questions of
   `D0_KPi.csv` and prints a count for each.
3. **Clean by script.** A third script applies the decisions, writes the
   cleaned table to `data/processed/` and prints what it removed.
4. **Write it down.** The rules and the counts go into the README.

The new tool of the session is Pandas. Everything else is known: the project
folder, the terminal, running a script, NumPy masks, checksums.

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
Windows the terminal is Git Bash. The page writes `python`. On macOS it is
`python3`. Where a command differs between systems, both forms are given.

| Clock | Section | The room ends with |
|--|--|--|
| | **Part 1 · A small table by script** · 35 min | |
| 0:00 | [1. Install Pandas](#install) | A version number printed |
| 0:08 | [2. Read the pendulum file](#read) | Three columns, two with the right type |
| 0:20 | [3. Clean it and compare](#compare) | A file identical to the hand-cleaned one |
| | **Part 2 · Audit the data file** · 40 min | |
| 0:35 | [4. Shape and types](#types) | 91 583 rows, four columns of `float64` |
| 0:43 | [5. The summary and the code −100](#code) | 49 codes turned into NaN |
| 0:58 | [6. Five questions](#questions) | A count for each question |
| | **Part 3 · Clean by script** · 30 min | |
| 1:15 | [7. The cleaning script](#clean) | `data/processed/d0_clean.csv` and a log |
| 1:28 | [8. Check what it did](#check) | The raw file unchanged, the output the same on every laptop |
| 1:38 | [9. A table by group](#group) | `results/tau_by_region.csv` |
| | **Part 4 · Write it down** · 15 min | |
| 1:45 | [10. The cleaning in the README](#readme) | A **Cleaning** section with the counts |
| 1:55 | [11. Wrap up](#wrap-up) | The homework known |

In a 90-minute slot, stop after section 8 and go to the wrap-up. Sections 9
and 10 are then done at home.

## Prerequisites

For the room: the project folder with these three files, and Python with
NumPy.

| File | From |
|--|--|
| `data/raw/pendulum.csv` | The table as received: semicolons, decimal commas. [Download](../data/pendulum_raw.csv){ download="pendulum.csv" } |
| `data/processed/pendulum.csv` | The copy cleaned by hand in the editor. [Download](../data/pendulum.csv){ download="pendulum.csv" } |
| `data/raw/D0_KPi.csv` | [Download](../data/D0_KPi.csv) |

For you, before the session:

- Sections 1 to 8 done once on your own laptop.
- The hand-cleaned file of your own laptop checked: line ending `LF` in the
  Status Bar, 97 bytes. Section 3 compares against it.
- The network of the room tried: section 1 downloads about 10 MB. If it is
  slow, ask the room a week ahead to do section 1 at home.

## Part 1 · A small table by script { #part-1 }

**0:00 to 0:35 · sections 1 to 3**

The pendulum table was cleaned by hand: one line deleted, two replacements,
one column removed. The room now writes the same four edits as a script and
proves that the result is the same file.

## 1. Install Pandas { #install }

**0:00 · 8 min**

Pandas is a library for tables. A table in Pandas has columns with names,
one type per column, and cells that may be empty. It is installed with
`pip`, the program that comes with Python and fetches libraries.

1. Open the project folder in VS Code and select **Terminal** >
   **New Terminal**.

2. Install Pandas.

    ```text
    Windows (Git Bash)   python -m pip install pandas
    macOS                python3 -m pip install pandas
    ```

    Near the end of the output stands a line that begins with
    `Successfully installed`.

3. Check that Python finds it.

    ```text
    python -c "import pandas; print(pandas.__version__)"
    ```

You should now see a version number, for example `3.0.6`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `No module named pip` | Windows: `py -m pip install pandas` |
    | `externally-managed-environment` | The Python is the one of the system, not the one from python.org. Run the installer from python.org again |
    | The version starts with `2.` | Nothing. The one difference on this page is named where it occurs |

## 2. Read the pendulum file { #read }

**0:08 · 12 min**

`read_csv` turns a text file into a table. It has to be told two things that
a spreadsheet takes from the settings of the computer: the character between
the values and the decimal sign. The room finds both by reading the file
three times.

1. Select the `scripts` folder, then **New File**, and type
   `clean_pendulum.py`. Type:

    ```text
    import pandas as pd

    RAW = "data/raw/pendulum.csv"

    df = pd.read_csv(RAW)
    print(df.shape)
    ```

2. Save and run it.

    ```text
    python scripts/clean_pendulum.py
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

You should now see:

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
    | `ModuleNotFoundError: No module named 'pandas'` | `python` and `pip` belong to two installations. Install with `python -m pip`, as in section 1 |

## 3. Clean it and compare { #compare }

**0:20 · 15 min**

Each hand edit becomes one line. The two replacements are already done: they
are the two options of `read_csv`. What is left is the line with the mean,
the column of row numbers and the type of `length_cm`. Then the output is
compared with the file that was cleaned by hand.

1. In the Side Bar select `data/processed/pendulum.csv`, press `F2` (macOS
   `Enter`) and rename it `pendulum_by_hand.csv`. The script is about to
   write a file with the old name.

2. Replace the two `print` lines at the end of the script by:

    ```text
    df = df[df["nr"].notna()]
    df = df.drop(columns="nr")
    df["length_cm"] = df["length_cm"].astype(int)
    print(df.dtypes)

    OUT = "data/processed/pendulum.csv"
    df.to_csv(OUT, index=False)
    print(len(df), "rows written to", OUT)
    ```

3. Run the script.

    ```text
    length_cm      int64
    t10_s        float64
    dtype: object
    9 rows written to data/processed/pendulum.csv
    ```

4. Compare the two files in VS Code. Select `pendulum.csv` in the Side Bar,
   hold `Ctrl` (macOS `Cmd`) and select `pendulum_by_hand.csv`. Right-click
   and select **Compare Selected**. Two lines are marked:

    ```text
    by hand     80,17.90    90,19.10
    by script   80,17.9     90,19.1
    ```

    17.90 and 17.9 are the same number, and Pandas writes the shorter text.
    In the hand-cleaned file the zero said that the time was read to 0.01 s.

5. Say how the numbers are written. Change the line with `to_csv`:

    ```text
    df.to_csv(OUT, index=False, float_format="%.2f",
              lineterminator="\n")
    ```

    `"%.2f"` writes two decimals in every row. `"\n"` ends every line with
    one byte on every system. Without it Windows writes two.

6. Delete the line `print(df.dtypes)`, run the script and compare the
   checksums of the two files.

    ```text
    Git Bash, Linux   sha256sum data/processed/pendulum*.csv
    macOS             shasum -a 256 data/processed/pendulum*.csv
    ```

You should now see two lines that begin with the same 64 characters,
`be05af03…fff0870b`. The two files are identical: 97 bytes each.

Say it in these words: the script does what the hands did, and this is the
proof. From now on the hand-cleaned file is not needed. Delete
`pendulum.csv`, run the script, and it is back.

The script, complete:

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
print(len(df), "rows written to", OUT)
```

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The checksums differ, and **Compare Selected** shows no difference | The hand-cleaned file has `CRLF` line endings, or no line break after its last line. Open it and read the Status Bar. The two files hold the same table and are not the same bytes |
    | `ValueError: invalid literal for int() with base 10: 'mean'` | The line with `notna()` is missing or stands below `astype` |
    | The file begins with `,length_cm,t10_s` | `index=False` is missing |

## Part 2 · Audit the data file { #part-2 }

**0:35 to 1:15 · sections 4 to 6**

Nobody can read 91 583 rows. An audit asks the table a fixed list of
questions, and every answer is a count. Nothing is changed in this part: the
script only reads and prints.

## 4. Shape and types { #types }

**0:35 · 8 min**

The first look at a table is its size and the type of each column. Line 1
of the file becomes the names of the columns.

1. Select the `scripts` folder, then **New File**, and type `audit.py`.
   Type:

    ```text
    import numpy as np
    import pandas as pd

    df = pd.read_csv("data/raw/D0_KPi.csv")
    print(df.shape)
    print(df.dtypes)
    print(df.head())
    ```

2. Run it with `python scripts/audit.py`.

You should now see:

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

## 5. The summary and the code −100 { #code }

**0:43 · 15 min**

`describe()` gives eight numbers for each column. Reading them is the
fastest way to find a value that cannot be a measurement. Give the room two
minutes with the table before you say anything.

1. Replace the line `print(df.head())` by `print(df.describe())` and run
   the script.

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

You should now see the same four lines twice, and then the summary of `TAU`
without the code:

```text
M          0
PT         0
TAU       49
IPCHI2     0
dtype: int64
```

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

## 6. Five questions { #questions }

**0:58 · 17 min**

The audit has five questions: completeness, validity, uniqueness,
consistency, units. Each is one line and one count. The room rewrites
`audit.py` so that it prints the whole list, and fills in a table.

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

You should now see twelve lines of counts and two small tables in the
terminal, and the five findings on the board.

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

## Part 3 · Clean by script { #part-3 }

**1:15 to 1:45 · sections 7 to 9**

The audit found 49 codes, 3 impossible values and 2 masses outside the
window. The cleaning script turns each finding into a decision, applies it
and reports it.

## 7. The cleaning script { #clean }

**1:15 · 13 min**

Three decisions, said aloud before any typing. A gap stays a gap: the 49
rows keep their mass and momentum, and `TAU` becomes NaN. A row that breaks
a rule is removed. Nothing is filled in. Each rule is one mask with a name,
and the script prints the count of each.

1. Select the `scripts` folder, then **New File**, and type `clean_d0.py`.
   Type:

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

2. Run it with `python scripts/clean_d0.py`.

You should now see:

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
`~`. Let a student try `clean = df[df["TAU"] >= 0]` on the projector: it
keeps 91 531 rows. The 49 rows with NaN are gone as well, because NaN is
not greater than or equal to anything, and nothing was printed.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `OSError: Cannot save file into a non-existent directory` | The folder `data/processed` is missing. Create it in the Side Bar |
    | `rows written 91529` | A mask was written for the good rows. See the paragraph above |

## 8. Check what it did { #check }

**1:28 · 10 min**

A cleaning script is trusted after its output has been looked at and the
raw file has been shown to be untouched.

1. Open `data/processed/d0_clean.csv` in VS Code and press `Ctrl+End`
   (macOS `Cmd+↓`). The last line is 91 580 and it is empty: one header
   line and 91 578 rows.

2. Press `Ctrl+F` (macOS `Cmd+F`) and type `,,`. VS Code finds 49 places.
   The first is in line 343:

    ```text
    1818.1002,2978.644,,9901.186
    ```

    Pandas writes NaN as an empty cell, and `read_csv` reads an empty cell
    as NaN.

3. Compute the checksum of both files.

    ```text
    Git Bash, Linux   sha256sum data/raw/D0_KPi.csv
                      sha256sum data/processed/d0_clean.csv
    macOS             shasum -a 256 data/raw/D0_KPi.csv
                      shasum -a 256 data/processed/d0_clean.csv
    ```

    | File | Bytes | SHA-256 |
    |--|--|--|
    | `data/raw/D0_KPi.csv` | 3 926 142 | `25c3c972…c1505136` |
    | `data/processed/d0_clean.csv` | 3 925 641 | `7aa9470b…bb91b16` |

4. Delete `d0_clean.csv` in the Side Bar, run the script again and compute
   the checksum again. It is the same.

You should now see the same two checksums on every laptop in the room.

The first checksum is the one of the file as downloaded: the script read it
and did not write it. The second is the same on every laptop because the
script, not a person, made the file. Ask two students to read their last
eight characters aloud.

## 9. A table by group { #group }

**1:38 · 7 min**

An analysis starts from the cleaned file, not from the raw one. `groupby`
splits the rows by the values of a column, computes something for each
group and puts the results into one small table. The column to split by is
made first.

1. Create `scripts/summary.py`:

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

2. Run it with `python scripts/summary.py`.

You should now see:

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

## Part 4 · Write it down { #part-4 }

**1:45 to 2:00 · sections 10 and 11**

## 10. The cleaning in the README { #readme }

**1:45 · 10 min**

The log of the script is the cleaning written as numbers. It belongs in the
README, next to where the file came from. A reader then knows which rows
are not in the cleaned table and why, without running anything.

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

    `scripts/clean_pendulum.py` makes `data/processed/pendulum.csv`
    from `data/raw/pendulum.csv`.
    ```

2. In the **Data** section, delete the line that lists the edits made by
   hand to the pendulum file. The script now says what was done.

3. Open the preview with `Ctrl+K`, then `V`, and read the table.

4. Commit the scripts and the README.

    ```text
    git add scripts README.md results/tau_by_region.csv
    git commit -m "Clean both tables by script"
    ```

You should now see a **Cleaning** section with four rules in the preview,
and the commit in the Source Control view.

## 11. Wrap up { #wrap-up }

**1:55 · 5 min**

Put the tasks of the next section on the projector and read them aloud. Ask
on the way out which step was hardest.

What the room has learned:

- `read_csv` is told the separator and the decimal sign. The types of the
  columns then show where a cell is not a number.
- A script reads `data/raw/` and writes `data/processed/`. The raw file
  keeps its checksum.
- `describe()` first: a minimum or a mean that cannot be measured points at
  a code or an error.
- A code for a missing value is replaced by NaN before anything is
  computed.
- One mask per rule, written for the rows that break it, with a count.
- The same script gives the same bytes on every laptop.
- The counts go into the README.

## Next steps, at home

**45 min, before the next session**

1. Write `scripts/audit_mine.py` for your own dataset. Print the shape, the
   types, `describe()`, the number of empty cells per column and the number
   of duplicate rows.

2. Find out how your file writes a missing value: an empty cell, `-999`,
   `NA`, `n/a`, `?`. Count the cells and turn them into NaN.

3. Write one validity rule for each numeric column, from what the column
   means, and count the rows that break it.

4. Write `scripts/clean_mine.py`. It reads from `data/raw/`, writes to
   `data/processed/` and prints a log like the one of section 7.

5. Add a **Cleaning** section for your dataset to the README.

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
- Flag instead of dropping. In `summary.py` add
  `clean["long_tau"] = clean["TAU"] > 0.01` and count it. The answer is
  1452 rows with a decay time above 10 ps.
- Save the cleaned table as Parquet. Install the library with
  `python -m pip install pyarrow`, then `clean.to_parquet(...)` with a name
  that ends in `.parquet`. The file has about 3.3 MB against 3.9 MB, and
  `pd.read_parquet(...)` gives a table that `equals` the one written.
- Sort the cleaned table by `PT`, largest first, and print three rows:
  `clean.sort_values("PT", ascending=False).head(3)`. The largest is
  64509.95, in a row whose `TAU` is NaN.

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
