#!/usr/bin/python3
def add_integer(a, b=98):
    """Return the integer addition of a and b.

        Float arguement will be type casted to
        integer before addition.

        Raise:
            TypeError: if a or b variable are non integer or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
