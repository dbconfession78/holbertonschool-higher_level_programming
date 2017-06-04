#!/usr/bin/python3
"""
Module: 9-add_item
adds all arguments to a Python list, and then saves them to a file
"""


import sys
import os

load_from_json_file = __import__("8-load_from_json_file").load_from_json_file
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
_list = []

# if os.path.exists("add_item.json"):
try:
    _list = load_from_json_file("add_item.json")
except:
    pass

for i in range(1, len(sys.argv)):
    _list.append(sys.argv[i])

save_to_json_file(_list, "add_item.json")
