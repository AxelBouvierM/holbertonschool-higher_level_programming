#!/usr/bin/python3
"""
Function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that matrix_divided
    matrix is a list that contain other lists of the same size
    div is the integer that divide matrix
    Return:
        A new matrix with the result of division
    Raises:
        TypeError: If div is not int or float
        ZeroDivisionError: If div is equal to 0
        TypeError: If the matrix is not list or the content of list is not int
        or float
        TypeError: If the list inside the matrix are the diferent types
    """
    result = []
    msj = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        for x in i:
            if type(x) is not int and type(x) is not float:
                raise TypeError(msj)
    for listt in matrix:
        if len(matrix[0]) != len(listt):
            raise TypeError("Each row of the matrix must have the same size")
        matrix2 = []
        for elements in listt:
            matrix2.append(round(elements / div, 2))
        result.append(matrix2)
    return result
