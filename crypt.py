from cryptography.fernet import Fernet
import os
from pathlib import Path
class Crypt:

    def __init__(self):
        self.keys()

    def keys(self) -> None:
        """
        Read a key file, if the key file does not exist create one
        """
        path = Path('./config/key')
        global key
        # If the file path does not exist, create one 
        if not path.exists():
            os.makedirs(path)
        while True:
            # read key.key file
            try:
                file = open(path / 'key.key', 'rb')
                key = file.read()
                file.close
            # when key.key file does not exist. Create one
            except FileNotFoundError:
                key = Fernet.generate_key()
                file = open(path / 'key.key', 'wb')
                file.write(key)
                file.close()
                continue
            break
        
    
    def encrypt(self, msg) -> str:
        # msg must be converted to bytes to use the encrypt function
        byteMsg = msg.encode()
        f = Fernet(key)
        # encrypted is converted from bytes to string
        encrypted = f.encrypt(byteMsg).decode()
        return encrypted


    def decrypt(self, msg) -> str:
        # msg must be converted from string to bytes for decryption
        encrypted = msg.encode()
        f = Fernet(key)
        # decrypted is converted from bytes to string
        decrypted = f.decrypt(encrypted).decode()
        return decrypted