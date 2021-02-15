#! python3 
# account.py - Handles the user's account queries
from databaseManager import DatabaseManager as dm
from query import GenereateQuery
from genereateId import GenerateId
import pyinputplus as pyip
import sys,re, password, logging, pyperclip, pprint
from config import Config
from crypt import Crypt
from typing import List

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
        
    
    def select_account(self, resultList: List[List]) -> List:
        """
        If there is more than 1 account with the same app, the user gets to chose which account to modify or get password
        """
        # When there is only 1 account with an app
        if len(resultList) == 1:
            print(*resultList)
            pyperclip.copy(resultList[0][2])
            print("Password copied to clipboard")
            return resultList[0]
        # When there are multiple account linked to an app
        else: 
            for num, account in enumerate(resultList):
                print(num+1, '\t', account)
            choice = pyip.inputInt("Select the account you want to choose:\t")
            while choice-1 > len(resultList):
                choice = pyip.inputInt("Option unavailable. Please choose again:\t")
            print(resultList[choice-1])
            pyperclip.copy(resultList[choice-1][2])
            print("Password copied to clipboard")
            return resultList[choice-1]




resultList = [['6369773579', 'benwgye@gmail.com', 'DUuMf579DPEv9', 'www.discord.com', ''], ['7069138754', 'dddd', 'y&riv2TRbP8r', 'www.discord.com', '123321'], ['919253408', 'w3ye@pm.me', ',~QjPrkq&25M4', 'www.discord.com', '']]
singleList = [['6369773579', 'benwgye@gmail.com', 'DUuMf579DPEv9', 'www.discord.com', '']]
Account().select_account(resultList) 