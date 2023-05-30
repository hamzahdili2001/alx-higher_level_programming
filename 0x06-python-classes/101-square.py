#!/usr/bin/python3
"""class Square."""


class Square:
    """Square."""
    def __init__(self, size=0, position=(0, 0)):
        """Define a Square
        Args:
            sise - Private instance attribute
            position - a tuple of 2 positive integers"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Returns: the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints square with the character #"""
        if self.size == 0:
            print()
            return

        for i in range(self.position[1]):
            print()

        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """Returns: result"""
        result = ""
        if self.size == 0:
            result += "\n"
            return result

        for i in range(self.position[1]):
            result += "\n"

        for i in range(self.size):
            result += " " * self.position[0] + "#" * self.size + "\n"

        return result[:-1]
