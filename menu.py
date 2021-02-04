from databaseManager import DatabaseManager as dm, GenereateQuery as query
import sys
import secretPassword 

class Menu:
    def __init__(self):
        print("Enter the number of your choice")
        print("(1) Add account")
        print("(2) Find account")
        print("(q) to quit")
        choice = input()
        if choice == 'q':
            sys.exit()
        if choice == '1':
            self.add_account()

    def add_account(self):
        print("Please enter your username")
        username = input()
        print("Do you want to genereate a password? y/n")
        choice = input()
        # if the user wants a generated password
        # TODO if the user enters something else, let them enter it again
        if choice.lower() == 'y':
            print("Do you need symbols in your password? y/n")
            choice = input()
            # if the user need symbols in their password
            if choice.lower() == 'y':
                password = secretpassword.generate_password()
            # if the user just wants an alphanumeric password
            # TODO if the user enters something else, let them enter it again
            else: password = secretpassword.generate_password(2)
        else:
            print("Enter your password")
            password = input()
        print("Please enter the url for the password")
        url = input()
        print("Do you want to add any notes to for this account? (Press enter if you don't want to add a note)")
        note = input()
        #TODO display all the account details, check if they need any changes
        #TODO generate account_id not done
        query = query().GenereateQuery().new_account(accountId,username,password,url,note)

Menu()