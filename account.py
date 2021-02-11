#! python3 
# account.py - Handles the user's account queries
from databaseManager import DatabaseManager as dm
from query import GenereateQuery
from genereateId import GenerateId
import pyinputplus as pyip
import sys,re, password, logging, pyperclip
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

    def add_existing_account(self):
            """
            Adding an existing account
            """
            c = Crypt()
            accountId = str(gId.generate_account_id())
            username = pyip.inputStr("Enter account name:\n")
            password = Config().validate_password()
            appName = pyip.inputStr("Enter the App name or url:\n")
            note = pyip.inputStr("Enter note (OPTIONAL - Press ENTER key to skip):\n", blank=True)

            dbm.execute_query(query.new_account(c.encrypt(accountId), c.encrypt(username), c.encrypt(password), c.encrypt(appName), c.encrypt(note)))
            print("Account Name: %s\nPassword: %s\n App Name: %s\n note: %s\nHas uploaded successfully" % (username, password, appName, note))
        
    def create_new_account(self):
        """
        Creating a new account\n 
        Optional password genereation and copied to clipboad
        """
        c = Crypt()
        accountId = str(gId.generate_account_id())
        username = pyip.inputStr("Enter account name:\n")
        
    def find_account(self):
        
        pass

    def remove_account(self):
        pass

Account().add_existing_account() 