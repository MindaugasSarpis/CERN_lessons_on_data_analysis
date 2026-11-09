# Seminar 11 · A Language Model by Hand

**Paired lecture:** 11 From Neurons to Language Models · **Format:** type-along tutorial, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** What does a language model do with a prompt?

**Today's goal:** every student builds a language model in plain Python from
the station's twelve months in words: it counts which word follows which,
turns the counts into next-word probabilities and writes sentences with
them; turns three scores into probabilities at a temperature; then asks a
chat model to explain a function of `weather.py` and to write a test for it,
runs the test, and writes down where the model was used.

Everything is typed in VS Code: the scripts in the editor, the commands in
its terminal (zsh on macOS, Git Bash on Windows; the lines are the same in
both). In the blocks, a line that starts with `$` is typed in the terminal,
a line that starts with `>>>` is typed at Python's prompt, and every other
line is what comes back; `...` stands for lines left out. Today needs no new
package: plain Python, and a chat model in the browser.

**If time runs short:** skip the Tasks, but keep section 9, the test of a
chat model's answer, and section 11, your project.

??? info "Before the session"
    - **Room:** Miniforge and VS Code with its Python extension on every
      laptop (the [Setup](../setup.md) page), internet for the download
      (0.6 MB) and for a chat model in the browser.
    - **A chat model:** any chat model on a free account works (for
      example ChatGPT, Claude, Gemini, Copilot). A student without one
      works with a neighbour, or follows the lecturer's screen.
    - **You:** a student who has the environment `analysis` of Seminars 8
      to 10 uses it; one who has not makes it in section 1 (Python,
      Matplotlib and pandas). Today's code needs Python alone.
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.

---

## Part 1 · Today's folder and today's text { #part-1 }

<!-- 0:00 to 0:15 -->

The weather log becomes text: one sentence for each month, written by a script from the month's mean temperature.

---

### 1. Get today's folder, switch on the environment { #start }

<!-- 0:00 · 10 min -->

Today's folder holds the data, the module `weather.py`, a script that writes today's text, and `environment.yml`.

