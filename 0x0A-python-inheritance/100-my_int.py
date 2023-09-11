#!/usr/bin/python3
"""class MyInt that inherits from int"""

class MyInt(int):
    """Define Class"""

    def __eq__(self, other) -> bool:
        """function 1"""
        return super().__eq__(other)

    def __ne__(self, other) -> bool:
        """function 2"""
        return super().__ne__(other)
