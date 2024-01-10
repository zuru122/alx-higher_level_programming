#!/usr/bin/python3
# Sunday, Justice Gabriel
"""
Write a function that replaces an element in a list
at a specific position without modifying the original
list (like in C).
"""


def new_in_list(my_list, idx, element):
    _copy = my_list.copy()
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    _copy[idx] = element
    return _copy
