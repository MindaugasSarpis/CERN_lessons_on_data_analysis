# Seminar 7 — The Whole File in Python

**Paired lecture:** 07 Python for Data & NumPy · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student reads `D0_KPi.csv` into one NumPy array,
masks its missing values, and has a script that writes the numbers to
`results/summary.txt`.

The tools are the editor, the terminal of VS Code (`zsh` on macOS,
PowerShell 7 on Windows) and Python, as in Seminar 6. The new one is NumPy,
installed in section 4. The file is first read with plain Python, so that
the room has seen what an array replaces.

## Run sheet

One screen for the front of the room. Each line links to its section.

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · The file with plain Python** · 35 min | | |
| 0:00 | [1. Read the header and the first row](#first-row) | `scripts/read_csv.py`, run in the terminal | Two lists of strings on the screen |
| 0:10 | [2. Read a column with a function](#column) | `def read_column(path, index):` | A list of 91 583 floats |
| 0:22 | [3. A mean and a count by loop](#loop) | `def mean(values):`, then a loop over `TAU` | The mean of `M`, and 49 missing values |
| | **Part 2 · NumPy** · 30 min | | |
| 0:35 | [4. Install NumPy](#install) | `python -m pip install numpy` (macOS `python3`) | `import numpy` works |
| 0:45 | [5. Read the file into an array](#loadtxt) | `np.loadtxt(...)` with `skiprows=1` | An array of shape `(91583, 4)` |
| 0:55 | [6. Columns and their numbers](#columns) | `M.mean(), M.std(), M.min(), M.max()` | Mean, standard deviation, minimum and maximum of `M` and `TAU` |
| | **Part 3 · Masks and counts** · 35 min | | |
| 1:05 | [7. Mask the missing values](#mask) | `mask = TAU != -100` | 91 534 valid rows, and a mean that makes sense |
| 1:17 | [8. Count rows with a condition](#window) | `(M > 1840) & (M < 1890)` | The number of rows in a mass window |
| 1:27 | [9. Count in bins, and time both scripts](#histogram) | `np.histogram(M, bins=20, range=(1815, 1915))` | 20 counts, and two times in ms |
| | **Part 4 · Write the result** · 20 min | | |
| 1:40 | [10. Write the numbers to a file](#write) | `open("results/summary.txt", "w")` | `results/summary.txt` |
| 1:50 | [11. A note in the README](#readme) | `## Summary numbers` in `README.md`, then a commit | A **Summary numbers** section, committed |
| 1:55 | [12. Wrap up](#wrap-up) | The list of what was learned | |

**If time runs short:** do section 3 as a demonstration on the projector,
and leave out the timing, step 5 of section 9. Sections 10 and 11 stay: they
are the result of the session.

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

    Commands are typed in the terminal of VS Code, in the project folder,
    and ended with `Enter`. Where the two shells differ, the step has a tab
    for **macOS** (`zsh`) and one for **Windows** (PowerShell 7), as in
    [Seminar 4](seminar_04.md): the program is `python3` on macOS and
    `python` on Windows. A command that is the same in both, such as
    `git ...`, stands in one block.

??? info "Before the session"
    For the room: the project folder with `data/raw/D0_KPi.csv`, under Git
    since [Seminar 5](seminar_05.md), and Python running from the terminal
    of VS Code, as installed in [Seminar 4](seminar_04.md). A student who
    does not have [`D0_KPi.csv`](../data/D0_KPi.csv) downloads it now and
    drags it onto the `raw` folder.

    For you:

    - NumPy installed on your own laptop, and section 4 done once, so that
      you know what `pip` prints on your system.
    - A network connection for the room. `pip` downloads up to 13 MB. If the
      network of the room is weak, a phone hotspot is enough.
    - Sections 5 to 9 done once. The numbers on your screen must be the
      numbers on this page.

---

## Part 1 · The file with plain Python { #part-1 }

**0:00 to 0:35 · sections 1 to 3**

The room reads the file with what Python has built in. This is the slow
way, and it is done first so that everyone has seen what an array replaces.

---

### 1. Read the header and the first row { #first-row }

**0:00 · 10 min**

**Tell the room.** A CSV file is text. The `csv` module of Python splits
each line at the commas and gives a list of strings. `pathlib` builds the
path so that the same script runs on Windows and on macOS.

1. In the Side Bar select the `scripts` folder, then **New File**, and name
   it:

    ```text
    read_csv.py
    ```

2. Type into the file:

    ```text
    import csv
    from pathlib import Path

    path = Path("data") / "raw" / "D0_KPi.csv"
    print(path.exists())

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        first = next(reader)

    print(header)
    print(first)
    ```

3. Open the terminal with **Terminal** > **New Terminal** and run the
   script.

    === "macOS"

        ```text
        python3 scripts/read_csv.py
        ```

    === "Windows"

        ```text
        python scripts/read_csv.py
        ```

4. Add a line at the end, run again, and ask the room what it will print
   before you press Enter.

    ```text
    print(first[0] + first[1])
    ```

    It prints `1880.6493000.9534`. The two values are strings, and `+`
    joins strings.

5. Change that line to the one below and run again. It prints `4881.6024`.

    ```text
    print(float(first[0]) + float(first[1]))
    ```

!!! success "You should now see"
    ```text
    True
    ['M', 'PT', 'TAU', 'IPCHI2']
    ['1880.649', '3000.9534', '0.00041271152', '1299.1675']
    4881.6024
    ```

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `False`, then `FileNotFoundError` | The terminal is not in the project folder. Run `pwd`. Go there with `cd`, or open the project folder with **File** > **Open Folder...** |
    | Windows: `Python was not found; run without arguments to install from the Microsoft Store, …` | A stand-in of Windows answered, not Python. See [Seminar 4, section 4](seminar_04.md#shell), Watch for. Until it is fixed, `py` works in place of `python` |
    | `IndentationError` | The lines under `with` start with four spaces. Select them and press `Tab` |

---

### 2. Read a column with a function { #column }

**0:10 · 12 min**

**Tell the room.** A loop over the reader gives every row. One column is
collected into a list, and each value is converted with `float`. The steps
go into a function, so that the second column costs one more line.

1. Delete everything below the two `import` lines and type:

    ```text
    def read_column(path, index):
        values = []
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                values.append(float(row[index]))
        return values


    path = Path("data") / "raw" / "D0_KPi.csv"
    M = read_column(path, 0)
    print(len(M), "rows")
    print(M[:3])
    ```

2. Run the script. It stops with a traceback. Read it with the room from
   the bottom:

    ```text
    ValueError: could not convert string to float: 'M'
    ```

    The first line of the file is the header, and `float("M")` has no
    number to return. The traceback names two places: the line of the
    script that called the function, and the line inside the function that
    failed.

3. Add one line to the function, between `reader = csv.reader(f)` and the
   `for` line, with the same indentation as both:

    ```text
            next(reader)
    ```

    It takes the header off before the loop starts.

4. Run the script again.

!!! success "You should now see"
    ```text
    91583 rows
    [1880.649, 1860.6599, 1913.8755]
    ```

**Say it in these words.** A path and a column number go into the function,
a list of floats comes out. The names `values`, `f`, `reader` and `row`
exist only inside it.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `TypeError: object of type 'NoneType' has no len()` | The `return values` line is missing |
    | `1 rows` | `return values` stands inside the `for` loop. It has four spaces, not twelve |
    | `IndexError: list index out of range` | The file has an empty line at its end that was added by hand. Download the file again |

---

### 3. A mean and a count by loop { #loop }

**0:22 · 13 min**

**Tell the room.** With the column in a list, a mean is a sum and a
division. A count is a loop with an `if`. Both are written by hand once.

1. Add a second function under `read_column`, above the line that starts
   with `path`:

    ```text
    def mean(values):
        total = 0.0
        for v in values:
            total += v
        return total / len(values)
    ```

2. Test it on a case that can be checked in the head. Add at the end of the
   script and run. It prints `5.0`.

    ```text
    print(mean([2, 4, 9]))
    ```

3. Now use it on the column. Add:

    ```text
    print("mean M:", mean(M))
    ```

4. Read the third column and count the rows in which it is not `-100`. Add:

    ```text
    TAU = read_column(path, 2)
    n_valid = 0
    for t in TAU:
        if t != -100:
            n_valid += 1
    print("valid TAU:", n_valid, " missing:", len(TAU) - n_valid)
    ```

5. Run the script.

!!! success "You should now see"
    ```text
    91583 rows
    [1880.649, 1860.6599, 1913.8755]
    5.0
    mean M: 1864.1045817826146
    valid TAU: 91534  missing: 49
    ```

The mean of the mass column is 1864.10 MeV/c², at the D⁰ peak. The 49 rows
are the 49 lines that `grep -c` and `Select-String` counted for `,-100` in
[Seminar 4, section 8](seminar_04.md#count).

Ask what the script needs for the smallest mass, the largest mass and the
mean of the valid decay times: one more loop for each.

---

## Part 2 · NumPy { #part-2 }

**0:35 to 1:05 · sections 4 to 6**

NumPy holds a whole column, or the whole table, in one array. A sum, a mean
or a comparison is then one call, and the loop runs in compiled code.

---

### 4. Install NumPy { #install }

**0:35 · 10 min**

**Tell the room.** NumPy is not part of Python. It is installed once per
computer with `pip`, the installer that comes with Python. `pip` downloads
the library from the Python Package Index, pypi.org.

1. In the terminal, type the command for your system and press Enter.

    === "macOS"

        ```text
        python3 -m pip install numpy
        ```

    === "Windows"

        ```text
        python -m pip install numpy
        ```

2. Wait for the download. Near the end the output reads
   `Successfully installed numpy-` followed by a version number, such as
   `2.5.3`. A notice about a new release of pip may follow it.

3. Check it.

    === "macOS"

        ```text
        python3 -c "import numpy; print(numpy.__version__)"
        ```

    === "Windows"

        ```text
        python -c "import numpy; print(numpy.__version__)"
        ```

!!! success "You should now see"
    A version number: `2.` and two more numbers.

**Say it in these words.** `python -m pip` (`python3 -m pip` on macOS)
runs the `pip` that belongs to this Python, so the library lands where this
Python looks for it. A lone `pip install numpy` can belong to another Python
on the same computer.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | A notice that a new release of pip is available | Nothing. It is not an error |
    | Windows: `Python was not found; …` | As in section 1. Until it is fixed: `py -m pip install numpy` |
    | `No module named pip` | `python3 -m ensurepip` on macOS, `python -m ensurepip` on Windows, then the install command again |
    | `error: externally-managed-environment` | This Python belongs to the system or to Homebrew. Install Python from python.org and use that one |
    | The check prints a version, and the **Run** button of VS Code says `No module named 'numpy'` | VS Code runs another Python. Press `Ctrl+Shift+P` (macOS `Cmd+Shift+P`), type `Python: Select Interpreter` and pick the one the terminal uses |
    | The download does not start | Use a phone hotspot. The download is up to 13 MB |

---

### 5. Read the file into an array { #loadtxt }

**0:45 · 10 min**

**Tell the room.** `np.loadtxt` reads a text file of numbers into one
array. It has to be told two things about this file: the sign between the
values, and that the first line is not data.

1. In the Side Bar select the `scripts` folder, then **New File**, and name
   it:

    ```text
    summary.py
    ```

2. Type into the file:

    ```text
    import numpy as np

    data = np.loadtxt("data/raw/D0_KPi.csv", delimiter=",")
    print(data.shape)
    ```

3. Run it.

    === "macOS"

        ```text
        python3 scripts/summary.py
        ```

    === "Windows"

        ```text
        python scripts/summary.py
        ```

    It stops:

    ```text
    ValueError: could not convert string 'M' to float64 at row 0, column 1.
    ```

    This is the header again. NumPy names the row and the column of the
    field it could not convert.

4. Add `skiprows=1` to the call, and two more lines:

    ```text
    data = np.loadtxt("data/raw/D0_KPi.csv", delimiter=",", skiprows=1)
    print(data.shape)
    print(data.dtype)
    print(data[0])
    ```

5. Run it again.

!!! success "You should now see"
    ```text
    (91583, 4)
    float64
    [1.8806490e+03 3.0009534e+03 4.1271152e-04 1.2991675e+03]
    ```

Read the three lines with the room. The shape is rows first, then columns:
91 583 rows and 4 columns. The `dtype` is `float64`, the 64-bit float of
Lecture 03, for every value of the array. `data[0]` is the first row. NumPy
prints a row of mixed sizes in powers of ten: `1.8806490e+03` is 1880.649.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `ModuleNotFoundError: No module named 'numpy'` | The script runs with another Python than the one of section 4. See the table there |
    | `FileNotFoundError` | The terminal is not in the project folder |
    | `could not convert string '1880.649,3000.9534,…'` | `delimiter=","` is missing |

---

### 6. Columns and their numbers { #columns }

**0:55 · 10 min**

**Tell the room.** An array has no column names. The script gives each
column a name, with the unit in a comment. Each column then answers `mean`,
`std`, `min` and `max` without a loop.

1. Delete the three `print` lines and add:

    ```text
    M = data[:, 0]         # mass, MeV/c^2
    PT = data[:, 1]        # transverse momentum, MeV/c
    TAU = data[:, 2]       # decay time, ns; -100 = missing
    IPCHI2 = data[:, 3]    # chi^2 of the impact parameter

    print("M  ", M.mean(), M.std(), M.min(), M.max())
    print("TAU", TAU.mean(), TAU.std(), TAU.min(), TAU.max())
    ```

2. Run the script.

3. Compare the mean of `M` with the one of section 3,
   `1864.1045817826146`. The two agree in the first 13 digits. NumPy adds
   the values in another order, and every addition of floats rounds.

4. The room does this step alone: add the same line for `PT`. The answer is
   a mean of 3448.93 and a largest value of 64 509.95 MeV/c.

!!! success "You should now see"
    ```text
    M   1864.1045817826453 25.564956548991027 1766.2096 2453.6584
    TAU -0.05252210273908192 2.3124877358319695 -100.0 0.5787994
    ```

Ask the room to read the second line as a physicist would. The mean decay
time is negative, and the smallest decay time is −100 ns. Neither can be
right.

**Say it in these words.** The minimum and the maximum of a column are
printed before its mean is believed.

---

## Part 3 · Masks and counts { #part-3 }

**1:05 to 1:40 · sections 7 to 9**

A comparison on an array gives an array of `True` and `False`, a mask. A
mask counts rows and selects rows. This is how the missing values are taken
out, and how any other selection is made.

---

### 7. Mask the missing values { #mask }

**1:05 · 12 min**

**Tell the room.** In this file `-100` in the column `TAU` means that the
decay time could not be computed. It is a mark, not a measurement. Lecture
04 showed what the 49 marks do, on the slide *What 49 Rows Do to a Mean*,
and Seminar 4 got the two means from two files, the raw one and
`D0_valid.csv`. Here one array gives both. The mask `TAU != -100` is `True`
in the rows that have a value.

1. Add to `summary.py`:

    ```text
    mask = TAU != -100
    print(mask.sum(), (~mask).sum())
    ```

2. Run the script. The new line reads `91534 49`. In a sum `True` counts
   as 1, so `mask.sum()` is the number of rows with a value. `~mask` is the
   opposite mask.

3. Use the mask as an index. Add and run:

    ```text
    print("TAU", TAU[mask].mean(), TAU[mask].std(), TAU[mask].min())
    ```

4. Put the two means beside the slide *What 49 Rows Do to a Mean* of
   Lecture 04: −0.0525 ns with the marks, +0.00098 ns without. They are
   the numbers of `column_stats.py` in
   [Seminar 4, section 13](seminar_04.md#list), now from one array and one
   mask. The sum on that slide, 49 × (−100) / 91 583 = −0.0535, is the
   shift the marks cause.

5. The room does this step alone: print the two shapes below. The answers
   are `(91534,)` and `(91534, 4)`. A mask made from one column selects the
   same rows in any other.

    ```text
    print(M[mask].shape, data[mask].shape)
    ```

!!! success "You should now see"
    From the line added in step 3:

    ```text
    TAU 0.000981802006321804 0.004381973120438549 -0.13715266
    ```

The mean of the valid decay times is 0.00098 ns, about 1 ps. With the 49
marks it was −0.0525 ns: the wrong sign and 53 times too large, from 0.05 %
of the rows.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `AttributeError: 'bool' object has no attribute 'sum'` | `TAU` is a list, as in Part 1. This is `summary.py`, with `TAU = data[:, 2]` |
    | The count is 91583 and 0 | The comparison reads `TAU != 100`. The mark is `-100` |

---

### 8. Count rows with a condition { #window }

**1:17 · 10 min**

**Tell the room.** Two masks are combined with `&` for *and*, `|` for *or*
and `~` for *not*. Each comparison stands in its own brackets.

1. Add and run:

    ```text
    window = (M > 1840) & (M < 1890)
    print(window.sum(), window.mean())
    ```

    It prints `56577 0.6177674895995982`. The mean of a mask is the
    fraction of `True`: 61.8 % of the rows have a mass within 25 MeV/c² of
    1865.

2. Leave the brackets out once, and run:

    ```text
    window = M > 1840 & M < 1890
    ```

    The script stops with a `TypeError`. `&` is applied before `>`, so
    Python tries `1840 & M` first. Put the brackets back.

3. Replace `&` by `and` once, and run:

    ```text
    window = (M > 1840) and (M < 1890)
    ```

    The script stops with `ValueError: The truth value of an array with
    more than one element is ambiguous`. `and` works on single values. Put
    `&` back.

4. The room does this step alone: how many rows have `PT` above 5000, and
   how many of those lie in the window?

    ```text
    fast = PT > 5000
    print(fast.sum(), (window & fast).sum())
    ```

!!! success "You should now see"
    As the last line:

    ```text
    7263 5886
    ```

---

### 9. Count in bins, and time both scripts { #histogram }

**1:27 · 13 min**

**Tell the room.** A mean and a standard deviation say little about the
shape of a column. `np.histogram` cuts a range into intervals of equal
width, the bins, and counts the values in each. The counts are the last
numbers a plot needs.

1. Add and run:

    ```text
    counts, edges = np.histogram(M, bins=20, range=(1815, 1915))
    print(counts)
    print(len(counts), len(edges))
    ```

2. Read the output with the room. Twenty bins of 5 MeV/c² have 21 edges.
   The counts rise from about 3500 to 8931 and fall again.

3. Find the fullest bin. Add and run:

    ```text
    i = counts.argmax()
    print(i, edges[i], edges[i + 1], counts[i])
    ```

    It prints `9 1860.0 1865.0 8931`: the bin from 1860 to 1865 MeV/c².

4. Ask how many rows were not counted. Add and run. 339 rows have a mass
   outside the range.

    ```text
    print(len(M) - counts.sum())
    ```

5. Time the mean in both scripts. At the top of `summary.py` add:

    ```text
    import time
    ```

    and at the end:

    ```text
    t0 = time.perf_counter()
    m = M.mean()
    t1 = time.perf_counter()
    print("NumPy:", (t1 - t0) * 1000, "ms")
    ```

    Do the same in `read_csv.py`: `import time` at its top, and at its
    end the loop version:

    ```text
    t0 = time.perf_counter()
    m = mean(M)
    t1 = time.perf_counter()
    print("loop:", (t1 - t0) * 1000, "ms")
    ```

    Run both scripts.

!!! success "You should now see"
    From `summary.py`:

    ```text
    [3500 3622 3623 3643 3741 3722 4224 5083 7124 8931 8565 6512 4876 3938
     3602 3378 3412 3397 3287 3064]
    20 21
    9 1860.0 1865.0 8931
    339
    ```

    and two times that differ from laptop to laptop.

On an Apple M2 Pro the loop takes about 1.6 ms and NumPy about 0.07 ms.
Collect a few pairs from the room and write the factors on the board.

**Say it in these words.** Both are fast for 91 583 rows. The factor
matters for a file a thousand times larger, and for a step that is repeated
a thousand times.

---

## Part 4 · Write the result { #part-4 }

**1:40 to 2:00 · sections 10 to 12**

The numbers of Parts 2 and 3 go into a file, and the README says how the
file is made.

---

### 10. Write the numbers to a file { #write }

**1:40 · 10 min**

**Tell the room.** Numbers on the screen are gone when the terminal is
closed. The script writes them to a file in `results`, with their units.
The file can be made again at any time by running the script.

1. In `summary.py`, delete the `print` lines of sections 6 to 9 and the
   timing lines. Keep the lines that define `data`, the four columns,
   `mask` and `window`.

2. Add at the end:

    ```text
    lines = [
        f"rows {len(data)}",
        f"rows with a valid TAU {mask.sum()}",
        f"M mean {M.mean():.2f} std {M.std():.2f} MeV/c^2",
        f"TAU mean {TAU[mask].mean() * 1000:.3f} ps",
        f"rows with 1840 < M < 1890: {window.sum()}",
    ]
    with open("results/summary.txt", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    print("written: results/summary.txt")
    ```

3. Run the script and open `results/summary.txt` from the Side Bar.

4. Run the script a second time. The file is the same: `"w"` replaces it.

!!! success "You should now see"
    In `results/summary.txt`:

    ```text
    rows 91583
    rows with a valid TAU 91534
    M mean 1864.10 std 25.56 MeV/c^2
    TAU mean 0.982 ps
    rows with 1840 < M < 1890: 56577
    ```

The script reads `data/raw/D0_KPi.csv` and does not change it. The decay
time is multiplied by 1000 before it is written, so that the file says
0.982 ps and not 0.001 ns.

---

### 11. A note in the README { #readme }

**1:50 · 5 min**

**Tell the room.** A result file is worth as much as the note that says how
it was made.

1. Open `README.md` and add a section:

    ```text
    ## Summary numbers

    `results/summary.txt` is written by `scripts/summary.py`
    from `data/raw/D0_KPi.csv`. It needs NumPy:
    `python3 -m pip install numpy` on macOS,
    `python -m pip install numpy` on Windows.

    Rows with `TAU = -100` have no decay time. They are left out
    of the mean of `TAU` and kept in the numbers for `M`.
    ```

2. Save the two scripts, the result and the README as one commit, in the
   Source Control view or typed in the terminal:

    ```text
    git add scripts results README.md
    ```

    ```text
    git commit -m "Summary numbers of D0_KPi.csv with NumPy"
    ```

!!! success "You should now see"
    The new section in the preview, and no changed files in the Source
    Control view.

---

### 12. Wrap up { #wrap-up }

**1:55 · 5 min**

Read the list aloud. Ask on the way out which step was hardest.

- `csv.reader` gives every row as a list of strings. `float` makes numbers
  of them.
- A function takes values in through its parameters and gives one back with
  `return`. It is tested on a small case first.
- NumPy is installed once with `python -m pip install numpy`, `python3` on
  macOS.
- `np.loadtxt` with `delimiter` and `skiprows` reads a file of numbers into
  one array. Its `shape` is rows, then columns.
- A comparison on an array gives a mask. A mask counts rows with `.sum()`
  and selects them as an index.
- A mark for a missing value is masked before a mean is taken. The minimum
  and the maximum of a column show such a mark.
- `np.histogram` gives the counts in bins, and one more edge than counts.

---

## Stretch goals

For students who finish a section early. Answers are given for the
lecturer.

- Print the median of `M` with `np.median(M)`, and the median and the mean
  of `IPCHI2`. The answers are 1864.0781, then 6.30 and 457.5: a few very
  large values carry the mean of `IPCHI2`.
- Find the row with the largest mass. `M.argmax()` is 10046, and
  `data[10046]` is a row with `M` = 2453.6584.
- Count the valid decay times that are negative:
  `(TAU[mask] < 0).sum()` is 3.
- Compare the array with the file. `data.nbytes` is 2 930 656 bytes:
  32 bytes per row, four values of 8 bytes. The file on disk has
  3 926 142 bytes, about 43 per line, as `wc -c` and `Get-Item` measured
  in [Seminar 4, section 7](seminar_04.md#sizes). As text a value takes as
  many bytes as it has characters, in an array always 8.
  `data.astype(np.float32).nbytes` is 1 465 328, half again.
- Compute *g* from the pendulum table without a loop. Read
  `data/processed/pendulum.csv` with `np.loadtxt`, then
  `g = 4 * np.pi**2 * (p[:, 0] / 100) / (p[:, 1] / 10)**2`. The nine values
  lie between 9.70 and 9.93, and `g.mean()` is 9.795.
- Read the file as received, `data/raw/pendulum.csv`, with
  `csv.reader(f, delimiter=";")`. Convert the length with `float(row[1])`
  and the time with `float(row[2].replace(",", "."))` inside `try`, and
  count the rows that raise `ValueError`. The answer is 9 rows read and 2
  skipped, the header and the line with the mean. The mean of the nine
  times is 15.14.
- A student who already has a dataset of their own reads it the same way:
  `np.loadtxt` if every field is a number, `read_column` and
  `np.array(values)` if it has columns of text. Then find how the file
  marks a missing value, an empty field, a word or a number such as `-999`,
  and mask those rows.

## If students ask for more

| Topic | Week |
|--|--|
| Drawing the 20 counts as a histogram | 8 (Data Visualisation) |
| What a standard deviation says, and the uncertainty of a mean | 9 (Probability & Statistics) |
| Tables with column names and missing values: Pandas | 12 (Pandas & Data Cleaning) |
| A script that takes the file name as an argument | 13 (Reproducible Workflows) |

## Aims practised

📁 raw data read by script, never edited · ⚙️ one script from file to result · ♻️ the result file can be made again · 🔧 the same code on every system
