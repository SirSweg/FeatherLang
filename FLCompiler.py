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
        readFunc(pyFile, flFile, "")

# Reads chars from flFile until a divide char is found, then sends the
# full function found before the divide into matchFunc
def readFunc(pyFile, flFile, tmpStr):
    x = flFile.read(1)

    match x:
        case " ":
            matchFunc(pyFile, flFile, tmpStr)
        case "(":
            matchFunc(pyFile, flFile, tmpStr)
        case "":
            return
        case _:
            readFunc(pyFile, flFile, tmpStr + x)

# Matches tmpStr to its corresponding function. If there is no corresponding
# function, readFunc is called with tmpStr reset to ""
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

# Writes the math operation corresponding to tmpStr to the pyFile. Calls
# nextWord to find the two variables for the operation.
def mathOps(pyFile, flFile, tmpStr):
    var1 = nextWord(flFile, "")
    var2 = nextWord(flFile, "")

    pyFile.write(var1 + " " + tmpStr + " " + var2)


# Reads chars from the flFile until a divide is found, then returns the full
# word found before the divide.
def nextWord(flFile, word):
    x = flFile.read(1)

    match x:
        case " ":
            return word
        case "\n":
            return word
        case "(":
            return word
        case _:
            return nextWord(flFile, word + x)

if __name__ == "__main__":
    main()
