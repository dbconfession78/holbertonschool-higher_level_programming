#!/usr/bin/python3
"""
Module: 3-write_file
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file and returns the number of characters written
    """
    with open("my_first_file.txt", mode="w", encoding="utf-8") as _file:
        chars = _file.write(text)

    return chars
