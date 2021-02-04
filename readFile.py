#! python3
# ReadFile.py - Get mySql Credential from a text file

from typing import List, Dict
import re
class Credentials:

    # Get sql credentials from text file
    def read_file(self) -> List:
        data = None
        try:
            with open('sqlCred.txt') as file:
                data = file.readlines()
            file.close
        except FileNotFoundError as err:
            print("OS error: {0}".format(err))
        return data

    # Process the data from 'read_file()'
    def get_cred(self) -> Dict:
        data = self.read_file()
        cred = {}
        # Setting key and value for Dict
        for i in data:
            noSpace = re.compile(r'\s*').sub('',i.lower())  # Removing space in 'i'
            temp = noSpace.split('=')   # Split 'noSpace' by delimiter('=')
            
            # Setting synonyms  nouns to a specific one using regex
            if re.compile(r'host|host.|endpoint', re.VERBOSE).search(temp[0]) != None:
                temp[0] = 'host'
            if re.compile(r'user.').search(temp[0]) != None:
                temp[0] = 'user'
            if re.compile(r'password | pass', re.VERBOSE).search(temp[0]) != None:
                temp[0] = 'password'
            cred[temp[0]] = temp[1]         # Store the data read from the textfile into dictionary 'cred'

        # Makes sure that essential login credentials is not missing in the textfile
        # Check if host,user and password is in cred
        if ('host' in cred.keys()) and     \
        ('user' in cred.keys()) and        \
        ('password' in cred.keys()):
            return cred
        # If not display a warning 
        else:
            raise Warning("Credential infomation missing")
            return None