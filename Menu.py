from UI import *
from data_io import *
from classes import Drink, Person, Round
import user_input
import devito as danny

class Menu:
    def __init__(self):
        self._main_menu_options = {
            1: "People",
            2: "Drinks",
            3: "Exit Application",
            4: "Danny"
        }
        self._people_menu_options = {
            1: "List People",
            2: "Add People",
            3: "Remove People",
            4: "Change Drink Preference",
            5: "Return to Main Menu"
        }
        self._drink_menu_options = {
            1: "List Drinks",
            2: "Add Drinks",
            3: "Remove Drinks",
            4: "Return to Main Menu"
        }
    
    #prints provided menu options to user and returns their selection
    def print_menu_options(self, menu_options):
        for key, val in menu_options.items():
            menu_row = f"| [{key}] {val}"
            menu_row += f"{' ' * (get_header() - len(menu_row)-1)}|"
            print(menu_row)
        
        print_header()
        return menu_options[user_input.get_int_input("Option: ")]

        
    def main_menu(self):
        clear()
        print_main_menu_title()
        
        try:
            menu_selection = self.print_menu_options(self._main_menu_options)
            
            if menu_selection == "People":
                self.people_menu()
            elif menu_selection == "Drinks":
                self.drink_menu()
            elif menu_selection == "Danny":
                danny.devito_time()
                press_enter_to_continue()
            else:
                clear()
                print("Thank You for using BrIW™. See you again soon! ^_^")
                exit()
        except ValueError:
            exit()

    def people_menu(self):
        while True:
            clear()
            print_people_menu_title()
            
            try:
                menu_selection = self.print_menu_options(self._people_menu_options)
                clear()

                if menu_selection == "List People":
                    list_people()
                    press_enter_to_continue()
                elif menu_selection == "Add People":
                    add_people()
                elif menu_selection == "Remove People":
                    list_people()
                    remove_people()
                elif menu_selection == "Change Drink Preference":
                    #TODO
                    pass
                elif menu_selection == "Return to Main Menu":
                    clear()
                    break
            except ValueError:
                #return to main menu
                break 

    def drink_menu(self):
        while True:
            clear()
            print_drinks_menu_title()

            try:
                menu_selection = self.print_menu_options(self._drink_menu_options)

                if menu_selection == "List Drinks":
                    list_drinks()
                    press_enter_to_continue()
                elif menu_selection == "Add Drinks":
                    add_drinks()
                elif menu_selection == "Remove Drinks":
                    #TODO
                    pass
                elif menu_selection == "Return to Main Menu":
                    clear()
                    break
            except ValueError:
                #return to main menu
                break 
