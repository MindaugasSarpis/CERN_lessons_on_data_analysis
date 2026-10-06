# Seminar 6 — A Line of Text into Numbers

**Paired lecture:** 06 Python Foundations · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student turns one line of `D0_KPi.csv` into four
numbers in a script, runs the same steps over the first lines in a loop, and
reads a traceback from the bottom.

The new tool is Python, with the Python extension of VS Code. Everything
else is known: the project folder, the terminal of VS Code (`zsh` on macOS,
PowerShell 7 on Windows, as set up in Seminar 4), Git. No function is
written today and no file is opened from Python: the lines of data are
pasted into the script.

## Run sheet

One screen for the front of the room. Each line links to its section.

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · Run Python** · 30 min | | |
| 0:00 | [1. Check Python and install the extension](#check) | `python3 --version` (Windows `python`), then Extensions, `python`, **Install** | A version number, and coloured code |
| 0:10 | [2. The prompt](#prompt) | `"9.02" / 10` at `>>>` | A number, a text, and the error between them |
| 0:20 | [3. A first script](#script) | `python3 scripts/period.py` (Windows `python`) | `scripts/period.py`, run in three ways |
| | **Part 2 · One line into numbers** · 35 min | | |
| 0:30 | [4. A line of the file as a string](#line) | `clean.split(",")` | A list of four strings |
| 0:42 | [5. Four numbers](#numbers) | `float(parts[0])` | Four floats, a formatted line, a dictionary |
| 0:55 | [6. Read the message](#tracebacks) | `parts[4]`, and the traceback read from the bottom | Three tracebacks read, one silent error seen |
| | **Part 3 · A loop over the first lines** · 35 min | | |
| 1:05 | [7. The first lines in a loop](#loop) | `for line in lines[1:]:` | A table of five rows |
| 1:20 | [8. A mean and a missing value](#mean) | `if tau == MISSING:` | A mean that is wrong, and the same mean put right |
| | **Part 4 · Find a bug** · 20 min | | |
| 1:40 | [9. A wrong number without a message](#debug) | A breakpoint on line 16, then `F5` | The bug found with `print` and with the debugger |
| 1:55 | [10. Wrap up](#wrap-up) | `git commit -m "Add the first Python scripts"` | The scripts listed in the README and committed |

**If time runs short:** section 9 is the one to leave out. Go from section 8
to the wrap-up and leave `mean_period.py` out of the README list.

??? info "How to use this page"
    This page is written for the person at the front. Students follow the
    same page.

    - **Tell the room** is the paragraph to say before the steps.
    - The **numbered steps** are what to do on the projector. The room
      repeats each step on their own laptops.
    - **You should now see** closes a section. Ask for hands: "who sees
      this?" Go on when about four in five have it. The rest get help from a
      neighbour.
    - **Watch for** is the usual slip in that section.

    Every command stands alone in a block. It is typed as it stands and
    ended with `Enter`. The terminal is the one inside VS Code: `zsh` on
    macOS, PowerShell 7 on Windows. Where the two differ, the step has a
    tab for **macOS** and one for **Windows**: Python is `python3` on macOS
    and `python` on Windows. Python itself, at `>>>` and in a script, is the
    same on both. The outputs were printed by `zsh` and by PowerShell 7.6 on
    Windows. Keys are written for Windows, with macOS in brackets.

??? info "Before the session"
    For the room:

    - The project folder as Seminar 4 left it, with `data/raw/D0_KPi.csv`
      and `data/processed/pendulum.csv`. A student who does not have them
      downloads [`project_after_s1.zip`](../data/project_after_s1.zip),
      unpacks it, and opens `analysis-project` with **File** >
      **Open Folder...**.
    - Python, installed in class in Seminar 4
      ([Install Python, Git and PowerShell 7](install_python_git.md)), and
      the terminal of VS Code set up there: `zsh` on macOS, PowerShell 7 on
      Windows.

    A student whose Python does not start follows on a neighbour's laptop
    today and stays for five minutes after the session.

    For you:

    - All ten sections done once on a Mac and once on a Windows laptop with
      PowerShell 7, with the breakpoints of section 9 placed and removed at
      least once.
    - The Python installers for Windows and macOS on a USB stick, for a
      laptop on which the installation in Seminar 4 failed.
    - Decide whether to remove the Python extension from your own VS Code,
      so that you install it together with the room in section 1.

---

## Part 1 · Run Python { #part-1 }

**0:00 to 0:30 · sections 1 to 3**

The room ends this part with a script of five lines that prints a number,
and knows three ways to run it.

---

### 1. Check Python and install the extension { #check }

**0:00 · 10 min**

**Tell the room.** Python is a program on the laptop. It was installed in
Seminar 4 and ran `scripts/clean_pendulum.py` there, the script that
Lecture 06 then read line by line. Today the room writes scripts of its
own. VS Code needs an extension to work with them: the extension colours
the code, completes names and adds a button that runs a script. The
extension does not contain Python.

1. Open the project folder in VS Code and open the terminal with
   **Terminal** > **New Terminal**.

2. Ask Python for its version.

    === "macOS"

        ```text
        python3 --version
        ```

    === "Windows"

        ```text
        python --version
        ```

    It prints one line such as `Python 3.14.0`. Any version from 3.11 on
    is fine.

3. Select the **Extensions** icon in the Activity Bar, or press
   `Ctrl+Shift+X` (macOS `Cmd+Shift+X`). Type into the search box:

    ```text
    python
    ```

4. Select **Python**, published by Microsoft, and then **Install**. A few
   more extensions are installed with it, among them **Pylance** and
   **Python Debugger**.

5. Go back to the Explorer. Right-click the folder `scripts`, select
   **New File** and type:

    ```text
    period.py
    ```

    The file opens empty.

6. Look at the right end of the Status Bar. It now shows the version of
   Python that VS Code has found, for example `3.14.0`.

!!! success "You should now see"
    An empty file `period.py` in `scripts`, and a Python version in the
    Status Bar.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `zsh: command not found: python` | Type `python3`, as in the macOS tab, here and in every later step |
    | Windows: `Python was not found`, or the Microsoft Store opens | Try `py --version`. If it prints a version, type `py` instead of `python` for now. Repair the installation after the session, with the student, as in Seminar 4: run the installer again, select **Modify**, **Next**, tick **Add Python to environment variables**, **Install** |
    | The Status Bar shows **Select Interpreter** instead of a version | Select it and pick the entry with the version that the terminal printed |
    | Nothing is found although Python is installed | Close VS Code with **File** > **Exit** (macOS `Cmd+Q`) and start it again |

---

### 2. The prompt { #prompt }

**0:10 · 10 min**

**Tell the room.** Python can be used one line at a time. It then shows
`>>>`, waits for a line, works it out and prints the value. This is the
place to try a line before it goes into a script. The first row of the
pendulum table gives the numbers: a length of 20 cm, and 10 swings in
9.02 s.

1. Start the prompt in the terminal. A line with the version appears, then
   `>>>`.

    === "macOS"

        ```text
        python3
        ```

    === "Windows"

        ```text
        python
        ```

2. Type each line and press Enter. Ask the room for the result before each
   Enter.

    ```text
    9.02 / 10
    ```

    ```text
    type(9.02)
    ```

    ```text
    type("9.02")
    ```

    ```text
    "9.02" / 10
    ```

    ```text
    float("9.02") / 10
    ```

    Python answers:

    | Line | Python answers |
    |--|--|
    | `9.02 / 10` | `0.9019999999999999` |
    | `type(9.02)` | `<class 'float'>` |
    | `type("9.02")` | `<class 'str'>` |
    | `"9.02" / 10` | A traceback. Its last line is `TypeError: unsupported operand type(s) for /: 'str' and 'int'` |
    | `float("9.02") / 10` | `0.9019999999999999` |

3. Say what the fourth line shows: `"9.02"` in quotes is a text of four
   characters. A text cannot be divided. `float` turns it into a number.

4. Two more lines from the lecture, for the types `int` and `str`.

    ```text
    2 ** 64
    ```

    ```text
    len("ąžuolas")
    ```

    They answer `18446744073709551616` and `7`.

5. Leave the prompt. The prompt of the terminal is back.

    ```text
    exit()
    ```

!!! success "You should now see"
    The terminal prompt again, and the room can say why
    `0.9019999999999999` is not an error: 9.02 has no exact binary form, as
    0.1 had none in Lecture 3.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `SyntaxError: invalid syntax` after typing `python3 scripts/period.py` at `>>>` | That is a terminal command, typed at the Python prompt. `exit()` first |
    | macOS: `zsh: command not found: 9.02` | That is Python, typed at the shell's prompt `%`. Type `python3` first |
    | Windows: `0.902`, with the PowerShell prompt `PS>` before the line instead of `>>>` | PowerShell worked out the line itself, with fewer digits. Type `python` first, then the line again |

---

### 3. A first script { #script }

**0:20 · 10 min**

**Tell the room.** A script is a text file with the lines that would be
typed at the prompt. Python runs it from the first line to the last and
keeps nothing afterwards. The file stays, so the calculation can be run
again and can be put under Git. It is run with the same kind of line that
ran `clean_pendulum.py` in Seminar 4: the program, then the path of the
script.

1. Type into `scripts/period.py`:

    ```text
    # The first row of the pendulum table
    length_cm = 20
    t10_s = 9.02
    period_s = t10_s / 10
    print(period_s)
    ```

2. Save with `Ctrl+S` (macOS `Cmd+S`). Run the script in the terminal.

    === "macOS"

        ```text
        python3 scripts/period.py
        ```

    === "Windows"

        ```text
        python scripts/period.py
        ```

    It prints `0.9019999999999999`.

3. Run it a second way: select the ▶ button at the top right of the Editor,
   **Run Python File**. VS Code types a command into the terminal and the
   same number appears. Read the command: the full path of Python, then the
   full path of the file, the absolute paths of Lecture 04.

4. Run one line a third way: put the cursor in line 3 and press
   `Shift+Enter`. VS Code opens a Python prompt in the terminal and sends
   the line to it. Type at that prompt:

    ```text
    t10_s
    ```

    It answers `9.02`. Leave that prompt:

    ```text
    exit()
    ```

5. The room does this step alone: add a sixth line that prints the period
   with three decimals, and run the script.

    ```text
    print(f"T = {period_s:.3f} s")
    ```

!!! success "You should now see"
    Two lines in the terminal:

    ```text
    0.9019999999999999
    T = 0.902 s
    ```

Leave this table on the projector while the room types.

| Way to run | Use it for |
|--|--|
| `python3 scripts/period.py` in the terminal (Windows `python`) | Every run that counts. This line goes into the README |
| ▶ **Run Python File** | The same, with one click |
| `Shift+Enter` on a line | Trying one line of a script |

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `can't open file '…period.py': [Errno 2] No such file or directory` | The terminal is not in the project folder, or the name is misspelled. `pwd`, then `ls scripts`: both work in `zsh` and in PowerShell |
    | The old output, or no output | The file is not saved. A dot on the tab means *not saved* |
    | `IndentationError: unexpected indent` | A space stands before the first character of a line. Delete it |
    | `NameError: name 'period_s' is not defined` | The lines are in another order, or a name is spelled in two ways |

---

## Part 2 · One line into numbers { #part-2 }

**0:30 to 1:05 · sections 4 to 6**

Everything a program reads from a text file arrives as text. This part
takes one line of the data file and makes four numbers of it in three
steps: strip, split, convert.

---

### 4. A line of the file as a string { #line }

**0:30 · 12 min**

**Tell the room.** The line is copied from the file and pasted into the
script between quotes. To Python it is then a string of 43 characters: 42
that can be seen and the line break. Seminar 4 counted the same bytes per
row: 42 characters and one line break.

1. Print the first two lines of the data file in the terminal.

    === "macOS"

        ```text
        head -n 2 data/raw/D0_KPi.csv
        ```

    === "Windows"

        ```text
        Get-Content data/raw/D0_KPi.csv -Head 2
        ```

    The terminal shows:

    ```text
    M,PT,TAU,IPCHI2
    1880.649,3000.9534,0.00041271152,1299.1675
    ```

2. Create a new file in `scripts`:

    ```text
    parse_line.py
    ```

    Type `line = "`, paste the second line of the output, and close it
    with `\n"`. The two characters `\n` stand for the line break that ends
    the line in the file.

    ```text
    line = "1880.649,3000.9534,0.00041271152,1299.1675\n"
    print(len(line))
    ```

    Run it. It prints `43`.

3. Strip the line break and count again. Add:

    ```text
    clean = line.strip()
    print(len(clean))
    ```

    It prints `42`.

4. Cut the string at the commas. Add:

    ```text
    parts = clean.split(",")
    print(parts)
    print(len(parts))
    print(parts[0])
    print(type(parts[0]))
    ```

!!! success "You should now see"
    Six lines of output:

    ```text
    43
    42
    ['1880.649', '3000.9534', '0.00041271152', '1299.1675']
    4
    1880.649
    <class 'str'>
    ```

Point at the quotes in the third line. `parts` is a list of four strings.
`parts[0]` prints as `1880.649` and looks like a number, and its type is
still `str`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `SyntaxError: unterminated string literal` | The closing `"` is missing, or the pasted text brought a real line break with it. The string has to stand on one line |
    | `44` instead of `43` | A space was pasted with the line. Delete it |

---

### 5. Four numbers { #numbers }

**0:42 · 13 min**

**Tell the room.** `float` turns a string into a number. After that the
values can be used in arithmetic. The four names are the four columns of
the header line: the mass `M`, the transverse momentum `PT`, the decay time
`TAU` and `IPCHI2`.

1. Delete every `print` line except `print(parts)`. Four lines remain.
   Then add:

    ```text
    m = float(parts[0])
    pt = float(parts[1])
    tau = float(parts[2])
    ipchi2 = float(parts[3])
    print(m, pt, tau, ipchi2)
    print(m - 1865)
    ```

    Leave an empty line above `m = …`. The script is read more easily in
    blocks.

2. Run it. The last line of the output is `15.648999999999887`: the mass of
   this candidate lies 15.6 MeV/c² above 1865. The long tail of digits is
   the float64 again.

3. Print the same for a reader. Add:

    ```text
    print(f"M = {m:.1f}, {m - 1865:.1f} above 1865")
    ```

4. Keep the row with the names of its columns. Add, after an empty line:

    ```text
    row = {"M": m, "PT": pt, "TAU": tau, "IPCHI2": ipchi2}
    print(row)
    print(row["TAU"])
    ```

!!! success "You should now see"
    ```text
    ['1880.649', '3000.9534', '0.00041271152', '1299.1675']
    1880.649 3000.9534 0.00041271152 1299.1675
    15.648999999999887
    M = 1880.6, 15.6 above 1865
    {'M': 1880.649, 'PT': 3000.9534, 'TAU': 0.00041271152, 'IPCHI2': 1299.1675}
    0.00041271152
    ```

Compare the first two lines of the output: with quotes and without. That
difference is the whole section. Then compare `parts[2]` with `row["TAU"]`:
the same value, and only the second says what it is.

---

### 6. Read the message { #tracebacks }

**0:55 · 10 min**

**Tell the room.** A script that cannot go on stops and prints a traceback.
It is read from the bottom: the last line says what went wrong, the lines
above it say where. The room now makes three errors on purpose, reads each
message and takes the error back with `Ctrl+Z` (macOS `Cmd+Z`).

1. In line 9 change `parts[3]` to `parts[4]`. The line reads:

    ```text
    ipchi2 = float(parts[4])
    ```

    Run it. The traceback ends:

    ```text
        ipchi2 = float(parts[4])
                       ~~~~~^^^
    IndexError: list index out of range
    ```

    The list has four items with the indices 0 to 3. The line above the
    message names the file and `line 9`. Undo the change.

2. In line 6 change `m = float(parts[0])` to:

    ```text
    m = parts[0]
    ```

    Run it. The traceback ends:

    ```text
        print(m - 1865)
              ~~^~~~~~
    TypeError: unsupported operand type(s) for -: 'str' and 'int'
    ```

    The traceback names line 11. Line 11 is correct. The mistake is in
    line 6, where `m` was made. Ask the room how to get from line 11 to
    line 6: follow the name `m` upwards. Undo the change.

3. In line 10 change `ipchi2` to `ipchi`. The line reads:

    ```text
    print(m, pt, tau, ipchi)
    ```

    Before running, look at the Editor: the extension has drawn a wavy
    line under `ipchi`. Run it. The last line of the traceback:

    ```text
    NameError: name 'ipchi' is not defined. Did you mean: 'ipchi2'?
    ```

    Undo the change.

4. Now an error without a message. In line 1 change `1880.649` to
   `1880,649`, a decimal comma. The line reads:

    ```text
    line = "1880,649,3000.9534,0.00041271152,1299.1675\n"
    ```

    Run it. The output begins:

    ```text
    ['1880', '649', '3000.9534', '0.00041271152', '1299.1675']
    1880.0 649.0 3000.9534 0.00041271152
    ```

    Python reports nothing. The comma made five parts out of four, and
    every value moved one place to the right: the momentum is now 649 and
    the decay time 3000.9534. Undo the change and run once more.

!!! success "You should now see"
    The six lines of section 5 again.

**Say it in these words.** Python finds a line that it cannot carry out. It
does not find a number that is wrong. For that someone has to know what the
number should be.

---

## Part 3 · A loop over the first lines { #part-3 }

**1:05 to 1:40 · sections 7 and 8**

The three steps of Part 2 work for one line. A loop applies them to every
line that it is given: five lines today, 91 583 once the whole file is
read.

---

### 7. The first lines in a loop { #loop }

**1:05 · 15 min**

**Tell the room.** A string between three quotes may run over several
lines. `splitlines` cuts it into a list with one string for each line. The
loop `for line in lines:` then runs its block once for each of them. The
block is the lines that are indented by four spaces.

1. Print the first six lines of the file in the terminal and copy them.

    === "macOS"

        ```text
        head -n 6 data/raw/D0_KPi.csv
        ```

    === "Windows"

        ```text
        Get-Content data/raw/D0_KPi.csv -Head 6
        ```

2. Create a new file in `scripts`:

    ```text
    first_rows.py
    ```

    Type `table = """`, paste the six lines, and close with `"""`
    directly after the last number.

    ```text
    table = """M,PT,TAU,IPCHI2
    1880.649,3000.9534,0.00041271152,1299.1675
    1860.6599,2803.4126,0.0001864154,0.34182164
    1913.8755,2542.169,0.00018464602,17.386473
    1888.7571,4453.104,0.00056827645,56.79793
    1862.51,2764.228,0.0002869703,3.6449974"""

    lines = table.splitlines()
    print(len(lines))
    print(lines[0])
    ```

    Run it. It prints `6` and `M,PT,TAU,IPCHI2`.

3. Add the loop. After the `:` press Enter: VS Code indents the next line
   by four spaces.

    ```text
    for line in lines:
        parts = line.split(",")
        m = float(parts[0])
        print(m)
    ```

4. Run it. The script stops in the first turn of the loop:

    ```text
    ValueError: could not convert string to float: 'M'
    ```

    Ask the room what `'M'` is. It is the first part of the header line.
    The header is not data.

5. Change `lines` in the `for` line to `lines[1:]`: every line from index 1
   on. Run again. Five masses are printed.

    ```text
    for line in lines[1:]:
    ```

6. Print two columns with a fixed width. Replace the loop by:

    ```text
    print(f"{'M':>10}{'PT':>10}")
    for line in lines[1:]:
        parts = line.split(",")
        m = float(parts[0])
        pt = float(parts[1])
        print(f"{m:>10.1f}{pt:>10.1f}")
    ```

!!! success "You should now see"
    ```text
    6
    M,PT,TAU,IPCHI2
             M        PT
        1880.6    3001.0
        1860.7    2803.4
        1913.9    2542.2
        1888.8    4453.1
        1862.5    2764.2
    ```

`>10.1f` reads: to the right, in a width of 10 characters, with one
decimal. The numbers stand under each other because every one of them takes
the same width.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `IndentationError: expected an indented block after 'for' statement` | The lines under `for` are not indented. Select them and press `Tab` |
    | `IndentationError: unindent does not match any outer indentation level` | The lines of the block are indented by different amounts. Give each of them four spaces |
    | Only one row is printed | The `print` line is not indented, so it runs once, after the loop |
    | `ValueError: could not convert string to float: ''` | An empty line stands before the closing `"""`. Close the quotes directly after the last number |

---

### 8. A mean and a missing value { #mean }

**1:20 · 20 min**

**Tell the room.** A sum is built in a loop from three pieces: a start value
before the loop, an update inside it, and the result after it. The file
marks a missing decay time with `-100`. Seminar 4 counted 49 such rows with
`grep -c` and `Select-String`. A marker like this has to be taken out
before any arithmetic.

1. Open `data/raw/D0_KPi.csv`, press `Ctrl+G` (the same key on macOS), type
   the line number and press Enter.

    ```text
    343
    ```

    Line 343 is the first row without a decay time:

    ```text
    1818.1002,2978.644,-100.0,9901.186
    ```

    Copy the line and paste it into `first_rows.py` as the last line of the
    table, before the closing `"""`. Close the data file without saving.

2. Add the mean of the mass at the end of the script.

    ```text
    n = 0
    total = 0.0
    for line in lines[1:]:
        parts = line.split(",")
        n = n + 1
        total = total + float(parts[0])
    print(f"{n} rows, mean M = {total / n:.1f}")
    ```

    Run it. The last line is `6 rows, mean M = 1870.8`.

3. The room does this step alone: copy the seven lines below themselves and
   change the copy to the mean of the decay time, column 2, printed with
   `:.6f`. The last line is then:

    ```text
    6 rows, mean TAU = -16.666393
    ```

    Ask what is wrong with this number. A time cannot be negative. One
    value of −100 among six has moved the mean from 0.0003 to −16.7.

4. Put the marker into a name at the top of the block and skip the row.
   Change the copy to:

    ```text
    MISSING = -100
    n = 0
    n_missing = 0
    total = 0.0
    for line in lines[1:]:
        parts = line.split(",")
        tau = float(parts[2])
        if tau == MISSING:
            n_missing = n_missing + 1
        else:
            n = n + 1
            total = total + tau
    print(f"{n} rows with a decay time, {n_missing} without")
    print(f"mean TAU = {total / n:.6f}")
    ```

!!! success "You should now see"
    As the last lines of the output:

    ```text
        1818.1    2978.6
    6 rows, mean M = 1870.8
    6 rows, mean TAU = -16.666393
    5 rows with a decay time, 1 without
    mean TAU = 0.000328
    ```

The block under `if` is indented twice: once for the loop and once for the
decision. `MISSING` is written in capitals because it never changes, and it
has a name because a bare `-100` in the middle of a script explains nothing.

!!! warning "Watch for"
    A mean of TAU that is still negative after step 4. The update
    `total = total + tau` stands outside the `else`, so the −100 is added
    after all. Its indentation has to match `n = n + 1`.

---

## Part 4 · Find a bug { #part-4 }

**1:40 to 2:00 · sections 9 and 10**

A script that gives a wrong number without any message is examined with
`print` and with the debugger. Then the scripts are committed.

---

### 9. A wrong number without a message { #debug }

**1:40 · 15 min**

**Tell the room.** The pendulum table of Lecture 2 came with a line
`;mean;15,14`: ten swings took 15.14 s on average, so the mean period is
1.514 s. That is the expected value. The script below gets another number
and reports no error. The room finds the reason twice: with a `print`, and
with the debugger, which stops the script at a line and shows every name
with its value.

1. Create a new file in `scripts`:

    ```text
    mean_period.py
    ```

    Open `data/processed/pendulum.csv`, copy its ten lines and paste them
    between three quotes. Then type the rest as it stands here, with the
    mistake in it.

    ```text
    table = """length_cm,t10_s
    20,9.02
    30,11.05
    40,12.61
    50,14.23
    60,15.49
    70,16.84
    80,17.90
    90,19.10
    100,20.01"""

    lines = table.splitlines()
    total = 0.0
    for line in lines[1:]:
        parts = line.split(",")
        total = total + float(parts[1]) / 10
    mean = total / len(lines)
    print(mean)
    ```

2. Run it. It prints `1.3625`. Expected was 1.514.

3. Look with `print`. Add a line above `mean = …`, at line 17, and run.

    ```text
    print(f"{total=} {len(lines)=}")
    ```

    The output:

    ```text
    total=13.625 len(lines)=10
    1.3625
    ```

    Give the room a minute. The sum 13.625 is right. The table has nine
    rows and the script divides by 10. Delete the added line again with
    `Ctrl+Shift+K` (macOS `Cmd+Shift+K`).

4. Now the same with the debugger. Click to the left of the line number 16.
   A red dot appears: a **breakpoint**.

5. Press `F5`. In the list that opens select **Python Debugger**, then
   **Python File**. The script starts and stops before line 16, which is
   marked. On the left, under **Variables**, read `line = '20,9.02'` and
   `total = 0.0`.

6. Press `F5` again: **Continue**. The script runs one turn of the loop and
   stops at the same line. Now `line = '30,11.05'` and
   `total = 0.9019999999999999`. Once more: `total = 2.0069999999999997`.

7. Press `F10`: **Step Over**. Only line 16 runs. `total` changes to
   `3.268`, and the mark moves on.

8. Click the red dot to remove it and put one at line 17. Press `F5`. The
   loop is finished: `total = 13.625`. Under **Variables** open `lines`
   with the arrow in front of it. Its last entry is `len(): 10`. Select the
   **Debug Console** tab in the Panel, type and press Enter:

    ```text
    total / 9
    ```

    It answers `1.5138888888888888`.

9. Press `Shift+F5` to stop. Remove the breakpoint. Repair line 17 and
   print the result for a reader.

    ```text
    mean = total / (len(lines) - 1)
    print(f"mean period = {mean:.3f} s")
    ```

!!! success "You should now see"
    `mean period = 1.514 s` in the terminal.

`print` answers the one question that was asked. The debugger shows every
name at once, at any line, without a change to the script.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `F5` does nothing, or changes the brightness (macOS, some laptops) | Hold `Fn` with the key, or select **Run** > **Start Debugging** |
    | No list after `F5`, and a file `launch.json` opens | Close it without saving. Select `mean_period.py` in the Editor first, then press `F5` |
    | The script runs through without stopping | The red dot stands on an empty line or on a line of the table. Put it on line 16 |
    | The yellow mark stays and the terminal is silent | The script is stopped, not broken. `F5` continues, `Shift+F5` ends |

---

### 10. Wrap up { #wrap-up }

**1:55 · 5 min**

**Tell the room.** The scripts are part of the project now. They are listed
in the README and committed, like every other file of the folder.

1. Add a section to `README.md`.

    ```text
    ## Scripts

    Run from the project folder, for example
    `python3 scripts/parse_line.py` in zsh,
    `python scripts/parse_line.py` in PowerShell.

    - `period.py`: the period of one pendulum row
    - `parse_line.py`: one line of `D0_KPi.csv` as four numbers
    - `first_rows.py`: the first rows in a loop, mean of M and TAU
    - `mean_period.py`: the mean period of the pendulum table
    ```

2. Commit the four scripts and the README: in the **Source Control** view
   stage the changes, type the message `Add the first Python scripts` and
   select **Commit**. Or type the two lines below, the same in `zsh` and in
   PowerShell:

    ```text
    git add scripts README.md
    ```

    ```text
    git commit -m "Add the first Python scripts"
    ```

3. Read the list below aloud. Ask on the way out which step was hardest.

!!! success "You should now see"
    The commit `Add the first Python scripts` in the **Source Control**
    view.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `fatal: not a git repository` | The folder was unpacked from the zip today and is not under Git. Select **Initialize Repository** in the **Source Control** view once, as in Seminar 5, then commit |
    | Windows: `warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it` | A note, not an error: the commit is made. Git on this laptop missed the setting of Seminar 5. Type `git config --global core.autocrlf false` once |

What the room has learned:

- Python runs at a prompt, one line at a time, and as a script, from top to
  bottom.
- A value has a type. `9.02` is a number and `"9.02"` is a text, and only
  the first can be divided.
- A line of a CSV file becomes numbers in three steps: `strip`, `split`,
  `float`.
- A loop applies the steps for one line to every line. The block is the
  indented lines.
- A marker of a missing value is taken out with an `if` before anything is
  added up.
- A traceback is read from the bottom: what, then where.
- A wrong number without a message is found by comparing with an expected
  value, with `print` or with a breakpoint.

---

## Stretch goals

For students who finish a section early. Answers are given for the
lecturer.

- In `parse_line.py`, convert all parts in one line:
  `values = [float(p) for p in parts]`. The answer is
  `[1880.649, 3000.9534, 0.00041271152, 1299.1675]`.
- In `first_rows.py`, find the smallest and the largest mass with a loop
  and two `if`, without `min` and `max`. With the seven lines of section 8
  the answer is 1818.1002 and 1913.8755.
- Count the rows of `first_rows.py` whose mass lies between 1840 and 1890.
  The answer is 4 of 6.
- Parse a row of the raw pendulum file, `"1;20;9,02"`: replace the comma,
  split at `;`, and print the period. The answer is
  `line.replace(",", ".").split(";")`, then `0.902` with `:.3f`.
- Compute g for every row of the pendulum table from
  g = 4π²L / T², with L in metres. `import math` gives `math.pi`. The
  answer is nine values between 9.70 and 9.93 m/s²: 9.70, 9.70, 9.93, 9.75,
  9.87, 9.74, 9.86, 9.74, 9.86.
- Build one dictionary per row in `first_rows.py`, with the names of the
  header line as keys, and collect them in a list `rows`. The answer:
  `rows[0]["M"]` is 1880.649 and `rows[-1]["TAU"]` is -100.0.
- A student with a dataset of their own pastes its header line and first
  five rows into `scripts/my_first_rows.py`, splits each line with the
  separator of the file and converts the columns that hold numbers. Which
  columns does `float` not convert, and why: a text, a date, a decimal
  comma, an empty field? Then print two columns with a fixed width, as in
  section 7, and, if the file marks missing values, count them with an
  `if`, as in section 8.

## If students ask for more

| Topic | Week |
|--|--|
| Reading the whole file instead of pasting lines | 7 (Python for Data & NumPy) |
| Writing a function, so that the three steps have a name | 7 (Python for Data & NumPy) |
| What to do when one line of 91 583 cannot be converted | 7 (Python for Data & NumPy) |
| A plot of the periods against the length | 8 (Data Visualisation) |

Leave out altogether, even if asked: notebooks, virtual environments,
installing packages, classes.

## Aims practised

🔧 the same script on every system · ⚙️ one recipe applied to every row · ♻️ a calculation that runs again · 📁 text from a file turned into numbers
