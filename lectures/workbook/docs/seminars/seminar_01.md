# Seminar 1 — Get Started with VS Code and Markdown

**Paired lecture:** 02 Introduction to Data · **Format:** follow-along, from zero · **~120 min**
in class, 30 min at home

The seminar has four parts, in this order.

1. **VS Code.** The room installs Visual Studio Code, learns the parts of its
   window and builds a project folder.
2. **Markdown.** The room writes a first document: the README of that folder.
3. **Edit many lines at once.** A small table arrives in the wrong format. The
   room cleans a copy of it and turns it into a table in a short report.
4. **A real data file.** A file with 91 583 rows is opened in VS Code, and the
   README records where it came from.

It is the first hands-on session of the course and it starts from zero.
Today needs VS Code and a web browser. No Python, no Git, no terminal.

## How to use this page

This page is written for the person at the front. Students can follow the
same page.

- The **paragraph at the top of a section** is what to tell the room.
- The **numbered steps** are what to do on the projector. The room repeats
  each step on their own laptops.
- **You should now see** closes a section. Ask for hands: "who sees this?"
  Go on when about four in five have it. The rest get help from a neighbour.
- **Watch for** is the usual slip in that section.

Keys are written for Windows, with macOS in brackets: `Ctrl+S` (macOS
`Cmd+S`). Linux has the Windows keys. The one exception on this page is
named where it occurs.

