from utils import process_input, get_model
import os

model_inputs = process_input(location="akshaya nagar", total_sqft=1200, bath=2, bhk=2)
MODEL_PATH = r"app\artifacts\house_price_prediction_model.pkl"

if os.path.exists(MODEL_PATH):
    model = get_model(MODEL_PATH)
    print(model_inputs)
    prediction = model.predict(model_inputs)
    print(prediction)
