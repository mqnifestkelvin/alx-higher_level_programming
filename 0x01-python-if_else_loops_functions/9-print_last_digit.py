#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        number %= 10
        print("{}".format(number))
        return number
    if number < 0:
        number %= -10
        print("{}".format(number))
        return number * -1
    if number == 0:
        number %= 10
        print("{}".format(number))
        return number


print_last_digit(2023)
