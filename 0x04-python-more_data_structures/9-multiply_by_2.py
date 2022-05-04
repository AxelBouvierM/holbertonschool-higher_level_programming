#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    key = list(a_dictionary)
    aux = {}
    for i in key:
        aux[i] = a_dictionary[i] * 2
    return aux
