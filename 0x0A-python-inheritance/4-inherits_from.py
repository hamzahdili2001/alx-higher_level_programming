#!/usr/bin/python3
"""Function that returns True if the object is
an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Returns True or false"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
