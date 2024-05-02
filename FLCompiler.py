from collections import deque
import sys

# selects the input file and makes a String containing each character
file = open(sys.argv[1])
fileStr = file.read()
file.close()

# adds each char in fileStr to compilerChars and handles special characters
compilerChars = deque([])
for x in fileStr:
    match x:
        case ' ':
            compilerChars.append('#')
        case '\t':
            compilerChars.append('#')
        case '\n':
            compilerChars.append('@')
        case '(':
            continue
        case ')':
            continue
        case _:
            compilerChars.append(x)
        
# interprets each char in compilerChars meaning in FeatherLang and converts
# it into Python Code
print(compilerChars)
