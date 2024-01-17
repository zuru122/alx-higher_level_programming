#!/usr/bin/python3
# Author: Sunday, Justice Gabriel
# ALX Task

"""
Create a function def roman_to_int(roman_string):
that converts a Roman numeral to an integer.
"""


def roman_to_int(roman_string):
    dict_ = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    _sum = 0
    prev_value = 0

    for i in reversed(roman_string):
        current_value = dict_[i]

        if current_value < prev_value:
            _sum -= current_value
        else:
            _sum += current_value

        prev_value = current_value

    return _sum
