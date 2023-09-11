#!/usr/bin/python3
"""class Mylist that inherits form list"""


class MyList(list):
    """Class Mylist"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
