#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    aux = []
    if a_dictionary:
        for i in a_dictionary.keys():
            if a_dictionary[i] == value:
                aux.append(i)
    for i in aux:
        del a_dictionary[i]
    return a_dictionary
