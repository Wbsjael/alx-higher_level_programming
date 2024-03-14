#!/usr/bin/python3
import sys
if __name__ == "__main__":

    argv = sys.argv[1:]
    n_args = len(argv)  # n_args is the number of arguments

    if n_args == 0:
        print("{:d} arguments.".format(0))
    elif n_args == 1:
        print("{:d} argument:".format(1))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(n_args))
        for i, arg in enumerate(argv, 1):
            print("{:d}: {}".format(i, arg))
