#!/usr/bin/python3
"""101-add_attribute.py"""


def add_attribute(obj, attr, value):
    """a function that adds a new attribute to an object if it’s possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr] = value
