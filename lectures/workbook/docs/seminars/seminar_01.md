# Seminar 1 · Data

**Paired lecture:** 02 Introduction to Data · **Format:** follow-along, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's goal:** What do the weather files say? Every student has the folder `weather-project` open in VS
Code, with the station's two files in `data/raw`, the export repaired by hand
into `data/processed/daily.csv`, and a README that says what is in the folder,
where the data came from and what each column means.

Everything happens in VS Code and a web browser. No terminal today. In the
blocks stands the text to type, or what appears on the screen.

Further reading: [the VS Code user interface](https://code.visualstudio.com/docs/editing/getting-started/userinterface);
[Markdown in ten minutes, CommonMark](https://commonmark.org/help/).

**If time runs short:** section 6 in two minutes; leave out the Task of Part
3, nothing later needs `results/daily.md`.

??? info "Before the session"
    - **Room:** internet, and a laptop on which the student can install
      programs.
    - **You:** a VS Code with no `weather-project` folder yet. Today's files
      are `weather-s01.zip` on the Releases page of
      [MindaugasSarpis/weather-project](https://github.com/MindaugasSarpis/weather-project/releases);
      the session needs nothing from any other seminar.
    - **Keys** are written for Windows, macOS in brackets.

---

## Part 1 · VS Code and the README { #part-1 }

<!-- 0:00 to 0:40 -->

VS Code, a folder for the project, and its first file: the README.

---

### 1. Install VS Code { #install }

<!-- 0:00 · 10 min -->

VS Code is a free editor for text, the same on Windows, macOS and Linux.

1. Open the address in a browser, click **Download** for your system.

    ```text
    code.visualstudio.com
    ```

2. Install it.

    === "macOS"

        Open the downloaded file. Drag **Visual Studio Code** into
        **Applications**, then open it from there.

    === "Windows"

        Run the installer and keep every default.

3. Start VS Code. Close the **Chat** panel on the right if it is open.

**Check:** a window with a **Welcome** tab.

!!! warning "Windows asks for an administrator password"
    Take the **User Installer** on the download page. It needs none.

---

### 2. Make and open the project folder { #open-folder }

<!-- 0:10 · 5 min -->

VS Code works on a folder: one project, one folder.

1. **File** > **Open Folder...** The dialog opens; go to your home folder (the
   one with your user name).
2. Click **New Folder** in the dialog and type the name.

    ```text
    weather-project
    ```

3. Select `weather-project`, click **Open** (Windows **Select Folder**).
4. Answer **Yes, I trust the authors**.

**Check:** `WEATHER-PROJECT` at the top of the Side Bar, nothing under it.

---

### 3. Name the five regions, try three keys { #interface }

<!-- 0:15 · 5 min -->

The rest of the course calls the parts of the window by these names.

1. Point at each region and name it.

    | | Region | Holds |
    |--|--|--|
    | 1 | **Activity Bar** | the icons on the far left |
    | 2 | **Side Bar** | the files: the **Explorer** |
    | 3 | **Editor** | the open files, one tab each |
    | 4 | **Panel** | hidden today; the terminal, from Seminar 4 |
    | 5 | **Status Bar** | the line at the bottom: facts about the open file |

2. Hide the Side Bar and bring it back: `Ctrl+B` (macOS `Cmd+B`), twice.
3. Open the **Command Palette**: `Ctrl+Shift+P` (macOS `Cmd+Shift+P`). Type:

    ```text
    color theme
    ```

    Pick a theme with the arrow keys and `Enter`.

4. Make the text larger and smaller: `Ctrl+=` and `Ctrl+-` (macOS `Cmd`).

**Check:** everyone can name region 5.

---

### 4. Folders and a README { #folders }

<!-- 0:20 · 5 min -->

Files as they arrived are kept apart from everything made from them.

1. Move the mouse over the Side Bar; click the **New Folder** icon. Type:

    ```text
    data/raw
    ```

    The `/` makes both folders at once.

2. Click the empty area under the folders, then **New Folder** again.

    ```text
    data/processed
    ```

3. The same for `scripts` and `results`.
4. Click the empty area, then **New File**.

    ```text
    README.md
    ```

**Check:** the Explorer shows this tree.

```text
WEATHER-PROJECT
  data
    processed
    raw
  results
  scripts
  README.md
```

!!! warning "A new folder lands inside the selected folder"
    Drag it onto the empty area of the Side Bar.

---

### 5. Markdown and its preview { #markdown }

<!-- 0:25 · 10 min -->

Markdown is plain text with a few signs for structure; `README.md` is the first file anyone opens.

1. In `README.md`, type:

    ```text
    # Weather Station

    The hourly log of one weather station, 2016 to 2025, and a table of daily
    mean temperatures typed into a spreadsheet from it.
    ```

2. A dot on the tab means *not saved*. Save: `Ctrl+S` (macOS `Cmd+S`).
3. Switch on **File** > **Auto Save**: from now on every change is saved.
4. Open the preview beside the text: `Ctrl+K`, release, then `V` (macOS
   `Cmd+K`, then `V`).
5. Add a section heading below the paragraph.

    ```text
    ## Folders
    ```

**Check:** the preview shows a large title, a paragraph and a smaller heading.

| You type | The preview shows |
|--|--|
| `# Title` | the title of the page |
| `## Section` | a section heading |
| `**text**` | **bold** |
| `- item` | a list item |
| `` `name` `` | a file name in code type |
| `| a | b |` | a row of a table |

---

### 6. Three mistakes, on purpose { #mistakes }

<!-- 0:35 · 5 min -->

The preview is the test. Make each mistake, read the preview, undo with `Ctrl+Z` (macOS `Cmd+Z`).

1. Delete the space after `#` in the title.

    ```text
    #Weather Station
    ```

    The preview shows `#Weather Station` as plain text.

2. Put an empty line inside the paragraph, after `daily`.

    The preview shows two paragraphs: only an empty line starts a new one.

3. Write a bold word with a space before the closing stars.

    ```text
    **Station **
    ```

    The preview shows the stars.

**Check:** the README is back as it was at the end of section 5.

!!! question "Task: the Folders section"
    Under `## Folders`, write a table with two columns, **Folder** and **What
    goes in**, and one row for each of the four folders. Check it in the
    preview.

??? success "Answer"
    ```text
    | Folder | What goes in |
    |--|--|
    | `data/raw` | files as they arrived, never edited |
    | `data/processed` | files made from `data/raw` by commands and scripts |
    | `scripts` | programs |
    | `results` | numbers and figures the programs produce |
    ```

    Without the second line, `|--|--|`, the preview shows text with `|`
    signs, not a table.

---

## Part 2 · The files arrive { #part-2 }

<!-- 0:40 to 1:10 -->

The station's operator sent two files by e-mail.

---

### 7. Download the station's files { #download }

<!-- 0:40 · 10 min -->

Files from outside go into `data/raw` and are never edited there.

1. Open the Releases page of the course repository.

    ```text
    github.com/MindaugasSarpis/weather-project/releases
    ```

2. Under **Assets**, click `weather-s01.zip`. The browser saves it in
   **Downloads**.
3. Unpack it into your home folder.

    === "macOS"

        In Finder, open **Downloads** and double-click `weather-s01.zip`.
        Select the new folder `weather-s01`, press `Cmd+C`, then
        `Cmd+Shift+H` (your home folder), then `Cmd+V`.

    === "Windows"

        In File Explorer, open **Downloads**, right-click
        `weather-s01.zip` > **Extract All...** > **Browse...**, choose
        `C:\Users\` and your name, **Select Folder**, **Extract**.

4. Open the folder `weather-s01` in Finder or File Explorer: three files.

    ```text
    daily_export.csv
    message.txt
    weather.csv
    ```

5. Drag `weather.csv` and `daily_export.csv` onto `data/raw` in the Side Bar
   of VS Code. They are copied there.
6. Drag `message.txt` onto the editor area. It opens in a tab, and is not
   copied into the project.

    ```text
    here are the two files of our weather station:

    weather.csv        the hourly log, 1 January 2016 to 31 December 2025
    daily_export.csv   the daily mean temperature of 1 to 9 October 2025,
                       typed into a spreadsheet and exported from it

    You may use them for anything, with no conditions (CC0).
    ```

**Check:** `data/raw` holds `daily_export.csv` and `weather.csv`.

---

### 8. Read the long file { #data-file }

<!-- 0:50 · 10 min -->

How many rows, what one row is, and how a missing value is marked: the file shows it.

1. Click `data/raw/weather.csv`. The first lines:

    ```text
    time,temp_c,humidity_pct,wind_ms
    2016-01-01T00:00,-4.4,93,2.5
    2016-01-01T01:00,-4.8,95,2.6
    ```

2. Read row 2 aloud: "at 01:00 on 1 January 2016, −4.8 °C, 95 % humidity,
   wind 2.6 m/s".
3. Jump to the end: `Ctrl+End` (macOS `Cmd+↓`). The line number on the left:

    ```text
    87674
    ```

    The last line is empty. 87 673 lines, minus the header: **87 672 rows**,
    one per hour of ten years (10 × 365 × 24 + 3 leap days × 24).

4. Go to a line: `Ctrl+G` (the same on macOS), type `5000`, `Enter`.

    ```text
    2016-07-27T06:00,18.2,71,1.1
    ```

5. Find a value: `Ctrl+F` (macOS `Cmd+F`), type `-999`. The counter:

    ```text
    1 of 120
    ```

    Press `Enter` a few times: all are in `temp_c`, 22 to 26 July 2019.

6. Read the Status Bar, bottom right: `UTF-8` and `LF`.

**Check:** 87 672 rows, and 120 rows with `-999`.

---

### 9. Write where the data came from { #provenance }

<!-- 1:00 · 10 min -->

Someone else, or you in six months, must be able to tell where the files came from.

1. In `README.md`, under the Folders table, add the **Data** section. The
   source and the date come from `message.txt`.

    ```text
    ## Data

    - `data/raw/weather.csv`: one row per hour, from 2016-01-01 00:00 to
      2025-12-31 23:00.
    - `data/raw/daily_export.csv`: the daily mean temperature of 1 to 9 October
      2025, exported from a spreadsheet.
    - **Source:** the station's operator, by e-mail
    - **Received:** 2026-10-13
    ```

2. Check the list in the preview: four items, two words in bold.

**Check:** a stranger reading the README knows what each file is and who sent it.

!!! question "Task: the columns of `weather.csv`"
    Add a section **Columns of weather.csv** with a table: **Column**,
    **Meaning**, **Unit**, one row per column. Find each unit from the
    numbers: `temp_c` runs from −16.3 to 32.4, `humidity_pct` from 34 to
    100, `wind_ms` has a median of 3.5 and at most 12. Below the table, one
    line on the `-999` rows.

??? success "Answer"
    ```text
    ## Columns of `weather.csv`

    | Column | Meaning | Unit |
    |--|--|--|
    | `time` | start of the hour | ISO 8601 |
    | `temp_c` | air temperature | °C |
    | `humidity_pct` | relative humidity | % |
    | `wind_ms` | wind speed | m/s |

    Missing value: `temp_c` is `-999` in 120 rows, 2019-07-22 to 07-26, when
    the temperature sensor was down.
    ```

    −999 °C is below absolute zero (−273.15 °C): a mark for "no value", not
    a temperature. `wind_ms` is metres per second; milliseconds of wind make
    no sense.

---

## Part 3 · Repair the export { #part-3 }

<!-- 1:10 to 1:55 -->

`daily_export.csv` has to become a plain table, on a copy.

```text
nr;date;temp_c          date,temp_c
1;2025-10-01;6,3   ->   2025-10-01,6.3
...                     ...
9;2025-10-09;9,8        2025-10-09,9.8
;mean;7,97
```

---

### 10. A copy to repair { #copy }

<!-- 1:10 · 5 min -->

A file in `data/raw` is never edited; the edits go on a copy in `data/processed`.

1. Click `data/raw/daily_export.csv` in the Side Bar. Copy it: `Ctrl+C`
   (macOS `Cmd+C`).
2. Click `data/processed`. Paste: `Ctrl+V` (macOS `Cmd+V`).
3. Rename the copy: `F2` (macOS `Enter`), type the new name, `Enter`.

    ```text
    daily.csv
    ```

4. Open `data/processed/daily.csv`.

**Check:** the tab reads `daily.csv` and the path above the text says `processed`.

---

### 11. Delete the mean line { #lines }

<!-- 1:15 · 5 min -->

One row is one day; the mean line is not a day.

1. Click anywhere in the line `;mean;7,97`.
2. Delete the whole line: `Ctrl+Shift+K` (macOS `Cmd+Shift+K`).
3. Move a line and put it back: `Alt+↑`, then `Alt+↓` (macOS `Option`).

**Check:** ten lines: the header and nine days.

---

### 12. Find and Replace { #replace }

<!-- 1:20 · 10 min -->

The counter shows how many matches there are before anything changes.

1. Open Replace: `Ctrl+H` (macOS `Cmd+Option+F`).
2. Find `,` and replace with `.`. Read the counter first.

    ```text
    1 of 9
    ```

    Click **Replace All** (the button right of the Replace box).

3. Find `;` and replace with `,`.

    ```text
    1 of 20
    ```

    **Replace All**.

4. Close the box: `Esc`.

    ```text
    nr,date,temp_c
    1,2025-10-01,6.3
    2,2025-10-02,5.0
    ```

**Check:** commas between the values, points in the numbers.

!!! warning "In the other order the decimal comma is lost"
    `;` to `,` first makes `1,2025-10-01,6,3`. Undo with `Ctrl+Z` and start
    with `,` to `.`.

---

### 13. A cursor on every line { #cursors }

<!-- 1:30 · 10 min -->

What is typed or deleted happens at every cursor at once.

1. Select the ten lines: click before `nr`, then `Shift`+click after the
   last `9.8`.
2. A cursor at the end of every line: `Shift+Alt+I` (macOS `Shift+Option+I`).
3. All cursors to the line start: `Home` (macOS `Cmd+←`).
4. Select the first word: `Ctrl+Shift+→` (macOS `Option+Shift+→`).
5. Add the comma: `Shift+→`.
6. Delete: `Delete` (macOS `Backspace`).
7. Back to one cursor: `Esc`.

    ```text
    date,temp_c
    2025-10-01,6.3
    2025-10-02,5.0
    ```

**Check:** ten lines, two columns, no `nr`.

---

### 14. Check the size, write down the edits { #note }

<!-- 1:40 · 5 min -->

The size in bytes shows that nothing else changed.

1. Right-click `data/processed/daily.csv` > **Reveal in Finder** (Windows
   **Reveal in File Explorer**).
2. The size.

    === "macOS"

        Select the file, `Cmd+I` (**Get Info**): **148 bytes**.

    === "Windows"

        Right-click the file > **Properties**: **Size: 148 bytes**.

3. The arithmetic: 180 − 11 (`;mean;7,97` and its line end) − 21 (`nr;`
   and `1;` to `9;`) = 148. The replacements swap one character for one.
4. In `README.md`, add one item at the end of the Data list.

    ```text
    - **Cleaned copy:** `data/processed/daily.csv`. Mean line deleted, `,` to
      `.`, `;` to `,`, column `nr` deleted.
    ```

**Check:** 148 bytes, and the four edits in the README.

!!! question "Task: the daily table in Markdown"
    Make `results/daily.md`: the ten lines of `daily.csv` as a Markdown
    table, with the multi-cursor keys and no typing line by line. Check it in
    the preview.

??? success "Answer"
    1. Copy all of `daily.csv` into a new file `results/daily.md`.
    2. Select one `,`, then all of them: `Ctrl+Shift+L` (macOS
       `Cmd+Shift+L`). Type ` | `.
    3. Select the ten lines (click, `Shift`+click), `Shift+Alt+I`, type
       ` |`. `Home` (macOS `Cmd+←`), type `| `. `Esc`.
    4. In line 1, `Ctrl+Enter` (macOS `Cmd+Enter`) opens a line below it.
       Type `|--|--|`.

    ```text
    | date | temp_c |
    |--|--|
    | 2025-10-01 | 6.3 |
    | 2025-10-02 | 5.0 |
    ```

---

### 15. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->


| To | Press |
|--|--|
| open the Command Palette | `Ctrl+Shift+P` |
| preview Markdown | `Ctrl+K`, then `V` |
| go to the end, to a line | `Ctrl+End`, `Ctrl+G` |
| find, replace | `Ctrl+F`, `Ctrl+H` |
| delete a line | `Ctrl+Shift+K` |
| a cursor on every line | `Ctrl+A`, `Shift+Alt+I` |
| select every match | `Ctrl+Shift+L` |

macOS: `Cmd` for `Ctrl`, `Option` for `Alt`.

---

## Optional, if the room goes fast { #optional }

---

### 16. Sort the lines: numbers sort as text { #sort }

<!-- — · 5 min -->

The editor sees characters, not numbers.

1. **File** > **New Text File**. Type five temperatures of `daily.csv`, one
   per line: `6.3`, `5.0`, `10.4`, `9.8`, `5.6`.
2. Select them, `Ctrl+Shift+P`, type `sort lines`, take **Sort Lines
   Ascending**.

    ```text
    10.4
    5.0
    5.6
    ```

    `10.4` comes first: the character `1` comes before `5`.

3. Close the file without saving.

**Check:** everyone can say why `10.4` stands first.

---

### 17. Rename a column everywhere { #rename }

<!-- — · 5 min -->

`Ctrl+D` adds the next match to the selection; every match is seen before it changes.

1. In `results/daily.md`, double-click `temp_c`.
2. `Ctrl+D` (macOS `Cmd+D`) until every `temp_c` of the file is selected.
3. Type `t_mean_c` once.

**Check:** the preview shows `t_mean_c` in the header.

---

### 18. The export in a spreadsheet { #spreadsheet }

<!-- — · 10 min -->

A spreadsheet reads the export by the settings of the laptop.

1. In Finder or File Explorer, double-click `weather-s01/daily_export.csv`
   (the copy outside the project).
2. Look: one column per value, or all of a line in column A; `6,3` as a
   number or as text.
3. Close the spreadsheet with **Don't Save**.

**Check:** two neighbours with different settings see the file differently.

---

### 19. Advanced tasks { #advanced }

<!-- — · 20 min -->

Harder questions to the same files, answered with the keys of today.

!!! question "Task: noon below freezing, by a pattern"
    How many days of 2025 were below 0 °C at noon? In `weather.csv`, open
    Find (`Ctrl+F`, macOS `Cmd+F`) and switch on **Use Regular Expression**
    (the `.*` button, or `Alt+R`, macOS `Cmd+Option+R`). In a pattern, `^`
    is the start of a line, `\d` any digit.

??? success "Answer"
    ```text
    ^2025-\d\d-\d\dT12:00,-
    ```

    The counter reads `1 of 85`: the line starts with a date of 2025, the
    hour is 12:00, and the temperature after the comma starts with a minus.
    None of the `-999` rows is in 2025.

!!! question "Task: the warmest and the coldest hour"
    The warmest hour of the ten years is 32.4 °C, the coldest −16.3 °C. On
    which lines of `weather.csv` are they, and when? Add both to the
    README's Columns section.

??? success "Answer"
    Find `,32.4,` and `,-16.3,`, with the commas, so that `132.4` or
    `-16.35` could not match. Each counter reads `1 of 1`, and the line
    number is on the left.

    ```text
    21593  2018-06-18T15:00,32.4,52,3.1
    79063  2025-01-07T05:00,-16.3,100,3.3
    ```

    ```text
    Warmest hour: 32.4 °C, 2018-06-18 15:00 (line 21 593).
    Coldest hour: −16.3 °C, 2025-01-07 05:00 (line 79 063).
    ```

!!! question "Task: check the spreadsheet's mean"
    The export ended with `;mean;7,97`, deleted in section 11. Compute the
    mean of the nine temperatures of `daily.csv` with a calculator. Does
    the spreadsheet's number agree? Write the check into the README.

??? success "Answer"
    ```text
    6.3 + 5.0 + 5.6 + 7.0 + 9.4 + 10.4 + 9.2 + 9.0 + 9.8 = 71.7
    71.7 / 9 = 7.9667
    ```

    7.97, rounded to two decimals: the line agreed, and could go because
    it is computed from the nine rows. In the README, under the Data list:

    ```text
    The deleted mean line, 7.97, is the mean of the nine days (71.7 / 9).
    ```

---

## Aims practised

- 📁 **Files:** raw files kept as they arrived, edits made on a copy and
  checked by the size in bytes.
- ♻️ **Reproducibility:** the README says what each file is, where it came
  from, what each column means and what was changed.
- 🔧 **Tool-agnostic:** plain text and Markdown, read the same by any editor
  on any system.
