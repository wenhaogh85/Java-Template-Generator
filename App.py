import utilities as utils
import JavaClass
import JavaMain

def getUserOption():

    print(
        "\n===========================================" +
        "\nWelcome to Java Template factory" +
        "\n===========================================" +
        "\n\nEnter one of the following options:" +
        "\n+--------+------------------------------+" +
        "\n| Option | Description                  |" +
        "\n+--------+------------------------------+" +
        "\n|    1   | To create a main progam file |" +
        "\n+--------+------------------------------+" +
        "\n|    2   | To create a class file       |" +
        "\n+--------+------------------------------+" +
        "\n|    q   | To quit the program          |" +
        "\n+--------+------------------------------+" +
        "\n==========================================="
    )

    option = input("\nEnter option: ")

    return option

def createJavaMainProgram():
    className = utils.createClassName()
    fileName = utils.createFileName(className, "java")
    mainProgramTemplate = JavaMain.getMainProgramTemplate(className)
    utils.createProgram(fileName, mainProgramTemplate)
    utils.updateLogFile(fileName)

def createJavaClassProgram():

    className = utils.createClassName()
    fileName = utils.createFileName(className, "java")
    classAttributes = JavaClass.createClassAttributes()

    if len(classAttributes) != 0:

        classTemplate = JavaClass.getClassTemplate(className, classAttributes)
        constructorTemplate = JavaClass.getConstructorTemplate(className, classAttributes)
        allSetterAndGetterMethodTemplate = JavaClass.getAllSetterAndGetterMethodTemplate(classAttributes)

        allClassTemplate = JavaClass.getAllClassTemplate(
                                        classTemplate,
                                        constructorTemplate,
                                        allSetterAndGetterMethodTemplate
        )

        utils.createProgram(fileName, allClassTemplate)
        utils.updateLogFile(fileName)

# ---------------------------------------------------------------------
while True:

    option = getUserOption()

    if option == "q":
        print("Thank you for using Java Template Factory")
        break

    elif option == "1":
        createJavaMainProgram()

    elif option == "2":
        createJavaClassProgram()

    else:
        print("Please enter a valid option!\n")