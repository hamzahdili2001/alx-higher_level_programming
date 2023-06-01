#!/usr/bin/python3
"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix.
    """

    if not isinstance(matrix, list)\
            or not all(isinstance(row, list) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(num / div, 2) for num in row] for row in matrix]
