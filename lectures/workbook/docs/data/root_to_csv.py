#!/usr/bin/env python3
"""Convert the LHCb masterclass ROOT file to the CSV used in the seminars.

Source: CERN Open Data Portal, record 401 — "LHCb event file for real measurement"
        DOI 10.7483/OPENDATA.LHCb.E7EJ.JUWR
        https://opendata.cern.ch/record/401/files/MasterclassData.root
        sha256 8694a2ed518472b02994629154de3077fdff4aef1065691fa13ae9f6b23b039b

The file's DecayTree declares 147 columns, but only four are filled. Those four
are written out with shorter names — values, row order and float32 precision
are unchanged:

    CSV column  ROOT branch    meaning                                      unit
    M           D0_MM          K-pi+ invariant mass of the candidate        MeV/c^2
    PT          D0_PT          transverse momentum of the candidate         MeV/c
    TAU         D0_TAU         decay time of the candidate; -100 = invalid  ns
    IPCHI2      D0_MINIPCHI2   chi^2 of the impact parameter with respect
                               to the collision point                       —

Usage:  python root_to_csv.py MasterclassData.root D0_KPi.csv      (needs uproot)
"""
import sys

import uproot

COLUMNS = {"M": "D0_MM", "PT": "D0_PT", "TAU": "D0_TAU", "IPCHI2": "D0_MINIPCHI2"}


def main(src, dst):
    tree = uproot.open(src)["DecayTree"]
    data = tree.arrays(list(COLUMNS.values()), library="np")
    with open(dst, "w", newline="\n") as out:
        out.write(",".join(COLUMNS) + "\n")
        for row in zip(*(data[branch] for branch in COLUMNS.values())):
            out.write(",".join(str(v) for v in row) + "\n")
    print(f"{dst}: {tree.num_entries} rows, {len(COLUMNS)} columns")


if __name__ == "__main__":
    main(*sys.argv[1:3])
