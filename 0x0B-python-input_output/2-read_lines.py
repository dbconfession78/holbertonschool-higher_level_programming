#!/usr/bin/python3
"""
Module: 2-read_lines
"""


def read_lines(filename="", nb_lines=0):
    """
    reads n lines of a text file (UTF8) and prints it to stdout
    """
    count = 0

    with open(filename, "r", encoding="utf-8") as _file:
        for line in _file:
            count += 1
        _file.seek(0)
        if nb_lines <= 0 or nb_lines >= count:
            print(_file.read(), end="")
        else:
            count = 0
            while (count < nb_lines):
                print("{}".format(_file.readline()), end="")
                count += 1
    _file.closed
