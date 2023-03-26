#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda i : list(map(lambda j : (j**2), i)), matrix))

    return (new_matrix)

    return new_matrix
