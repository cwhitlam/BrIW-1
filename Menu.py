from UI import *
from data_io import *
from classes import Drink, Person, Round

class Menu:
    def __init__(self):
        self._main_menu_options = {
            1: "People",
            2: "Drinks",
            3: "Exit Application"
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
            2: "Add Drnks",
            3: "Remove Drinks",
            4: "Return to Main Menu"
        }
    
    #prints provided menu options to user and returns their selection
    def print_menu_options(self, menu_options):
        for key, val in menu_options.items():
            menu_row = f"| [{key}] {val}"
            menu_row += f"{' ' * (header_width - len(menu_row)-1)}|"
            print(menu_row)
        
        print_header()
        return menu_options[int(input("Option: "))]

        
    def main_menu(self):
        clear()
        print_main_menu_title()
        
        try:
            menu_selection = self.print_menu_options(self._main_menu_options)
            
            if menu_selection == "People":
               self.people_menu()
            elif menu_selection == "Drinks":
                self.drink_menu()
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
                    self.list_people()                
                elif menu_selection == "Add People":
                    add_people()
                elif menu_selection == "Remove People":
                    #TODO
                    pass
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
                    #TODO
                    pass
                elif menu_selection == "Add Drinks":
                    #TODO
                    pass
                elif menu_selection == "Remove Drinks":
                    #TODO
                    pass
                elif menu_selection == "Return to Main Menu":
                    clear()
                    break
            except ValueError:
                #return to main menu
                break


    def list_people(self):
        people = unpickle("people")
       
        header = header_width
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
        column_headers += f"{' ' * (header_width - len(column_headers)-1)}|"
        print(column_headers)
        print_header()

        for p_id, person in people.items():
            id_padding = 0 if len(str(p_id)) == max_id_digits else max_id_digits - len(str(p_id))
            person_row = f"| {p_id}. {' ' * id_padding}{person.full_name}"
            person_row += f"{' ' * (second_col_index - len(person_row)-1)}| {person.fav_drink.name}"
            person_row += f"{' ' * (header_width - len(person_row)-1)}|"
            print(person_row)

        print_header()
        press_enter_to_continue()
