# Seminar 1 · Data

**Paired lecture:** 02 Introduction to Data · **Format:** a showcase, then a problem, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** How many days are missing from the daily record of the Vilnius weather station, 1881 to 2025, and in which years?

Part 1 is the room's first VS Code and Markdown, one small step at a time;
the lecturer runs Part 2 from this page; in Part 3 the room works in pairs.
Everything happens in VS Code and a web browser: no terminal today. In the
blocks stands the text to type, or what appears on the screen.

**If time runs short:** leave out section 9 (the CO₂ file); Part 3 asks the same of another file.

??? info "Before the session"
    - **Room:** internet, and laptops on which students can install programs.
    - **No file is handed out.** One short file is typed from this page; the
      others are saved from their public addresses with the browser:
        - a week of the hourly weather of Vilnius from a weather model:
          Open-Meteo's historical weather API, CC BY 4.0, "Weather data by
          Open-Meteo.com" (4 kB);
        - a day of hourly observations at the Vilnius station: the Meteo LT
          API of the Lithuanian Hydrometeorological Service (LHMT),
          CC BY-SA 4.0, the service to be named as the source (7 kB);
        - the monthly CO₂ at Mauna Loa: NOAA Global Monitoring Laboratory,
          free to use, credit asked (39 kB);
        - the daily record of the Vilnius station since 1881: NOAA National
          Centers for Environmental Information (NCEI), GHCN-Daily, free to
          use, citation asked (6.1 MB).
    - **The numbers** on this page come from runs on 10 November 2026. The
      CO₂ file gains a month every month; GHCN-Daily is processed again
      every day, so a count or a flag in it can change.
    - **Keys** are written for Windows, macOS in brackets.

---

## Part 1 · VS Code and the README { #part-1 }

<!-- 0:00 to 0:34: the room's first VS Code, so longer than the 15 minutes of a later Part 1 -->

VS Code, a folder for the project, and its first file: the README.

### 1. Install VS Code { #install }

<!-- 0:00 · 8 min -->

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

<!-- 0:08 · 4 min -->

VS Code works on a folder: one project, one folder.

1. **File** > **Open Folder...**, go to your home folder (the one with your
   user name), click **New Folder** in the dialog and type the name.

    ```text
    weather-s01
    ```

2. Select `weather-s01`, click **Open** (Windows **Select Folder**), and
   answer **Yes, I trust the authors**.

**Check:** `WEATHER-S01` at the top of the Side Bar, nothing under it.

---

### 3. Name the five regions, try three keys { #interface }

<!-- 0:12 · 5 min -->

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

### 4. Make the four folders and the README { #folders }

<!-- 0:17 · 5 min -->

Files as they arrived are kept apart from everything made from them.

1. Move the mouse over the Side Bar; click the **New Folder** icon. Type:

    ```text
    data/raw
    ```

    The `/` makes both folders at once.

2. Three more folders, one at a time: click the empty area under the
   folders, then the **New Folder** icon, and type the name.

    ```text
    data/processed
    scripts
    results
    ```

3. Click the empty area, then the **New File** icon. Type the name; the
   Explorer then shows the whole tree.

    ```text
    README.md
    ```

    ```text
    WEATHER-S01
      data
        processed
        raw
      results
      scripts
      README.md
    ```

**Check:** `data` holds `processed` and `raw`; `results`, `scripts` and
`README.md` stand beside `data`.

!!! warning "A new folder lands inside the selected folder"
    Drag it onto the empty area of the Side Bar.

---

### 5. Markdown and its preview { #markdown }

<!-- 0:22 · 8 min -->

Markdown is plain text with a few signs for structure; `README.md` is the first file anyone opens.

1. In `README.md`, type:

    ```text
    # Weather of Vilnius

    Open data about the weather of Vilnius, saved from public services, and
    what each file says.
    ```

2. A dot on the tab means *not saved*. Save with `Ctrl+S` (macOS `Cmd+S`):
   the dot goes. Then switch on **File** > **Auto Save**: from now on every
   change is saved.
