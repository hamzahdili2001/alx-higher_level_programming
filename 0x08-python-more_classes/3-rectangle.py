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

    def area(self):
        """Returns: Rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns: Rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print Rectangle with char '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = ['#' * self.__width for _ in range(self.__height)]

        return "\n".join(rows)

    def __repr__(self):
        """
        Rectangle that can be used to recreate it
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
