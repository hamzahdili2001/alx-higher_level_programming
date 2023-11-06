#!/usr/bin/python3
"""11-square.py"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle (9-rectangle.py).
     (task based on 10-square.py).
    """

    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self) -> str:
        """Return a string info"""
        return "[Square] {}/{}".format(self.__size, self.__size)
