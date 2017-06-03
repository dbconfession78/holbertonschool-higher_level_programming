#!/usr/bin/python3
"""
Module: 0-read-file.py
"""


def read_file(filename=""):
    if filename is None:
        return None

    with open(filename, encoding="utf-8", mode="r") as a_file:
        text = a_file.read()

    print("{}".format(text), end="")
