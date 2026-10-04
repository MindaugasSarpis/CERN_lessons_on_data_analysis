import math

import numpy as np
import pytest

from scripts.fit import fit_g, g_from_slope


def test_g_from_slope():
    # T^2 = (4 pi^2 / g) L: the slope 4 s^2/m belongs to g = pi^2
    assert g_from_slope(4.0) == pytest.approx(math.pi**2)


def test_fit_recovers_known_g():
    length = np.array([0.2, 0.4, 0.6, 0.8, 1.0])     # m
    period = 2 * math.pi * np.sqrt(length / 9.81)     # s, no noise
    g, g_error = fit_g(length, period)
    assert g == pytest.approx(9.81)
