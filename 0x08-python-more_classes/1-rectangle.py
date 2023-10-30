#!/usr/bin/python3
"""1-Rectangle.py"""


class Rectangle:
    """class that defines a rectangle by: (based on 0-rectangle.py)"""

    def __init__(self, width=0, height=0):
        """initialize private instances attribute"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value to the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value to the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
