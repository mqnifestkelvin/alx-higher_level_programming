#!/usr/bin/python
"""A Module for a Class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """A Class Rectangle Inheriting form the Class Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of instance attributes
            
            Args:
                width (int): The width of the new Rectangle.
                height (int): The height of the new Rectangle.
                x (int): The x coordinate of the new Rectangle
                y (int): The y coordinate of the new Rectangle
                id (int): The identify of the new Rectangle

            Raises:
                TypeError: If either width or height is not an integer
                ValueError: if either width or height is less than Zero
                TypeError: if either x or y is not an integer
                ValueError: if either x or y is less than Zero
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the value of width for the Rectangle object"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
         """Returns the value of height for the Rectangle object"""
         return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        """Returns the value of x for the Rectangle object"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    @property
    def y(self):
        """Returns the value of y for the Rectangle object"""
        return self.__y

    @x.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an int")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height
    
    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        return "[Rectangle] ({}) {}/{} {}/{}".format(self.id,
                                                     self.x,
                                                     self.y,
                                                     self.width,
                                                     self.height)
