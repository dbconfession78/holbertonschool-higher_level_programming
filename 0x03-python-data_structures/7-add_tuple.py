#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return

    a1 = 0
    a2 = 0
    b1 = 0
    b2 = 0

    if len(tuple_a) != 0:
        a1 = tuple_a[0]

    if len(tuple_b) != 0:
        b1 = tuple_b[0]

    if len(tuple_a) > 1:
        a2 = tuple_a[1]

    if len(tuple_b) > 1:
        b2 = tuple_b[1]

    sum_1 = a1 + b1
    sum_2 = a2 + b2

    return (sum_1, sum_2)
