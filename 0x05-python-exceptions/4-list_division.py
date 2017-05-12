#!/usr/bin/python3

# list_division - divides element by elemnt between two lists
# my_list_1: list containing numbers to be divided
# my_list_2: list containing numbers to divide with
# Return: a new_list containing the result of each division


def list_division(my_list_1, my_list_2, list_length):
    div_list = []

    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            div_list.append(div)
    return div_list
