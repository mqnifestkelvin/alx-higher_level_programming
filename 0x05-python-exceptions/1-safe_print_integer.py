#!/usr/bin/python3
def safe_print_intget(value):
    try:
        if value <= 0 or value >= 0:
            print("{:d}".format(value))
            return True
        except (TypeError, ValueError):
            print("{} is not an integer".format(value))
            return False
