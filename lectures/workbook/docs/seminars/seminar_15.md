# Seminar 15 · Computing

**Paired lecture:** 15 Computing Infrastructure & HPC · **Format:** type-along tutorial, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's goal:** How long does it take, and how to make it faster? Every student times the rebuild and one slow script,
finds which part of it is slow, makes it 17 times faster on one core,
compares that with more cores, runs it as a background job, and writes the
times into the README.

Everything is typed in the terminal of VS Code (zsh on macOS, Git Bash on
Windows), in today's folder `weather-s15`, with its environment `s15` active.
No cluster and no account is needed. In the blocks, a line that starts with
`$` is typed in the terminal, and every other line is what comes back.

**If time runs short:** stop after section 8 and do section 11; Part 4 is
optional on a laptop.

??? info "Before the session"
    - **Room:** VS Code and Miniforge (Seminar 4, or the Setup page), and
      internet: today's folder is 0.6 MB, its environment about 45
      packages. Nothing from an earlier seminar is needed.
    - **You:** nothing to prepare. Every time on this page was measured on
      one machine (Linux); times in the room differ, often by a factor of
      two. On macOS and Windows each worker of Part 3 starts a fresh Python,
      so the times with workers are higher there. The results of the scripts
      do not differ.
    - **Keys** are written for Windows, macOS in brackets. Every line typed is
      the same on both systems.

---

## Part 1 · How long does it take? { #part-1 }

<!-- 0:00 to 0:25 -->

Before making anything faster, measure it.

