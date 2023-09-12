#!/usr/bin/python3
"""Read from a file"""


def read_file(filename=""):
    """function that read from a file"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
