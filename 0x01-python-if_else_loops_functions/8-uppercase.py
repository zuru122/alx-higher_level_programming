#!/usr/bin/python3
def uppercase(str):
    """function that checks for upper case characters"""
    if ord(str) >= 65 and ord(str) <= 90:
        return True
    else:
        return False
