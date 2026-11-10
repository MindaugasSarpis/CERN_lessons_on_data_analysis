# Seminar 15 · Computing

**Paired lecture:** 15 Computing Infrastructure & HPC · **Format:** a showcase, then a problem, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** How long would your laptop need to find the hottest day of every weather station in GHCN-Daily, and would more cores or a cluster make it faster?

The lecturer runs Part 2 from this page; in Part 3 the room works in pairs.
Everything is typed in VS Code: the scripts in the editor, the commands in its
terminal (zsh on macOS, Git Bash on Windows; the same lines in both). A line
that starts with `$` is typed without the `$`; `...` stands for lines left out.
No cluster and no account is needed.

**If time runs short:** leave out section 6 (the job in the background); its calls are on the library card.

??? info "Before the session"
    - **Room:** Miniforge and VS Code with its Python extension on every
      laptop (the [Setup](../setup.md) page); internet for conda, if
      `analysis` has to be made, and for the data: 6.1 MB in Part 1, about
      13 MB in Part 3. Nothing from earlier seminars is needed.
    - **No file is handed out.** All data comes from GHCN-Daily, the daily
      records of weather stations collected by NOAA NCEI: the file of the
      Vilnius station, `LH000026730.csv` (6.1 MB, 1881 to 24 August 2025);
      in Part 3 the list of all stations (11 MB) and two more station files
      (40 kB and 1.2 MB). Terms: "for free and unrestricted use in research,
      education, and other non-commercial activities" (WMO Resolution 40);
      cite Menne et al. 2012, *Global Historical Climatology Network - Daily
      (GHCN-Daily)*, Version 3.35, NOAA NCDC,
      [doi:10.7289/V5D21VHZ](https://doi.org/10.7289/V5D21VHZ), accessed
      10 November 2026.
    - **The times** on this page were measured on 10 November 2026 on one
      desktop computer (Linux, 8 cores of two threads each). A laptop's
      times differ, often by a factor of two; on macOS and Windows every
      worker of a pool starts a new Python, which costs more. The results
      (dates, sums, counts) do not differ. NCEI rebuilds the archive every
      day, so its size grows a little.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` (Miniforge): [Setup, steps 2–4](../setup.md#shell); the Python
      extension: [Setup, step 7](../setup.md#extensions).
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.

---

## Part 1 · Set up { #part-1 }

### 1. A new folder, and the environment `analysis` { #start }

<!-- 0:00 · 7 min -->

An environment is a folder with its own Python and its own packages; `analysis` serves weeks 8 to 16, and today needs pandas, which brings NumPy with it.

1. In VS Code, **View** > **Terminal**. Make the folder and go into it.

    ```text
    $ mkdir ~/weather-s15
    $ cd ~/weather-s15
    ```

2. **File** > **Open Folder...** > `weather-s15` (in your home folder) >
   **Open**, then **View** > **Terminal**. The Explorer on the left is empty.

3. **If `analysis` is on this laptop** (Seminars 8 to 14): switch it on.

    ```text
    $ conda activate analysis
    ```

4. **If it is not:** make it in one line. At `Proceed ([y]/n)?` press
   `Enter`. Then switch it on.

    ```text
    $ conda create -n analysis python=3.14 pandas=3.1 matplotlib-base=3.11
    ...
    Proceed ([y]/n)?
    ...
    $ conda activate analysis
    ```

    `conda: command not found`: install Miniforge as on the
    [Setup page, steps 2–4](../setup.md#shell), then open a new terminal.

5. Ask for the versions.

    ```text
    $ python -c "import pandas, numpy; print(pandas.__version__, numpy.__version__)"
    3.1.1 2.5.4
    ```

**Check:** `(analysis)` at the start of the prompt, and `3.1.1 2.5.4` (the last digits may be higher).

---

### 2. The station file, the number of cores, the environment written down { #install }

<!-- 0:07 · 8 min -->

Part 2 reads one real file; Part 3 needs two numbers of this laptop: how fast it downloads, and how many cores it has.

1. Download the daily record of the Vilnius station. Write down the
   number under **Average Speed** (**Dload**): `3602k` is 3602 kilobytes
   of 1024 bytes, 3.7 MB, a second.

    ```text
    $ curl -O https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/LH000026730.csv
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100 5976k  100 5976k    0     0  3602k      0  0:00:01  0:00:01 --:--:-- 3600k
    $ wc -c LH000026730.csv
    6119696 LH000026730.csv
    ```

    Your speed differs. macOS pads the number of `wc` with spaces.

2. Ask the operating system how many cores this computer has. Write it
   down.

    ```text
    $ python -c "import os; print(os.cpu_count())"
    16
    ```

    This computer has 8 cores of two threads each. A laptop prints 4 to 16.

3. Write the environment into a file, then click `environment.yml` in the
   Explorer, delete its last line, `prefix: ...`, and save (`Ctrl+S`, macOS
   `Cmd+S`).

    ```text
    $ conda env export --from-history -f environment.yml
    ```

4. Tell VS Code which Python to use: `Ctrl+Shift+P` (macOS `Cmd+Shift+P`),
   `Python: Select Interpreter`, pick the entry with `envs/analysis` in its
   path.

**Check:** `LH000026730.csv` in the Explorer; the download speed and the number of cores on paper.

---

## Part 2 · Showcase { #part-2 }

The lecturer runs four complete scripts on the station file; the room watches
or types along. For each: in the Explorer, right-click > **New File...**, the
name above the code, paste, save, run it in the terminal. Every time printed
here differs on your laptop.

### 3. One sum, five times: a Python loop and NumPy { #noise }

<!-- 0:15 · 9 min -->

A time measured once includes whatever else the computer was doing; measure five times and keep the smallest.

```python title="sums.py"
import time

import pandas as pd

df = pd.read_csv("LH000026730.csv", usecols=["TAVG"])
temps = (df["TAVG"].dropna() / 10).to_numpy()    # a NumPy array, in °C
values = temps.tolist()                          # the same, as a Python list
print(len(values), "daily means")

for run in range(5):
    start = time.perf_counter()
    total = 0.0
    for v in values:                             # one addition at a time
        total += v
    loop = time.perf_counter() - start
    start = time.perf_counter()
    total_np = temps.sum()                       # one call for all of them
    numpy = time.perf_counter() - start
    print(f"loop {loop * 1000:6.3f} ms   numpy {numpy * 1000:6.3f} ms   "
          f"{total!r}   {total_np!r}")
```

```text
$ python sums.py
50814 daily means
loop  1.191 ms   numpy  0.018 ms   331225.5000000016   np.float64(331225.5)
loop  1.169 ms   numpy  0.011 ms   331225.5000000016   np.float64(331225.5)
loop  1.149 ms   numpy  0.007 ms   331225.5000000016   np.float64(331225.5)
loop  1.169 ms   numpy  0.010 ms   331225.5000000016   np.float64(331225.5)
loop  1.149 ms   numpy  0.007 ms   331225.5000000016   np.float64(331225.5)
```

**Notice:** the smallest times, 1.149 ms and 0.007 ms, differ by a factor of about 160; the first NumPy run took more than twice as long as the smallest.

**Ask the room:** the two sums differ in the last digits. Which one is right, and why do they differ?

??? note "Answer"
    The file holds whole tenths of a degree, so the exact sum is
    331 225.5. Neither 0.1 nor most other tenths can be stored exactly in
    binary, and every addition rounds. The loop adds 50 814 numbers one
    after another and its rounding errors pile up; NumPy adds in pairs,
    then pairs of pairs, and rounds less. Both are right to 15 significant
    digits; a result should never depend on the last ones.

---

### 4. Where the time of one run goes { #parts }

<!-- 0:24 · 9 min -->

Time each part before making any part faster: a part that takes a share p of the run, made infinitely fast, saves at most that share (Amdahl's law).

```python title="parts.py"
import time

start = time.perf_counter()
from pathlib import Path
import numpy as np
import pandas as pd
imported = time.perf_counter()

df = pd.read_csv("LH000026730.csv")
read = time.perf_counter()
mean = df["TAVG"].mean() / 10                   # the file holds tenths of °C
computed = time.perf_counter()
print(f"mean of {df['TAVG'].count()} days: {mean:.2f} °C")
print(f"import {imported - start:.3f} s   read {read - imported:.3f} s   "
      f"compute {computed - read:.4f} s")
size = Path("LH000026730.csv").stat().st_size
print(f"file {size / 1e6:.1f} MB, "
      f"in memory {df.memory_usage(deep=True).sum() / 1e6:.1f} MB")

numbers = df[["TMAX", "TMIN", "TAVG", "PRCP"]].to_numpy()
np.save("numbers.npy", numbers)                 # the bytes as in memory
start = time.perf_counter()
numbers = np.load("numbers.npy")
loaded = time.perf_counter()
print(f"numbers.npy {numbers.nbytes / 1e6:.1f} MB, "
      f"load {loaded - start:.4f} s")
```

```text
$ python parts.py
mean of 50814 days: 6.52 °C
import 0.154 s   read 0.071 s   compute 0.0004 s
file 6.1 MB, in memory 24.3 MB
numbers.npy 1.6 MB, load 0.0005 s
```

**Notice:** turning 6.1 MB of text into numbers takes 0.071 s, loading the four number columns from a binary file 0.0005 s; importing pandas takes longer than both.

**Ask the room:** the read is replaced by the binary load. How much faster does the whole run get?

??? note "Answer"
    The run took 0.154 + 0.071 + 0.0004 = 0.225 s; with the load it takes
    0.154 + 0.0005 + 0.0004 = 0.155 s: 1.45 times faster, not 140 times. The
    read was p = 0.071 / 0.225 = 32 % of the run, so even an instant read
    gives at most 1 / (1 − 0.32) = 1.46. The import is now the slow part,
    and it does not grow with the data: for one file there is nothing left
    worth an hour's work.

    In memory the table takes 24.3 MB, four times the file: every text field
    (the station's name, the flags) is a Python object of its own.

---

### 5. One to eight worker processes on the same years: resampling and summing { #pool }

<!-- 0:33 · 10 min -->

One Python process runs on one core; `multiprocessing.Pool` starts more processes and hands each one item at a time. Starting them has a price.

The job: for each of the 142 years, draw its days again at random 2000 times and see how far the year's mean moves (a bootstrap). The years do not depend on each other.

```python title="pool.py"
import random
import statistics
import time
from multiprocessing import Pool

import pandas as pd


def resampled_spread(temps):
    """How far a year's mean moves when its days are drawn again."""
    rng = random.Random(0)
    means = [statistics.fmean(rng.choices(temps, k=len(temps)))
             for _ in range(2000)]
    return statistics.stdev(means)


def timed(job, items, workers):
    start = time.perf_counter()
    with Pool(workers) as pool:                  # start the worker processes
        results = pool.map(job, items)           # one item at a time to each
    return time.perf_counter() - start


if __name__ == "__main__":       # the workers import this file: not for them
    df = pd.read_csv("LH000026730.csv", usecols=["DATE", "TAVG"]).dropna()
    by_year = df.groupby(df["DATE"].str[:4])["TAVG"]
    years = [(group / 10).tolist() for _, group in by_year]
    print(len(years), "years")
    for workers in [1, 2, 4, 8]:
        seconds = timed(resampled_spread, years, workers)
        print(f"resampling, {workers} workers: {seconds:.2f} s")
    start = time.perf_counter()
    sums = [sum(temps) for temps in years]
    print(f"sums, no pool: {(time.perf_counter() - start) * 1000:.1f} ms")
    print(f"sums, 4 workers: {timed(sum, years, 4) * 1000:.1f} ms")
```

```text
$ python pool.py
142 years
resampling, 1 workers: 4.62 s
resampling, 2 workers: 2.35 s
resampling, 4 workers: 1.23 s
resampling, 8 workers: 0.77 s
sums, no pool: 0.2 ms
sums, 4 workers: 12.6 ms
```

**Notice:** 8 workers make the resampling 6.0 times faster; 4 workers make the sums 60 times slower.

**Ask the room:** from the times for 1 and 2 workers, predict 8 workers with T(N) = T<sub>s</sub> + T<sub>p</sub> / N. Why is the measured time longer?

??? note "Answer"
    T(1) − T(2) = T<sub>p</sub> / 2, so T<sub>p</sub> = 2 × (4.62 − 2.35)
    = 4.54 s and T<sub>s</sub> = 4.62 − 4.54 = 0.08 s. Predicted: 0.08 +
    4.54 / 8 = 0.65 s; measured 0.77 s. The law is the best case: the
    eight workers share the cores with everything else the computer runs,
    and the last worker to finish sets the time. The sums take 0.2 ms of
    work; starting four Pythons and sending them the years costs 12 ms.
    A job is worth splitting when its work is much longer than that price.

!!! warning "`RuntimeError: An attempt has been made to start a new process...`"
    The lines that start the pool stand outside `if __name__ == "__main__":`.
    On macOS and Windows each worker imports the script, and would start a
    pool of its own.

---

### 6. A job in the background, and why its log stays empty { #background }

<!-- 0:43 · 9 min -->

`&` at the end of a line runs it in the background and gives the prompt back; `>` sends what it prints into a file, the log.

```python title="job.py"
import random
import statistics
import time

import pandas as pd

df = pd.read_csv("LH000026730.csv", usecols=["DATE", "TAVG"]).dropna()
df["year"] = df["DATE"].str[:4].astype(int)
start = time.perf_counter()
for year, group in df.groupby("year"):
    temps = (group["TAVG"] / 10).tolist()
    rng = random.Random(0)
    means = [statistics.fmean(rng.choices(temps, k=len(temps)))
             for _ in range(2000)]                   # the work of pool.py
    if year % 10 == 0:
        print(f"{year} done after {time.perf_counter() - start:.1f} s")
print("all years done")
```

1. Start it in the background, and read the log at once. `[1]` is the
   job's number in this terminal, then its process id; yours differs.

    ```text
    $ python job.py > job.log &
    [1] 1143749
    $ cat job.log
    ```

    The log is empty, while the job has been at work for seconds.

2. Wait for it to end, then read the log again.

    === "macOS"

        ```text
        $ wait
        [1]  + done       python job.py > job.log
        ```

    === "Windows"

        ```text
        $ wait
        [1]+  Done                    python job.py > job.log
        ```

    ```text
    $ cat job.log
    1890 done after 0.3 s
    1900 done after 0.7 s
    ...
    2020 done after 4.7 s
    all years done
    ```

3. The same with `-u`: Python then writes each line into the file at once.
   Read the log a few seconds after the start.

    ```text
    $ python -u job.py > job.log &
    [1] 1143831
    $ cat job.log
    1890 done after 0.3 s
    1900 done after 0.7 s
    1910 done after 1.0 s
    ...
    ```

**Notice:** without `-u` the 15 lines waited in Python's buffer and reached the file only when the job ended.

**Ask the room:** a job on a cluster has run for three hours, and its log is empty. Is it stuck?

??? note "Answer"
    Not necessarily: what it printed may still be in the buffer. Run it with
    `python -u`, or print with `print(..., flush=True)`, so that the log
    shows how far the job has come, and its last line before a crash. A job
    started with `&` ends when its terminal is closed; `nohup` keeps it
    running: `nohup python -u job.py > job.log 2>&1 &` (`2>&1` sends the
    error messages into the same log; in Git Bash the log then starts with
    `nohup: ignoring input`).

---

### 7. Library card: the calls of this page { #card }

<!-- 0:52 · 3 min -->

Every call and command of the examples and of the solution below, one line each.

| Call or command | What it does |
|--|--|
| `time.perf_counter()` | a time in seconds, for differences: `end - start` |
| `values.tolist()`, `df["TAVG"].to_numpy()` | a NumPy array as a Python list; a column as a NumPy array |
| `np.save("a.npy", array)`, `np.load("a.npy")` | an array into a binary file, and back |
| `df.memory_usage(deep=True).sum()` | bytes the table takes in memory, text included |
| `Path(name).stat().st_size`, `Path(name).read_bytes()` | the size of a file; its bytes |
| `gzip.compress(data)`, `gzip.decompress(packed)` | pack bytes as gzip does, and unpack them |
| `with Pool(4) as pool:` | four worker processes, closed at the end of the block |
| `pool.map(function, items)` | the function on every item, in the workers; the results in order |
| `if __name__ == "__main__":` | lines for the script started by hand, not for the workers |
| `os.cpu_count()` | the number of cores (threads) the system reports |
| `python script.py > job.log &` | run in the background, the printed lines into `job.log` |
| `python -u ...`, `print(..., flush=True)` | every line into the log at once |
| `wait` | waits until the background jobs of this terminal have ended |
| `nohup COMMAND > log 2>&1 &` | keeps running when the terminal closes; errors into the same log |
| `curl -sI URL`, `curl -O URL` | only the headers of an address (its size among them); the file itself |

---

## Part 3 · The problem { #part-3 }

### 8. How long for every station of GHCN-Daily, and with how many cores? { #problem }

<!-- 0:55 · 50 min: predict 5, solve 25, check 10, hand in 10 -->

GHCN-Daily holds the daily records of the weather stations of the world, one
CSV file per station, as the Vilnius file of Part 2. NCEI also packs all of
them into one archive. How long would your laptop need to find the hottest day
of every station: download the archive, unpack it, read every file? How much
would all your cores save, and would a cluster be faster? The addresses (NOAA
NCEI; terms under "Before the session"):

```text
https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/archive/daily-summaries-latest.tar.gz
https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt
https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/ACW00011604.csv
https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/LH000026603.csv
```

The archive is about 8 GB: do not download it. `curl -sI` reads only its
headers, its size among them. The station list has one line per station; the
last two are the files of a station in Antigua with seven months of 1949
(40 kB) and of Nida (1.2 MB).

Work in pairs, with any tools, an LLM too: the work is the measurements, the estimate and the checks.

1. **Predict**, before any measurement: the time for all stations on one
   core, in minutes or hours, and which part will take longest: the
   download, the unpacking or the reading. One reason for each.
2. **Solve.** Measure what you need on the files you have, scale it up,
   and give the time on one core and with all your cores, as a range.
3. **Check the machine's work.**
    - The hottest day of Vilnius: is it plausible? A value from the file
      flagged as failing a quality check gives 198.0 °C (27 August 1911);
      the hottest day that passed is 35.4 °C.
    - The model: predict the time of the Nida file from the other two,
      then measure it.
    - The units: is curl's speed in bytes or in bits? A network sold as
      100 Mbit/s moves at most 12.5 MB a second.
    - The size of the whole: two different ways to estimate it; do they
      agree within a factor of two?
    - Against your prediction: which part did you misjudge, and why?
4. **Hand in** the time on one core and with all cores, each as a range,
   and two sentences: what limits it, and whether a cluster would help.

??? tip "Hint 1: two files give the cost of a file and of a byte"
    Reading a file costs a fixed part (opening it, starting the parser) and
    a part that grows with its size: t = a + b × size. The 40 kB file of
    Antigua is almost all a; the Vilnius file gives b. Time each five times
    and keep the smallest, as in section 3.

??? tip "Hint 2: the size of the whole"
    The archive is packed with gzip: its size times how well a CSV file
    packs is the size unpacked. `gzip.compress(data)` packs bytes as gzip
    does; three files pack differently. Or: the number of stations times
    the size of a typical file. Is Vilnius, with 145 years, typical?

??? tip "Hint 3: what more cores do not speed up"
    The download comes through one network connection, and gzip unpacks on
    one core. Only the reading of the files splits over workers; section 5
    measured how well.

??? note "One solution"
    The sizes, without downloading the archive, and the two station files:

    ```text
    $ curl -sI https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/archive/daily-summaries-latest.tar.gz | grep -i content-length
    Content-Length: 8100138197
    $ curl -O https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt
    ...
    $ wc -l ghcnd-stations.txt
    133041 ghcnd-stations.txt
    $ curl -O https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/ACW00011604.csv
    ...
    $ curl -O https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/LH000026603.csv
    ...
    ```

    The hottest day of each file, five times, the smallest time; how well
    each file packs, and how fast it unpacks:

    ```python title="measure.py"
    import gzip
    import sys
    import time
    from pathlib import Path

    import pandas as pd


    def hottest(path):
        """Date and °C of the hottest day; values with a quality flag left out."""
        df = pd.read_csv(path, low_memory=False)
        flag = df["TMAX_ATTRIBUTES"].str.split(",").str[1]   # "" if it passed
        good = df[df["TMAX"].notna() & (flag == "")]
        row = good.loc[good["TMAX"].idxmax()]
        return row["DATE"], float(row["TMAX"]) / 10


    for name in sys.argv[1:]:
        data = Path(name).read_bytes()
        times = []
        for run in range(5):
            start = time.perf_counter()
            day, celsius = hottest(name)
            times.append(time.perf_counter() - start)
        packed = gzip.compress(data)
        start = time.perf_counter()
        gzip.decompress(packed)
        unpack = len(data) / (time.perf_counter() - start) / 1e6
        print(f"{name}: {len(data) / 1e6:.2f} MB, {min(times) * 1000:.1f} ms, "
              f"packed 1/{len(data) / len(packed):.1f}, "
              f"unpacks {unpack:.0f} MB/s, hottest {day} {celsius} °C")
    ```

    ```text
    $ python measure.py LH000026730.csv ACW00011604.csv LH000026603.csv
    LH000026730.csv: 6.12 MB, 38.2 ms, packed 1/11.6, unpacks 837 MB/s, hottest 1959-07-13 35.4 °C
    ACW00011604.csv: 0.04 MB, 1.1 ms, packed 1/21.4, unpacks 908 MB/s, hottest 1949-04-25 30.6 °C
    LH000026603.csv: 1.24 MB, 7.1 ms, packed 1/17.6, unpacks 778 MB/s, hottest 2014-07-29 32.8 °C
    ```

    From Antigua and Vilnius: b = (38.2 − 1.1) ms / (6.12 − 0.04) MB =
    6.1 ms per MB, a = 1.1 − 0.04 × 6.1 = 0.9 ms. For Nida that predicts
    0.9 + 1.24 × 6.1 = 8.5 ms; measured 7.1 ms. The estimate:

    ```python title="estimate.py"
    # What this computer measured today; put in your own numbers.
    ARCHIVE = 8.100e9    # bytes: curl -sI of the archive, Content-Length
    STATIONS = 133_041   # wc -l ghcnd-stations.txt
    SPEED = 3.7e6        # bytes a second: curl's Average Speed, 3602k
    PER_FILE = 0.9e-3    # seconds: Antigua's 40 kB file, nearly all overhead
    PER_BYTE = 6.1e-9    # seconds: (38.2 - 1.1) ms / (6.12 - 0.04) MB
    UNPACK = 800e6       # bytes a second, gzip on one core
    SPEED_UP = 6.0       # pool.py: 4.62 s with 1 worker, 0.77 s with 8

    download = ARCHIVE / SPEED
    for ratio in [11.6, 17.6, 21.4]:      # how well the three files packed
        unpacked = ARCHIVE * ratio
        unpack = unpacked / UNPACK
        scan = STATIONS * PER_FILE + unpacked * PER_BYTE
        print(f"packed 1/{ratio}: {unpacked / 1e9:.0f} GB unpacked")
        print(f"  download {download / 60:.0f} min, unpack {unpack / 60:.0f} min, "
              f"scan {scan / 60:.0f} min on 1 core, {scan / 60 / SPEED_UP:.0f} "
              f"on 8 workers")
        one = download + unpack + scan
        eight = download + unpack + scan / SPEED_UP
        print(f"  in all {one / 60:.0f} min, or {eight / 60:.0f} with 8 workers")
    ```

    ```text
    $ python estimate.py
    packed 1/11.6: 94 GB unpacked
      download 36 min, unpack 2 min, scan 12 min on 1 core, 2 on 8 workers
      in all 50 min, or 40 with 8 workers
    packed 1/17.6: 143 GB unpacked
      download 36 min, unpack 3 min, scan 16 min on 1 core, 3 on 8 workers
      in all 56 min, or 42 with 8 workers
    packed 1/21.4: 173 GB unpacked
      download 36 min, unpack 4 min, scan 20 min on 1 core, 3 on 8 workers
      in all 60 min, or 43 with 8 workers
    ```

    On this computer all stations take 50 to 60 minutes on one core and 40
    to 43 minutes with eight workers. The download, 36 minutes at 3.7 MB a
    second, is most of it and does not split; eight workers shorten only
    the reading, from 12–20 to 2–3 minutes.

**With your own project data:** how long would your analysis take on ten or
a hundred times the data you have now? Time its parts on what you have, find
what each part grows with, and say which part sets the limit.

---

## Part 4 · Show and discuss { #part-4 }

### 9. Three questions about the pairs' estimates { #discuss }

<!-- 1:45 · 15 min -->

Two or three pairs show their numbers and read their two sentences.

**Ask the room:** one pair estimates 13 hours, another about one hour, from the same measurements. Where can a factor of ten come from?

??? note "Answer"
    From the size of the whole. 133 041 stations × 6.1 MB, as if every
    station were Vilnius, is 814 GB. Vilnius is one of the longest records:
    NCEI's listing of the folder of station files gives the true sizes, and
    fewer than 3000 files are larger.

    ```python title="listing.py"
    import re
    import statistics
    import urllib.request

    URL = ("https://www.ncei.noaa.gov/data/"
           "global-historical-climatology-network-daily/access/")
    with urllib.request.urlopen(URL) as response:     # 20 MB of HTML
        page = response.read().decode()
    # each file is a table row: its name, the date it changed, its size in bytes
    sizes = [int(size) for size in re.findall(
        r'\.csv</a></td>\s*<td[^>]*>[^<]*</td>\s*<td[^>]*>(\d+)</td>', page)]
    print(f"{len(sizes)} station files, {sum(sizes) / 1e9:.1f} GB")
    print(f"mean {statistics.mean(sizes) / 1e6:.2f} MB, "
          f"median {statistics.median(sizes) / 1e6:.2f} MB, "
          f"largest {max(sizes) / 1e6:.1f} MB")
    print(f"files larger than Vilnius: {sum(s > 6_119_696 for s in sizes)}")
    ```

    ```text
    $ python listing.py
    132895 station files, 147.5 GB
    mean 1.11 MB, median 0.47 MB, largest 20.4 MB
    files larger than Vilnius: 2952
    ```

    147.5 GB lies between the estimates from the three files (94 to
    173 GB), close to the one from Nida (143 GB). The files change every
    day, so the numbers grow a little.

**Ask the room:** a laptop with twice the cores: twice as fast?

??? note "Answer"
    No. On this computer the reading on one core is 12 to 20 of the 50 to
    60 minutes; the download and the unpacking, about 40 minutes, stay as
    they are. Eight workers bring the whole from about 56 to 42 minutes,
    a speed-up of 1.3, and no number of cores brings it below 39.

**Ask the room:** would a cluster be faster?

??? note "Answer"
    For the reading, yes: a hundred cores read the files in seconds. But
    the download sets the time: 8.1 GB over the same network take as long
    as on the laptop. A cluster helps when the data is already near it, or
    comes over a faster link; that is why the LHC sends jobs to the
    computing centres that hold the data. The unpacked files, about
    147 GB, may not fit on a laptop's disk at all: Python's `tarfile` can
    read the archive file by file as it arrives, and then the download and
    the reading overlap.

Measure each part on a small sample, scale each by what it grows with, and the largest part that does not split sets the time, however many cores there are.

---

## Optional, if the room is fast { #optional }

### 10. Is Vilnius a typical station? Twenty stations drawn at random { #sample }

<!-- — · 15 min -->

A random sample of the station list gives the size of a typical file, and its
uncertainty, without the 20 MB listing. The script downloads 20 station files,
about 26 MB.

??? note "One solution"
    ```python title="sample.py"
    import random
    import statistics
    import time
    import urllib.request

    import pandas as pd

    ACCESS = ("https://www.ncei.noaa.gov/data/"
              "global-historical-climatology-network-daily/access/")
    with open("ghcnd-stations.txt") as handle:
        stations = [line[:11] for line in handle]
    chosen = random.Random(2026).sample(stations, 20)
    sizes, seconds = [], []
    for station in chosen:
        with urllib.request.urlopen(ACCESS + station + ".csv") as response:
            data = response.read()
        with open(station + ".csv", "wb") as out:
            out.write(data)
        start = time.perf_counter()
        df = pd.read_csv(station + ".csv", low_memory=False)
        if "TMAX" in df:
            hottest = df["TMAX"].max()        # the work of the scan, flags aside
        seconds.append(time.perf_counter() - start)
        sizes.append(len(data))
    mean = statistics.mean(sizes)
    error = statistics.stdev(sizes) / len(sizes) ** 0.5
    print(f"20 stations: mean {mean / 1e6:.2f} ± {error / 1e6:.2f} MB a file, "
          f"{sum(sizes) / sum(seconds) / 1e6:.0f} MB/s")
    print(f"all {len(stations)}: {len(stations) * mean / 1e9:.0f} "
          f"± {len(stations) * error / 1e9:.0f} GB")
    ```

    ```text
    $ python sample.py
    20 stations: mean 1.31 ± 0.48 MB a file, 138 MB/s
    all 133041: 174 ± 64 GB
    ```

    Twenty stations give 174 ± 64 GB; the listing gives 147.5 GB, within
    the error. Thirteen of the twenty files are from the United States, as
    are 78 570 of the 133 041 stations, and thirteen hold no `TMAX` at all,
    only rain and snow.

---

## Aims practised

- ⚙️ **Automation:** a job that runs in the background and writes its log
  line by line; the same function run by one worker or eight.
- ♻️ **Reproducibility:** every time is the smallest of five, written down
  with the machine it ran on; the estimate is a script whose numbers can be
  replaced by the next laptop's.
- 📁 **Data & files:** the size of a file as text, packed, in memory and as
  binary numbers, and what each costs to read.
