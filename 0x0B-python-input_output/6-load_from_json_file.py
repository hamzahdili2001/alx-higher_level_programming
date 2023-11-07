#!/usr/bin/python3
"""6-load_from_json_file.py"""

import json as jsn


def load_from_json_file(filename):
    """load form json file"""
    with open(filename, "r", encoding="utf-8") as file:
        return jsn.load(file)
