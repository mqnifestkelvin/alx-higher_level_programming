#!/usr/bin/python3
""" 5-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

    print("This is height {}".format(r1.height))
    print("This is width {}".format(r1.width))
    print("This is x {}".format(r1.x))
    print("This is y {}".format(r1.y))
