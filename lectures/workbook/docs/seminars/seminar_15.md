# Seminar 15 — How Long Does It Take, and How to Make It Faster? Timing the Weather Project

**Paired lecture:** 15 Computing Infrastructure & HPC · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student times the rebuild and one slow script,
finds which part of it is slow, makes it 17 times faster on one core,
compares that with more cores, runs it as a background job, and pushes the
times in the README.

Everything is typed in the terminal of VS Code (zsh on macOS, Git Bash on
Windows), in the weather project, with the `weather` environment active. No cluster and no
account is needed.

## Run sheet

| Clock | Section | Typed | The room ends with |
|--|--|--|--|
| | **Part 1 · How long does it take?** · 25 min | | |
| 0:00 | [1. Get today's scripts](#pull) | `git pull --no-edit course main` | two new scripts, the number of cores |
| 0:10 | [2. Time the rebuild](#rebuild) | `time python run_all.py` | the rebuild in seconds |
| 0:15 | [3. A time has noise](#noise) | `for i in 1 2 3 4 5; do time ...` | five times, the smallest kept |
| | **Part 2 · Where the time goes** · 35 min | | |
| 0:25 | [4. The warmest 30 days of each year](#warmest) | `python scripts/warmest.py` | read 0.70 s, windows 0.66 s |
| 0:35 | [5. The windows in NumPy](#numpy) | `--method numpy` | half the time, not less |
| 0:45 | [6. Read the file once](#once) | `--read once` | 0.08 s: 17 times faster |
| | **Part 3 · More cores** · 25 min | | |
| 1:00 | [7. Several years at a time](#workers) | `--workers 4` | times for 1, 2, 4, 8 workers |
| 1:15 | [8. Cores or a better method](#compare) | `--workers 10` | 0.28 s on ten cores, 0.08 s on one |
| | **Part 4 · A job that runs without you** · 35 min | | |
| 1:25 | [9. A job script for a cluster](#slurm) | `head -n 6 scripts/warmest_job.sh` | the job script run on the laptop |
| 1:35 | [10. A job in the background](#background) | `... > logs/warmest.log &` | `logs/warmest.log`, growing while the job runs |
| 1:45 | [11. Write the times down, push](#push) | `git push` | a **Timing** section on GitHub |
| 1:55 | [12. Wrap up](#wrap-up) | | |
| | **Optional, if the room is fast** | | |
| — | [13. A running sum](#running) | `--method running` | the windows without NumPy, as fast |
| — | [14. A profiler](#profile) | `python -m cProfile` | 876 730 rows read |

**If time runs short:** stop after section 8 and do section 11; Part 4 is
optional on a laptop.

??? info "Before the session"
    - **Room:** the weather project as it stands after Seminar 13, pushed to
      the student's own GitHub repository, with the `course` remote of
      Seminar 6 and the `weather` environment (NumPy and pandas in it).
    - **You:** nothing to prepare. Every time on this page was measured on
      one machine (Linux); times in the room differ, often by a factor of
      two. On macOS and Windows each worker of Part 3 starts a fresh Python,
      so the times with workers are higher there. The results of the scripts
      do not differ.
    - **Keys** are written for Windows, macOS in brackets. Every line typed is
      the same on both systems.

---

## Part 1 · How long does it take? { #part-1 }

**0:00 to 0:25** · Before making anything faster, measure it.

---

### 1. Get today's scripts { #pull }

**0:00 · 10 min** · Two scripts come from the course repository.

1. Open the weather project in VS Code, then the terminal: **View** >
   **Terminal**.
2. Activate the environment.

    ```text
    conda activate weather
    ```

3. Get the scripts.

    ```text
    git pull --no-edit course main
    ```

    ```text
    From https://github.com/MindaugasSarpis/weather-project
     * branch            main       -> FETCH_HEAD
    Merge made by the 'ort' strategy.
     scripts/warmest.py     | 129 +++++++++++++++++++++++++++++++++++++++++++++++++
     scripts/warmest_job.sh |  17 +++++++
     2 files changed, 146 insertions(+)
    ```

4. How many cores this computer has.

    ```text
    python -c "import os; print(os.cpu_count())"
    ```

    ```text
    128
    ```

    This run was on a server. A laptop prints 4 to 16.

**Check:** two new scripts; the number of cores on the board for the room.

---

### 2. Time the rebuild { #rebuild }

**0:10 · 5 min** · `time` in front of a command runs it and then prints how long it took.

1. Time the one command of Seminar 13; `> /dev/null` throws its own output
   away.

    ```text
    time python run_all.py > /dev/null
    ```

    === "macOS"

        ```text
        python run_all.py > /dev/null  0.63s user 0.08s system 100% cpu 0.709 total
        ```

    === "Windows"

        ```text
        real    0m0.662s
        user    0m0.544s
        sys     0m0.119s
        ```

    zsh ends its line with the time on the clock, `0.709 total`; Git Bash
    gives it as `real`. `user` and `sys` are the time the processor spent.
    Your times differ.

**Check:** a time on the clock below one second.

---

### 3. A time has noise { #noise }

**0:15 · 10 min** · Other programs take the processor now and then and only add time, so time five times and keep the smallest.

1. The rebuild, five times.

    ```text
    for i in 1 2 3 4 5; do time python run_all.py > /dev/null; done
    ```

    === "macOS"

        ```text
        python run_all.py > /dev/null  0.57s user 0.08s system 100% cpu 0.650 total
        python run_all.py > /dev/null  0.62s user 0.08s system 100% cpu 0.701 total
        python run_all.py > /dev/null  0.56s user 0.10s system 100% cpu 0.658 total
        python run_all.py > /dev/null  0.62s user 0.08s system 100% cpu 0.702 total
        python run_all.py > /dev/null  0.58s user 0.11s system 100% cpu 0.683 total
        ```

    === "Windows"

        Five blocks like the one of section 2; their `real` lines:

        ```text
        real    0m0.678s
        real    0m0.704s
        real    0m0.744s
        real    0m0.674s
        real    0m0.698s
        ```

    The smallest, about 0.65 s, is the time of the rebuild.

2. Python starting and stopping, doing nothing.

    ```text
    time python -c "pass"
    ```

    === "macOS"

        ```text
        python -c "pass"  0.02s user 0.00s system 99% cpu 0.022 total
        ```

    === "Windows"

        ```text
        real    0m0.020s
        user    0m0.020s
        sys     0m0.000s
        ```

3. Python importing pandas.

    ```text
    time python -c "import pandas"
    ```

    === "macOS"

        ```text
        python -c "import pandas"  0.20s user 0.05s system 99% cpu 0.247 total
        ```

    === "Windows"

        ```text
        real    0m0.236s
        user    0m0.200s
        sys     0m0.036s
        ```

**Check:** Python starts in 0.02 s; `import pandas` alone takes about
0.24 s.

!!! question "Task: the slowest stage of the rebuild"
    `run_all.py` runs five stages (its list `STAGES`). Time each of them.
    Which stage takes most of the 0.65 s, and why?

??? note "Answer"
    ```text
    time python scripts/clean_hill.py > /dev/null
    ```

    ```text
    python scripts/clean_hill.py > /dev/null  0.26s user 0.04s system 99% cpu 0.305 total
    ```

    ```text
    time python -m pytest -q > /dev/null
    ```

    ```text
    python -m pytest -q > /dev/null  0.16s user 0.02s system 99% cpu 0.185 total
    ```

    These are the zsh lines; Git Bash gives `real 0m0.304s` and
    `real 0m0.181s`. The other three take 0.01 s (`clean_export.py`),
    0.04 s (`drop_missing.py`) and 0.11 s (`column_stats.py`).
    `clean_hill.py` is the slowest at 0.30 s, and about 0.24 s of it is
    `import pandas`: the hill station's 8740 rows take almost nothing.

---

## Part 2 · Where the time goes { #part-2 }

**0:25 to 1:00** · One script that is slow enough to be worth making faster.

---

### 4. The warmest 30 days of each year { #warmest }

**0:25 · 10 min** · `warmest.py` finds, for each year, the 720 hours in a row with the highest mean temperature.

1. Run it. The last line gives the seconds spent reading and on the
   windows.

    ```text
    python scripts/warmest.py
    ```

    ```text
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

**0:35 · 10 min** · `means_numpy` gets all windows of a year from one cumulative sum, in three lines.

1. Find `def means_numpy` in the script and read its three lines.
2. Run with it.

    ```text
    python scripts/warmest.py --method numpy
    ```

    ```text
    2016  from 2016-07-15  19.59 °C
    ...
    2025  from 2025-07-08  19.89 °C
    read 0.73 s  windows 0.00 s  total 0.74 s
    ```

    The ten years are the same as in section 4; the page leaves out eight.

3. The windows now take 0.00 s, and the total only halved: the reading is
   still there. Making one part infinitely fast saves at most that part's
   share. This is Amdahl's law of the lecture.

**Check:** the same ten dates, total 0.74 s.

---

### 6. Read the file once { #once }

**0:45 · 15 min** · `read_all` reads the file once and sorts the rows by year.

1. Find `def read_all` in the script.
2. Read once, with the slow windows.

    ```text
    python scripts/warmest.py --read once
    ```

    ```text
    2016  from 2016-07-15  19.59 °C
    ...
    read 0.09 s  windows 0.65 s  total 0.74 s
    ```

3. Both changes.

    ```text
    python scripts/warmest.py --read once --method numpy
    ```

    ```text
    2016  from 2016-07-15  19.59 °C
    ...
    read 0.08 s  windows 0.00 s  total 0.08 s
    ```

**Check:** the same ten dates in 0.08 s instead of 1.36 s: 17 times faster.

!!! question "Task: predict, then measure"
    Before running it: what total do you expect for `--read once --method
    running`? The running sum (optional section 13) takes about 0.01 s for
    the windows. Then run it.

??? note "Answer"
    Reading 0.08 s plus windows 0.01 s: about 0.09 s.

    ```text
    python scripts/warmest.py --read once --method running
    ```

    ```text
    ...
    read 0.08 s  windows 0.01 s  total 0.09 s
    ```

---

## Part 3 · More cores { #part-3 }

**1:00 to 1:25** · The ten years are independent, so ten processes could do one year each.

---

### 7. Several years at a time { #workers }

**1:00 · 15 min** · `--workers N` starts N Python processes and hands each a year, then the next, until all ten are done.

1. Two workers, with the slow version.

    ```text
    python scripts/warmest.py --workers 2
    ```

    ```text
    2016  from 2016-07-15  19.59 °C
    ...
    workers 2  total 0.92 s
    ```

2. Four and eight, only the last line of each.

    ```text
    python scripts/warmest.py --workers 4 | tail -n 1
    ```

    ```text
    workers 4  total 0.54 s
    ```

    ```text
    python scripts/warmest.py --workers 8 | tail -n 1
    ```

    ```text
    workers 8  total 0.41 s
    ```

3. Write the four times on the board: 1.36, 0.92, 0.54, 0.41. Twice the
   workers is never twice as fast: starting the workers and handing out the
   years cost time, and eight workers need two rounds for ten years.

**Check:** a table of four times, falling more slowly than the number of
workers rises.

---

### 8. Cores or a better method { #compare }

**1:15 · 10 min** · One year per worker, all at once.

1. Ten workers.

    ```text
    python scripts/warmest.py --workers 10 | tail -n 1
    ```

    ```text
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

??? note "Answer"
    More workers than cores do not help: they share the same cores. More
    than ten do not help either: there are ten years to hand out. So the
    best number is the smaller of your cores and ten; the five timings show
    whether half of it is nearly as fast.

---

## Part 4 · A job that runs without you { #part-4 }

**1:25 to 2:00** · A long job runs while you do something else, on a laptop or on a cluster.

---

### 9. A job script for a cluster { #slurm }

**1:25 · 10 min** · Slurm, the queue of most clusters, reads what a job needs from the first lines of its script.

1. The first lines of the job script.

    ```text
    head -n 6 scripts/warmest_job.sh
    ```

    ```text
    #!/bin/bash
    #SBATCH --job-name=warmest        # the name shown in the queue
    #SBATCH --output=logs/%x_%j.log   # the log: %x is the name, %j the job number
    #SBATCH --time=00:05:00           # the job is stopped after 5 minutes
    #SBATCH --cpus-per-task=4         # four cores, all on one node
    #SBATCH --mem=1G                  # memory for the whole job
    ```

2. Open the script and read the rest: it activates `weather` and runs
   `warmest.py` with as many workers as Slurm gave cores.
3. For bash the `#SBATCH` lines are comments, so the script runs on the
   laptop too. Give it the two numbers Slurm would set.

    ```text
    SLURM_JOB_ID=1 SLURM_CPUS_PER_TASK=4 bash scripts/warmest_job.sh
    ```

    ```text
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

**1:35 · 10 min** · `&` at the end of a line runs it in the background, and the prompt comes back at once.

1. A folder for logs, as in the job script.

    ```text
    mkdir -p logs
    ```

2. Run `warmest.py` ten times in the background, its last line into the log.

    ```text
    for i in {1..10}; do python scripts/warmest.py | tail -n 1; done > logs/warmest.log &
    ```

    ```text
    [1] 2381891
    ```

    `[1]` is the job's number in this terminal, then its process id; yours
    differs.

3. The jobs of this terminal.

    ```text
    jobs
    ```

    === "macOS"

        ```text
        [1]  + running    for i in {1..10}; do; python scripts/warmest.py | tail -n 1; done >
        ```

    === "Windows"

        ```text
        [1]+  Running                 for i in {1..10};
        do
            python scripts/warmest.py | tail -n 1;
        done > logs/warmest.log &
        ```

4. While it runs, read the log.

    ```text
    cat logs/warmest.log
    ```

    ```text
    read 0.64 s  windows 0.62 s  total 1.27 s
    read 0.65 s  windows 0.62 s  total 1.27 s
    read 0.66 s  windows 0.61 s  total 1.27 s
    ```

5. Wait for it to end.

    ```text
    wait
    ```

    === "macOS"

        ```text
        [1]  + done       for i in {1..10}; do; python scripts/warmest.py | tail -n 1; done >
        ```

    === "Windows"

        ```text
        [1]+  Done                    for i in {1..10};
        do
            python scripts/warmest.py | tail -n 1;
        done > logs/warmest.log
        ```

6. Count the lines of the log.

    ```text
    wc -l logs/warmest.log
    ```

    ```text
    10 logs/warmest.log
    ```

    macOS pads the number with spaces.

**Check:** ten lines in `logs/warmest.log`; the smallest total is the time
of the script.

!!! question "Task: stop a job, and a job that outlives the terminal"
    1. Start `python scripts/warmest.py > /dev/null &` and stop it before
       it ends.
    2. A job started with `&` ends when its terminal is closed. Start
       `warmest.py --workers 4` so that it does not, with its output in
       `logs/nohup.log`, and read the log's last line.

??? note "Answer"
    1. `kill %1` stops job 1. The shell then reports it:

        ```text
        kill %1
        ```

        === "macOS"

            ```text
            [1]  + terminated  python scripts/warmest.py > /dev/null
            ```

        === "Windows"

            ```text
            [1]   Terminated              python scripts/warmest.py > /dev/null
            ```

    2. `nohup` keeps the job running when the terminal closes; `2>&1` sends
       the errors into the same log.

        ```text
        nohup python scripts/warmest.py --workers 4 > logs/nohup.log 2>&1 &
        ```

        ```text
        tail -n 1 logs/nohup.log
        ```

        ```text
        workers 4  total 0.51 s
        ```

        In Git Bash the log starts with the line `nohup: ignoring input`.

---

### 11. Write the times down, push { #push }

**1:45 · 10 min** · A time without the machine and the method beside it means nothing.

1. Logs stay out of the history. Open `.gitignore`, add a line and save.

    ```text
    logs/
    ```

2. In `README.md`, above `## How to rebuild`, add a section with your own
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

3. What changed.

    ```text
    git status --short
    ```

    ```text
     M .gitignore
     M README.md
    ```

4. Commit and push.

    ```text
    git commit -am "Record how long warmest.py takes"
    ```

    ```text
    [main 788b165] Record how long warmest.py takes
     2 files changed, 13 insertions(+)
    ```

    ```text
    git push
    ```

    ```text
    To https://github.com/your-username/weather-project.git
       0184479..788b165  main -> main
    ```

**Check:** the **Timing** section on GitHub.

---

### 12. Wrap up { #wrap-up }

**1:55 · 5 min**

| To | Type or do |
|--|--|
| time a command | `time COMMAND` |
| trust a time | run it five times, keep the smallest |
| find the slow part | time each part; the profiler of section 14 |
| speed up | the slow part first: a better method, then more cores |
| run without waiting | `COMMAND &`, `jobs`, `wait`, `kill %1`, `nohup`; on a cluster `sbatch` |

---

## Optional, if the room is fast { #optional }

---

### 13. A running sum { #running }

**— · 10 min** · Moving the window by one hour adds one value and drops one: two operations instead of 720.

1. Find `def means_running` in the script.
2. Run it.

    ```text
    python scripts/warmest.py --method running
    ```

    ```text
    2016  from 2016-07-15  19.59 °C
    ...
    read 0.66 s  windows 0.01 s  total 0.67 s
    ```

**Check:** windows 0.01 s in plain Python: a better method needs no
NumPy.

---

### 14. A profiler { #profile }

**— · 10 min** · `cProfile` counts every call of every function and the time spent in it.

1. Profile the slow version, the first lines after the script's own output.

    ```text
    python -m cProfile -s tottime scripts/warmest.py | sed -n '12,20p'
    ```

    ```text
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

## Aims practised

- ⚙️ **Automation:** a job that runs ten times on its own and writes a
  log; a job script a cluster runs without anyone at the keyboard.
- ♻️ **Reproducibility:** the times are written down with the run that
  gave them, and the ten dates are the same whichever way they are
  computed.
- 🔧 **Tool-agnostic:** the same lines in zsh and Git Bash; the
  same Python on a laptop and on a cluster.
