from random import randint
from databaseManager import DatabaseManager as dm

class GenerateId:
    
    def __init__(self):
        print(self.generate_account_id())

    # Generates a random length 10 number
    def generate_account_id(self) -> int:
        length = 10
        accountId = ""
        for i in range(length):
            accountId += str(randint(0,9))
        self.check_account_id(self.check_account_id())
        return int(accountId)

    # Checks in mysql if there's a same number
    def check_account_id(self, accountId: int) -> None:
        if dm().execute_query("SELECT * FROM accounts.acc WHERE account_id = %s" % accountId, 2) != []:
            self.generate_account_id()
