#!/usr/bin/python3
"""9-student.py"""


class Student:
    """class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """initialize the class with public instance attrs"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        attrs = self.__dict__

        json = {}

        for key, value in attrs.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json[key] = value

        return json
