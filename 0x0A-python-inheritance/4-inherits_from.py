#!/usr/bin/python3

"""
Module:  4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
    determines if an object's type is a subclass (not the class irself)
    of the speciied class (a_class)
    """
    if issubclass(type(obj), a_class):
        if type(obj) is not a_class:
            return True
    else:
        return False
    return False
