from app.utils import get_model, InputData
from sklearn.linear_model import LinearRegression
import os
import requests
import json

MODEL_PATH = os.path.join("app", "artifacts", "model.pkl")
METADATA_PATH = os.path.join("app", "artifacts", "columns.json")
user_input = InputData(area="akshaya nagar", sqft=1200, num_baths=3, num_beds=2)
BASE_URL = "http://localhost:7751"


def test_load_metadata():
    assert os.path.exists(METADATA_PATH), "Metadata file does not exist"


def test_load_model():
    ## Test if the file exists
    assert os.path.exists(MODEL_PATH), "Model file does not exist"
    ## If yes, then test if you are able to load the model
    model = get_model(MODEL_PATH)
    assert type(model) is LinearRegression


def test_root_endpoint():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200, "The server is not running"


def test_predict_endpoint():

    params = {"area": "whitefield", "sqft": 500, "num_baths": 1, "num_beds": 2}
    response = requests.post(f"{BASE_URL}/predict", json=params)
    assert (
        response.status_code == 200
    ), f"The API is not running responding with {response.status_code}"
    assert "price" in response.json(), f"There was some issue with the response"
