#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_aux = tuple_a + (0, 0)
    tuple_aux1 = tuple_b + (0, 0)
    sum0 = tuple_aux[0] + tuple_aux1[0]
    sum1 = tuple_aux[1] + tuple_aux1[1]
    result = (sum0, sum1)
    return result
