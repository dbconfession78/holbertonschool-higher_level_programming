#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    args = sys.argv

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if args[2] != "+" and args[2] != "-" and args[2] != "*" and args[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(args[1])
    b = int(args[3])

    if args[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif args[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif args[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif args[2] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
