#! python3
# menu.py - A menu for the user 
import pyinputplus as pyip
import sys
from config import Config
from account import Account

class Menu:

    def __init__(self):
        #initializing global variables
        local = Config()
        inputPassword = pyip.inputPassword("Hi, " + local.get_name() + ". Please enter your password\n")
        while inputPassword != str(local.get_password()):
            inputPassword = pyip.inputPassword("Password incorrect, please retry or press q to quit: \n")
            if inputPassword == 'q':
                sys.exit()

        self.main_menu()
        
    def main_menu(self):
        """
        Main menu the user will see.
        """
        menuArr = ["Enter an account",
            "Find an account (If you want to remove an account, find the account first)",
            "Generate a password",
            "QUIT"]
        print('=' * 20 + ' MENU ' + '='*20)
        option = pyip.inputMenu(menuArr, numbered=True, blank=True)
        if option == menuArr[0]:
            self.account_menu()
        if option == menuArr[-1]:
            sys.exit()
    
    
    def account_menu(self):
        menuArr = ["Enter an existing account",
            "Creating a new account",
            "Main Menu",
            "QUIT"]
        print('=' * 20 + ' ACCOUNT ' + '='*20)
        option = pyip.inputMenu(menuArr, numbered=True, blank=True)
        
        if option == menuArr[-2]:
            self.main_menu()
        if option == menuArr[-1]:
            sys.exit()
        
Menu()