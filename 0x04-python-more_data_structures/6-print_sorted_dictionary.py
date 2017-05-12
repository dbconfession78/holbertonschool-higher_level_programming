#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    if my_dict is None:
        return

    for key in sorted(my_dict):
        print("{}: {}".format(key, my_dict[key]))