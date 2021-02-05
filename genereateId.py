#! python3
# generateId.py - Generate a uniqe random integer to use as a primary key of a database
from random import randint
from databaseManager import DatabaseManager as dm

class GenerateId:
    
    def __init__(self):
        print(self.generate_account_id())

    def generate_account_id(self) -> int:
        """
        Generate a 10 digit random number
        """
        length = 10
        accountId = ""
        for i in range(length):
            accountId += str(randint(0,9))
        self.check_account_id(self.check_account_id())
        return int(accountId)

    def check_account_id(self, accountId: int) -> None:
        """
        Validate in mysql if accountId exist
        """
        # ? Move the query statement to query.py
        if dm().execute_query("SELECT * FROM accounts.acc WHERE account_id = %s" % accountId, 2) != []:
            self.generate_account_id()
