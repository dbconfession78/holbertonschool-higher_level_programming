#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_elements = set()
    for elem in set_1:
        if elem in set_2:
            common_elements.add(elem)
    return common_elements
