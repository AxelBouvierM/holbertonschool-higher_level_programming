#!/usr/bin/python3
"""
function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    filename is the file to open
    text is the text to append
    returns the number of characters
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
