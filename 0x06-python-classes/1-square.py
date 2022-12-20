#!/usr/bin/python3
"""A Square Module."""


class Square:
    """Representation of a square."""
    def __init__(self,  size):
        """Constructor.

        args:
            size: The length of all sizes of a square.

        Raises:
            TypeError: If the size arguement is not an integer
            ValueError: If the size arguement is less than Zero (0)
        """
        if not instance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
