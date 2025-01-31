import pandas as pd
from pydantic import BaseModel
import numpy as np
import os
import json
import pickle

METADATA_PATH = os.path.join("app", "artifacts", "columns.json")

if os.path.exists(METADATA_PATH):
    with open(METADATA_PATH, "r") as json_file:
        metadata = json.load(json_file)

    COLUMNS = metadata["columns"]

else:
    COLUMNS = None
    print("No metadata file found")


# Define the input data model
class InputData(BaseModel):
    area: str
    sqft: int
    num_beds: int
    num_baths: int


def get_model(path):
    with open(path, "rb") as pkl_file:
        model = pickle.load(pkl_file)
    return model


def process_input(user_input: InputData):
    try:

        x_input = np.zeros(len(COLUMNS))
        loc_index = list(COLUMNS).index(user_input.area)
        x_input[0] = user_input.sqft
        x_input[1] = user_input.num_baths
        x_input[2] = user_input.num_baths
        x_input[loc_index] = 1

        input_data = pd.DataFrame(x_input.reshape(1, -1), columns=COLUMNS, dtype=int)
        return input_data

    except Exception as e:
        print("There was some error while processing the user inputs")
        print(f"Error: {e}")
