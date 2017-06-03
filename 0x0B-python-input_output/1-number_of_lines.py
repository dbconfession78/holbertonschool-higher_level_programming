#!/usr/bin/python3
"""
Module: number_of_lines
"""


def number_of_lines(filename=""):
    """
    counts the number of lines in a file
    """
    count = 0

    with open(filename, "r") as _file:
        for line in _file:
            count += 1
    return count
