#! python3
# ReadFile.py - Get mySql Credential from a text file

from typing import List, Dict
import re
class Credentials:

    def read_file(self) -> List:
        """
        Read mysql credential from a textfile in current working directory
        """
        data = None
        try:
            with open('sqlCred.txt') as file:
                data = file.readlines()
            file.close
        except FileNotFoundError as err:
            print("OS error: {0}".format(err))
        return data

    def get_cred(self) -> Dict:
        """
        Process the infomation from 'read_file' to generate a dictionary of mysql credentials for easy access.
        """
        data = self.read_file()
        cred = {}
        # Setting key and value for Dict
        for i in data:
            noSpace = re.compile(r'\s*').sub('',i)  # Removing space in 'i'
            temp = noSpace.split('=')   # Split 'noSpace' by delimiter('=')
            
            # Setting synonyms  nouns to a specific one using regex
            if re.compile(r'host | host. | endpoint', re.VERBOSE | re.IGNORECASE).search(temp[0]) != None:
                temp[0] = 'host'
            if re.compile(r'user.', re.IGNORECASE).search(temp[0]) != None:
                temp[0] = 'user'
            if re.compile(r'password | pass', re.VERBOSE | re.IGNORECASE).search(temp[0]) != None:
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