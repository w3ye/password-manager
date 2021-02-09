#! python3
# menu.py - A menu for the user 
from databaseManager import DatabaseManager as dm
from query import GenereateQuery
from genereateId import GenerateId as gId
import pyinputplus as pyip
import sys,re, password, pprint
from config import Config

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
        accountId = gId().generate_account_id()
        username = pyip.inputStr("Enter username:\n")
        password = Config.validate_password()
        appName = pyip.inputStr("Enter the App name or url:\n")
        note = pyip.inputStr("Enter note (OPTIONAL - Press ENTER key to skip):\n")
        
        query.new_account(accountId, username, password, appName, note)

    def find_account(self):
        pass

    def remove_account(self):
        pass

class Test:
    def add_account(self):
        accountId = gId().generate_account_id()
        username = pyip.inputStr("Enter username")
        password = Config().validate_password()
        appName = pyip.inputStr("Enter the App name or url")
        notes = pyip.inputStr("Enter note (OPTIONAL - Press ENTER key to skip)")
        print(accountId)
        print(username)
        print(password)
        print(appName)
        print(notes)
        

Test().add_account()