#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = sorted(a_dictionary)    
    for i in key:
        print(f"{i}: {a_dictionary[i]}")
