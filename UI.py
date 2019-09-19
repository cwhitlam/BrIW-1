import os

def get_header():
    return 72

def print_header():
    print(f"+ {'=' * (get_header() - 4)} +")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def print_main_menu_title():
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
    print(main_menu_text)


def print_people_menu_title(clear_term=False):
    if clear_term:
        clear()

    people_ascii_title = """|    ___    ____  ____    ___    __    ____
|   / _ \  / __/ / __ \  / _ \  / /   / __/
|  / ___/ / _/  / /_/ / / ___/ / /__ / _/  
| /_/    /___/  \____/ /_/    /____//___/ 
|"""
    print_header()
    #loops through each line of ascii title and works out blank space
    #then applies border end using |
    for line in iter(people_ascii_title.splitlines()):
        print(line + f"{' ' * (get_header() - len(line)-1)}|")
    print_header()


def print_drinks_menu_title(clear_term=False):
    if clear_term:
        clear()

    drink_ascii_title = """|     ____     ____     ____    _   __    __ __   _____
|    / __ \   / __ \   /  _/   / | / /   / //_/  / ___/
|   / / / /  / /_/ /   / /    /  |/ /   / ,<     \__ \ 
|  / /_/ /  / _, _/  _/ /    / /|  /   / /| |   ___/ / 
| /_____/  /_/ |_|  /___/   /_/ |_/   /_/ |_|  /____/  
|"""

    print_header()
    #loops through each line of ascii title and works out blank space
    #then applies border end using |
    for line in iter(drink_ascii_title.splitlines()):
        print(line + f"{' ' * (get_header() - len(line)-1) }|")
    print_header()


def press_enter_to_continue():
    input("Press Enter to continue ")
