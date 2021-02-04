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
        noSpaceReg = re.compile(r'\s*')     # Remove all spaces
        hostReg = re.compile(r'host | host. | endpoint')
        for i in data:
            noSpace = noSpaceReg.sub('',i.lower())
            temp = noSpace.split('=')
            if temp[0] == 'host' or temp[0] == 'endpoint' or temp[0] == 'hostname':
                temp[0] = 'host'
            if temp[0] == 'username' or temp[0] == 'user':
                temp[0] = 'user'
            if temp[0] == 'password' or temp[0] == 'pass':
                temp[0] = 'password'
            cred[temp[0]] = temp[1]         # Store the data read from the textfile into dictionary 'cred'

        # Makes sure that essential login credentials is not missing in the textfile
        # Check if host,user and password is in cred
        if ('host' in cred.keys()) and     \
        ('user' in cred.keys()) and        \
        ('password' in cred.keys()):
            print(cred)
            return cred
        # If not display a warning 
        else:
            raise Warning("Credential infomation missing")
            return None
    
Credentials().get_cred()