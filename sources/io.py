import pickle
import os

class Pickle_IO:
    def unpickle(self, file_name):
        path = f"./data/{file_name}.p"
        if os.path.exists(path):
            with open(path, "rb") as file:
                return pickle.load(file)


    def picklize(self, file_name, obj):
        path = f"./data/{file_name}.p"
        with open(path, "wb") as file:
            pickle.dump(obj, file)
