#! python3
# query.py - Generate sql queries
class GenereateQuery:
    
    def new_account(self, accountId: int, username: str, password: str,url: str,note: str) -> str:
        """
        Generate a queries to insert an array of account information to mysql
        """
        # Check if note is empty
        k = note.replace(' ','')
        if len(k) != 0:
            query = "INSERT INTO accounts.acc (account_id, username, psword, url, note) VALUES (%s, '%s', '%s', '%s', '%s')" % (accountId, username, password, url, note)
        else: 
            query = "INSERT INTO accounts.acc (account_id, username, psword, url) VALUES (%s, '%s', '%s', '%s')" % (accountId, username, password, url)
        return query

    def find_account(self, choice: str) -> str:
        """
        Generate a queries to find all information to an account
        """
        query = "SELECT * FROM accounts.acc WHERE %s " % choice 
        return query
    
    def delete_account(self, accountId: int) -> str:
        """
        Generate a query to delete an account by accountId(primary key)
        """
        query = "DELETE FROM accounts.acc WHERE account_id = %s" % accountId
        return query
    
    def update_account(self, accountId: int, newPassword: str) -> str:
        """
        Generate an query to update account password using accountId(primary key)
        """
        query = "UPDATE accounts.acc SET password = '%s' WHERE account_id = %s" % (accountId, newPassword)
        return query