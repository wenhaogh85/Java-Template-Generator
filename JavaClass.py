import utilities as utils

def createClassAttributes():

    attributes = []

    while True:

        #gets attribute from user
        print(
            "\nSelect one of the following attribute type:\n" +
            "\n===============================================" +
            "\n1. byte     5. float       9. String" +
            "\n2. short    6. double     10. User-defined" +
            "\n3. int      7. char" +
            "\n4. long     8. boolean" +
            "\n===============================================" +
            "\n\nEnter q to stop entering attributes\n"
        )

        option = input("Enter option (1-10): ")

        attributeType = parseAttributeOption(option)

        if option == "q":
            return attributes

        elif attributeType != None:

            attribute = None

            if attributeType == "user-defined":

                userDefinedAttributeType = input("\nEnter user-defined attribute: ")
                attributeName = getAttributeName()

                attribute = createAttribute(attributeName, userDefinedAttributeType)

            else:
                print("\nSelected attribute type:", attributeType)
                attributeName = getAttributeName()

                attribute = createAttribute(attributeName, attributeType)

            attributes.append(attribute)

        else:
            print("Please enter a valid option!")

def getAttributeName():

    while True:

        attributeName = input("Enter attribute name: ")

        if utils.isTokensValid(attributeName) == True:
            return attributeName
        else:
            print("{} is not a valid attribute name!\n".format(attributeName))

def parseAttributeOption(option):

    TYPES = [
        "byte", "short", "int", "long", "float", "double",
        "char", "boolean", "String", "user-defined"
    ]

    if utils.isDigit(option) == True or option == "10":

        for index in range(len(TYPES)):

            if (int(option) - 1) == index:
                return TYPES[index]
    return None

# ---------------------------------------------------------------------
def createAttribute(attributeName, attributeType):
    return {
        "name" : attributeName,
        "type" : attributeType
    }

# ---------------------------------------------------------------------
def createInstanceVariable(attribute):
    return utils.tab() + "private {} {};\n".format(attribute["type"], attribute["name"])

def createInstanceVariables(attributes):

    instanceVariables = ""
    for attribute in attributes:

        instanceVariables += createInstanceVariable(attribute)

    return instanceVariables

# ---------------------------------------------------------------------
def createArgument(attribute):
    return "{} {}".format(attribute["type"], attribute["name"])

def createArguments(attributes):

    arguments = ""
    for index in range(len(attributes)):

        arguments += createArgument(attributes[index])

        if index != len(attributes) - 1:
            arguments += ", "

    return arguments

# ---------------------------------------------------------------------
def getSetterMethodTemplate(attribute):

    return [
        "\n" + utils.tab() + "// setter method for " + attribute["name"],
        utils.tab() + "public void set" + utils.toCamelCase(attribute["name"]) + "(" + createArgument(attribute) + ") {",
        createSetterStatement(attribute),
        utils.tab() + "}"
    ]

def getGetterMethodTemplate(attribute):

    return [
        "\n" + utils.tab() + "// getter method for " + attribute["name"],
        utils.tab() + "public " + attribute["type"] + " get" + utils.toCamelCase(attribute["name"]) + "() {",
        utils.tab(2) + createGetterStatement(attribute),
        utils.tab() + "}"
    ]

def createGetterStatement(attribute):
    return "return {};".format(attribute["name"])

def getSetterAndGetterMethodTemplate(attribute):

    setterMethodTemplate = getSetterMethodTemplate(attribute)
    getterMethodTemplate = getGetterMethodTemplate(attribute)

    return joinTemplate(
        setterMethodTemplate,
        getterMethodTemplate
    )

def getAllSetterAndGetterMethodTemplate(attributes):

    joinedTemplates = []
    for attribute in attributes:

        setterAndGetterMethod = getSetterAndGetterMethodTemplate(attribute)

        for line in setterAndGetterMethod:
            joinedTemplates.append(line)

    return joinedTemplates

# ---------------------------------------------------------------------
def createSetterStatement(attribute):
    return utils.tab(2) + "this.{0} = {0};".format(attribute["name"])

def createSetterStatements(attributes):

    setters = ""
    for index in range(len(attributes)):
        setters += createSetterStatement(attributes[index])

        if index != len(attributes) - 1:
            setters += "\n"

    return setters

# ---------------------------------------------------------------------
def getClassTemplate(className, attributes):

    instanceVariables = createInstanceVariables(attributes)

    return [
        "public class " + className + " {",
        instanceVariables
    ]

def getConstructorTemplate(className, attributes):

    arguments = createArguments(attributes)
    setterStatements = createSetterStatements(attributes)

    return [
        utils.tab() + "// constructor",
        utils.tab() + "public " + className + " (" + arguments + ") {",
        setterStatements,
        utils.tab() + "}"
    ]

def joinTemplate(*templates):

    joinedTemplates = []
    for template in templates:
        for line in template:
            joinedTemplates.append(line)

    return joinedTemplates

def getAllClassTemplate(classTemplate, constructorTemplate, allSetterAndGetterTemplate):

    joinedTemplates = joinTemplate(
                                    classTemplate,
                                    constructorTemplate,
                                    allSetterAndGetterTemplate
                                    )

    # adds in "}" to close the whole Java class file
    joinedTemplates.append("}")

    return joinedTemplates