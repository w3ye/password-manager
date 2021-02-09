#! python3
# config.py - Read and store user configs
import os,re,sys
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
            self.user_menu()
        
        user = {}
        # If user_config file exists
        # Read the contents of it 
        sFile = shelve.open('./config/user_config')
        user['user'] = sFile['user']
        user['password'] = sFile['password']
        
        return user

    def user_menu(self) -> None:
        """
        User can chose between creating a new sql table or enter an exisiting one
        """
        menuArr = ["Create a new user",
            "Already have a username",
            "QUIT"]
        print('=' * 20 + ' USER ' + '=' * 20)
        option = pyip.inputMenu(menuArr, numbered=True).lower()
        # If the user wants to create a new user/new sql table 
        if option == menuArr[0]:
            self.existing_user()
        # If the user already has a sql table
        if option == menuArr[1]:
            pass
        # If the user wants to quit
        if option == menuArr[-1]:
            sys.exit()
    
    def existing_user(self) -> None:
        """
        If the user already have an existing user
        """
        name = pyip.inputStr("Enter your name:\n")
        user = pyip.inputStr("Enter your username:\n")
        while self.check_sql_table(user):
            user = pyip.inputStr("Username Does not exist. Please enter it again. (Enter q to quit or b to go back to the previous menu)")
            # if user enters q: exit the program
            if user == 'q':
                sys.exit()
            # if user enters b: go back to the user menu
            if user == 'b':
                self.user_menu()
        password = self.validate_password(password)
    
    def write_user_config(self, name, user, password, email) -> None:
        """
        Writes the local user information into a shelf file
        """
        # write the user info into shelve file
        shelfFile = shelve.open('./config/user_config')
        shelfFile['name'] = name
        shelfFile['user'] = user
        shelfFile['password'] = password
        shelfFile['email'] = email
        shelfFile.close()
        
            
    
    def check_sql_table(self, user) -> bool:
        """
        Check if the table name exists\n
        True -> table name does not exist\n
        False -> table name exists
        """
        checkUser = dm().execute_query("SHOW TABLES LIKE '%s'" % user,2)
        # if table doesn't exist in database
        if checkUser == []:
            return True
        return False
    
    def create_sql_table(self, user) -> None:
        """
        Creating an sql table with the username
        """
        dm().execute_query("""
            create table %s(
            account_id int primary key,
            username varchar(255) not null,
            psword varchar(255) not null,
            app_name varchar(255) not null,
            note varchar(255) default null
            );
        """ % user, 0)

    def validate_password(self) -> str:
        """
        User enters password and confirms that p1 == p2
        """
        while True:
            p1 = pyip.inputPassword("Enter password:\n")
            p2 = pyip.inputPassword("Confirm password:\n")
            if p1 == p2:
                return p1
            print("Password does not match please try again")

    def validate_email(self):
        """
        Validate user email\n
        User enters email twice, both email values must match and in the right email format
        """
        emailRegx = re.compile(r'''
            [a-zA-Z0-9._%+-]+       # username
            @                       # @ symbol
            [a-zA-Z0-9.-]+          # domain name
            (\.[a-zA-Z]{2,4})       # dot something
        ''', re.VERBOSE)

        while True:
            e1 = pyip.inputStr("Enter your email:\n")
            e2 = pyip.inputStr("Confirm your email\n")
            # If the email format is incorrect, user types in their information again
            if not (re.search(emailRegx,e1)):
                print("Email format incorrect")
                continue
            # Return the email if e1 == e2
            if e1 == e2:
                return e1

    def create_user_config(self) -> None:
        """
        Creates a user config file
        """
        print("Seems like you're information is not on file. Let's set up")
        # User input their name
        name = pyip.inputStr("Please enter your name")
        # User input their username which is also used as table name in mysql
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

print(Config().validate_email())