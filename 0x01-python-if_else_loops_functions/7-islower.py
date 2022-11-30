#!/usr/bin/python3
def islower(c):
    res = ""
    for lalpha in range(97, 123):
        res = res + chr(lalpha)
    if c in res:
        print("{} is lower".format(c))
        return False
    elif c not in res:
        print("{} is upper".format(c))
        return True
