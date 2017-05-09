#!/usr/bin/python3
def max_integer(my_list=[]):
    _max = 0
    if my_list is None or len(my_list) == 0:
        return None

    for elem in my_list:
        if elem > _max or elem == my_list[0]:
            _max = elem

    return _max