3. Open the preview beside the text: `Ctrl+K`, release, then `V` (macOS
   `Cmd+K`, then `V`).
4. Under the paragraph, add a section with a table. Without the second
   line, `|--|--|`, the preview shows text with `|` signs, not a table.

    ```text
    ## Folders

    | Folder | What goes in |
    |--|--|
    | `data/raw` | files as they arrived, never edited |
    | `data/processed` | files made from `data/raw` |
    | `scripts` | programs |
    | `results` | numbers and figures the programs produce |
    ```

    | You type | The preview shows |
    |--|--|
    | `# Title` | the title of the page |
    | `## Section` | a section heading |
    | `**text**` | **bold** |
    | `- item` | a list item |
    | `` `name` `` | a file name in code type |
    | `| a | b |` | a row of a table |

**Check:** the preview shows a large title, a paragraph, a smaller heading and a table of four rows.

---

### 6. Three mistakes, on purpose { #mistakes }

<!-- 0:30 · 4 min -->

The preview is the test. Make each mistake, read the preview, undo with `Ctrl+Z` (macOS `Cmd+Z`).

1. Delete the space after `#` in the title.

    ```text
    #Weather of Vilnius
    ```

    The preview shows `#Weather of Vilnius` as plain text.

2. Put an empty line inside the paragraph, after `saved`. The preview shows
   two paragraphs: only an empty line starts a new one.
3. Write a bold word with a space before the closing stars.

    ```text
    **Vilnius **
    ```

    The preview shows the stars.

**Check:** after the undos the preview shows the title, one paragraph and the Folders table again.

---

## Part 2 · Showcase { #part-2 }

The lecturer opens four files in VS Code, three saved from public services
and one typed; the room watches or does the same. A file with an address:
right-click the link > **Save Link As...** (Safari: **Download Linked File
As...**), go to `weather-s01` > `data` > `raw`, type the name given,
**Save**.

### 7. A week of Vilnius from a weather model: the header names the units { #model-csv }

<!-- 0:34 · 8 min -->

A CSV file is a table as text: one line per row, a comma between the values, the column names on a header line.

