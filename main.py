from menu import Menu
from functions import *

def main():
    while True:
        menu_options = {
            1: "People",
            2: "Drinks",
            3: "Exit"
        }
        main_menu = Menu(menu_options, "BrIW")
        main_menu.build_menu()
        press_enter_to_continue()

if __name__ == "__main__":
    main()
