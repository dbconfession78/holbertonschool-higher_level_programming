#!/usr/bin/python3
"""
Module: 9-add_item
adds all arguments to a Python list, and then save them to a file
"""
import sys
import json


_list = []

with open("add_item.json", mode="r+", encoding="utf-8") as _file:
    
    for i in range(len(sys.argv)):
        if i > 0:
            _list.append(sys.argv[i])
    _file.write(json.dumps(_list))