1. On the [Releases page](https://github.com/MindaugasSarpis/weather-project/releases),
   under **Assets**, click `weather-s11.zip`. Open VS Code, then the
   terminal (**View** > **Terminal**), and unzip it into the home folder.

    ```text
    $ unzip ~/Downloads/weather-s11.zip -d ~
    Archive:  /Users/smilte/Downloads/weather-s11.zip
       creating: /Users/smilte/weather-s11/
    ...
      inflating: /Users/smilte/weather-s11/scripts/weather.py
    $ cd ~/weather-s11
    $ ls
    README.md  data  environment.yml  results  scripts
    ```

    Safari unpacks a zip by itself: then `mv ~/Downloads/weather-s11 ~`
    instead.

2. **File** > **Open Folder...** > `weather-s11` > **Open**. The window
   reloads: open the terminal again (**View** > **Terminal**); it starts in
   the folder.

3. Look for the environment of the last weeks.

    ```text
    $ conda env list
    ...
    analysis                 /Users/smilte/miniforge3/envs/analysis
    ...
    ```

    `analysis` in the list: switch it on, `conda activate analysis`, and go
    to step 4. Not in the list: make it from the folder's file first.

    ```text
    $ cat environment.yml
    name: analysis
    channels:
      - conda-forge
    dependencies:
      - python=3.14
      - matplotlib-base=3.11
      - pandas=3.1
    $ conda env create -f environment.yml
    ...
    $ conda activate analysis
    ```

4. VS Code too: `Ctrl+Shift+P` (macOS `Cmd+Shift+P`), `Python: Select
   Interpreter`, pick the entry with `envs/analysis` in its path.

5. Ask for Python's version.

    ```text
    $ python --version
    Python 3.14.10
    ```

**Check:** `(analysis)` at the start of the prompt, and `Python 3.14` (the
last number may differ).

---

### 2. Write today's text from the log { #text }

<!-- 0:10 · 5 min -->

A script writes one sentence per month: the word comes from the month's mean temperature.

1. Run the script that came with the folder.

    ```text
    $ python scripts/sentences.py
    12 sentences in data/processed/months.txt
    120 sentences in data/processed/months_by_year.txt
    ```

2. Print the first file: the twelve months, each over the ten years
   2016 to 2025.

    ```text
    $ cat data/processed/months.txt
    in january it was cold .
    in february it was cold .
    in march it was cool .
    in april it was cool .
    in may it was mild .
    in june it was warm .
    in july it was warm .
    in august it was warm .
    in september it was mild .
    in october it was cool .
    in november it was cool .
    in december it was cold .
    ```

    The full stop stands apart, with a space before it, so that it counts as
    a word of its own.

3. Open `scripts/weather.py` and find its last function, `word_for`. It
   gives the word for a mean temperature: below 0 °C `cold`, below 10 °C
   `cool`, below 15 °C `mild`, else `warm`. `sentences.py` uses it with
   `group`, the function above it, which collects the temperatures of each
   month in a dictionary of lists.

**Check:** twelve lines in `months.txt`, the seventh `in july it was warm .`

---

## Part 2 · A language model by counting { #part-2 }

<!-- 0:15 to 1:05 -->

The simplest language model reads a text, counts which word follows which, and continues a text by drawing from the counts.

---

### 3. Split a sentence into words { #split }

<!-- 0:15 · 10 min -->

A **list of words** is the text as a program sees it: `split()` cuts a text at every space and line break.

1. Start Python in the terminal and split one sentence.

    ```pycon
    >>> sentence = "in july it was warm ."
    >>> words = sentence.split()
    >>> words
    ['in', 'july', 'it', 'was', 'warm', '.']
    >>> len(words)
    6
    >>> words[0]
    'in'
    >>> words[3]
    'was'
    >>> words[4]
    'warm'
    ```

    `words[3]` is the fourth word: the positions start at 0.

2. Each word with the word after it: `i` runs over the positions 0 to 4,
   and `words[i + 1]` is the next word.

    ```pycon
    >>> for i in range(len(words) - 1):
    ...     print(words[i], words[i + 1])
    ...
    in july
    july it
    it was
    was warm
    warm .
    >>> exit()
    ```

    `range(len(words) - 1)` gives 0, 1, 2, 3, 4: the last word has nothing
    after it. Press `Enter` on the empty `...` line to run the loop.

**Check:** five pairs, the fourth `was warm`.

---

### 4. Count which word follows which { #count }

<!-- 0:25 · 15 min -->

A **dictionary of lists**: one key per word, and under it every word that came right after it in the text.

1. New file `scripts/next_word.py`. Type, save.

    ```python
    text = open("data/processed/months.txt").read()
    words = text.split()
    print(len(words), words[0:6])
    ```

2. Run it from the project folder.

    ```text
    $ python scripts/next_word.py
    72 ['in', 'january', 'it', 'was', 'cold', '.']
    ```

    Twelve sentences of six words: 72 words.

3. Under the three lines, add the counting, save.

    ```python
    follow = {}
    for i in range(len(words) - 1):
        word = words[i]
        if word not in follow:
            follow[word] = []
        follow[word].append(words[i + 1])
    print(follow["in"])
    print(follow["was"])
    ```

    These are the four lines of `group` in `weather.py`: the first time a
    word turns up, `follow[word] = []` gives it an empty list; `append` adds
    the word that came after it.

4. Run it.

    ```text
    $ python scripts/next_word.py
    72 ['in', 'january', 'it', 'was', 'cold', '.']
    ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    ['cold', 'cold', 'cool', 'cool', 'mild', 'warm', 'warm', 'warm', 'mild', 'cool', 'cool', 'cold']
    ```

    After `in` came each month once; after `was`, the twelve weather words
    in the order of the months.

**Check:** `follow["was"]` holds twelve words: three `cold`, four `cool`,
two `mild`, three `warm`.

---

### 5. From counts to probabilities { #odds }

<!-- 0:40 · 10 min -->

The probability of a next word is its count divided by the count of all words that came after: 4 of 12 for `cool`.

1. At the end of `next_word.py`, add these lines, save.

    ```python
    after = follow["was"]
    for word in ["cold", "cool", "mild", "warm"]:
        print(word, after.count(word), round(after.count(word) / len(after), 3))
    ```

    `after.count(word)` counts how often `word` stands in the list;
    `round(x, 3)` keeps three decimals.

2. Run it.

    ```text
    $ python scripts/next_word.py
    ...
    cold 3 0.25
    cool 4 0.333
    mild 2 0.167
    warm 3 0.25
    ```

    The four probabilities add up to 1. This table, a word in and a
    probability for each next word out, is a language model.

**Check:** `cool 4 0.333`.

---

### 6. Write sentences with the model { #generate }

<!-- 0:50 · 15 min (Task: 5 min, skip if late) -->

The model writes by drawing: from the list of the last word it picks the next one, appends it, and goes on until the full stop.

1. Make `import random` the first line of `next_word.py`: `random` comes
   with Python and draws at random.

    ```python
    import random

    text = open("data/processed/months.txt").read()
    ...
    ```

2. At the end of the file, add these lines, save.

    ```python
    random.seed(78)
    for n in range(5):
        word = "in"
        sentence = [word]
        while word != ".":
            word = random.choice(follow[word])
            sentence.append(word)
        print(" ".join(sentence))
    ```

    `random.choice` picks one element of a list, each equally likely: `cool`
    stands four times in `follow["was"]`, so it comes with 4 of 12. `while`
    repeats its block as long as its condition holds, here until the word is
    the full stop. `" ".join(sentence)` puts the words together with a space
    between them. `random.seed(78)` makes every laptop draw the same.

3. Run it.

    ```text
    $ python scripts/next_word.py
    ...
    in april it was cool .
    in december it was cool .
    in november it was cool .
    in july it was cold .
    in june it was cool .
    ```

4. Compare with `months.txt`: two of the five sentences are in the text,
   `april` and `november`. The model wrote `in july it was cold .`: after
   `was` it sees `was` alone, and three times in twelve `cold` followed it.

**Check:** five sentences, every one grammatical, three of them false.

!!! question "Task: how often is the model right?"
    Draw 1000 sentences and count those that are in the text. Hint:
    `text.splitlines()` gives the list of the twelve lines, and `x in a_list`
    is `True` when `x` is in the list.

??? success "Answer"
    At the end of `next_word.py`:

    ```python
    lines = text.splitlines()
    true = 0
    for n in range(1000):
        word = "in"
        sentence = [word]
        while word != ".":
            word = random.choice(follow[word])
            sentence.append(word)
        if " ".join(sentence) in lines:
            true = true + 1
    print(true, "of 1000 are in the text")
    ```

    ```text
    $ python scripts/next_word.py
    ...
    285 of 1000 are in the text
    ```

    About one in four. On average 38 of 144: a month is drawn with 1/12,
    its own word with 3, 4, 2 or 3 of 12. The other sentences are fluent and
    false: the counts know which word follows which, not which month was
    warm.

---

## Part 3 · Scores into probabilities { #part-3 }

<!-- 1:05 to 1:15 -->

A large model gives every possible next word a score. Softmax turns the scores into probabilities; a temperature makes them sharper or flatter.

---

### 7. Softmax, then with a temperature { #softmax }

<!-- 1:05 · 10 min (Task: 3 min, skip if late) -->

Softmax: e to the power of each score, divided by the sum of these powers. `math.exp(z)` computes e to the power `z`.

1. At Python's prompt, three scores: 2.0 for `warm`, 1.0 for `mild`, 0.1
   for `cool`.

    ```pycon
    >>> import math
    >>> math.exp(2.0)
    7.38905609893065
    >>> math.exp(1.0)
    2.718281828459045
    >>> math.exp(0.1)
    1.1051709180756477
    >>> total = math.exp(2.0) + math.exp(1.0) + math.exp(0.1)
    >>> total
    11.212508845465344
    >>> math.exp(2.0) / total
    0.6590011388859679
    >>> round(math.exp(1.0) / total, 3)
    0.242
    >>> round(math.exp(0.1) / total, 3)
    0.099
    >>> exit()
    ```

    Every power is positive, and dividing by their sum makes the three
    numbers add up to 1: 0.659, 0.242, 0.099.

2. As a function with a temperature `T`: each score is divided by `T`
   first. New file `scripts/softmax.py`. Type, save.

    ```python
    import math


    def softmax(scores, T):
        e = []
        for z in scores:
            e.append(math.exp(z / T))
        total = sum(e)
        p = []
        for x in e:
            p.append(round(x / total, 3))
        return p


    scores = [2.0, 1.0, 0.1]          # warm, mild, cool
    for T in [0.5, 1, 2]:
        print(T, softmax(scores, T))
    ```

3. Run it.

    ```text
    $ python scripts/softmax.py
    0.5 [0.864, 0.117, 0.019]
    1 [0.659, 0.242, 0.099]
    2 [0.502, 0.304, 0.194]
    ```

    A low temperature gives the top word more (0.864); a high one spreads
    the probability (0.502). A chat model draws each word of its reply at a
    temperature: the same prompt can get a different reply.

**Check:** `1 [0.659, 0.242, 0.099]`, the numbers of step 1.

!!! question "Task: very low and very high"
    Change the list of temperatures to `[0.1, 10]`. What does the model
    write at each?

??? success "Answer"
    ```text
    $ python scripts/softmax.py
    0.1 [1.0, 0.0, 0.0]
    10 [0.366, 0.331, 0.303]
    ```

    At 0.1 the top word every time; at 10 nearly a third each, the scores
    hardly matter. Put the list back to `[0.5, 1, 2]`.

---

## Part 4 · A chat model, checked by running { #part-4 }

<!-- 1:15 to 1:40 -->

A chat model writes the likely text after the prompt, fluent whether it is right or not. Its answer about code is checked by running the code.

---

### 8. Ask a chat model to explain a function { #explain }

<!-- 1:15 · 10 min -->

The prompt gives the model what it cannot know: the code itself and what you want back.

1. Open a chat model in the browser. Copy the function `word_for` from
   `scripts/weather.py` into this prompt, and send it.

    ```text
    I am learning Python. Explain line by line what this function does,
    and say what it returns for -3.9, 0, 10 and 18.5:

    def word_for(temp):
        """The word for a mean temperature in °C."""
        if temp < 0:
            return "cold"
        if temp < 10:
            return "cool"
        if temp < 15:
            return "mild"
        return "warm"
    ```

2. Read the reply. Your reply differs from your neighbour's: the model
   draws its words. Look at what it says about 0 and 10, the values on a
   border.

3. Check its four answers by running them. Python finds `weather.py` in the
   terminal's folder, so start it in `scripts`.

    ```text
    $ cd scripts
    $ python
    ```

    ```pycon
    >>> import weather
    >>> weather.word_for(-3.9)
    'cold'
    >>> weather.word_for(0)
    'cool'
    >>> weather.word_for(10)
    'mild'
    >>> weather.word_for(18.5)
    'warm'
    >>> exit()
    ```

    ```text
    $ cd ..
    ```

    0 is not below 0, so it is `cool`; 10 is not below 10, so it is `mild`.

**Check:** the reply's four answers against `cold`, `cool`, `mild`, `warm`.
Where they differ, the run is right.

---

### 9. Ask for a test, then run it { #test }

<!-- 1:25 · 13 min (Task: 5 min, skip if late) -->

A **test** states facts known without the code and checks them: `assert` stops the script with an `AssertionError` when its condition is false.

1. In the same chat, send this prompt.

    ```text
    Write a test for word_for in a file test_weather.py: plain Python,
    no pytest, `import weather` at the top, one assert per value, and
    print("all tests passed") at the end. Test the borders 0, 10 and 15,
    and one value inside each of the four ranges.
    ```

2. New file `scripts/test_weather.py`: paste the code of the reply, save.
   It should look like this one; yours may test other values. If it has
   no test of 0, add the line `assert weather.word_for(0) == "cool"`.

    ```python
    import weather

    assert weather.word_for(-3.9) == "cold"
    assert weather.word_for(0) == "cool"
    assert weather.word_for(9.9) == "cool"
    assert weather.word_for(10) == "mild"
    assert weather.word_for(14.9) == "mild"
    assert weather.word_for(15) == "warm"
    assert weather.word_for(18.5) == "warm"
    print("all tests passed")
    ```

3. Run it from the project folder.

    ```text
    $ python scripts/test_weather.py
    all tests passed
    ```

    An `AssertionError` instead names the line that failed. Read that
    value, find its word by the rule of section 2, and decide who is wrong:
    the test or the function.

4. A test must fail on a wrong function. In `weather.py`, change
   `if temp < 0:` to `if temp <= 0:`, save, run the test again. The
   traceback names the line that tests 0, line 4 in the file above.

    ```text
    $ python scripts/test_weather.py
    Traceback (most recent call last):
      File "/Users/smilte/weather-s11/scripts/test_weather.py", line 4, in <module>
        assert weather.word_for(0) == "cool"
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
    ```

    The test caught the changed border. Put `<` back, save, run: `all tests
    passed`.

5. A test can be wrong too. The four measured hours of 21 July 2019 have
   the mean 25.275, worked out by hand. Start Python in `scripts` again.

    ```pycon
    >>> import weather
    >>> weather.mean([27.3, 25.6, 24.6, 23.6])
    25.275000000000002
    >>> weather.mean([27.3, 25.6, 24.6, 23.6]) == 25.275
    False
    >>> round(weather.mean([27.3, 25.6, 24.6, 23.6]), 3) == 25.275
    True
    >>> exit()
    ```

    The function is right; the decimals are not exact in binary, so `==`
    fails. A test of a float compares the rounded value.

6. Write down where the chat model was used. At the end of `README.md`, add
   these lines with your tool and today's date, save.

    ```text
    ## Use of AI tools

    scripts/test_weather.py was drafted with <the chat model> on
    15 December 2026 and checked by running it, also against a word_for
    with a changed border, which it caught.
    ```

**Check:** `all tests passed`, the `AssertionError` with `<=`, and the note
at the end of the README.

!!! question "Task: a question only the data can answer"
    Ask the chat model: *How many hours of my weather log are below 0 °C?*
    Then count them in Python: `weather.temps("../data/raw/weather.csv")` in
    `scripts` gives every measured temperature.

??? success "Answer"
    The model has not seen the file: a number in its reply is a guess, or it
    asks for the file. The data answer it:

    ```pycon
    >>> import weather
    >>> temps = weather.temps("../data/raw/weather.csv")
    >>> count = 0
    >>> for t in temps:
    ...     if t < 0:
    ...         count = count + 1
    ...
    >>> count
    22352
    >>> len(temps)
    87552
    ```

    22 352 of the 87 552 measured hours. A statement about your data is
    computed from the data.

---

### 10. Wrap up { #wrap-up }

<!-- 1:38 · 2 min -->

The lines of today, by what they do.

| To | Type |
|--|--|
| cut a text into words | `text.split()` |
| collect what follows each word | `follow[word].append(words[i + 1])`, as `group` does |
| count and divide | `after.count(word) / len(after)` |
| draw a word | `random.choice(a_list)`, after `random.seed(78)` |
| join words into a text | `" ".join(sentence)` |
| softmax | `math.exp(z / T)` for each score, divided by their sum |
| test | `assert condition`, then run the file |

---

## Part 5 · Your project { #part-5 }

<!-- 1:40 to 2:00 -->

The same steps on your own code: an explanation, a test you run, and a note in the README.

---

### 11. A test for one function of your project { #project }

<!-- 1:40 · 20 min -->

Nothing new: sections 8 and 9 with your file names. Skip it if your project has no code yet, or take a few lines of your notebook.

1. Open your project folder in VS Code (**File** > **Open Folder...**) and
   pick one short function, or a few lines that compute one number.

2. Ask the chat model to explain it. Give it what it cannot know: what your
   data are, the columns and their units, the mark for a missing value.
   Paste your code, never your data's personal details, a password, or
   someone else's unpublished results.

3. Work out one answer by hand: a small input whose result you know, such
   as the four hours of section 9 for a mean.

4. Ask it for a test in plain Python with that input, save it in your
   `scripts` folder, and run it. Then change one detail of the function on
   purpose: the test must fail. Put it back.

5. Add the note of section 9, step 6, to your project's `README.md`: which
   tool, the date, what for, how it was checked. If your project is a Git
   repository, commit both files.

    ```text
    $ git add scripts README.md
    $ git commit -m "Test one function; note the use of a chat model"
    ```

**Check:** a test that passes, fails on a changed function, and a README
that says where a chat model was used.

---

## Optional, if the room goes fast { #optional }

---

### 12. The ten years as text { #ten-years }

<!-- — · 10 min -->

`months_by_year.txt` holds a sentence for each of the 120 months: the weather of single months, not of the ten-year means.

1. In the first lines of `next_word.py`, read the other file.

    ```python
    text = open("data/processed/months_by_year.txt").read()
    ```

2. Run it. The two lists now hold 120 words each, left out here.

    ```text
    $ python scripts/next_word.py
    720 ['in', 'january', 'it', 'was', 'cold', '.']
    ...
    cold 29 0.242
    cool 40 0.333
    mild 22 0.183
    warm 29 0.242
    in september it was cool .
    in december it was mild .
    in july it was cold .
    in november it was cool .
    in november it was cool .
    ```

    Lines of a Task left in `next_word.py` print theirs too. Ten Januaries:
    nine cold, one cool (2018, 0.2 °C). July was warm in every year, and the
    model still writes `in july it was cold .`

**Check:** `cold 29 0.242`. Put `months.txt` back in the first lines.

---

### 13. Months as vectors { #vectors }

<!-- — · 15 min -->

A month described by four numbers: how often each weather word came with it in the 120 sentences. Months used alike get similar lists, from the text alone.

1. New file `scripts/vectors.py`. Type, save, run.

    ```python
    import math

    counts = {}
    for line in open("data/processed/months_by_year.txt").read().splitlines():
        parts = line.split()
        month = parts[1]
        word = parts[4]
        if month not in counts:
            counts[month] = {"cold": 0, "cool": 0, "mild": 0, "warm": 0}
        counts[month][word] = counts[month][word] + 1
    print(counts["january"])
    print(counts["july"])
    ```

    ```text
    $ python scripts/vectors.py
    {'cold': 9, 'cool': 1, 'mild': 0, 'warm': 0}
    {'cold': 0, 'cool': 0, 'mild': 0, 'warm': 10}
    ```

2. The **dot product** multiplies the numbers in the same places and adds
   them up; divided by the lengths of the two lists it gives the
   **cosine**: 1 for the same direction, 0 for nothing in common. Add these
   lines, save, run.

    ```python
    def vector(month):
        return list(counts[month].values())


    def dot(a, b):
        total = 0
        for i in range(len(a)):
            total = total + a[i] * b[i]
        return total


    def cosine(a, b):
        return dot(a, b) / math.sqrt(dot(a, a) * dot(b, b))


    january = vector("january")
    for month in ["february", "march", "july", "december"]:
        print(month, vector(month), round(cosine(january, vector(month)), 3))
    ```

    ```text
    $ python scripts/vectors.py
    ...
    february [10, 0, 0, 0] 0.994
    march [1, 9, 0, 0] 0.22
    july [0, 0, 0, 10] 0.0
    december [9, 1, 0, 0] 1.0
    ```

**Check:** January and December, 1.0; January and July, 0.0.

---

### 14. The probabilities as a bar chart { #chart }

<!-- — · 10 min -->

The table of section 5 as a figure, with Matplotlib, which the environment `analysis` holds.

1. Under `import random` in `next_word.py`, add
   `import matplotlib.pyplot as plt`. At the end of the file, add these
   lines, save, run.

    ```python
    names = ["cold", "cool", "mild", "warm"]
    probs = []
    for word in names:
        probs.append(after.count(word) / len(after))
    fig, ax = plt.subplots()
    ax.bar(names, probs)
    ax.set_ylabel("Probability after “was”")
    ax.set_title("Cool comes after “was” 4 times in 12")
    fig.savefig("results/next_word.png", dpi=150)
    ```

2. Open `results/next_word.png`: four bars, the tallest `cool` at 0.333.

**Check:** the bars at 0.25, 0.333, 0.167 and 0.25.

---

## Aims practised

- ♻️ **Reproducibility:** `random.seed` makes every laptop draw the same
  sentences; a chat cannot be run again, so its code goes into a file with
  a test.
- 📁 **Files:** today's text is written by a script from the raw log; the
  README says where a chat model was used.
- 🔧 **Tool-agnosticism:** a language model built from a dictionary and a
  loop, the same counting as `group`; any chat model, checked the same way.
