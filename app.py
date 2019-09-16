import os
from classes import Round, Person, Drink
from UI import UI
from Menu import Menu
import pickle


ui = UI()
menu = Menu()


#PROGRAM FLOW
while True:
    ui.clear()
    #main menu functionality
    menu.main_menu()
