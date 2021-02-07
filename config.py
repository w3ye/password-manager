#! python3
# config.py - Read and store user configs
import os,re
from pathlib import Path
import shelve, pyinputplus as pyip
from databaseManager import DatabaseManager as dm
from typing import Dict

class Config:

    def __init__(self):
        self.validate_path()

    def validate_path(self) -> None:
        """
        Check if the config file exisits\n
        Create a config directory 
        """
        path = Path('./config')
        if not path.exists():
            os.mkdir('./config')

    
    def local_user_config(self) -> Dict:
        """
        Read the user config file
        """
        path = Path('./config')
        # Check if the user_config file exists
        if list(path.glob('user_config.*')) == []:
            self.create_user_config()
        
        user = {}
        # If user_config file exists
        # Read the contents of it 
        sFile = shelve.open('./config/user_config')
        user['user'] = sFile['user']
        user['password'] = sFile['password']
        
        return user

    def create_user_config(self) -> None:
        """
        Creates a user config file
        """
        print("Seems like you're information is not on file. Let's set up")
        user = pyip.inputStr("Please enter a username:\n")
        while True:
            # Remove spaces in the username
            user = re.compile(r'\s*').sub('',user)
            # Checks in sql if a table with 'user' name exists
            checkUser = dm().execute_query("SHOW TABLES LIKE '%s'" % user,2)
            # if it doesn't create a table
            if checkUser == []:
                dm().execute_query("""
                    create table %s(
                    account_id int primary key,
                    username varchar(255) not null,
                    psword varchar(255) not null,
                    app_name varchar(255) not null,
                    note varchar(255) default null
                    );
                """ % user, 0) 
                break
            # if it exists ask the user to eneter another name
            else:
                user = pyip.inputStr("Username taken. Please enter another username:\n")
        
        # Make sure the user enter's both password correctly
        while True:
            pass1 = pyip.inputPassword("Please enter a password:\n")
            pass2 = pyip.inputPassword("Confirm your password:\n")
            if pass1 == pass2:
                break
            continue
            
        # write the user info into shelve file
        shelfFile = shelve.open('./config/user_config')
        shelfFile['user'] = user
        shelfFile['password'] = pass1
        shelfFile.close()