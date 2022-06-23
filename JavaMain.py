import utilities as utils

def getMainProgramTemplate(className):

    return [
        "public class " + className + " {",
        "    public static void main(String[] args) {",
        "\n" + utils.tab(2) + "// insert code here...",
        utils.tab(2) + "System.out.println(\"Hello World\");",
        utils.tab() + "}",
        "}"
    ]
