#!/usr/bin/python3
"""function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices"""
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a) or\
            not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or \
m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if len(m_a) == 0 or len(m_a[0]) == 0 \
            or len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Check if m_a and m_b contain only integers or floats
    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or\
            not\
            all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats \
or m_b should contain only integers or floats")

    # Check if m_a and m_b are rectangles
    if len(set(len(row) for row in m_a)) > 1 \
            or len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_a must be of the same size or each \
row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(element)
        result.append(row)

    return result
