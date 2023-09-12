#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    """function that append to a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
