#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    num = sum(list(map(lambda x: x[0] * x[1], my_list)))
    num1 = sum(list(map(lambda x: x[1], my_list)))
    return num / num1
