import sys

# To-Do
# 1. Take input file and create a .py file that shares the same name
# 2. Convert the input file FeatherLang code into a bytecode like string
#    that will be put into the compiler
# 3. Read bytecode string and print corresponding python code to the .py file
# ΘΣΨ

def main():
    # this is the input file with the FeatherLang code
    flFile = open(sys.argv[1])

    # gets the name of the file w/o .txt and makes a corresponding .py
    nameLength = len(flFile.name)
    pyFileName = flFile.name[:nameLength-4] + ".py"
    with open(pyFileName, "w") as pyFile:
        pyFile.write("# FeatherLang\n")

    # How recursive compiler works:
    # readChar reads a single char from the flFile.
    # If char is a space or equivalent, calls matchFunc function, which
    #     matches the current value of tmpStr to the corresponding function.
    # Else, char is a standard letter, is added to tmpStr, and readChar again.

    # begins the recursive char reading (acts as the compiler)
    with open(pyFileName, "a") as pyFile:
        readChar(pyFile, flFile, "")

def readChar(pyFile, flFile, tmpStr):
    x = flFile.read(1)

    match x:
        case " ":
            matchFunc(pyFile, flFile, tmpStr)
        case "(":
            matchFunc(pyFile, flFile, tmpStr)
        case "":
            return
        case _:
            readChar(pyFile, flFile, tmpStr + x)

def matchFunc(pyFile, flFile, tmpStr):
    match tmpStr:
        case "+":
            mathOps(pyFile, flFile, tmpStr)
        case "-":
            mathOps(pyFile, flFile, tmpStr)
        case "/":
            mathOps(pyFile, flFile, tmpStr)
        case "*":
            mathOps(pyFile, flFile, tmpStr)
        case "%":
            mathOps(pyFile, flFile, tmpStr)

def mathOps(pyFile, flFile, tmpStr):
    pyFile.write("1 " + tmpStr + " 2")

if __name__ == "__main__":
    main()
