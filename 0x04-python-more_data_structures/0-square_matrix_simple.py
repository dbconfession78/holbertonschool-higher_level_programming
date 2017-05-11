#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = []
    for i, list in enumerate(matrix):
        sq_list = []
        for number in matrix[i]:
            square = number ** 2
            sq_list.append(square)
        result_matrix.append(sq_list)
    return (result_matrix)
