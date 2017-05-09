#!/usr/bin/python3
DEFAULT = object()
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None

    if len(matrix[0]) == 0 and len(matrix) == 1:
        print()
        return

    for i in range(0, len(matrix)):
        print("{}".format(matrix[i]))
