from datetime import datetime

def getCurrentDate():
    return datetime.today().strftime("%d-%m-%Y")

def getCurrentTime():
    return datetime.today().strftime("%H:%M:%S")

def updateLogFile(fileName):

    fileMode = "a"

    file = open("log.txt", fileMode)

    logMessage = "{} was created at date: {} time: {}\n".format(
                                                fileName, 
                                                getCurrentDate(), 
                                                getCurrentTime()
                                                )

    file.write(logMessage)
    file.close()

def tab(factor = 1):
    return "    " * factor

def createClassName():

    while True:

        # gets Java class name
        className = input("Enter Java class name: ")

        # checks if class name is valid
        if isTokensValid(className) == True:

            # returns the Java class name in camel case
            return toCamelCase(className)

        else:
            print("{} is not a valid class name!\n".format(className))

def toCamelCase(className):
    return className[0].upper() + className[1:]

def createFileName(fileName, fileExtension):
    return fileName + "." + fileExtension

def isTokensValid(tokens):

    if isDigit(tokens[0]): return False

    for token in tokens:
        if isAlphabet(token) == False and isDigit(token) == False:
            return False
    return True

def isAlphabet(token):

    ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for alphabet in ALPHABETS:
        if token.upper() == alphabet:
            return True
    return False

def isDigit(token):

    DIGITS = "0123456789"

    for digit in DIGITS:
        if token == digit:
            return True
    return False

def createProgram(fileName, template):

    fileMode = "w"

    file = open(fileName, fileMode)

    for line in template:
        file.write(line + "\n")

    file.close()

    print("\n{} has been successfully created...".format(fileName))