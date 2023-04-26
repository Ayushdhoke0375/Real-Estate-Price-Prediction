import json
import pickle
import numpy as np

__locations = None
__data_Columns = None
__model = None


def get_estimated_price(total_sqft, bath, bhk, location):
    try:
        loc_index = __data_Columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_Columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations


def load_saved_artifacts():
    print("Loading saved artifacts....starts")
    global __locations
    global __data_Columns

    with open('./artifacts/columns.json', 'r') as f:
        __data_Columns = json.load(f)['data_columns']
        __locations = __data_Columns[3:]
    global __model
    with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)
        print("Loading saved artifacts...done")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price(1000, 2, 2, '1st phase jp nagar'))
    print(get_estimated_price(1000, 3, 3, '1st phase jp nagar'))
    print(get_estimated_price(1200, 2, 2, 'Wanadongri hingna'))  # other location
