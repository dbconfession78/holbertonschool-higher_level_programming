#!/usr/bin/python3
"""
Module:  2-is_same_class
class MyList inherits from list
"""


def is_same_class(obj, a_class):
    """
    determines if 'obj' is exactly an instance of 'a_class'
    """
    return issubclass(a_class, type(obj))
