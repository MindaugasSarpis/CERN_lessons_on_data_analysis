"""Facts about the results, known without the scripts: python -m pytest"""
import pytest

def read(path):
    """The lines of a file the rebuild made."""
    with open(path, encoding="utf-8") as handle:
        return handle.read().splitlines()

def numbers(path):
    """A file of `name value` lines, as a dict."""
    return dict(line.rsplit(maxsplit=1) for line in read(path))

def test_valid_rows():
    # 87 672 hours, 120 of them -999, and the header line
    assert len(read("data/processed/weather_valid.csv")) == 87553

def test_mean_temperature():
    stats = numbers("results/temp_c.txt")
    assert stats["rows"] == "87552"
    assert float(stats["mean"]) == pytest.approx(7.16, abs=0.005)

def test_hill_station():
    hill = numbers("results/hill.txt")
    assert hill["days compared"] == "361"
    assert float(hill["hill - valley"]) == pytest.approx(-1.19, abs=0.005)
