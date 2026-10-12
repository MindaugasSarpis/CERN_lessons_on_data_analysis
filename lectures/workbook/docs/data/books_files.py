#!/usr/bin/env python3
"""Write the files of Seminar 1 next to this script.

The files are generated, not collected: a made-up reading list and the loans
log of a made-up town library. The titles are real books; the page counts are
those of one edition, the ratings and every loan are invented. The random
numbers are seeded and the zip and the picture carry fixed metadata, so the
output is the same on every run.

  books_reading_list.csv        the reading list as a spreadsheet with
                                European settings exports it: `;` between the
                                values, a decimal comma, a column `nr`, and a
                                line with the means at the end
  books_reading_list_clean.csv  the same list repaired in the editor
                                (sections 8 to 10 of the seminar)
  books_report.txt              results/report.md at the end of section 11
  books_pages.png               the picture in the report
  books_loans.csv               one row per loan, 2021 to 2025; `NA` where a
                                book has not come back
  books_README.txt              README.md at the end of the seminar
  books_project.zip             the whole folder `reading-project` at the end

The README and the report are `.txt`, because MkDocs turns every `.md` file
in `docs/` into a page. The seminar page links them with `download="…md"`.

Usage:  python3 books_files.py      (needs matplotlib for the picture)
"""
import random
import zipfile
from datetime import date, timedelta
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
ZIP_DATE = (2026, 9, 29, 12, 0, 0)
EXPORT_DAY = date(2025, 12, 31)

BOOKS = [
    ("The Little Prince", "Antoine de Saint-Exupéry", 96),
    ("Pride and Prejudice", "Jane Austen", 432),
    ("Frankenstein", "Mary Shelley", 280),
    ("Metai", "Kristijonas Donelaitis", 120),
    ("Dracula", "Bram Stoker", 418),
    ("Brave New World", "Aldous Huxley", 288),
    ("The Old Man and the Sea", "Ernest Hemingway", 127),
    ("Animal Farm", "George Orwell", 112),
    ("Altorių šešėly", "Vincas Mykolaitis-Putinas", 452),
    ("Crime and Punishment", "Fyodor Dostoevsky", 671),
    ("The Martian", "Andy Weir", 369),
    ("Solaris", "Stanisław Lem", 204),
]


def half_up(value, places):
    q = Decimal(1).scaleb(-places)
    return Decimal(str(value)).quantize(q, rounding=ROUND_HALF_UP)


def reading_list():
    rng = random.Random(1)
    ratings = [rng.choice([3.0, 3.5, 4.0, 4.0, 4.5, 4.5, 5.0]) for _ in BOOKS]
    raw = ["nr;title;author;pages;rating"]
    clean = ["title,author,pages,rating"]
    for nr, ((title, author, pages), rating) in enumerate(zip(BOOKS, ratings), start=1):
        raw.append(f"{nr};{title};{author};{pages};{str(rating).replace('.', ',')}")
        clean.append(f"{title},{author},{pages},{rating}")
    mean_pages = half_up(sum(p for _, _, p in BOOKS) / len(BOOKS), 1)
    mean_rating = half_up(sum(ratings) / len(ratings), 2)
    raw.append(f";mean;;{str(mean_pages).replace('.', ',')};{str(mean_rating).replace('.', ',')}")
    return "\n".join(raw) + "\n", "\n".join(clean) + "\n", ratings


def loans():
    rng = random.Random(2026)
    shelf = {f"B{n:04d}": rng.randint(64, 900) for n in range(1, 1201)}
    ids = list(shelf)
    weights = [1 / (i + 10) for i in range(len(ids))]
    rows = ["loan_date,book_id,pages,days_kept,late_fee_eur"]
    day = date(2021, 1, 4)
    while day <= EXPORT_DAY:
        if day.weekday() != 6:  # closed on Sundays
            for _ in range(rng.randint(6, 16)):
                book = rng.choices(ids, weights)[0]
                kept = min(90, max(1, round(rng.gauss(17, 8))))
                if rng.random() < 0.08:
                    kept += rng.randint(10, 30)
                lost = rng.random() < 0.002
                if lost or day + timedelta(days=kept) > EXPORT_DAY:
                    rows.append(f"{day.isoformat()},{book},{shelf[book]},NA,NA")
                else:
                    fee = max(0, kept - 28) * Decimal("0.10")
                    rows.append(f"{day.isoformat()},{book},{shelf[book]},{kept},{fee:.2f}")
        day += timedelta(days=1)
    return "\n".join(rows) + "\n"


