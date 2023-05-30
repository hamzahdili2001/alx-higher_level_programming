#!/usr/bin/python3
"""Definition iof MagicClass"""


import math


class MagicClass:
    """MagicClass"""

    def __init__(self, radius=0):
        """constractor"""
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        """returns: radius"""
        return self.radius

    @radius.setter
    def radius(self, value):
        """set the radius"""
        if type(value) not in [int, float]:
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """claculate the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """claculate circumference"""
        return 2 * math.pi * self.__radius
