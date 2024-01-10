#!/usr/bin/python3
# Author: Sunday, Justice Gabriel

"""
Write a function that removes all characters c and C from a string.
"""


def no_c(my_string):
    chars_to_remove = ['C', 'c']
    new_string = "".join(
            char for char in my_string if char not in chars_to_remove
    )
    return new_string
