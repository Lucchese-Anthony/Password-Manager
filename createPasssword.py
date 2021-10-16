import random
import os

import encryptPass
import decryptPass
import findKey


def main():
    createOrFind = int(input("finding or creating new password? (1/2): "))
    
    if createOrFind == 1:
        overallPassword = str(input("type password: "))
        program = str(input("for what program?: "))
        decryptedPassword = decryptPass.decrypt(overallPassword, program)
        print(decryptedPassword)
    else:
        createNewPassword()

def createNewPassword():
    numOfChars = findNumChar()
    possibleChars = findInput()
    password = makePassword(numOfChars, possibleChars)
    print("This is your new password:\n{0}".format(password))
    newPassword = True
    while(newPassword):
        yesOrNo = str(input("want another password (y/n): "))
        if yesOrNo == 'y':
            numOfChars = findNumChar()
            possibleChars = findInput()
            password = makePassword(numOfChars, possibleChars)
            print("This is your new password:\n{0}".format(password))
        else:
            newPassword = False
            currentWorkingDirectory = os.getcwd()
            applicationName = str(input("what are you using this application for?: ")).lower()
            overallPassword = str(input("what is your master password?: "))
            fileName = "{}/{}/key.txt".format(currentWorkingDirectory, applicationName)
            try:
                os.mkdir(applicationName.lower())
                with open(fileName, "wb+") as f:
                    insertString = bytes(password, encoding='utf8')
                    f.write(insertString)
                f.close()
                encryptPass.encrypt(overallPassword, applicationName)
            except FileExistsError:
                print("A password already exists for the program, delete the folder!")
                break

def findNumChar():
    numOfChars = int(input("how long do you want the password: "))
    return numOfChars

def makePassword(numOfChars, possibleChars):
    password = ""
    iterator = numOfChars
    while(iterator != 0):
        password += random.choice(possibleChars)
        iterator -= 1
    return password

def findInput():
    charList = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    temp = str(input("do you want numbers y/n: "))
    if temp == 'y':
        charList += "0123456789"
    temp = str(input("do you want special characters(y/n): "))
    if temp == 'y':
        charList += "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    return charList

if __name__ == "__main__":
    main()
