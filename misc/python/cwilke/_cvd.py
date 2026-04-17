"""Colour-vision-deficiency simulation matrices (Machado et al. 2009).

Used by several CWilke figures that illustrate how palettes look under
deuteranomaly, protanomaly, tritanomaly, and full desaturation.
"""

from __future__ import annotations

import numpy as np

# Machado 2009 simulation matrices at severity = 1.0 (strong anomaly).
# Applied in linear-RGB space to the row-vector [r, g, b] on the right
# (i.e. sim_rgb = M @ rgb).
DEUTER = np.array([
    [0.367, 0.861, -0.228],
    [0.280, 0.673,  0.047],
    [-0.012, 0.043, 0.969],
])

PROTAN = np.array([
    [0.152, 1.053, -0.205],
    [0.115, 0.786,  0.099],
    [-0.004, -0.048, 1.052],
])

TRITAN = np.array([
    [1.256, -0.077, -0.179],
    [-0.078, 0.931,  0.148],
    [0.005,  0.691,  0.304],
])

MATRICES = {
    "original":    None,
    "deuteranopia": DEUTER,
    "protanopia":   PROTAN,
    "tritanopia":   TRITAN,
}


def _hex_to_rgb(hex_code: str) -> np.ndarray:
    hex_code = hex_code.lstrip("#")
    return np.array([int(hex_code[i:i + 2], 16) for i in (0, 2, 4)]) / 255.0


def _rgb_to_hex(rgb: np.ndarray) -> str:
    rgb = np.clip(rgb, 0.0, 1.0) * 255
    return "#{:02X}{:02X}{:02X}".format(*[int(round(v)) for v in rgb])


def simulate(hex_code: str, kind: str) -> str:
    """Return the hex code of `hex_code` simulated under CVD `kind`."""
    if kind == "original":
        return hex_code
    if kind == "desaturated":
        r, g, b = _hex_to_rgb(hex_code)
        luma = 0.2126 * r + 0.7152 * g + 0.0722 * b
        return _rgb_to_hex(np.array([luma, luma, luma]))
    matrix = MATRICES.get(kind)
    if matrix is None:
        raise ValueError(f"unknown CVD kind: {kind!r}")
    rgb = _hex_to_rgb(hex_code)
    sim = matrix @ rgb
    return _rgb_to_hex(sim)
