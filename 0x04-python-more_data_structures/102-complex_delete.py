#!/usr/bin/python3
def complex_delete(my_dict, value):
    del_keys = []

    if my_dict is None or value is None:
        return
    if value not in my_dict.values() or len(my_dict) == 0:
        return my_dict
    for (key, val) in my_dict.items():
        if val == value:
            del_keys.append(key)
    for key in del_keys:
        del(my_dict[key])
    return my_dict
