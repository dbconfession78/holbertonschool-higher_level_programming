#!/usr/bin/python3
import sys

# safe_print_integer_err - prints an integer
# value: value to print
# Return: True if value correctly printed. False otherwise


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
