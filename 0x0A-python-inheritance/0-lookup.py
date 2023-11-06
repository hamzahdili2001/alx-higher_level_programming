#!/usr/bin/python3
"""0-lookup.py"""


def lookup(obj):
    """
    Function that returns the list of available attributes
        and methods of an object.
    Attrs - obj: the object
    Returns: a list object
    """

    return dir(obj)
