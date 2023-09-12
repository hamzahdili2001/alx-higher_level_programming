#!/usr/bin/python3
"""class Student"""


class Student:
    """Student instances"""

    def __init__(self, first_name, last_name, age) -> None:
        """constractor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=""):
        """Function that retrieves a dictionary
        representation of a Student instance
        (same as 8-class_to_json.py)"""

        if attr is None:
            j_dict = {}
            for a in attr:
                if hasattr(self, attr):
                    j_dict[a] = getattr(self, a)
        return j_dict
