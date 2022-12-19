#!/usr/bin/python3
def magic_calculation(a, b):
    hold = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                hold += a ** b / i
        except(TypeError, ValueError, IndexError):
            hold = b + a
            break
    return hold
