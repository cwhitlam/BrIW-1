
def unpickle(path):
    if os.path.exists(path):
        with open(path, "rb") as file:
            return pickle.load(file)

def pickle_load(path, obj):
    with open(path, "wb") as file:
        pickle.dump(obj, file)
