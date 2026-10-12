# Seminar 1 — VS Code and Markdown

**Paired lecture:** 02 Introduction to Data · **Format:** follow-along, from zero · **~120 min**
in class

**Today's goal:** every student has a project folder open in VS Code, with a
README in Markdown that says what is in the folder and where its data came
from, a small table repaired in the editor, and a short report.

The tools are VS Code and a web browser: no terminal, no Python. The files
are a reading list and the loans log of a library.

## Run sheet

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · VS Code** · 25 min | | |
| 0:00 | [1. Install VS Code](#install) | `code.visualstudio.com`, **Download** | VS Code running |
| 0:10 | [2. Open a project folder](#open-folder) | **File**, **Open Folder…** | `reading-project` open |
| 0:15 | [3. The window and three keys](#interface) | The five regions, `Ctrl+Shift+P` | The regions named |
| 0:20 | [4. Folders and a README](#folders) | **New Folder**, **New File** | The project skeleton |
| | **Part 2 · Markdown** · 15 min | | |
| 0:25 | [5. Write the README](#markdown) | `README.md` beside its preview | A README with a title, a list, a table, a link |
| 0:35 | [6. Five mistakes, on purpose](#mistakes) | `#Title` without the space | Each mistake seen and fixed |
| | **Part 3 · Repair a table** · 30 min | | |
| 0:40 | [7. The reading list arrives](#copy) | The file in `data/raw`, a copy in `data/processed` | Two copies of the list |
| 0:45 | [8. Whole lines](#lines) | `Ctrl+Shift+K` on the mean line | The mean line gone |
| 0:50 | [9. Find and replace](#replace) | `Ctrl+H`: `,` to `.`, then `;` to `,` | Commas between the values |
| 0:57 | [10. A cursor on every line](#cursors) | `Shift+Alt+I`, `Home`, `Ctrl+Shift+→` | Column `nr` gone |
| 1:03 | [11. A table for a report](#report) | `Ctrl+Shift+L` on the commas | `results/report.md` with a table and a picture |
| | **Part 4 · A long file and its note** · 30 min | | |
| 1:11 | [12. Read a long file](#data-file) | `Ctrl+End`, `Ctrl+G`, `Ctrl+F` | Rows counted, units and the mark `NA` found |
| 1:23 | [13. Open it in a spreadsheet](#spreadsheet) | Both files in a spreadsheet, nothing saved | Who sees which outcome |
| 1:28 | [14. Write where the data came from](#provenance) | The **Data** section of the README | A README a stranger can follow |
| 1:38 | [15. Wrap up](#wrap-up) | The list of what was learned | |
| | **Optional, if the room is fast** | | |
| — | [16. Rename a column everywhere](#rename) | `Ctrl+Shift+L` on `rating` | `stars` in README and report |
| — | [17. Sorting sorts text](#sort) | **Sort Lines Ascending** | `120` before `96` |
| — | [18. Check the edits by size](#sizes) | The file sizes, then the arithmetic | 546 − 18 − 30 = 498 |
| — | [19. The five questions, your dataset](#own-data) | A dataset of the student's field | Five answers in the README |

**If time runs short:** leave out section 13 and the swap test of section 14.
A student who falls behind downloads the file of that step from **Files for
this seminar** and goes on.

??? info "How to use this page"
    This page is written for the person at the front. Students follow the
    same page.

    - **Tell the room** is what to say before the steps.
    - The **numbered steps** are done on the projector, and the room repeats
      each one.
    - **You should now see** closes a section. Ask for hands, and go on when
      about four in five have it.
    - **Watch for** is the usual slip in that section.

    Keys are written for Windows, with macOS in brackets: `Ctrl+S` (macOS
    `Cmd+S`). Linux has the Windows keys.

??? info "Before the session, about 5 minutes"
    - Open this page on a second screen or a phone.
    - Download the two data files once, so you know they arrive:
      [`reading_list.csv`](../data/books_reading_list.csv){ download="reading_list.csv" }
      and [`loans.csv`](../data/books_loans.csv){ download="loans.csv" }.
    - Your VS Code should look like a fresh one: no `reading-project` folder
      yet. You build it with the room.
    - Ask who has written code before. Seat each of them next to someone who
      has not, with one rule: explain, never take the keyboard.

<a id="files"></a>

??? info "Files for this seminar"
    A browser saves each file under the name in the second column.

    | File | Saved as | Goes to | Used in |
    |--|--|--|--|
    | [`books_reading_list.csv`](../data/books_reading_list.csv){ download="reading_list.csv" } | `reading_list.csv` | `data/raw` | Section 7: the list as received |
    | [`books_reading_list_clean.csv`](../data/books_reading_list_clean.csv){ download="reading_list.csv" } | `reading_list.csv` | `data/processed` | The end of section 10 |
    | [`books_pages.png`](../data/books_pages.png){ download="reading_pages.png" } | `reading_pages.png` | `results` | Section 11 |
    | [`books_report.txt`](../data/books_report.txt){ download="report.md" } | `report.md` | `results` | The end of section 11 |
    | [`books_loans.csv`](../data/books_loans.csv){ download="loans.csv" } | `loans.csv` | `data/raw` | Section 12 |
    | [`books_README.txt`](../data/books_README.txt){ download="README.md" } | `README.md` | the project folder | The end of section 14 |
    | [`books_project.zip`](../data/books_project.zip) | `books_project.zip` | | The whole `reading-project` at the end |

---

## Part 1 · VS Code { #part-1 }

**0:00 to 0:25 · sections 1 to 4**

The room ends this part with VS Code installed and an empty project folder
open in it.

---

### 1. Install VS Code { #install }

**0:00 · 10 min**

**Tell the room.** VS Code is a free editor for text. It looks the same on
Windows, macOS and Linux, so every screen in the room shows the same thing.

1. Open this address in a browser and select **Download** for your system:

    ```text
    code.visualstudio.com
    ```

2. Install it.

    === "macOS"

        Open the downloaded file and drag **Visual Studio Code** into the
        **Applications** folder.

    === "Windows"

        Run the downloaded installer and keep every default.

3. Start VS Code. If a **Chat** panel is open on the right, close it with
   the **X** in its corner.

!!! success "You should now see"
    A window with a **Welcome** tab.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows asks for an administrator password | Take the **User Installer** from the download page. It needs none |
    | macOS: "cannot be opened because it is from an unidentified developer" | Drag the app to **Applications** first, then open it from there |
    | A university laptop blocks the installation | Open [vscode.dev](https://vscode.dev) in Chrome or Edge and pair with a neighbour |

---

### 2. Open a project folder { #open-folder }

**0:10 · 5 min**

**Tell the room.** VS Code works on a folder. The folder is the project:
everything that belongs to one piece of work lives in it.

1. In the file manager (File Explorer on Windows, Finder on macOS), make a
   folder in **Documents** named:

    ```text
    reading-project
    ```

2. In VS Code select **File**, **Open Folder…** and pick `reading-project`.

3. If VS Code asks whether you trust the authors, select
   **Yes, I trust the authors**.

!!! success "You should now see"
    `READING-PROJECT` at the top of the left-hand column, with nothing under
    it.

---

### 3. The window and three keys { #interface }

**0:15 · 5 min**

**Tell the room.** The window has five regions. Point at each one and name
it.

| | Region | What it is for |
|--|--|--|
| 1 | Activity Bar | The column of icons on the far left |
| 2 | Side Bar | The files of the project: the **Explorer** |
| 3 | Editor | The open files, one tab each |
| 4 | Panel | Hidden today. It holds the terminal, later in the course |
| 5 | Status Bar | The line at the bottom: facts about the open file |

1. Press `Ctrl+B` (macOS `Cmd+B`) twice. The Side Bar hides and comes back.

2. Press `Ctrl+Shift+P` (macOS `Cmd+Shift+P`). This is the
   **Command Palette**. Type:

    ```text
    theme
    ```

    Select **Preferences: Color Theme** and pick a theme with the arrow
    keys and Enter.

3. Press `Ctrl+=` (macOS `Cmd+=`) and `Ctrl+-` (macOS `Cmd+-`) until the
   text has a size you like.

!!! success "You should now see"
    Your theme, and the Explorer in the Side Bar.

---

### 4. Folders and a README { #folders }

**0:20 · 5 min**

**Tell the room.** Every project has the same folders. Files as they arrived
are kept apart from everything made from them.

| Folder | What goes in |
|--|--|
| `data/raw` | Files exactly as received. Never edited |
| `data/processed` | Cleaned copies |
| `scripts` | Programs, later in the course |
| `results` | The report, figures, numbers |

1. Move the mouse over the Side Bar. Four small icons appear next to the
   project name. Select **New Folder** and type:

    ```text
    data/raw
    ```

    A name with `/` makes both folders at once.

2. Select the empty area below the folders, then **New Folder**, and type:

    ```text
    data/processed
    ```

3. The room does this alone: make `scripts` and `results` the same way.

4. Select the empty area, then **New File**, and type:

    ```text
    README.md
    ```

!!! success "You should now see"
    ```text
    reading-project/
    |- data/
    |  |- processed/
    |  |- raw/
    |- results/
    |- scripts/
    |- README.md
    ```

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | A new folder lands inside the folder that was selected | The usual slip. Drag it onto the empty area of the Side Bar |
    | A folder is called `Data` | Select it and press `F2` (macOS `Enter`) to rename it to `data` |

---

## Part 2 · Markdown { #part-2 }

**0:25 to 0:40 · sections 5 and 6**

The room ends this part with a README that has a title, a list, a table and
a link, with the preview open beside it.

---

### 5. Write the README { #markdown }

**0:25 · 10 min**

**Tell the room.** Markdown is plain text with a few signs for structure.
The file name ends in `.md`, and `README.md` is the first file anyone opens
in a project. Leave this table on the projector:

| You type | You get |
|--|--|
| `# Title` | The title of the page |
| `## Section` | A section heading |
| `**text**` | Bold |
| `- item` | A list item |
| `` `text` `` | A file name or code |
| `[text](address)` | A link |
| `| a | b |` | A row of a table |

1. Type into `README.md`:

    ```text
    # Reading Project

    A reading list and the loans log of a library, used to practise
    VS Code and Markdown.
    ```

2. Look at the tab: a dot means *not saved*. Press `Ctrl+S` (macOS
   `Cmd+S`). Then select **File**, **Auto Save**.

3. Press `Ctrl+K`, release, then `V` (macOS `Cmd+K`, then `V`). The preview
   opens beside the text.

4. Add a section with a list. Each student types their own name and
   today's date, written year, month, day.

    ```text
    ## About

    - **Author:** your name
    - **Started:** 2026-09-29
    ```

5. Add a section with a table.

    ```text
    ## Folders

    | Folder | What goes in |
    |--|--|
    | `data/raw` | files exactly as received, never edited |
    | `data/processed` | cleaned copies |
    | `scripts` | programs, later in the course |
    | `results` | the report and its picture |
    ```

6. Add a link at the end of the first paragraph:

    ```text
    The editor is [VS Code](https://code.visualstudio.com).
    ```

!!! success "You should now see"
    In the preview: one title, two sections, a list of two items, a table of
    four rows, and a link.

---

### 6. Five mistakes, on purpose { #mistakes }

**0:35 · 5 min**

**Tell the room.** The preview is the test. Each mistake below is made on
purpose, read in the preview, and taken back with `Ctrl+Z` (macOS `Cmd+Z`).

| Type this | The preview shows | Reason |
|--|--|--|
| `#Reading Project` | `#Reading Project` as text | No space after `#` |
| `**Author: **` | The asterisks | A space before the closing `**` |
| Two lines with one line break between | One line | Only an empty line starts a paragraph |
| The table without `|--|--|` | Text with `|` signs | The second line makes the table |
| No empty line before the table | Often still a table here, not in other programs | Leave an empty line before a list or a table |

!!! success "You should now see"
    The README as it was at the end of section 5.

---

## Part 3 · Repair a table { #part-3 }

**0:40 to 1:11 · sections 7 to 11**

A table arrives in a spreadsheet's format. The room keeps it as received,
repairs a copy, and turns the copy into a table in a short report. Every fix
is made once and lands on every line.

---

### 7. The reading list arrives { #copy }

**0:40 · 5 min**

**Tell the room.** A friend kept a list of the books they read, in a
spreadsheet set to Lithuanian. The export has `;` between the values and a
decimal comma. The file goes to `data/raw` and stays as it is; the work is
done on a copy.

1. Download
   [`reading_list.csv`](../data/books_reading_list.csv){ download="reading_list.csv" }
   and drag it from **Downloads** onto the `raw` folder in the Side Bar.

2. Select it to open it:

    ```text
    nr;title;author;pages;rating
    1;The Little Prince;Antoine de Saint-Exupéry;96;3,5
    2;Pride and Prejudice;Jane Austen;432;4,5
    …
    12;Solaris;Stanisław Lem;204;4,0
    ;mean;;297,4;4,17
    ```

3. Right-click `reading_list.csv` in the Side Bar and select **Copy**.
   Right-click the `processed` folder and select **Paste**.

4. Close the tab of the file in `raw` and open the copy in `processed`. From
   here on only the copy is changed.

!!! success "You should now see"
    `reading_list.csv` twice in the Side Bar, under `raw` and under
    `processed`, and the copy open.

Ask the room which four fixes the list needs before a program can read it:
the mean line out, the decimal comma to a point, `;` to `,`, the column `nr`
out.

---

### 8. Whole lines { #lines }

**0:45 · 5 min**

**Tell the room.** A line is deleted, moved or copied with one key. Nothing
has to be selected: the keys act on the line the cursor is in.

1. Click in the last line, `;mean;;297,4;4,17`. It is not a book. Press
   `Ctrl+Shift+K` (macOS `Cmd+Shift+K`). The line is gone.

2. Click in the line of `Dracula`. Press `Alt+↑` (macOS `Option+↑`) twice:
   the line moves up. Press `Ctrl+Z` (macOS `Cmd+Z`) twice: it is back.

3. Press `Shift+Alt+↓` (macOS `Shift+Option+↓`): the line is copied below.
   Press `Ctrl+Shift+K` to delete the copy.

!!! success "You should now see"
    Thirteen lines: the header and twelve books, the last one `Solaris`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: the keyboard switches between Lithuanian and English | Left `Alt` and `Shift` pressed alone switch the language. Press them once more |
    | The file in `raw` changed | Press `Ctrl+Z` in that tab until its last line is `;mean;;297,4;4,17` again |

---

### 9. Find and replace { #replace }

**0:50 · 7 min**

**Tell the room.** Find and Replace changes the same text everywhere in the
file. The counter says how many places match: read it before replacing.

1. Press `Ctrl+H` (macOS `Cmd+Option+F`). Two boxes open: **Find** and
   **Replace**.

2. Type into **Find**:

    ```text
    ,
    ```

    The counter ends in `of 12`: twelve books, twelve decimal commas.

3. Type into **Replace**, then select **Replace All**, the second button
   beside the box:

    ```text
    .
    ```

4. Now the semicolons. Into **Find**:

    ```text
    ;
    ```

    Into **Replace**:

    ```text
    ,
    ```

    The counter ends in `of 52`: four on each of thirteen lines. Select
    **Replace All**, then `Esc`.

!!! success "You should now see"
    ```text
    nr,title,author,pages,rating
    1,The Little Prince,Antoine de Saint-Exupéry,96,3.5
    2,Pride and Prejudice,Jane Austen,432,4.5
    ```

Ask what happens if the semicolons go first. Try it on the projector, then
`Ctrl+Z`: the line `1;The Little Prince;…;96;3,5` becomes
`1,The Little Prince,…,96,3,5`, and nothing tells the decimal comma from
the separators any more.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The counter says 14 and 56 | The mean line is still there. Delete it, then count again |

---

### 10. A cursor on every line { #cursors }

**0:57 · 6 min**

**Tell the room.** Find and Replace cannot delete a column. A cursor on
every line can: whatever is typed or deleted happens on all lines at once.

1. Press `Ctrl+A` (macOS `Cmd+A`), then `Shift+Alt+I` (macOS
   `Shift+Option+I`). A cursor stands at the end of every line, and the
   Status Bar reads `13 selections`.

2. Press `Home` (macOS `Cmd+←`). Every cursor jumps to the start of its
   line.

3. Press `Ctrl+Shift+→` (macOS `Option+Shift+→`). On every line the first
   word is selected: `nr`, or a number from `1` to `12`.

4. Press `Shift+→`. The comma is selected too.

5. Press `Delete`, then `Esc`.

!!! success "You should now see"
    ```text
    title,author,pages,rating
    The Little Prince,Antoine de Saint-Exupéry,96,3.5
    Pride and Prejudice,Jane Austen,432,4.5
    ```

Say why step 3 uses the word key: `nr` has two characters, `1` has one and
`12` has two. Cursors that move by one character drift apart on lines of
different length. `Home`, `End` and the word keys do not.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The laptop has no `Home` key | `Fn+←` |
    | A cursor is in the wrong place | `Esc`, then `Ctrl+Z` until the file is whole, and start again at step 1 |

---

### 11. A table for a report { #report }

**1:03 · 8 min**

**Tell the room.** A Markdown table is the same text with `|` signs in it.
Three edits turn the repaired list into a table. The report is a result, so
it goes into `results`.

1. In the repaired copy press `Ctrl+A`, then `Ctrl+C` (macOS `Cmd+A`,
   `Cmd+C`).

2. Select the `results` folder, then **New File**, and type:

    ```text
    report.md
    ```

    Paste with `Ctrl+V` (macOS `Cmd+V`) and open the preview with `Ctrl+K`,
    then `V`.

3. Click just before any comma, hold `Shift` and press `→`. Press
   `Ctrl+Shift+L` (macOS `Cmd+Shift+L`): all commas are selected. Type a
   space, `|` and a space.

4. Press `Ctrl+A`, then `Shift+Alt+I`. Type a space and `|`. Press `Home`,
   type `|` and a space. Press `Esc`.

5. Click in line 1 and press `Ctrl+Enter` (macOS `Cmd+Enter`). Type into the
   new line 2:

    ```text
    |--|--|--|--|
    ```

6. Press `Ctrl+Home` (macOS `Cmd+↑`), then `Enter` twice and `↑` twice, and
   type:

    ```text
    # My Reading List

    Twelve books, with the pages of the edition read and my rating.
    ```

7. Download [`reading_pages.png`](../data/books_pages.png){ download="reading_pages.png" }
   and drag it onto the `results` folder. Add at the end of `report.md`,
   after an empty line:

    ```text
    ![Pages per book](reading_pages.png)
    ```

!!! success "You should now see"
    In the preview: a title, one sentence, a table with a header and twelve
    rows, and a bar chart of pages per book. The text begins:

    ```text
    # My Reading List

    Twelve books, with the pages of the edition read and my rating.

    | title | author | pages | rating |
    |--|--|--|--|
    | The Little Prince | Antoine de Saint-Exupéry | 96 | 3.5 |
    ```

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The table shows as text | Line 2 of the table is not `|--|--|--|--|`, or an empty line stands between it and the header |
    | A lone `|  |` at the end | The file ended with an empty line and it got a cursor. Delete that line |
    | The picture is broken | The file is not in `results`, or it is called `reading_pages (1).png` |

---

## Part 4 · A long file and its note { #part-4 }

**1:11 to 1:41 · sections 12 to 15**

A file too long to read by eye. The room counts it, reads its units from the
numbers, finds how it marks a missing value, and writes all of it into the
README.

---

### 12. Read a long file { #data-file }

**1:11 · 12 min**

**Tell the room.** A small town library sent its loans log: one line for
every book lent out from 2021 to 2025. It came with no note.

1. Download [`loans.csv`](../data/books_loans.csv){ download="loans.csv" }
   and drag it onto the `raw` folder. Open it.

    ```text
    loan_date,book_id,pages,days_kept,late_fee_eur
    2021-01-04,B0023,309,19,0.00
    2021-01-04,B0051,155,22,0.00
    ```

2. Press `Ctrl+End` (macOS `Cmd+↓`) and read the line number on the left.

    VS Code shows line 17 281, and it is empty: the file ends with a line
    end. 17 280 lines, one of them the header: **17 279 loans**.

3. Press `Ctrl+G` (the same on macOS) and type:

    ```text
    1000
    ```

    Line 1000 is `2021-04-20,B0214,622,7,0.00`: the same shape as line 2.

4. Press `Ctrl+F` (macOS `Cmd+F`) and type:

    ```text
    NA
    ```

    The counter shows **438**. Each such line has `NA` twice, in
    `days_kept` and in `late_fee_eur`: 438 / 2 = **219 loans** with no
    value. Press `Enter` a few times: most are in December 2025.

5. Work out the units with the room, from the numbers:

    | Column | The numbers | Unit |
    |--|--|--|
    | `pages` | 64 to 900 | pages of the book |
    | `days_kept` | 1 to 70 | days: a loan of 70 hours or 70 weeks makes no sense |
    | `late_fee_eur` | 0.00 to 4.20 | euros, as `_eur` says |

6. Find the rule of the fee. Press `Ctrl+F` and type `,30,`, then press
   `Enter` a few times: every loan of 30 days has the fee `0.20`. Then
   `,46,`: every one has `1.80`. Ask the room for the rule.

    ```text
    (30 − 28) × 0.10 = 0.20
    (46 − 28) × 0.10 = 1.80
    ```

    The fee is **0.10 euro for each day after 28**. It is a derived column:
    computed from `days_kept`, not measured.

!!! success "You should now see"
    Every student can say: 17 279 loans, the unit of each column, the
    missing-value mark `NA` in 219 loans, and the rule of the fee.

`NA` is the library's mark for "the book has not come back". 179 of the 219
are loans of December 2025, still out when the file was written. The other
40 are books that never came back.

---

### 13. Open it in a spreadsheet { #spreadsheet }

**1:23 · 5 min**

**Tell the room.** VS Code shows the characters of a file, the same on every
laptop. A spreadsheet shows an interpretation of them, and the
interpretation depends on the computer's settings.

1. Right-click `loans.csv` in the Side Bar, select **Reveal in File
   Explorer** (macOS **Reveal in Finder**), and open it in a spreadsheet
   program from there. Do not save anything.

2. Ask who sees which of these:

    | On the screen | Reason |
    |--|--|
    | Every line in column A, as one text | The spreadsheet expects `;` between values |
    | Columns, but `0.20` turned into a date or text | It expects a decimal comma |
    | The right columns | The computer's settings match the file |

3. Open `data/raw/reading_list.csv` the same way. It has `;` and a decimal
   comma. Ask who sees correct columns now: often the other half of the
   room.

4. Close the spreadsheet. If it asks whether to save, answer **No**.

!!! success "You should now see"
    Each student knows which of the two files their spreadsheet reads
    correctly.

**Say it in these words.** The file is the same on every laptop. Saving from
the spreadsheet writes its interpretation back into the file. That is why a
file in `data/raw` is never saved from a spreadsheet.

---

### 14. Write where the data came from { #provenance }

**1:28 · 10 min**

**Tell the room.** A data file without a note on its origin cannot be checked
by anyone, its owner included, six months later. The note goes into the
README, with every change made by hand.

1. Add to `README.md`:

    ```text
    ## Data

    - **Source:** the course workbook, Seminar 1 page
    - **Licence:** CC0
    - **Received:** today's date
    - **File:** `data/raw/reading_list.csv`, 12 books, exported from a
      spreadsheet: `;` between the values, a decimal comma
    - **Cleaned copy:** `data/processed/reading_list.csv`. Mean line
      deleted, `,` replaced by `.`, `;` replaced by `,`, column `nr` deleted
    - **File:** `data/raw/loans.csv`, 17 279 rows
      - **One row:** one loan of one book
      - **Units:** `pages`, `days_kept` in days, `late_fee_eur` in euros,
        0.10 for each day after 28
      - **Missing:** `NA` when the book has not come back, 219 rows
    ```

2. Swap laptops with a neighbour for three minutes. Using only their README:
   what is one row of `loans.csv`? What does `NA` mean? Tell them what was
   missing.

!!! success "You should now see"
    A **Data** section in the preview that a stranger could follow.

---

### 15. Wrap up { #wrap-up }

**1:38 · 3 min**

Read the list aloud. Ask on the way out which step was hardest.

- VS Code works on a folder, and the folder is the project.
- Markdown is plain text with a few signs; the preview is the test.
- A file in `data/raw` is never edited. Work is done on a copy.
- Find and Replace changes the same text everywhere. Read the counter first.
- A cursor on every line makes one edit on all lines. `Home`, `End` and the
  word keys keep the cursors in step.
- A long file is counted, and its units and its missing-value mark are read
  from the numbers.
- A spreadsheet shows an interpretation; VS Code shows the characters.
- The README says where each file came from and what was changed by hand.

---

## Optional, if the room is fast { #optional }

---

### 16. Rename a column everywhere { #rename }

**Tell the room.** The same word in many places is selected at once and
typed once.

1. In `report.md`, double-click the word `rating` in the header row.

2. Press `Ctrl+D` (macOS `Cmd+D`): the next `rating`, if any, is added.
   Press `Ctrl+Shift+L` (macOS `Cmd+Shift+L`) to add all of them.

3. Type:

    ```text
    stars
    ```

!!! success "You should now see"
    `stars` in the header and in the sentence under the title, if it named
    the rating.

---

### 17. Sorting sorts text { #sort }

**Tell the room.** The editor sorts characters, not numbers.

1. Make a new file `results/sort_test.txt` and type three lines:

    ```text
    96
    432
    120
    ```

2. Select the three lines, press `Ctrl+Shift+P` and type:

    ```text
    Sort Lines Ascending
    ```

!!! success "You should now see"
    ```text
    120
    432
    96
    ```

    `120` comes first because the character `1` comes before `4` and `9`.
    Dates written as `2021-01-04` sort right as text; numbers of different
    length do not.

---

### 18. Check the edits by size { #sizes }

**Tell the room.** Each edit removed a known number of bytes. The sizes of
the two files check the edits.

1. Right-click each `reading_list.csv` and select **Reveal in File
   Explorer** (macOS **Reveal in Finder**). Read the size: **Properties** on
   Windows, **Get Info** on macOS.

    The raw file is 546 bytes, the repaired copy 498 bytes.

2. Work it out with the room:

    ```text
    ;mean;;297,4;4,17 and its line end        18
    nr; then 1; to 9; then 10; 11; 12;        3 + 9 × 2 + 3 × 3 = 30
    the replacements, one character for one    0
    546 − 18 − 30 = 498
    ```

!!! success "You should now see"
    The arithmetic closes. A different size means one fix went wrong.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: the copy is larger than 498 | VS Code wrote `CRLF` line ends. The Status Bar shows `CRLF`; select it and choose `LF` |

---

### 19. The five questions, your dataset { #own-data }

For a student who has a dataset in mind. Put a CSV file of your own field
into `data/raw` and answer, in the README, the five questions of the lecture:

1. What kind is each column, and which can be averaged?
2. Where did the file come from, and under which licence?
3. What is one row?
4. In which unit is each column?
5. How are missing values marked?

Good places to look are the [Lithuanian open data portal](https://data.gov.lt),
Eurostat, Copernicus and Zenodo.

---

## Stretch goals

For students who already program and finish early. Answers are given for the
lecturer.

- In the Find box, switch on the button `.*` and search a fresh copy of the
  raw list for `(\d),(\d)`: it matches only a comma between two digits, 14
  matches, the mean line included. Replace with `$1.$2`. The semicolons stay.
- Hold `Shift+Alt` (macOS `Shift+Option`) and drag the mouse down through the
  table in `report.md`: one cursor per row in the same column.
- Install the **Rainbow CSV** extension from the Extensions view and open
  `loans.csv` again: each column gets its own colour.

## If students ask for more

Parts of VS Code that later lectures use. Show them for ten seconds if asked.

| Part of VS Code | Lecture |
|--|--|
| The Status Bar: encoding, line endings | 3 (How Computers Work) |
| The terminal in the Panel | 4 (Command Line) |
| Source Control | 5 (Git) |
| Running a Python script | 6 (Python Foundations) |

## Aims practised

♻️ provenance in the README · 📁 raw data kept untouched · ⚙️ one edit applied to every line · 🔧 the same steps on every system
