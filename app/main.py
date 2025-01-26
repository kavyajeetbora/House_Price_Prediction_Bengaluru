from fastapi import FastAPI
import pickle
from pydantic import BaseModel

app = FastAPI(title="Bengaluru House Price Prediction")
MODEL_PATH = "app\artifacts\house_price_prediction_model.pickle"


# Define the input data model
class InputData(BaseModel):
    area: str
    sqft: int
    num_beds: int
    num_baths: int


@app.get("/")
def home():
    return {"Health Status": "Ok"}


@app.get("/info")
def info():
    return {"Application": "House Price Prediction", "Units": "In Lakhs"}


def get_model(path):
    with open(path, "rb") as pkl_file:
        model = pickle.load(pkl_file)
    return model


@app.post("/predict")
def predict(input_data: InputData) -> float:
    model = get_model(MODEL_PATH)
    # price = model.predict(
    #     input_data.area, input_data.sqft, input_data.num_beds, input_data.num_baths
    # )
    price = model.predict("Indira Nagar", 1000, 2, 3)
    return price
