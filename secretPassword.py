import string
import secrets
import random

def generate_password(mode=1) -> str:
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