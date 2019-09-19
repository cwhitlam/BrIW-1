import pickle
import os
from UI import *
from classes import *
import user_input

def load_from_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            return pickle.load(file)
    else:
        raise Exception("File does not exist")


def save_to_file(file_path, file_to_save):
    with open(file_path, "wb") as file:
        pickle.dump(file_to_save, file)


def load_dictionary_from_file(file_name):
    file_path = f"./sources/data/{file_name}.p"
    retreived_file = load_from_file(file_path)
    if type(retreived_file) is dict:
        return retreived_file
    else:
        raise TypeError("File retreived is not of type Dictionary")


"""
will create new file if existing file cannot be found
"""
def save_dictionary_to_file(file_name, dictionary_to_save):
    file_path = f"./sources/data/{file_name}.p"
    save_to_file(file_path, dictionary_to_save)

def list_people():
        people = load_dictionary_from_file("people")
       
        header = get_header()
        second_col_index = int(header / 2)
        max_name_length = max(len(person.full_name) for person in people.values())
        max_id_digits = max(len(str(key)) for key in people.keys())
        
        #if a name is larger than the width of the first col, increase header width and re-evalute until name will fit
        while max_name_length > second_col_index:
            header = int(header * 1.05)
            second_col_index = int(header / 2)

        print_people_menu_title()

        column_headers = "| Name"
        column_headers += f"{' ' * (second_col_index - len(column_headers)-1)}| Preference"
        column_headers += f"{' ' * (header - len(column_headers)-1)}|"
        print(column_headers)
        print_header()

        for p_id, person in people.items():
            id_padding = 0 if len(str(p_id)) == max_id_digits else max_id_digits - len(str(p_id))
            person_row = f"| {p_id}. {' ' * id_padding}{person.full_name}"
            person_row += f"{' ' * (second_col_index - len(person_row)-1)}| {person.fav_drink.name}"
            person_row += f"{' ' * (header - len(person_row)-1)}|"
            print(person_row)

        print_header()


def add_people():
        while True:
            current_people = load_dictionary_from_file("people")
            print_people_menu_title(True)
            
            first_name_input = user_input.get_striped_string_input("What is the new persons first name?: ").capitalize()
            last_name_input = user_input.get_striped_string_input("what is the new persons last name?: ").capitalize()
            #TODO select new persons drink preference
            fav_drink = None
            
            if first_name_input != "" and last_name_input != "":
                new_person = Person(
                    max(current_people.keys())+1,
                    first_name_input,
                    last_name_input,
                    fav_drink
                )

                print_people_menu_title(True)
                print(f"First Name: {new_person.forename}")
                print(f"Last Name: {new_person.surname}")
                print(f"Favourite Drink: {new_person.fav_drink.name}")
                print()
                print("Please check the details above are correct.")
                print("Would you like to submit the entered details?", end=" ")
                if user_input.get_bool_yes_no_input():
                    print_people_menu_title(True)
                    
                    try:
                        current_people[new_person.identifier] = new_person
                        save_dictionary_to_file("people", current_people)

                        print("new person succesfully added.")
                    except Exception as e:
                        print(f"there was an issue saving the new person. Message: {e}")
                else:
                    print_people_menu_title(True)
                    print("The new person entry was aborted")
            else:
                print("blank first or last name's are not allowed")

            print("Would you like to add someone else?", end=" ") 
            if not user_input.get_bool_yes_no_input():
                break


def remove_people():
    try:
        user_to_remove = user_input.get_int_input("Select a person to delete by ID: ")
        people = load_dictionary_from_file("people")
        del people[user_to_remove]
        save_dictionary_to_file("people", people)

    except:
        raise Exception("Could not delete person from file")


def change_drink_preference():
    list_people()


def list_drinks():
    drinks = load_dictionary_from_file("drinks")
       
    max_id_digits = max(len(str(key)) for key in drinks.keys())
    
    print_drinks_menu_title(True)

    column_headers = "| Name"
    column_headers += f"{' ' * (get_header() - len(column_headers)-1)}|"
    print(column_headers)
    print_header()

    for d_id, drink in drinks.items():
        id_padding = 0 if len(str(d_id)) == max_id_digits else max_id_digits - len(str(d_id))
        person_row = f"| {d_id}. {' ' * id_padding}{drink.name}"
        person_row += f"{' ' * (get_header() - len(person_row)-1)}|"
        print(person_row)

    print_header()

def add_drinks():
    while True:
        current_drinks = load_dictionary_from_file("drinks")
        print_drinks_menu_title(True)

        name_input = user_input.get_striped_string_input("Please enter the new drink").capitalize()
        instructions = user_input.get_striped_string_input("what instructions are needed for this drink? (Can be blank)").capitalize()
        
        if name_input != "":
            new_drink = Drink(
                max(current_drinks.keys())+1,
                name_input,
                instructions if instructions != "" else None
            )
            
            print_drinks_menu_title(True)
            print(f"Drink: {new_drink.name}")
            print(f"Instructions: {new_drink.instructions}")
            print()
            print("Please checj the details above are correct.")
            print("Would you like to submit the entered details?", end=" ")
            if user_input.get_bool_yes_no_input():
                print_drinks_menu_title(True)

                try:
                    current_drinks[new_drink.identifier] = new_drink
                    save_dictionary_to_file("drinks", current_drinks)

                    print("new drink succesfully added.")
                except Exception as e:
                    print(f"there was an issue saving the new person. Message: {e}")
            else:
                print_drinks_menu_title(True)
                print("The new dink entry was aborted")
        else:
            print("blank drink name is not allowed")

        print("Would you like to add another drink?", end=" ")
        if not user_input.get_bool_yes_no_input():
            break
