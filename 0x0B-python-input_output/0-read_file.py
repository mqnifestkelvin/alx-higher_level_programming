#!/usr/bin/python3
"A Module for Reading Files"


def read_file(filename=" "):
    """A fundction that reads a text file using Utf encoding"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print("{}".format(f.read()), end="")
