import pytest
from sklearn.model_selection import train_test_split
import pandas as pd
from data import process_data

CAT_FEATURES = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]


@pytest.fixture(scope="module")
def X():
    data_path = "modified_census.csv"
    data = pd.read_csv(data_path)
    train, _ = train_test_split(data, test_size=0.20)
    X, _, _, _ = process_data(
        train, categorical_features=CAT_FEATURES, label="salary", training=True
    )
    return X


def test_size(X):
    assert X[:3, :].shape[0] == 3
