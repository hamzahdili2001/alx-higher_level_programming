#!/usr/bin/python3
"""5-save_to_json_file.py"""

import json as jsn


def save_to_json_file(my_obj, filename):
    """save to json file"""
    with open(filename, "w", encoding="utf-8") as file:
        return jsn.dump(my_obj, file)
