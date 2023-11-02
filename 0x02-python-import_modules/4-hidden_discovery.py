#!/usr/bin/python3
import py_compile

# Compile the .pyc file to a code object
pyc_path = 'hidden_4.pyc'
code = py_compile.compile(pyc_path)

# Extract and print the names from the code object
names = [name for name in code.co_names if not name.startswith('__')]
names.sort()

for name in names:
    print(name)

