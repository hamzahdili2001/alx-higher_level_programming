#!/usr/bin/python3
"""11-student.py"""


class Student:
    """class Student that defines a student by: (based on 10-student.py)"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
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

    def reload_from_json(self, json):
        """Function that replace all
        attributes of the Student instance"""
        for k, v in json.items():
            setattr(self, k, v)
