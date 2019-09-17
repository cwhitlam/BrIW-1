from UI import UI
from IO import Pickle_IO
from classes import Drink, Person, Round

#test brancing

class Menu:
    def __init__(self):
        self._ui = UI()
        self._io = Pickle_IO()
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
            menu_row += f"{' ' * (self._ui.header_width - len(menu_row)-1)}|"
            print(menu_row)
        
        self._ui.print_header()
        return menu_options[int(input("Option: "))]

        
    def main_menu(self):
        self._ui.clear()
        self._ui.print_main_menu_title()
        
        try:
            menu_selection = self.print_menu_options(self._main_menu_options)
            
            if menu_selection == "People":
               self.people_menu()
            elif menu_selection == "Drinks":
                self.drink_menu()
            else:
                self._ui.clear()
                print("Thank You for using BrIW™. See you again soon! ^_^")
                exit()
        except ValueError:
            exit()

    def people_menu(self):
        while True:
            self._ui.clear()
            self._ui.print_people_menu_title()
            
            try:
                menu_selection = self.print_menu_options(self._people_menu_options)
                self._ui.clear()

                if menu_selection == "List People":
                    self.list_people()                
                elif menu_selection == "Add People":
                    self.add_people()
                elif menu_selection == "Remove People":
                    #TODO
                    pass
                elif menu_selection == "Change Drink Preference":
                    #TODO
                    pass
                elif menu_selection == "Return to Main Menu":
                    self._ui.clear()
                    break
            except ValueError:
                #return to main menu
                break 

    def drink_menu(self):
        while True:
            self._ui.clear()
            self._ui.print_drinks_menu_title()

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
                    self._ui.clear()
                    break
            except ValueError:
                #return to main menu
                break


    def list_people(self):
        people = self._io.unpickle("people")
        
        header_width = self._ui.header_width #taking a local copy in function as to not affect the state of the wider application
        second_col_index = int(header_width / 2)
        max_name_length = max(len(person.full_name) for person in people.values())
        max_id_digits = max(len(str(key)) for key in people.keys())
        
        #if a name is larger than the width of the first col, increase header width and re-evalute until name will fit
        while max_name_length > second_col_index:
            header_width = int(header_width * 1.05)
            second_col_index = int(header_width / 2)

        self._ui.print_people_menu_title()

        column_headers = "| Name"
        column_headers += f"{' ' * (second_col_index - len(column_headers)-1)}| Preference"
        column_headers += f"{' ' * (header_width - len(column_headers)-1)}|"
        print(column_headers)
        self._ui.print_header()

        for p_id, person in people.items():
            id_padding = 0 if len(str(p_id)) == max_id_digits else max_id_digits - len(str(p_id))
            person_row = f"| {p_id}. {' ' * id_padding}{person.full_name}"
            person_row += f"{' ' * (second_col_index - len(person_row)-1)}| {person.fav_drink.name}"
            person_row += f"{' ' * (header_width - len(person_row)-1)}|"
            print(person_row)

        self._ui.print_header()
        self._ui.press_enter_to_continue()

    def add_people(self):
        while True:
            self._ui.print_people_menu_title(True)
            
            first_name = input("What is the new persons first name?: ").capitalize()
            last_name = input("what is the new persons last name?: ").capitalize()
            #TODO select new persons drink preference
            fav_drink = None
            
            self._ui.print_people_menu_title(True)
            print(f"First Name: {first_name}")
            print(f"Last Name: {last_name}")
            print(f"Favourite Drink: {'No Preference' if fav_drink is None else fav_drink.fav_drink}")
            print()
            print("Please check the details you have entered above are correct.")
            if input("Would you like to submit the entered details? (Y/N): ").upper() == "Y":
                self._ui.print_people_menu_title(True)
                
                try:
                    self._ui.print_people_menu_title(True)

                    people = self._io.unpickle("people")
                    new_id = max(people.keys())+1
                    new_person = Person(new_id, first_name, last_name, fav_drink)

                    people[new_id] = new_person
                    self._io.picklize("people", people)
                    print("new person succesfully added.")
                except Exception as e:
                    print(f"there was an issue saving the new person. Message: {e}")
            else:
                self._ui.print_people_menu_title(True)
                print("The new person entry was aborted")
                self._ui.press_enter_to_continue()
                self._ui.print_people_menu_title(True)

            if input("Would you like to add someone else?(Y/N): ").upper() == "N":
                break

