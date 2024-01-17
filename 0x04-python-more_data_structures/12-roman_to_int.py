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
    for i in roman_string:
        if _sum == 0:
            _sum += dict_[i]
        elif _sum < dict_[i]:
            _sum = dict_[i] - _sum
        elif _sum > dict_[i]:
            _sum += dict_[i]
        else:
            _sum = None
    return _sum
