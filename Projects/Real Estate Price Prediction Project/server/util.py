import pickle
import json
import numpy as np
import pandas as pd

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        # Find the column index for the location
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    # Create an input array with zeros
    x = np.zeros(len(__data_columns))

    # Assign values to the respective features
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    # Set the location feature to 1 if found
    if loc_index >= 0:
        x[loc_index] = 1

    # Predict using the model
    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        # Ensure feature names are in the correct case
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # First 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location