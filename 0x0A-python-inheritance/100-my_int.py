#!/usr/bin/python3
"""class MyInt that inherits from int"""

class MyInt(int):
    """Define Class"""

    def __eq__(self, other):
        """function 1"""
        return self.real != other

    def __ne__(self, other):
        """function 2"""
        return self.real == other
