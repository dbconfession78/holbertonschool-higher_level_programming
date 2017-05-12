#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_count = 0
    for i in range(x):
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end='')
                int_count = int_count + 1
        except IndexError as err:
            print(err)
            raise

    print()
    return int_count
