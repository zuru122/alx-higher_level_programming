#!/usr/bin/python3
# Author: Sunday, Justice Gabriel

def multiple_returns(sentence):
    if sentence != '':
        first_char = sentence[0]
    else:
        first_char = None
    return (len(sentence), first_char)
