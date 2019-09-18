import os
from prettyprint import PrettyTable
from pyfiglet import Figlet
from functions import *

def clear_screen(self):
    os.system("cls" if os.name == "nt" else "clear")


def press_enter_to_continue(self):
    input("Press Enter to continue ")

def generate_ascii_title(text):
    ascii_generator = Figlet(font='speed')
    return ascii_generator.renderText(text)


def generate_ascii_items_table(column_names, data):
    item_table = PrettyTable()
    item_table.field_names = column_names

    for row in data:
        item_table.add_row(row)

    return item_table

def generate_columns_for_ascii_table(item_type):
    colum_names = []
    if item_type == "People":
        colum_names = ["ID", "Name", "Preference"]
    elif item_type = "Drinks":
        colum_names = ["ID", "Name", "Instructions"]
    else:
        raise ValueError(f"{item_type} is not a valid option")
    
    return colum_names


def generate_data_list_for_ascii_table(item_type, item_dictionary):
    data_row_list = []

    for key, item in item_dictionary.items():
        column_1_data = item.identifier
        column_2_data = item.full_name if item_type == "Person" else item.name
        column_3_data = item.fav_drink.name if item_type == "Person" else item.instructions

        data_row_list.append([column_1_data, column_2_data, column_3_data])

def get_item_selection_from_user(item_type):
    item_dictionary = get_item_dictionary_from_pickle(item_type)
    colum_names = generate_columns_for_ascii_table(item_type)
    data = generate_data_list_for_ascii_table(item_type, item_dictionary)

    ascii_table = generate_ascii_items_table(colum_names, data)
    print(ascii_table)
    return get_option()

def get_item


