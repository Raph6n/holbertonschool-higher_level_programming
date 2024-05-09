#!/usr/bin/env python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
message = f"Last digit of {number} is {last_digit}"

if last_digit > 5:
    message += " and is greater than 5"
else:
    if last_digit == 0:
        message += " and is 0"
    else:
        message += " and is less than 6 and not 0"

print(message)
