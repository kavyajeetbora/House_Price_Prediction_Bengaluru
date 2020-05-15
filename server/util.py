import json
import pickle
import numpy as np

## create global variables
__location = None
__data_columns = None
__model = None


def get_estimated_price(location,sqft,bhk,bath):
    '''
    This fucntion predicts the house price in lakhs rupees given
    location, sqft, bhk and bath as user input
    '''
    try:
        loc_index = __location.index(location.lower())
    except:
        # if location not found, then taken as others
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    if loc_index >= 0:
        x[loc_index+3] = 1

    return round(__model.predict(x.reshape(1,-1))[0],2)

def get_location_names():
    return __location

def load_saved_artifacts():
    '''
    This fucntion will load the artifacts containing all the columns and the trained model
    Then will extract the model and the json file and store it into a global variables
    '''
    print('Loading the artifacts...')
    global __data_columns
    global __location

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    global __model

    with open("./artifacts/house_price_prediction_model.pickle",'rb') as f:
        __model = pickle.load(f)


if __name__ == "__main__":
    load_saved_artifacts()
    # print(get_location_names())

    print(get_estimated_price('1st block jayanagar',1000,2,2))
    print(get_estimated_price('yeshwanthpur',1000,2,2))
