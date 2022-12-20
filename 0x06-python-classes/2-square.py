#!/usr/bin/python3
"A Square Module"


class Square:
    """Construct of a square"""

    def __init__(self, size=0)
        """Constructor.

        Args:
            Size: The length of the sides of the square.

        Raises:
            TypeError: The arguement size must be an integer.
            ValueError: The arguement passed must be greater than Zero (0)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
