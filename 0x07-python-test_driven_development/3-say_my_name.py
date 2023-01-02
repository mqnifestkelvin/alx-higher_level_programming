#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints first and last name given.
    args:
        first_name: The first argument passed known as first name
        last_name: The second arguement passed known as last name

    Raises:
        TypeError: if first_name or last_name passed is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
