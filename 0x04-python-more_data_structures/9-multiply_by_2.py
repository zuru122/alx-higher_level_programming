#!/usr/bin/python3
# Author: Sunday, Justice Gabriel

"""
Write a function that returns a new dictionary
with all values multiplied by 2

Prototype: def multiply_by_2(a_dictionary):
You can assume that all values are only integers
Returns a new dictionary
You are not allowed to import any module
"""


def multiply_by_2(a_dictionary):
    'Create a duplicate'
    a_dict_duplicate = a_dictionary.copy()
    for key in a_dict_duplicate:
        a_dict_duplicate[key] *= 2
    return a_dict_duplicate
