#!/usr/bin/python3
"""Define a Class Square."""


class Square:
    def __init__(self, size):
        """Constructor
        Args:
            size: Size of the square
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the instanciated square"""
        return self.__self

    @size.setter
    def size(self, value):
        """sets a value that is an integer and above zero for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        return self.__size = value

    def area(self):
        return self.__size ** 2
