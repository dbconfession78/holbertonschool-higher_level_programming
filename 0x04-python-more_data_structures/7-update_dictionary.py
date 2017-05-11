#!/usr/bin/python3
def update_dictionary(my_dict, key, value):
    if my_dict is None or key is None or value is None:
        return

    my_dict[key] = value
    return my_dict
