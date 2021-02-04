from typing import List
import mysql.connector
from readFile import Credentials as rc

class DatabaseManager:
    mydb = None
    cursor = None
    
    def __init__(self):
        self.connect(rc().get_cred())


    def connect(self, cred):
        host = cred['host']
        user = cred['user']
        password = cred['password']
        self.mydb = mysql.connector.connect(
            host=host, 
            user=user, 
            password=password
        )
        # Checking if the database is connected
        if self.mydb.is_connected():
            print("Connected")
        else: print("Failed to connect")
    
    # Executes query - mode 1: insert/delete/update  | mode 2: select
    def execute_query(self, query: str, mode: int) -> List:
        self.cursor = self.mydb.cursor()
        self.cursor.execute(query)
        # If user wants to insert/ delete into database:
        if mode == 1:
            self.mydb.commit()
        # If user wants to view data 
        elif mode == 2:
            result = self.cursor.fetchall()
            return result
        return None


class GenereateQuery:
    
    def new_account(self, accountId: int, username: str, password: str,url: str,note: str) -> str:
        # Check if note is empty
        k = note.replace(' ','')
        if len(k) != 0:
            query = "INSERT INTO accounts.acc (account_id, username, psword, url, note) VALUES (%s, '%s', '%s', '%s', '%s')" % (accountId, username, password, url, note)
        else: 
            query = "INSERT INTO accounts.acc (account_id, username, psword, url) VALUES (%s, '%s', '%s', '%s')" % (accountId, username, password, url)
        return query

    def find_account(self, choice: str) -> str:
        query = "SELECT * FROM accounts.acc WHERE %s " % choice 
        return query
    
    def delete_account(self, accountId: int) -> str:
        query = "DELETE FROM accounts.acc WHERE account_id = %s" % accountId
        return query
    
    def update_account(self, accountId: int, newPassword: str) -> str:
        query = "UPDATE accounts.acc SET password = '%s' WHERE account_id = %s" % (accountId, newPassword)
        return query

DatabaseManager()   