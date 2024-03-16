#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    the_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return the_list
    the_list[idx] = element
    return the_list
