# Seminar 15 — Timing, Memory and a Background Job

**Paired lecture:** 15 Computing Infrastructure & HPC · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student times one sum three ways, works out the
memory of a table before loading it, and runs a job in the background with
a log.

Everything runs on a laptop, in the terminal of VS Code, with Python, NumPy
and Pandas. No cluster and no account anywhere is needed. New today:
`multiprocessing`, `tracemalloc`, and a job in the background of the shell:
`&` in both shells, then `jobs`, `kill` and `tail -f` in `zsh`, `Get-Job`,
`Stop-Job` and `Get-Content -Wait` in PowerShell 7.

## Run sheet

One screen for the front of the room. Each line links to its section.

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · One sum, three ways** · 55 min | | |
| 0:00 | [1. Know the machine](#machine) | `os.cpu_count()`, then the memory | Cores and memory of the laptops on the board |
| 0:08 | [2. A stopwatch around a loop](#loop) | `scripts/time_sum.py`, the loop | The loop timed five times |
| 0:22 | [3. The same sum in NumPy](#numpy) | `M.sum()` added to the script | The factor between the loop and NumPy |
| 0:30 | [4. The same sum on four processes](#pool) | `Pool(4)` added to the script | A time longer than that of the loop |
| 0:43 | [5. A job worth splitting](#split) | `sum_parallel.py --workers 1`, `2`, then `4` | Times for 1, 2 and 4 workers, and a prediction |
| | **Part 2 · Memory before loading** · 28 min | | |
| 0:55 | [6. Estimate, then check](#bytes) | `91583 * 4 * 8`, then `scripts/table_size.py` | 2 930 656 bytes, on paper and in Python |
| 1:05 | [7. The peak while reading](#peak) | `scripts/peak_memory.py` | Two peaks, both larger than the table |
| 1:15 | [8. Will a larger file fit?](#fit) | The bytes and lines of `D0_KPi.csv`, then `4e9 / 42.87` | The largest file each laptop can take |
| | **Part 3 · A job in the background** · 37 min | | |
| 1:23 | [9. A job that reports its progress](#job) | `long_job.py --steps 5`, then `echo $?` or `$LASTEXITCODE` | The job run once in the foreground, and a `0` |
| 1:31 | [10. Into the background](#background) | `python -u ... &`, then `tail -f` or `Get-Content -Wait` | A log followed while the job runs |
| 1:45 | [11. An error in the log](#error) | `--path data/raw/none.csv`, with and without `2>&1` | A traceback found in the log |
| 1:50 | [12. Write down what was measured](#readme) | `README.md`, then the preview | A **Timing** section in the README |
| 1:57 | [13. Wrap up](#wrap-up) | The list of what was learned | |

**If time runs short:** leave out sections 5, 7 and 11, and give the rule of
section 7 (keep three times the table free) in one sentence before section 8.
Each part starts from the project folder as it is, so the session can also
stop after Part 2.

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

    Commands are typed in the terminal of VS Code: `zsh` on macOS,
    PowerShell 7 on Windows, as since [Seminar 4](seminar_04.md#shell).
    Where the two differ, the step has a tab for each: `python3` on macOS,
    `python` on Windows, and in Part 3 the commands that look after a job.
    The Windows outputs were printed by PowerShell 7.6. Keys are written for
    Windows, with macOS in brackets.

    Every time on this page was measured on the lecturer's laptop: a MacBook
    Pro with an Apple M2 Pro (2023), 12 cores, 16 GB of memory, Python 3.13
    and NumPy 2.3. The times in the room will differ. The sums and the byte
    counts will not.

??? info "Before the session"
    For the room: the project folder with `data/raw/D0_KPi.csv`, a `scripts`
    folder and a `results` folder, and a Python that has NumPy and Pandas. A
    student who does not have [`D0_KPi.csv`](../data/D0_KPi.csv) downloads it
    now into `data/raw`. A laptop without NumPy or Pandas installs them now,
    in the terminal of VS Code:

    === "macOS"

        ```text
        python3 -m pip install numpy pandas
        ```

    === "Windows"

        ```text
        python -m pip install numpy pandas
        ```

    For you:

    - Sections 2 to 5 and 10 done once on your own laptop, with your own
      times written down. They replace the times printed on this page.
    - Part 3 done once in `zsh` and once in PowerShell 7: its commands
      differ between the two.
    - The number of cores and the memory of your laptop, to write on the
      board.
    - The first three scripts of the next box on a USB stick, for a student
      who falls behind.

??? info "Files for this seminar"
    A browser saves each file under the name in the second column, the name
    it has in the project. The scripts go into `scripts`.

    | File | Saved as | What it is |
    |--|--|--|
    | [`hpc_time_sum.py`](../data/hpc_time_sum.py){ download="time_sum.py" } | `time_sum.py` | Sections 2 to 4: the finished timing script |
    | [`hpc_sum_parallel.py`](../data/hpc_sum_parallel.py){ download="sum_parallel.py" } | `sum_parallel.py` | Section 5: the long sum on 1, 2 or 4 workers |
    | [`hpc_long_job.py`](../data/hpc_long_job.py){ download="long_job.py" } | `long_job.py` | Sections 9 to 11: the job that reports its progress |
    | [`hpc_job.sh`](../data/hpc_job.sh){ download="job.sh" } | `job.sh` | Stretch goals, macOS: the job script of the lecture |

---

## Part 1 · One sum, three ways { #part-1 }

**0:00 to 0:55 · sections 1 to 5**

One computation, the sum of 91 583 numbers, is done three ways and timed:
as a Python loop, as a NumPy call and on four processes. The room writes
one script, `scripts/time_sum.py`, and adds to it in three steps. Then a
longer job is split over 1, 2 and 4 workers, and the time for 4 is
predicted before it is measured.

---

### 1. Know the machine { #machine }

**0:00 · 8 min**

**Tell the room.** A time means something only together with the machine it
was measured on. Two numbers describe the machine well enough for today:
the number of cores and the amount of memory.

1. Open the project folder in VS Code and a terminal with **Terminal** >
   **New Terminal**. Check that the terminal is in the project folder:

    ```text
    pwd
    ```

2. Ask Python for the number of cores.

    === "macOS"

        ```text
        python3 -c "import os; print(os.cpu_count())"
        ```

    === "Windows"

        ```text
        python -c "import os; print(os.cpu_count())"
        ```

    The lecturer's laptop prints `12`.

3. Find the memory.

    === "macOS"

        Apple menu, **About This Mac**.

    === "Windows"

        Open Task Manager with `Ctrl+Shift+Esc`, tab **Performance**, then
        **Memory**.

4. Check that NumPy is there. Any version from 2.0 on will do.

    === "macOS"

        ```text
        python3 -c "import numpy; print(numpy.__version__)"
        ```

    === "Windows"

        ```text
        python -c "import numpy; print(numpy.__version__)"
        ```

5. Collect on the board the smallest and the largest number of cores in the
   room, and the smallest and the largest memory.

!!! success "You should now see"
    Two ranges on the board, for example 4 to 12 cores and 8 to 32 GB.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `zsh: command not found: python` | On macOS the program is `python3`, as in the macOS tab |
    | `No module named numpy` | The terminal uses another Python than the project. Activate the environment of [Seminar 13](seminar_13.md), `source .venv/bin/activate` (Windows `.venv\Scripts\Activate.ps1`), or install NumPy and Pandas as in the box **Before the session** |
    | Windows: the number of cores is twice what the laptop was sold with | `os.cpu_count()` counts hardware threads. Task Manager shows both, as **Cores** and **Logical processors** |

---

### 2. A stopwatch around a loop { #loop }

**0:08 · 14 min**

**Tell the room.** The sum is written as a loop first, the way Lecture 06
would do it. `time.perf_counter()` is read before and after. The loop is
timed five times, because a single time can be disturbed by whatever else
the laptop is doing.

1. Create a new file in `scripts` and name it:

    ```text
    time_sum.py
    ```

2. Type the first part. The function goes above the line
   `if __name__ == "__main__":`, and everything else is indented under it.
   Section 4 needs it that way.

    ```text
    import time

    import numpy as np

    PATH = "data/raw/D0_KPi.csv"


    def loop_sum(values):
        total = 0.0
        for v in values:
            total += v
        return total


    if __name__ == "__main__":
        start = time.perf_counter()
        M = np.loadtxt(PATH, delimiter=",", skiprows=1, usecols=0)
        elapsed = time.perf_counter() - start
        print(f"read   {elapsed * 1000:8.3f} ms  {len(M)} rows")
        masses = M.tolist()

        for attempt in range(5):
            start = time.perf_counter()
            total = loop_sum(masses)
            elapsed = time.perf_counter() - start
            print(f"loop   {elapsed * 1000:8.3f} ms  {total!r}")
    ```

3. Run it.

    === "macOS"

        ```text
        python3 scripts/time_sum.py
        ```

    === "Windows"

        ```text
        python scripts/time_sum.py
        ```

    On the lecturer's laptop it prints:

    ```text
    read     14.709 ms  91583 rows
    loop      1.580 ms  170720289.9133972
    loop      1.578 ms  170720289.9133972
    loop      1.572 ms  170720289.9133972
    loop      1.531 ms  170720289.9133972
    loop      1.565 ms  170720289.9133972
    ```

4. Ask the room what is the same in the five lines and what is not. The sum
   is the same. The time is not.

5. Ask which of the five times to quote. The smallest: other programs can
   only add time. On the lecturer's laptop the loop costs 1.53 ms.

6. Divide the sum by the number of rows. It is the mean mass.

    === "macOS"

        ```text
        python3 -c "print(170720289.9133972 / 91583)"
        ```

    === "Windows"

        ```text
        python -c "print(170720289.9133972 / 91583)"
        ```

    The answer is `1864.1045817826146`.

!!! success "You should now see"
    Six lines, and the sum `170720289.9133972` on every laptop. The times
    differ from laptop to laptop. Collect the smallest loop time of three or
    four students on the board.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `FileNotFoundError` | The terminal is not in the project folder. `pwd`, then `cd` |
    | `IndentationError` | The lines under `if __name__` are indented by four spaces, the lines under `for` by eight |
    | A sum that ends in other digits | A typing slip in `usecols=0` or `skiprows=1` |

---

### 3. The same sum in NumPy { #numpy }

**0:22 · 8 min**

**Tell the room.** Lecture 07 replaced loops by array operations. Here the
same sum is timed both ways in one script, so that the factor belongs to
this laptop.

1. Add a second block at the end of the script, indented like the first.

    ```text
        for attempt in range(5):
            start = time.perf_counter()
            total = M.sum()
            elapsed = time.perf_counter() - start
            print(f"numpy  {elapsed * 1000:8.3f} ms  {float(total)!r}")
    ```

2. Run the script again.

    === "macOS"

        ```text
        python3 scripts/time_sum.py
        ```

    === "Windows"

        ```text
        python scripts/time_sum.py
        ```

    Five more lines appear:

    ```text
    numpy     0.043 ms  170720289.9134
    numpy     0.021 ms  170720289.9134
    numpy     0.019 ms  170720289.9134
    numpy     0.018 ms  170720289.9134
    numpy     0.018 ms  170720289.9134
    ```

3. Each student divides the smallest loop time by the smallest NumPy time.
   On the lecturer's laptop: 1.531 / 0.018 = 85.

4. Divide both times by the 91 583 rows: 16.7 ns per row for the loop, 0.2
   ns for NumPy.

5. Ask why the first NumPy line is the slowest. Code and data are not yet in
   the cache of the processor on the first run.

!!! success "You should now see"
    A factor on every laptop, most between 50 and 150, and the board shows a
    few of them next to the machine they came from.

The sums of the two methods differ in their last digits: `…9133972` against
`…9134`. Both are correct to 14 digits. The additions are done in another
order, and every addition of floats rounds.

---

### 4. The same sum on four processes { #pool }

**0:30 · 13 min**

**Tell the room.** The laptop has several cores, and the loop used one. A
pool of four worker processes splits the rows into four lists and adds up
each list on its own core. The room predicts the result before running it.
Most will say: four times faster.

1. Add one line to the imports at the top of the script.

    ```text
    from multiprocessing import Pool
    ```

2. Add a third block at the end, indented like the others.

    ```text
        chunks = [masses[i::4] for i in range(4)]
        for attempt in range(5):
            start = time.perf_counter()
            with Pool(4) as pool:
                parts = pool.map(loop_sum, chunks)
            total = sum(parts)
            elapsed = time.perf_counter() - start
            print(f"pool   {elapsed * 1000:8.3f} ms  {total!r}")
    ```

3. Say what the lines do. `masses[i::4]` is every fourth row, starting at
   row `i`. `Pool(4)` starts four more Python processes. `pool.map` gives
   each of them one list and collects the four partial sums.

4. Ask for predictions, then run the script.

    === "macOS"

        ```text
        python3 scripts/time_sum.py
        ```

    === "Windows"

        ```text
        python scripts/time_sum.py
        ```

    The last five lines:

    ```text
    pool    109.817 ms  170720289.91340062
    pool    100.515 ms  170720289.91340062
    pool    111.831 ms  170720289.91340062
    pool    108.677 ms  170720289.91340062
    pool     91.396 ms  170720289.91340062
    ```

5. Read the result with the room. Four processes take 91 ms, the loop took
   1.53 ms: 60 times slower. Starting a Python process and importing NumPy
   in it takes about 60 ms, and that has to happen for every worker before
   any number is added.

!!! success "You should now see"
    Fifteen lines of timing, and a pool time that is far longer than the
    loop time on every laptop. On Windows it is often longer still.

The sum has changed again in its last digits. Four partial sums added
together round at other places than one long sum.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Tracebacks without end, with `RuntimeError: An attempt has been made to start a new process` | The pool lines are not under `if __name__ == "__main__":`. Stop with `Ctrl+C`, several times if needed, and indent them |
    | `NameError: name 'Pool' is not defined` | The import line of step 1 is missing |

---

### 5. A job worth splitting { #split }

**0:43 · 12 min**

**Tell the room.** Splitting costs about a tenth of a second before any
work is done. It pays for a job that takes much longer than that. The next
script does the same loop 1 200 times over, 110 million additions, and
takes the number of workers from the command line.

1. Download [`hpc_sum_parallel.py`](../data/hpc_sum_parallel.py){ download="sum_parallel.py" }
   and save it in `scripts` as:

    ```text
    sum_parallel.py
    ```

    Open it and read it with the room: the function `sum_passes` reads the
    file and loops over it, and each worker gets its share of the 1 200
    passes.

2. Run it with one worker, then with two.

    === "macOS"

        ```text
        python3 scripts/sum_parallel.py --workers 1
        ```

        ```text
        python3 scripts/sum_parallel.py --workers 2
        ```

    === "Windows"

        ```text
        python scripts/sum_parallel.py --workers 1
        ```

        ```text
        python scripts/sum_parallel.py --workers 2
        ```

    On the lecturer's laptop:

    ```text
    workers  1  passes 1200  time  1.964 s  sum 204864347896.70938
    workers  2  passes 1200  time  1.044 s  sum 204864347896.07877
    ```

3. Work out the two parts of the time on the board, with the times of your
   own laptop. The model is T(N) = Ts + Tp / N.

    ```text
    Tp = 2 x (T(1) - T(2)) = 2 x (1.964 - 1.044) = 1.840 s
    Ts = T(1) - Tp         = 1.964 - 1.840       = 0.124 s
    ```

4. Predict the time for four workers before running it.

    ```text
    T(4) = Ts + Tp / 4 = 0.124 + 0.460 = 0.584 s
    ```

5. Run it and compare.

    === "macOS"

        ```text
        python3 scripts/sum_parallel.py --workers 4
        ```

    === "Windows"

        ```text
        python scripts/sum_parallel.py --workers 4
        ```

    ```text
    workers  4  passes 1200  time  0.586 s  sum 204864347895.95145
    ```

!!! success "You should now see"
    Three times on every laptop and a prediction next to the third. On the
    lecturer's laptop the prediction is off by 2 ms. Each student runs each
    line twice or three times and keeps the smallest time.

The serial part is 0.124 s of 1.964 s, or 6.3 %. By Amdahl's law no number
of cores makes this job more than 1 / 0.063 = 16 times faster.

!!! warning "Watch for"
    A laptop with two cores gains nothing from four workers, and its
    measured time for four is longer than the prediction. That is the right
    result for that laptop: the model assumes a free core for every worker.

---

## Part 2 · Memory before loading { #part-2 }

**0:55 to 1:23 · sections 6 to 8**

Time was the first thing to measure. Memory is the second. A script that
needs more memory than the laptop has does not get slower by a factor. It
stops, or it stops the laptop. The size of the table in memory is worked out
on paper, checked against the loaded table, and compared with the peak
while reading.

---

### 6. Estimate, then check { #bytes }

**0:55 · 10 min**

**Tell the room.** A table of numbers needs rows × columns × bytes per
value. A float64 has 8 bytes and a float32 has 4, as in Lecture 03. The room
does the product on paper first.

1. Ask for the product: 91 583 rows, 4 columns, 8 bytes. Then check it.

    === "macOS"

        ```text
        python3 -c "print(91583 * 4 * 8)"
        ```

    === "Windows"

        ```text
        python -c "print(91583 * 4 * 8)"
        ```

    The answer is `2930656`, about 2.9 MB.

2. Create a new file in `scripts` and name it:

    ```text
    table_size.py
    ```

    Type:

    ```text
    import numpy as np
    import pandas as pd

    PATH = "data/raw/D0_KPi.csv"

    table = np.loadtxt(PATH, delimiter=",", skiprows=1)
    print(table.shape, table.dtype, table.nbytes)
    print(table.astype(np.float32).nbytes)

    df = pd.read_csv(PATH)
    print(df.memory_usage())
    ```

3. Run it.

    === "macOS"

        ```text
        python3 scripts/table_size.py
        ```

    === "Windows"

        ```text
        python scripts/table_size.py
        ```

    ```text
    (91583, 4) float64 2930656
    1465328
    Index        132
    M         732664
    PT        732664
    TAU       732664
    IPCHI2    732664
    dtype: int64
    ```

4. Read the output with the room. `nbytes` is the product of step 1, to the
   byte. As float32 the table takes half. Pandas keeps every column as an
   array of 91 583 × 8 = 732 664 bytes, and 132 bytes for the row numbers.

5. Compare with the file on disk: 3 926 142 bytes of text. In memory the
   table is smaller than its text file, by the factor 2 930 656 / 3 926 142 =
   0.75.

!!! success "You should now see"
    The number `2930656` twice: once from the product and once from
    `nbytes`.

---

### 7. The peak while reading { #peak }

**1:05 · 10 min**

**Tell the room.** The table is not all the memory a script needs. While a
file is read, the text and the numbers are in memory at the same moment.
`tracemalloc`, a module that comes with Python, reports the largest amount
that was in use.

1. Create a new file in `scripts` and name it:

    ```text
    peak_memory.py
    ```

    Type:

    ```text
    import tracemalloc

    import numpy as np
    import pandas as pd

    PATH = "data/raw/D0_KPi.csv"

    tracemalloc.start()
    table = np.loadtxt(PATH, delimiter=",", skiprows=1)
    current, peak = tracemalloc.get_traced_memory()
    print(f"loadtxt   table {table.nbytes}  peak {peak}")

    before = current
    tracemalloc.reset_peak()
    df = pd.read_csv(PATH)
    current, peak = tracemalloc.get_traced_memory()
    print(f"read_csv  table {df.memory_usage().sum()}  peak {peak - before}")
    ```

2. Run it.

    === "macOS"

        ```text
        python3 scripts/peak_memory.py
        ```

    === "Windows"

        ```text
        python scripts/peak_memory.py
        ```

    ```text
    loadtxt   table 2930656  peak 3107323
    read_csv  table 2930788  peak 5916301
    ```

3. Divide each peak by its table. NumPy needed 1.06 times the table, Pandas
   2.0 times.

4. Give the rule: keep three times the table free. One for the table, one
   for a working copy such as `M - M.mean()`, one for the reader and for
   whatever else runs.

!!! success "You should now see"
    Two peaks, both larger than their table. The last digits of the peaks
    vary from run to run and from laptop to laptop.

---

### 8. Will a larger file fit? { #fit }

**1:15 · 8 min**

**Tell the room.** The estimate is made before a file is opened, from its
size alone. The room does it for a file of 4 GB with the same four columns,
and then each student for their own laptop.

1. Measure the bytes per row of text, as in
   [Seminar 4, section 7](seminar_04.md#sizes): first the size of the file
   in bytes, then the number of lines.

    === "macOS"

        ```text
        wc -c data/raw/D0_KPi.csv
        ```

        ```text
         3926142 data/raw/D0_KPi.csv
        ```

        ```text
        wc -l data/raw/D0_KPi.csv
        ```

        ```text
           91584 data/raw/D0_KPi.csv
        ```

    === "Windows"

        ```text
        (Get-Item data/raw/D0_KPi.csv).Length
        ```

        ```text
        3926142
        ```

        ```text
        (Get-Content data/raw/D0_KPi.csv).Count
        ```

        ```text
        91584
        ```

    3 926 142 bytes / 91 584 lines = 42.87 bytes per line.

2. Rows in a file of 4 GB.

    === "macOS"

        ```text
        python3 -c "print(4e9 / 42.87)"
        ```

    === "Windows"

        ```text
        python -c "print(4e9 / 42.87)"
        ```

    About 93 million rows.

3. Memory for the table: the text size times 0.75, which is 3.0 GB. Three
   times that is 9.0 GB.

4. Ask who could load this file. A laptop with 16 GB can. A laptop with 8 GB
   cannot.

5. Each student works out the largest text file of this kind for their own
   laptop: memory / 3 / 0.75. For 16 GB it is 7.1 GB of text, for 8 GB it is
   3.6 GB.

6. Ask what to do with a file that is too large. Read only the columns that
   are needed (`usecols=0` is a quarter of the table), read them as float32,
   or read the file in pieces and keep only the sum.

!!! success "You should now see"
    One number per student: the largest file of this kind that their laptop
    can load.

---

## Part 3 · A job in the background { #part-3 }

**1:23 to 2:00 · sections 9 to 13**

A job that takes an hour should not need a person watching it. The room
starts a job of half a minute in the background and learns the four things
that go with it: the log, following the log, stopping the job, and finding
an error afterwards.

---

### 9. A job that reports its progress { #job }

**1:23 · 8 min**

**Tell the room.** The job of this part adds up the mass column 300 times
per step, for 60 steps, and prints one line per step with the time of day.
It stands for any long analysis.

1. Download [`hpc_long_job.py`](../data/hpc_long_job.py){ download="long_job.py" }
   and save it in `scripts` as:

    ```text
    long_job.py
    ```

    Open it and find three things with the room: the two options `--steps`
    and `--path`, the `print` inside the loop, and the last line, which
    prints `done`.

2. Run it in the foreground with five steps.

    === "macOS"

        ```text
        python3 scripts/long_job.py --steps 5
        ```

    === "Windows"

        ```text
        python scripts/long_job.py --steps 5
        ```

    ```text
    18:44:19  read 91583 rows from data/raw/D0_KPi.csv
    18:44:20  step  1 of 5    0.5 s
    18:44:20  step  2 of 5    0.9 s
    18:44:21  step  3 of 5    1.4 s
    18:44:21  step  4 of 5    1.9 s
    18:44:22  step  5 of 5    2.3 s
    18:44:22  done  mean of M = 1864.1046
    ```

3. Ask the shell how the script ended: its exit status.

    === "macOS"

        ```text
        echo $?
        ```

    === "Windows"

        ```text
        $LASTEXITCODE
        ```

    It prints `0`: the script ended without an error. Any other number
    means an error.

4. From the time per step, estimate the full job of 60 steps. On the
   lecturer's laptop: 60 × 0.47 s = 28 s.

!!! success "You should now see"
    Seven lines, a `0`, and an estimate for 60 steps on every laptop.

---

### 10. Into the background { #background }

**1:31 · 14 min**

**Tell the room.** `&` at the end of a command starts it in the background:
the prompt comes back at once. Both shells have it. `> results/run.log`
sends what the script prints into a file, and `2>&1` sends error messages
to the same file. PowerShell runs such a command as a *job*, in a second
PowerShell of its own, and has its own commands to list and stop it. The
first attempt goes wrong on purpose.

1. Start the job in the background.

    === "macOS"

        ```text
        python3 scripts/long_job.py > results/run.log 2>&1 &
        ```

        `zsh` prints the job number and a process number, such as
        `[1] 26267`.

    === "Windows"

        ```text
        python scripts/long_job.py > results/run.log 2>&1 &
        ```

        PowerShell prints a table of one row: the job's `Id` 1, its name
        `Job1`, and the state `Running`.

2. Look at the log, twice, a few seconds apart. `cat` is the same word in
   both shells.

    ```text
    cat results/run.log
    ```

    It prints nothing. Ask the room why.

3. List the jobs, then stop the job.

    === "macOS"

        ```text
        jobs
        ```

        ```text
        [1]  + running    python3 scripts/long_job.py > results/run.log 2>&1
        ```

        ```text
        kill %1
        ```

    === "Windows"

        ```text
        Get-Job
        ```

        The row of job 1 shows `Running`.

        ```text
        Stop-Job 1
        ```

    Look at the log once more:

    ```text
    cat results/run.log
    ```

    The log is still empty.

4. Explain. When its output goes into a file, Python collects it in a buffer
   and writes it when the buffer is full or the script ends. A stopped
   script loses its buffer. `python -u` writes every line at once.

5. Start the job again with `-u`, and follow the log. The lines appear one
   by one. `Ctrl+C` ends the following. The job goes on.

    === "macOS"

        ```text
        python3 -u scripts/long_job.py > results/run.log 2>&1 &
        ```

        ```text
        tail -f results/run.log
        ```

    === "Windows"

        ```text
        python -u scripts/long_job.py > results/run.log 2>&1 &
        ```

        This job gets the `Id` 3: PowerShell also numbers the part inside
        each job.

        ```text
        Get-Content results/run.log -Wait
        ```

6. Check that the job is still there: `jobs` (Windows `Get-Job`). Wait for
   it to end, and read the end of the log.

    === "macOS"

        ```text
        tail -n 3 results/run.log
        ```

    === "Windows"

        ```text
        Get-Content results/run.log -Tail 3
        ```

    ```text
    18:27:10  step 59 of 60   27.4 s
    18:27:10  step 60 of 60   27.9 s
    18:27:10  done  mean of M = 1864.1046
    ```

!!! success "You should now see"
    A log of 62 lines whose last line says `done`. This command counts them:

    === "macOS"

        ```text
        wc -l results/run.log
        ```

        ```text
              62 results/run.log
        ```

    === "Windows"

        ```text
        (Get-Content results/run.log).Count
        ```

        ```text
        62
        ```

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The log stays empty while the job runs | The job was started without `-u`. `Ctrl+C`, stop the job, start it again with `-u` |
    | macOS: `kill: %1: no such job` | The job has ended, or it was started in another terminal. `jobs` lists what this terminal has |
    | Windows: `Stop-Job: The command cannot find a job with the job ID 1.` | `Get-Job` lists the jobs of this terminal with their `Id`. Use the `Id` of the row that shows `Running` |
    | Windows: `Get-Content` is still waiting after `done` | It follows the file until it is stopped. `Ctrl+C` |
    | A job ends as soon as its terminal is closed | Correct, in both shells. The stretch goals show how a job outlives its terminal on macOS |

---

### 11. An error in the log { #error }

**1:45 · 5 min**

**Tell the room.** A job that fails at night has nobody at the terminal. Its
error message has to be in the log. That is what `2>&1` is for.

1. Start the job with a file name that does not exist, and without `2>&1`.

    === "macOS"

        ```text
        python3 scripts/long_job.py --path data/raw/none.csv > results/run.log
        ```

    === "Windows"

        ```text
        python scripts/long_job.py --path data/raw/none.csv > results/run.log
        ```

    The traceback appears in the terminal. Look at the log:

    ```text
    cat results/run.log
    ```

    It prints nothing.

2. Run the same line with `2>&1` at the end. Nothing appears in the
   terminal.

    === "macOS"

        ```text
        python3 scripts/long_job.py --path data/raw/none.csv > results/run.log 2>&1
        ```

    === "Windows"

        ```text
        python scripts/long_job.py --path data/raw/none.csv > results/run.log 2>&1
        ```

3. Read the last line of the log, then ask the shell how the script ended.

    === "macOS"

        ```text
        tail -n 1 results/run.log
        ```

        ```text
        echo $?
        ```

        ```text
        FileNotFoundError: data/raw/none.csv not found.
        0
        ```

        The `0` belongs to `tail`, the last program. Run the failing line
        again and then `echo $?` at once: it prints `1`.

    === "Windows"

        ```text
        Get-Content results/run.log -Tail 1
        ```

        ```text
        $LASTEXITCODE
        ```

        ```text
        FileNotFoundError: data/raw/none.csv not found.
        1
        ```

        `$LASTEXITCODE` is set by programs only. `Get-Content` is a part
        of PowerShell, so the `1` is still the one Python left.

!!! success "You should now see"
    The line with `FileNotFoundError` in the log, and the room can say which
    stream it came through.

---

### 12. Write down what was measured { #readme }

**1:50 · 7 min**

**Tell the room.** A timing belongs in the README, together with the
machine. Whoever runs the project on another laptop then knows what to
expect.

1. Open `README.md` and add a section. The room fills in its own machine and
   its own times.

    ```text
    ## Timing

    Machine: MacBook Pro, Apple M2 Pro (2023), 12 cores, 16 GB.
    Python 3.13, NumPy 2.3. Smallest of five runs.

    | Sum of column M, 91 583 rows | Time |
    |--|--|
    | Python loop | 1.53 ms |
    | NumPy | 0.018 ms |
    | 4 processes | 91 ms |

    The table takes 2 930 656 bytes in memory: 91 583 x 4 x 8.

    A long run is started in the background, with a log
    (on macOS `python3`):
    `python -u scripts/long_job.py > results/run.log 2>&1 &`
    ```

2. Open the preview with `Ctrl+K`, then `V` (macOS `Cmd+K`, then `V`) and
   read the section.

!!! success "You should now see"
    A **Timing** section with a table of three rows in the preview.

---

### 13. Wrap up { #wrap-up }

**1:57 · 3 min**

Read the list aloud. Ask on the way out which result was the least
expected.

- A time is measured several times and the smallest is kept. It is quoted
  with the machine.
- The same sum takes 1.5 ms as a Python loop and 0.02 ms in NumPy.
- A pool of processes costs about a tenth of a second to start. It pays for
  jobs that take seconds or more.
- Two measurements give the serial part of a job. Amdahl's law then predicts
  the time on more workers.
- A table of numbers takes rows × columns × bytes per value. Reading it
  takes up to twice that, and three times the table should be free.
- `echo $?` (Windows `$LASTEXITCODE`) tells how the last program ended:
  `0` is success.
- `python -u script.py > run.log 2>&1 &` (macOS `python3`) runs a job in the
  background with a log, in both shells. `zsh` lists, follows and stops it
  with `jobs`, `tail -f` and `kill %1`; PowerShell with `Get-Job`,
  `Get-Content -Wait` and `Stop-Job`.
- The sum changes in its last digits with the order of the additions.

---

## Stretch goals

For students who finish a section early. Answers are given for the lecturer,
with the times of the lecturer's laptop.

- Time the loop over the array `M` itself instead of the list `masses`:
  `loop_sum(M)`. The answer is 4.7 ms, three times slower than the list.
  Every value has to be made into an object before it is added.
- Compute the sum with `math.fsum(masses)` and with `sum(masses)`. Both give
  `170720289.9134`, the correctly rounded sum, in Python 3.12 and later.
- Save the table with `np.save("data/processed/D0_KPi.npy", table)` and time
  `np.load` on that file. The answer is 0.26 ms against 17.6 ms for
  `np.loadtxt`, and a file of 2 930 784 bytes: the table and a header of 128
  bytes.
- Run `sum_parallel.py` with as many workers as the laptop has cores, and
  with twice as many. On the lecturer's laptop 8 and 12 workers both take
  0.41 s, and 24 workers take about 0.7 s: more workers than cores only add
  starting time.
- Give every run a folder of its own. The log lands in a folder such as
  `results/run_2026-10-04_1826`. Type the three lines one by one.

    === "macOS"

        ```text
        RUN=results/run_$(date +%Y-%m-%d_%H%M)
        mkdir -p "$RUN"
        python3 -u scripts/long_job.py > "$RUN/run.log" 2>&1 &
        ```

    === "Windows"

        ```text
        $RUN = "results/run_$(Get-Date -Format yyyy-MM-dd_HHmm)"
        mkdir $RUN
        python -u scripts/long_job.py > "$RUN/run.log" 2>&1 &
        ```

- macOS: start the job with `nohup` in front, close the terminal with the
  bin icon, open a new one and read the log. The job has run to `done`.
  Without `nohup` it stops when the terminal closes. On Windows a job of
  PowerShell always ends with its terminal.

    ```text
    nohup python3 -u scripts/long_job.py > results/run.log 2>&1 &
    ```

- macOS: download the job script of the lecture,
  [`hpc_job.sh`](../data/hpc_job.sh){ download="job.sh" }, save it as
  `scripts/job.sh` and run it with `bash`, which every Mac has. For `bash`
  the `#SBATCH` lines are comments. The script prints a start line, the
  line of `sum_parallel.py` and a done line. It first activates the
  environment `.venv` of [Seminar 13](seminar_13.md), so that `python`
  is found; without that folder it stops at once with
  `.venv/bin/activate: No such file or directory`. On Windows read the
  script against the slide of the lecture instead: PowerShell does not run
  it.

    ```text
    SLURM_JOB_ID=1 SLURM_CPUS_PER_TASK=2 bash scripts/job.sh
    ```

A student who has a dataset of their own can repeat the session on it:

- Time the reading of the dataset and one computation on it, five times
  each. If the computation is a loop, time it as an array operation too.
- Estimate the memory of the table from rows, columns and bytes per value
  before loading it. Then check with `nbytes` or with
  `df.memory_usage(deep=True)`. For a column of text the option `deep=True`
  is needed, and the result will be larger than the estimate.
- Give an analysis script a progress line per step and a last line that
  says `done`. Run it in the background with a log, and follow the log.

## If students ask for more

| Topic | What to say |
|--|--|
| Threads instead of processes | They share memory and start faster, but only one thread at a time runs Python code. They help when a script waits for downloads or for a disk |
| A table larger than memory, without writing the pieces by hand | The libraries Polars and Dask do the reading in pieces themselves |
| A graphics card from Python | The library CuPy has the functions of NumPy and computes them on the card |
| An account on a real cluster | Research groups get one through their institute. The job script of the lecture is the form such a cluster expects |

Leave out altogether, even if asked: MPI, writing code for a GPU, opening an
account with a cloud provider.

## Aims practised

⚙️ a job that runs without its author and reports what it does · 🔧 one job run in the background from `zsh` and from PowerShell, and the job script a cluster expects · 📁 a table sized before it is loaded · ♻️ timings written down with the machine
