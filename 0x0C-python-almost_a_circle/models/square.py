#!/usr/bin/python3
"""Square Module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constractor"""
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """returns String"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width
                )

    @property
    def size(self):
        """size Getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.heigth = value

    def update(self, *args, **kwargs):
        """Update attrs of Square"""
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
        "return dict representation of a Square"
        order = ["id", "x", "size", "y"]
        attrs = {}
        for key in order:
            attrs[key] = getattr(self, key)
        return attrs
