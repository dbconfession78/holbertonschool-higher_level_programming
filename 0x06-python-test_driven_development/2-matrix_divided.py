#!/usr/bin/python3
"""
This is the matrix_divided module

This module returns a matrix of list
division results.

"""


def matrix_divided(matrix, div):
    """
    matrix_divide
    matrix: matrix whose elements are divided
    div: number to divide matrix lements by
    Return: list of division results
    """

    type_error = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None or len(matrix) == 0:
        raise TypeError(type_error)

    match_list_len = len(matrix[0])
    result = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) == 0:
            raise TypeError(type_error)
        _list = []
        if len(row) != match_list_len:
            raise TypeError("Each row of the matrix must have the same size")
        for number in row:
            if not isinstance(number, (int, float)):
                raise TypeError(type_error)
            _list.append(round(number / div, 2))
        result.append(_list)

    return result
