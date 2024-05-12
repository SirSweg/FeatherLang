from collections import deque
import sys

# To-Do
# 1. Take input file and create a .py file that shares the same name
# 2. Convert the input file FeatherLang code into a bytecode like string
#    that will be put into the compiler
# 3. Read bytecode string and print corresponding python code to the .py file
# ΘΣΨ

# this is the input file with the FeatherLang code
flFile = open(sys.argv[1])

# gets the name of the file w/o .txt and makes a corresponding .py
nameLength = len(flFile.name)
pyFile = open(flFile.name[:nameLength-4] + ".py", "w")

# How to turn code into compiler-ready string
# - ignore () turn them into spaces?
# - turn spaces into \s
# - if you find \( or \), replace with just ( or )
# - \e at end of file if necessary
# - ; ignore everything until end of line

# Making compiler-ready queue:
# 1. add chars from flFileStr to tmpCompilerStr until you meet a space or an 
#    equivalent
# 2. add tmpCompilerStr to compilerQueue, then set tmpCompilerStr to ""
compilerQueue = deque([])
flFileStr = flFile.read()
tmpCompilerStr = ""

for x in flFileStr:
    match x:
        # Spaces and their equivalents
        case ' ':
            compilerQueue.append(tmpCompilerStr)
            tmpCompilerStr = ""
        case '\t':
            compilerQueue.append(tmpCompilerStr)
            tmpCompilerStr = ""
        case '(':
            compilerQueue.append(tmpCompilerStr)
            tmpCompilerStr = ""
        case ')':
            compilerQueue.append(tmpCompilerStr)
            tmpCompilerStr = ""
        # Comments
        case ';':
            compilerQueue.append(x)
        # New Lines
        case '\n':
            compilerQueue.append(tmpCompilerStr)
            tmpCompilerStr = ""
            compilerQueue.append(x)
        # Adding regular chars
        case _:
            tmpCompilerStr += x

print(compilerQueue)
