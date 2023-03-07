#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if (number < 0):
    last = -last
if (last > 5):
    print("Last digit of {0} is {1} and is greater than 5".format(number, last))
elif (last == 0):
    print("Last digit of {0} is {1} and is 0".format(number, last))
else:
    print("Last digit of {0} is {1} and is less than 6 and not 0".format(number, last))
