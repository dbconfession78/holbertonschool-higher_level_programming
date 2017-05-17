#!/usr/bin/python3
"""
This module provides a function to add two integers
args passed must be of type int or float otherwise TypeError is raised
float args are cast as int
"""


def add_integer(a, b):
    """
    add_integer:
    checks for correct arg type
    returns int cassted sum of args
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
