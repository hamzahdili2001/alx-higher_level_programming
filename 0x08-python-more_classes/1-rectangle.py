#!/usr/bin/python3
"""Define Class Rectangle"""


class Rectangle():
    """Class Rectangle"""
    def __init__(self, width=0, height=0):
        """Constractor
        Args:
            width - (int)
            height - (int)
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Property to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets Value to the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets value to the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value