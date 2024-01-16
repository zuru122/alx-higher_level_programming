#!/usr/bin/python3
# Author: Sunday, Justice Gabriel
"""
Write a function that returns a set of
all elements present in only one set.
Prototype: def only_diff_elements(set_1, set_2):
You are not allowed to import any module
"""


def only_diff_elements(set_1, set_2):
    _set1 = set_1.difference(set_2)
    _set2 = set_2.difference(set_1)
    _set = _set1.union(_set2)
    return _set
