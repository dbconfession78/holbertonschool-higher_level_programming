#!/usr/bin/python3

# safe_print_integer - prints value only if it is an integer
# value: value to print
# Return: True if integer was printed. False otherwise


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except:
        return False
    return True
