#!/usr/bin/python3
"""
Module: 3-say_my_name
prints "My name is" followed by a first and last name
"""
import sys


def say_my_name(first_name, last_name=""):
    """
    say_my_name: prints "My name is " followed by a first and last name.
    Raises a TypeError If either first or last name are not stringd.
    Raises a TypeError ig there isn't at lesst one string provided
    """

    if not isinstance(first_name, str) or first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str) or last_name is None:
        raise TypeError("last_name must be a string")

    if last_name == "":
        print("My name is {:s}".format(first_name))
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
