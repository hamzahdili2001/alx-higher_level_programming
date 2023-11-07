#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    triangle = []

    for _ in range(n):
        row = [1]
        if triangle:
            prev_r = triangle[-1]
            row.extend(
                prev_r[j] + prev_r[j + 1] for j in range(len(prev_r) - 1)
            )
            row.append(1)
        triangle.append(row)
    return triangle
