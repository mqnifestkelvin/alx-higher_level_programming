#!/usr/bin/python3
def safe_print_intget(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
