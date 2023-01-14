#!/usr/bin/python3
from module.rectangle import Rectangle
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
        super.__init__(size, x, y, id)

    @property
    def size(self):
        """Validating the values passed into the size variable"""
        return self.width

    @size.setter
    def size(self, value):
        """Setting the value of a square"""
        self.width = value
        self.heigth = value

