#!/usr/bin/python3
# function that takes integer as input
def print_last_digit(number):
    last_digit = number % 10
    print("{:d}".format(last_digit), end="")
    if number < 0:
        last_digit = -last_digit
        return last_digit
