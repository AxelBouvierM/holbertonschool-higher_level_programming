#!/usr/bin/python3
"""
returns a list of lists of integers representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle
    """
    if n <= 0:
        return []

    lista = [[1]]
    while len(lista) != n:
        aux = lista[-1]
        tmp = [1]

        for i in range(len(aux) - 1):
            tmp.append(aux[i] + aux[i + 1])

        tmp.append(1)
        lista.append(tmp)
    return lista
