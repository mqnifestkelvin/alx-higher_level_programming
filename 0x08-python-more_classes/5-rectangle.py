#!/usr/bin/python3
"""Module for Rectangle class."""


class Rectangle:
    """This class defines a simple Rectangle."""

    def __init__(self, width=0, height=0):
        """Constructor.
        Args:
            width: The width of the rectangle.
            height: The height of a rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property for the width of the rectangle.
        Raises:
            TypeError: if the width is not an integer.
            ValueError: if the width is less than zeror (0).
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
        """Property of the height of a rectangle.
        Raises:
            TypeError: if the height is not an integer.
            ValueError: if the height is less than zero (0).
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of an instantiated Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of an instantiated Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the Rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (("#" * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        """Returns formal string representation of the rectangle"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """when an Instance is Deleted"""
        print("Bye rectangle...")
