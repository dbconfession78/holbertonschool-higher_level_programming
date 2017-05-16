#!/usr/bin/python3
"""
Module 4-print_square
prints a square made of '#' that is
'size" long and 'size' wide.
"""


def print_square(size):
    """
    print_square: prints a square of '#' that is 'size' long and 'size' wide.
    Raises a TypeError if 'size' is not an integer
    Raises a TypeError if 'size' is a float and is less than 0.0
    Raises a ValueError if 'size' is less than 0
    """

    if not isinstance(size, int) or (isinstance(size, float) and size < 0.0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
