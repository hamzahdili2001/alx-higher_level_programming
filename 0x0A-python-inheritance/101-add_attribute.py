#!/usr/bin/python3
"""Function That adds a new attribute to an object"""


def add_attribute(obj, attr, value):
    """The function"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr] = value
