#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None or search is None or replace is None:
        return
    new_list = []
    for i, elem in enumerate(my_list):
        if elem == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
    return new_list
