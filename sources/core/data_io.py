import pickle
import os

def unpickle(file_name):
    path = f"./data/{file_name}.p"
    if os.path.exists(path):
        with open(path, "rb") as file:
            return pickle.load(file)


def picklize(file_name, obj):
    path = f"./data/{file_name}.p"
    with open(path, "wb") as file:
        pickle.dump(obj, file)


def get_item_dictionary_from_pickle(item_type):
    return unpickle(item_type)

