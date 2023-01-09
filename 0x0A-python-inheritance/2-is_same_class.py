#!/usr/bin/python3
def is_same_class(obj, a_class):
    """A function that check instance membership.

    Args:
        Obj: The object class to be checked.
        a_class: The class to be chacked for membership.
    Returns:
        True if obj is part of a_class and  False if it isn't
    """
    return type(obj) == a_class
