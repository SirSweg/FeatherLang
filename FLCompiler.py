from collections import deque
import sys

# list of all functions for matching purposes in compiler
funcList = ["pr", "+", "-", "/", "*", "if", "ef", "df", "fn"]

# selects the input file and makes a String containing each character
file = open(sys.argv[1])
fileStr = file.read()
file.close()

# adds each char in fileStr to compilerChars and handles special characters
# ΘΣΨ
compilerChars = deque([])
for x in fileStr:
    match x:
        case ' ':
            compilerChars.append('Θ')
        case '\t':
            compilerChars.append('Θ')
        case '\n':
            compilerChars.append('Ψ')
        case '(':
            continue
        case ')':
            continue
        case _:
            compilerChars.append(x)
# ~ denotes end of file
compilerChars.append('Σ')
        
# interprets each char in compilerChars meaning in FeatherLang and converts
# it into Python Code
pyFile = open("fl.py", "w")

def compile(matchStr):
    x = compilerChars.popleft()
    match x:
        case 'Θ':
            compile("")
        case 'Ψ':
            compile("")
        case 'Σ':
            exit()
        case _:
            matchStr += x
            if matchStr in funcList:
                func = globals()[matchStr]
                func()
                compile("")
            else:
                compile(matchStr)

# definitions of built in functions
def pr():
    # removing space between pr and function input
    compilerChars.popleft()
    tmp = ""

    while compilerChars[0] != 'Ψ' and compilerChars[0] != 'Σ':
        if compilerChars[0] == 'Θ':
            compilerChars.popleft()
            tmp += " "
        else:
            tmp += compilerChars.popleft()

    pyFile.write("print(\'" + tmp + "\')")

# finally run the compiler
compile("")
