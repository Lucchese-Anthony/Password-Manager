from cryptography.fernet import Fernet
import findKey
import os

def encrypt(password, program):
    key = findKey.createKey(password, True, program) # Use one of the methods to get a key (it must be the same when decrypting)
    currentWorkingDirectory = os.getcwd()
    input_file = ('{}/{}/key.txt'.format(currentWorkingDirectory, program)).lower()
    output_file = ('{}/{}/key.encrypted'.format(currentWorkingDirectory, program)).lower()

    with open(input_file, 'rb+') as f:
        data = f.read()  # Read the bytes of the input file
    fernet = Fernet(key[0])
    encrypted = fernet.encrypt(data)
    with open(output_file, 'wb+') as f:
        f.write(key[1])
        f.write(encrypted)  # Write the encrypted bytes to the output file
    f.close()
    os.remove(input_file)   # Note: You can delete input_file here if you want
