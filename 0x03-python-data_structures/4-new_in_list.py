#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > len(my_list) - 1:
        return my_list.copy()
    my_list[idx] = element
    return my_list.copy()
