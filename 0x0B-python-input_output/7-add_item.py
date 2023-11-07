#!/usr/bin/python3
"""7-add_item.py"""


import sys
from os import path


save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


def add_item():
    """Function that adds all arguments to a Python list,
    and then save them to a file"""
    argv = sys.argv[1:]
    filename = "add_item.json"
    items = []
    if path.exists(filename):
        items = load(filename)

    items = items + argv

    save(items, filename)


if __name__ == "__main__":
    add_item()
