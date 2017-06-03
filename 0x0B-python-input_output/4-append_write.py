#!/usr/bin/python3
"""
Module: 4-append_write
"""


def append_write(filename="", text=""):
    """
    appends text to a file. creates a new file if it doesn't al;ready exist
    """
    with open(filename, mode="a", encoding="utf-8") as _file:
        chars = _file.write(text)
    _file.closed
    return chars
