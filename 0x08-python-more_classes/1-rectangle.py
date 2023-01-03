#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represents a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initalize a Rectangle.

        Args:
            width: the integer value of the rectangles width.
            height: the integer value of the retangles height.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        """
        Raise:
            TypeError: if width is not an int.
            ValueError: if width is less than zero (0)
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
         """
        Raise:
            TypeError: if height is not an int.
            ValueError: if height is less than zero (0)
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__heigth = value
