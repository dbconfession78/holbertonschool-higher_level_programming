#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    if idx > len(my_list) - 1 or idx < 0:
        return my_list
    my_list[idx] = element
    return my_list.copy()
