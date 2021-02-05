#! python3
# menu.py - A menu for the user 
from databaseManager import DatabaseManager as dm
import pyinputplus as pyip
import sys,re
import password 
import pprint

class Menu:
    def __init__(self):
        self.main_menu()

    def main_menu(self):
        print('=' * 20 + ' MENU ' + '='*20)
        option = pyip.inputMenu([\
            "Enter an account",\
            "Find an account", \
            "Generate a password",
            "quit"], numbered=True, blank=True).lower()
        if option == "enter an account":
            self.account_menu()
        if option == "quit":
            sys.exit()
    
    def remove_spaces(self, opt):
        opt = re.compile(r'/s*').sub('',opt)
        return opt
    
    def account_menu(self):
        print('=' * 20 + ' ACCOUNT ' + '='*20)
        option = pyip.inputMenu([\
            "Enter an existing account", \
            "Creating a new account", \
            "Main Menu"], numbered=True, blank=True).lower()
        
        if option == 'main menu':
            self.main_menu()


        
Menu()