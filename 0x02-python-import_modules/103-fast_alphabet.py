#!/usr/bin/python3
def print_alphabet(letter):
    print(letter, end='')
    if letter < 'Z':
        print_alphabet(chr(ord(letter) + 1))

if __name__ == "__main__":
    print_alphabet('A')
    print()

