#!/usr/bin/python3
# function that takes a string as input
def uppercase(str):
    # cheking if the char is lowercase
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            # converting the lowercase char to uppercase
            char = ord(char) - 32
        else:
            char = ord(char)
        print("{:c}".format(char), end="")
    print()
