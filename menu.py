from pyfiglet import Figlet
from prettytable import PrettyTable
from functions import *

class Menu:
    def __init__(self, menu_options, header_text):
        self.options = menu_options
        self.header_text = header_text

    def generate_ascii_art(self, text):
        figlet = Figlet(font="slant")
        return figlet.renderText(text)

    #TODO GENERATE MENU AND GET INPUT FOR FACTORY

    def build_menu(self):
        print(self.generate_ascii_art(self.header_text))
            
        for key, val in self.options.items():
            print(f"[{key}]. {val} {self.header_text.lower().capitalize()}")

        user_selection = self.options[get_option()]

        factory = MenuFactory()
        factory.action(header_text, user_selection)

class MenuFactory:
    def action(self, menu, option):
        action = self._get_action(option)
        return action(menu, option)

    def _get_action(self, option):
        if option == "Add":
            return self._add_item
        elif option == "Remove":
            return self._remove_item
        elif option == "Preference":
            return self._change_preference
        elif option == "Exit":
            return self._exit
        elif option == "People" or option == "Drinnks":
            return self._create_menu
        else:
            raise ValueError("Menu Option Not Recognised")

    def _create_menu(self, menu, option): 
        print("menu created")

    def _add_item(self, menu, option):
        print("item added")

    def _remove_item(self, menu, option):
        print("item removed")

    def _change_preference(self, menu, option):
        print("preference changed")

    def _exit(self, menu, option):
        print("menu exited")
