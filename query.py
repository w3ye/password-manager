#! python3
# query.py - Generate sql queries
class GenereateQuery:
    
    def __init__(self, tableName):
        self.tableName = tableName

    # TODO: Read the user config file to get the table name OR receive the table name from menu
    def new_account(self, accountId: int, username: str, password: str,url: str,note: str) -> str:
        """
        Generate a queries to insert an array of account information to mysql
        """
        # Check if note is empty
        k = note.replace(' ','')
        if len(k) != 0:
            query = "INSERT INTO %s (account_id, username, psword, url, note) VALUES (%s, '%s', '%s', '%s', '%s')" % (self.tableName, accountId, username, password, url, note)
        else: 
            query = "INSERT INTO %s (account_id, username, psword, url) VALUES (%s, '%s', '%s', '%s')" % (self.tableName, accountId, username, password, url)
        return query

    def find_account(self, choice: str) -> str:
        """
        Generate a queries to find all information to an account
        """
        query = "SELECT * FROM %s WHERE %s " % (self.tableName, choice)
        return query
    
    def delete_account(self, accountId: int) -> str:
        """
        Generate a query to delete an account by accountId(primary key)
        """
        query = "DELETE FROM %s WHERE account_id = %s" % (self.tableName, countId)
        return query
    
    def update_account(self, accountId: int, newPassword: str) -> str:
        """
        Generate an query to update account password using accountId(primary key)
        """
        query = "UPDATE %s SET password = '%s' WHERE account_id = %s" % (self.tableName, accountId, newPassword)
        return query