#!/usr/bin/python3
import random
number = random.randint(-10, 20)
if number > 0:
    print(f"{number} is postive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")
