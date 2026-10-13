# Seminar 3 — What Are the 148 Bytes of `daily.csv`? Files as Bytes

**Paired lecture:** 03 How Computers Work · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student opens the files of `weather-project` as
bytes, names each of the 148 bytes of `daily.csv`, and sees what a line end,
an encoding and a file format do to the bytes.

Everything happens in VS Code with the **Hex Editor** extension. No terminal
today: Seminar 4 sets up the terminal and does the same by command.

## Run sheet

| Clock | Section | Typed | The room ends with |
|--|--|--|--|
| | **Part 1 · The Hex Editor** · 30 min | | |
| 0:00 | [1. Open the project, install the Hex Editor](#hex-editor) | `Ctrl+Shift+X`, `hex editor` | the extension installed |
| 0:10 | [2. Open `daily.csv` as bytes](#bytes) | **Open With...** > **Hex Editor** | `64 61 74 65` read as `date` |
| 0:20 | [3. Count the 148 bytes](#count) | the ten `0A` | 12 + 8 × 15 + 16 = 148 |
| | **Part 2 · Line ends and sizes** · 25 min | | |
| 0:30 | [4. The size in the file manager](#sizes) | **Get Info**, **Properties** | 148 bytes; 2 515 215 bytes |
| 0:40 | [5. A copy with CRLF](#crlf) | `LF` > `CRLF` in the Status Bar | 158 bytes, `0D 0A` |
| | **Part 3 · Text beyond ASCII** · 30 min | | |
| 0:55 | [6. Letters of two bytes](#utf8) | `Šilutė: 6.3 °C` | 15 characters, 18 bytes |
| 1:05 | [7. Another table: Windows 1257](#encoding) | **Save with Encoding** | 15 bytes; `�` as UTF-8 |
| 1:15 | [8. Three bytes in front: the BOM](#bom) | **UTF-8 with BOM** | `EF BB BF`, 21 bytes |
| | **Part 4 · Files that are not text** · 35 min | | |
| 1:25 | [9. The first bytes of a file](#magic) | `weather-files.zip` | `50 4B`, `PK` |
| 1:35 | [10. The same bytes, packed](#zip) | the two sizes | 22 % |
| 1:45 | [11. A checksum by hand](#checksum) | `6.3` byte by byte | 151 |
| 1:55 | [12. Wrap up](#wrap-up) | | |
| | **Optional, if the room is fast** | | |
| — | [13. A spreadsheet saves the export](#spreadsheet) | **Save As** `.xlsx` | `PK` again |
| — | [14. The README by another table](#readme-1257) | **Reopen with Encoding** | `Ā°C` |

**If time runs short:** section 8 on the projector only; stop after
section 11.

??? info "Before the session"
    - **Room:** internet for the extension. Each student has
      `weather-project` from [Seminar 1](seminar_01.md); section 1 has the
      zip for anyone without it.
    - **You:** nothing to prepare.
    - **Keys** are written for Windows, macOS in brackets. Bytes are written
      as two hex digits, as the Hex Editor shows them.

---

## Part 1 · The Hex Editor { #part-1 }

**0:00 to 0:30**

---

### 1. Open the project, install the Hex Editor { #hex-editor }

**0:00 · 10 min** · An extension adds a tool to VS Code; this one shows the bytes of a file.

1. Open VS Code, **File** > **Open Folder...** > `weather-project` (in your
   home folder) > **Open**.

    ??? warning "No `weather-project` from Seminar 1"
        Open `github.com/MindaugasSarpis/weather-project/releases`, under
        **Assets** click `weather-project-s1.zip`, and unpack it into your
        home folder (macOS: double-click it in **Downloads**, `Cmd+C`,
        `Cmd+Shift+H`, `Cmd+V`; Windows: right-click > **Extract All...** >
        **Browse...** > `C:\Users\` and your name > **Extract**). Then
        step 1.

2. Open the Extensions view: `Ctrl+Shift+X` (macOS `Cmd+Shift+X`).
3. Search:

    ```text
    hex editor
    ```

4. Take **Hex Editor** by **Microsoft** (the publisher under the name), click
   **Install**.

**Check:** the Extensions view lists **Hex Editor** as installed.

---

### 2. Open `daily.csv` as bytes { #bytes }

**0:10 · 10 min** · A file is a row of bytes; the editor turns them into letters by a table.

1. In the Side Bar, right-click `data/processed/daily.csv` > **Open
   With...** > **Hex Editor**.
2. Read the three columns: the **offset** (number of the first byte of the
   row, in hex), 16 bytes, the same bytes as text.

    ```text
    00000000  64 61 74 65 2C 74 65 6D 70 5F 63 0A 32 30 32 35  date,temp_c.2025
    00000010  2D 31 30 2D 30 31 2C 36 2E 33 0A 32 30 32 35 2D  -10-01,6.3.2025-
    ```

3. Click the first byte, `64`. The **Data Inspector** at the right shows it
   as binary, `01100100`, and as a number, `100`: 6 × 16 + 4 = 100, the
   letter `d` in the ASCII table.

4. Read the first five bytes with the room: `64 61 74 65 2C` is `d a t e ,`.

**Check:** everyone finds `2C`, the comma, after `date`.

---

### 3. Count the 148 bytes { #count }

**0:20 · 10 min** · The ten bytes nobody sees in the text are the line ends.

1. The whole file.

    ```text
    00000000  64 61 74 65 2C 74 65 6D 70 5F 63 0A 32 30 32 35  date,temp_c.2025
    00000010  2D 31 30 2D 30 31 2C 36 2E 33 0A 32 30 32 35 2D  -10-01,6.3.2025-
    00000020  31 30 2D 30 32 2C 35 2E 30 0A 32 30 32 35 2D 31  10-02,5.0.2025-1
    00000030  30 2D 30 33 2C 35 2E 36 0A 32 30 32 35 2D 31 30  0-03,5.6.2025-10
    00000040  2D 30 34 2C 37 2E 30 0A 32 30 32 35 2D 31 30 2D  -04,7.0.2025-10-
    00000050  30 35 2C 39 2E 34 0A 32 30 32 35 2D 31 30 2D 30  05,9.4.2025-10-0
    00000060  36 2C 31 30 2E 34 0A 32 30 32 35 2D 31 30 2D 30  6,10.4.2025-10-0
    00000070  37 2C 39 2E 32 0A 32 30 32 35 2D 31 30 2D 30 38  7,9.2.2025-10-08
    00000080  2C 39 2E 30 0A 32 30 32 35 2D 31 30 2D 30 39 2C  ,9.0.2025-10-09,
    00000090  39 2E 38 0A                                      9.8.
    ```

    The text column shows `.` for `0A`: a byte with no letter.

2. Find the ten `0A` bytes, one at the end of each line.
3. The last byte is at offset `93` (row `00000090`, column `03`): 0x93 = 147,
   counted from 0, so **148 bytes**.
4. Count by lines: the header `date,temp_c` and its `0A` is 12 bytes; a row
   such as `2025-10-01,6.3` and its `0A` is 15.

    ```text
    12 + 8 × 15 + 16 = 148
    ```

**Check:** everyone can say which row has 16 bytes, and why.

!!! question "Task: where does 6 October start?"
    1. At which offset does the row `2025-10-06,10.4` start? Find it, then
       compute it from the line lengths.
    2. Which byte, in hex, stands for each of `-`, `,` and `.`?

??? note "Answer"
    1. Offset `57`, in decimal 87 = 12 + 5 × 15: the header and five rows
       of 15 bytes come before it. The Hex Editor shows it in row
       `00000050`, column `07`.
    2. `-` is `2D`, `,` is `2C`, `.` is `2E`. In all of `daily.csv`: 91
       digits, 18 `2D`, 10 `2C`, 9 `2E`, 10 letters and `_`, 10 `0A`.

---

## Part 2 · Line ends and sizes { #part-2 }

**0:30 to 0:55**

---

### 4. The size in the file manager { #sizes }

**0:30 · 10 min** · The size in bytes is exact; kB and MB are rounded, and counted two ways.

1. Right-click `data/processed/daily.csv` > **Reveal in Finder** (Windows
   **Reveal in File Explorer**).
2. The size.

    === "macOS"

        Select the file, `Cmd+I` (**Get Info**).

        ```text
        Size: 148 bytes (4 KB on disk)
        ```

    === "Windows"

        Right-click > **Properties**.

        ```text
        Size:          148 bytes
        ```

3. The same for `data/raw/weather.csv`.

    === "macOS"

        ```text
        Size: 2,515,215 bytes (2.5 MB on disk)
        ```

    === "Windows"

        ```text
        Size:          2.39 MB (2,515,215 bytes)
        ```

    macOS counts 1 MB = 1 000 000 bytes, Windows 1 MB = 1 048 576 bytes:
    2 515 215 / 1 048 576 = 2.399.

**Check:** both files measured to the byte.

---

### 5. A copy with CRLF { #crlf }

**0:40 · 15 min** · A line end is one byte, `0A` (LF), on macOS and Linux; Windows programs often write two, `0D 0A` (CRLF).

1. In the Side Bar, click `data/processed/daily.csv`, `Ctrl+C`, `Ctrl+V`
   (macOS `Cmd`). A copy appears, `daily copy.csv`.
2. Rename it: `F2` (macOS `Enter`).

    ```text
    daily_crlf.csv
    ```

3. Open it. In the Status Bar, click `LF` and choose `CRLF`. Save if the tab
   shows a dot.
4. Right-click `daily_crlf.csv` > **Open With...** > **Hex Editor**.

    ```text
    00000000  64 61 74 65 2C 74 65 6D 70 5F 63 0D 0A 32 30 32  date,temp_c..202
    00000010  35 2D 31 30 2D 30 31 2C 36 2E 33 0D 0A 32 30 32  5-10-01,6.3..202
    ```

5. Its size, as in section 4.

    ```text
    158 bytes
    ```

    Ten lines, one `0D` more each: 148 + 10 = 158. In the text editor both
    files look the same.

**Check:** 158 bytes and `0D 0A` at each line end.

!!! question "Task: `weather.csv` with CRLF"
    1. `weather.csv` has 87 673 lines. How many bytes would it have with
       CRLF? Compute first.
    2. Check it on a copy in `data/processed` (never in `data/raw`), then
       delete the copy and `daily_crlf.csv` (right-click > **Delete**).

??? note "Answer"
    1. 2 515 215 + 87 673 = **2 602 888 bytes**.
    2. Copy `data/raw/weather.csv` into `data/processed` as in step 1, open
       the copy, `LF` > `CRLF` in the Status Bar, save, measure: 2 602 888
       bytes. Then delete both copies.

---

## Part 3 · Text beyond ASCII { #part-3 }

**0:55 to 1:25** · ASCII has 128 characters; UTF-8 writes every other letter in two to four bytes.

---

### 6. Letters of two bytes { #utf8 }

**0:55 · 10 min** · In UTF-8, `a` to `z` and the digits take one byte; `Š`, `ė` and `°` take two.

1. Click `results` in the Side Bar, then **New File**.

    ```text
    note.txt
    ```

2. Copy this line from the page, paste it, and press `Enter` once so that the
   file ends with a line end.

    ```text
    Šilutė: 6.3 °C
    ```

3. Windows: the Status Bar says `CRLF`; click it and choose `LF`.
4. Open `note.txt` with the Hex Editor.

    ```text
    00000000  C5 A0 69 6C 75 74 C4 97 3A 20 36 2E 33 20 C2 B0  ..ilut..: 6.3 ..
    00000010  43 0A                                            C.
    ```

5. Find the pairs: `Š` is `C5 A0`, `ė` is `C4 97`, `°` is `C2 B0`.

**Check:** 15 characters, with the line end, and 18 bytes.

---

### 7. Another table: Windows 1257 { #encoding }

**1:05 · 10 min** · An encoding is the table from characters to bytes; the same text gives other bytes in another table.

1. Click the tab of `note.txt` in the text editor. In the Status Bar, click
   `UTF-8` > **Save with Encoding** > **Baltic (Windows 1257)**.
2. Close the Hex Editor tab of `note.txt` and open it again.

    ```text
    00000000  D0 69 6C 75 74 EB 3A 20 36 2E 33 20 B0 43 0A     .ilut.: 6.3 .C.
    ```

    15 bytes: one byte per character. `Š` is `D0`, `ė` is `EB`, `°` is `B0`.

3. Read those bytes by the UTF-8 table: Status Bar `Windows 1257` >
   **Reopen with Encoding** > **UTF-8**.

    ```text
    �ilut�: 6.3 �C
    ```

    `D0`, `EB` and `B0` are not UTF-8 on their own: `�` marks each.

4. Read them by the right table again: **Reopen with Encoding** > **Baltic
   (Windows 1257)**.

**Check:** **Reopen** changes only what is shown; **Save with** changes the bytes.

---

### 8. Three bytes in front: the BOM { #bom }

**1:15 · 10 min** · Some programs put `EF BB BF`, the byte-order mark, in front of a UTF-8 file.

1. Status Bar: **Save with Encoding** > **UTF-8 with BOM**.
2. Open `note.txt` with the Hex Editor again.

    ```text
    00000000  EF BB BF C5 A0 69 6C 75 74 C4 97 3A 20 36 2E 33  .....ilut..: 6.3
    00000010  20 C2 B0 43 0A                                    ..C.
    ```

    18 + 3 = 21 bytes. The text editor shows no difference.

3. **Save with Encoding** > **UTF-8**: back to 18 bytes.

**Check:** the Status Bar says `UTF-8` and the Hex Editor starts with `C5 A0`.

!!! question "Task: count before you look"
    1. How many characters and how many bytes is `Vėjas 3 m/s` (no line
       end) in UTF-8, and in Windows 1257?
    2. Your `README.md` has one `°`. By how many bytes is its size larger
       than its number of characters?

??? note "Answer"
    1. 11 characters. UTF-8: 12 bytes (`ė` is two). Windows 1257: 11.
    2. By 1: `°` is `C2 B0`, the other characters are ASCII. On Windows the
       README may also have CRLF line ends (Status Bar): one more byte per
       line, which is not a character.

---

## Part 4 · Files that are not text { #part-4 }

**1:25 to 2:00**

---

### 9. The first bytes of a file { #magic }

**1:25 · 10 min** · The name's ending is a hint for people; the first bytes, the **magic number**, say what a file is.

1. **File** > **Open File...** > **Downloads** > `weather-files.zip` (from
   Seminar 1; or download it again from the Releases page).
2. VS Code says the file is binary. Click **Open Anyway**, then **Hex
   Editor**.

    ```text
    00000000  50 4B 03 04 14 00 00 00 00 00 C0 4B 4D 5D 00 00  PK.........KM]..
    00000010  00 00 00 00 00 00 00 00 00 00 0E 00 00 00 77 65  ..............we
    00000020  61 74 68 65 72 2D 66 69 6C 65 73 2F 50 4B 03 04  ather-files/PK..
    ```

3. `50 4B` is `PK`, the start of every ZIP file. Further on, the name of the
   folder in it, `weather-files/`.

| Kind | First bytes |
|--|--|
| text, CSV, Markdown | none: the text itself |
| ZIP, and `.docx`, `.xlsx` | `50 4B`, `PK` |
| PNG picture | `89 50 4E 47`, `.PNG` |
| PDF | `25 50 44 46`, `%PDF` |

**Check:** everyone finds `PK` at offset 0.

---

### 10. The same bytes, packed { #zip }

**1:35 · 10 min** · Lossless compression stores repeats once and gives back every byte.

1. The size of `weather-files.zip` in Finder or File Explorer.

    ```text
    562,255 bytes
    ```

2. It holds `weather.csv`, 2 515 215 bytes, and two small files.

    ```text
    562 255 / 2 515 215 = 0.22
    ```

3. Why it packs so well: every line of `weather.csv` starts with `20`, a
   year, `-`, a month. Scroll the Hex Editor of `weather.csv`: the same
   bytes again and again.
4. Unpacked in Seminar 1, the file had its 2 515 215 bytes again: nothing
   lost.

**Check:** 22 %, and the same bytes after unpacking.

!!! question "Task: a picture with a wrong name"
    1. Take a screenshot (macOS `Cmd+Shift+4`, drag; Windows `Win+PrtScn`,
       saved in **Pictures** > **Screenshots**). Open it in VS Code with the
       Hex Editor. What are its first bytes?
    2. Rename a copy of it to `screenshot.txt`. What are the first bytes
       now?

??? note "Answer"
    1. `89 50 4E 47 0D 0A 1A 0A`, `.PNG....`: a PNG picture.
    2. The same. A new name changes no byte: the file is still a PNG, and a
       text editor shows nonsense.

---

### 11. A checksum by hand { #checksum }

**1:45 · 10 min** · A checksum is a number computed from every byte; a changed byte changes it.

1. In the Hex Editor of `daily.csv`, the bytes of `6.3`, the first value:
   `36 2E 33`. Click each; the Data Inspector gives the numbers.

    ```text
    54 + 46 + 51 = 151
    ```

2. Change one byte in your head, `6.4`: `36 2E 34`.

    ```text
    54 + 46 + 52 = 152
    ```

    The sum differs: the change is caught.

3. Swap two, `3.6`: `33 2E 36`.

    ```text
    51 + 46 + 54 = 151
    ```

    The same sum: the swap is not caught. SHA-256, the checksum of Seminar
    4, is built so that no change keeps its number.

**Check:** everyone has 151, 152 and 151.

---

### 12. Wrap up { #wrap-up }

**1:55 · 5 min**

| To | Do |
|--|--|
| see the bytes of a file | right-click > **Open With...** > **Hex Editor** |
| find the size in bytes | **Get Info** (`Cmd+I`), **Properties** |
| change the line ends | `LF` / `CRLF` in the Status Bar |
| read by another table | Status Bar encoding > **Reopen with Encoding** |
| write by another table | **Save with Encoding**, only on purpose |

Seminar 4 measures the same files from the terminal.

---

## Optional, if the room is fast { #optional }

---

### 13. A spreadsheet saves the export { #spreadsheet }

**— · 10 min** · An `.xlsx` file is a ZIP of text files.

1. In Finder or File Explorer, open `weather-files/daily_export.csv` (the
   copy outside the project) in Excel or Numbers.
2. **File** > **Save As...** > **Excel Workbook (.xlsx)**, into
   `weather-files`.
3. Open the `.xlsx` with the Hex Editor: it starts with `50 4B`, `PK`.

**Check:** the same first bytes as `weather-files.zip`.

---

### 14. The README by another table { #readme-1257 }

**— · 5 min** · Mojibake: UTF-8 bytes read by the wrong table.

1. Open `README.md`. Status Bar `UTF-8` > **Reopen with Encoding** >
   **Baltic (Windows 1257)**.
2. The units in the Columns table.

    ```text
    | `temp_c` | air temperature | Ā°C |
    ```

    `C2` is `Ā` in Windows 1257, `B0` is `°`.

3. **Reopen with Encoding** > **UTF-8**. Nothing was saved.

**Check:** `°C` again.

---

## Aims practised

- 📁 **Files:** a file is a row of bytes, measured to the byte; its first
  bytes say what it is, its name does not.
- 🔧 **Tool-agnostic:** UTF-8 and LF give the same bytes on every system; a
  setting that differs is read in the Status Bar.
- ♻️ **Reproducibility:** a sum of the bytes tells two copies apart, the
  start of the checksums of Seminar 4.
