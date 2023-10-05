#!/usr/bin/python3
import sys
arg = sys.argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(arg) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if arg[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(arg[1])
    b = int(arg[3])
    if arg[2] == '+':
        print("{0} + {1} = {2}".format(a, b, add(a, b)))
    elif arg[2] == '-':
        print("{0} - {1} = {2}".format(a, b, sub(a, b)))
    elif arg[2] == '*':
        print("{0} * {1} = {2}".format(a, b, mul(a, b)))
    elif arg[2] == '/':
        print("{0} / {1} = {2}".format(a, b, div(a, b)))
