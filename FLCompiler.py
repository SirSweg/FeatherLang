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
