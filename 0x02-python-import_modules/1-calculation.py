#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    a = 10
    b = 5
    output = "{:d} {} {:d} = {:d}"
    print(output.format(a, '+', b, add(a, b)))
    print(output.format(a, '-', b, sub(a, b)))
    print(output.format(a, '*', b, mul(a, b)))
    print(output.format(a, '/', b, div(a, b)))
