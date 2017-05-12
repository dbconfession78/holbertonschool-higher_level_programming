#!/usr/bin/python3

# safe_print_division - divides 2 integers and prinst the result
# a: number to be divided
# b: divider
# Return: result of division or None on fail


def safe_print_division(a, b):
    div = 0
    try:
        div = a / b
    except:
        div = None
    finally:
        print("Inside result: {}".format(div))
        return div
