#!/usr/bin/python3
"""4-from_json_string.py"""

import json as jsn


def from_json_string(my_str):
    """convert obj to json"""
    return jsn.loads(my_str)
