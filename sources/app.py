from menu import Menu
from functions import *

def main():
    
    clear()
    main_menu = Menu(menu_options, "BrIW")
    main_menu.build_menu()

if __name__ == "__main__":
    main()
