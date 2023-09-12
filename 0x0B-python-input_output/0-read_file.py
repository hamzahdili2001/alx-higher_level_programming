#!/usr/bin/python3
"""Read from a file"""


def read_file(filename=""):
    """function that read from a file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read(), end='')
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    read_file("my_file_0.txt")
