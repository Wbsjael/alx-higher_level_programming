#!/usr/bin/python3
# looping from numbers 0 to 9
for i in range(10):
    # looping through numbers i to 9
    for j in range(i + 1, 10):
        print("{:d}{:d}".format(i, j), end="")
        if i < 8:
            print(", ", end="")
        else:
            print("\n", end="")
