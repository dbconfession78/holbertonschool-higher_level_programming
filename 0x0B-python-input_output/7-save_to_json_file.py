#!/usr/bin/python3
"""
Module: 7-save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    with open(filename, mode="w", encoding="utf-8") as _file:
        _file.write(json.dumps(my_obj))
    _file.closed
