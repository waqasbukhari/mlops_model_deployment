import pandas as pd


def test_X():
    data_path = "modified_census.csv"
    data = pd.read_csv(data_path)
    assert len(data.shape) == 2
