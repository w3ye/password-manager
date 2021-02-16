#! python3
# query.py - Generate sql queries
class GenereateQuery:

    def __init__(self, tableName):
        self.tableName = tableName

    def new_account(self, accountId: int, username: str, password: str,app_name: str,note: str) -> str:
        """
        Generate a queries to insert an array of account information to mysql
        """
        # Check if note is empty
        if len(note.replace(' ','')) != 0:
            query = "INSERT INTO %s (account_id, username, psword, app_name, note) VALUES ('%s', '%s', '%s', '%s', '%s')" % (self.tableName, accountId, username, password, app_name, note)
        else: 
            query = "INSERT INTO %s (account_id, username, psword, app_name) VALUES ('%s', '%s', '%s', '%s')" % (self.tableName, accountId, username, password, app_name)
        return query

    def find_account(self, appName: str) -> str:
        """
        Generate a queries to find all information to an account
        """
        query = f"SELECT * FROM {self.tableName} WHERE app_name like '%{appName}%'"
        return query
    
    def delete_account(self, accountId: int) -> str:
        """
        Generate a query to delete an account by accountId(primary key)
        """
        query = "DELETE FROM %s WHERE account_id = %s" % (self.tableName, accountId)
        return query
    
    def change_password(self, accountId: int, newPassword: str) -> str:
        """
        Generate an query to update account password using accountId(primary key)
        """
        query = "UPDATE %s SET psword = '%s' WHERE account_id = '%s'" % (self.tableName, newPassword, accountId)
        return query