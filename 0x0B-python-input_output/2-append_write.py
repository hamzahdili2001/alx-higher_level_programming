#!/usr/bin/python3
"""2-append_write.py"""


def append_write(filename="", text=""):
    """append to a file"""
    with open(filename, "a", encoding="UTF-8") as file:
        return file.write(text)
