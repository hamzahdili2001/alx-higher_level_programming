#!/usr/bin/python3
"""
This module contains a function that adds two integers.
Functions:
    add_integer(a, b=98): Adds two integers.
"""


def add_integer(a, b=98):
    """Adds two integers.
        Return: a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
