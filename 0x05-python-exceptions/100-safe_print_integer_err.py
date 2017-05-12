#!/usr/bin/python3
import sys

# safe_print_integer_err - prints an integer
# value: value to print
# Return: True if value correctly printed. False otherwise


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False
