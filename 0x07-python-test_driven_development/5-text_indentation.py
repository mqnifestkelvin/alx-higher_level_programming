#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 newlines after each of these characters (., ?, and :).
    args:
        text: an array of strings.

    Raise:
        TypeError: if not a str.
    """
    if not isinstance(text,str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join([line.strip(" ") for line in text.split(delim)])

    print(text, end="")
