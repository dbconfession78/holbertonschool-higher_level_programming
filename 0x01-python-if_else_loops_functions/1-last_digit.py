#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
is_neg = False
last_digit = abs(number) % 10

if number < 0 and last_digit != 0:
    is_neg = True

print("Last digit of {:d} is ".format(number), end='')
if is_neg:
    print("-", end='')
print("{:d} ".format(last_digit), end='')
if is_neg:
    print("and is less than 6 and not 0")
else:
    if last_digit > 5:
        print("and is greater than 5")
    elif last_digit == 0:
        print("and is 0")
    else:
        print("and is less than 6 and not 0")
