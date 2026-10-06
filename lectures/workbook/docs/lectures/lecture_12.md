# 12: Pandas & Data Cleaning

Lectures 9 to 11 computed with tables that were already in order: a mean, a
fit, a trained neuron. Lecture 12 is about how a table gets into that state.
It opens on a second pendulum file from the lab partner. The script handed
out in Lecture 4, `clean_pendulum.py`, makes the four edits of Lecture 2 as
text. On this file it writes 10 rows for nine lengths with no warning: a
`Mean` row and an empty time pass through. The lecture writes the cleaning
again with Pandas, as rules about what a column holds. The new script gives
the same 97 bytes as Lecture 4's on the first file and 9 rows on the second.
The method is then used on the file with 91 583 rows, and the lecture closes
on the second file with five checks and a count for each. The new tool is
Pandas. NumPy arrays, masks and `np.loadtxt` are known from Lecture 7 and are
used without introduction.

## What the lecture covers

0. **The opening** — the partner's second file, `pendulum_run2.csv`, and
   what Lecture 4's script writes from it: 10 rows, a `Mean` row kept, the
   missing time as an empty piece of text.
1. **Cleaning by script** — `np.loadtxt` fails on the raw file;
   `pd.read_csv` with `sep=";"` and `decimal=","`; what the types of the
   columns say about the file; a mask for the row that is not a measurement;
   `drop`, `astype`, `to_csv`; the output compared with Lecture 4's as a
   table and as bytes; the script `scripts/clean.py`; the same script on the
   second file, and the two scripts side by side.
2. **The DataFrame** — columns, index and types; a DataFrame from a dict;
   one column and several; rows by position and by label; masks; a new
   column computed from others; sorting and summary numbers, and why g has
   three uncertainties in Lectures 9, 10 and 12.
3. **A real file** — `D0_KPi.csv` read, its types and its size in memory;
   `describe()`; the code −100 of Lecture 7 in a histogram, then turned into
   NaN and kept in the table; how NaN behaves in a mean and in a comparison;
   which rows have the gap, and three reasons a value can be missing.
4. **Data quality** — a documented case of a spreadsheet error; impossible
   values; outliers and the 1.5 × IQR rule; duplicates; consistency and
   units; mixed units in one column; the five questions on one slide, each
   with its line of Pandas and its result on both files.
5. **The cleaned table** — one mask per rule; the script and its log; what
   the script changed and what it left alone; a derived column and
   `groupby`.
6. **Reshape & join** — tidy tables; `melt`; `concat`; `merge`, and what a
   join does to the number of rows.
7. **The close** — the second file again: the five questions, each with
   its line and its answer.

The section CSV or Parquet is parked in
`lectures/content/parked/12_Pandas_and_Data_Cleaning.md`.

## The numbers on the slides

Every number about `pendulum.csv` and `D0_KPi.csv` comes from
`figures/src/cleaning.py`:

```text
python figures/src/cleaning.py                    the numbers
python figures/src/build.py --only cleaning       the five figures
```

The first command needs NumPy and Pandas, the second NumPy and Matplotlib.

| Fact | Value |
|--|--|
| Hand-cleaned `pendulum.csv`, and Lecture 4's `pendulum_script.csv` | 97 bytes, SHA-256 `be05af03…fff0870b` |
| The script's output with `to_csv` defaults | 95 bytes: `17.9` and `19.1` for `17.90` and `19.10`; 105 on Windows (CR LF) |
| The script's output with `float_format="%.2f"` and `lineterminator="\n"` | identical to the hand-cleaned file |
| `pendulum_run2.csv`, raw | 11 lines, 125 bytes, SHA-256 `2e04cdeb…b1659754`; `Mean` line, no time at 80 cm |
| Lecture 4's script on it | `10 rows written`, 103 bytes, ends in `80,` and `Mean,14.80` |
| `clean.py` on it | `9 rows written`, 92 bytes, one gap at 80 cm |
| Mean of its eight times | 118.41 / 8 = 14.80125, the file says `14,80`; with the gap as 0, 13.16 |
| g from its eight rows | 9.73 to 9.86 m/s², median 9.76 |
| `D0_KPi.csv` | 91 583 rows, 3 926 142 bytes, SHA-256 `25c3c972…c1505136` |
| `TAU = -100` | 49 rows |
| Mean of `TAU` with and without the code | −0.0525 and 0.000982 ns |
| Negative `TAU` | 3 rows: labels 22854, 35318, 42860 |
| `M` outside 1800 to 1930 | 2 rows: labels 10046 and 89859 |
| Duplicate rows | 0 |
| `d0_clean.csv` | 91 578 rows, 3 925 641 bytes, SHA-256 `7aa9470b…3bb91b16` |

