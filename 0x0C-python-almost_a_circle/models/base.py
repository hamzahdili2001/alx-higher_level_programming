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

    @classmethod
    def save_to_file(cls, list_objs):
        """write the string representation of json to a file"""
        filename = "{}.json".format(cls.__name__)
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                _dict = obj.to_dictionary()
                list_dicts.append(_dict)
            jsn_str = Base.to_json_string(list_dicts)
            with open(filename, 'w') as f:
                if list_objs is None:
                    f.write("[]")
                else:
                    f.write(jsn_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of json string"""
        if json_string is None or bool(json_string) is False:
            json_string = "[]"
        return jsn.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Updates the Base class"""
        if cls.__name__ == "Rectangle":
            dm = cls(1, 1)
        elif cls.__name__ == "Square":
            dm = cls(1)
        dm.update(**dictionary)
        return dm

    @classmethod
    def load_from_file(cls):
        """load data from a file"""
        filename = "{}.json".format(cls.__name__)
        instance_lst = []
        try:
            with open(filename, 'r') as f:
                jsn_str = f.read()
                list_dict = cls.from_json_string(jsn_str)
                for i in list_dict:
                    instance = cls.create(**i)
                    instance_lst.append(instance)
        except FileNotFoundError:
            return instance_lst
        return instance_lst
