#!/usr/bin/python3
"""class Square."""


class Square:
    """Square."""
    def __init__(self, size=0, position=(0, 0)):
        """Define a Square
        Args:
            sise - Private instance attribute
            position - a tuple of 2 positive integers"""
        self.__size = size
        self.__position = position

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
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """position property"""
        return self.__position

    @position.setter
    def position(self):
        """position setter"""
        if not isinstance(value, tuple) or len(value) != 2\
                or not isinstance(value[0], int)\
                or not isinstance(value[1], int) or value[0] < 0\
                or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns: the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
