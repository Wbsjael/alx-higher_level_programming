#!/usr/bin/python3
# loop through the numbers 0 to 99
# using the {0:d} format specifier to print integer value in decimal form
for num in range(0, 99):
    print("{0:d} = 0x{0:x}".format(num))
