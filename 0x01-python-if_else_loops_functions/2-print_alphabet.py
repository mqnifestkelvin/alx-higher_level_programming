#!/usr/bin/python3
N = 20
res = ""
for alphabet in range(97, 103 + N):
    res = res + chr(alphabet)
print("{:s}".format(res), end="")
