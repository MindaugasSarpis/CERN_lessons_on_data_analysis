<!--
Parked slides from slides/12_Pandas_and_Data_Cleaning.md, taken out on 2026-10-06.

The lecture now opens on the lab partner's second file
(lectures/workbook/docs/data/pendulum_run2_raw.csv, made by pendulum_run2.py)
and the script handed out in Lecture 4, and it closes on the same file. The
slides below stood in the way of that story or repeated an earlier lecture. A
comment before each slide says where it stood. To restore one, move it back
into the lecture file.
-->

<!-- Parked 2026-10-06 from Lecture 12, section Cleaning by Script, first slide after 'Cleaning by Script' (section): the room did not clean the table by hand (Seminar 1 Part 3 was not done), and Lecture 4 already ran a script that makes the four edits -->

---
hideInToc: true
---

# The Pendulum Table, Cleaned **by Hand**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 📥 **`data/raw/pendulum.csv`**

```text
nr;length_cm;t10_s
1;20;9,02
2;30;11,05
…
9;100;20,01
;mean;15,14
```

</div>

<div class="card card-primary card-glass pad-compact">

## ✍️ **Four edits in the editor**

1. The line with the mean deleted: 1 line
2. `,` replaced by `.`: 9 places
3. `;` replaced by `,`: 20 places
4. The column `nr` deleted with a cursor on every line: 10 lines

The result is `data/processed/pendulum.csv`: ten lines, 97 bytes.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The README lists the four edits. A list can be read. It cannot be run. When the lab partner sends the table for 200 lengths, every edit is made again, and nothing checks that it was made the same way.

</div>

<!--
Speaker: ask the room what they would do if the same partner sent a second
file tomorrow. The honest answer is: the same four edits, from memory. (~2 min)
-->

<!-- Parked 2026-10-06 from Lecture 12, section A Real File, after 'describe(): Eight Numbers per Column': the same arithmetic as Lecture 7's 'What 49 Rows Do to a Mean'; replaced by 'Lecture 7's Mask, Kept in the Table' -->

---
hideInToc: true
---

# 49 Rows Move the **Mean**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔎 **The value −100**

```python
print((df["TAU"] == -100).sum())
```

```text
49
```

`TAU = -100` is this file's code for *no decay time was computed*. The mask `TAU != -100` kept 91 534 rows of the array. The other 49 are 0.054 % of the file.

</div>

<div class="card card-secondary card-glass pad-compact">

## ➗ **The mean, by hand**

```text
49 rows × (−100)       −4900.000
91 534 other rows         +89.868
sum of TAU             −4810.132

−4810.132 / 91 583  =  −0.0525
    89.868 / 91 534  =   0.000982
```

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ One row in about 1900 turns a mean of 0.000982 ns into −0.0525 ns and a standard deviation of 0.0044 into 2.31. The median barely moves: 0.0002723 against 0.0002725. A code for a missing value is a number, and every sum counts it.

</div>

<!--
Speaker: nothing warned. describe() ran, a fit would run, a histogram would
be drawn. With the array the code had to be masked out by hand in every
calculation. The check is to look at min and max of every column and ask
whether such a value can be measured. (~3 min)
-->

<!-- Parked 2026-10-06 from Lecture 12: the section CSV or Parquet (section slide and one slide), after 'A Join Changes the Row Count' and before the Recap. The deck closes on the second pendulum file instead; Lecture 7 made the text-against-binary point -->

---
layout: section
hideInToc: true
---

# CSV or **Parquet**

<!--
Speaker: one more file format, in two slides. CSV stays the format of this
course. Parquet is what the same table looks like when programs, not people,
are the readers. (~1 min)
-->

---
hideInToc: true
---

# The Same Table as **Parquet**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 💾 **Write, read, compare**

```python
clean = pd.read_csv("data/processed/d0_clean.csv")
out = "data/processed/d0_clean.parquet"
clean.to_parquet(out)
back = pd.read_parquet(out)
print(back.equals(clean))
```

```text
True
```

Pandas needs one more library for this format: `python -m pip install pyarrow`. Without it `to_parquet` stops with `ImportError: Unable to find a usable engine`.

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## ⚖️ **`d0_clean`, 91 578 rows**

| | CSV | Parquet |
| --- | --- | --- |
| Form | text, row by row | binary, column by column |
| Reader | any editor | programs only |
| Types | found at each read | stored in the file |
| Gap | an empty cell | stored as missing |
| Size | 3.9 MB | 3.3 MB |
| Read | 18 ms | 2 ms |

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Parquet stores each column with its type, so nothing is guessed at reading and one column can be read without the others. The numbers of this file have many digits, and the file is only about 15 % smaller. CSV is the format a person can open and check. Parquet is for large tables that programs pass on.

</div>

<!--
Speaker: the times are from one laptop and the size depends a little on the
version of pyarrow. The order is what matters: a few times faster to read, and
no separator, decimal sign or missing-value code to state. (~2 min)
-->
