#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        cpy = my_list
        return cpy
    if idx >= len(my_list):
        cpy = my_list
        return cpy
    cpy = my_list[:]
    cpy[idx] = element
    return cpy
