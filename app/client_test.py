import pickle
import os

MODEL_PATH = r"app\artifacts\house_price_prediction_model.pkl"


def get_model(path):
    with open(path, "rb") as pkl_file:
        model = pickle.load(pkl_file)
    return model


if os.path.exists(MODEL_PATH):
    model = get_model(MODEL_PATH)
    print(model)
else:
    print("Model not found")
