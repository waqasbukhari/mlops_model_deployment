import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split

from data import process_data
from model import inference

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


data_path = "modified_census.csv"
data = pd.read_csv(data_path)
print("Salary column in modified_census.csv")
print("salary" in data.columns)
train, _ = train_test_split(data, test_size=0.20)
X, y, _, _ = process_data(
                          train,
                          categorical_features=CAT_FEATURES,
                          label="salary", training=True)

model = DummyClassifier()
model.fit(X, y)
preds = inference(model, X)


def test_y():
    assert data.columns[-1] == 'salary'
