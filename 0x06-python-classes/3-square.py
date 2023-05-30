#!/usr/bin/python3
"""class Square."""


class Square:
    """Square."""
    def __init__(self, size=0):

        """Class Square that defines a square by: (based on 0-square.py)
        Args:
            size (int): Private instance attribute."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns: the current square area"""
        return self.__size ** 2
