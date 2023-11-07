#!/usr/bin/python3
"""3-json_to_string.py"""

import json as jsn


def to_json_string(my_obj):
    """convert obj to json"""
    return jsn.dumps(my_obj)
