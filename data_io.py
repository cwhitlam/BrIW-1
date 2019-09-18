import pickle
import os
from UI import *
from classes import *

def unpickle(file_name):
    path = f"./data/{file_name}.p"
    if os.path.exists(path):
        with open(path, "rb") as file:
            return pickle.load(file)


def picklize(file_name, obj):
    path = f"./data/{file_name}.p"
    with open(path, "wb") as file:
        pickle.dump(obj, file)


def add_people():
        while True:
            print_people_menu_title(True)
            
            first_name = input("What is the new persons first name?: ").capitalize()
            last_name = input("what is the new persons last name?: ").capitalize()
            #TODO select new persons drink preference
            fav_drink = None
            
            print_people_menu_title(True)
            print(f"First Name: {first_name}")
            print(f"Last Name: {last_name}")
            print(f"Favourite Drink: {'No Preference' if fav_drink is None else fav_drink.fav_drink}")
            print()
            print("Please check the details you have entered above are correct.")
            if input("Would you like to submit the entered details? (Y/N): ").upper() == "Y":
                print_people_menu_title(True)
                
                try:
                    print_people_menu_title(True)

                    people = unpickle("people")
                    new_id = max(people.keys())+1
                    new_person = Person(new_id, first_name, last_name, fav_drink)

                    people[new_id] = new_person
                    picklize("people", people)
                    print("new person succesfully added.")
                except Exception as e:
                    print(f"there was an issue saving the new person. Message: {e}")
            else:
                print_people_menu_title(True)
                print("The new person entry was aborted")
                press_enter_to_continue()
                print_people_menu_title(True)

            if input("Would you like to add someone else?(Y/N): ").upper() == "N":
                break

def remove_people():
    pass
