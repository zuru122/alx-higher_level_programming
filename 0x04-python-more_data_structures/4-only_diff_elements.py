#!/usr/bin/python3
# Author: Sunday, Justice Gabriel
"""
Write a function that returns a set of
all elements present in only one set.
Prototype: def only_diff_elements(set_1, set_2):
You are not allowed to import any module
"""


def only_diff_elements(set_1, set_2):
    return (set_1 ^ set_2)
