#!/usr/bin/python3
"""
function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    filename is the file to open
    text is the text to write
    return the number of characters
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        return len(text)
