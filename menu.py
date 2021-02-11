#! python3
# menu.py - A menu for the user 
from databaseManager import DatabaseManager as dm
from query import GenereateQuery
from genereateId import GenerateId as gId
import pyinputplus as pyip
import sys,re, password, pprint
from config import Config
from crypt import Crypt

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

        #self.main_menu()
        
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

    def add_existing_account(self):
        """
        Adding an existing account
        """
        accountId = Crypt().encrypt(str(gId().generate_account_id()))
        username = Crypt().encrypt(pyip.inputStr("Enter username:\n"),blank=False)
        password = Crypt().encrypt(Config.validate_password(), blank=False)
        appName = Crypt().encrypt(pyip.inputStr("Enter the App name or url:\n"), blank=False)
        note = Crypt().encrypt(pyip.inputStr("Enter note (OPTIONAL - Press ENTER key to skip):\n"),blank=True)
        
        dm.execute_query(query.new_account(accountId, username, password, appName, note))

    def find_account(self):
        
        pass

    def remove_account(self):
        pass

class Test:
    def add_account(self):
        pass
        

Test().add_account()