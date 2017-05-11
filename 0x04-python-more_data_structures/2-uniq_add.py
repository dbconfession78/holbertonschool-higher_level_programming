#!/usr/bin/python3
def uniq_add(my_list=[]):
    _sum = 0
    used_list = []

    if my_list is None:
        return
    for elem in my_list:
        if elem not in used_list:
            used_list.append(elem)
            _sum += elem
    return _sum
