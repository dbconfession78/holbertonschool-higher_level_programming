#!/usr/bin/python3
def multiply_by_2(my_dict):
    result_dict = {}

    if my_dict is None:
        return
    for key in my_dict:
        result_dict[key] = my_dict[key] * 2
    return result_dict