1. Save [the hourly weather of Vilnius, 1 to 7 October 2025](https://archive-api.open-meteo.com/v1/archive?latitude=54.69&longitude=25.28&start_date=2025-10-01&end_date=2025-10-07&hourly=temperature_2m,relative_humidity_2m&format=csv)
   as:

    ```text
    vilnius_week.csv
    ```

2. Click it in the Side Bar. Lines 1 and 2 say where the values are; line 3
   is empty; line 4 names the columns.

    ```text
    latitude,longitude,elevation,utc_offset_seconds,timezone,timezone_abbreviation
    54.727592,25.256916,95.0,0,GMT,GMT

    time,temperature_2m (°C),relative_humidity_2m (%)
    2025-10-01T00:00,5.5,86
    2025-10-01T01:00,4.8,87
    2025-10-01T02:00,4.0,90
    2025-10-01T03:00,3.1,94
    ```

3. Jump to the end: `Ctrl+End` (macOS `Cmd+↓`). The Status Bar:

    ```text
    Ln 173, Col 1
    ```

    Line 173 is the empty line after the last line end. 172 lines, minus
    the four lines on top: 168 rows, 7 days × 24 hours.

4. Write down where the file came from: in `README.md`, under the Folders
   table, a **Data** section with today's date.

    ```text
    ## Data

    - `data/raw/vilnius_week.csv`: Vilnius, 1 to 7 October 2025, one row
      per hour: temperature (°C) and relative humidity (%) from a weather
      model. Source: Open-Meteo, CC BY 4.0, "Weather data by
      Open-Meteo.com". Fetched 2026-11-10.
    ```

**Notice:** the units stand in the header, `(°C)` and `(%)`; the place on line 2, 54.73° N 25.26° E, is not the 54.69, 25.28 of the address but the point of the model's grid that the values belong to.

**Ask the room:** is 5.5 °C, the first row, a measurement?

??? note "Answer"
    No. Open-Meteo's archive is a reanalysis: a weather model run over the
    past and fed with the observations of many stations. The row is the
    model's value for that hour at its grid point: derived, not measured.
    The README says so.

---

### 8. One day at the Vilnius station, as JSON: measured, with the units in the documentation { #station-json }

<!-- 0:42 · 8 min -->

JSON writes data as names and values: `{ }` holds one record, `[ ]` a list of records.

1. Save [the observations of the Vilnius station on 1 October 2025](https://api.meteo.lt/v1/stations/vilniaus-ams/observations/2025-10-01)
   as:

    ```text
    vilnius_station.json
    ```

2. Click it. The whole file, 6 508 characters, is one line. Wrap it into
   the window: **View** > **Word Wrap**, `Alt+Z` (macOS `Option+Z`). The
   first hour, broken here at the commas:

    ```text
    {"station":{"code":"vilniaus-ams","name":"Vilniaus AMS",
    "coordinates":{"latitude":54.625992,"longitude":25.107064}},
    "observations":[{"observationTimeUtc":"2025-10-01 00:00:00",
    "airTemperature":6.1,"feelsLikeTemperature":5.1,"windSpeed":1.6,
    "windGust":2.5,"windDirection":41,"cloudCover":100,
    "seaLevelPressure":1034.6,"relativeHumidity":95,"precipitation":0,
    "snowDepth":0,"conditionCode":"cloudy"},
    ```

3. Find a name: `Ctrl+F` (macOS `Cmd+F`), type `airTemperature`. The
   counter: one per hour.

    ```text
    1 of 24
    ```

    `Enter` three times goes to 03:00:

    ```text
    "observationTimeUtc":"2025-10-01 03:00:00","airTemperature":5,
    ```

    The model's file of section 7 has `3.1` at 03:00.

4. Look for a unit in the file: there is none. The service's documentation,
   [api.meteo.lt](https://api.meteo.lt/) (in Lithuanian), lists them:
   `airTemperature` in °C, `windSpeed` in m/s, `seaLevelPressure` in hPa,
   `snowDepth` in cm; a measurement the station did not make is `null`.

**Notice:** the station is at 54.63° N 25.11° E, about 15 km south-west of the model's grid point; its thermometer measured 5.0 °C at 03:00, the model gave 3.1 °C.

**Ask the room:** which file holds the temperature of Vilnius at 03:00 on 1 October 2025?

??? note "Answer"
    Each holds a different quantity. The JSON holds what one thermometer
    measured at the station; the CSV holds what a model computed for a
    point 15 km away. Over the whole day they differ by about half a degree
    (means of 6.38 and 5.90 °C). A README names which one its numbers are,
    and the source.

---

### 9. CO₂ at Mauna Loa: a file whose notes say how it was made { #notes }

<!-- 0:50 · 6 min -->

Some files carry their own notes: lines that start with `#` are read by people, not as rows.

1. Save [NOAA's monthly CO₂ at Mauna Loa](https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv)
   as:

    ```text
    co2_mm_mlo.csv
    ```

2. Click it. Forty lines of notes, then the header on line 41 and the
   first month, March 1958, on line 42:

    ```text
    # Data from March 1958 through April 1974 have been obtained by C. David Keeling
    # of the Scripps Institution of Oceanography (SIO) and were obtained from the
    # Scripps website (scrippsco2.ucsd.edu).
    ...
    # Missing months have been interpolated, for NOAA data indicated by negative stdev
    # and uncertainty. We have no information for SIO data about Ndays, stdv, unc
    # so that they are also indicated by negative numbers
    #
    # NOTE: Due to the eruption of the Mauna Loa Volcano, measurements from Mauna Loa Observatory
    # were suspended as of Nov. 29, 2022 and resumed in July 2023.
    # Observations starting from December 2022 to July 4, 2023 are from a site at the
    # Maunakea Observatories, approximately 21 miles north of the Mauna Loa Observatory.
    #
    year,month,decimal date,average,deseasonalized,ndays,sdev,unc
    1958,3,1958.2027,315.71,314.44,-1,-9.99,-0.99
    ```

3. Count one of the marks: `Ctrl+F`, type `-9.99`.

    ```text
    1 of 196
    ```

4. `Ctrl+End` (macOS `Cmd+↓`): `Ln 865, Col 1`. 865 − 1 − 41 = 823 months,
   March 1958 to September 2026. Your count may be higher: the file gains a
   month every month.

**Notice:** the notes say who measured, how a month is made, how a gap is marked (negative numbers in the last three columns) and where the instrument stood; they do not give the unit of the CO₂.

**Ask the room:** where is the unit, and what does `426.07`, September 2026, mean?

??? note "Answer"
    On NOAA's page of the record,
    [gml.noaa.gov/ccgg/trends/mlo.html](https://gml.noaa.gov/ccgg/trends/mlo.html):
    a dry-air mole fraction in parts per million (ppm). 426.07 ppm is 426
    molecules of CO₂ in every million molecules of dry air. The README
    gets the unit and that page's address.

---

### 10. A spreadsheet export repaired: the decimal comma first { #repair }

<!-- 0:56 · 8 min -->

A spreadsheet set to a Lithuanian or German region writes `6,3` for 6.3 and `;` between values; a plain CSV has `.` and `,`.

1. In the Side Bar, click the empty area, then **New File**, and type the
   path. Paste the eleven lines, press `Enter` after the last, and set
   the line end: if the Status Bar, bottom right, reads `CRLF`, click it
   and pick `LF`.

    ```text
    data/raw/daily_export.csv
    ```

    ```text
    nr;date;temp_c
    1;2025-10-01;6,3
    2;2025-10-02;5,0
    3;2025-10-03;5,6
    4;2025-10-04;7,0
    5;2025-10-05;9,4
    6;2025-10-06;10,4
    7;2025-10-07;9,2
    8;2025-10-08;9,0
    9;2025-10-09;9,8
    ;mean;7,97
    ```

2. Repair a copy, never the raw file: click `daily_export.csv`, `Ctrl+C`,
   click `data/processed`, `Ctrl+V` (macOS `Cmd`); rename the copy with
   `F2` (macOS `Enter`) to `daily.csv` and open it.
3. The mistake first. Open Replace: `Ctrl+H` (macOS `Cmd+Option+F`). Find
   `;`, replace with `,`. The counter, before anything changes:

    ```text
    1 of 22
    ```

    **Replace All** (the button right of the Replace box). Line 2 now has
    four commas, and `6,3` reads as two values:

    ```text
    1,2025-10-01,6,3
    ```

    Undo: `Ctrl+Z` (macOS `Cmd+Z`).

4. The repair, in this order. Click into `;mean;7,97`, delete the line:
   `Ctrl+Shift+K` (macOS `Cmd+Shift+K`). Find `,`, replace with `.`
   (`1 of 9`), **Replace All**. Find `;`, replace with `,` (`1 of 20`),
   **Replace All**, `Esc`.
5. Delete the column `nr` on all ten lines at once: click before `nr`,
   `Shift`+click after the last `9.8`; a cursor at the end of every line,
   `Shift+Alt+I` (macOS `Shift+Option+I`); all to the line start, `Home`
   (macOS `Cmd+←`); select the first word and the comma after it,
   `Ctrl+Shift+→` (macOS `Option+Shift+→`), then `Shift+→`; `Delete`
   (macOS `Backspace`); `Esc`.

    ```text
    date,temp_c
    2025-10-01,6.3
    2025-10-02,5.0
    ```

6. Right-click `daily.csv` > **Reveal in Finder** (Windows **Reveal in File
   Explorer**); **Get Info**, `Cmd+I` (Windows right-click > **Properties**):
   **148 bytes**.

**Notice:** the decimal comma is replaced first, while it is the only comma in the file.

**Ask the room:** Replace All changed twenty characters at once. How do you know it changed nothing else?

??? note "Answer"
    Two numbers checked it. The counter said 20 before the replacement:
    two `;` on each of ten lines. The size says the rest: the export has
    180 bytes; the mean line and its line end are 11, `nr;` and `1;` to
    `9;` are 21, and each replacement swaps one byte for one:
    180 − 11 − 21 = 148.

---

### 11. Key card { #card }

<!-- 1:04 · 1 min -->

The keys of this page.

| To | Windows | macOS |
|--|--|--|
| open the Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| preview Markdown beside the text | `Ctrl+K`, then `V` | `Cmd+K`, then `V` |
| wrap a long line into the window | `Alt+Z` | `Option+Z` |
| go to the end of a file | `Ctrl+End` | `Cmd+↓` |
| go to a line by its number | `Ctrl+G` | `Ctrl+G` |
| find, with a counter of the matches | `Ctrl+F` | `Cmd+F` |
| replace | `Ctrl+H` | `Cmd+Option+F` |
| delete a line | `Ctrl+Shift+K` | `Cmd+Shift+K` |
| a cursor at the end of every selected line | `Shift+Alt+I` | `Shift+Option+I` |
| undo | `Ctrl+Z` | `Cmd+Z` |
| save a file from a link | right-click > **Save Link As...** | Safari: **Download Linked File As...** |
| the size in bytes | **Reveal in File Explorer** > **Properties** | **Reveal in Finder** > **Get Info** |

---

## Part 3 · The problem { #part-3 }

### 12. How complete is the record of the Vilnius station? { #problem }

<!-- 1:05 · 42 min -->

The weather station of Vilnius (station `LH000026730` of GHCN-Daily,
54.63° N 25.10° E, 156 m) has a daily record from 1 January 1881 to
24 August 2025: one row per day, 6.1 MB. It comes from NOAA's National
Centers for Environmental Information (NCEI), free to use; the
[readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt) asks
for the citation Menne et al. (2012), *Global Historical Climatology
Network – Daily (GHCN-Daily), Version 3*, doi:10.7289/V5D21VHZ, with the
date of access, and its section III gives the meaning of every column and
flag. Save [the station's file](https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/LH000026730.csv)
into `data/raw` under its own name, `LH000026730.csv`.

Work in pairs, with any tools, an LLM too: the work is the reasoning and the checks.

1. **Predict**, before opening the file. How many rows should 1 January
   1881 to 24 August 2025 give, about how many days are missing, and in
   which years? One reason.
2. **Solve.** The number of days with no row, and the years they fall in;
   the unit of `TMAX`; how a value that is missing inside a row is
   written.
3. **Check the machine's work.**
    - Count the days from 1 January 1881 to 24 August 2025 by hand: the
      whole years with their leap days, then the days of 2025.
    - Read the number of rows off VS Code: `Ctrl+End`, the Status Bar,
      minus the header and the empty last line.
    - Read five rows of one July day with the unit you found; then find
      the largest `TMAX` and decide whether it can be true.
    - Set the answer against your prediction; where they differ, say which
      was wrong, and why.
4. **Hand in.** The number of missing days with how you found it; a
   **Data** section in `README.md` for this file that says what one row
   is, how many there are, the units, how a gap is marked, and where the
   file came from; two sentences in your own words.

??? tip "Hint 1: rows and lines"
    `Ctrl+End` puts the cursor on the empty line after the last line end.
    Line 1 is the header. The Find box counts the rows of one year: type
    `"1916-` with the quote mark, so that only the date column matches.
    Its counter stops at 19 999, so count year by year.

??? tip "Hint 2: the calendar"
    A year divisible by 4 is a leap year, except 1900 (divisible by 100 but
    not by 400). From 1884 to 2024, 36 years are divisible by 4: 35 leap
    years. 2025 up to 24 August: 31 + 28 + 31 + 30 + 31 + 30 + 31 + 24
    days.

??? tip "Hint 3: the units and the flags"
    On 13 July 2025 `TMAX` reads `"  265"`; a summer afternoon in Vilnius is
    near 26 °C. The field after a value, `TMAX_ATTRIBUTES`, holds three
    flags separated by commas; the second is the quality flag, and the
    readme lists what each letter means.

??? note "One solution"
    The rows: `Ctrl+End`, then the Status Bar.

    ```text
    Ln 51043, Col 1
    ```

    51 043 − 1 (the empty last line) − 1 (the header) = **51 041** rows,
    one per day. The days by hand:

    ```text
    1881 to 2024:  144 × 365 + 35 leap days        = 52 595
    2025 to 24 August:  31+28+31+30+31+30+31+24    =    236
                                                     52 831 days
    52 831 − 51 041 = 1 790 days without a row (3.4 %)
    ```

    The years, each counted with Find (`"1915-` gives `1 of 212`):

    | Year | Rows | Days | Missing |
    |--|--|--|--|
    | 1883 | 59 | 365 | 306 |
    | 1884 | 294 | 366 | 72 |
    | 1890 | 335 | 365 | 30 |
    | 1892 | 335 | 366 | 31 |
    | 1915 | 212 | 365 | 153 |
    | 1916 | 0 | 366 | 366 |
    | 1917 | 0 | 365 | 365 |
    | 1920 | 213 | 366 | 153 |
    | 1941 | 279 | 365 | 86 |
    | 1944 | 152 | 366 | 214 |
    | 2021 | 362 | 365 | 3 |
    | 2024 | 355 | 366 | 11 |

    The longest gap shows on two neighbouring lines (`Ctrl+G`, `12191`):
    31 July 1915 is followed by 1 January 1918.

    ```text
    "LH000026730","1915-07-31","54.6331","25.1","156.0","VILNIUS, LH","    7",",,r",,,"  204",",,E","   95",",,E","  159",",,r"
    "LH000026730","1918-01-01","54.6331","25.1","156.0","VILNIUS, LH","    9",",,r",,,"  -45",",,r","  -68",",,r","  -49",",,r"
    ```

    The unit: `TMAX`, `TMIN` and `TAVG` are in tenths of °C (`"  204"` is
    20.4 °C on 31 July 1915, `"  -68"` is −6.8 °C on 1 January 1918), `PRCP`
    in tenths of mm.
    A value missing inside a row is an empty field, nothing between two
    commas: on 10 July 2025 there is no `TMAX`, and `TMAX` starts only on
    1 January 1900. The largest `TMAX` values carry the quality flag `X`,
    "failed bounds check" (Find `,X,`: `1 of 2`):

    ```text
    "LH000026730","1904-07-10","54.6331","25.1","156.0","VILNIUS, LH","   57",",,r",,," 1680",",X,E","  110",",,E","  146",",,r"
    "LH000026730","1911-08-27","54.6331","25.1","156.0","VILNIUS, LH","   20",",,r",,," 1980",",X,E","  155",",,E","  173",",,r"
    ```

    168.0 and 198.0 °C cannot be air temperatures in Vilnius; the next
    largest, `"  354"` on 13 July 1959, 35.4 °C, carries no flag.

    The README:

    ```text
    - `data/raw/LH000026730.csv`: the daily record of the weather station
      of Vilnius, GHCN-Daily station LH000026730, 1 January 1881 to
      24 August 2025. One row per day: 51 041 rows for 52 831 days; the
      1 790 missing days have no row, most of them in 1883-1884,
      1915-1917, 1920, 1941 and 1944.
    - **Units:** `TMAX`, `TMIN`, `TAVG` in tenths of °C, `PRCP` in tenths
      of mm. A missing value in a row is an empty field. Two `TMAX` values
      failed NOAA's bounds check (flag `X`): 1904-07-10 and 1911-08-27.
    - **Source:** NOAA NCEI, GHCN-Daily; cite Menne et al. (2012),
      doi:10.7289/V5D21VHZ. Fetched 2026-11-10.
    ```

    The record of the Vilnius station lacks 1 790 of its 52 831 days, 3.4 %.
    1 337 of them fall in 1915–1917, 1920, 1941 and 1944, years of war in
    Vilnius; the file leaves such a day out instead of marking it.

**With your own project data:** the same questions of a file of your own:
what one row is, how many rows it should have against how many it has, the
units, how a gap is marked and where it came from, in its README.

---

## Part 4 · Show and discuss { #part-4 }

### 13. Three questions about the pairs' answers { #discuss }

<!-- 1:47 · 13 min -->

Two or three pairs show their README in the preview and read their two sentences.

**Ask the room:** one pair counted 51 043 days, another 51 041. Which is right?

??? note "Answer"
    51 041. `Ln 51043` is the empty line after the last line end, and
    line 1 is the header: two lines that are not days. A line number is
    not a count of rows.

**Ask the room:** an LLM answered that the hottest day of the record was 27 August 1911, at 198.0 °C. What went wrong, and where does the file say so?

??? note "Answer"
    It read the unit right and the value without a check: 198 °C is twice
    the boiling point of water. The file marks the value: the quality flag
    `X` in `TMAX_ATTRIBUTES`, "failed bounds check" in the readme. The
    largest and the smallest value of a column are the first two numbers
    to read with their unit.

**Ask the room:** today's files mark a gap four ways: a number such as `-999`, `null` in the JSON, negative numbers in NOAA's CO₂ file, and in GHCN an empty field or no row at all. Which way is the easiest to get wrong in a mean, and which the easiest to miss?

??? note "Answer"
    A mark that is a number is the easiest to get wrong: counted as a
    value it moves a mean (four evening hours at 27.3, 25.6, 24.6 and
    23.6 °C have the mean 25.275; with two `-999` hours counted, the mean
    of six is −316.15). A day with no row is the easiest to miss: nothing
    in the file shows it, only the rows counted against the calendar.

A file is data only with its rule: what one row is, how many rows there should be, the units, how a gap is marked, where it came from; the README writes each one down, checked against the file.

---

## Optional, if the room is fast { #optional }

### 14. Sort the lines: numbers sort as text { #sort }

<!-- — · 5 min -->

The editor sees characters, not numbers.

1. **File** > **New Text File**. Type five temperatures of `daily.csv`, one
   per line: `6.3`, `5.0`, `10.4`, `9.8`, `5.6`.
2. Select them, `Ctrl+Shift+P` (macOS `Cmd+Shift+P`), type `sort lines`,
   take **Sort Lines Ascending**.

    ```text
    10.4
    5.0
    5.6
    6.3
    9.8
    ```

    `10.4` comes first: the character `1` comes before `5`. Close the file
    with **Don't Save**.

**Check:** everyone can say why `10.4` stands first.

---

### 15. The export in a spreadsheet { #spreadsheet }

<!-- — · 10 min -->

A spreadsheet reads a CSV file by the region settings of the laptop.

1. Right-click `data/raw/daily_export.csv` > **Reveal in Finder** (Windows
   **Reveal in File Explorer**), then double-click the file.
2. Look: one column per value, or all of a line in column A; `6,3` as a
   number or as text. Do the same with `data/raw/vilnius_week.csv`. Close
   the spreadsheet with **Don't Save**: the files in `data/raw` stay as
   they came.

**Check:** two neighbours with different region settings see the same file differently.

---

## Aims practised

- 📁 **Files:** raw files kept as they arrived and repaired on a copy; rows
  counted against what they should be.
- ♻️ **Reproducibility:** the README says what each file is, its units, how
  a gap is marked, where it came from and when it was fetched.
- 🔧 **Tool-agnosticism:** CSV, JSON and Markdown are plain text, read the
  same by any editor on any system.
