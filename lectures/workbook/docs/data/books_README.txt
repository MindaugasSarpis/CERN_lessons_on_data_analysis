# Reading Project

A reading list and the loans log of a library, used to practise VS Code
and Markdown.

## Folders

| Folder | What goes in |
|--|--|
| `README.md` | what the project is and where the data came from |
| `data/raw` | files exactly as received, never edited |
| `data/processed` | cleaned copies |
| `scripts` | programs, later in the course |
| `results` | the report and its picture |

## Data

- **Source:** the course workbook, Seminar 1 page
- **Licence:** CC0
- **Received:** 2026-09-29
- **File:** `data/raw/reading_list.csv`, 546 bytes, 12 books,
  exported from a spreadsheet: `;` between the values, a decimal comma
- **Cleaned copy:** `data/processed/reading_list.csv`, 498 bytes.
  Mean line deleted, `,` replaced by `.`, `;` replaced by `,`, column `nr`
  deleted
- **File:** `data/raw/loans.csv`, 497 313 bytes, 17 279 rows
  - **One row:** one loan of one book
  - **Columns:** `loan_date` (YYYY-MM-DD), `book_id` (a label), `pages`,
    `days_kept` (days), `late_fee_eur` (euros: 0.10 for each day after 28)
  - **Missing:** `NA` in `days_kept` and `late_fee_eur` when the book has
    not come back, 219 rows
