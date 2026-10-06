# 7: Python for Data & NumPy

Lecture 6 gave the language: values, types, loops, lists, dicts, strings and
the traceback, and one line of the data file was turned into four numbers.
Lecture 7 reads the whole file, 91 583 rows, and computes with it. It does
so twice: with lists and a loop, and then with a NumPy array, and it
measures what the second way gains.

## What the lecture covers

1. **One task, two ways** — the file `data/raw/D0_KPi.csv` and four
   questions: how many rows, the mean of `M`, the number of valid `TAU`, the
   mean of the valid `TAU`. The room guesses the fourth from the first three
   rows (0.41, 0.19 and 0.18 ps) and writes the guess on the board.
2. **Functions** — `def`, parameters and arguments, a default value,
   `return` against `print`, local names; the period of a pendulum and the
   parsing of one line as functions.
3. **Exceptions** — what a traceback through a function shows; `try` and
   `except`; the exceptions a data file raises; skipping and counting a bad
   row; why a bare `except:` hides errors.
4. **Files & the csv module** — reading and writing a text file with `with
   open` (91 584 lines: question 1); the working directory, run in zsh and in
   PowerShell; `pathlib`; `csv.reader`; four columns into four lists; a mean
   and a count by loop (questions 2 and 3); the script as two functions.
5. **From lists to arrays** — what one step of the loop costs; a list and an
   array in memory; installing and importing NumPy; the same task with an
   array; the two versions timed on the file.
6. **`dtype` & shape** — one type per array; `int8` wrapping around, worked
   by the weights of Lecture 3; `float32` against `float64` on the sum of
   the mass column, with the 1880.6490478515625 of Lecture 3; rows and
   columns.
7. **Indexing, slicing & masks** — index and slice in one and two
   dimensions; a slice is a view; a comparison gives a mask; `TAU != -100`
   keeps 91 534 rows; question 4 answered: the mean is 0.98 ps, the median
   0.27 ps, close to the guess, and −52.5 ps with the 49 marks left in;
   `&`, `|`, `~`.
8. **Arithmetic & broadcasting** — operators on whole arrays; *g* from the
   nine rows of the pendulum table, run in the browser; a worked 2-by-3
   example, then the rule for two shapes in one operation read off it;
   `axis`.
9. **Summary numbers & the histogram** — the mean and the standard
   deviation by hand and as array code, on the nine values of *g*; the four
   columns in numbers; `np.loadtxt` and its arguments; text against binary
   on disk; `np.histogram` on the 11 masses that Lecture 6 counted with a
   dict, then the mass column in 20 bins; the whole analysis as one script.
   The Recap answers the four questions and sets the loop against the array.

## The lecture in 90 minutes

The lecture is slides 1–63 and estimates about 137 min. Slides 64–70 are the
self-check quizzes and take no lecture time. In a 2-hour slot nothing is
skipped. For a 90-minute slot, skip the slides in the second table: the
estimate is then about 90 min. To jump, type the slide number and press
Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–8 | The file, the four questions and the guess; functions |
| 0:13 | 11–14 | One line as a function, exceptions, `try` and `except` |
| 0:20 | 18–24 | Text files, the working directory, `pathlib`, `csv`, the loop: questions 1–3 |
| 0:36 | 26–27, 29–31 | The cost of the loop, NumPy, the measured times |
| 0:45 | 33–35 | `dtype`, `int8` |
| 0:51 | 38, 40–44 | Two dimensions, masks, **question 4 answered** (slide 44, about 1:00) |
| 1:02 | 45, 47–49 | Combining masks, arithmetic, *g* from the pendulum table |
| 1:11 | 51–52, 54–55 | Broadcasting: the worked example, then the rule; mean and standard deviation |
| 1:18 | 60–63 | `np.histogram`, the mass column, the script, the Recap |
| 1:30 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Names Inside a Function Are Local, Try It — A Function for the Mean | 9–10 | 6 min |
| Exceptions in Data Files, Try It — Skip a Bad Row, Catch Only What You Expect | 15–17 | 8 min |
| The Script as Functions | 25 | 2 min |
| A List and an Array in Memory | 28 | 2 min |
| Try It — Time Both | 32 | 4 min |
| `float32` and `float64` on the Data File, Shape: Rows and Columns | 36–37 | 5 min |
| Index and Slice, as in a List | 39 | 2 min |
| Try It — Masks | 46 | 4 min |
| Functions on Whole Arrays | 50 | 2 min |
| `axis`: Down the Rows or Along Them | 53 | 2 min |
| The Four Columns in Numbers, Centre and Scale, `np.loadtxt` in Full, An Array on Disk | 56–59 | 10 min |

- **Do not cut** slide 63 (Recap — Four Questions, Two Ways): it answers
  the opening slide. Nor slides 19–24 (files, the working directory, `csv`,
  the loop), 40–44 (two-dimensional indexing, masks and the answer to
  question 4) or 60–61 (`np.histogram`). The seminar does exactly these
  steps.
- **Slide 3** (One Task, Two Ways): write the four questions on the board,
  and next to question 4 the guesses of the room. Most guess about 0.26 ps,
  the mean of the three rows shown. They stay on the board until slide 44
  and the Recap.
- **Slide 7** (Parameters, Arguments, Defaults) stays in: `delimiter=","`
  and `skiprows=1` in `np.loadtxt` are arguments given by name.
