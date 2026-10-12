#!/usr/bin/env python3
"""Write the files of Seminar 3 next to this script.

The seminar hands out a small folder of everyday files, as they might sit in
the Downloads folder of a friend's laptop. Every file hides one thing that
only its bytes show: a name with a space, a letter that takes two bytes, a
line ending of two bytes, an old Baltic encoding, a byte-order mark, a
picture with the wrong ending, and a copy that differs in one digit. The
files are made up; nothing is measured.

  inbox.zip        the folder as handed out: seven files at the top level, so
                   that both Finder and Explorer unpack it into a folder `inbox`
  inbox_after.zip  the folder `inbox` at the end of the seminar, sorted into
                   `text`, `tables` and `images`, with `todo.txt` in LF and
                   `labas.txt` in UTF-8

The zips carry a fixed date, so the output is the same on every run.

Usage:  python3 inbox_files.py
"""
import struct
import zipfile
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATE = (2026, 10, 12, 12, 0, 0)

SHOPPING = "pienas\nduona\nsūris\nobuoliai\nkava\n"
LABAS = "Labas! Šiandien šilta.\nĮ parką eisime pėsčiomis.\n"
TODO = "call the dentist\npay the rent\nbuy a birthday card\nwater the plants\n"
EXPENSES = (
    "date,item,eur\n"
    "2026-10-01,coffee,2.80\n"
    "2026-10-01,bus ticket,1.00\n"
    "2026-10-02,lunch,6.50\n"
    "2026-10-03,book,12.90\n"
)


def png(size=32):
    """A small picture: a yellow disc on blue, as a PNG file."""
    rows = []
    c = (size - 1) / 2
    for y in range(size):
        row = bytearray([0])  # filter byte: none
        for x in range(size):
            inside = (x - c) ** 2 + (y - c) ** 2 <= (size * 0.3) ** 2
            row += bytes((250, 200, 40) if inside else (40, 90, 170))
        rows.append(bytes(row))

    def chunk(kind, data):
        body = kind + data
        return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body))

    header = struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header)
            + chunk(b"IDAT", zlib.compress(b"".join(rows), 9)) + chunk(b"IEND", b""))


def handed_out():
    return {
        "shopping list.txt": SHOPPING.encode("utf-8"),
        "labas.txt": LABAS.encode("cp1257"),
        "todo.txt": TODO.replace("\n", "\r\n").encode("ascii"),
        "expenses.csv": b"\xef\xbb\xbf" + EXPENSES.encode("utf-8"),
        "expenses_copy.csv": b"\xef\xbb\xbf" + EXPENSES.replace("6.50", "6.60").encode("utf-8"),
        "photo.txt": png(),
        "notes.md": NOTES.encode("utf-8"),
    }


def after():
    files = handed_out()
    return {
        "text/shopping_list.txt": files["shopping list.txt"],
        "text/labas.txt": LABAS.encode("utf-8"),
        "text/todo.txt": TODO.encode("ascii"),
        "tables/expenses.csv": files["expenses.csv"],
        "tables/expenses_copy.csv": files["expenses_copy.csv"],
        "images/photo.png": files["photo.txt"],
        "notes.md": files["notes.md"],
    }


def write_zip(path, files, root="", folders=()):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for folder in [root] + [root + f for f in folders]:
            if folder:
                info = zipfile.ZipInfo(folder, DATE)
                info.external_attr = 0o40755 << 16
                z.writestr(info, b"")
        for name, data in files.items():
            info = zipfile.ZipInfo(root + name, DATE)
            info.external_attr = 0o644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data)


NOTES = """\
# Inbox

Files copied from an old laptop. Nobody remembers what is in them.

- Which files are text, and which are not?
- Why does `labas.txt` look broken?
- Are `expenses.csv` and `expenses_copy.csv` the same file?
"""


def main():
    write_zip(HERE / "inbox.zip", handed_out())
    write_zip(HERE / "inbox_after.zip", after(), root="inbox/",
              folders=("text/", "tables/", "images/"))
    for name, data in handed_out().items():
        print(f"{len(data):5d}  {name}")


if __name__ == "__main__":
    main()
