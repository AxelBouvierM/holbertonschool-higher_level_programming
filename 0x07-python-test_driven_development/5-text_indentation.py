#!/usr/bin/python3
"""
function that prints a text with 2 new lines after each of these characters:
., ? and :
"""


def text_indentation(text):
    """
    Function that print blanckline when find a special
    character text_indentation
    Raises:
        TypeError: If text is not str
    """
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
