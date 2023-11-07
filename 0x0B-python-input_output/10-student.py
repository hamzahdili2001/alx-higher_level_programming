#!/usr/bin/python3
"""10-student.py"""


class Student:
    """class Student that defines a student by: (based on 9-student.py)"""

    def __init__(self, first_name, last_name, age):
        """initialize the class with public instance attrs"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        return {
            attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)
        }
