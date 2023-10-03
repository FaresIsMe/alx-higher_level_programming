#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = abs(number) % 10
if x > 5 and number > 0:
    print(f"Last digit of {number} is {x} and is greater than 5")
elif x == 0:
    print(f"Last digit of {number} is {0} and is 0")
else:
    x = -x
    print(f"Last digit of {number} is {x} and is less than 6 and not 0")
