from fastapi import FastAPI

app = FastAPI(title="Bengaluru House Price Prediction")


@app.get("/")
def home():
    return {"Health Status": "Ok"}


@app.get("/info")
def info():
    return {"Application": "House Price Prediction", "Units": "In Lakhs"}


@app.post("/predict")
def predict(input_data: InputData) -> float:
    model = get_model(MODEL_PATH)
    # price = model.predict(
    #     input_data.area, input_data.sqft, input_data.num_beds, input_data.num_baths
    # )
    price = model.predict("Indira Nagar", 1000, 2, 3)
    return price
