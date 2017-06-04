#!/usr/bin/python3
"""
Module: 10-load_from_json_file
"""


def class_to_json(obj):
    """
    returns a dictionary description with the simple
    data structure (list, dictionary, string, integer and boolean) for
    JSON serialization of an object
    """

    return(obj.__dict__)
