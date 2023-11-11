#!/usr/bin/python3
"""this script defines a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize private instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """calculate the area"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.__width == 0 or self.height == 0:
            print("")
            return

        # print("" * self.y)
        [print("") for _ in range(self.y)]
        for _ in range(self.__height):
            # print(" " * self.x, end="")
            # print("#" * self.__width, end="")
            # print("")
            [print(" ", end="") for _ in range(self.x)]
            [print("#", end="") for _ in range(self.__width)]
            print("")

    def __str__(self) -> str:
        """retrun info in a string format"""
        s = self
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            s.id, s.x, s.y, s.__width, s.height
        )