def report(clean_text):
    lines = clean_text.splitlines()
    table = ["| " + line.replace(",", " | ") + " |" for line in lines]
    table.insert(1, "|--|--|--|--|")
    return (
        "# My Reading List\n\n"
        "Twelve books, with the pages of the edition read and my rating.\n\n"
        + "\n".join(table)
        + "\n\n![Pages per book](reading_pages.png)\n"
    )


def picture(path):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    titles = [t for t, _, _ in BOOKS][::-1]
    pages = [p for _, _, p in BOOKS][::-1]
    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
    ax.barh(titles, pages, color="#3b82f6")
    ax.set_xlabel("pages")
    ax.set_title("Pages per book")
    fig.tight_layout()
    fig.savefig(path, metadata={"Software": None})
    plt.close(fig)


README = """\
# Reading Project

A made-up reading list and the loans log of a made-up library, used to
practise VS Code and Markdown.

## Folders

| Folder | What goes in |
|--|--|
| `README.md` | what the project is and where the data came from |
| `data/raw` | files exactly as received, never edited |
| `data/processed` | cleaned copies |
| `scripts` | programs, later in the course |
| `results` | the report and its picture |

## Data

- **Source:** generated for the course by `books_files.py`; the list and
  the library are made up, the titles are real books
- **Licence:** CC0
- **Received:** 2026-09-29
- **File:** `data/raw/reading_list.csv`, {raw_size} bytes, 12 books,
  exported from a spreadsheet: `;` between the values, a decimal comma
- **Cleaned copy:** `data/processed/reading_list.csv`, {clean_size} bytes.
  Mean line deleted, `,` replaced by `.`, `;` replaced by `,`, column `nr`
  deleted
- **File:** `data/raw/loans.csv`, {loans_size} bytes, {loans_rows} rows
  - **One row:** one loan of one book
  - **Columns:** `loan_date` (YYYY-MM-DD), `book_id` (a label), `pages`,
    `days_kept` (days), `late_fee_eur` (euros: 0.10 for each day after 28)
  - **Missing:** `NA` in `days_kept` and `late_fee_eur` when the book has
    not come back, {na_rows} rows
"""


def main():
    raw_text, clean_text, _ = reading_list()
    loans_text = loans()
    report_text = report(clean_text)
    files = {
        "books_reading_list.csv": raw_text.encode(),
        "books_reading_list_clean.csv": clean_text.encode(),
        "books_report.txt": report_text.encode(),
        "books_loans.csv": loans_text.encode(),
    }
    for name, data in files.items():
        (HERE / name).write_bytes(data)
    picture(HERE / "books_pages.png")
    loans_rows = loans_text.count("\n") - 1
    na_rows = loans_text.count(",NA,NA\n")
    readme = README.format(
        raw_size=len(files["books_reading_list.csv"]),
        clean_size=len(files["books_reading_list_clean.csv"]),
        loans_size=f"{len(files['books_loans.csv']):,}".replace(",", " "),
        loans_rows=f"{loans_rows:,}".replace(",", " "),
        na_rows=na_rows,
    ).encode()
    (HERE / "books_README.txt").write_bytes(readme)

    root = "reading-project/"
    with zipfile.ZipFile(HERE / "books_project.zip", "w", zipfile.ZIP_DEFLATED) as z:
        def put(name, data=None):
            info = zipfile.ZipInfo(root + name, ZIP_DATE)
            if data is None:
                info.external_attr = 0o40755 << 16
                z.writestr(info, b"")
            else:
                info.external_attr = 0o644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, data)
        put("")
        put("README.md", readme)
        put("data/")
        put("data/raw/")
        put("data/raw/reading_list.csv", files["books_reading_list.csv"])
        put("data/raw/loans.csv", files["books_loans.csv"])
        put("data/processed/")
        put("data/processed/reading_list.csv", files["books_reading_list_clean.csv"])
        put("scripts/")
        put("results/")
        put("results/report.md", files["books_report.txt"])
        put("results/reading_pages.png", (HERE / "books_pages.png").read_bytes())


if __name__ == "__main__":
    main()
