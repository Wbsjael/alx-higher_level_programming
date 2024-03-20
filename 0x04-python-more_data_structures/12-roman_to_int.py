#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    num = 0

    # Iterate over the symbols of the Roman numeral from right to left
    for i in range(len(roman_string) - 1, -1, -1):
        if i == len(roman_string) - 1 or \
                rom[roman_string[i]] >= rom[roman_string[i + 1]]:

            num += rom[roman_string[i]]

        else:

            num -= rom[roman_string[i]]

    return num
