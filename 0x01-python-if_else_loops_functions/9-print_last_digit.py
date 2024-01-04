#!/usr/bin/python3
""" a function that prints the last digit of a number."""


def print_last_digit(number):
    last_num = (abs(number) % 10)
    print("{:d}".format(last_num), end="")
    return last_num
