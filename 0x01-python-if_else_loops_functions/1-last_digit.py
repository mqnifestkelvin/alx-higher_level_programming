#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    if number % 10 > 5:
        hold = number % 10
        print(f"Last digit of {number} is {hold} and is greater than 5")
elif number % 10 == 0:
    hold = number % 10
    print(f"Last digit of {number} is {hold} and is 0")
elif number > 0 and number % 10 < 6:
    hold = number % 10
    print(f"Last digit of {number} is {hold} and is less than 6 and not 0")
if number < 0 and number % -10 < 0:
    hold = number % -10
    print(f"Last digit of {number} is {hold} and is less than 6 and not 0")
