# Seminar 3 · Computers

**Paired lecture:** 03 How Computers Work · **Format:** follow-along, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's goal:** What are the 148 bytes of `daily.csv`? Every student types
the station's ten-line table `daily.csv` into a new folder, opens it as
bytes, names each of its 148 bytes, finds the two `-999` of the evening the
sensor failed in the bytes of `weather.csv`, and sees what a line end, an
encoding and a file format do to the bytes.

Everything happens in VS Code with the **Hex Editor** extension. No terminal
today: Seminar 4 sets up the terminal and does the same by command. In the
blocks stands what the Hex Editor or the text editor shows, or the text to
type.

**If time runs short:** section 9, the BOM, on the projector only; stop
after section 12, the checksum.

??? info "Before the session"
    - **Room:** internet, for the extension. The session needs nothing from
      any other seminar: every file is typed from this page.
    - **Missing a tool?** No VS Code: [Setup, step 1](../setup.md#vscode).
    - **You:** nothing to prepare.
    - **Keys** are written for Windows, macOS in brackets. Bytes are written
      as two hex digits, as the Hex Editor shows them.

---

## Part 1 · The Hex Editor { #part-1 }

<!-- 0:00 to 0:40 -->

A file is a row of bytes; the Hex Editor shows each one as two hex digits.

---

### 1. Install the Hex Editor, type `daily.csv` { #hex-editor }

<!-- 0:00 · 10 min -->

An extension adds a tool to VS Code; this one shows the bytes of a file. `daily.csv` holds the station's daily mean temperature, 1 to 9 October 2025: a header and nine rows.

1. Open the Extensions view: `Ctrl+Shift+X` (macOS `Cmd+Shift+X`).
2. Search:

    ```text
    hex editor
    ```

3. Take **Hex Editor** by **Microsoft** (the publisher under the name), click
   **Install**.
4. **File** > **Open Folder...**, go to your home folder (the one with your
   user name), click **New Folder** in the dialog and type the name.

    ```text
    weather-s03
    ```

5. Select `weather-s03`, click **Open** (Windows **Select Folder**), and
   answer **Yes, I trust the authors**.
6. Move the mouse over the Side Bar, click the **New File** icon and type
   the name.

    ```text
    daily.csv
    ```

7. Copy the block with the button at its top right, paste it into
   `daily.csv`, then press `Enter` once: the cursor stands on line 11, which
   stays empty.

    ```text
    date,temp_c
    2025-10-01,6.3
    2025-10-02,5.0
    2025-10-03,5.6
    2025-10-04,7.0
    2025-10-05,9.4
    2025-10-06,10.4
    2025-10-07,9.2
    2025-10-08,9.0
    2025-10-09,9.8
    ```

8. Set the line end and save. Windows: the Status Bar says `CRLF`; click
   it and choose `LF`. Then `Ctrl+S` (macOS `Cmd+S`): the dot on the tab
   goes.

**Check:** `daily.csv` saved with `LF` in the Status Bar, and the Extensions
view lists **Hex Editor** as installed.

---

### 2. Open `daily.csv` as bytes { #bytes }

<!-- 0:10 · 10 min -->

A file is a row of bytes; the editor turns them into letters by a table.

1. In the Side Bar, right-click `daily.csv` > **Open With...** > **Hex
   Editor**.
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

<!-- 0:20 · 10 min -->

The ten bytes nobody sees in the text are the line ends.

1. Read the whole file, ten rows in the Hex Editor.

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

---

### 4. Find `-999` in the bytes of `weather.csv` { #missing }

<!-- 0:30 · 10 min -->

`weather.csv` holds six hours of the station's log, 21 July 2019 20:00 to 22 July 01:00, the evening the temperature sensor failed: the log writes `-999` where a reading is missing.

1. Click the empty area of the Side Bar, then **New File**, and type the
   name.

    ```text
    weather.csv
    ```

2. Copy the six hours with the button at the block's top right, paste them,
   then press `Enter` once: line 8 stays empty. Windows: click `CRLF` in the
   Status Bar and choose `LF`. Save: `Ctrl+S` (macOS `Cmd+S`).

    ```text
    time,temp_c,humidity_pct,wind_ms
    2019-07-21T20:00,27.3,63,4.5
    2019-07-21T21:00,25.6,65,4.0
    2019-07-21T22:00,24.6,68,3.5
    2019-07-21T23:00,23.6,74,3.4
    2019-07-22T00:00,-999,76,3.2
    2019-07-22T01:00,-999,81,3.0
    ```

3. Right-click `weather.csv` > **Open With...** > **Hex Editor**. The last
   byte, `0A`, is at offset `CE` = 206: **207 bytes**.

    ```text
    00000000  74 69 6D 65 2C 74 65 6D 70 5F 63 2C 68 75 6D 69  time,temp_c,humi
    00000010  64 69 74 79 5F 70 63 74 2C 77 69 6E 64 5F 6D 73  dity_pct,wind_ms
    00000020  0A 32 30 31 39 2D 30 37 2D 32 31 54 32 30 3A 30  .2019-07-21T20:0
    00000030  30 2C 32 37 2E 33 2C 36 33 2C 34 2E 35 0A 32 30  0,27.3,63,4.5.20
    00000040  31 39 2D 30 37 2D 32 31 54 32 31 3A 30 30 2C 32  19-07-21T21:00,2
    00000050  35 2E 36 2C 36 35 2C 34 2E 30 0A 32 30 31 39 2D  5.6,65,4.0.2019-
    00000060  30 37 2D 32 31 54 32 32 3A 30 30 2C 32 34 2E 36  07-21T22:00,24.6
    00000070  2C 36 38 2C 33 2E 35 0A 32 30 31 39 2D 30 37 2D  ,68,3.5.2019-07-
    00000080  32 31 54 32 33 3A 30 30 2C 32 33 2E 36 2C 37 34  21T23:00,23.6,74
    00000090  2C 33 2E 34 0A 32 30 31 39 2D 30 37 2D 32 32 54  ,3.4.2019-07-22T
    000000A0  30 30 3A 30 30 2C 2D 39 39 39 2C 37 36 2C 33 2E  00:00,-999,76,3.
    000000B0  32 0A 32 30 31 39 2D 30 37 2D 32 32 54 30 31 3A  2.2019-07-22T01:
    000000C0  30 30 2C 2D 39 39 39 2C 38 31 2C 33 2E 30 0A     00,-999,81,3.0.
    ```

4. Click into the bytes, `Ctrl+F` (macOS `Cmd+F`), type `-999` with the
   text option. Find stops at offset `A6` (row `000000A0`, column `06`);
   `Enter` goes on to `C3`.

    ```text
    000000A0  30 30 3A 30 30 2C 2D 39 39 39 2C 37 36 2C 33 2E  00:00,-999,76,3.
    000000C0  30 30 2C 2D 39 39 39 2C 38 31 2C 33 2E 30 0A     00,-999,81,3.0.
    ```

    `-999` is `2D 39 39 39`, four characters of text, as `23.6` is
    `32 33 2E 36`. Nothing in the bytes says "missing": a program has to be
    told.

**Check:** `weather.csv` has 207 bytes, and Find stops twice on
`2D 39 39 39`, at `A6` and at `C3`.

!!! question "Task: where the `-999` rows start"
    1. At which offset does the line of 22 July 00:00, the first `-999`
       row, start? Compute it from the line lengths, then find it.
    2. Which byte, in hex, stands for each of `-`, `,` and `.`?

??? success "Answer"
    1. The header is 33 bytes (32 characters and `0A`), every hour 29:
       33 + 4 × 29 = **149**, `0x95`, row `00000090`, column `05`.

        ```text
        00000090  2C 33 2E 34 0A 32 30 31 39 2D 30 37 2D 32 32 54  ,3.4.2019-07-22T
        ```

        `0A` at `0x94` ends 23:00, the last hour with a temperature;
        `-999` follows at `0xA6` = 166 = 149 + 17, after the time and a
        comma. In the station's full log the lines run from 28 to 31
        bytes (`0.0` or `-10.3`, a humidity of `80` or `100`): there only
        Find can tell where a line starts.
    2. `-` is `2D`, `,` is `2C`, `.` is `2E`. In all of `daily.csv`: 91
       digits, 18 `2D`, 10 `2C`, 9 `2E`, 10 letters and `_`, 10 `0A`.

---

## Part 2 · Line ends and sizes { #part-2 }

<!-- 0:40 to 1:00 -->

The end of a line is a byte too, and not the same byte on every system.

---

### 5. The size in the file manager { #sizes }

<!-- 0:40 · 5 min -->

The size in bytes is exact; kB and MB are rounded, and counted two ways.

1. Right-click `daily.csv` > **Reveal in Finder** (Windows **Reveal in File
   Explorer**).
2. The size of `daily.csv`.

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

    Larger files are shown in MB, rounded, and macOS and Windows count
    them differently: the station's full log, 2 515 215 bytes, is 2.5 MB in
    Finder (1 MB = 1 000 000 bytes) and 2.39 MB in File Explorer
    (1 MB = 1 048 576 bytes).

3. Select `weather.csv`, next to `daily.csv`, and read its size by **Get
   Info** (Windows **Properties**): the 207 bytes of the Hex Editor.

    ```text
    207 bytes
    ```

**Check:** `daily.csv` measured to the byte, 148, and `weather.csv`, 207.

---

### 6. A copy with CRLF { #crlf }

<!-- 0:40 · 15 min -->

A line end is one byte, `0A` (LF), on macOS and Linux; Windows programs often write two, `0D 0A` (CRLF).

1. In the Side Bar, click `daily.csv`, `Ctrl+C`, `Ctrl+V` (macOS `Cmd`). A
   copy appears, `daily copy.csv`.
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

5. Its size, by **Get Info** in Finder (Windows **Properties** in File
   Explorer).

    ```text
    158 bytes
    ```

    Ten lines, one `0D` more each: 148 + 10 = 158. In the text editor both
    files look the same.

**Check:** 158 bytes and `0D 0A` at each line end.

!!! question "Task: where does 6 October start with CRLF?"
    1. At which offset does `2025-10-06` start in `daily_crlf.csv`?
       Compute it from the line lengths, then find it.
    2. How many bytes would `daily.csv` have without the line end after
       `9.8`? And `daily_crlf.csv`?
    3. Delete `daily_crlf.csv` (right-click > **Delete**).

??? success "Answer"
    1. Offset `5D`, in decimal 93 = 13 + 5 × 16: with CRLF the header is 13
       bytes and each row before it 16. The Hex Editor shows it in row
       `00000050`, column `0D`.
    2. 147 and 156: the last line end is one byte with LF, two with CRLF.

---

## Part 3 · Text beyond ASCII { #part-3 }

<!-- 1:00 to 1:25 -->

ASCII has 128 characters; UTF-8 writes every other letter in two to four bytes.

---

### 7. Letters of two bytes { #utf8 }

<!-- 1:00 · 10 min -->

In UTF-8, `a` to `z` and the digits take one byte; `Š`, `ė` and `°` take two.

1. Click the empty area of the Side Bar, then **New File**.

    ```text
    note.txt
    ```

2. Copy this line from the page, paste it, and press `Enter` once so that the
   file ends with a line end.

    ```text
    Šilutė: 6.3 °C
    ```

3. Set the line end and save. Windows: the Status Bar says `CRLF`; click
   it and choose `LF`. Then `Ctrl+S` (macOS `Cmd+S`).
4. Right-click `note.txt` > **Open With...** > **Hex Editor**.

    ```text
    00000000  C5 A0 69 6C 75 74 C4 97 3A 20 36 2E 33 20 C2 B0  ..ilut..: 6.3 ..
    00000010  43 0A                                            C.
    ```

5. Find the pairs: `Š` is `C5 A0`, `ė` is `C4 97`, `°` is `C2 B0`.

**Check:** 15 characters, with the line end, and 18 bytes.

---

### 8. Another table: Windows 1257 { #encoding }

<!-- 1:10 · 10 min -->

An encoding is the table from characters to bytes; the same text gives other bytes in another table.

1. Click the tab of `note.txt` in the text editor. In the Status Bar, click
   `UTF-8` > **Save with Encoding** > **Baltic (Windows 1257)**.
2. Close the Hex Editor tab of `note.txt` and open it again.

    ```text
    00000000  D0 69 6C 75 74 EB 3A 20 36 2E 33 20 B0 43 0A     .ilut.: 6.3 .C.
    ```

    15 bytes: one byte per character. `Š` is `D0`, `ė` is `EB`, `°` is `B0`.

3. Read the Windows 1257 bytes by the UTF-8 table: Status Bar
   `Windows 1257` > **Reopen with Encoding** > **UTF-8**.

    ```text
    �ilut�: 6.3 �C
    ```

    `D0`, `EB` and `B0` are not UTF-8 on their own: `�` marks each.

4. Read the bytes by their own table again: Status Bar `UTF-8` > **Reopen
   with Encoding** > **Baltic (Windows 1257)**. `Šilutė: 6.3 °C` is back.

**Check:** **Reopen** changes only what is shown; **Save with** changes the bytes.

---

### 9. Three bytes in front: the BOM { #bom }

<!-- 1:20 · 5 min -->

Some programs put `EF BB BF`, the byte-order mark, in front of a UTF-8 file.

1. In the text editor tab of `note.txt`, click `Windows 1257` in the Status
   Bar > **Save with Encoding** > **UTF-8 with BOM**.
2. Close the Hex Editor tab of `note.txt` and open it again.

    ```text
    00000000  EF BB BF C5 A0 69 6C 75 74 C4 97 3A 20 36 2E 33  .....ilut..: 6.3
    00000010  20 C2 B0 43 0A                                    ..C.
    ```

    18 + 3 = 21 bytes. The text editor shows no difference.

3. Status Bar `UTF-8 with BOM` > **Save with Encoding** > **UTF-8**: back
   to 18 bytes.

**Check:** the Status Bar says `UTF-8` and the Hex Editor starts with `C5 A0`.

!!! question "Task: count before you look"
    1. How many characters and how many bytes is `Vėjas 3 m/s` (no line
       end) in UTF-8, and in Windows 1257?
    2. How many bytes would `daily.csv` have saved with Windows 1257? With
       UTF-8 with BOM?

??? success "Answer"
    1. 11 characters. UTF-8: 12 bytes (`ė` is two). Windows 1257: 11.
    2. 148 in Windows 1257: every character of `daily.csv` is ASCII, and
       the 128 ASCII characters have the same bytes in both tables. With
       the BOM, 148 + 3 = 151.

---

## Part 4 · Files that are not text { #part-4 }

<!-- 1:25 to 2:00 -->

A picture, a zip or a spreadsheet is bytes as well, but not text; its first bytes say what it is.

---

### 10. The first bytes of a file { #magic }

<!-- 1:25 · 10 min -->

The name's ending is a hint for people; the first bytes, the **magic number**, say what a file is.

1. Pack today's folder into a zip.

    === "macOS"

        In Finder, `Cmd+Shift+H` (your home folder), right-click
        `weather-s03` > **Compress "weather-s03"**. `weather-s03.zip`
        appears next to the folder.

    === "Windows"

        In File Explorer, open `C:\Users\` and your name, right-click
        `weather-s03` > **Compress to ZIP file** (or **Compress to** >
        **ZIP File**; Windows 10: **Send to** > **Compressed (zipped)
        folder**). `weather-s03.zip` appears next to the folder.

2. In VS Code, **File** > **Open File...** (macOS **Open...**) >
   `weather-s03.zip` in your home folder. VS Code says the file is binary.
   Click **Open Anyway**, then **Hex Editor**.
3. The row `00000000` starts with `50 4B 03 04`, `PK` in the text column:
   the start of every ZIP file. From offset `1E`, after 30 bytes, stands
   the name of the first thing packed. The bytes between hold the date and
   the packing program, so they differ from laptop to laptop.
4. Click the Hex Editor tab of `daily.csv`: it starts with `64 61`, `da`,
   its own text. Other kinds of file start with their own bytes.

    | Kind | First bytes |
    |--|--|
    | text, CSV, Markdown | none: the text itself |
    | ZIP, and `.docx`, `.xlsx` | `50 4B`, `PK` |
    | PNG picture | `89 50 4E 47`, `.PNG` |
    | PDF | `25 50 44 46`, `%PDF` |

**Check:** everyone finds `PK` at offset 0.

!!! question "Task: a picture with a wrong name"
    1. Take a screenshot (macOS `Cmd+Shift+4`, drag; Windows `Win+PrtScn`,
       saved in **Pictures** > **Screenshots**). Open it in VS Code with the
       Hex Editor. What are its first bytes?
    2. Rename a copy of it to `screenshot.txt`. What are the first bytes
       now?

??? success "Answer"
    1. `89 50 4E 47 0D 0A 1A 0A`, `.PNG....`: a PNG picture.
    2. The same. A new name changes no byte: the file is still a PNG, and a
       text editor shows nonsense.

---

### 11. Measure the zip, pack a file of repeats { #zip }

<!-- 1:35 · 10 min -->

Lossless compression stores repeats once and gives back every byte; a zip also stores the name of every file in it, twice.

1. The size of `weather-s03.zip`, by **Get Info** (Windows
   **Properties**): more than the 148 + 207 + 18 = 373 bytes of
   `daily.csv`, `weather.csv` and `note.txt`. A zip stores each file's name
   twice, with a header of 30 bytes in front and an entry of 46 at the end.
   For `weather-s03/daily.csv`, 21 characters, that is at least:

    ```text
    30 + 21 + 46 + 21 = 118 bytes
    ```

2. In the Side Bar, click `daily.csv`, `Ctrl+C`, `Ctrl+V` (macOS `Cmd`),
   and rename the copy: `F2` (macOS `Enter`).

    ```text
    repeats.csv
    ```

3. Open it, click into its text and double it seven times: `Ctrl+A`,
   `Ctrl+C`, `Ctrl+V`, `Ctrl+V` (macOS `Cmd`), seven times over. Save. The
   Status Bar shows where the cursor is.

    ```text
    Ln 1281, Col 1
    ```

    1 280 lines, the ten of `daily.csv` 128 times: 148 × 128 = 18 944 bytes.

4. Pack `repeats.csv` alone: right-click it > **Reveal in Finder** (Windows
   **Reveal in File Explorer**), right-click > **Compress "repeats.csv"**
   (Windows **Compress to ZIP file**). `repeats.csv.zip` (Windows
   `repeats.zip`) has a few hundred bytes: the ten lines are stored once,
   the rest as "the same again". Real data repeats less: the station's full
   log, 2 515 215 bytes, packs to about 22 %.

**Check:** `repeats.csv`, 18 944 bytes, packs into a few hundred.

---

### 12. A checksum by hand { #checksum }

<!-- 1:45 · 10 min -->

A checksum is a number computed from every byte; a changed byte changes it.

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

### 13. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->

Today's tools, all in VS Code and the file manager; Seminar 4 does the same by command in the terminal.

1. Go through the table with the room, one tool per row.

    | To | Do |
    |--|--|
    | see the bytes of a file | right-click > **Open With...** > **Hex Editor** |
    | find a text in the bytes | `Ctrl+F` (macOS `Cmd+F`) in the Hex Editor |
    | find the size in bytes | **Get Info** (`Cmd+I`), **Properties** |
    | change the line ends | `LF` / `CRLF` in the Status Bar |
    | read by another table | Status Bar encoding > **Reopen with Encoding** |
    | write by another table | **Save with Encoding**, only on purpose |
    | pack into a zip | **Compress** (Windows **Compress to ZIP file**) |

---

## Optional, if the room goes fast { #optional }

---

### 14. A spreadsheet saves the table { #spreadsheet }

<!-- — · 10 min -->

An `.xlsx` file is a ZIP of text files.

1. In Finder or File Explorer, open `weather-s03/daily.csv` in Excel or
   Numbers (right-click > **Open With**). Change nothing.
2. Excel: **File** > **Save As...** > **Excel Workbook (.xlsx)**; Numbers:
   **File** > **Export To** > **Excel...**. Save it into `weather-s03`.
3. Open the `.xlsx` with the Hex Editor: it starts with `50 4B`, `PK`.

**Check:** the same first bytes as `weather-s03.zip`.

---

### 15. `note.txt` by the wrong table { #readme-1257 }

<!-- — · 5 min -->

Mojibake: UTF-8 bytes read by the wrong table.

1. Open `note.txt`, saved as UTF-8 (the Status Bar says `UTF-8`). Status
   Bar `UTF-8` > **Reopen with Encoding** > **Baltic (Windows 1257)**.

    ```text
    Å ilutÄ—: 6.3 Ā°C
    ```

    Each two-byte letter reads as two: `C5 A0` is `Å` and a space that does
    not break, `C4 97` is `Ä—`, `C2 B0` is `Ā°`.

2. **Reopen with Encoding** > **UTF-8**. Nothing was saved.

**Check:** `Šilutė: 6.3 °C` again.

---

### 16. Advanced tasks { #advanced }

<!-- — · 20 min -->

Harder questions about the bytes of `daily.csv` and `note.txt`, with the Data Inspector of the Hex Editor.

!!! question "Task: four bytes read as one number"
    In the Hex Editor of `daily.csv`, click the first byte, `64`. The Data
    Inspector also reads the four bytes from there, `64 61 74 65`
    (`date`), as one number: `uint32` and `float32`. What does it show,
    and why is the number so large?

??? success "Answer"
    ```text
    uint32   1702125924
    float32  7.212837e+22
    ```

    With **Little Endian** ticked (the default) the first byte is the
    smallest: `0x65746164` = 6 × 16⁷ + 5 × 16⁶ + … = 1 702 125 924. The same
    four bytes are the text `date`, a whole number or a float: the bytes
    carry no type, the program that reads them chooses one.

!!! question "Task: UTF-16, two bytes for every letter"
    Save `note.txt`, `Šilutė: 6.3 °C`, with **UTF-16 LE**. Predict its size first.
    What do its first four bytes say? Save it as **UTF-8** again
    afterwards.

??? success "Answer"
    ```text
    00000000  FF FE 60 01 69 00 6C 00 75 00 74 00 17 01 3A 00  ..`.i.l.u.t...:.
    ```

    32 bytes: `FF FE`, the byte-order mark of UTF-16 LE, then two bytes for
    each of the 15 characters, the smaller byte first: `Š` is `60 01`
    (U+0160), `i` is `69 00`. ASCII text doubles in size; UTF-8 kept it at
    one byte per letter.

---

## Aims practised

- 📁 **Files:** a file is a row of bytes, measured to the byte; its first
  bytes say what it is, its name does not.
- 🔧 **Tool-agnostic:** UTF-8 and LF give the same bytes on every system; a
  setting that differs is read in the Status Bar.
- ♻️ **Reproducibility:** a sum of the bytes tells two copies apart, the
  start of the checksums of Seminar 4.
