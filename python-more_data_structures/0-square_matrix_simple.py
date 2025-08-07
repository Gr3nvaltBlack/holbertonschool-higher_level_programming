#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [[idx ** 2 for idx in row] for row in matrix]
    return new_matrix
