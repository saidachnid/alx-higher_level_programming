#!/usr/bin/python3
for letter in range(97, 123):  # ASCII values for lowercase letters 'a' to 'z'
    if letter != 101 and letter != 113:  # ASCII values for 'e' and 'q'
        print("{:c}".format(letter), end='')

# Print a newline to separate the output from the shell prompt
print()
