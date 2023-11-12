#!/usr/bin/python3
"""base.py is a file that contains a class Base"""

import json as jsn
import csv
import turtle


class Base:
    """Defines the Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a public instance : id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"
        else:
            jsn_str = jsn.dumps(list_dictionaries)
            return jsn_str

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or bool(json_string) is False:
            json_string = "[]"
        return jsn.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dm = cls(1, 1)
        elif cls.__name__ == "Square":
            dm = cls(1)
        dm.update(**dictionary)
        return dm

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    names = ["id", "width", "height", "x", "y"]
                else:
                    names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file_csv"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    names = ["id", "width", "height", "x", "y"]
                else:
                    names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(file, fieldnames=names)
                list_dicts = [
                    dict([k, int(v)] for k, v in d.items()) for d in list_dicts
                ]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        tr = turtle.Turtle()
        tr.screen.bgcolor("#393552")
        tr.pensize(3)
        tr.shape("turtle")
        tr.color("#f6c177")

        for rect in list_rectangles:
            tr.showturtle()
            tr.up()
            tr.goto(rect.x, rect.y)
            tr.down()
            for _ in range(2):
                tr.forward(rect.width)
                tr.left(90)
                tr.forward(90)
                tr.left(90)
            tr.hideturtle()

        tr.color("#3e8fb0")
        for sq in list_squares:
            tr.showturtle()
            tr.up()
            tr.goto(sq.x, sq.y)
            tr.down()
            for _ in range(2):
                tr.forward(sq.width)
                tr.left(90)
                tr.forward(sq.height)
                tr.left(90)
            tr.hideturtle()

        turtle.exitonclick()
