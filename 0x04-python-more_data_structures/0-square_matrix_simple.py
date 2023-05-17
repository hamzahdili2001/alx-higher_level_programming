#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        square_row = map(lambda x: x ** 2, row)
        square_matrix.append(list(square_row))

    return square_matrix
