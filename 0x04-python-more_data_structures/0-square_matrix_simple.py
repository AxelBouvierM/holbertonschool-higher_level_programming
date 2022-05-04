#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    dup = []
    for i in matrix:
        dup.append(list(map(lambda x: x ** 2, i)))
    return dup
