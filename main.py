import os
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
from data import process_data
from model import inference
import joblib
import subprocess


class Input(BaseModel):
    age: int = Field(..., example=49)
    workclass: str = Field(..., example="Private")
    fnlgt: int = Field(..., example=160187)
    education: str = Field(..., example="9th")
    education_num: int = Field(..., example=5, alias="education-num")
    marital_status: str = Field(
        ..., example="Married-spouse-absent", alias="marital-status"
    )
    occupation: str = Field(..., example="Other-service")
    relationship: str = Field(..., example="Not-in-family")
    race: str = Field(..., example="Black")
    sex: str = Field(..., example="Female")
    capital_gain: int = Field(..., example=0, alias="capital-gain")
    capital_loss: int = Field(..., example=0, alias="capital-loss")
    hours_per_week: int = Field(..., example=16, alias="hours-per-week")
    native_country: str = Field(..., example="Jamaica", alias="native-country")


class Output(BaseModel):
    Income: str = Field(..., example=">50K")


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

app = FastAPI()

if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("ls -l")
    os.system("dvc remote add -df s3remote s3://udacity-student-waqas")
    os.system("dvc config core.hardlink_lock true")
    dvc_output = subprocess.run(["dvc", "pull"],
                                capture_output=True,
                                text=True)
    print(dvc_output.stdout)
    print(dvc_output.stderr)
    if dvc_output.returncode != 0:
        print("dvc pull failed")
    os.system("dvc pull")
    os.system("ls -l")
    os.system("dvc config core.no_scm true")
    if os.system("dvc pull") != 0:
        exit("dvc pull failed")
    # os.system("rm -r .dvc .apt/usr/lib/dvc")


@app.on_event("startup")
def startup_event():
    """
    Additionally load model and encoder on startup for faster predictions
    """
    with open("encoder.pkl", "rb") as f:
        global ENCODER
        ENCODER = joblib.load(f)
    with open("model.pkl", "rb") as f:
        global MODEL
        MODEL = joblib.load(f)
    with open("lb.pkl", "rb") as f:
        global LB
        LB = joblib.load(f)


@app.get("/")
def welcome() -> str:
    return {"message": "Welcome to Income prediction"}


@app.post("/predict")
def predict(data: Input):
    print("entered. ")
    df = pd.DataFrame.from_dict([data.dict(by_alias=True)])
    X, _, _, _ = process_data(
        df, categorical_features=CAT_FEATURES, training=False, encoder=ENCODER
    )
    pred = inference(MODEL, X)
    # out_category = LB.inverse_transform(pred)[0]

    if pred == 1:
        pred = ">50K"
    elif pred == 0:
        pred = "<=50K"
    # return {"Income": out_category}
    return {"Income": pred}
