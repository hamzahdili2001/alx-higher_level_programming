#!/usr/bin/python3
"""The Rectangle Class"""


from models.base import Base


class Rectangle(Base):
    """Class that inherits from the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constractor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
