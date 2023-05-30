#!/usr/bin/python3
"""class Square."""


class Square:
    """Square."""
    def __init__(self, size=0):
        """Define a Square
        Args:
            sise - Private instance attribu"""
        self.size = size

    @property
    def size(self):
        """defines property"""
        return self.__size

    @size.setter
    def size(self, size=0):

        """defines setter
        Args:
            size (int): Private instance attribute."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns: the current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare the area of the current shape with the
        area of another shape for equality.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare the area of the current shape with the
        area of another shape for inequalit"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Compare the area of the current shape with the
        area of another shape for greater than.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare the area of the current shape with the
        area of another shape for greater than or equal to.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Compare the area of the current shape with the
        area of another shape for less than.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare the area of the current shape with the
        area of another shape for less than or equal to.
        """
        return self.area() <= other.area()
