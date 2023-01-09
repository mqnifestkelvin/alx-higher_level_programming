#!/usr/bin/python3
"""Module for method lookup."""

def lookup(arg):
    """This function returns a list of all the available methods and attributes.

        Args:
            arg (object): inbuild or user class object.

        Returns:
            list: Returnss a list of all the attributes and methods available in a class. 
    """
    return dir(arg)
