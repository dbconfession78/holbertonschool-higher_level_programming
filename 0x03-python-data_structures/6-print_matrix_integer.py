#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None

    if len(matrix[0]) == 0 and len(matrix) == 1:
        print()
        return

    for i in range(0, len(matrix)):
        for number in matrix[i]:
            print("{:d}".format(number), end='')
            if matrix[i].index(number) != len(matrix[i]) - 1:
                print(' ', end='')
            else:
                print()
