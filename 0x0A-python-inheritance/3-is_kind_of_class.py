#!/usr/bin/python3

"""
Module:  3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """
    determines if an object is an instance of a specified class
    or is a class instance that inherited from the specified class
    """

    if (issubclass(type(obj), a_class)):
        return True
    else:
        return False
