# 12: Pandas & Data Cleaning

Lectures 9 to 11 computed with tables that were already in order: a mean, a
fit, a trained neuron. Lecture 12 is about how a table gets into that state.
It goes back to the small pendulum table that was repaired by hand in the
editor in Lecture 2, does the same repair as a script, and then applies the
method to the file with 91 583 rows. The new tool is Pandas. NumPy arrays,
masks and `np.loadtxt` are known from Lecture 7 and are used without
introduction.

## What the lecture covers

1. **Cleaning by script** — the four hand edits of the pendulum table;
   `np.loadtxt` fails on the raw file; `pd.read_csv` with `sep=";"` and
   `decimal=","`; what the types of the columns say about the file; a mask
   for the row that is not a measurement; `drop`, `astype`, `to_csv`; the
   output compared with the hand-cleaned file as a table and as bytes; the
   script, and what it gives that the editor did not.
2. **The DataFrame** — columns, index and types; a DataFrame from a dict;
   one column and several; rows by position and by label; masks; a new
   column computed from others; sorting and summary numbers.
3. **A real file** — `D0_KPi.csv` read, its types and its size in memory;
   `describe()`; how 49 rows with the code −100 move the mean; the code
   turned into NaN; how NaN behaves in a mean and in a comparison; which
   rows have the gap, and three reasons a value can be missing.
4. **Data quality** — a documented case of a spreadsheet error; impossible
   values; outliers and the 1.5 × IQR rule; duplicates; consistency and
   units; mixed units in one column; the five questions on one slide, each
   with its line of Pandas and its result on both files.
5. **The cleaned table** — one mask per rule; the script and its log; what
   the script changed and what it left alone; a derived column and
   `groupby`.
6. **Reshape & join** — tidy tables; `melt`; `concat`; `merge`, and what a
   join does to the number of rows.
7. **CSV or Parquet** — the same table in both formats, with sizes and
   read times.

## The numbers on the slides

Every number about the two files comes from `figures/src/cleaning.py`:

```text
python figures/src/cleaning.py                    the numbers
python figures/src/build.py --only cleaning       the five figures
```

The first command needs NumPy and Pandas, the second NumPy and Matplotlib.

| Fact | Value |
|--|--|
| Hand-cleaned `pendulum.csv` | 97 bytes, SHA-256 `be05af03…fff0870b` |
| The script's output with `to_csv` defaults | 95 bytes: `17.9` and `19.1` for `17.90` and `19.10` |
| The script's output with `float_format="%.2f"` | identical to the hand-cleaned file |
| `D0_KPi.csv` | 91 583 rows, 3 926 142 bytes, SHA-256 `25c3c972…c1505136` |
| `TAU = -100` | 49 rows |
| Mean of `TAU` with and without the code | −0.0525 and 0.000982 ns |
| Negative `TAU` | 3 rows: labels 22854, 35318, 42860 |
| `M` outside 1800 to 1930 | 2 rows: labels 10046 and 89859 |
| Duplicate rows | 0 |
| `d0_clean.csv` | 91 578 rows, 3 925 641 bytes, SHA-256 `7aa9470b…bb91b16` |

The code and output on the slides for the two files were run with Pandas
2.3.3 and checked with Pandas 3.0.6. The one visible difference: a column of
text has the type `object` up to Pandas 2 and `str` from Pandas 3 on. The
runnable fences use the Pandas of the browser, 2.2.0, and build their small
tables in the code, because the browser has no project folder.

## The lecture in 90 minutes

The lecture is slides 1–60 and estimates about 139 min. Slides 61–67 are
the self-check quizzes and take no lecture time. In a 2-hour slot, skip the
section Reshape & Join or leave it for the room to read. For a 90-minute
slot, skip the slides in the second table. To jump, type the slide number
and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–3 | Opening and objectives |
| 0:03 | 4–15 | The pendulum table by script, compared with the hand-cleaned file |
| 0:29 | 17–20, 22–23 | The DataFrame: columns, masks, a new column |
| 0:46 | 25–29, 31, 33–35 | The real file: types, `describe()`, the code −100, NaN |
| 1:04 | 36–38, 41–42, 44 | Data quality and the five questions |
| 1:18 | 46–50 | The cleaning script, its log, `groupby` |
| 1:27 | 60 | Recap |
| 1:29 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Try It: the Cleaning in the Browser | 16 | 4 min |
| Rows: Position and Label; Sort and Summarise | 21, 24 | 8 min |
| The Code in a Histogram; How NaN Behaves | 30, 32 | 5 min |
| Outliers and the 1.5 × IQR rule | 39–40 | 4 min |
| Mixed Units in One Column; The Checklist as a Function | 43, 45 | 7 min |
| The Groups in a Picture | 51 | 2 min |
| Reshape & Join | 52–57 | 18 min |
| CSV or Parquet | 58–59 | 3 min |

- **Do not cut** slides 7–14 (the file read three times, the row, the
  column, the type, the comparison, the script), 28–33 without 30 and 32
  (`describe()`, the code, NaN, the comparison with NaN), 44 (the five
  questions) or 47–48 (the masks and the log). The seminar writes exactly
  these three scripts.
- **Slides 7–14 are shown live** in VS Code: type the script of slide 14
  line by line, run it after each line, rename the hand-cleaned file and
  compare the checksums in the terminal.
- **Slide 12** has the point that is easy to rush: the two files are equal
  as tables and differ as bytes, 95 against 97. Let the room find the two
  lines before slide 13 repairs them.
- **Slide 29** is board work: 49 × (−100) = −4900, the other 91 534 values
  sum to 89.868, and −4810.132 / 91 583 = −0.0525.
- **Slide 33**: ask for the number of rows of `df[df["TAU"] >= 0]` before
  showing it. The answer, 91 531, is 52 fewer than the file and not 3.
- **The runnable fences** (slides 16, 19–24, 32, 41, 43, 45, 54–57) load
  Python into the browser at the first click. That takes a while and needs
  the network. Click Run on slide 19 before the lecture starts. Each fence
  fits its slide with the output open.
- **Slide 37** (the documented case) can be told in one minute. Its place
  is before the checklist, as the reason for having one.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 61–67: six quiz slides for students to try afterwards. The same
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
Pandas and writes three scripts. `clean_pendulum.py` repeats the hand
cleaning of the pendulum table and gives a file with the same checksum as
the hand-cleaned one. `audit.py` asks the five questions of `D0_KPi.csv`
and prints a count for each. `clean_d0.py` writes
`data/processed/d0_clean.csv` and a log of what it removed. The rules and
the counts go into the README. At home students audit and clean their own
dataset in the same way.

## Take-aways

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
