import pandas as pd
# from sklearn.model_selection import train_test_split
# from data import process_data


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


def test_X():
    data_path = "modified_census.csv"
    data = pd.read_csv(data_path)
    assert "salary" in data.columns
    # train, _ = train_test_split(data, test_size=0.20)
    # X, _, _, _ = process_data(
    #                           train,
    #                           categorical_features=CAT_FEATURES,
    #                           label="salary",
    #                           training=True)
    # assert len(X.shape) == 2
