#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

if number < 0:
    last_digit = 0 - last_digit

strng = "Last digit of {} is {} and ".format(number, last_digit)

if (last_digit > 5):
    strng = strng + "is greater than 5"
elif (last_digit == 0):
    strng = strng + "is 0"
elif (last_digit < 6 and last_digit != 0):
    strng = strng + "is less than 6 and not 0"

print(strng)
