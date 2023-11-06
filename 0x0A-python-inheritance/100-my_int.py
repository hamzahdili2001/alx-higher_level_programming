#!/usr/bin/python3
"""100-my_int.py"""


class MyInt(int):
    """a class MyInt that inherits from int"""
    def __eq__(self, value) -> bool:
        """Override the equality (==) operator"""
        return not super().__eq__(value)

    def __ne__(self, value) -> bool:
        """Override the inequality (!=) operator"""
        return not super().__ne__(value)
