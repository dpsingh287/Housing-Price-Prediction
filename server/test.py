import pickle

with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
    model = pickle.load(f)
print("loading saved artifacts...done")