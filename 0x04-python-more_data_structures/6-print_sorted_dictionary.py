#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    # print the key value pairs in order also changed j to key
    for key in sorted_keys:
        print(key, ":", a_dictionary[key])
