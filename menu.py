#! python3
# menu.py - A menu for the user 
from databaseManager import DatabaseManager as dm
from query import GenereateQuery
from genereateId import GenerateId as gId
import pyinputplus as pyip
import sys,re, password, pprint, logging
from config import Config

logging.basicConfig(level=logging.CRITICAL, format=' %(funcName)s - %(levelname)s: %(message)s')

class Menu:

    def __init__(self):
        local = Config()
        inputPassword = pyip.inputPassword("Hi, " + local.get_name() + ". Please enter your password\n")
        while inputPassword != str(local.get_password()):
            inputPassword = pyip.inputPassword("Password incorrect, please retry or press q to quit: \n")
            if inputPassword == 'q':
                sys.exit()

        global query
        query = GenereateQuery(local.get_user())

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
        option = pyip.inputMenu(menuArr, numbered=True, blank=True).lower()
        
        if option == "main menu":
            self.main_menu()
        if option == menuArr[-1]:
            sys.exit()

    def add_account(self):
        accountId = gId().generate_account_id()
        print(accountId)
        pass

    def find_account(self):
        pass

    def remove_account(self):
        pass

class Test:
    def add_account(self):
        accountId = gId().generate_account_id()
        username = pyip.inputStr("Enter username")
        password = pyip.inputStr("Enter the password")
        appName = pyip.inputStr("Enter the App name")
        notes = pyip.inputStr("Enter note(Enter to skip)")
        notes = re.compile(r'*\s*').sub('',notes)
        

Menu()