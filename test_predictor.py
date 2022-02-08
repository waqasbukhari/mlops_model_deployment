import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split

from data import process_data
from model import compute_model_metrics, inference

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


def test_compute_model_metrics_count():
    metrics = compute_model_metrics(y, preds)
    assert len(metrics) == 3


def test_compute_model_metrics_range():
    metrics = compute_model_metrics(y, preds)
    result = map((lambda m: (m >= 0) & (m <= 1)), metrics)
    assert all(result)


def test_inference_shape():
    preds = inference(model, X)
    assert len(preds) == X.shape[0]


def test_inference_values():
    preds = inference(model, X)
    assert np.all((preds == 0) | (preds == 1))
