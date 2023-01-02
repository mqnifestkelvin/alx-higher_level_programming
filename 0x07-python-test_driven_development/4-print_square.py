#!/usr/bin/python3
def print_square(size):
    """
    Prints a square out of the pound symbol.
    arg:
        Size: The dimension of the square
        
    raise:
        TypeError: if size is not an integer
        ValueError: if size is less than zero (0)
        TypeError: if size is a float and less than zero (0)
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise TypeError("size must be >= 0")
        
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
