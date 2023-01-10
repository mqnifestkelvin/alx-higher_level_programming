#!/usr/bin/python3
"""A Module that Appends text to a File."""


def append_write(filename="", text=""):
    """This function appends a string to a text file using utf-8 encoding.

    Args:
        filename (str): The name of the file to be appended to.
        text (str): The next to be appended.
    Returns:
        Returns the number of characters appended.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
