#!/usr/bin/python3
'''Function that adds two integer'''


def add_integer(a, b=98):
    '''Function that adds two integer
    Return: result of two number
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    result = int(a) + int(b)

    return result
