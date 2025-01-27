from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.utils import get_model, process_input, InputData
import os

app = FastAPI(title="Bengaluru House Price Prediction")
MODEL_PATH = os.path.join("app", "artifacts", "model.pkl")


@app.get("/")
def home():
    return {"Health Status": "Ok"}


@app.get("/info")
def info():
    return {"Application": "House Price Prediction", "Units": "In Lakhs"}


@app.post("/predict", response_class=JSONResponse)
def predict(input_data: InputData) -> dict:

    ## Process the user input
    model_input = process_input(input_data)
    model = get_model(MODEL_PATH)

    # ## Now make the predictions
    price = model.predict(model_input)[0]
    return {"price": price}
