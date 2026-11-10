# Seminar 3 · Computers

**Paired lecture:** 03 How Computers Work · **Format:** a showcase, then a problem, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** How many bytes does a year of the hourly temperature of Vilnius take as a CSV file, and how many as numbers of four bytes?

Part 1 opens a file as bytes for the first time, one small step at a time;
the lecturer runs Part 2 from this page; in Part 3 the room works in pairs.
Everything happens in VS Code with its **Hex Editor**, a web browser and the
file manager: no terminal today (Seminar 4 sets it up). In the blocks stands
what the Hex Editor or the text editor shows, or the text to type.

**If time runs short:** leave out section 7 (the zip); the first bytes of a ZIP file are on the card.

??? info "Before the session"
    - **Room:** internet, for the extension and the files. The session
      needs nothing from any other seminar.
    - **No file is handed out.** Two short files are typed from this page;
      the others are saved from their public addresses with the browser:
        - the names of Lithuania's weather stations: the Meteo LT API of the
          Lithuanian Hydrometeorological Service (LHMT), CC BY-SA 4.0, the
          service to be named as the source (6 kB);
        - NOAA's graph of the monthly CO₂ at Mauna Loa, a PNG picture: NOAA
          Global Monitoring Laboratory, free to use, credit asked (80 kB);
        - the hourly temperature of Vilnius: Open-Meteo's historical weather
          API, CC BY 4.0, "Weather data by Open-Meteo.com" (7 kB a
          fortnight).
    - **Open-Meteo's free service** allows one internet address 10 000
      calls a day, and a classroom shares one address. A fortnight of one
      quantity counts as one call; the whole year in Part 4, once, as
      about three.
    - **The numbers** on this page come from runs on 10 November 2026. NOAA
      draws its graph again every month, so the size of the PNG changes;
      its first 32 bytes do not.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode).
    - **Keys** are written for Windows, macOS in brackets. Bytes are written
      as two hex digits, as the Hex Editor shows them.

---

## Part 1 · A file as bytes { #part-1 }

<!-- 0:00 to 0:25: the room's first look at bytes, so longer than the 15 minutes of a later Part 1 -->

A file is a row of bytes; the Hex Editor shows each one as two hex digits.

### 1. Install the Hex Editor, make the folder { #hex-editor }

<!-- 0:00 · 6 min -->

An extension adds a tool to VS Code; this one shows the bytes of a file.

1. Open the Extensions view: `Ctrl+Shift+X` (macOS `Cmd+Shift+X`).
2. Search:

    ```text
    hex editor
    ```

3. Take **Hex Editor** by **Microsoft** (the publisher under the name),
   click **Install**.
4. **File** > **Open Folder...**, go to your home folder (the one with your
   user name), click **New Folder** in the dialog and type the name.

    ```text
    weather-s03
    ```

5. Select `weather-s03`, click **Open** (Windows **Select Folder**), and
   answer **Yes, I trust the authors**.

**Check:** `WEATHER-S03` at the top of the Side Bar, and **Hex Editor** listed as installed.

---

### 2. Type `daily.csv`, open it as bytes { #bytes }

<!-- 0:06 · 10 min -->

`daily.csv` holds a station's daily mean temperature, 1 to 9 October 2025: a header and nine rows.

1. Move the mouse over the Side Bar, click the **New File** icon and type
   the name.

    ```text
    daily.csv
    ```

2. Copy the block with the button at its top right, paste it into
   `daily.csv`, then press `Enter` once: the cursor stands on line 11,
   which stays empty.

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

3. Set the line end and save. If the Status Bar, bottom right, reads
   `CRLF` (the Windows default), click it and choose `LF`. Then `Ctrl+S`
   (macOS `Cmd+S`): the dot on the tab goes.
4. In the Side Bar, right-click `daily.csv` > **Open With...** > **Hex
   Editor**. Three columns: the **offset** (the number of the row's first
   byte, in hex), 16 bytes, the same bytes as text.

    ```text
    00000000  64 61 74 65 2C 74 65 6D 70 5F 63 0A 32 30 32 35  date,temp_c.2025
    00000010  2D 31 30 2D 30 31 2C 36 2E 33 0A 32 30 32 35 2D  -10-01,6.3.2025-
    ```

