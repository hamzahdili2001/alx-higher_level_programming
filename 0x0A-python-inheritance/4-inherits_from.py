#!/usr/bin/python3
"""4-inherits_from.py"""


def inherits_from(obj, a_class):
    """
    Write a function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False.
    """

    return issubclass(type(obj), a_class)
