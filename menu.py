#! python3
# menu.py - A menu for the user 
from databaseManager import DatabaseManager as dm
from query import GenereateQuery
from genereateId import GenerateId as gId
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
        menuArr = ["Enter an account",
            "Find an account (If you want to remove an account, find the account first)",
            "Generate a password",
            "QUIT"]
        print('=' * 20 + ' MENU ' + '='*20)
        option = pyip.inputMenu(menuArr, numbered=True, blank=True).lower()
        if option == "enter an account":
            self.account_menu()
        if option == menuArr[-1]:
            sys.exit()
    
    def remove_spaces(self, opt):
        opt = re.compile(r'/s*').sub('',opt)
        return opt
    
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
        

Test().add_account()