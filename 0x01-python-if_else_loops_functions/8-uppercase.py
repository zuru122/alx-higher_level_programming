#!/usr/bin/python3
def uppercase(str):
    """function that checks for upper case characters"""
    upper = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            upper += (chr(ord(char) - 32))
        else:
            upper += char
    print(upper)
