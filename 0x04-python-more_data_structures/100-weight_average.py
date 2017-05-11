#!/usr/bin/python3
def weight_average(my_list=[]):
    _sum = 0
    avg = 0
    tot_weight = 0

    if my_list is None or len(my_list) == 0:
        return 0
    for i, elem in enumerate(my_list):
        _sum += (elem[0] * elem[1])
    for elem in my_list:
        tot_weight += elem[1]
    return _sum / tot_weight
