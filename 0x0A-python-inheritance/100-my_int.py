#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """Define Class"""

    def __eq__(self, value):
        """Change == opeartor with !="""
        return self.real != value

    def __ne__(self, value):
        """Change != opeartor with =="""
        return self.real == value
