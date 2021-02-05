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
        host = cred['host']
        user = cred['user']
        password = cred['password']
        # Check if database is specified from the credential textfile
        if 'database' in cred.keys():
            database = cred['database']
        else: 
            database = 'accounts'

        try:
            self.mydb = mysql.connector.connect(
                host=host, 
                user=user, 
                password=password,
                database=database
            )
            # Checking if the database is connected
            if self.mydb.is_connected():
                print("Connected")
                
        # Catching sql.connector Errors
        except mysql.connector.errors.InterfaceError as e:
            print(e, '\nPlease make sure the host name is correct: ', cred['host'])
        except mysql.connector.errors.ProgrammingError as e:
            print(e, '\nPlease make sure the username, password, database in the credentials text file is correct\nText file default name: \'sqlCred.txt\'')        
    
    # Executes query - mode 1: insert/delete/update  | mode 2: select
    def execute_query(self, query: str, mode=1) -> List:
        """
        Execute mysql query.\n
        mode 1: INSERT/DELETE/UPDATE (commit queries)\n
        mode 2: SELECT (view queries)
        mode 0: CREATE TABLE
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

# DatabaseManager()