# password-manager
---
## Description
This is a python script that manages password using mysql

### Features
- Mysql connection
- Encrypts username, password when inserting into mysql database
- Decrypts information when retrieving from database
- Reads mysql credentials from textfile
- Generate an alpha numeric password or a password containting at lease 1 upper case letter, 1 lower case letter and 1 symbol
- Generate a unique random number as primary key for the database
- Creates a local config file that stores a username and password for local access
- Every time the user  does an account lookup, this script will copy the account password to the clipboard

--- 

## Usage
```
py main.py
```
