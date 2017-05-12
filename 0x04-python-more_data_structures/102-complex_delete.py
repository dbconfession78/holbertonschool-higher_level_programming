#!/usr/bin/python3
def complex_delete(my_dict, value):
    i = 0

    while i < len(my_dict):
        for idx, (key, val) in enumerate(my_dict.items()):
            if val == value:
                my_dict.pop(key)
                if idx == len(my_dict) - 1:
                    return my_dict
                else:
                    i = 0
                    break
            i = i + 1
    return my_dict
