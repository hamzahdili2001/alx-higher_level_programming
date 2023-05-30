import math
"""MagicClass Python bytecode"""


class MagicClass:
    def __init__(self, radius=0):
        """constractor"""
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        """radius property"""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """sets the value"""
        if type(value) not in [int, float]:
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """calc the area"""
        return self.radius ** 2 * math.pi

    def circumference(self):
        """return circumference"""
        return 2 * math.pi * self.radius
