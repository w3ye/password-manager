#! python3 
# databaseManger.py - Connects to mysql database and execute queries
from typing import List, Dict
import mysql.connector
from readFile import Credentials as rc

class DatabaseManager:
    mydb = None
    cursor = None
    
    def __init__(self):
        self.connect(rc().get_cred())


    def connect(self, cred: Dict):
        """
        Establis a mysql database connections
        """
        try:
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
        # Catching sql.connector Errors
        except mysql.connector.errors.InterfaceError as e:
            print(e, '\nPlease make sure the host name is correct: ', cred['host'])
        except mysql.connector.errors.ProgrammingError as e:
            print(e, '\nPlease make sure the username and password is correct') 

    # TODO: Check if a database exists. If not create one.
    # TODO: Create multiple databases for different users.
    # TODO: Save database names in binary files (shelf)        
    
    # Executes query - mode 1: insert/delete/update  | mode 2: select
    def execute_query(self, query: str, mode=1) -> List:
        """
        Execute mysql query.\n
        mode 1: INSERT/DELETE/UPDATE (commit queries)\n
        mode 2: SELECT (view queries)
        """
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
