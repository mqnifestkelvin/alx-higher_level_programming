#!/usr/bin/python3
import sys


def safe_function(fct, *arg):
    try:
        hold = fct(*arg)
        return hold
    except:
        print("Exception: {}".format(sys.exc_info()[1], file=sys.stderr)
        return None
