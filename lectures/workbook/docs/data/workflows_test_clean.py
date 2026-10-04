from scripts.clean import clean

RAW = "data/raw/pendulum.csv"


def test_nine_measurements():
    assert len(clean(RAW)) == 9


def test_two_columns():
    table = clean(RAW)
    assert list(table.columns) == ["length_cm", "t10_s"]


def test_decimal_comma_is_read():
    table = clean(RAW)
    assert table["t10_s"].iloc[0] == 9.02
