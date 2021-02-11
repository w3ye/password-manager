#! python3
# menu.py - A menu for the user 
from databaseManager import DatabaseManager as dm
from query import GenereateQuery
from genereateId import GenerateId
import pyinputplus as pyip
import sys,re, password, pprint, logging
from config import Config

logging.getLogger("Menu").setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
        global gId
        gId = GenerateId(local.get_user())

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
        
        if option == menuArr[0]: self.add_existing_account()
        if option == menuArr[-2]:
            self.main_menu()
        if option == menuArr[-1]:
            sys.exit()

    def add_existing_account(self):
        """
        Adding an existing account
        """
        logging.debug('Method start')
        accountId = gId.generate_account_id()
        username = pyip.inputStr("Enter username:\n")
        password = Config().validate_password()
        appName = pyip.inputStr("Enter the App name or url:\n")
        note = pyip.inputStr("Enter note (OPTIONAL - Press ENTER key to skip):\n", blank=True)

        print('accountId: %s  | username: %s | password: %s | appName: %s | note: %s' % (accountId, username, password, appName, note))
        
        # k = (query.new_account(accountId, username, password, appName, note))
        # print(k)

    def find_account(self):
        pass

    def remove_account(self):
        pass

class Test:
    def add_account(self):
        #accountId = gId().generate_account_id()
        username = pyip.inputStr("Enter username")
        password = Config().validate_password()
        appName = pyip.inputStr("Enter the App name or url")
        notes = pyip.inputStr("Enter note (OPTIONAL - Press ENTER key to skip)")
        print(accountId)
        print(username)
        print(password)
        print(appName)
        print(notes)
        
Menu()