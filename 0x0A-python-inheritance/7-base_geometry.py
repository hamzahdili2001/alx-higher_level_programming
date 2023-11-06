#!/usr/bin/python3
"""7-base_geometry.py"""


class BaseGeometry:
    """class BaseGeometry (based on 6-base_geometry.py)."""

    def area(self):
        """Public instance method: that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method:  that validates value."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))
