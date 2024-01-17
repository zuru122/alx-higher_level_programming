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
    if a_dictionary:
        max_value = max(a_dictionary, key=a_dictionary.get)
    else:
        max_value = None
    return(max_value)
