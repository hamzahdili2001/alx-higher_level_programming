#!/usr/bin/python3
"""100-append_after.py"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, "r", encoding="UTF-8") as file:
        lines = file.readlines()

    with open(filename, "w", encoding="UTF-8") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
