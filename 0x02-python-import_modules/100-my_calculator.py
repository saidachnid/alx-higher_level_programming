#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = args

    if operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a, b = int(a), int(b)
    result = 0

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        result = div(a, b)

    print(f"{a} {operator} {b} = {result}")

