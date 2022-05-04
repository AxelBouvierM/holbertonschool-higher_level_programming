#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        key = list(a_dictionary)
        max_num = key[0]
        for i in key:
            if a_dictionary[i] > a_dictionary[max_num]:
                max_num = i
            else:
                max_num
        return max_num
