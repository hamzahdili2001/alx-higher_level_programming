#!/usr/bin/python3
"""9-rectangle.py"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
    (task based on 8-rectangle.py).
    """

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self) -> str:
        """Return: string with info"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
