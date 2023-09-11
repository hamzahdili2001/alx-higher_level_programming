#!/usr/bin/python3
"""class MyInt that inherits from int"""

class MyInt(int):
    """Define Class"""

    def __eq__(self, other):
        """Change == opeartor with !="""
        return self.real != other

    def __ne__(self, other):
        """Change != opeartor with =="""
        return self.real == other