The second file is made by `lectures/workbook/docs/data/pendulum_run2.py`,
which writes `pendulum_run2_raw.csv` (students save it as
`data/raw/pendulum_run2.csv`). The numbers for it were checked by running
both scripts on it, in `zsh` with Pandas 3.0.1 and in Windows PowerShell 7
with Pandas 3.0.6: the same rows and the same bytes.

The code and output on the slides for the two files were run with Pandas
2.3.3 and checked with Pandas 3.0.6. The one visible difference: a column of
text has the type `object` up to Pandas 2 and `str` from Pandas 3 on. The
runnable fences use the Pandas of the browser, 2.2.0, and build their small
tables in the code, because the browser has no project folder.

## The lecture in 90 minutes

The lecture is slides 1–61 and estimates about 143 min. Slides 62–68 are
the self-check quizzes and take no lecture time. In a 2-hour slot, skip the
section Reshape & Join or leave it for the room to read. For a 90-minute
slot, skip the slides in the second table. To jump, type the slide number
and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–6 | Opening: the partner's second file, what Lecture 4's script wrote, objectives |
| 0:08 | 7–17 | The first file by Pandas, compared with Lecture 4's output; the second file by rule (the opening is answered at slide 16) |
| 0:33 | 19–22, 24–25 | The DataFrame: columns, masks, a new column |
| 0:44 | 27–30, 32–33, 35–37 | The real file: types, `describe()`, the code −100 kept as NaN, the comparison with NaN, the gaps |
| 1:03 | 38–40, 43–44, 46 | Data quality and the five questions |
| 1:15 | 48–50, 52 | The cleaning script, its log, `groupby` |
| 1:24 | 60–61 | The second file, five questions; Recap |
| 1:28 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| The Cleaning in the Browser | 18 | 4 min |
| Rows: Position and Label; Sort and Summarise | 23, 26 | 8 min |
| The Code in a Histogram; How NaN Behaves | 31, 34 | 5 min |
| Outliers and the 1.5 × IQR rule | 41–42 | 4 min |
| Mixed Units in One Column; The Checklist as a Function | 45, 47 | 7 min |
| What the Script Changed; The Groups in a Picture | 51, 53 | 4 min |
| Reshape & Join | 54–59 | 18 min |

- **Do not cut** slides 3–4 (the opening), 8–17 (the file read three
  times, the row, the column, the type, the comparison, the script, the
  second file), 30, 32–33 and 35 (`describe()`, the code kept as NaN, the
  comparison with NaN), 46 (the five questions), 49–50 (the masks and the
  log), and **slide 60, the closing slide**: it answers the opening on the
  same file. The seminar writes the script of slide 15 as
  `scripts/clean.py`, runs both scripts on the second file as on slides 4
  and 16, asks the five questions of slide 46 in `audit.py`, and writes the
  script of slide 50.
- **Slides 3–4** need the room's eyes first: show the file, ask how many
  rows the script should write, then run it. Lecture 4's script is
  `scripts/clean_pendulum.py` from Lecture 4 and Seminar 4; the second file
  is [`pendulum_run2_raw.csv`](../data/pendulum_run2_raw.csv){ download="pendulum_run2.csv" },
  saved as `data/raw/pendulum_run2.csv`.
