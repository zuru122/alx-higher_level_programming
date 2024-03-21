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
    if not a_dictionary:
        return None
        '''float('-inf') represents negative infinity as a
        floating-point number in Python.'''
    max_value = float('-inf')
    for key in a_dictionary:
        if a_dictionary[key] > max_value:
            max_value = a_dictionary[key]
    return max_value
