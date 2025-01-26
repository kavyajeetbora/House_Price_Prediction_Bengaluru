from utils import process_input, get_model, InputData
import os

MODEL_PATH = r"app\artifacts\model.pkl"
user_input = InputData(area="akshaya nagar", sqft=1200, num_baths=3, num_beds=2)

if os.path.exists(MODEL_PATH):
    model = get_model(MODEL_PATH)
    model_input = process_input(user_input)
    prediction = model.predict(model_input)[0]
    print(prediction)

else:
    print("No Model")
