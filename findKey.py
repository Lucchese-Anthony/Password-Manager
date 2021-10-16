import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def createKey(password, isNewProgram, program):
    resultTuple = (None, None)
    password_provided = password.encode()
    currentWorkingDir = os.getcwd()
    input_file = ('{}/{}/key.encrypted'.format(currentWorkingDir, program)).lower()
    if isNewProgram:
        salt = os.urandom(16)
    elif os.path.isfile(input_file):
        currentWorkingDir = os.getcwd()
        with open(input_file, "rb") as f:
            salt = f.readline(16)
        f.close()
        kdf = PBKDF2HMAC(
            algorithm = hashes.SHA256(),
            length=32,
            salt = salt,
            iterations=100000,
            backend=default_backend()

        )
        returnTuple[0] = base64.urlsafe_b64encode(kdf.derive(password_provided)) # key
        returnTuple[1] = salt
        
    else:
        return resultTuple

    
    return resultTuple

