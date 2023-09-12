#!/usr/bin/python3
"""Json"""


import json as jsn


def to_json_string(my_obj):
    """function that that returns the
    JSON representation of an object (string):"""
    return jsn.dumps(my_obj)
