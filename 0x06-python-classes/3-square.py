#!/usr/bin/python3
"""Define a Class Square"""


class Square:
    def __init__(self, size=0):
        """Constructor.
        Args:
            size: The size of the square.
            
        Raise:
            TypeError: The argument passed is not and integer.
            ValueError: The arguement passed is less than Zero (0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__self = size

    def area(self):
        """Area of the square passed.

        Returns:
            The area of the square
        """
        return self.__self ** 2
