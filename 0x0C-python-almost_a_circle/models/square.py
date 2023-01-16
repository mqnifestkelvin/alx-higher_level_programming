#!/usr/bin/python3
from models.rectangle import Rectangle
"""A Module for a Class Rectangle"""


class Square(Rectangle):
    """Representation of a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """The initialization of square attributes inherited fromrectangle.
    Args:
        size (int): The size of the new Square.
        x (int): The x coordinate of the new Square.
        y (int): The y coordinate of the new Square.
        id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Validating the values passed into the size variable"""
        return self.width

    @size.setter
    def size(self, value):
        """Setting the value of a square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the print() representation and __str__ represntation of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """This module updates keyword args and non-keyword arguements"""
        if args:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """This returns a dictionary representation of the class Square"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width':self.width}
