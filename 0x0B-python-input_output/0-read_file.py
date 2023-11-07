#!/usr/bin/python3
"""0-read_file.py"""


def read_file(filename=""):
    """read from a file"""
    with open(filename, "r", encoding="UTF-8") as file:
        print(file.read(), end="")
