#!/usr/bin/python3
# Author: Sunday, Justice Gabriel
# Task 15: Remove at position

def remove_char_at(str, n):
    if n < 0:
        return str
    return str[:n] + str[n+1:]
