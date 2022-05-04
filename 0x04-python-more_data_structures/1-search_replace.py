#!/usr/bin/python3
def search_replace(my_list, search, replace):
    dup = my_list[:]
    for i, x in enumerate(dup):
        if x == search:
            dup[i] = replace
    return dup
