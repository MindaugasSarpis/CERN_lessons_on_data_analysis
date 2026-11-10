"""The figures' typeface for the interactive components, as web fonts.

The static figures set their text in STIX General (style.py); the
interactive components (lectures/content/components/*.vue) draw their plots
as SVG in the page, so they need the same face as a web font. This module
writes three WOFF2 files beside the components' stylesheet,
lectures/content/components/figure-look/: regular, italic and bold, made
from the faces style.use() registers (Matplotlib's STIX General, completed
with the thin spaces and subscript digits, the italic with its upright
symbols), cut down to the characters a plot label needs (Latin, Greek,
punctuation, sub- and superscripts, arrows, mathematical operators).

Licence: the STIX fonts are under the SIL Open Font License 1.1 with the
Reserved Font Names "STIX Fonts" and "TM Math" (Matplotlib's LICENSE_STIX,
copied to figure-look/OFL.txt). A cut-down copy is a Modified Version, so
the files carry the family name "Figure Serif", keep the copyright notice
and name the licence in their name table.

    python figures/src/web_fonts.py    (fontTools with brotli: pip install brotli)

The output is byte-identical from run to run (the source's timestamps).
"""
import sys
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import style  # noqa: E402

OUT = style.ROOT / "lectures" / "content" / "components" / "figure-look"
FAMILY = "Figure Serif"
# Basic Latin, Latin-1, Latin Extended-A, Greek, general punctuation (the
# thin and narrow spaces, dashes, the ellipsis), super- and subscripts,
# letterlike symbols, arrows, mathematical operators.
UNICODES = [*range(0x20, 0x7F), *range(0xA0, 0x180), *range(0x370, 0x400),
            *range(0x2000, 0x2070), *range(0x2070, 0x20A0), *range(0x2100, 0x2150),
            *range(0x2190, 0x2200), *range(0x2200, 0x2300)]
LICENSE = ("This Font Software is licensed under the SIL Open Font License, "
           "Version 1.1. A subset of STIX General as bundled with Matplotlib, "
           "renamed: Reserved Font Names \"STIX Fonts\" and \"TM Math\".")
LICENSE_URL = "https://openfontlicense.org"
# (style name, weight class, source face, its upright face for completion)
FACES = (("Regular", 400, "STIXGeneral.ttf", None),
         ("Italic", 400, "STIXGeneralItalic.ttf", "STIXGeneral.ttf"),
         ("Bold", 700, "STIXGeneralBol.ttf", None))


def _rename(font: TTFont, sub: str) -> None:
    name = font["name"]
    copyright_ = name.getDebugName(0)
    name.names = []
    full = FAMILY if sub == "Regular" else f"{FAMILY} {sub}"
    ps = f"{FAMILY.replace(' ', '')}-{sub}"
    for nid, value in ((0, copyright_), (1, FAMILY), (2, sub), (3, f"{ps};course"),
                       (4, full), (5, "Version 1.0; STIX General subset"), (6, ps),
                       (13, LICENSE), (14, LICENSE_URL)):
        if value:
            name.setName(value, nid, 3, 1, 0x409)


def build() -> list[Path]:
    OUT.mkdir(parents=True, exist_ok=True)
    written = []
    for sub, weight, src, upright in FACES:
        completed = style._stix_completed(style.STIX / src, style.STIX / upright if upright else None)
        font = TTFont(completed, recalcTimestamp=False)
        opts = subset.Options()
        opts.flavor = "woff2"
        opts.layout_features = ["*"]
        opts.name_IDs = ["*"]
        opts.notdef_outline = True
        opts.hinting = False
        opts.recalc_timestamp = False
        sub_ = subset.Subsetter(options=opts)
        sub_.populate(unicodes=UNICODES)
        sub_.subset(font)
        _rename(font, sub)
        font["head"].modified = font["head"].created  # the source's date: runs agree
        font["OS/2"].usWeightClass = weight
        font.flavor = "woff2"
        out = OUT / f"FigureSerif-{sub}.woff2"
        font.save(out)
        written.append(out)
        print(f"  + {out.relative_to(style.ROOT)} ({out.stat().st_size // 1024} kB)")
    return written


if __name__ == "__main__":
    build()
