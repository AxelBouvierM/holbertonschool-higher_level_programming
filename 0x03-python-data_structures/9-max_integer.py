#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_num = my_list[0]
    for count in my_list:
        if count > max_num:
            max_num = count
    return max_num
