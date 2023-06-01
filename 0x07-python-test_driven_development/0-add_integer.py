#!/usr/bin/python3
"""
This module contains a function that adds two integers.

Functions:
    add_integer(a, b=98): Adds two integers.

"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int or float): The first integer to be added.
        b (int or float): The second integer to be added. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
