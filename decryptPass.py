from cryptography.fernet import Fernet, InvalidToken
import findKey
import os

def decrypt(password, program):
    outputPassword = ""
    key = findKey.createKey(password, False, program) # Use one of the methods to get a key (it must be the same as used in encrypting)
    if key != (None, None):
        currentWorkingDirectory = os.getcwd()
        input_file = ('{}/{}/key.encrypted'.format(currentWorkingDirectory, program)).lower()
        output_file = ('{}/{}/key.txt'.format(currentWorkingDirectory, program)).lower()
        with open(input_file, 'rb') as f:
            salt = f.readline(16)  # Read the bytes of the encrypted file
            restOfFile = f.read()
        try:   
            fernet = Fernet(key[0])
            outputPassword = "Password: {}".format(fernet.decrypt(restOfFile).decode())
        except InvalidToken as e:
            print("Invalid Master Password!")
    else:
        outputPassword = "There is no found password for {}".format(program)
    return outputPassword
