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
import clear

class Account:
    def __init__(self):
        #initializing global variables
        local = Config()
        global query, gId, dbm, c
        dbm = dm()
        query = GenereateQuery(local.get_user())
        gId = GenerateId(local.get_user())
        c = Crypt()

    def add_existing_account(self) -> None:
        """
        Adding an existing account
        """
        # User information validation
        while True: 
            accountId = str(gId.generate_account_id())
            username = pyip.inputStr("Enter account name:\n")
            pswd = password.confirm_password()
            appName = pyip.inputStr("Enter the App name or url:\n")
            note = pyip.inputStr("Enter note (OPTIONAL - Press ENTER key to skip):\n", blank=True)
            print("Account Name: %s\nPassword: %s\nApp Name: %s\nnote: %s" % (username, pswd, appName, note))
            yesno = pyip.inputYesNo("Is the information listed above correct?  y/n:\t")
            if yesno == 'yes':
                break
            continue

        dbm.execute_query(query.new_account(accountId, c.encrypt(username), c.encrypt(pswd), appName, c.encrypt(note)))
        clear.clear()
        print("Account Name: %s\nPassword: %s\nApp Name: %s\nnote: %s\nHas uploaded successfully" % (username, pswd, appName, note))
        
    def create_new_account(self) -> None:
        """
        Creating a new account\n 
        Optional password genereation and copied to clipboad
        """
        clear.clear()
        while True:
            accountId = str(gId.generate_account_id())
            username = pyip.inputStr("Enter account name:\n")
            psw = password.password_choice()
            appName = pyip.inputStr("Enter the App name or url:\n")
            note = pyip.inputStr("Enter note (OPTIONAL - Press ENTER key to skip):\n", blank=True)
            # user checks the information is correct
            print("Account Name: %s\nPassword: %s\nApp Name: %s\nnote: %s" % (username, psw, appName, note))
            yesno = pyip.inputYesNo("Is the information listed above correct?  y/n\t")
            if yesno == 'yes':
                break
            continue
        # Encrypt values to store into sql
        dbm.execute_query(query.new_account(accountId, c.encrypt(username), c.encrypt(psw), appName, c.encrypt(note)))
        clear.clear()
        print("Account Name: %s\nPassword: %s\nApp Name: %s\nnote: %s\nHas uploaded successfully" % (username, psw, appName, note))
        
    def find_account(self) -> None:
        """
        Find account information based on: App name
        """
        clear.clear()
        appName = pyip.inputStr("Enter the app name for the account you would like to find (Enter #all# to find all accounts):\n")
        clear.clear()
        if appName == '#all#':
            result = dbm.execute_query(query.find_all(),2)
        else:
            result = dbm.execute_query(query.find_account(appName),2)
        while result == []:
            appName = pyip.inputStr("Could not find what you're looking for. Your database could be empty. Please try again or press q to quit\n")
            if appName == 'q':
                sys.exit()
            if appName == '#all#':
                result = dbm.execute_query(query.find_all(),2)
            else:
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
            
        selectedAccount = self.select_account(resultList)
        self.account_options(selectedAccount)
        
    
    def select_account(self, resultList: List[List]) -> List:
        """
        If there is more than 1 account with the same app, the user gets to chose which account to modify or get password
        """
        # When there is only 1 account with an app
        if len(resultList) == 1:
            print(*resultList)
            pyperclip.copy(resultList[0][2])
            print('*'*10, "Password copied to clipboard", '*'*10)
            return resultList[0]
        # When there are multiple account linked to an app
        else: 
            for num, account in enumerate(resultList):
                print(num+1, '\t', account)
            choice = pyip.inputInt("Select the account you want to choose:\t")
            while choice-1 > len(resultList):
                choice = pyip.inputInt("Option unavailable. Please choose again:\t", blank=True)
            clear.clear()
            print(resultList[choice-1])
            pyperclip.copy(resultList[choice-1][2])
            print('*'*10, "Password copied to clipboard", '*'*10)
            return resultList[choice-1]
        
    def account_options(self, account: List) -> None:
        """
        User is presented with options to do with the account
        """
        accountOpt = ["Update Password", "Remove account", "Main Menu"]
        choice = pyip.inputMenu(accountOpt,blank=True, numbered=True, prompt="Please select one of the following (Empty will take you back to find account):\n")
        # if choice is left blank. Go back to the previous section
        if len(choice) == 0:
            self.find_account()
        if choice == accountOpt[-1]:
            return None
        # Update Password
        if choice == accountOpt[0]:
            clear.clear()
            print("Changing password for: ", end='   ')
            for i in account:
                print('   |   ', i , end=' '*3)
            print()
            pswd = password.password_choice()
            print(pswd)
            dbm.execute_query(query.change_password(account[0],c.encrypt(pswd)))
            account[2] = pswd
            print("Password change success!", end=' '*3)
            for i in account:
                print('   |   ', i , end=' '*3)
            print()
        # Delete account
        if choice == accountOpt[1]:
            dbm.execute_query(query.delete_account(account[0]))
            print(account[0], "\tSuccessful deleted")
