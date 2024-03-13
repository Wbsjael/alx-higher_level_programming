#!/usr/bin/python3
# function that takes a single char as input
def islower(c):
    # checking if unicode code is between 97 and 122
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
