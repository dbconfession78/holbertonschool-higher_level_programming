#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or my_list == []:
        return
    truth_list = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            truth_list.append(True)
        else:
            truth_list.append(False)
    return truth_list
