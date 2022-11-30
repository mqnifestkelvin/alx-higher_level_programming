#!/usr/bin/python3
res = ""
N = 20
for alphabet in range(97, 103 + N):
    if alphabet != 101 and alphabet != 113:
        res = res + chr(alphabet)
print("{:s}".format(res), end="")
