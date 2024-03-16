#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if not row:
            print()
            pass
        else:
            for j, val in enumerate(row):
                if j != (len(row) - 1):
                    print("{:d}".format(row[j]), end=" ")
                else:
                    print("{:d}".format(val))
