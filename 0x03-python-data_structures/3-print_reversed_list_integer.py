#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return

    reverse_my_list = reversed(my_list)
    for i in reverse_my_list:
        print("{:d}".format(i))
