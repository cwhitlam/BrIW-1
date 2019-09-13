import os
from classes import Round, Person, Drink
import pickle
import UI
import json

ui = UI.UI()

def unpickle(path):
    if os.path.exists(path):
        with open(path, "rb") as file:
            return pickle.load(file)

def pickle_load(path, obj):
    with open(path, "wb") as file:
        pickle.dump(obj, file)

def load_json(command):
    with open(f"data/{command}.json") as file:
        return json.load(file)[command]

people_path = "./data/people"
drinks_path = "./data/drinks"

json_people_list = load_json("people")
json_drink_list = load_json("drinks")

pickle_people_list = []
pickle_drink_list = []

for json_person in json_people_list:
    p_id = json_person["id"]
    p_fname = json_person["name"].split()[0]
    p_sname = json_person["name"].split()[1]
    
    p_fav_drink_id = None if json_person["favourite_drink"] == "No Preference" else int(json_person["favourite_drink"])
    fav_drink = None
    
    if p_fav_drink_id is not None:
        fav_drink = Drink(p_fav_drink_id, json_drink_list[p_fav_drink_id]["name"])

    person = Person(p_id, p_fname, p_sname, fav_drink)

    pickle_people_list.append(person)

pickle_load(people_path, pickle_people_list)

for json_drink in json_drink_list:
    d_id = json_drink["id"]
    d_name = json_drink["name"]
    d_instruc = json_drink["instructions"]

    drink = Drink(d_id, d_name, d_instruc)

    pickle_drink_list.append(drink)

pickle_load(drinks_path, pickle_drink_list)