5. Click the first byte, `64`. The **Data Inspector** beside the bytes
   shows it as binary, `01100100`, and as a number, `100`:
   6 × 16 + 4 = 100, the letter `d` in the ASCII table. The first five
   bytes, `64 61 74 65 2C`, are `d a t e ,`.

**Check:** everyone finds `2C`, the comma, after `date`.

---

### 3. Count the 148 bytes; a copy with CRLF { #count }

<!-- 0:16 · 9 min -->

The ten bytes nobody sees in the text are the line ends.

1. Read the whole file, ten rows in the Hex Editor. The text column shows
   `.` for `0A`, a byte with no letter.

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

2. The last byte is at offset `93` (row `00000090`, column `03`):
   0x93 = 9 × 16 + 3 = 147, counted from 0, so **148 bytes**. By lines:
   the header and its `0A` are 12 bytes, a row such as `2025-10-01,6.3`
   and its `0A` 15.

    ```text
    12 + 8 × 15 + 16 = 148
    ```

3. A copy with Windows line ends. In the Side Bar, click `daily.csv`,
   `Ctrl+C`, `Ctrl+V` (macOS `Cmd`); rename the copy with `F2` (macOS
   `Enter`) to `daily_crlf.csv`. Open it, click `LF` in the Status Bar,
   choose `CRLF`, save. Open it with the Hex Editor:

    ```text
    00000000  64 61 74 65 2C 74 65 6D 70 5F 63 0D 0A 32 30 32  date,temp_c..202
    00000010  35 2D 31 30 2D 30 31 2C 36 2E 33 0D 0A 32 30 32  5-10-01,6.3..202
    ```

    Every line ends in `0D 0A`. The last byte is at `9D` = 157: **158
    bytes**, ten more. In the text editor both files look the same.

**Check:** 148 and 158; everyone can say which row of `daily.csv` has 16 bytes, and why.

---

## Part 2 · Showcase { #part-2 }

The lecturer opens real files as bytes; the room watches or does the same.
A file with an address above it: right-click the link > **Save Link As...**
(Safari: **Download Linked File As...**), go to `weather-s03`, type the
name given, **Save**.

### 4. One line with Lithuanian letters, in UTF-8 and in Windows 1257 { #encoding }

<!-- 0:25 · 10 min -->

An encoding is the table from characters to bytes. The same text in another table is other bytes, and bytes read by the wrong table come out garbled.

1. Make `note.txt` (Side Bar, **New File**), paste the line, press `Enter`
   once, set `LF` and save. It is the reading of the Šiauliai station at
   00:00 UTC on 1 October 2025.

    ```text
    Šiaulių AMS: 6 °C
    ```

2. Open it with the Hex Editor.

    ```text
    00000000  C5 A0 69 61 75 6C 69 C5 B3 20 41 4D 53 3A 20 36  ..iauli.. AMS: 6
    00000010  20 C2 B0 43 0A                                    ..C.
    ```

    18 characters with the line end, 21 bytes: in UTF-8 `Š` is `C5 A0`,
    `ų` is `C5 B3`, `°` is `C2 B0`.

3. Write the same text by another table. In the text tab of `note.txt`,
   click `UTF-8` in the Status Bar > **Save with Encoding** > **Baltic
   (Windows 1257)**. Close the Hex Editor tab and open it again.

    ```text
    00000000  D0 69 61 75 6C 69 F8 20 41 4D 53 3A 20 36 20 B0  .iauli. AMS: 6 .
    00000010  43 0A                                            C.
    ```

    18 bytes, one per character: `Š` is `D0`, `ų` is `F8`, `°` is `B0`.

4. The mistake: read these bytes by the UTF-8 table. Status Bar
   `Windows 1257` > **Reopen with Encoding** > **UTF-8**.

    ```text
    �iauli� AMS: 6 �C
    ```

    `D0`, `F8` and `B0` are not UTF-8 on their own: `�` marks each.

