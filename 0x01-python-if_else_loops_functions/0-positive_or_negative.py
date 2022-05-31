#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
     "{} is negative".format(number)
elif number > 0:
     "{} is positive".format(number)
else:
     "{} is zero".format(number)