import os
from classes import Round, Person, Drink
import UI
import pickle

def unpickle(path):
    if os.path.exists(path):
        with open(path, "rb") as file:
            return pickle.load(file)

def pickle_load(path, obj):
    with open(path, "wb") as file:
        pickle.dump(obj, file)

people_path = "./data/people"
drinks_path = "./data/drinks"
ui = UI.UI()


#PROGRAM FLOW
ui.clear()
ui.print_main_menu()

menu_input_raw = input("Option: ")

if menu_input_raw.isnumeric():
    menu_selection = ui.main_menu_options[int(menu_input_raw)]
    if menu_selection == "People":
        ui.print_people_menu()
    elif menu_selection == "Drinks":
        ui.print_drinks_menu()
    elif menu_selection == "Exit Application":
        exit()

else:
    #TODO easteregg
    pass

