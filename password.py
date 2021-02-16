#! python3 
# password.py - Creates a password
import string
import secrets, pyperclip
import random, pyinputplus as pyip

def generate_password(mode=1) -> str:
    """
    Generate password\n
    mode 1: Generate alphanumeric + symbol password\n
    mode 2: Generate only an alphanumeric password\n
    Default mode set to 1
    """
    alphabet_symbols = string.ascii_letters + string.digits + string.punctuation
    alpha_numeric = string.ascii_letters + string.digits
    # generate a random password length 8 - 16
    length = random.randint(8,16)
    # if the mode is set to 1 (default) it genereates an alphanumeric and symbol password
    if mode == 1:
        while True:
            password = ''.join(secrets.choice(alphabet_symbols) for i in range(length))
            # Ensures that there is atleast one lowercase, one uppercase and one digit in the password
            if (any(c.islower() for c in password) and any(c.isupper() for c in password) and sum(c.isdigit() for c in password)):
                break
    # gereates a alphanumeric password
    else: 
        password = ''.join(secrets.choice(alpha_numeric) for i in range(length))
    return password

def confirm_password() -> str:
    """
    User enters password and confirms that p1 == p2
    """
    while True:
        p1 = pyip.inputPassword("Enter your password:\n")
        p2 = pyip.inputPassword("Confirm password:\n")
        if p1 == p2:
            return p1
        print("Password does not match please try again")

def password_choice():
    passOpt = ["Generate a password", "Enter your own password"]
    passOption = pyip.inputMenu(passOpt, numbered=True)
    # If the user wants to genereate a password
    if passOption == passOpt[0]:
        passOpt = ["Genereate a password containing at lease 1 Upper Case, 1 number and 1 symbol", "Genereate a alphanumeric password"]
        passOption = pyip.inputMenu(passOpt, numbered=True)
        # If the user choses for a password with symbols
        if passOption == passOpt[0]:
            psw = str(generate_password())
        else: 
            psw = str(generate_password(2))
        pyperclip.copy(psw)
    elif passOption == passOpt[1]:
        psw = confirm_password()
    print("Password %s copied to clipboard" % psw)
    return psw