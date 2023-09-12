#!/usr/bin/python3
"""Json"""


import json as jsn

def save_to_json_file(my_obj, filename):
    """function that writes an Object
    to a text file, using a JSON representation"""
    with open(filename, 'w') as j:
        jsn.dump(my_obj, j)
