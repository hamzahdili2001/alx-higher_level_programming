#!/usr/bin/python3
"""Json"""


import json as jsn


def load_from_json_file(filename):
    """Write a function that creates an Object from a “JSON file”"""
    with open(filename, 'r') as j:
        return jsn.load(j)
