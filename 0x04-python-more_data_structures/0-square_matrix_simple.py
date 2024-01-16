#!/usr/bin/python3
#  Author: Sunday, Justice Gabriel
"""Write a function that computes the square value
of all integers of a matrix."""


def square_matrix_simple(matrix=[]):
    squared = [[x**2 for x in row] for row in matrix]
    return squared
