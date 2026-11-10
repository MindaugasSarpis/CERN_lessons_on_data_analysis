# Seminar 11 · A Language Model by Hand

**Paired lecture:** 11 From Neurons to Language Models · **Format:** a showcase, then a problem, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** What does a language model do with a prompt, and does a longer one always help?

The lecturer runs Part 2 from this page; in Part 3 the room works in pairs.
Everything is typed in VS Code: the scripts in the editor, the commands in its
terminal (zsh on macOS, Git Bash on Windows; the same lines in both). A line
that starts with `$` is typed without the `$`; `...` stands for lines left out.
A chat LLM runs in the browser beside it.

**If time runs short:** leave out section 4 (the drawn names and the loss); section 5 draws names too.

??? info "Before the session"
    - **Room:** Miniforge and VS Code with its Python extension on every
      laptop (the [Setup](../setup.md) page), internet for the data and for
      a chat LLM; for conda only on a laptop without `analysis` (Python,
      pandas and Matplotlib, about 100 MB on a Mac and 220 MB on Windows).
    - **No file is handed out.** The scripts fetch two public text files
      when they run, the first unchanged since 2022, the second since 2015:
        - `names.txt`, 32 033 first names, one per line (228 kB), from
          Andrej Karpathy's [makemore](https://github.com/karpathy/makemore)
          repository, MIT licence: "the most common 32K names taken from
          ssa.gov for the year 2018", the baby-name list of the US Social
          Security Administration;
        - `input.txt`, 40 000 lines of Shakespeare's plays (1.1 MB), from
          his [char-rnn](https://github.com/karpathy/char-rnn) repository,
          MIT licence; the plays are in the public domain.
    - **The numbers** on this page come from runs on 10 November 2026; with
      the same files and `random.seed`, every laptop prints the same.
    - **A chat LLM:** any chat LLM in the browser on a free account (for
      example ChatGPT, Claude, Gemini or Copilot). The page shows no reply
      of a chat: replies differ from chat to chat and from day to day. A
      student without one works with a neighbour who has one, or follows
      the lecturer's screen. Nothing personal goes into a prompt.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` (Miniforge): [Setup, steps 2–4](../setup.md#shell); the Python
      extension: [Setup, step 7](../setup.md#extensions).
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.

---

## Part 1 · Set up { #part-1 }

### 1. A new folder and the environment `analysis` { #start }

<!-- 0:00 · 6 min -->

Today needs no new package: Python counts and draws, and Matplotlib from `analysis`, the environment of weeks 8 to 12, draws the figures.

1. In VS Code, **View** > **Terminal**. Make the folder and go into it.

    ```text
    $ mkdir ~/weather-s11
    $ cd ~/weather-s11
    $ pwd
    /Users/smilte/weather-s11
    ```

2. **File** > **Open Folder...** > `weather-s11` (in your home folder) >
   **Open**, then **View** > **Terminal**. The Explorer on the left is empty.

3. Switch on `analysis`.

    ```text
    $ conda activate analysis
    ```

    `EnvironmentNameNotFound`: this laptop does not have it yet. Make it
    with one line (at `Proceed ([y]/n)?` press `Enter`), then switch it on.

    ```text
    $ conda create -n analysis python=3.14 pandas=3.1 matplotlib-base=3.11
    ...
    #     $ conda activate analysis
    $ conda activate analysis
    ```

4. Ask for Matplotlib's version.

    ```text
    $ python -c "import matplotlib; print(matplotlib.__version__)"
    3.11.2
    ```

**Check:** `(analysis)` at the start of the prompt, and `3.11.2` (the last digit may be higher).

---

### 2. Write the environment down, open a chat { #chat }

<!-- 0:06 · 4 min -->

`environment.yml` in today's folder records what today's scripts ran with.

1. Write the environment into a file.

    ```text
    $ conda env export --from-history -f environment.yml
    ```

2. Click `environment.yml` in the Explorer, delete its last line,
   `prefix: ...` (a folder on this laptop), save (`Ctrl+S`, macOS `Cmd+S`).
   The packages may stand in another order, and a package you added in an
   earlier week stands there too.

    ```text
    name: analysis
    channels:
      - conda-forge
    dependencies:
      - python=3.14
      - pandas=3.1
      - matplotlib-base=3.11
    ```

3. Tell VS Code which Python to use: `Ctrl+Shift+P` (macOS `Cmd+Shift+P`),
   `Python: Select Interpreter`, pick the entry with `envs/analysis` in its
   path.

4. Open a chat LLM in the browser and start a new chat.

**Check:** `analysis` in the Status Bar, no `prefix:` in `environment.yml`, an empty chat.

---

## Part 2 · Showcase { #part-2 }

The lecturer runs four complete scripts on two real texts; the room watches
or types along, and sends the same questions to a chat LLM. For each script:
in the Explorer, right-click > **New File...**, the name above the code,
paste, save, run it in the terminal.

### 3. Which letter follows which in 32 033 names { #count }

<!-- 0:10 · 9 min -->

The simplest language model counts: for each letter, how often each letter came right after it; a count divided by the row's total is the probability of the next letter.

Before running it, ask the chat: *In US first names, which letters follow the letter q, and how often?* Write its answer down.

```python title="next_letter.py"
import urllib.request
from collections import Counter

URL = "https://raw.githubusercontent.com/karpathy/makemore/master/names.txt"
with urllib.request.urlopen(URL) as response:
    names = response.read().decode().split()
print(len(names), "names:", names[:5])

pairs = Counter()                # (letter, next letter) -> how often
for name in names:
    word = "." + name + "."      # "." marks the start and the end
    for a, b in zip(word, word[1:]):
        pairs[a, b] += 1
print(sum(pairs.values()), "pairs of neighbours,", len(pairs), "different")

after_q = Counter()
for (a, b), n in pairs.items():
    if a == "q":
        after_q[b] = n
total = after_q.total()
for b, n in after_q.most_common(5):
    print(f"after q: {b}  {n:3} of {total}  P = {n / total:.3f}")
```

```text
$ python next_letter.py
32033 names: ['emma', 'olivia', 'ava', 'isabella', 'sophia']
228146 pairs of neighbours, 627 different
after q: u  206 of 272  P = 0.757
after q: .   28 of 272  P = 0.103
after q: a   13 of 272  P = 0.048
after q: i   13 of 272  P = 0.048
after q: w    3 of 272  P = 0.011
```

**Notice:** the table holds only what the file holds: after `q`, `u` in 206 of 272 cases, and the end of the name (`.`) in 28.

**Ask the room:** the chat answered from the text it was trained on. Set its answer beside these counts: where do they differ, and which of the two describes this file?

??? note "Answer"
    The counts describe the file. In English words `q` is followed by `u`
    almost always, and a chat that has not seen the file continues with
    what is likely in general. These names come from many languages:
    `tariq` and `ishaq` end in `q`, `qiana` has `i` after it. A statement
    about a file is computed from the file.

---

### 4. New names drawn from the counts, and their loss { #draw }

<!-- 0:19 · 10 min -->

The model writes by drawing each next letter with the probabilities of its row, until the end mark; the **loss**, the mean of −ln p of the letter that really came, says how well the table predicts the names.

```python title="draw.py"
import math
import random
import urllib.request
from collections import Counter

URL = "https://raw.githubusercontent.com/karpathy/makemore/master/names.txt"
with urllib.request.urlopen(URL) as response:
    names = response.read().decode().split()
follow = {}                      # letter -> Counter of the letters after it
for name in names:
    word = "." + name + "."
    for a, b in zip(word, word[1:]):
        follow.setdefault(a, Counter())[b] += 1

random.seed(3)
for i in range(8):
    name, letter = "", "."
    while True:                  # draw the next letter until "." ends it
        row = follow[letter]
        letter = random.choices(list(row), weights=list(row.values()))[0]
        if letter == ".":
            break
        name += letter
    print(name + (" (in the list)" if name in names else ""))

loss = 0                         # the mean of -ln P(the letter that came)
n = 0
for name in names:
    word = "." + name + "."
    for a, b in zip(word, word[1:]):
        loss -= math.log(follow[a][b] / follow[a].total())
        n += 1
print(f"loss {loss / n:.3f}; letters drawn blindly: {math.log(27):.3f}")
```

```text
$ python draw.py
s
min (in the list)
ee
sbrul
anireyntarlereeyonieitellden
ge
zimeitcorsuoosoyar
jynielau
loss 2.454; letters drawn blindly: 3.296
```

Then the same request in the chat: *Invent eight new first names in the style of US baby names. Only the names, one per line.*

**Notice:** each pair of neighbours in `sbrul` stands somewhere in the names; the whole is no name, because the model looks one letter back.

**Ask the room:** the loss is 2.454; drawing each of the 27 symbols blindly scores ln 27 = 3.296. How many equally likely letters does each number stand for?

??? note "Answer"
    e^2.454 = 11.6: the table predicts as if choosing among about 12
    equally likely letters; blind, among 27. The
    [makemore README](https://github.com/karpathy/makemore) reports about
    1.92 for a small transformer trained on the same file, on names it had
    not seen: e^1.92 = 6.8 letters. A network that sees all the letters
    so far guesses better; a chat LLM is a very large network of that
    kind, which is why its names look like names.

---

### 5. The same counts at three temperatures { #temperature }

<!-- 0:29 · 9 min -->

Softmax of the scores ln(count) at a temperature T gives each count the weight count^(1/T): T = 1 gives back the counts, T = 0.5 squares them, T = 2 takes their square root.

```python title="temperature.py"
import random
import urllib.request
from collections import Counter
import matplotlib.pyplot as plt

URL = "https://raw.githubusercontent.com/karpathy/makemore/master/names.txt"
with urllib.request.urlopen(URL) as response:
    names = response.read().decode().split()
follow = {}
for name in names:
    word = "." + name + "."
    for a, b in zip(word, word[1:]):
        follow.setdefault(a, Counter())[b] += 1


def new_name(T):
    """Each letter drawn with the weights count ** (1 / T): softmax at T."""
    name, letter = "", "."
    while True:
        row = follow[letter]
        weights = [n ** (1 / T) for n in row.values()]
        letter = random.choices(list(row), weights=weights)[0]
        if letter == ".":
            return name
        name += letter


random.seed(1)
after_a = follow["a"].most_common()     # largest count first: ".", the end
fig, ax = plt.subplots(figsize=(9, 4), layout="constrained")
for T in [0.5, 1, 2]:
    weights = [n ** (1 / T) for b, n in after_a]
    p = [w / sum(weights) for w in weights]
    ax.plot([b for b, n in after_a], p, "o-", label=f"T = {T}")
    print(f"T = {T}: P(end after a) = {p[0]:.3f};",
          " ".join(new_name(T) for i in range(5)))
ax.set_xlabel("The letter after “a” (“.” ends the name)")
ax.set_ylabel("Probability")
ax.set_title("After “a”, T = 0.5 ends the name twice as often as T = 1")
ax.legend(frameon=False)
fig.savefig("temperature.svg")
```

```text
$ python temperature.py
T = 0.5: P(end after a) = 0.396; ana mana en klan da
T = 1: P(end after a) = 0.196; eny siabrabe la jan yr
T = 2: P(end after a) = 0.101; m kwecki xzusamrarockayssenn epkh inb
```

![The probability of each of the 27 symbols after the letter a, sorted from the most common, at three temperatures: at T = 0.5 the end of the name rises to 0.396 and n to 0.27, the rare letters fall to near 0; at T = 1 the counts, 0.196 for the end; at T = 2 the curve is flatter, 0.101 for the end and about 0.01 for the rarest letters](img/s11/temperature.svg)

**Notice:** a low T gives the likely symbols more, the end of the name among them, so names come out short (`ana`, `mana`, `en`); a high T gives the rare letters more, and names run long.

**Ask the room:** as T goes to 0, the model takes the most likely letter at every step. Which name does it write?

??? note "Answer"
    Change the loop's line to `for T in [0.05]:` and run it:

    ```text
    $ python temperature.py
    T = 0.05: P(end after a) = 0.982; a a a a a
    ```

    The name `a`, every time: `a` is the most likely first letter, and
    after `a` the end. No name in the list has fewer than two letters: the
    most likely step at every point does not give a likely name. Large
    models that always take the most likely token tend to repeat
    themselves too; chat models draw at a temperature above 0.

---

### 6. Shakespeare from 1, 3 and 6 characters of context { #context }

<!-- 0:38 · 9 min -->

The next character drawn from the last k characters: the longer the context, the more the text reads like the plays, and the larger the table (C. E. Shannon's experiment of 1948, with letters of English).

```python title="shannon.py"
import random
import urllib.request
from collections import Counter

URL = ("https://raw.githubusercontent.com/karpathy/char-rnn/master/data/"
       "tinyshakespeare/input.txt")
with urllib.request.urlopen(URL) as response:
    text = response.read().decode()
print(len(text), "characters,", len(set(text)), "different ones")

for k in [1, 3, 6]:              # characters of context
    follow = {}                  # the k characters -> Counter of the next
    for i in range(k, len(text)):
        follow.setdefault(text[i - k:i], Counter())[text[i]] += 1
    random.seed(1)
    out = text[:k]               # start as the text starts
    while len(out) < 160:
        row = follow[out[-k:]]
        out += random.choices(list(row), weights=list(row.values()))[0]
    print(f"--- {k} character(s) of context: a table of {len(follow)} rows")
    print(out)
```

```text
$ python shannon.py
1115394 characters, 65 different ones
--- 1 character(s) of context: a table of 65 rows
Figrer in wilande n.
Bos hano t hed wicouk'l esch is gs d htherined.
I t wiond tnth hado hiordsink theld thald, t her
TETh it wisthen t ho m, s fove y!
Bullyope
--- 3 character(s) of context: a table of 11556 rows
First, their faitorswere of more the consel
they ins thou have stoo here mighwardshio dening Edwarrant to the hou like only chiefs are the backing hast March th
--- 6 character(s) of context: a table of 283313 rows
First Citizens, where, Friar, the father:
Yours, and how to be to his brethren here pitch our sunshine's blood upon my greedy looks he storms than it is a reeli
```

Then in the chat: *Continue this in the style of Shakespeare for five lines: First Citizen:*

**Notice:** with 6 characters the words and the line breaks are right and the sense is not; pieces of about ten characters (`his brethren`, `upon my gr`) stand word for word in the plays, the whole line nowhere.

**Ask the room:** what does the model write with 20 characters of context?

??? note "Answer"
    Change the loop's line to `for k in [20]:` and run it:

    ```text
    $ python shannon.py
    1115394 characters, 65 different ones
    --- 20 character(s) of context: a table of 1103360 rows
    First Citizen:
    Before we proceed any further, hear me speak.

    All:
    Speak, speak.

    First Citizen:
    Your belly's answer? What!
    The kingly-crowned head, the vigilan
    ```

    The table has a row for nearly every one of the 1 115 374 positions:
    almost every 20 characters stand once in the plays, so the model
    reprints them, and jumps only where 20 characters repeat, as after
    `First Citizen:`. A longer context copies more of the text it counted.
    Part 3 asks what that does to a text it has not counted.

---

### 7. Library card: the calls of this page { #card }

<!-- 0:47 · 3 min -->

Every call of the examples and of the solution below, one line each.

| Call | What it does |
|--|--|
| `urllib.request.urlopen(URL)`, then `.read().decode()` | the file at the address, as one text |
| `text.split()` | the words of a text (here the names), cut at spaces and line ends |
| `Counter()`, `c[key] += 1` | a dict that counts; a key not yet there counts 0 |
| `c.most_common(5)`, `c.total()` | the five largest counts, largest first; the sum of all counts |
| `zip(word, word[1:])` | each letter with the letter after it |
| `d.setdefault(key, Counter())` | the value of `key`, made first if it is missing |
| `d.get(key)` | the value of `key`, or `None` if it is missing |
| `text[i - k:i]` | the k characters before position i |
| `names[::10]` | every tenth element, from the first |
| `random.seed(3)` | the same draws on every run and every laptop |
| `random.choices(items, weights=w)[0]` | one item, drawn with the probability weight / sum of the weights |
| `n ** (1 / T)` | the weight of a count n at temperature T: softmax of ln n / T |
| `math.log(p)` | ln p, the natural logarithm |
| `ax.plot(x, y, "o-", label=...)`, `ax.legend(frameon=False)` | a line through points; the labels of the lines, without a frame |
| `ax.errorbar(x, y, yerr=errors, fmt="o-", capsize=3)`, `fig.savefig("name.svg")` | points with a bar of ± `errors` at each; the figure into a file |

---

## Part 3 · The problem { #part-3 }

### 8. Does a longer context always guess the next letter better? { #problem }

<!-- 0:50 · 55 min: predict 5, solve 25, check 15, hand in 10 -->

A model that sees the last k letters guesses the next one: the most likely
letter of the row of its context. Count on nine of every ten names of
`names.txt`, then guess every letter, and the end, of the other names, which
the model never counted. The file of sections 3 to 5 (makemore, MIT licence;
the names from the US Social Security Administration):

```text
https://raw.githubusercontent.com/karpathy/makemore/master/names.txt
```

Work in pairs, with any tools, an LLM too: what counts is the prediction, the checks and the answer in your own words.

1. **Predict**, before any code, on paper: the share of next letters of
   the new names guessed right with k = 0, 1, 2, 4 and 7 letters of
   context (with k = 0 the model guesses the most common symbol every
   time). Sketch the curve, and give one reason for its shape.
2. **Solve.** For k = 0 to 7: the share guessed right on the names counted
   and on the new names, the second with its standard error
   √(p(1 − p) / n), in one figure.
3. **Check the machine's work.**
    - By hand: in `emma olivia ava isabella sophia`, what comes after `a`,
      and how often? Count on paper; your counting code on these five
      names alone must give the same.
    - Read off: n, the number of guesses on the new names (each name's
      letters and its end); the y-axis, a share from 0 to 1; whether the
      error bars are smaller than the steps between neighbouring k.
    - Write down what your code does with a context it never saw; another
      pair may have chosen otherwise.
    - Against your prediction: where they differ, say which was wrong, and
      why.
4. **Hand in.** The figure, the best k with its share ± error, two
   sentences in your own words, and one line: which LLM wrote which part,
   and what you checked yourself.

??? tip "Hint 1: the two sets of names"
    `new = names[::10]` is every tenth name, from the first;
    `[name for i, name in enumerate(names) if i % 10 != 0]` the others.
    With k dots before each name and one after it, `"." * k + name + "."`,
    the first letter has a context too, and the end is guessed like a
    letter.

??? tip "Hint 2: one guess"
    At position `i` of a word, the context is `word[i - k:i]` and the
    letter to guess `word[i]`. The guess is the top of the context's row,
    `follow[context].most_common(1)[0][0]`. A context that is not in
    `follow` has no row: count the guess as wrong, or use a shorter
    context, and say which.

??? tip "Hint 3: the error of a share"
    A share p of n guesses right has the standard error √(p(1 − p) / n):
    with p = 0.36 and n near 22 700, about 0.003.

??? note "One solution"
    ```python title="context.py"
    import urllib.request
    from collections import Counter
    import matplotlib.pyplot as plt

    URL = "https://raw.githubusercontent.com/karpathy/makemore/master/names.txt"
    with urllib.request.urlopen(URL) as response:
        names = response.read().decode().split()
    after_a = Counter(b for name in names[:5]
                      for a, b in zip(name, name[1:] + ".") if a == "a")
    print("after a in", names[:5], dict(after_a))
    new = names[::10]                # every tenth name: kept out of the counts
    seen = [name for i, name in enumerate(names) if i % 10 != 0]
    print(len(seen), "names counted,", len(new), "new names")


    def guesses(k, counted, tested):
        """The share right of the top guesses after k letters, how many guesses,
        and the share of the contexts never seen in the names counted."""
        follow = {}
        for name in counted:
            word = "." * k + name + "."
            for i in range(k, len(word)):
                follow.setdefault(word[i - k:i], Counter())[word[i]] += 1
        right = total = unseen = 0
        for name in tested:
            word = "." * k + name + "."
            for i in range(k, len(word)):
                row = follow.get(word[i - k:i])   # None: a context never seen
                unseen += row is None
                right += row is not None and row.most_common(1)[0][0] == word[i]
                total += 1
        return right / total, total, unseen / total


    counted, shares, errors = [], [], []
    print(" k  counted  new    error  never seen")
    for k in range(8):
        counted.append(guesses(k, seen, seen)[0])
        p, n, unseen = guesses(k, seen, new)
        shares.append(p)
        errors.append((p * (1 - p) / n) ** 0.5)       # the standard error
        print(f"{k:2}  {counted[-1]:.3f}    {p:.3f}  {errors[-1]:.3f}"
              f"  {unseen:.3f}")
    print("letters guessed in the new names: n =", n)

    fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
    ax.plot(range(8), counted, "o-", label="Names it counted")
    ax.errorbar(range(8), shares, yerr=errors, fmt="o-", capsize=3,
                label="New names")
    ax.set_ylim(0, 0.6)
    ax.set_xlabel("Letters of context, k")
    ax.set_ylabel("Share of next letters guessed right")
    ax.set_title("On new names the counting model is best with 4 letters")
    ax.legend(frameon=False)
    fig.savefig("context.svg")
    ```

    ```text
    $ python context.py
    after a in ['emma', 'olivia', 'ava', 'isabella', 'sophia'] {'.': 5, 'v': 1, 'b': 1}
    28829 names counted, 3204 new names
     k  counted  new    error  never seen
     0  0.148    0.149  0.002  0.000
     1  0.228    0.227  0.003  0.000
     2  0.304    0.299  0.003  0.000
     3  0.374    0.349  0.003  0.006
     4  0.447    0.362  0.003  0.041
     5  0.489    0.327  0.003  0.105
     6  0.499    0.283  0.003  0.155
     7  0.501    0.261  0.003  0.177
    letters guessed in the new names: n = 22717
    ```

    ![The share of next letters guessed right against the letters of context, k = 0 to 7, with error bars smaller than the points: on the names counted it rises from 0.15 to 0.50 and levels off; on the new names it rises with it to 0.30 at k = 2, peaks at 0.36 at k = 4 and falls to 0.26 at k = 7](img/s11/context.svg)

    By hand: after `a` come the end in all five names, `v` once (`ava`)
    and `b` once (`isabella`): 5, 1 and 1 of 7, as the first line prints.

    Handed in: *With 4 letters of context the counting model guesses
    0.362 ± 0.003 of the next letters of names it never counted, more than
    with 3 (0.349) or 5 (0.327). Beyond 4 it gets worse on new names while
    it keeps improving on the names it counted: a long context mostly
    repeats a counted name, and 10 to 18 % of the long contexts of new
    names were never seen at all.*

**With your own project data:** the same question on a sequence of your
own field: the words of a text you wrote, a DNA sequence, the states in a
device's log. Count on nine tenths, guess on the rest, and find the k where
the guesses are best.

---

## Part 4 · Show and discuss { #part-4 }

### 9. Three questions about the pairs' curves { #discuss }

<!-- 1:45 · 15 min -->

Two or three pairs show their figure and read their two sentences.

**Ask the room:** two pairs agree up to k = 3 and differ from k = 5 on: one counted a context never seen as a wrong guess, the other used a shorter context instead. Which curve is right?

??? note "Answer"
    Both, each for its rule, which belongs next to the figure. From k = 5
    on, 10 to 18 % of the contexts of the new names were never seen: with
    a shorter context in their place the curve stops falling and stays
    near its top; counted as wrong, it falls. Either way the longest
    context is not the best one.

**Ask the room:** why does the curve of the names counted level off near 0.50, not at 1?

??? note "Answer"
    The first letter of every name has the same context, the dots, so the
    model guesses `a` for every name, and the next one or two letters
    still fit thousands of names. Only once the context points to one
    counted name can the model copy it.

**Ask the room:** a chat LLM reads a prompt of thousands of tokens and uses all of it. Why does a long context help it, when it ruined the table?

??? note "Answer"
    A table has a row only for a context it has seen letter for letter. A
    network computes the probabilities from learned vectors of the tokens,
    so a context it never saw gets probabilities from similar ones. It
    still writes what is likely after the prompt: a fact it needs has to
    be in the prompt or in its training text.

A language model turns the context into a probability for each next token; a longer context helps only as far as the model can carry what it learned from similar contexts, which a table of counts cannot and a large network can.

---

## Optional, if the room is fast { #optional }

### 10. With five times as much text, does a longer context pay? { #plays }

<!-- — · 15 min -->

The plays of section 6 hold 1.1 million characters, five times the letters
of `names.txt`. Count on the first nine tenths, guess every character of
the last tenth.

Predict, solve, check the machine's work, hand in, as in section 8: the best k with its share ± error, against the best k of the names.

??? note "One solution"
    ```python title="plays.py"
    import urllib.request
    from collections import Counter

    URL = ("https://raw.githubusercontent.com/karpathy/char-rnn/master/data/"
           "tinyshakespeare/input.txt")
    with urllib.request.urlopen(URL) as response:
        text = response.read().decode()
    cut = len(text) * 9 // 10
    seen, new = text[:cut], text[cut:]     # the last tenth is never counted
    print(len(seen), "characters counted,", len(new), "new")

    print(" k  rows     new    error  never seen")
    for k in range(11):
        follow = {}
        for i in range(k, len(seen)):
            follow.setdefault(seen[i - k:i], Counter())[seen[i]] += 1
        best = {context: row.most_common(1)[0][0]
                for context, row in follow.items()}
        right = unseen = 0
        for i in range(k, len(new)):
            guess = best.get(new[i - k:i])     # None: a context never seen
            unseen += guess is None
            right += guess == new[i]
        n = len(new) - k
        p = right / n
        error = (p * (1 - p) / n) ** 0.5
        print(f"{k:2}  {len(follow):6}  {p:.3f}  {error:.3f}  {unseen / n:.3f}")
    ```

    ```text
    $ python plays.py
    1003854 characters counted, 111540 new
     k  rows     new    error  never seen
     0       1  0.149  0.001  0.000
     1      65  0.270  0.001  0.000
     2    1380  0.381  0.001  0.002
     3   11228  0.468  0.001  0.014
     4   48539  0.512  0.001  0.042
     5  133293  0.495  0.001  0.101
     6  264623  0.444  0.001  0.208
     7  413620  0.365  0.001  0.348
     8  559503  0.282  0.001  0.497
     9  684640  0.205  0.001  0.636
    10  780165  0.141  0.001  0.749
    ```

    The best k is 4 again, 0.512 ± 0.001. Five times the text does not
    buy one more character: each character of context multiplies the
    rows by two to three (48 539, 133 293, 264 623), and the share of
    contexts never seen doubles or more with each step (0.042, 0.101,
    0.208).

---

## Aims practised

- ♻️ **Reproducibility:** the texts come from their public addresses and
  `random.seed` makes every laptop draw the same names; a chat's reply
  cannot be drawn again, so the hand-in says which LLM wrote what.
- 🔧 **Tool-agnosticism:** a language model built from a `Counter` and one
  draw; any chat LLM is checked the same way, against counts computed from
  the file.
- 📁 **Files:** a statement about a file is computed from the file: the
  counts after `q`, the share guessed right, the contexts never seen.
