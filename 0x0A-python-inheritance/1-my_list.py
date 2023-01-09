#!/usr/bin/python3
"""Module for Class MyList."""


class MyList(list):
    """A Class My_List."""
    def __init__(self):
        """Initializing the object MyList"""
        super().__init__()

    def print_sorted(self):
        """Method for printing a sorted list."""
        print(sorted(self))
