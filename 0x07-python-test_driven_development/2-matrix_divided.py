#!/usr/bin/python3
def matrix_divided(matrix, div):
    result = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        for x in i:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for listt in matrix:
        if len(matrix[0]) != len(listt):
            raise TypeError("Each row of the matrix must have the same size")
        matrix2 = []
        for elements in listt:
            matrix2.append(round(elements / div, 2))
        result.append(matrix2)
    return result
