#!/usr/bin/python3
"""square.py"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """define a class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """inherits all properties from Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        return """[Square] ({}) {}/{} - {}""".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the attrs"""
        attrs = ["id", "size", "x", "y"]
        if args is not None and bool(args) is True:
            i = 0
            for key in attrs:
                try:
                    setattr(self, key, args[i])
                except IndexError:
                    pass
                i += 1

        else:
            for key in attrs:
                try:
                    setattr(self, key, kwargs[key])
                except KeyError:
                    pass

    def to_dictionary(self):
        """return dict representation"""
        order = ["id", "x", "size", "y"]
        attrs = {}
        for key in order:
            attrs[key] = getattr(self, key)
        return attrs