| Clock | Section | The room ends with |
|--|--|--|
| | **Part 1 · VS Code** · 40 min | |
| 0:00 | [1. Install VS Code](#install) | VS Code running |
| 0:15 | [2. Open a folder](#open-folder) | The project folder open |
| 0:20 | [3. Explore the user interface](#interface) | Five regions named, the Command Palette used |
| 0:30 | [4. Create folders and a file](#folders) | The project skeleton and an empty README |
| | **Part 2 · Markdown** · 15 min | |
| 0:40 | [5. Write Markdown](#markdown) | A README with headings, a list, a table, a link |
| | **Part 3 · Edit many lines at once** · 30 min | |
| 0:55 | [6. Work with whole lines](#lines) | A table row copied, moved and deleted with one key each |
| 1:00 | [7. Find and replace](#replace) | A copy of the table with `,` between values and `.` as the decimal sign |
| 1:08 | [8. Put a cursor on every line](#cursors) | The first column deleted on all lines at once |
| 1:15 | [9. Make a table for a report](#report) | `results/report.md` with a title, the table and a plot |
| | **Part 4 · A real data file** · 30 min | |
| 1:25 | [10. Look at a data file](#data-file) | The file in `data/raw/`, rows counted, seen in a spreadsheet |
| 1:45 | [11. Record where the data came from](#provenance) | A **Data** section in the README |
| 1:55 | [12. Wrap up](#wrap-up) | The homework known |

In a 90-minute slot, stop after Part 3 and go to the wrap-up. Part 4 then
opens the next session. Every part starts from files the room already has, so
the session can also stop after Part 2.

## Prerequisites

For the room: a laptop and a web browser. Nothing installed, no programming
experience.

For you, before the session:

- Your own VS Code looks like a fresh installation: default theme, Side Bar
  on the left, no `analysis-project` folder yet. You build it with the room.
- A USB stick with the VS Code installers for Windows and macOS and with
  `D0_KPi.csv`, `pendulum_raw.csv` and `pendulum_plot.png`, in case the
  network fails.
- `D0_KPi.csv` opened once in the spreadsheet program on your laptop, so that
  you know which of the three outcomes in section 10 your computer shows.
- Sections 7 to 9 done once on your own laptop. They are short, and every key
  in them has to work under your fingers.
- This page open on a second device, or printed.

At the start, ask who has written code before. Seat each of them next to
someone who has not. The rule for the experienced one: explain, never take
the keyboard.

## Files for this seminar { #files }

Each file is the state that a step ends in. A student who lost a step
downloads it and goes on from there. A browser saves it under the name in
the second column.

| File | Saved as | The state at the end of |
|--|--|--|
| [`pendulum_raw.csv`](../data/pendulum_raw.csv){ download="pendulum.csv" } | `pendulum.csv` | Section 7, step 1: the table as received, for `data/raw/` |
| [`pendulum_replaced.csv`](../data/pendulum_replaced.csv){ download="pendulum.csv" } | `pendulum.csv` | Section 7: `,` and `;` replaced, for `data/processed/` |
| [`pendulum.csv`](../data/pendulum.csv){ download="pendulum.csv" } | `pendulum.csv` | Section 8: column `nr` deleted, for `data/processed/` |
| [`pendulum_report.txt`](../data/pendulum_report.txt){ download="report.md" } | `report.md` | Section 9, for `results/` |
| [`pendulum_plot.png`](../data/pendulum_plot.png){ download="pendulum_plot.png" } | `pendulum_plot.png` | Section 9, step 9, for `results/` |
| [`D0_KPi.csv`](../data/D0_KPi.csv) | `D0_KPi.csv` | Section 10, for `data/raw/` |
| [`project_README_s1.txt`](../data/project_README_s1.txt){ download="README.md" } | `README.md` | Section 11: the README of the whole seminar |
| [`project_after_s1.zip`](../data/project_after_s1.zip) | `project_after_s1.zip` | The seminar: the whole `analysis-project` folder |

The zip is for a student who missed the session. Unpack it, then
**File** > **Open Folder...** and pick `analysis-project`. Its README
still says *your name* and *one sentence*, so fill those in.

## Part 1 · VS Code { #part-1 }

**0:00 to 0:40 · sections 1 to 4**

The room ends this part with VS Code installed and a project folder open in
it. Nothing is typed into a file yet.

## 1. Install VS Code { #install }

**0:00 · 15 min**

VS Code is a free editor for text and code. It looks and behaves the same on
Windows, macOS and Linux, so every screen in the room shows the same thing.
Everything done today by clicking can be done in any other editor.

1. Open `code.visualstudio.com` in a browser and select the **Download**
   button for your system.

2. Install it.

    - **Windows:** run the downloaded installer and keep every default.
    - **macOS:** open the downloaded file and drag **Visual Studio Code**
      into the **Applications** folder.

3. Start VS Code.

4. If a **Chat** panel is open on the right, close it with the **X** in its
   corner. It is not used today.

You should now see a window with a **Welcome** tab.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: the installer asks for an administrator password | Take the **User Installer** from the download page. It needs none |
    | macOS: "cannot be opened because it is from an unidentified developer" | The file was opened from **Downloads**. Drag it to **Applications** first |
    | macOS: VS Code is gone after a restart | It was started from the downloaded archive. Drag it to **Applications** |
    | A university or work laptop blocks the installation | Use [vscode.dev](https://vscode.dev) in Chrome or Edge today. It can open a local folder. Install at home |
    | The download is slow | Pass round the USB stick |

## 2. Open a folder { #open-folder }

**0:15 · 5 min**

VS Code can open a single file, but it is made to work on a folder. That
folder is the project: everything that belongs to one piece of work lives in
it. For Excel users: a project folder is what a workbook is in Excel, except
that every sheet is a separate file.

1. In the file manager (File Explorer on Windows, Finder on macOS), create a
   folder named `analysis-project`, for example in **Documents**.

2. In VS Code select **File** > **Open Folder...** and pick
   `analysis-project`.

3. If a dialog asks whether you trust the authors, select
   **Yes, I trust the authors**.

You should now see the title `ANALYSIS-PROJECT` on the left, with nothing
under it.

## 3. Explore the user interface { #interface }

**0:20 · 10 min**

The window has five regions. Point at each one on the projector and name it.

```text
+---+-------------+------------------------------------+
|   |             |                                    |
| 1 |      2      |                 3                  |
|   |             |                                    |
|   |             +------------------------------------+
|   |             |                 4                  |
+---+-------------+------------------------------------+
|                          5                           |
+------------------------------------------------------+
```

| | Region | What it is for |
|--|--|--|
| 1 | Activity Bar | A column of icons. Each one switches what the Side Bar shows |
| 2 | Side Bar | The files of the project. This view is called the **Explorer** |
| 3 | Editor | The file you are working on. Several files open as tabs |
| 4 | Panel | Hidden at first. It holds the terminal, which is used in later weeks |
| 5 | Status Bar | Facts about the open file |

1. Select the icons of the Activity Bar one after another and watch the Side
   Bar change. Finish on the top icon, the **Explorer**.

2. Press `Ctrl+B` (macOS `Cmd+B`) twice. The Side Bar hides and comes back.

3. Press `Ctrl+Shift+P` (macOS `Cmd+Shift+P`). This is the
   **Command Palette**: a search box for everything VS Code can do.

4. Type `theme` and select **Preferences: Color Theme**. Move through the
   list with the arrow keys and press Enter on the theme you like.

5. Press `Ctrl+=` (macOS `Cmd+=`) to make everything larger and `Ctrl+-`
   (macOS `Cmd+-`) to make it smaller. Set your own zoom for the projector
   now.

You should now see your own theme, and the Explorer in the Side Bar.

!!! tip
    The Command Palette is the one shortcut worth memorising today. Every
    other action can be found through it by typing part of its name.

## 4. Create folders and a file { #folders }

**0:30 · 10 min**

A project has the same few folders every time. Files that were downloaded
are kept apart from everything that is made from them.

| Folder | What goes in |
|--|--|
| `data/raw` | Files exactly as downloaded. Never edited |
| `data/processed` | Cleaned versions, made later by scripts |
| `scripts` | Code |
| `results` | Figures and numbers that the code produces |

1. Move the mouse over the Side Bar. Four small icons appear next to the
   project name. Select **New Folder**, type `data` and press Enter.

2. Select `data`, then **New Folder**, and type `raw`.

    The Side Bar shows `data / raw` on one row. VS Code joins a folder with
    its only subfolder. The row splits in the next step.

3. Select the empty area below the folders, then **New Folder**, and type
   `data/processed`. A name with `/` creates the folder in the right place.

4. The room does this step alone: create `scripts` and `results` the same
   way.

5. Select the empty area again, then **New File**, and type `README.md`. The
   file opens in the Editor.

6. Right-click `README.md` and select **Reveal in File Explorer** (macOS
   **Reveal in Finder**). It is an ordinary file in an ordinary folder. VS
   Code only shows it.

You should now see this in the Side Bar. VS Code lists folders first, so
`README.md` is the last row.

```text
analysis-project/
|- data/
|  |- processed/
|  |- raw/
|- results/
|- scripts/
|- README.md
```

!!! warning "Watch for"
    A new folder that lands inside the folder that was selected. This is the
    most common slip of the session. Drag the folder onto the empty area of
    the Side Bar to move it out. To rename, select it and press `F2` (macOS
    `Enter`).

## Part 2 · Markdown { #part-2 }

**0:40 to 0:55 · section 5**

The room ends this part with a README that has a title, two sections, a
list, a table and a link, and with the preview open beside the text.

## 5. Write Markdown { #markdown }

**0:40 · 15 min**

Markdown is plain text with a few signs for structure: `#` starts a heading,
`-` starts a list item, `**` makes text bold. Any editor can open it, and it
can be read without any formatting at all. The file name ends in `.md`.

`README.md` is the first file anyone opens in a project. It says what the
project is and what is in it.

1. Type into `README.md`:

    ```text
    # Analysis Project

    Seminar exercises for the course
    *Best Research and Data Analysis Practices from CERN*.
    ```

2. Look at the tab of the file. A dot means *not saved*. Save with `Ctrl+S`
   (macOS `Cmd+S`). Then select **File** > **Auto Save**, so that saving
   cannot be forgotten.

3. Press `Ctrl+K`, release, then press `V` (macOS `Cmd+K`, then `V`). The
   preview opens beside the text: what you type is on the left, the
   formatted page on the right.

4. Add a section with a list. Each student fills in their own answers. The
   last line is the answer from the lecture's thought exercise.

    ```text
    ## About

    - **Author:** your name
    - **Started:** 2026-09-29
    - **Data I would like to look at:** one sentence
    ```

5. Add a section with a table.

    ```text
    ## Folders

    | Folder | What goes in |
    |--|--|
    | `data/raw` | files exactly as downloaded, never edited |
    | `data/processed` | cleaned versions, made later by scripts |
    | `scripts` | code |
    | `results` | figures and numbers that the code produces |
    ```

6. Add a link under the first paragraph.

    ```text
    The example data is from the [CERN Open Data Portal](https://opendata.cern.ch).
    ```

You should now see a formatted page on the right: one title, two sections, a
list with three items, a table with four rows, and a link that opens the
portal.

Leave this table on the projector while the room types:

| You type | You get |
|--|--|
| `# Title` | The title of the page |
| `## Section` | A section heading |
| `*text*` | Italic |
| `**text**` | Bold |
| `- item` | A list item |
| `` `text` `` | A file name or code |
| `[text](address)` | A link |
| `![description](file)` | A picture |
| `| a | b |` | A row of a table |

Leave an empty line before a list and before a table, as in the blocks above.
The preview in VS Code forgives a missing one. Other programs that read
Markdown do not.

!!! warning "Watch for"
    | On the screen | Reason |
    |--|--|
    | `#Title` stays plain text | The space after `#` is missing |
    | `**Author: **` shows the asterisks | A space stands before the closing `**` |
    | Two lines show as one | A single line break does not show. An empty line starts a new paragraph |
    | The table shows as text with `|` signs | The second line, `|--|--|`, is missing |

## Part 3 · Edit many lines at once { #part-3 }

**0:55 to 1:25 · sections 6 to 9**

A table arrives in the wrong format. The room keeps the file as received,
cleans a copy and turns the copy into a table in a short report. Each change
is made once and lands on every line. The lecture slide
*Keys — Windows & macOS* lists every key of this part. Leave it on the
projector while the room works.

## 6. Work with whole lines { #lines }

**0:55 · 5 min**

A line is moved, copied or deleted with one key. Nothing has to be selected
first: the keys act on the line the cursor is in. The room tries them on the
table in the README.

1. In `README.md`, click anywhere in the last row of the **Folders** table,
   the row of `results`.

2. Press `Shift+Alt+↓` (macOS `Shift+Option+↓`, Linux `Ctrl+Shift+Alt+↓`).
   The row is copied below.

3. Change the copy so that it reads:

    ```text
    | `README.md` | what the project is and where the data came from |
    ```

4. Press `Alt+↑` (macOS `Option+↑`) four times. The row moves up, one line
   per press, to the first place under `|--|--|`.

5. Press `Ctrl+Z` (macOS `Cmd+Z`). The last move is taken back. Press
   `Ctrl+Y` (macOS `Cmd+Shift+Z`). It is made again. Every step in the
   editor can be taken back this way.

6. Click in the row of `scripts`. Press `Ctrl+C`, then `Ctrl+V` (macOS
   `Cmd+C`, `Cmd+V`). With nothing selected, the whole line is copied. There
   are now two rows for `scripts`.

7. Press `Ctrl+Shift+K` (macOS `Cmd+Shift+K`). The line with the cursor is
   deleted.

You should now see, in the preview, a table of five rows that begins with
`README.md`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The preview shows text with `|` signs instead of the table | The row was moved above `|--|--|`. Press `Alt+↓` once |
    | Windows: the keyboard changes between Lithuanian and English | Left `Alt` and `Shift` pressed alone switch the language. Press them once more |

## 7. Find and replace { #replace }

**1:00 · 8 min**

A lab partner sends a small table: the time of 10 swings of a pendulum for
nine lengths. It was saved from a spreadsheet on a computer set to
Lithuanian, so it has `;` between the values and `,` as the decimal sign. The
file is kept as received and a copy is cleaned. The first tool is Find and
Replace: it changes the same text everywhere in the file.

1. Select the `raw` folder in the Side Bar, then **New File**, and type
   `pendulum.csv`. Copy the block below with the button in its corner, paste
   it into the file and save.

    ```text
    nr;length_cm;t10_s
    1;20;9,02
    2;30;11,05
    3;40;12,61
    4;50;14,23
    5;60;15,49
    6;70;16,84
    7;80;17,90
    8;90;19,10
    9;100;20,01
    ;mean;15,14
    ```

2. Right-click `pendulum.csv` in the Side Bar and select **Copy**.
   Right-click the `processed` folder and select **Paste**. Close the tab of
   the file in `raw` and open the copy in `processed`. From here on only the
   copy is changed.

3. The last line holds the mean of the column. It is not a measurement.
   Click in it and press `Ctrl+Shift+K` (macOS `Cmd+Shift+K`).

4. Press `Ctrl+H` (macOS `Cmd+Option+F`). Two boxes open at the top of the
   Editor: **Find** and **Replace**.

5. Type `,` into **Find**. Every comma lights up, and the counter beside the
   box ends in `of 9`: nine rows, nine decimal commas.

6. Type `.` into **Replace** and select **Replace All**, the second of the
   two small buttons beside that box.

7. Do the same for the semicolons: `;` in **Find**, `,` in **Replace**. The
   counter ends in `of 20`. Select **Replace All** and close the boxes with
   `Esc`.

You should now see ten lines. The first three are:

```text
nr,length_cm,t10_s
1,20,9.02
2,30,11.05
```

Ask the room what happens when the semicolons are replaced first. Let one
student try it on the projector and take it back with `Ctrl+Z`. The line
`1;20;9,02` becomes `1,20,9,02`: three commas, and nothing tells the decimal
one from the others. The sign that can be told apart is replaced first.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The counter says 10 and 22 | The line with the mean is still in the file. Delete it and count again |
    | The file in `raw` has changed | The work was done in the wrong tab. Press `Ctrl+Z` in that tab until line 1 reads `nr;length_cm;t10_s` again |
    | Pasting does not work | Download [`pendulum_raw.csv`](../data/pendulum_raw.csv){ download="pendulum.csv" } and drag it onto the `raw` folder |

## 8. Put a cursor on every line { #cursors }

**1:08 · 7 min**

Find and Replace cannot delete a column, and the row numbers in the first
column are not needed. The editor can place a cursor on every line. Whatever
is typed or deleted then happens on all lines at once.

1. Press `Ctrl+A` (macOS `Cmd+A`). Everything is selected.

2. Press `Shift+Alt+I` (macOS `Shift+Option+I`). There is now a cursor at
   the end of every line, and the Status Bar reads `10 selections`.

3. Press `Home` (macOS `Cmd+←`). Every cursor jumps to the start of its
   line.

4. Press `Ctrl+Shift+→` (macOS `Option+Shift+→`). On every line the first
   word is selected: `nr` in line 1, a number in the other lines.

5. Press `Shift+→`. The comma is selected as well.

6. Press `Delete`, then `Esc` to go back to one cursor.

You should now see:

```text
length_cm,t10_s
20,9.02
30,11.05
40,12.61
50,14.23
60,15.49
70,16.84
80,17.90
90,19.10
100,20.01
```

Say why step 4 uses the word key. `nr` has two characters and `1` has one, so
cursors that move by characters end up in different places. `Home`, `End`
and the word keys land in the right place on every line, whatever its
length.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The laptop has no `Home` and `End` keys | `Fn+←` and `Fn+→` |
    | A cursor is missing or in the wrong place | Press `Esc`, then `Ctrl+Z` until the file is whole, and start again at step 1 |

## 9. Make a table for a report { #report }

**1:15 · 10 min**

A report shows the numbers as a table. A Markdown table is the same text
with `|` signs in it, so three edits turn the cleaned file into a table. The
report is a result, and it goes into `results`.

1. In the cleaned file press `Ctrl+A`, then `Ctrl+C` (macOS `Cmd+A`,
   `Cmd+C`).

2. Select the `results` folder, then **New File**, and type `report.md`.
   Paste with `Ctrl+V` and open the preview with `Ctrl+K`, then `V`. The
   preview shows one paragraph: single line breaks do not show.

3. Click just before any comma, hold `Shift` and press `→`. One comma is
   selected.

4. Press `Ctrl+Shift+L` (macOS `Cmd+Shift+L`). All ten commas are selected.
   Type a space, `|` and a space.

5. Press `Ctrl+A`, then `Shift+Alt+I` (macOS `Cmd+A`, `Shift+Option+I`).
   Type a space and `|`.

6. Press `Home` (macOS `Cmd+←`). Type `|` and a space. Press `Esc`.

7. Click in line 1 and press `Ctrl+Enter` (macOS `Cmd+Enter`). An empty
   line 2 opens. Type `|--|--|`. The preview now shows a table.

8. Press `Ctrl+Home` (macOS `Cmd+↑`) to go to the top of the file. Press
   `Enter` twice and `↑` twice, then type a title and one sentence. Keep an
   empty line between the sentence and the table.

    ```text
    # Pendulum

    Time of 10 swings for nine lengths.
    ```

9. Download [`pendulum_plot.png`](../data/pendulum_plot.png){ download="pendulum_plot.png" }
   and drag it from **Downloads** onto the `results` folder. Add an empty
   line at the end of `report.md`, and under it:

    ```text
    ![Time of 10 swings against length](pendulum_plot.png)
    ```

You should now see, in the preview, a title, one sentence, a table with a
header and nine rows, and the plot. The text on the left begins:

```text
# Pendulum

Time of 10 swings for nine lengths.

| length_cm | t10_s |
|--|--|
| 20 | 9.02 |
```

Say that the same three edits make a table of ten lines or of ten thousand.
The change is described once and the editor repeats it.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The table shows as text | Line 2 of the table is not `|--|--|`, or an empty line stands between the header and it |
    | A lone `|  |` at the end of the file | The file ended with two empty lines and one of them got a cursor. Delete that line |
    | The picture is broken | The file is not in `results`, or it is named `pendulum_plot (1).png` |

## Part 4 · A real data file { #part-4 }

**1:25 to 1:55 · sections 10 and 11**

Section 10 uses VS Code to read a file that is too long to read by eye.
Section 11 uses Markdown to write down where the files came from and what
was done to them.

## 10. Look at a data file { #data-file }

**1:25 · 20 min**

Everyone uses the same file, `D0_KPi.csv`, so that every screen in the room
shows the same thing. It is the file from the lecture's section
*A Dataset Up Close*. Students choose their own dataset at home.

1. Download [`D0_KPi.csv`](../data/D0_KPi.csv) with the browser. The file
   lands in **Downloads**.

2. Drag the file from **Downloads** onto the `raw` folder in the Side Bar.
   Do not rename it.

3. Select the file in the Side Bar to open it. Read line 1 and one line of
   numbers.

    | Question | Answer |
    |--|--|
    | What is written in line 1? | `M,PT,TAU,IPCHI2`: the four column names |
    | Which character separates the values? | The comma |
    | Which character is the decimal separator? | The point |

4. Press `Ctrl+End` (macOS `Cmd+↓`) to jump to the end, and read the line
   number on the left.

    VS Code numbers 91 585 lines. The last one is empty, because the file
    ends with a line break. That leaves 91 584 lines: one header line and
    **91 583 rows of data**.

5. Press `Ctrl+G` (the same key on macOS), type `5000` and press Enter. Line
   5000 begins with `1868.8636`.

6. Press `Ctrl+F` (macOS `Cmd+F`) and type `-100`. VS Code finds 49 places,
   all in the third column, `TAU`. In these rows the decay time could not be
   computed, and the file marks that with `-100`. This is how this file
   writes a missing value.

7. Open the same file in a spreadsheet program (Excel, LibreOffice, Numbers)
   **without saving anything**. Right-click the file in the Side Bar, select
   **Reveal in File Explorer** (macOS **Reveal in Finder**), and open it from
   there. A student without a spreadsheet program looks at a neighbour's
   screen.

    Ask who sees which of these:

    | On the screen | Reason |
    |--|--|
    | The whole line in column A, as one text | The spreadsheet expects `;` between values |
    | Four columns, but numbers turned into text or into wrong values | The spreadsheet expects `,` as the decimal separator |
    | Four correct columns | The computer is set to English regional settings |

8. Open `data/raw/pendulum.csv` in the spreadsheet the same way. This is the
   file with `;` and decimal commas. Ask who sees correct columns now: those
   computers are set to Lithuanian or another European format. Which of the
   two files opens correctly depends on the computer.

9. Close the spreadsheet. If it asks whether to save, the answer is **No**.

You should now have `D0_KPi.csv` in `data/raw/`, and every student can say
the number of data rows and the four column names.

This comparison is the centre of the session. Say it in these words: the
file is the same on every laptop, and VS Code shows the same text on every
laptop. The spreadsheet shows an interpretation, and the interpretation
depends on the settings of the computer. Saving from the spreadsheet writes
that interpretation back into the file. That is why a file in `data/raw/` is
never edited and never saved from a spreadsheet.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The file is named `D0_KPi (1).csv` | It was downloaded twice. Delete both and download once |
    | Safari shows the numbers in a tab instead of saving | **File** > **Save As...** |
    | The file is not under `raw` | It was dropped onto another folder. Drag it again |
    | Someone saved from the spreadsheet | They download the file again |

## 11. Record where the data came from { #provenance }

**1:45 · 10 min**

A data file without a note on its origin cannot be checked by anyone,
including its owner six months later. The note goes into the README. It is
written in the Markdown from section 5, and it also lists what was changed
by hand.

1. Open [record 401](https://opendata.cern.ch/record/401) of the CERN Open
   Data Portal in the browser. Find the DOI and the licence on the page
   together with the room.

2. Add a **Data** section to `README.md`. The room types the labels and
   looks up the values. Filled in, the section reads:

    ```text
    ## Data

    - **Source:** CERN Open Data Portal, record 401
    - **Address:** https://opendata.cern.ch/record/401
    - **DOI:** 10.7483/OPENDATA.LHCb.E7EJ.JUWR
    - **Licence:** CC0
    - **Fetched:** 2026-09-29
    - **File:** `data/raw/D0_KPi.csv`, converted from the record's
      `MasterclassData.root` by the course's `root_to_csv.py`
    - **Size:** 3 926 142 bytes, 91 583 rows, 4 columns
    - **One row:** one candidate pair of a kaon and a pion from one collision
    ```

    The line **One row** is the one that needs thought. Give the room a
    minute before you show the answer.

3. Look up the size of the file in the file manager. Windows shows about
   3 835 KB and macOS about 3.9 MB. Both are 3 926 142 bytes: Windows counts
   in units of 1024, macOS in units of 1000.

4. Add the second file under it. A change made by hand is part of where a
   file came from, so the edits of sections 7 and 8 are listed.

    ```text
    - **File:** `data/raw/pendulum.csv`, from a lab partner, 2026-09-29
    - **Cleaned copy:** `data/processed/pendulum.csv`. Mean line deleted,
      `,` replaced by `.`, `;` replaced by `,`, column `nr` deleted
    ```

5. Swap laptops with a neighbour. Using only the neighbour's README, could
   you find and download the same file? Tell them what was missing. This
   takes three minutes.

You should now see a **Data** section in the preview that a stranger could
follow.

The record holds `MasterclassData.root`, and the CSV is a converted copy. The
README names both, because the file in `data/raw/` is not the file a
stranger would download from the portal.

## 12. Wrap up { #wrap-up }

**1:55 · 5 min**

Put the three tasks of the next section on the projector and read them
aloud. Then:

- Say that an installation which fails at home is not a problem. Students
  bring the error message, a photo of the screen is enough, and it gets
  fixed at the start of the next session.
- Ask on the way out which step was hardest.

What the room has learned:

- VS Code works on a folder. The folder is the project.
- Markdown is plain text with a few signs for structure.
- The README says what is in the project and where each data file came from.
- Find and Replace changes the same text everywhere. The counter is read
  before anything is replaced.
- A cursor on every line makes one edit on all lines. `Home`, `End` and the
  word keys keep the cursors in step.
- A change made by hand is written down in the README.
- A CSV file is plain text. VS Code shows the same text on every laptop.
- A spreadsheet shows an interpretation of the file, and the interpretation
  depends on the computer.
- A file in `data/raw/` is never edited.

## Next steps, at home

**30 min, before the next session**

1. **Choose a dataset of your own.** A table from a field you care about:
   weather, sport, prices, health, astronomy, your lab. Good places to look
   are the portals from the lecture (Eurostat, Copernicus, NASA, Zenodo,
   Kaggle) and the [Lithuanian open data portal](https://data.gov.lt). It
   should be a CSV file with at least a few hundred rows and at least one
   column of numbers.

2. Put it in `data/raw/` and add an entry to the **Data** section of the
   README, with the same lines as in section 11.

3. Answer the five questions from the lecture for your file, in the README:
   how many rows and columns, what one row is, which columns are measured,
   derived or bookkeeping, the units, how missing values are marked.

4. Install Python and Git by following
   [Install Python and Git](install_python_git.md). Neither was needed
   today.

## Stretch goals

For students who already program and finish a section early. These need the
terminal and Python. Answers are given for the lecturer.

- Open the terminal with **Terminal** > **New Terminal** and compute the
  checksum of the file, a fingerprint that proves two copies are
  byte-identical. The answer is SHA-256 `25c3c972…c1505136` on every system.

    ```text
    Windows (PowerShell)   Get-FileHash data\raw\D0_KPi.csv -Algorithm SHA256
    macOS                  shasum -a 256 data/raw/D0_KPi.csv
    Linux, Git Bash        sha256sum data/raw/D0_KPi.csv
    ```

- Write `scripts/count_rows.py` that prints the number of data rows and the
  smallest and largest value of column `M`, without Pandas. The answer is
  91 583 rows, with `M` from 1766.2096 to 2453.6584.
- Download the record's original file `MasterclassData.root` and open it in
  VS Code. The file is binary, so VS Code declines to show it as text.
- Install the **Rainbow CSV** extension from the Extensions view of the
  Activity Bar and open `D0_KPi.csv` again. Each column gets its own colour.

Four more need only the editor.

- Add a column to `data/processed/pendulum.csv` with the uncertainty of the
  time, `0.10` on every row. Select lines 2 to 10, press `Shift+Alt+I` and
  type `,0.10`. The header gets `,dt10_s` by hand.
- In the Find box, switch on the button `.*` and search for `(\d),(\d)`
  in a fresh copy of the raw file. It matches only a comma that stands
  between two digits: 10 matches, the mean line included. Replace with
  `$1.$2`. The semicolons stay as they are.
- Hold `Shift+Alt` (macOS `Shift+Option`) and drag the mouse straight down
  through the rows of the table in `report.md`. This places one cursor per
  row in the same column.
- Install the **Marp for VS Code** extension. Put the three lines `---`,
  `marp: true`, `---` at the top of a copy of `report.md` and a line `---`
  between its parts. The preview shows slides, and the Marp button at the
  top of the Editor exports them as a PDF file.

## If students ask for more

Four parts of VS Code are kept for later lectures. If asked today, show it
for ten seconds and name the lecture.

| Part of VS Code | Lecture |
|--|--|
| The Status Bar: encoding, line endings | 3 (How Computers Work) |
| The terminal in the Panel | 4 (Command Line) |
| Source Control: saving and comparing versions | 5 (Git) |
| Extensions: Python, running a script | 6 (Python Foundations) |

Leave out altogether, even if asked: the debugger, settings sync, remote
development, AI assistants, Jupyter.

## Aims practised

♻️ provenance = reproducibility · 📁 raw data captured, untouched · ⚙️ one edit applied to every line · 🔧 the same steps on every system