Further reading: [Python's `time` module](https://docs.python.org/3/library/time.html).

---

### 1. Get today's folder { #pull }

<!-- 0:00 · 10 min -->

One zip holds everything: the weather data, the hill station's file, the scripts and tests that `run_all.py` runs, today's two scripts `warmest.py` and `warmest_job.sh`, and an `environment.yml`.

1. On the [Releases page](https://github.com/MindaugasSarpis/weather-project/releases),
   under **Assets**, click `weather-s15.zip`.
2. In a terminal (VS Code: **View** > **Terminal**), unpack it into the
   home folder and look inside.

    ```text
    $ unzip -q ~/Downloads/weather-s15.zip -d ~
    $ cd ~/weather-s15
    $ ls
    README.md  data  environment.yml  run_all.py  scripts  tests
    ```

    Safari unpacks a download by itself: then type
    `mv ~/Downloads/weather-s15 ~` instead of `unzip`.

3. **File** > **Open Folder...** > `weather-s15`. Then **View** >
   **Terminal**: the new terminal starts in the folder.
4. Make the environment of this seminar, `s15`, from the file: Python,
   NumPy, pandas and pytest. It ends with the line that switches it on.

    ```text
    $ conda env create -n s15 -f environment.yml
    Channels:
     - conda-forge
    ...
    #     $ conda activate s15
    ```

5. Switch it on; the prompt starts with `(s15)`.

    ```text
    $ conda activate s15
    ```

6. How many cores this computer has: `os.cpu_count()` asks the operating
   system.

    ```text
    $ python -c "import os; print(os.cpu_count())"
    128
    ```

    This run was on a server. A laptop prints 4 to 16.

**Check:** `(s15)` in the prompt; the number of cores on the board for the room.

---

### 2. Time the rebuild { #rebuild }

<!-- 0:10 · 5 min -->

`time` in front of a command runs it and then prints how long it took.

1. Time `run_all.py`, which rebuilds every result of the project;
   `> /dev/null` throws its output away.

    === "macOS"

        ```text
        $ time python run_all.py > /dev/null
        python run_all.py > /dev/null  0.63s user 0.08s system 100% cpu 0.709 total
        ```

    === "Windows"

        ```text
        $ time python run_all.py > /dev/null

        real    0m0.662s
        user    0m0.544s
        sys     0m0.119s
        ```

    zsh's `0.709 total` and Git Bash's `real` are the time on the clock;
    `user` and `sys` the processor's. Your times differ.

**Check:** a time on the clock below one second.

---

### 3. Time it five times, keep the smallest { #noise }

<!-- 0:15 · 10 min -->

Other programs take the processor now and then and only add time, so time five times and keep the smallest.

1. The rebuild, five times: `for ... do ...; done` repeats what is between.

    ```text
    $ for i in 1 2 3 4 5; do time python run_all.py > /dev/null; done
    python run_all.py > /dev/null  0.57s user 0.08s system 100% cpu 0.650 total
    python run_all.py > /dev/null  0.62s user 0.08s system 100% cpu 0.701 total
    python run_all.py > /dev/null  0.56s user 0.10s system 100% cpu 0.658 total
    python run_all.py > /dev/null  0.62s user 0.08s system 100% cpu 0.702 total
    python run_all.py > /dev/null  0.58s user 0.11s system 100% cpu 0.683 total
    ```

    This is zsh. Git Bash prints five blocks of `real`, `user` and `sys`;
    its `real` lines read 0.678, 0.704, 0.744, 0.674 and 0.698 s.

2. Keep the smallest of the five, about 0.65 s here: that is the time of
   the rebuild. Write yours on the board.

3. Python starting and stopping, doing nothing: the part of every run
   that no script can avoid.

    === "macOS"

        ```text
        $ time python -c "pass"
        python -c "pass"  0.02s user 0.00s system 99% cpu 0.022 total
        ```

    === "Windows"

        ```text
        $ time python -c "pass"

        real    0m0.020s
        user    0m0.020s
        sys     0m0.000s
        ```

4. Python importing pandas, and nothing else.

    === "macOS"

        ```text
        $ time python -c "import pandas"
        python -c "import pandas"  0.20s user 0.05s system 99% cpu 0.247 total
        ```

    === "Windows"

        ```text
        $ time python -c "import pandas"

        real    0m0.236s
        user    0m0.200s
        sys     0m0.036s
        ```

**Check:** Python starts in 0.02 s; `import pandas` alone takes about
0.24 s.

!!! question "Task: the slowest stage of the rebuild"
    `run_all.py` runs five stages (its list `STAGES`). Time each of them.
    Which stage takes most of the 0.65 s, and why?

??? success "Answer"
    ```text
    $ time python scripts/clean_hill.py > /dev/null
    python scripts/clean_hill.py > /dev/null  0.26s user 0.04s system 99% cpu 0.305 total
    $ time python -m pytest -q > /dev/null
    python -m pytest -q > /dev/null  0.16s user 0.02s system 99% cpu 0.185 total
    ```

    These are the zsh lines; Git Bash gives `real 0m0.304s` and
    `real 0m0.181s`. The other three take 0.01 s (`clean_export.py`),
    0.04 s (`drop_missing.py`) and 0.11 s (`column_stats.py`).
    `clean_hill.py` is the slowest at 0.30 s, and about 0.24 s of it is
    `import pandas`: the hill station's 8740 rows take almost nothing.

---

## Part 2 · Where the time goes { #part-2 }

<!-- 0:25 to 1:00 -->

One script that is slow enough to be worth making faster.

Further reading: [`numpy.cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html).

---

### 4. The warmest 30 days of each year { #warmest }

<!-- 0:25 · 10 min -->

`warmest.py` finds, for each year, the 720 hours in a row with the highest mean temperature.

1. Run it. The last line gives the seconds spent reading and on the
   windows.

    ```text
    $ python scripts/warmest.py
    2016  from 2016-07-15  19.59 °C
    2017  from 2017-06-07  17.52 °C
    2018  from 2018-06-12  19.47 °C
    2019  from 2019-06-29  22.36 °C
    2020  from 2020-05-25  18.75 °C
    2021  from 2021-07-09  20.27 °C
    2022  from 2022-06-28  19.69 °C
    2023  from 2023-06-11  21.81 °C
    2024  from 2024-07-29  18.10 °C
    2025  from 2025-07-08  19.89 °C
    read 0.70 s  windows 0.66 s  total 1.36 s
    ```

2. Open `scripts/warmest.py` and find `def means_loop`. For each of about
   8 000 windows of a year it adds up 720 values: 5.8 million additions a
   year.
3. Find `def read_year`. It reads the whole file, all ten years, to keep the
   rows of one year. It is called once per year.

**Check:** the last line; reading and windows take about half each.

---

### 5. The windows in NumPy { #numpy }

<!-- 0:35 · 10 min -->

`means_numpy` gets all windows of a year from one cumulative sum, in three lines.

1. Find `def means_numpy` in the script and read its three lines. The
   cumulative sum `c` holds at each place the sum of all values up to it,
   so the sum of a window is one subtraction: `c[end] - c[start]`.
2. Run with it. `--method numpy` picks the function.

    ```text
    $ python scripts/warmest.py --method numpy
    2016  from 2016-07-15  19.59 °C
    ...
    2025  from 2025-07-08  19.89 °C
    read 0.73 s  windows 0.00 s  total 0.74 s
    ```

    The ten years are the same as in section 4; the page leaves out eight.

3. The windows now take 0.00 s, and the total only halved: the reading is
   still there. Making one part infinitely fast saves at most that part's
   share of the time: this limit is called **Amdahl's law**.

**Check:** the same ten dates, total 0.74 s.

---

### 6. Read the file once { #once }

<!-- 0:45 · 15 min -->

`read_all` reads the file once and sorts the rows by year.

1. Find `def read_all` in the script: one dictionary with a year as key,
   filled in one pass over the file.
2. Read once, with the slow windows.

    ```text
    $ python scripts/warmest.py --read once
    2016  from 2016-07-15  19.59 °C
    ...
    read 0.09 s  windows 0.65 s  total 0.74 s
    ```

3. Both changes.

    ```text
    $ python scripts/warmest.py --read once --method numpy
    2016  from 2016-07-15  19.59 °C
    ...
    read 0.08 s  windows 0.00 s  total 0.08 s
    ```

**Check:** the same ten dates in 0.08 s instead of 1.36 s: 17 times faster.

!!! question "Task: predict, then measure"
    Before running it: what total do you expect for `--read once --method
    running`? The running sum (optional section 13) takes about 0.01 s for
    the windows. Then run it.

??? success "Answer"
    Reading 0.08 s plus windows 0.01 s: about 0.09 s.

    ```text
    $ python scripts/warmest.py --read once --method running
    ...
    read 0.08 s  windows 0.01 s  total 0.09 s
    ```

---

## Part 3 · More cores { #part-3 }

<!-- 1:00 to 1:25 -->

The ten years are independent, so ten processes could do one year each.

Further reading: [Python's `multiprocessing`](https://docs.python.org/3/library/multiprocessing.html).

---

### 7. Several years at a time { #workers }

<!-- 1:00 · 15 min -->

`--workers N` starts N Python processes and hands each a year, then the next, until all ten are done.

1. Two workers, with the slow version. The last line now gives only the
   total.

    ```text
    $ python scripts/warmest.py --workers 2
    2016  from 2016-07-15  19.59 °C
    ...
    workers 2  total 0.92 s
    ```

2. Four and eight; `| tail -n 1` keeps only the last line.

    ```text
    $ python scripts/warmest.py --workers 4 | tail -n 1
    workers 4  total 0.54 s
    $ python scripts/warmest.py --workers 8 | tail -n 1
    workers 8  total 0.41 s
    ```

3. Write the four times on the board: 1.36, 0.92, 0.54, 0.41. Twice the
   workers is never twice as fast: starting the workers and handing out the
   years cost time, and eight workers need two rounds for ten years.

**Check:** a table of four times, falling more slowly than the number of
workers rises.

---

### 8. Cores or a better method { #compare }

<!-- 1:15 · 10 min -->

One year per worker, all at once.

1. Ten workers.

    ```text
    $ python scripts/warmest.py --workers 10 | tail -n 1
    workers 10  total 0.28 s
    ```

2. Compare with section 6: ten cores give 0.28 s; one core with a better
   method gives 0.08 s.

**Check:** the better method on one core beats ten cores. Change the method
first, then add cores.

!!! question "Task: a laptop with fewer cores"
    On a laptop with as many cores as your number from section 1, which
    `--workers` would you use? Try your number and half of it, five times
    each, and keep the smallest.

??? success "Answer"
    More workers than cores do not help: they share the same cores. More
    than ten do not help either: there are ten years to hand out. So the
    best number is the smaller of your cores and ten; the five timings show
    whether half of it is nearly as fast.

---

## Part 4 · A job that runs without you { #part-4 }

<!-- 1:25 to 2:00 -->

A long job runs while you do something else, on a laptop or on a cluster.

Further reading: [Slurm quick start](https://slurm.schedmd.com/quickstart.html).

---

### 9. A job script for a cluster { #slurm }

<!-- 1:25 · 10 min -->

Slurm, the queue of most clusters, reads what a job needs from the first lines of its script.

1. The first lines of the job script: each `#SBATCH` line asks for one
   thing.

    ```text
    $ head -n 6 scripts/warmest_job.sh
    #!/bin/bash
    #SBATCH --job-name=warmest        # the name shown in the queue
    #SBATCH --output=logs/%x_%j.log   # the log: %x is the name, %j the job number
    #SBATCH --time=00:05:00           # the job is stopped after 5 minutes
    #SBATCH --cpus-per-task=4         # four cores, all on one node
    #SBATCH --mem=1G                  # memory for the whole job
    ```

2. Open the script and read the rest: it activates `s15` and runs
   `warmest.py` with as many workers as Slurm gave cores.
3. For bash the `#SBATCH` lines are comments, so the script runs on the
   laptop too. Give it the two numbers Slurm would set.

    ```text
    $ SLURM_JOB_ID=1 SLURM_CPUS_PER_TASK=4 bash scripts/warmest_job.sh
    start on gluon, job 1
    2016  from 2016-07-15  19.59 °C
    ...
    2025  from 2025-07-08  19.89 °C
    workers 4  total 0.53 s
    done
    ```

    `gluon` is the name of the computer that ran it; yours differs.

4. On a cluster, from the project folder, it is submitted, watched and
   cancelled with these lines; there is no Slurm on the laptop, so they
   are not typed today.

    | Line | Does |
    |--|--|
    | `sbatch scripts/warmest_job.sh` | submits it, prints the job number |
    | `squeue --me` | your jobs: `PD` waiting, `R` running |
    | `scancel 4187263` | stops job 4187263 |

**Check:** the room can say what each `#SBATCH` line asks for.

---

### 10. A job in the background { #background }

<!-- 1:35 · 10 min -->

`&` at the end of a line runs it in the background, and the prompt comes back at once.

1. A folder for logs, as in the job script; `-p` makes no error when it
   is already there.

    ```text
    $ mkdir -p logs
    ```

2. Run `warmest.py` ten times in the background, its last line into the
   log. `[1]` is the job's number in this terminal, then its process id;
   yours differs.

    ```text
    $ for i in {1..10}; do python scripts/warmest.py | tail -n 1; done > logs/warmest.log &
    [1] 2381891
    ```

3. The jobs of this terminal.

    === "macOS"

        ```text
        $ jobs
        [1]  + running    for i in {1..10}; do; python scripts/warmest.py | tail -n 1; done >
        ```

    === "Windows"

        ```text
        $ jobs
        [1]+  Running                 for i in {1..10};
        do
            python scripts/warmest.py | tail -n 1;
        done > logs/warmest.log &
        ```

4. While it runs, read the log: the lines written so far.

    ```text
    $ cat logs/warmest.log
    read 0.64 s  windows 0.62 s  total 1.27 s
    read 0.65 s  windows 0.62 s  total 1.27 s
    read 0.66 s  windows 0.61 s  total 1.27 s
    ```

5. Wait for it to end.

    === "macOS"

        ```text
        $ wait
        [1]  + done       for i in {1..10}; do; python scripts/warmest.py | tail -n 1; done >
        ```

    === "Windows"

        ```text
        $ wait
        [1]+  Done                    for i in {1..10};
        do
            python scripts/warmest.py | tail -n 1;
        done > logs/warmest.log
        ```

6. Count the lines of the log; macOS pads the number with spaces.

    ```text
    $ wc -l logs/warmest.log
    10 logs/warmest.log
    ```

**Check:** ten lines in `logs/warmest.log`; the smallest total is the time
of the script.

!!! question "Task: stop a job, and a job that outlives the terminal"
    1. Start `python scripts/warmest.py > /dev/null &` and stop it before
       it ends.
    2. A job started with `&` ends when its terminal is closed. Start
       `warmest.py --workers 4` so that it does not, with its output in
       `logs/nohup.log`, and read the log's last line.

??? success "Answer"
    1. `kill %1` stops job 1. The shell then reports it:

        === "macOS"

            ```text
            $ kill %1
            [1]  + terminated  python scripts/warmest.py > /dev/null
            ```

        === "Windows"

            ```text
            $ kill %1
            [1]   Terminated              python scripts/warmest.py > /dev/null
            ```

    2. `nohup` keeps the job running when the terminal closes; `2>&1` sends
       the errors into the same log.

        ```text
        $ nohup python scripts/warmest.py --workers 4 > logs/nohup.log 2>&1 &
        $ tail -n 1 logs/nohup.log
        workers 4  total 0.51 s
        ```

        In Git Bash the log starts with the line `nohup: ignoring input`.

---

### 11. Write the times down { #push }

<!-- 1:45 · 10 min -->

A time without the machine and the method beside it means nothing.

1. In `README.md`, above `## How to rebuild`, add a section with your own
   times and save.

    ```text
    ## Timing

    `scripts/warmest.py`, smallest of five runs, on one laptop:

    | Run | Seconds |
    |--|--|
    | as handed out | 1.36 |
    | `--method numpy` | 0.74 |
    | `--read once` | 0.74 |
    | `--read once --method numpy` | 0.08 |
    | `--workers 4` | 0.54 |
    ```

2. Under the table, one line that says which laptop: its name, its
   number of cores from section 1, and the system. Save.

    ```text
    Measured on a laptop with 8 cores, macOS 15.
    ```

3. Look at it: `Ctrl+Shift+V` (macOS `Cmd+Shift+V`) opens the README's
   preview beside the text.

**Check:** the **Timing** section in the README's preview, with your
laptop's line under it.

---

### 12. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->

| To | Type or do |
|--|--|
| time a command | `time COMMAND` |
| trust a time | run it five times, keep the smallest |
| find the slow part | time each part; the profiler of section 14 |
| speed up | the slow part first: a better method, then more cores |
| run without waiting | `COMMAND &`, `jobs`, `wait`, `kill %1`, `nohup`; on a cluster `sbatch` |

---

## Optional, if the room goes fast { #optional }

Further reading: [The Python profilers](https://docs.python.org/3/library/profile.html);
[Slurm job arrays](https://slurm.schedmd.com/job_array.html).

---

### 13. A running sum { #running }

<!-- — · 10 min -->

Moving the window by one hour adds one value and drops one: two operations instead of 720.

1. Find `def means_running` in the script.
2. Run it.

    ```text
    $ python scripts/warmest.py --method running
    2016  from 2016-07-15  19.59 °C
    ...
    read 0.66 s  windows 0.01 s  total 0.67 s
    ```

**Check:** windows 0.01 s in plain Python: a better method needs no
NumPy.

---

### 14. A profiler { #profile }

<!-- — · 10 min -->

`cProfile` counts every call of every function and the time spent in it.

1. Profile the slow version. `-s tottime` sorts by the time spent inside
   each function; `sed -n '12,20p'` keeps the lines after the script's own
   output.

    ```text
    $ python -m cProfile -s tottime scripts/warmest.py | sed -n '12,20p'
             6519749 function calls (6517352 primitive calls) in 2.513 seconds

       Ordered by: internal time

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       876730    0.828    0.000    1.353    0.000 csv.py:173(__next__)
           10    0.626    0.063    0.632    0.063 warmest.py:52(means_loop)
           10    0.365    0.036    1.795    0.180 warmest.py:29(read_year)
       876740    0.276    0.000    0.278    0.000 {built-in method builtins.next}
    ```

2. 876 730 rows were read: 10 × 87 673, the file ten times over. That is
   what section 6 removed.
3. The profiled run takes 2.5 s instead of 1.36 s: counting the calls costs
   time too, most for the functions called most often.

**Check:** `read_year`, called 10 times, holds most of the time.

---

### 15. Advanced tasks { #advanced }

<!-- — · 30 min -->

Three harder tasks for whoever is done early; the answers are folded.

!!! question "Advanced task: where does the fast version spend its time?"
    Profile `--read once --method numpy` as in section 14. Which function
    holds most of the 0.08 s now, and what would you change next?

??? success "Answer"
    ```text
    $ python -m cProfile -s tottime scripts/warmest.py --read once --method numpy | sed -n '12,20p'
             823050 function calls (820646 primitive calls) in 0.344 seconds

       Ordered by: internal time

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        87673    0.094    0.000    0.157    0.000 csv.py:173(__next__)
            1    0.068    0.068    0.239    0.239 warmest.py:40(read_all)
        87674    0.035    0.000    0.035    0.000 {built-in method builtins.next}
       175345    0.015    0.000    0.015    0.000 csv.py:159(fieldnames)
    ```

    `read_all` holds 0.24 of the 0.34 s (the rest is starting Python and
    importing NumPy), and most of it is `csv.DictReader` turning each of
    the 87 673 lines into a dictionary. The windows do not appear any more.
    The next change is the reading: the next task.

!!! question "Advanced task: read the file faster"
    Write `read_all_split`, which does what `read_all` does but cuts each
    line with `line.split(",")` instead of `csv.DictReader`, and add
    `split` to the choices of `--read`. Time it five times. Does it give
    the same ten dates?

??? success "Answer"
    In `scripts/warmest.py`, after `read_all`:

    ```python
    def read_all_split():
        """Read the whole file once, cut each line with split."""
        data = {year: ([], []) for year in YEARS}
        with open(PATH) as handle:
            next(handle)                      # the header
            for line in handle:
                time_, temp = line.split(",")[:2]
                if temp != "-999":
                    times, temps = data[int(time_[:4])]
                    times.append(time_)
                    temps.append(float(temp))
        return data
    ```

    In `main`, the choices and the branch that reads once:

    ```python
    parser.add_argument("--read", default="each", choices=["each", "once", "split"])
    ```

    ```python
    if args.read in ("once", "split"):
        data = read_all() if args.read == "once" else read_all_split()
    ```

    ```text
    $ python scripts/warmest.py --read split --method numpy
    2016  from 2016-07-15  19.59 °C
    2017  from 2017-06-07  17.52 °C
    2018  from 2018-06-12  19.47 °C
    ...
    read 0.04 s  windows 0.00 s  total 0.04 s
    ```

    The same dates in 0.04 s against 0.08 s: half of the reading was
    building dictionaries nobody needed. `time_` has a `_` so that it does
    not hide the module `time` the script imports.

!!! question "Advanced task: one job per year on a cluster"
    A **job array** runs the same script many times, each task with its
    own number in `$SLURM_ARRAY_TASK_ID`. Give `warmest.py` an option
    `--year` that does one year only, and write `scripts/warmest_array.sh`
    with `#SBATCH --array=2016-2025`, one task per year. Try one task on
    the laptop.

??? success "Answer"
    In `main` of `warmest.py`, after `--workers`, and use `years` instead
    of `YEARS` in the two lines that build `jobs`:

    ```python
    parser.add_argument("--year", type=int, choices=YEARS)
    args = parser.parse_args()
    years = [args.year] if args.year else YEARS
    ```

    `scripts/warmest_array.sh`:

    ```bash
    #!/bin/bash
    #SBATCH --job-name=warmest-year
    #SBATCH --output=logs/%x_%a.log   # %a is the task number: the year
    #SBATCH --time=00:02:00
    #SBATCH --cpus-per-task=1
    #SBATCH --mem=500M
    #SBATCH --array=2016-2025         # ten tasks, one per year

    set -e
    eval "$(conda shell.bash hook)"
    conda activate s15
    python scripts/warmest.py --method numpy --year "$SLURM_ARRAY_TASK_ID"
    ```

    ```text
    $ SLURM_ARRAY_TASK_ID=2019 bash scripts/warmest_array.sh
    2019  from 2019-06-29  22.36 °C
    read 0.08 s  windows 0.00 s  total 0.08 s
    ```

    On a cluster `sbatch scripts/warmest_array.sh` queues ten tasks with
    ten logs, `logs/warmest-year_2016.log` to `_2025.log`. Each task reads
    the whole file for its one year, as `read_year` does: the reading is
    done ten times, but on ten cores at once.

---

## Aims practised

- ⚙️ **Automation:** a job that runs ten times on its own and writes a
  log; a job script a cluster runs without anyone at the keyboard.
- ♻️ **Reproducibility:** the times are written down with the run that
  gave them, and the ten dates are the same whichever way they are
  computed.
- 🔧 **Tool-agnostic:** the same lines in zsh and Git Bash; the
  same Python on a laptop and on a cluster.
