#!/usr/bin/python3
"""The Base Class"""


import json as jsn


class Base:
    """Manager of the id attr"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constractor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json representation"""
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return '[]'
        else:
            jsn_str = jsn.dumps(list_dictionaries)
            return jsn_str
