#!/usr/bin/python3
"""1-my_list.py"""


class MyList(list):
    """MyList a class that inherits from list"""

    def print_sorted(self):
        """Function that returns a sorted list"""
        print(sorted(self))
