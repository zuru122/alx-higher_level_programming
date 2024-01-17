#!/usr/bin/python3
# Author: Sunday, Justice Gabriel
"""
Write a function that returns a key with the biggest integer value.

Prototype: def best_score(a_dictionary):
You can assume that all values are only integers
If no score found, return None
You can assume all students have a different score
You are not allowed to import any module
"""


def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best_key = ''
    large_num = list(a_dictionary.values())[0]
    for key in a_dictionary:
        if a_dictionary[key] > large_num:
            large_num = a_dictionary[key]
            best_key = key
    return best_key
