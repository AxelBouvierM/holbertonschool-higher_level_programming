#!/usr/bin/python3
def text_indentation(text):
    flag = 0

    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if flag == 1:
            flag = 0
            continue
        else:
            print(char, end="")
        if char == "." or char == "?" or char == ":":
            flag = 1
            print()
            print()
