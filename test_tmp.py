import pandas as pd
from sklearn.model_selection import train_test_split


def test_X():
    data_path = "modified_census.csv"
    data = pd.read_csv(data_path)
    train, _ = train_test_split(data, test_size=0.20)
    assert len(train.shape) == 2
    # X, _, _, _ = process_data(
    #     train, categorical_features=CAT_FEATURES, label="salary",
    # training=True
    # )
    # return X
