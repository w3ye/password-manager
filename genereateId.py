#! python3
# generateId.py - Generate a uniqe random integer to use as a primary key of a database
from random import randint
from databaseManager import DatabaseManager as dm
from crypt import Crypt

class GenerateId:


    def __init__(self, tableName:str):
        self.tableName = tableName
    
    def generate_account_id(self) -> int:
        """
        Generate a 10 digit random number
        """
        length = 10
        accountId = ""
        for i in range(length):
            accountId += str(randint(0,9))
        self.check_account_id(int(accountId))
        return int(accountId)

    def check_account_id(self, accountId: int) -> None:
        """
        Validate in mysql if accountId exist
        """
        # ? Move the query statement to query.py
        if dm().execute_query("SELECT * FROM %s WHERE account_id = '%s'" % (self.tableName, str(accountId)), 2) != []:
            self.generate_account_id()