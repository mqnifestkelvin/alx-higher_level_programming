#!/usr/bin/python3
"""A Module that Inserts a Line of Text to A file."""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text to a file.

    Args:
        filename (str): The name of the file to be created.
        search_string (str): The the search string.
        new_string (str): The replacement string after the search.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')
