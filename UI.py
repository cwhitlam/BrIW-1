import os

class UI:
    header_width = 72
    main_menu_options = {
        1: "People",
        2: "Drinks",
        3: "Exit Application"
    }
    people_menu_options = {
        1: "List People",
        2: "Add People",
        3: "Remove People",
        4: "Change Drink Preference"
    }
    drink_menu_options = {
        1: "List Drinks",
        2: "Add Drnks",
        3: "Remove Drinks"
    }

    def __init__(self):
        pass

    def print_header(self):
        print(f"+ {'=' * (self.header_width - 4)} +")

    def print_main_menu(self):
        main_menu_text = """+ ==================================================================== +
|  _      __        __                             __                  |
| | | /| / / ___   / / ____ ___   __ _  ___       / /_ ___             |
| | |/ |/ / / -_) / / / __// _ \ /  ' \/ -_)     / __// _ \ _  _  _    |
| |__/|__/  \__/ /_/  \__/ \___//_/_/_/\__/      \__/ \___/(_)(_)(_)   |
|                                                                      |
|                ____             ____ _       __    __                |
|               / __ )   _____   /  _/| |     / /   / /                |
|              / __  |  / ___/   / /  | | /| / /   / /                 |
|             / /_/ /  / /     _/ /   | |/ |/ /   /_/                  |  
|            /_____/  /_/     /___/   |__/|__/   (_)                   |
|                                                                      |
+ ==================================================================== +"""
        for key, val in self.main_menu_options.items():
            main_menu_row = f"\n| [{key}] {val}"
            main_menu_row += f"{' ' * (self.header_width - len(main_menu_row))}|"
            main_menu_text += main_menu_row
        print(main_menu_text)
        self.print_header()

    def print_people_menu(self):
        people_menu_text = """"     ___  ____    ___    __    ____
   / _ \  / __/ / __ \  / _ \  / /   / __/
  / ___/ / _/  / /_/ / / ___/ / /__ / _/  
 /_/    /___/  \____/ /_/    /____//___/  
                                         


        """
        print(people_menu_text)


    def print_drinks_menu(self):
        pass


    def press_enter_to_continue(self):
        input("Press Enter to return to menu ")


    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")
