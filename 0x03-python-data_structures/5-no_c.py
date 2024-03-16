#!/usr/bin/python3

def no_c(my_string):
    new_str = ''
    for j in my_string:
        if j not in 'cC':
            new_str += j
    return new_str
