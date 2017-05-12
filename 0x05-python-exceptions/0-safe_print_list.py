#!/usr/bin/python3

# safe_print_list - prints x elemnts of a list
# my_list: list to print
# x: number of elements to print
# Return: number of elements printed


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            count = count + 1
    except:
        Exception
    print()
    return count
