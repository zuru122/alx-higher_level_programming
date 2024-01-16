#!/usr/bin/python3
# Author: Sunday, Justice Gabriel
"""
Write a function that adds all unique integers in a list
(only once for each integer).
Prototype: def uniq_add(my_list=[]):
You are not allowed to import any module
"""


def uniq_add(my_list=[]):
    new_list = set(my_list)
    _sum = 0
    for i in new_list:
        _sum += i
    return _sum
