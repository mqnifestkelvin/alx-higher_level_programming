#!/usr/bin/python3


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
        """
        Raise:
            TypeError: if width is not an integer.
            ValueError: if width is less than zero (0)
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Raise:
            TypeError: if height is not an integer.
            ValueError: if height is less than zero (0)
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