- **Slides 8–15 are shown live** in VS Code: type the script of slide 15
  line by line, run it after each line, and compare its output with
  Lecture 4's `pendulum_script.csv` by checksum in the terminal (`shasum -a
  256` on macOS, `Get-FileHash` in PowerShell).
- **Slide 13** has the point that is easy to rush: the two files are equal
  as tables and differ as bytes, 95 against 97. Let the room find the two
  lines before slide 14 repairs them.
- **Slide 16** changes `RAW` and `OUT` in `scripts/clean.py` to the second
  file and runs it: 9 rows, the `Mean` line dropped by the rule on `nr`,
  the missing time kept as a gap.
- **Slide 26** reconciles g: 9.80 ± 0.03 from the scatter of the nine
  values here, 9.80 ± 0.04 weighted in Lecture 9, 9.84 ± 0.09 from the fit
  in Lecture 10. Three methods, three uncertainties.
- **Slide 32**: ask which of the four means changes before showing the
  output. Only `TAU`, from −0.0525 to 0.000982, the numbers of Lecture 7.
- **Slide 35**: ask for the number of rows of `df[df["TAU"] >= 0]` before
  showing it. The answer, 91 531, is 52 fewer than the file and not 3.
- **The runnable fences** (slides 18, 21–26, 34, 43, 45, 47, 56–59) load
  Python into the browser at the first click. That takes a while and needs
  the network. Click Run on slide 21 before the lecture starts. Each fence
  fits its slide with the output open.
- **Slide 39** (the documented case) can be told in one minute. Its place
  is before the checklist, as the reason for having one.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 62–68: six quiz slides for students to try afterwards. The same
questions, with their answers:

1. A column holds 1000 temperatures. 990 have a mean of 20.0 and 10 cells
   hold the code −999. What does `mean()` give before the code is replaced?
   *9.81. The sum is 990 × 20 − 9990 = 9810. One cell in a hundred halves
   the mean.*
2. `s = pd.Series([4.0, np.nan, 8.0])`. What are `s.mean()`, `s.count()`
   and `(s > 5).sum()`?
   *6.0, 2 and 1. The mean and the count leave NaN out, and NaN > 5 is
   False.*
3. After `read_csv` a column `mass` has the type `object` (`str` in
   Pandas 3), and every value on the screen is a number. Why?
   *At least one cell is not a number: a word, a unit or a decimal comma. A
   column has one type, and `head()` shows five rows only.*
4. `describe()` gives 25 % = 10 and 75 % = 14. Which of 3, 5, 19 and 21
   does the 1.5 × IQR rule flag?
   *3 and 21. IQR = 4, the fences are 4 and 20.*
5. Table `a` has the keys 1 to 5, table `b` the keys 2, 3, 3, 6. How many
   rows has `a.merge(b, on="key", how="left")`?
   *6. Keys 1, 4 and 5 give one row each with NaN, key 2 one row, key 3 two
   rows.*
6. A table is saved with `df.to_csv("clean.csv")` and read again. It has
   one column more. Where from?
   *`to_csv` wrote the index as a first column. `index=False` writes only
   the columns of the table.*

## Paired seminar

[Seminar 12 — Clean a Table by Script](../seminars/seminar_12.md) installs
Pandas and writes three scripts. The first, `scripts/clean.py`, cleans the
pendulum table with Pandas, as on slide 15, and gives a file with the same
checksum as Lecture 4's `pendulum_script.csv`. Both scripts are then run on
the partner's second file: 10 rows from Lecture 4's, 9 from `clean.py`.
`audit.py` asks the five questions of `D0_KPi.csv` and prints a count for
each. `clean_d0.py` writes `data/processed/d0_clean.csv` and a log of what
it removed. The rules and the counts go into the README. Everything is done
in class.

## Take-aways

- A script that edits text repeats the edits and nothing more: on the
  partner's second file Lecture 4's script wrote 10 rows with no warning. A
  script that cleans by rule (a measurement has a row number) dropped the
  `Mean` line whatever its spelling, kept the missing time as a gap, and
  wrote 9 rows.
- A script is the written-down form of a cleaning. It can be read, run
  again, and checked: the same input gives the same bytes.
- Raw data is read and never written. Everything in `data/processed/` can
  be deleted and made again.
- `read_csv` has to be told the separator and the decimal sign. The types
  it returns are the first check: a numeric column that came back as text
  holds a cell that is not a number.
- A code for a missing value, such as −100, is a number to every sum. 49
  rows in 91 583 turned a mean of 0.000982 into −0.0525. Replace the code
  by NaN before computing anything.
- NaN is left out of a mean and makes every comparison False. A mask
  written for the good rows also drops the rows with gaps. Write the mask
  for the bad rows and turn it round.
- Five questions for any table: is every cell filled, can every value be
  true, is each row there once, do the parts agree, is a typical value the
  right size.
- A rule for outliers flags rows. Whether a flagged row is an error is a
  decision, and the decision is written beside the line that applies it.
- Every rule of a cleaning script has a reason and a count. The counts go
  into the README.
- A join can add gaps and can double rows. Count the rows before and
  after.
