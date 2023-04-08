#!/usr/bin/python3
"""Module for division of number with a matrix"""


def matrix_divided(matrix, div):
    """Matrix is divided by div"""
    err = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(err)
    len_row = []
    row_count = 0
    for row in (matrix):
        if type(row) is not list:
            raise TypeError(err)
        len_row.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(err)
        row_count += 1
    if len(set(len_row)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row:
                                    list(map(lambda x: round(x / div, 2), row)), matrix))
    return new_matrix
