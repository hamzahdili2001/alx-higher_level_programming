#!/usr/bin/python3
"""Json"""


import json as jsn


def from_json_string(my_str):
    """function that returns an object
    (Python data structure) represented by a JSON string:"""
    return jsn.loads(my_str)
