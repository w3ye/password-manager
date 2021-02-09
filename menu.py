#! python3
# menu.py - A menu for the user 
from databaseManager import DatabaseManager as dm
from query import GenereateQuery
import pyinputplus as pyip
import sys,re
import password 
import pprint
from config import Config

class Menu:

    def __init__(self):
        user = Config().local_user_config()
        inputPassword = pyip.inputPassword("Hi, " + user['user'] + ". Please enter your password\n")

        while inputPassword != user['password']:
            inputPassword = pyip.inputPassword("Password incorrect, please retry(press q to quit): \n")
            if inputPassword == 'q':
                sys.exit()
        
        global query
        query = GenereateQuery(user['user'])

        self.main_menu()
        


    def main_menu(self):
        menuArr = ["Enter an account",\
            "Find an account", \
            "Generate a password",
            "QUIT"]
        print('=' * 20 + ' MENU ' + '='*20)
        option = pyip.inputMenu(menuArr, numbered=True, blank=True).lower()
        if option == "enter an account":
            self.account_menu()
        if option == "quit":
            sys.exit()
    
    def remove_spaces(self, opt):
        opt = re.compile(r'/s*').sub('',opt)
        return opt
    
    def account_menu(self):
        menuArr = ["Enter an existing account", \
            "Creating a new account", \
            "Main Menu", \
            "QUIT"]
        print(query)
        print('=' * 20 + ' ACCOUNT ' + '='*20)
        option = pyip.inputMenu(menuArr, numbered=True, blank=True).lower()
        
        if option == 'main menu':
            self.main_menu()

    def add_account(self):
        
        pass
        
Menu()