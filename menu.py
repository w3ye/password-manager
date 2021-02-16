#! python3
# menu.py - A menu for the user 
import pyinputplus as pyip
import sys, password, clear, time, pyperclip
from config import Config
from account import Account

class Menu:

    def __init__(self):
        #initializing global variables
        clear.clear()
        global acc
        local = Config()
        inputPassword = pyip.inputPassword("Hi, " + local.get_name() + ". Please enter your password\n")
        while inputPassword != str(local.get_password()):
            inputPassword = pyip.inputPassword("Password incorrect, please retry or press q to quit: \n")
            if inputPassword == 'q':
                sys.exit()
        acc = Account()
        self.main_menu()
        
    def main_menu(self):
        """
        Main menu the user will see.
        """
        clear.clear()
        menuArr = ["Enter an account",
            "Find an account (If you want to remove an account, find the account first)",
            "Generate a password with symbols",
            "Genereate a password without symbols",
            "QUIT"]
        print('=' * 20 + ' MENU ' + '='*20)
        option = pyip.inputMenu(menuArr, numbered=True, blank=True)
        if option == menuArr[0]:
            clear.clear()
            self.account_menu()
        if option == menuArr[1]:
            clear.clear()
            acc.find_account()
        if option == menuArr[2]:
            clear.clear()
            pswd = password.generate_password()
            pyperclip.copy(pswd)
            print('Generated password %s' % pswd, '. Copied to your clipboard')
        if option == menuArr[3]:
            clear.clear()
            pswd = password.generate_password(2)
            pyperclip.copy(pswd)
            print('Generated password %s' % pswd, '. Copied to your clipboard')
        if option == menuArr[-1]:
            sys.exit()
        time.sleep(2)
        self.main_menu()
    
    
    def account_menu(self):
        """
        A menu for account 
        """
        menuArr = ["Enter an existing account",
            "Creating a new account",
            "Main Menu",
            "QUIT"]
        print('=' * 20 + ' ACCOUNT ' + '='*20)
        option = pyip.inputMenu(menuArr, numbered=True, blank=True)
        if option == menuArr[0]:
            acc.add_existing_account()
        if option == menuArr[1]:
            acc.create_new_account()
        if option == menuArr[-2]:
            self.main_menu()
        if option == menuArr[-1]:
            sys.exit()
        time.sleep(2)
        self.main_menu()