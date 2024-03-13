#!/usr/bin/python3
# looping through the numbers from 0 to 99 using range function
# using {:02d} to format the integer value in decimal
for num in range(0, 99):
    print("{:02d}".format(num), end=", ")
print("99")
