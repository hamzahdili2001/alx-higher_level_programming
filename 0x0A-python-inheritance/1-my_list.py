#!/usr/bin/python3
"""class MyList that inherits form list"""


class MyList(list):
    """implemantation of Class MyList"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
