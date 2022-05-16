#!/usr/bin/python3
def magic_calculation(a, b):
    i = 0
    for count in range(1, 3):
        try:
            if count > a:
                raise Exception("Too far")
            else:
                i += (a**b) / count
        except:
            i = (b + a)
            break
    return i
