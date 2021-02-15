#! python3 
# account.py - Handles the user's account queries
from databaseManager import DatabaseManager as dm
from query import GenereateQuery
from genereateId import GenerateId
import pyinputplus as pyip
import sys,re, password, logging, pyperclip, pprint
from config import Config
from crypt import Crypt

class Account:
    def __init__(self):
        #initializing global variables
        local = Config()
        global query, gId, dbm
        dbm = dm()
        query = GenereateQuery(local.get_user())
        gId = GenerateId(local.get_user())

    def add_existing_account(self) -> None:
        """
        Adding an existing account
        """
        # User information validation
        while True: 
            c = Crypt()
            accountId = str(gId.generate_account_id())
            username = pyip.inputStr("Enter account name:\n")
            password = Config().validate_password()
            appName = pyip.inputStr("Enter the App name or url:\n")
            note = pyip.inputStr("Enter note (OPTIONAL - Press ENTER key to skip):\n", blank=True)
            print("Account Name: %s\nPassword: %s\nApp Name: %s\nnote: %s" % (username, password, appName, note))
            yesno = pyip.inputYesNo("Is the information listed above correct?  y/n")
            if yesno == 'yes':
                break
            continue

        dbm.execute_query(query.new_account(accountId, c.encrypt(username), c.encrypt(password), appName, c.encrypt(note)))
        print("Account Name: %s\nPassword: %s\nApp Name: %s\nnote: %s\nHas uploaded successfully" % (username, password, appName, note))
        
    def create_new_account(self) -> None:
        """
        Creating a new account\n 
        Optional password genereation and copied to clipboad
        """
        while True:
            c = Crypt()
            accountId = str(gId.generate_account_id())
            username = pyip.inputStr("Enter account name:\n")
            passOpt = ["Generate a password", "Enter your own password"]
            passOption = pyip.inputMenu(passOpt, numbered=True)
            # If the user wants to genereate a password
            if passOption == passOpt[0]:
                passOpt = ["Genereate a password containing at lease 1 Upper Case, 1 number and 1 symbol", "Genereate a alphanumeric password"]
                passOption = pyip.inputMenu(passOpt, numbered=True)
                # If the user choses for a password with symbols
                if passOption == passOpt[0]:
                    psw = str(password.generate_password())
                else: 
                    psw = str(password.generate_password(2))
                print("Password %s copied to clipboard" % psw)
                pyperclip.copy(psw)
            elif passOption == passOpt[1]:
                psw = Config().validate_password()
            appName = pyip.inputStr("Enter the App name or url:\n")
            note = pyip.inputStr("Enter note (OPTIONAL - Press ENTER key to skip):\n", blank=True)
            # user checks the information is correct
            print("Account Name: %s\nPassword: %s\nApp Name: %s\nnote: %s" % (username, psw, appName, note))
            yesno = pyip.inputYesNo("Is the information listed above correct?  y/n")
            if yesno == 'yes':
                break
            continue
        # Encrypt values to store into sql
        dbm.execute_query(query.new_account(accountId, c.encrypt(username), c.encrypt(psw), appName, c.encrypt(note)))
        print("Account Name: %s\nPassword: %s\nApp Name: %s\nnote: %s\nHas uploaded successfully" % (username, psw, appName, note))
        
    def find_account(self) -> None:
        """
        Find account information based on: App name
        """
        c = Crypt()
        appName = pyip.inputStr("Enter the app name for the account you would like to find:\n")
        result = dbm.execute_query(query.find_account(appName),2)
        while result == []:
            appName = pyip.inputStr("Could not find what you're looking for. Please try again or press q to quit\n")
            if appName == 'q':
                sys.exit()
            result = dbm.execute_query(query.find_account(appName),2)
        resultList = []
        infoList = []
        i = 0
        for i in result:
            for x,y in enumerate(i):
                if x == 0 or x == 3:
                    infoList.append(y)
                else: 
                    infoList.append(c.decrypt(y))
            resultList.append(infoList)
            infoList = []
        print(resultList)

Account().find_account() 