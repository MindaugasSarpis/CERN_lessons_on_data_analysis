# Seminar 3 — Files and Bytes from the Terminal

**Paired lecture:** 03 How Computers Work · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student tidies a folder of files from the terminal,
and can say for each file how many bytes it has and why.

The tools are the terminal inside VS Code and one extension, the **Hex
Editor**. The shell is `zsh` on macOS and the PowerShell that Windows already
has, 5.1 or 7: every line on this page runs in both.

## Run sheet

One screen for the front of the room. Each line links to its section.

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · The terminal** · 20 min | | |
| 0:00 | [1. Open a terminal](#terminal) | **Terminal** > **New Terminal**, `pwd` | The prompt read aloud, part by part |
| 0:08 | [2. Move around](#move) | `ls`, `cd Downloads`, `cd ..`, `cd ~` | Back in the home folder, checked with `pwd` |
| 0:15 | [3. A folder for today](#lab) | `mkdir files-lab`, **Open Folder** | A prompt that ends in `files-lab` |
| | **Part 2 · A folder to tidy** · 25 min | | |
| 0:20 | [4. Bring the files in](#inbox) | `mv ~/Downloads/inbox .` | `inbox` with seven files |
| 0:30 | [5. A name with a space](#space) | `mv "inbox/shopping list.txt" …` | No space in any name |
| 0:35 | [6. Sort into folders](#sort) | `mkdir`, `mv`, `cp`, `rm` | `text` and `tables` hold five files |
| | **Part 3 · Bytes** · 35 min | | |
| 0:45 | [7. Sizes](#sizes) | `wc -c` or `(Get-Item …).Length` | 34, 71 and 49 bytes |
| 0:53 | [8. A letter of two bytes](#letters) | The Hex Editor on `shopping_list.txt` | `ū` found as `C5 AB` |
| 1:03 | [9. A line break of two bytes](#crlf) | `CRLF` in the Status Bar of `todo.txt` | 71 bytes, then 67 |
| 1:10 | [10. The wrong table](#encoding) | **Reopen with Encoding** on `labas.txt` | The letters back; 49 bytes, then 55 |
| | **Part 4 · What a file is** · 25 min | | |
| 1:20 | [11. A picture called .txt](#magic) | `hexdump -C` or `Format-Hex` on `photo.txt` | `89 50 4E 47`, and `photo.png` in `images` |
| 1:27 | [12. The same file?](#hash) | `shasum -a 256` or `Get-FileHash` | Two hashes, and the one byte that differs |
| 1:35 | [13. Write it down](#notes) | `notes.md` and its preview | Three answers in `notes.md` |
| 1:42 | [14. Wrap up](#wrap-up) | The list of what was learned | |
| | **Optional, if the room is fast** | | |
| — | [15. Three bytes before the header](#bom) | `expenses.csv` in the Hex Editor | `EF BB BF`; 111 bytes, 108 characters |
| — | [16. A checksum by hand](#by-hand) | `abc` in a new file | 38, and a change it misses |
| — | [17. An emoji](#emoji) | 😀 in the Hex Editor | Four bytes, `F0 9F 98 80` |

**If time runs short:** leave out section 13 and write the three answers on
the board instead. Every section of Part 3 and Part 4 starts from the folder
`inbox` alone.

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

    Every line to type stands in its own grey block. Where macOS and Windows
    differ, the step has a tab for each. Keys are written for Windows, with
    macOS in brackets.

??? info "Before the session"
    For the room: VS Code, and a laptop that can download a file. Nothing
    else is installed beforehand.

    For you, about ten minutes:

    - Download [`inbox.zip`](../data/inbox.zip) and do sections 4, 8 and 10
      once on your own laptop, so that you have seen the Hex Editor and
      **Reopen with Encoding**.
    - On Windows, the terminal of VS Code opens Windows PowerShell 5.1 unless
      PowerShell 7 is installed. Both are fine today. The layout of
      `Format-Hex` differs a little between them; the bytes are the same.

??? info "Files for this seminar"
    Each file hides a single thing that only its bytes show. They were made
    by [`inbox_files.py`](../data/inbox_files.py).

    | File | What it is |
    |--|--|
    | [`inbox.zip`](../data/inbox.zip) | Section 4: seven files, unpacked into a folder `inbox` |
    | [`inbox_after.zip`](../data/inbox_after.zip) | The folder `inbox` at the end of section 12. A student who lost a step takes the file from here |

---

## Part 1 · The terminal { #part-1 }

**0:00 to 0:20 · sections 1 to 3**

The room opens a terminal, reads its prompt, moves between folders, and
makes the folder for today.

---

### 1. Open a terminal { #terminal }

**0:00 · 8 min**

**Tell the room.** A terminal is a window. The program inside it, the
shell, reads each line you type, runs it, prints the answer and waits for
the next line. VS Code has a terminal in its Panel. The prompt at the start
of the line says who you are, where you are, and that the shell waits.

1. Open VS Code. Select **Terminal**, then **New Terminal**. The Panel opens
   at the bottom.

2. Read the prompt aloud, part by part.

    === "macOS"

        ```text
        smilte@MacBook-Air ~ %
        ```

        `smilte` is the user, `MacBook-Air` the computer, `~` the home folder,
        and `%` means the shell waits.

    === "Windows"

        ```text
        PS C:\Users\smilte>
        ```

        `PS` is PowerShell, `C:\Users\smilte` the folder it is in, and `>`
        means it waits.

3. Type, and press Enter:

    ```text
    pwd
    ```

    === "macOS"

        ```text
        /Users/smilte
        ```

    === "Windows"

        ```text
        Path
        ----
        C:\Users\smilte
        ```

4. Look at the top right of the Panel. It names the shell: `zsh`,
   `powershell` or `pwsh`.

!!! success "You should now see"
    The path of your own home folder, with your own user name in it. This
    folder is the **working directory**: commands start from here.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Nothing happens after `pwd` | The line was typed into the editor. Click into the Panel and type it again |
    | A Mac prompt that ends in `$`, and `bash` at the top right | An old account. Type `chsh -s /bin/zsh`, give the password, and open a new terminal |
    | The text is too small for the back row | `Ctrl` and `+` (macOS `Cmd` and `+`) |

---

### 2. Move around { #move }

**0:08 · 7 min**

**Tell the room.** `ls` lists the working directory. `cd` changes it, and
the prompt follows. A path that does not start at the top of the disk
starts at the working directory: it is **relative**. `..` is the folder
above.

1. List the home folder:

    ```text
    ls
    ```

    The room sees `Desktop`, `Documents`, `Downloads` and others. PowerShell
    prints a table, with a `d` in front of every folder.

2. Go into the Downloads folder:

    ```text
    cd Downloads
    ```

    The prompt now ends in `Downloads` (macOS `smilte@MacBook-Air Downloads %`,
    Windows `PS C:\Users\smilte\Downloads>`).

3. List it:

    ```text
    ls
    ```

4. Go one folder up, and check where you are:

    ```text
    cd ..
    ```

    ```text
    pwd
    ```

5. From any folder, `~` is the home folder:

    ```text
    cd Downloads
    ```

    ```text
    cd ~
    ```

6. Empty the Panel. Nothing is deleted, only the text on the screen:

    ```text
    clear
    ```

!!! success "You should now see"
    A prompt that shows the home folder again, and `pwd` that prints it.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `no such file or directory`, or `Cannot find path` | A letter is missing. Type the name as `ls` printed it |
    | A prompt that grows longer and longer | Several `cd` in a row went further down. `cd ~` goes home |

---

### 3. A folder for today { #lab }

**0:15 · 5 min**

**Tell the room.** Today's work happens in one new folder in the home
folder. VS Code opens it, and its terminal then starts there.

1. Make the folder, from the home folder:

    ```text
    cd ~
    ```

    ```text
    mkdir files-lab
    ```

    zsh prints nothing. PowerShell prints a short table with the new
    folder.

2. In VS Code select **File** > **Open Folder…**, go to the home folder,
   select `files-lab`, and **Open**.

3. Open a new terminal: **Terminal** > **New Terminal**. Check:

    ```text
    pwd
    ```

    === "macOS"

        ```text
        /Users/smilte/files-lab
        ```

    === "Windows"

        ```text
        Path
        ----
        C:\Users\smilte\files-lab
        ```

!!! success "You should now see"
    VS Code with `FILES-LAB` at the top of the Side Bar, and a prompt that
    ends in `files-lab`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `pwd` still prints the home folder | The terminal was opened before the folder. Close it with the bin icon of the Panel and open a new one |
    | `File exists`, or `An item with the specified name … already exists` | The folder is there from an earlier try. Go on with step 2 |

---

## Part 2 · A folder to tidy { #part-2 }

**0:20 to 0:45 · sections 4 to 6**

A folder of seven files arrives. The room moves it in, fixes a name, and
sorts the files into folders, all from the terminal.

---

### 4. Bring the files in { #inbox }

**0:20 · 10 min**

**Tell the room.** The files for today come as a zip: seven everyday files
copied from an old laptop. Each hides one thing that only its bytes show.
`notes.md` lists the three questions of the day.

1. Download [`inbox.zip`](../data/inbox.zip).

2. Unpack it in the Downloads folder.

    === "macOS"

        In Finder, open **Downloads** and double-click `inbox.zip`. A folder
        `inbox` appears. Safari may have done this already.

    === "Windows"

        In Explorer, open **Downloads**, right-click `inbox.zip`, select
        **Extract All…**, then **Extract**. A folder `inbox` appears.

3. In the terminal of `files-lab`, move the folder here. `.` is the working
   directory:

    ```text
    mv ~/Downloads/inbox .
    ```

4. List it:

    ```text
    ls inbox
    ```

5. Open `inbox/notes.md` in VS Code and read the three questions aloud.

!!! success "You should now see"
    `inbox` in the Side Bar with seven files: `expenses.csv`,
    `expenses_copy.csv`, `labas.txt`, `notes.md`, `photo.txt`,
    `shopping list.txt` and `todo.txt`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `No such file or directory` after `mv` | The folder has another name, such as `inbox 2`, or the zip is still packed. `ls ~/Downloads` shows what is there |
    | The seven files lie loose in Downloads, with no folder `inbox` | The zip was unpacked without a folder. Make a folder `inbox` in Downloads in Finder or Explorer, drag the seven files into it, then `mv` again |

---

### 5. A name with a space { #space }

**0:30 · 5 min**

**Tell the room.** The shell splits a line at every space. A name with a
space is read as two names. Quotes keep it together, and a name without
spaces needs no quotes at all.

1. Try the name without quotes:

    ```text
    ls inbox/shopping list.txt
    ```

    === "macOS"

        ```text
        ls: inbox/shopping: No such file or directory
        ls: list.txt: No such file or directory
        ```

    === "Windows"

        ```text
        Get-ChildItem: Cannot find path 'C:\Users\smilte\files-lab\inbox\shopping'
        because it does not exist.
        ```

2. With quotes:

    ```text
    ls "inbox/shopping list.txt"
    ```

3. Rename it with `mv`, the old name first, then the new one:

    ```text
    mv "inbox/shopping list.txt" inbox/shopping_list.txt
    ```

!!! success "You should now see"
    `shopping_list.txt` in the Side Bar, and no name with a space in
    `inbox`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | A prompt `dquote>` (macOS) or `>>` (Windows), waiting | A closing quote is missing. Press `Ctrl+C` and type the line again |

---

### 6. Sort into folders { #sort }

**0:35 · 10 min**

**Tell the room.** `mkdir` makes a folder, `mv` moves a file into it, `cp`
copies, `rm` deletes. `rm` has no Trash and no Recycle Bin: what it deletes
is gone.

1. Make three folders, one line each:

    ```text
    mkdir inbox/text
    ```

    ```text
    mkdir inbox/tables
    ```

    ```text
    mkdir inbox/images
    ```

2. Move the three text files into `text`:

    ```text
    mv inbox/shopping_list.txt inbox/text
    ```

    ```text
    mv inbox/todo.txt inbox/text
    ```

    ```text
    mv inbox/labas.txt inbox/text
    ```

3. Move the two tables into `tables`:

    ```text
    mv inbox/expenses.csv inbox/tables
    ```

    ```text
    mv inbox/expenses_copy.csv inbox/tables
    ```

    `photo.txt` stays where it is. Part 4 finds out what it is.

4. Make a spare copy, look at it, delete it:

    ```text
    cp inbox/text/todo.txt todo_spare.txt
    ```

    ```text
    ls
    ```

    ```text
    rm todo_spare.txt
    ```

    ```text
    ls
    ```

!!! success "You should now see"
    | Folder | Holds |
    |--|--|
    | `inbox` | `images`, `notes.md`, `photo.txt`, `tables`, `text` |
    | `inbox/text` | `labas.txt`, `shopping_list.txt`, `todo.txt` |
    | `inbox/tables` | `expenses.csv`, `expenses_copy.csv` |
    | `inbox/images` | nothing yet |

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | A file called `txt` or `tabels` in `inbox` | `mv` to a folder that does not exist renames the file. Move it back with the right name: `mv inbox/tabels inbox/tables/expenses.csv` |
    | `rm` removed the wrong file | It is gone. Take it from [`inbox_after.zip`](../data/inbox_after.zip) |

---

## Part 3 · Bytes { #part-3 }

**0:45 to 1:20 · sections 7 to 10**

Each file is measured to the byte, and each size is explained.

---

### 7. Sizes { #sizes }

**0:45 · 8 min**

**Tell the room.** A file manager rounds sizes to KB. The terminal gives
the exact number of bytes. Before each line, the room predicts.

1. Count the characters of `shopping_list.txt` with the room. The five
   words have 6 + 5 + 5 + 8 + 4 = 28 letters, and every line ends with a
   line break: 33 characters.

2. Measure it:

    === "macOS"

        ```text
        wc -c inbox/text/shopping_list.txt
        ```

        ```text
              34 inbox/text/shopping_list.txt
        ```

    === "Windows"

        ```text
        (Get-Item inbox/text/shopping_list.txt).Length
        ```

        ```text
        34
        ```

    One byte more than characters. Section 8 finds it.

3. Measure `todo.txt` and `labas.txt` the same way: change only the name of
   the file in the line.

!!! success "You should now see"
    | File | Bytes |
    |--|--|
    | `inbox/text/shopping_list.txt` | 34 |
    | `inbox/text/todo.txt` | 71 |
    | `inbox/text/labas.txt` | 49 |

    For later: `expenses.csv` and `expenses_copy.csv` have 111 bytes each,
    `photo.txt` 152, `notes.md` 216.

---

### 8. A letter of two bytes { #letters }

**0:53 · 10 min**

**Tell the room.** In UTF-8 the letters `a` to `z` take one byte each. A
Lithuanian letter takes two. The Hex Editor shows every byte of a file, two
hex digits each.

1. Install the Hex Editor. Select **Extensions** in the Activity Bar, or
   press `Ctrl+Shift+X` (macOS `Cmd+Shift+X`), and search:

    ```text
    hex editor
    ```

    Select **Hex Editor** published by **Microsoft**, then **Install**.

2. Right-click `inbox/text/shopping_list.txt` in the Side Bar, select
   **Open With…**, then **Hex Editor**.

3. Find `ū` of `sūris`: the two bytes `C5 AB`, at the end of the first row.
   Every other letter is one byte, and `0A` ends each line.

4. The same bytes from the terminal:

    === "macOS"

        ```text
        hexdump -C inbox/text/shopping_list.txt
        ```

        ```text
        00000000  70 69 65 6e 61 73 0a 64  75 6f 6e 61 0a 73 c5 ab  |pienas.duona.s..|
        00000010  72 69 73 0a 6f 62 75 6f  6c 69 61 69 0a 6b 61 76  |ris.obuoliai.kav|
        00000020  61 0a                                             |a.|
        00000022
        ```

        The last line is the size in hex: 0x22 = 2 × 16 + 2 = 34.

    === "Windows"

        ```text
        Format-Hex inbox/text/shopping_list.txt
        ```

        The first row ends in `73 C5 AB`, shown on the right as `sÅ«`:
        PowerShell 7 reads each byte alone, and `C5` alone is `Å`.

!!! success "You should now see"
    `73 C5 AB 72 69 73` is `sūris`: five letters, six bytes. 33 characters,
    34 bytes.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Several extensions called Hex Editor | Take the one published by Microsoft |
    | A last cell with `+` after the bytes | A button for adding a byte, not part of the file. Do not count it |

---

### 9. A line break of two bytes { #crlf }

**1:03 · 7 min**

**Tell the room.** A line break is a byte too: `0A`, called LF. Windows
programs often write two bytes, `0D 0A`, called CRLF. `todo.txt` was saved
that way.

1. Open `inbox/text/todo.txt` as text. The right end of the Status Bar
   reads `CRLF`.

2. Open it with the Hex Editor. After `call the dentist` come `0D 0A`.

3. Count with the room: the four lines have 16 + 12 + 19 + 16 = 63
   characters, and four line breaks of two bytes: 63 + 8 = 71.

4. Back in the text tab, select `CRLF` in the Status Bar, choose `LF`, and
   save with `Ctrl+S` (macOS `Cmd+S`).

5. Measure again, as in section 7.

!!! success "You should now see"
    67 bytes: one byte less on each of the four lines. The Status Bar reads
    `LF`.

!!! warning "Watch for"
    The size is still 71: the file was not saved. A dot on the tab means
    *not saved*.

---

### 10. The wrong table { #encoding }

**1:10 · 10 min**

**Tell the room.** The bytes of a text mean nothing without the table that
turns bytes into characters: the encoding. VS Code reads files as UTF-8.
`labas.txt` was saved with an older Baltic table, Windows-1257, so its
Lithuanian letters do not make sense as UTF-8.

1. Open `inbox/text/labas.txt`. VS Code shows `�` where the six Lithuanian
   letters should be:

    ```text
    Labas! �iandien �ilta.
    � park� eisime p�s�iomis.
    ```

2. Read the size, as in section 7: 49 bytes for 49 characters.

3. Select `UTF-8` in the Status Bar, then **Reopen with Encoding**, and
   type:

    ```text
    1257
    ```

    Choose **Baltic (Windows 1257)**. The text reads right:

    ```text
    Labas! Šiandien šilta.
    Į parką eisime pėsčiomis.
    ```

4. Now change the bytes. Select `Windows 1257` in the Status Bar, then
   **Save with Encoding**, and choose **UTF-8**.

5. Measure again.

!!! success "You should now see"
    55 bytes. Each of `Š`, `š`, `Į`, `ą`, `ė`, `č` took one byte in
    Windows-1257 and takes two in UTF-8: 49 + 6 = 55.

!!! warning "Watch for"
    **Save with Encoding** was chosen while the text still showed `�`. The
    signs were saved instead of the letters, and the letters are lost. Take
    `labas.txt` from [`inbox_after.zip`](../data/inbox_after.zip).

**Say it in these words.** Reopen reads the same bytes with another table
and is safe. Save writes other bytes. Letters that turn into `�`, `Ä…` or
`Å¾` are not broken: they were read with the wrong table.

---

## Part 4 · What a file is { #part-4 }

**1:20 to 1:45 · sections 11 to 14**

The name of a file is a hint. The first bytes say what it is, and a hash
says whether two files are the same.

---

### 11. A picture called .txt { #magic }

**1:20 · 7 min**

**Tell the room.** The ending of a file name is a hint for people and
programs. The first bytes of the file say what it is.

1. Select `inbox/photo.txt` in the Side Bar. VS Code does not show it as
   text: the file is binary.

2. Look at its first bytes:

    === "macOS"

        ```text
        hexdump -C inbox/photo.txt
        ```

        ```text
        00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
        ```

        That is the first of ten rows of bytes. The line after them,
        `00000098`, is the size: 9 × 16 + 8 = 152.

    === "Windows"

        ```text
        Format-Hex inbox/photo.txt
        ```

        ```text
        0000000000000000 89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52 �PNG����   �IHDR
        ```

        That is the first row of ten.

3. `89 50 4E 47` is how every PNG picture begins: the right column shows
   `PNG`. Move it to `images` with its right name:

    ```text
    mv inbox/photo.txt inbox/images/photo.png
    ```

4. Select `inbox/images/photo.png` in the Side Bar.

!!! success "You should now see"
    A small picture, a yellow disc on blue, 32 × 32 pixels. The bytes did
    not change, only the name.

---

### 12. The same file? { #hash }

**1:27 · 8 min**

**Tell the room.** `expenses.csv` and `expenses_copy.csv` look alike and have
the same size. A hash is a short number computed from every byte of a file.
The same bytes give the same hash on every computer, and one changed byte
gives a hash that differs in every digit.

1. Compute both hashes:

    === "macOS"

        ```text
        shasum -a 256 inbox/tables/expenses.csv
        ```

        ```text
        shasum -a 256 inbox/tables/expenses_copy.csv
        ```

        ```text
        557539a31da6340be480bc37a00762dc3b83fe950c41de7e84a28d20eca0569e  inbox/tables/expenses.csv
        19889d51ad959ab42c63159fe2aaa7d00144285fd981bf4aaefdf2b72f4ac001  inbox/tables/expenses_copy.csv
        ```

    === "Windows"

        ```text
        (Get-FileHash inbox/tables/expenses.csv).Hash
        ```

        ```text
        (Get-FileHash inbox/tables/expenses_copy.csv).Hash
        ```

        ```text
        557539A31DA6340BE480BC37A00762DC3B83FE950C41DE7E84A28D20ECA0569E
        19889D51AD959AB42C63159FE2AAA7D00144285FD981BF4AAEFDF2B72F4AC001
        ```

    Lower case and upper case are the same digits.

2. Find where they differ. In the Side Bar select `expenses.csv`, then
   `expenses_copy.csv` with `Ctrl` (macOS `Cmd`) held, right-click, and
   select **Compare Selected**.

3. Line 4 differs: `6.50` against `6.60`. In the Hex Editor it is the byte
   in row `00000050`, column `06`: `35` against `36`.

!!! success "You should now see"
    One byte of 111 differs, and the two hashes have nothing in common.

---

### 13. Write it down { #notes }

**1:35 · 7 min**

**Tell the room.** The answers go into the folder, next to the files, in
Markdown.

1. Open `inbox/notes.md` and add at the end:

    ```text
    ## Answers

    - Not text: `photo.txt` is a PNG picture (`89 50 4E 47`),
      now `images/photo.png`
    - `labas.txt` was saved in Windows-1257. Now UTF-8, 55 bytes
    - The two tables differ in one byte: `6.50` against `6.60`
    ```

2. Open the preview with `Ctrl+K`, then `V` (macOS `Cmd+K`, then `V`).

!!! success "You should now see"
    Three answers under the three questions, in the preview.

---

### 14. Wrap up { #wrap-up }

**1:42 · 3 min**

Read the list aloud. Ask on the way out which step was hardest.

- The prompt says where the shell is. `pwd`, `ls` and `cd` look around;
  `mkdir`, `cp`, `mv` and `rm` change things, and `rm` cannot be undone.
- A space splits a name in two. Names without spaces need no quotes.
- A size in bytes is exact. `a` to `z` take one byte each, `ū` two in
  UTF-8, and a line break one byte or two.
- Reopening with another encoding is safe. Saving with another encoding
  writes other bytes.
- The first bytes say what a file is. A hash says whether two files are
  the same.

---

## Optional, if the room is fast { #optional }

---

### 15. Three bytes before the header { #bom }

**— · 8 min**

**Tell the room.** Some programs write three bytes, `EF BB BF`, before the
first character of a UTF-8 file: the byte-order mark, or BOM. VS Code shows
it in the Status Bar.

1. Open `inbox/tables/expenses.csv`. The Status Bar reads
   `UTF-8 with BOM`.

2. Open it with the Hex Editor. The first three bytes are `EF BB BF`, and
   `64 61 74 65`, `date`, follows.

3. The file has 108 characters and 111 bytes: 111 − 108 = 3.

4. Make a spare copy, and remove the BOM in the copy only:

    ```text
    cp inbox/tables/expenses.csv no_bom.csv
    ```

    Open `no_bom.csv`, select `UTF-8 with BOM` in the Status Bar,
    **Save with Encoding**, **UTF-8**. Measure it: 108 bytes.

!!! success "You should now see"
    `expenses.csv` with 111 bytes and `no_bom.csv` with 108.

---

### 16. A checksum by hand { #by-hand }

**— · 6 min**

**Tell the room.** The simplest check of a file adds up its bytes and keeps
the remainder after dividing by 256. It catches some changes and misses
others.

1. Make a file `abc.txt` in `files-lab` with the three letters `abc` and no
   line break. Measure it: 3 bytes.

2. In the Hex Editor: `61 62 63`, which are 97, 98 and 99. Add them up on
   the board: 294. 294 − 256 = 38.

3. Change the text to `abd`: the sum is 39, the change is caught. Change it
   to `acb`: the sum is 38 again, the change is missed.

4. Compare with SHA-256 of `abc` and `acb`, as in section 12. The two hashes
   start with `ba7816bf` and `8e976608`.

!!! success "You should now see"
    The same sum, 38, for `abc` and `acb`, and two different hashes.

---

### 17. An emoji { #emoji }

**— · 6 min**

1. Open `abc.txt`, put the cursor at the end, and add an emoji: `Win+.`
   (macOS `Ctrl+Cmd+Space`), then 😀. Save.

2. Measure the file and open it with the Hex Editor.

!!! success "You should now see"
    7 bytes: `61 62 63 F0 9F 98 80`. The emoji takes four bytes in UTF-8.

---

## Stretch goals

For students who finish a section early. Answers are given for the lecturer.

- Predict the size of `notes.md` after section 13 before measuring it. The
  answer depends on the exact text; count the characters of the new lines,
  and add one byte per line break.
- In `labas.txt`, which line holds more bytes in UTF-8? Line 2: it has four
  of the six Lithuanian letters, `Į`, `ą`, `ė`, `č`.
- `photo.png` has 152 bytes for 32 × 32 pixels of 3 bytes each, which are
  3072 bytes. Ask where the rest went. PNG compresses without loss: the
  picture is two colours in large areas.

## If students ask for more

| Topic | Lecture |
|--|--|
| More commands: reading, counting and searching inside files | 4 (Command Line) |
| Checksums for a whole folder, and backups | 4 (Command Line) |
| Reading a file in Python with a given encoding | 7 (Python for Data & NumPy) |

## Aims practised

📁 a folder tidied and every file known at the byte level · 🔧 the same
commands in zsh and in PowerShell · ♻️ the answers written next to the files
