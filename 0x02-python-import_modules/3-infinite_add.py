#!/usr/bin/python3
import sys

if __name__ == "__main__":

    result = 0
    length = len(sys.argv)
    for i in range(1, length):
        result += int(sys.argv[i])
    print(result)
