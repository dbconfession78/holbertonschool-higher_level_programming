#!/usr/bin/python3
def max_integer(my_list=[]):
    _max = 0

    if my_list is None or len(my_list) == 0:
        return None

    _max = my_list[0]

    for elem in my_list:
        if elem > _max:
            _max = elem

    return _max
