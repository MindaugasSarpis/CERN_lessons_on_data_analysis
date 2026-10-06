# 15: Computing Infrastructure & HPC

Every analysis of the course so far ran on one laptop and finished in
seconds. Lecture 13 made such a run repeatable with one command. Lecture 15
asks what happens when the data or the time no longer fits: where the time
of a computation goes, how much memory a table needs, and what a cluster,
the grid and a cloud provider offer when a laptop is not enough. It is a
lecture of the block *Further Topics*. It uses the shell, Python, NumPy and
Pandas as known.

## What the lecture covers

1. **Where the time goes** — the machine behind the numbers; a stopwatch in
   Python and why the smallest of five runs is kept; the sum of the mass
   column as a Python loop (1.53 ms) and in NumPy (0.018 ms); the time per
   row in clock cycles; the whole script timed part by part, for the file as
   it is and for the file 100 times over; reading text against reading a
   binary file.
2. **Amdahl's law** — derived for one part that is made *k* times faster,
   applied to the measured run, then written for *N* workers with the serial
   share *s* and the limit 1/*s*.
3. **More than one core** — processes and a pool of workers; how a worker
   starts on Windows and macOS and why the script needs
   `if __name__ == "__main__":`; four processes that are 60 times slower
   than the loop; a job of 110 million additions on 1 to 12 workers; the law
   fixed by two runs and tested on the others; why the sum changes in its
   last digits; which quantities can be computed in parts and merged.
4. **The GPU** — thousands of simple cores, a clip, and when the copy to the
   card is worth it.
5. **Memory, disk, network** — rows × columns × bytes per value; the peak
   while reading; the estimate from the size of the file; what to do when
   the table does not fit; memory, SSD and network measured as a stream and
   as single items; the time to move a terabyte; the delay that the speed of
   light sets between Vilnius and CERN.
6. **Running unattended** — the two output streams and `2>&1`; `&`, `jobs`,
   `tail -f` and `kill`; why a log stays empty without `python -u`; what a
   log line should say; `nohup`, `ssh` and tmux; one folder per run.
7. **The batch system** — login node, compute nodes, queue; a complete Slurm
   job script, read line by line; `sbatch`, `squeue`, `scancel`, `sacct`;
   what to ask for, from the measurements of the lecture; backfill; the job
   array.
8. **The grid and the cloud** — the tiers of the LHC Computing Grid; why the
   job goes to the data; what a cloud provider rents out, with one bill
   worked out.
9. **Estimate before you start** — rows, memory and time for a file of a
   billion rows, on paper; which machine a job needs.

## The lecture in 90 minutes

The lecture is slides 1–64 and estimates about 136 min. Slides 65–70 are the
self-check quizzes and take no lecture time. For a 90-minute slot, skip the
slides in the second table. To jump, type the slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–3 | The goal and the objectives |
| 0:03 | 4–11 | Where the time goes: the loop, NumPy, time per row, the whole script, text against binary |
| 0:21 | 12–15 | Amdahl's law, derived and applied |
| 0:28 | 16–21, 24 | Processes: the pool, four workers, a job worth splitting, the law tested, what splits |
| 0:43 | 29–30, 32–34, 36 | Memory: the bytes of a table, does it fit, memory against disk against network |
| 0:56 | 39–43, 45 | Running unattended: streams, the background, the log, `nohup` |
| 1:09 | 47–50, 54 | The batch system: the cluster, the job script, the job array |
| 1:20 | 55–57 | The grid |
| 1:26 | 60, 62–64 | A billion rows, which machine, recap |
| 1:34 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Twelve Workers, No Faster Than Eight; The Sum Changes in the Last Digits | 22–23 | 5 min |
| The GPU, with its clip | 25–28 | 8 min |
| Peak Memory Is Larger Than the Table | 31 | 2 min |
| Order in Memory Matters | 35 | 3 min |
| The Limit Set by Light, and the clip on computer memory | 37–38 | 4 min |
| What a Log Tells; One Folder per Run | 44, 46 | 5 min |
| Submit, Watch, Cancel; What to Ask For; An Honest Request Starts Sooner | 51–53 | 7 min |
| The cloud | 58–59 | 5 min |
| Three Numbers Before Starting | 61 | 3 min |

- **Do not cut** slides 6–8 (the loop, the noise, NumPy), 17–21 (the pool
  and the test of Amdahl's law), 30 and 32 (the bytes of a table) or 41–43
  (streams, background, the log). The seminar types and runs exactly these.
- **Slides 6–8 and 19 are shown live:** `python scripts/time_sum.py` in the
  terminal. The room sees the five times scatter and the pool lose.
- **Slide 20 is shown live:** `python scripts/sum_parallel.py --workers 1`,
  then 2, then 4. Write the times on the board and do slide 21 with them.
- **Slide 37:** run `ping cern.ch` (macOS: `ping -c 4 cern.ch`) and compare
  with the bound of 16.5 ms.
- **Slides 41–43 are shown live** with two terminals side by side: the job
  in one, `tail -f results/run.log` in the other.
- **Slides 50 and 54 are read, not run.** The room has no cluster. If the
  cloud is skipped, say at slide 63 in one sentence what it is: machines
  rented by the hour.

## The numbers on the slides

Every time on the slides was measured on one laptop on 4 October 2026: a
MacBook Pro 14-inch (2023) with an Apple M2 Pro, 12 cores (8 performance, 4
efficiency), 16 GB of memory, Python 3.13.9 and NumPy 2.3.5. Each time is the
smallest of five runs.

| Numbers | Slides | Measured with |
|--|--|--|
| Loop, NumPy, four processes | 6–9, 19 | [`hpc_time_sum.py`](../data/hpc_time_sum.py) |
| 1 to 12 workers, the serial share | 20–22 | [`hpc_sum_parallel.py`](../data/hpc_sum_parallel.py) `--workers N` |
| The log and the background job | 40–44 | [`hpc_long_job.py`](../data/hpc_long_job.py) |
| The job script | 50 | [`hpc_job.sh`](../data/hpc_job.sh), a cluster script; on a Mac it also runs with `bash` |

- The long file of slides 10, 14, 32 and 33 is the 91 583 data rows written
  100 times into one file of 392 612 616 bytes. It is not kept.
- The times for 8 and 12 workers were taken while other programs used the
  laptop. On a quiet machine 8 workers come closer to the prediction. Run
  `hpc_sum_parallel.py` before the lecture. If the times differ, change
  slides 20–22 and the constants at the top of `figures/src/computing.py`,
  then run `python figures/src/build.py --only computing`.
- Memory and SSD on slide 34: a 1 GB array summed and copied in NumPy, and a
  2 GB file written and read with the file cache switched off, in one pass
  and in 2 000 blocks of 4 kB at random places.
- `ping cern.ch` gave 46 ms at best, from the lecturer's connection.
- The cloud prices of slides 58–59 are list prices of Amazon Web Services in
  the region US East, as of 2025. Check them before the lecture.
- Slide 56 is the grid slide that stood in Lecture 02, with its numbers:
  170+ sites, 42 countries, about 1.4 million cores.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 65–70: five quiz slides for students to try afterwards. The same
questions, with their answers:

1. A script spends 20 % of its time reading a file and 80 % in a loop that
   can be split over cores. What is the largest speed-up that 8 cores give?
   *1 / (0.2 + 0.8 / 8) = 3.3. The limit for any number of cores is 5.*
2. A table has 40 million rows and 5 columns of float64. Does it fit on a
   laptop with 8 GB, with working room of three times its size?
   *Yes. 40 000 000 × 5 × 8 bytes = 1.6 GB, and three times that is 4.8 GB.*
3. A job was started with `python job.py > run.log 2>&1 &` and killed after
   ten minutes. The log is empty. Why?
   *Python kept the output in its buffer, and the buffer was lost with the
   process. `python -u` writes every line at once.*
4. A node has 16 cores. A job on 8 of them runs for 3 more hours, and first
   in the queue is a job that needs all 16. Which waiting job can start now?
   *The one that asks for 8 cores and 2 hours. It ends before the 16-core
   job can start. A 6-hour job would still hold its cores then.*
5. The same simple operation is applied to 50 million independent values,
   thousands of times. Which hardware suits it best?
   *A GPU. The data is large and reused, so the one copy to the card is a
   small serial part.*

## Paired seminar

[Seminar 15 — Timing, Memory and a Background Job](../seminars/seminar_15.md)
runs on the laptops of the room. The sum of the mass column is timed as a
loop, in NumPy and on four processes, and a longer job on 1, 2 and 4
workers, with the time for 4 predicted from the first two. The size of the
table in memory is worked out on paper and checked in Python. A job of half
a minute is started in the background, its log is followed, the job is
stopped, and an error is found in the log.

## Slides that left the deck

The earlier deck opened with a tour of the hardware: the parts of a
processor, memory modules, hard disks and SSDs with photographs, the memory
hierarchy, input and output devices. Lecture 03 now covers the processor and
the hierarchy, and this deck refers back to it. Also gone are the slides on
vectorisation, which is Lecture 07, and on file formats (CSV, Parquet, HDF5,
ROOT, compression), which are Lectures 03 and 12. They are in the Git
history of `lectures/content/slides/15_Computing_Infrastructure.md` before
the rework of October 2026. The photographs are still in
`lectures/content/public/figures/`.

## Take-aways

- Time the parts of a script before changing it. Time each part five times
  and keep the smallest. Which part is slow depends on the size of the data.
- Amdahl's law: with a serial share *s*, *N* workers give a speed-up of
  1 / (*s* + (1 − *s*) / *N*), and never more than 1 / *s*. Work on the
  largest part first.
- A Python loop spends about 60 clock cycles per addition, NumPy less than
  one. Try the array operation before more cores.
- Starting worker processes costs about a tenth of a second. Splitting pays
  for jobs that take seconds or more, and the number of workers is found by
  measuring.
- A sum can be computed in parts and merged. So can a count, a mean kept as
  sum and count, and a histogram. A median cannot.
- The last digits of a sum depend on the order of the additions. Results are
  compared with a tolerance.
- A table of numbers takes rows × columns × bytes per value. Keep three
  times that free. If it does not fit: fewer columns, a smaller type, or
  pieces.
- One item at a time costs 6 ns from memory, 0.1 ms from an SSD and tens of
  milliseconds over a network. Data that is read in order and in large
  pieces travels well.
- `python -u script.py > run.log 2>&1 &` runs a job in the background with a
  log. `nohup` keeps it alive when the terminal closes.
- A batch system runs a job script that states cores, memory and time. A
  request close to the measured need starts sooner.
- The grid sends the job to the site that holds the data. A cloud provider
  rents machines by the hour, and charges for data that leaves.
