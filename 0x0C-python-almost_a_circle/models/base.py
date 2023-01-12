#!/usr/bin/python3
"""A Module of Class Base."""


class Base:
    """A class Base."""
    __nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            __class__.__nb_object += 1
            self.id = __class__.__nb_object
