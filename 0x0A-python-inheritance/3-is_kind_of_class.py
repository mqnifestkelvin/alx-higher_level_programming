#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """Checks if an object is a subclass of an instance.
    Args:
        obj: The object to be copared.
        a_class: The class to compare the object to.
    Return:
        If an object is an instance or inherited instance of a class -True
        Otherwise - False
    """
    return isinstance(obj, a_class)
