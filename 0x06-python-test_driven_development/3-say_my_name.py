#!/usr/bin/python3
"""
Module: 3-say_my_name
prints "My name is" followed by a first and last name
"""

def say_my_name(first_name, last_name=""):
    """
    say_my_name: prints "My name is " followed by a first and last name.
    Raises a TypeError if either first or last name are not stringd.
    Raises a TypeError ii there isn't at lesst one string provided
    """

    if not isinstance(first_name, str) or first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str) or last_name is None:
        raise TypeError("last_name must be a string")


    print("My name is {:} {:}".format(first_name, last_name))