- **Slides 6–8** are typed live in VS Code, in a scratch file.
- **Slide 20** (A Path Starts at the Working Directory) is done live, in
  zsh or in PowerShell: run the script from the project folder, then
  `cd scripts` and run it again. The prompt shows the folder; the message is
  the same on both systems.
- **Slides 27, 31 and 63** show times measured on one laptop: an Apple M2
  Pro with Python 3.13 and NumPy 2.3, the median of 51 runs. On another
  laptop the times differ and the factors stay close.
- **Slide 44** (Question 4, Answered): take the guesses from the board
  first, and ask why the mean is four times the three rows before showing
  the table. The answer is the long tail: 1 453 decay times above 10 ps,
  1.6 % of the rows, carry 35 % of the sum.
- **Slide 51** (the 2-by-3 example): work the two additions on the board
  first. The results are `[[11 22 33] [14 25 36]]` and
  `[[101 102 103] [204 205 206]]`. The rule on slide 52 is read off them.
- **Slides 10, 16, 32, 46, 49 and 60** run Python in the browser. The first
  run takes a few seconds while Python loads. The browser has an older
  NumPy on a 32-bit system: an array of whole numbers has the `dtype`
  `int32` there and `int64` on a laptop.
- The data file is not in the browser. Results on the file are shown as
  code with the output of a run on a laptop.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 64–70: six quiz slides for students to try afterwards. The same
questions, with their answers:

1. A function is defined as `def double(x): x * 2`. What does
   `print(double(4))` print?
   *`None`. The body computes 8 and does nothing with it. Without `return`
   a call gives back `None`.*
2. `rows = ['3.5', 'x', '', '7']`. A loop adds `float(r)` to `total` inside
   `try`, and `except ValueError` adds 1 to `skipped`. What are `total` and
   `skipped` at the end?
   *10.5 and 2. `float('x')` and `float('')` raise `ValueError`. An empty
   string is not a number.*
3. What does `np.array([200], dtype=np.uint8) + 100` give?
   *`[44]`. A `uint8` holds 0 to 255. 300 needs nine bits, and the eight
   that stay are 44, which is 300 − 256. There is no error.*
4. `x = np.array([3, 8, -1, 5, -1, 9])`, and `-1` marks a missing value.
   What is `x[x != -1].mean()`?
   *6.25: the mask keeps 3, 8, 5 and 9, and 25 / 4 is 6.25. Without the
   mask the mean is 23 / 6 = 3.83.*
5. The array `a` has shape `(4, 3)`. Which of these cannot be added to it:
   an array of shape `(3,)`, of shape `(4, 1)`, of shape `(4,)`, or a
   single number?
   *The array of shape `(4,)`. Shapes are compared from the right, and 3
   against 4 does not fit. `(3,)` is used for every row, `(4, 1)` for every
   column.*
6. What are the counts of
   `np.histogram([0.5, 1.5, 1.7, 2.0, 3.0], bins=3, range=(0, 3))`?
   *`[1 2 2]`. The edges are 0, 1, 2, 3. A value on an edge goes to the bin
   on its right, so 2.0 is in the third bin. The last bin takes its right
   edge too, so 3.0 is counted.*

## Paired seminar

[Seminar 7 — The Whole File in Python](../seminars/seminar_07.md) reads
`D0_KPi.csv` with the `csv` module into lists inside a function and takes
a mean and a count by loop. The room then installs NumPy with `pip`, reads
the file with `np.loadtxt`, masks the missing values with `TAU != -100`,
counts rows in a mass window and in 20 bins, and writes the numbers to
`results/summary.txt`.

## Take-aways

- A function takes values in through its parameters and gives one back
  with `return`. A function that only prints gives back `None`.
- `try` and `except` handle the exception that is named. Every other
  exception still stops the program, and that is wanted.
- A relative path starts at the working directory, the folder the terminal
  is in, and not at the folder of the script.
- `pathlib` builds a path from its parts, and the same script runs on every
  system. `csv.reader` gives every row as a list of strings. Numbers are
  made with `float`.
- A list holds references to separate objects, 32 bytes for each float. An
  array holds the values themselves in one block, 8 bytes each, with one
  type for all.
- On the 91 583 rows, reading the file with NumPy is 3.4 times faster than
  the `csv` loop, and computing is 47 to 70 times faster.
- The `dtype` is an integer or a float of fixed width. An `int8` wraps
  around past 127 without an error. A running total in `float32` was off
  by 590 on the sum of the mass column.
- `data[row, column]` selects by position. A comparison gives a mask, and a
  mask counts rows with `.sum()` and selects them as an index.
- `TAU != -100` keeps 91 534 of the 91 583 rows. The 49 others turn the
  mean of `TAU` from +0.98 ps into −52.5 ps.
- The mean of the valid `TAU` is 0.98 ps and its median 0.27 ps: 84 % of
  the decay times lie below the mean. Before trusting a mean, print the
  `shape`, the `dtype`, the minimum, the maximum and the median.
- Two shapes fit in one operation if, compared from the right, their
  lengths are equal or one of them is 1.
- `np.histogram` returns the counts and the edges of the bins, one more
  edge than counts. The mass column has its fullest bin from 1860 to
  1865 MeV/c².
