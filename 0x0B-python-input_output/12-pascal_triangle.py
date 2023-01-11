#!/usr/bin/python3
"""A Module tgat Defines a Pascals Triangle"""


def pascal_triangle(n):
    """A function that returns a list of the pascals triangle"""
    triangle = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
    return triangle
