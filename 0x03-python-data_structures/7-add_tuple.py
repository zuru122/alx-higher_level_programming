#!/usr/bin/python3
# Author: Sunday, Justice Gabriel
# Tupples Addition

def add_tuple(tuple_a=(), tuple_b=()):
    '''(0,0) Ensure tuples have at leat 2 element'''
    '''the [:2] takes the  firt two element of each tupple'''
    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)

    ''' Add correponding elements and return a new tuple'''
    return(a[0] + b[0], a[1] + b[1])