5. The fix: **Reopen with Encoding** > **Baltic (Windows 1257)**:
   `Šiaulių AMS: 6 °C` is back. Then **Save with Encoding** > **UTF-8**:
   21 bytes again.

**Notice:** **Reopen with Encoding** changes only what is shown; **Save with Encoding** changes the bytes.

**Ask the room:** how many bytes does `daily.csv` have when saved with Windows 1257?

??? note "Answer"
    148, the same. Every character of `daily.csv` is ASCII, and the 128
    ASCII characters have the same byte in UTF-8 and in Windows 1257. Only
    characters such as `Š` or `°` differ.

---

### 5. The station list of the Lithuanian weather service: `Š` as six ASCII bytes { #json-escape }

<!-- 0:35 · 7 min -->

JSON may write a character outside ASCII as `\u` and the four hex digits of its code point: six bytes that read the same by every table.

1. Save [the list of the service's stations](https://api.meteo.lt/v1/stations) as:

    ```text
    stations.json
    ```

2. Click it: one line with the 52 stations. Find (`Ctrl+F`, macOS
   `Cmd+F`) `iauli`:

    ```text
    {"code":"siauliu-ams","name":"\u0160iauli\u0173 AMS",
    ```

3. Open it with the Hex Editor, `Ctrl+F` (macOS `Cmd+F`) with the text
   option, type `\u0160`. Find stops at offset `1056` (row `00001050`,
   column `06`).

    ```text
    00001050  61 6D 65 22 3A 22 5C 75 30 31 36 30 69 61 75 6C  ame":"\u0160iaul
    00001060  69 5C 75 30 31 37 33 20 41 4D 53 22 2C 22 63 6F  i\u0173 AMS","co
    ```

    `Š`, code point U+0160, is `5C 75 30 31 36 30` here: six bytes,
    against `C5 A0` in UTF-8 and `D0` in Windows 1257.

4. Search the bytes for `C5` with the hex option: no results. The file,
   5 683 bytes, is plain ASCII; it holds 60 such escapes, and with the
   letters in UTF-8 it would be 60 × 4 = 240 bytes shorter, 5 443.

**Notice:** a file of ASCII bytes reads the same by any table, so no letter in it can be garbled; each letter outside ASCII costs four bytes more than in UTF-8.

**Ask the room:** a program reads `stations.json` and prints `Šiaulių AMS`. Where do the bytes of `Š` come from?

??? note "Answer"
    From the program, not from the file. The JSON reader turns `\u0160`
    into the character U+0160; whatever prints or saves it then writes it
    in its own encoding, `C5 A0` in UTF-8. The file never held those bytes.

---

### 6. A picture: the first bytes say PNG, the next eight its size { #magic }

<!-- 0:42 · 10 min -->

A file's first bytes, its magic number, say what it is. A PNG then gives its width and height as two numbers of four bytes, the largest byte first.

1. Save [NOAA's graph of CO₂ at Mauna Loa](https://gml.noaa.gov/webdata/ccgg/trends/co2_data_mlo.png) as:

    ```text
    co2_data_mlo.png
    ```

    Click it: VS Code shows the picture.

2. Right-click it > **Open With...** > **Hex Editor**.

    ```text
    00000000  89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52  .PNG........IHDR
    00000010  00 00 03 20 00 00 02 58 08 06 00 00 00 9A 76 82  ... ...X......v.
    ```

    `89 50 4E 47`, `.PNG`, starts every PNG file. `49 48 44 52`, `IHDR`,
    starts the picture's header: the width at offset `10`, the height at
    `14`.

3. The mistake: click the `00` at offset `10`. The Data Inspector reads
   four bytes from there as `uint32`. With **Little Endian** ticked (the
   default), the last of the four counts as the largest:

    ```text
    537067520
    ```

4. The fix: untick **Little Endian**.

    ```text
    800
    ```

    0x320 = 3 × 256 + 2 × 16 = 800. Offset `14` gives `600`: the picture
    is 800 × 600 pixels.

5. Its size, by **Get Info** (`Cmd+I`; Windows right-click >
   **Properties**): 80 184 bytes. 800 × 600 pixels of 4 bytes each (red,
   green, blue, opacity; the `06` at offset `19`) would be 1 920 000:
   the PNG packs them without losing any. Your size may differ: NOAA draws
   the graph again every month.

**Notice:** a number of several bytes needs its byte order; PNG writes the largest byte first, in the order a hex number is read.

**Ask the room:** rename a copy of the picture to `co2_data_mlo.txt`. What are its first bytes, and what does VS Code show when it opens the copy as text?

??? note "Answer"
    The same `89 50 4E 47`: a new name changes no byte. As text VS Code
    says the file is binary, or shows garbled characters: the `.txt`
    ending is a hint for people and programs, and here a wrong one.

---

### 7. Zip the station list and the picture: the list shrinks to a quarter { #zip }

<!-- 0:52 · 7 min -->

Lossless compression stores a repeat once and points back to it; bytes that are already packed have few repeats left.

1. Right-click `stations.json` > **Reveal in Finder** (Windows **Reveal in
   File Explorer**). Pack each file on its own: macOS right-click >
   **Compress "stations.json"**; Windows right-click > **Compress to ZIP
   file** (Windows 10: **Send to** > **Compressed (zipped) folder**). The
   same for `co2_data_mlo.png`.
2. Read the four sizes (**Get Info**, **Properties**).

    ```text
    stations.json        5 683 bytes    zipped    1 397
    co2_data_mlo.png    80 184 bytes    zipped   75 772
    ```

    The zip sizes are those of `zip` on Linux; Finder and File Explorer
    store the name, the dates and other details their own way, so their
    numbers differ a little.

3. In VS Code, **File** > **Open File...** (macOS **Open...**), the zip of
   `stations.json`, **Open Anyway**, **Hex Editor**: the first bytes are
   `50 4B 03 04`, `PK`, the start of every ZIP file.

**Notice:** the station list repeats `"code":`, `"name":` and `"coordinates":` 52 times and shrinks to a quarter; the PNG is packed already and loses 5 %.

**Ask the room:** zip the zip of `stations.json` again. Does it shrink further?

??? note "Answer"
    No, it grows: 1 397 bytes become 1 529. The packed bytes have no
    repeats left, and the new zip adds its own header and the name of the
    file inside it, twice.

---

### 8. Tool card { #card }

<!-- 0:59 · 2 min -->

What the examples and Part 3 use, in VS Code and the file manager.

| To | Do |
|--|--|
| see the bytes of a file | right-click > **Open With...** > **Hex Editor** |
| read one byte as a number | click it: the Data Inspector (binary, `uint8`) |
| read four bytes as one number | the Data Inspector's `uint32`; **Little Endian** sets the byte order |
| find a text or bytes in a file | `Ctrl+F` (macOS `Cmd+F`) in the Hex Editor; text or hex option |
| the size in bytes | **Get Info** (`Cmd+I`), **Properties**; or the last offset + 1 |
| change the line ends | `LF` / `CRLF` in the Status Bar |
| read by another table | Status Bar encoding > **Reopen with Encoding** |
| write by another table | Status Bar encoding > **Save with Encoding**, only on purpose |
| pack into a zip | **Compress** (Windows **Compress to ZIP file**) |
| save a file from a link | right-click > **Save Link As...** (Safari **Download Linked File As...**) |

| Kind of file | First bytes |
|--|--|
| text, CSV, JSON, Markdown | none: the text itself |
| UTF-8 with a byte-order mark | `EF BB BF` |
| PNG picture | `89 50 4E 47`, `.PNG` |
| ZIP, and `.docx`, `.xlsx` | `50 4B 03 04`, `PK` |
| PDF | `25 50 44 46`, `%PDF` |

---

## Part 3 · The problem { #part-3 }

### 9. How many bytes is a year of Vilnius's hourly temperature as CSV? { #problem }

<!-- 1:01 · 45 min -->

Open-Meteo's historical weather API gives the hourly temperature of
Vilnius as a CSV file (Open-Meteo, CC BY 4.0, "Weather data by
Open-Meteo.com"). This address asks for 1 to 14 January 2025:

```text
https://archive-api.open-meteo.com/v1/archive?latitude=54.69&longitude=25.28&start_date=2025-01-01&end_date=2025-01-14&hourly=temperature_2m&format=csv
```

Each pair takes another fortnight of 2025 (the lecturer gives each pair a
month): copy the address into the browser's address bar, change the two
dates to 14 days of that month, `Enter`. The browser saves
`open-meteo-54.73N25.26E95m.csv` in **Downloads**; drag it onto the Side
Bar of VS Code. Its first lines:

```text
latitude,longitude,elevation,utc_offset_seconds,timezone,timezone_abbreviation
54.727592,25.256916,95.0,0,GMT,GMT

time,temperature_2m (°C)
2025-01-01T00:00,2.9
2025-01-01T01:00,2.5
```

Work in pairs, with any tools, an LLM too: the work is the reasoning and the checks.

1. **Predict**, before downloading. The size in bytes of the whole year
   2025 in this form, and one reason.
2. **Solve.** From your fortnight: the bytes of the four lines on top, the
   bytes per row, and the size of the year with its uncertainty; then the
   size of the same temperatures as `float32` numbers.
3. **Check the machine's work.**
    - Count the bytes of one row by hand in the Hex Editor, from its first
      `32` to its `0A`.
    - Count the characters of line 4, `time,temperature_2m (°C)`, and its
      bytes in the Hex Editor; find `C2 B0`.
    - Work out the hours of 2025 from its days.
    - Set the answer against your prediction; where they differ, say which
      was wrong, and why.
4. **Hand in.** The size of the year as a number with its uncertainty, the
   size as `float32`, and two sentences in your own words: where the bytes
   of a row go, and why your fortnight may give too much or too little.

??? tip "Hint 1: the fortnight's bytes"
    The size: **Get Info** or **Properties**, or the last offset of the
    Hex Editor plus one. Take away the four lines on top; the rest is 336
    rows (14 × 24).

??? tip "Hint 2: why rows differ"
    `2025-01-01T00:00,` is 17 bytes in every row and the line end is one;
    the temperature takes 3 bytes (`2.9`), 4 (`-1.2`, `18.9`) or 5
    (`-10.3`). The shortest and the longest row give the range.

??? tip "Hint 3: the float32 size"
    A `float32` holds any of these temperatures in 4 bytes. The times need
    no bytes when the first hour and the step of one hour are written down
    once.

??? note "One solution"
    1 to 14 January 2025: **Get Info** gives 7 395 bytes. The four lines on
    top end at offset `8C`:

    ```text
    00000080  75 72 65 5F 32 6D 20 28 C2 B0 43 29 0A 32 30 32  ure_2m (..C).202
    00000090  35 2D 30 31 2D 30 31 54 30 30 3A 30 30 2C 32 2E  5-01-01T00:00,2.
    000000A0  39 0A 32 30 32 35 2D 30 31 2D 30 31 54 30 31 3A  9.2025-01-01T01:
    ```

    The first row runs from `8D` to `A1`: 21 bytes. Line 4 has 24
    characters and 26 bytes: `°` is the two bytes `C2 B0`, and the line
    end one more. The arithmetic:

    ```text
    four lines on top     79 + 35 + 1 + 26   =    141 bytes
    336 rows              7 395 − 141        =  7 254 bytes, 21.59 a row
                          (138 rows of 21 bytes, 198 of 22: a minus sign)
    2025: 365 × 24        =  8 760 hours
    the year              141 + 8 760 × 21.59  ≈  189 263 bytes
    all rows 21 or 22     184 101  to  192 861 bytes
    as float32            8 760 × 4          = 35 040 bytes
    ```

    The year 2025 in this form, fetched once in Part 4: **189 172 bytes**,
    91 bytes from the prediction. It has 31 rows of 23 bytes, at −10.0 °C
    and colder, which this fortnight did not have.

    A row of this file is 17 bytes of time and comma, one byte for each
    character of the temperature and one line end, 21.6 bytes on average;
    the year 2025 takes 189 172 bytes, 5.4 times the 35 040 of the same
    temperatures as `float32`. A January fortnight gives the year to
    0.05 % because its minus signs make its rows as long as the year's on
    average; a fortnight of May, with one-digit temperatures, gives 1.4 %
    too little.

**With your own project data:** a text file of your own: predict its size
from its first lines and the number of its rows, check it to the byte, and
work out how many bytes its numbers would take as `float32`.

---

## Part 4 · Show and discuss { #part-4 }

### 10. Three questions about the pairs' numbers { #discuss }

<!-- 1:46 · 14 min -->

Two or three pairs show their number and read their two sentences. The lecturer then saves [the whole year 2025](https://archive-api.open-meteo.com/v1/archive?latitude=54.69&longitude=25.28&start_date=2025-01-01&end_date=2025-12-31&hourly=temperature_2m&format=csv) once and reads its size: 189 172 bytes.

**Ask the room:** fortnights from 1 January, 1 May and 1 July give 189 263, 186 447 and 192 783 bytes for the year. Why is May low and July high?

??? note "Answer"
    May's temperatures are mostly one digit above zero, `9.4`: 3 bytes,
    and 246 of its 336 rows have 21 bytes. July's are mostly two digits,
    `18.9`: 4 bytes, rows of 22. January has the minus sign, `-1.2`: also
    4. A fortnight is a sample of the year; how it was chosen sets how far
    off it lands (−1.4 %, +1.9 %, +0.05 %).

**Ask the room:** how many bytes does the year take saved with Windows line ends?

??? note "Answer"
    189 172 + 8 764 = 197 936: one `0D` more on each of the 8 764 lines,
    the four on top included.

**Ask the room:** as `float32` the year takes 35 040 bytes, 5.4 times fewer. Why do weather services still send text?

??? note "Answer"
    Text is read by any program on any system, and the reader sees what
    each value is: the header names the column and its unit. Four bytes of
    a `float32` are only a number once the reader knows the type, the byte
    order and which hour each value belongs to, all written somewhere else.

The size of a text file is its characters counted in bytes: one for each ASCII character and line end, two for `°` or `Š` in UTF-8. A number as text takes one byte for each digit, sign and point; as `float32`, always four.

---

## Optional, if the room is fast { #optional }

### 11. The same fortnight as JSON: predict its size { #json }

<!-- — · 10 min -->

Without `&format=csv` at its end, the address of section 9 answers in JSON.

1. **Predict** the size of 1 to 14 January 2025 as JSON from the CSV's
   7 395 bytes: what does JSON add for each hour, and what does it leave
   out? Its start:

    ```text
    {"latitude":54.727592,"longitude":25.256916,"generationtime_ms":0.33485889434814453,"utc_offset_seconds":0,"timezone":"GMT","timezone_abbreviation":"GMT","elevation":95.0,"hourly_units":{"time":"iso8601","temperature_2m":"°C"},"hourly":{"time":["2025-01-01T00:00","2025-01-01T01:00",
    ```

2. Save [the fortnight as JSON](https://archive-api.open-meteo.com/v1/archive?latitude=54.69&longitude=25.28&start_date=2025-01-01&end_date=2025-01-14&hourly=temperature_2m)
   and read its size.

??? note "Answer"
    8 193 bytes, give or take a byte or two: `generationtime_ms`, the time
    the server took, has a different number of digits on each request.
    JSON writes the times in one list and the temperatures in another;
    each hour costs two bytes more than in the CSV: the two quote marks
    around the time, while the line end becomes a comma. The last entry of
    each list has no comma, and the part before the lists is 269 bytes
    against the CSV's 141 on top.

    ```text
    7 395 − 141 + 336 × 2 − 2 + 269 = 8 193
    ```

---

### 12. A checksum by hand { #checksum }

<!-- — · 10 min -->

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

## Aims practised

- 📁 **Files:** a file is a row of bytes, measured to the byte; its first
  bytes say what it is, its name does not.
- 🔧 **Tool-agnosticism:** UTF-8 and LF give the same bytes on every
  system; a text file is read by any program, a binary one only with its
  rule.
- ♻️ **Reproducibility:** a size predicted from the format and checked to
  the byte; the source, the licence and the date of every file named.
