import os
from prettytable import PrettyTable

def get_option():
        return int(input("Option: "))

def get_YesNo(text):
    return input(text + " (Y/N): ").upper() == "Y"

def print_table(header, data):
    table = PrettyTable()
    table.field_names = header
    for row in data:
        table.add_row(row)
    
    return table

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def press_enter_to_continue():
    input("Press Enter to Continue: ")
    
