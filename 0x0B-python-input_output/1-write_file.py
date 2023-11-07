#!/usr/bin/python3
"""1-write_file.py"""


def write_file(filename="", text=""):
    """write to a file"""
    with open(filename, "w", encoding="UTF-8") as file:
        return file.write(text)
